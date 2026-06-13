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
# "gemini-2.0-flash" for rapid, standard generation
# "gemini-1.5-pro" for ultra-complex reasoning
MODEL_NAME = "gemini-2.0-flash"

MAX_CHUNK_CHARS = 12_000

# ── Andy Persona Prompt ──────────────────────────────────────────────────────

def get_andy_prompt(target_count: int) -> str:
    """
    Dynamically generates the system prompt for Andy, enforcing the required
    question count and the situational/scenario-based rule.
    """
    return (
        f"You are Andy, a brilliant, friendly, and rigorous Computer Science study buddy. "
        f"Your goal is to help the user ace their exams. Analyze the provided module text. "
        f"Generate exactly {target_count} multiple-choice flashcards. "
        f"CRITICAL: Do not just ask for basic vocabulary definitions. The questions MUST be "
        f"highly situational, scenario-based applications of the concepts. Make them think! "
        f"Output a strictly formatted JSON array where each object has: "
        f'"type" (must be "multiple_choice"), "question" (string), '
        f'"options" (array of exactly 4 strings), and "correct_answer" (string matching one option exactly).'
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
            pass 

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
    Split text into chunks, breaking on paragraph boundaries.
    """
    if len(text) <= max_chars:
        return [text]

    chunks: list[str] = []
    paragraphs = text.split("\n\n")
    current_chunk = ""

    for paragraph in paragraphs:
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
    Strip markdown code fences so json.loads never fails due to stray backticks.
    """
    pattern = r"[`]{3}(?:json)?\s*([\s\S]*?)[`]{3}"
    match = re.search(pattern, raw)
    if match:
        return match.group(1).strip()
    return raw.strip()


# ── LLM interaction ───────────────────────────────────────────────────────────

def _query_gemini(client: genai.Client, text_chunk: str, system_prompt: str) -> list[dict]:
    """
    Send a chunk to Gemini with the dynamic system prompt.
    """
    prompt = (
        "Generate exam questions based ONLY on the following module content:\n\n"
        f"{text_chunk}"
    )

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
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

def generate_custom_deck(
    selected_files: list[str], 
    deck_name: str, 
    subject: str, 
    total_questions: int
) -> int | None:
    """
    Full pipeline to handle multiple files, specific question counts, and
    save the validated cards into the database.
    """
    print(f"\n[1/4] Processing {len(selected_files)} module(s)...")
    combined_text = ""
    
    # Combine text from all selected files
    for filename in selected_files:
        # Check 'uploads' folder first, fallback to current directory for local testing
        file_path = os.path.join("uploads", filename)
        if not os.path.exists(file_path) and os.path.exists(filename):
            file_path = filename

        text = process_module_file(file_path)
        if not text.startswith("Error") and not text.startswith("Unsupported"):
            combined_text += f"\n\n--- Content from {filename} ---\n\n" + text
        else:
            print(f"  [Warning] Skipping {filename}: {text}")

    text_length = len(combined_text)
    print(f"  Extracted {text_length:,} characters from all selected modules.")

    if text_length < 50:
        print("  [Abort] Not enough valid text extracted to generate meaningful questions.")
        return None

    # Chunking
    chunks = _chunk_text(combined_text)
    print(f"\n[2/4] Split into {len(chunks)} chunk(s) (max {MAX_CHUNK_CHARS:,} chars each).")
    
    # Math: Distribute the total requested questions evenly across text chunks
    questions_per_chunk = max(1, total_questions // len(chunks))
    
    # Query Gemini
    print(f"\n[3/4] Andy is generating {total_questions} situational questions using '{MODEL_NAME}'...")
    client = _get_client()
    all_raw_cards: list[dict] = []
    
    for i, chunk in enumerate(chunks, start=1):
        print(f"  Chunk {i}/{len(chunks)} ...", end=" ", flush=True)
        # Dynamically inject the target question count and persona into the prompt
        prompt = get_andy_prompt(questions_per_chunk) 
        cards = _query_gemini(client, chunk, system_prompt=prompt) 
        print(f"received {len(cards)} card(s).")
        all_raw_cards.extend(cards)

    # Trim the list if Gemini returned slightly more than the exact requested total
    all_raw_cards = all_raw_cards[:total_questions]
    print(f"  Total raw cards finalized for validation: {len(all_raw_cards)}")

    # Validation & Saving
    print(f"\n[4/4] Validating and saving to database...")
    
    valid_cards = [
        card for i, card in enumerate(all_raw_cards, start=1)
        if _validate_card(card, i)
    ]

    if not valid_cards:
        print("  [Abort] No valid cards were generated. Deck will not be created.")
        return None

    # Save multiple filenames as a single string reference for the database
    modules_included_string = ", ".join(selected_files)

    deck_id = create_deck(
        name=deck_name,
        modules_included=modules_included_string,
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

    print(f"\n  Deck '{deck_name}' created successfully by Andy.")
    print(f"  Deck ID       : {deck_id}")
    print(f"  Cards saved   : {len(valid_cards)}")
    print(f"  Cards skipped : {len(all_raw_cards) - len(valid_cards)}")

    return deck_id


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Updated CLI entry point to handle the new function signature for testing
    if len(sys.argv) >= 5:
        TEST_FILES   = sys.argv[1:-3]       # All arguments except the last 3 are treated as files
        TEST_DECK    = sys.argv[-3]
        TEST_SUBJECT = sys.argv[-2]
        try:
            TEST_COUNT   = int(sys.argv[-1])
        except ValueError:
            print("[Error] Final argument must be an integer (total questions).")
            sys.exit(1)
    else:
        # Default fallback tests
        TEST_FILES   = ["sample_module.pdf"] 
        TEST_DECK    = "Sample Custom Deck"
        TEST_SUBJECT = "Computer Science"
        TEST_COUNT   = 5
        print(f"Usage: python generator.py <file1.pdf> [file2.pdf ...] <deck_name> <subject> <total_questions>")
        print(f"Running default test with {TEST_FILES[0]} for {TEST_COUNT} questions...\n")

    deck_id = generate_custom_deck(
        selected_files=TEST_FILES,
        deck_name=TEST_DECK,
        subject=TEST_SUBJECT,
        total_questions=TEST_COUNT
    )

    if deck_id is not None:
        print(f"\n[Done] Deck ID {deck_id} is ready to use in the quiz app.")
    else:
        print("\n[Done] No deck was created.")