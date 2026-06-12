import os
import json
import re
import sys
from google import genai
from google.genai import types

from extractor import process_module_file
from database import create_deck, add_card

# ── Constants & Configuration ────────────────────────────────────────────────

# MODEL CHOICES: 
# Set to "gemini-3.5-flash" for rapid, standard generation
# Set to "gemini-3.1-pro" for ultra-complex reasoning or massive files
MODEL_NAME = "gemini-3.5-flash"

MAX_CHUNK_CHARS = 12_000

SYSTEM_PROMPT = (
    "You are an elite Computer Science professor writing a tricky "
    "application-based exam. Analyze the provided module text. Instead of "
    "asking for basic definitions, generate practical, conceptual, and "
    "scenario-based questions. Output a strictly formatted JSON array where "
    'each object has: "type" (must be "multiple_choice"), "question" '
    '(string), "options" (array of exactly 4 strings), and '
    '"correct_answer" (string matching one option exactly).'
)

# ── Gemini client ─────────────────────────────────────────────────────────────

def _get_client() -> genai.Client:
    """
    Create and return an authenticated Gemini client.
    Checks environment variables first, then falls back to Streamlit secrets.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # Fallback to loading Streamlit secrets if running locally
    if not api_key:
        try:
            import tomllib  # Built-in in Python 3.11+
            secrets_path = os.path.join(".streamlit", "secrets.toml")
            if os.path.exists(secrets_path):
                with open(secrets_path, "rb") as f:
                    secrets = tomllib.load(f)
                    api_key = secrets.get("GEMINI_API_KEY")
        except Exception:
            pass # Fall through to the error raise below

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY not found in environment variables or .streamlit/secrets.toml. "
            "Please ensure your key is configured."
        )
    
    # Clean up any accidental whitespaces or quotes added by Git Bash exports
    api_key = api_key.strip().strip('"').strip("'")
    
    return genai.Client(api_key=api_key)


# ── Text helpers ──────────────────────────────────────────────────────────────

def _chunk_text(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    """
    Split *text* into chunks of at most *max_chars* characters, breaking only
    on paragraph boundaries so that context is never cut mid-sentence.
    """
    if len(text) <= max_chars:
        return [text]

    chunks: list[str] = []
    paragraphs = text.split("\n\n")
    current_chunk = ""

    for paragraph in paragraphs:
        # A single paragraph that is itself too long gets hard-split.
        if len(paragraph) > max_chars:
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = ""
            for i in range(0, len(paragraph), max_chars):
                chunks.append(paragraph[i : i + max_chars])
            continue

        if len(current_chunk) + len(paragraph) + 2 > max_chars:
            chunks.append(current_chunk.strip())
            current_chunk = paragraph
        else:
            current_chunk = (current_chunk + "\n\n" + paragraph).lstrip("\n")

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


def _strip_json_fences(raw: str) -> str:
    """
    Gemini sometimes wraps its JSON output in markdown code fences.
    Strip them so json.loads never fails due to stray backticks.
    """
    # Using [`]{3} to match triple backticks safely without breaking parsers!
    pattern = r"[`]{3}(?:json)?\s*([\s\S]*?)[`]{3}"
    match = re.search(pattern, raw)
    if match:
        return match.group(1).strip()
    return raw.strip()


# ── LLM interaction ───────────────────────────────────────────────────────────

def _query_gemini(client: genai.Client, text_chunk: str) -> list[dict]:
    """
    Send a single *text_chunk* to Gemini and return the parsed list of
    question dicts.  Returns an empty list on any error so the caller can
    continue processing the remaining chunks.
    """
    prompt = (
        "Generate exam questions based ONLY on the following module content:\n\n"
        f"{text_chunk}"
    )

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                # Instruct the API to return clean JSON without extra prose
                response_mime_type="application/json",
                temperature=0.7,
            ),
            contents=prompt,
        )

        raw_text = response.text
        cleaned = _strip_json_fences(raw_text)
        questions = json.loads(cleaned)

        if not isinstance(questions, list):
            print("  [Warning] Gemini returned JSON but it is not a list — skipping chunk.")
            return []

        return questions

    except json.JSONDecodeError as e:
        print(f"  [Warning] JSON parse error: {e}. Raw response saved to 'gemini_raw_error.txt'.")
        with open("gemini_raw_error.txt", "w", encoding="utf-8") as f:
            f.write(raw_text if 'raw_text' in locals() else "No response text")
        return []
    except Exception as e:
        print(f"  [Error] Gemini request failed using {MODEL_NAME}: {e}")
        return []


# ── Card validation ───────────────────────────────────────────────────────────

def _validate_card(card: dict, index: int) -> bool:
    """
    Return True only if *card* has every required field in the correct shape.
    Logs a descriptive warning and returns False for every malformed entry.
    """
    required_keys = {"type", "question", "options", "correct_answer"}

    if not isinstance(card, dict):
        print(f"  [Skipped] Card #{index}: not a dict.")
        return False

    missing = required_keys - card.keys()
    if missing:
        print(f"  [Skipped] Card #{index}: missing keys {missing}.")
        return False

    if card.get("type") != "multiple_choice":
        print(f"  [Skipped] Card #{index}: type is '{card.get('type')}', expected 'multiple_choice'.")
        return False

    options = card.get("options")
    if not isinstance(options, list) or len(options) != 4:
        print(f"  [Skipped] Card #{index}: 'options' must be a list of exactly 4 strings.")
        return False

    if not all(isinstance(opt, str) for opt in options):
        print(f"  [Skipped] Card #{index}: every option must be a string.")
        return False

    if card.get("correct_answer") not in options:
        print(
            f"  [Skipped] Card #{index}: 'correct_answer' does not match any option.\n"
            f"    correct_answer : {card.get('correct_answer')}\n"
            f"    options        : {options}"
        )
        return False

    return True


# ── Core public function ──────────────────────────────────────────────────────

def generate_deck_from_file(
    file_path: str,
    deck_name: str,
    subject: str,
) -> int | None:
    """
    Full pipeline:
      1. Extract text from *file_path* (PDF or PPTX) via extractor.py.
      2. Chunk the text and query Gemini once per chunk.
      3. Validate every returned card.
      4. Persist the deck and all valid cards to SQLite via database.py.
    """

    # ── Step 1 · Extract text ────────────────────────────────────────────────
    print(f"\n[1/4] Extracting text from: {file_path}")
    raw_text = process_module_file(file_path)

    if raw_text.startswith("Error") or raw_text.startswith("Unsupported"):
        print(f"  [Abort] Extraction failed: {raw_text}")
        return None

    text_length = len(raw_text)
    print(f"  Extracted {text_length:,} characters.")

    if text_length < 50:
        print("  [Abort] Extracted text is too short to generate meaningful questions.")
        return None

    # ── Step 2 · Chunk ───────────────────────────────────────────────────────
    chunks = _chunk_text(raw_text)
    print(f"\n[2/4] Split into {len(chunks)} chunk(s) (max {MAX_CHUNK_CHARS:,} chars each).")

    # ── Step 3 · Query Gemini ────────────────────────────────────────────────
    print(f"\n[3/4] Querying Gemini using '{MODEL_NAME}' ({len(chunks)} request(s))...")
    client = _get_client()

    all_raw_cards: list[dict] = []
    for i, chunk in enumerate(chunks, start=1):
        print(f"  Chunk {i}/{len(chunks)} ({len(chunk):,} chars) ...", end=" ", flush=True)
        cards = _query_gemini(client, chunk)
        print(f"received {len(cards)} card(s).")
        all_raw_cards.extend(cards)

    print(f"  Total raw cards received: {len(all_raw_cards)}")

    # ── Step 4 · Validate & save ─────────────────────────────────────────────
    print(f"\n[4/4] Validating and saving to database...")
    module_filename = os.path.basename(file_path)

    valid_cards = [
        card for i, card in enumerate(all_raw_cards, start=1)
        if _validate_card(card, i)
    ]

    if not valid_cards:
        print("  [Abort] No valid cards were generated. Deck will not be created.")
        return None

    deck_id = create_deck(
        name=deck_name,
        modules_included=module_filename,
        subject=subject,
    )

    for card in valid_cards:
        add_card(
            deck_id=deck_id,
            card_type=card["type"],
            question=card["question"],
            correct_answer=card["correct_answer"],
            options=card["options"],
        )

    print(f"\n  Deck '{deck_name}' created successfully.")
    print(f"  Deck ID       : {deck_id}")
    print(f"  Cards saved   : {len(valid_cards)}")
    print(f"  Cards skipped : {len(all_raw_cards) - len(valid_cards)}")

    return deck_id


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Usage (default hardcoded values):
    #   python generator.py
    #
    # Usage (pass everything via CLI — no code edits needed):
    #   python generator.py "path/to/module.pdf" "Deck Name" "Subject"

    if len(sys.argv) == 4:
        TEST_FILE    = sys.argv[1]
        TEST_DECK    = sys.argv[2]
        TEST_SUBJECT = sys.argv[3]
    elif len(sys.argv) == 1:
        # ── Default test values ──────────────────────────────────────────────
        # Edit these three lines to point to a real file before running.
        TEST_FILE    = "sample_module.pdf"   # supports .pdf and .pptx
        TEST_DECK    = "Sample CS Deck"
        TEST_SUBJECT = "Computer Science"
    else:
        print("Usage: python generator.py [<file_path> <deck_name> <subject>]")
        sys.exit(1)

    if not os.path.isfile(TEST_FILE):
        print(f"[Error] File not found: '{TEST_FILE}'")
        print("Please set TEST_FILE to the path of a real PDF or PPTX file.")
        sys.exit(1)

    deck_id = generate_deck_from_file(
        file_path=TEST_FILE,
        deck_name=TEST_DECK,
        subject=TEST_SUBJECT,
    )

    if deck_id is not None:
        print(f"\n[Done] Deck ID {deck_id} is ready to use in the quiz app.")
    else:
        print("\n[Done] No deck was created.")