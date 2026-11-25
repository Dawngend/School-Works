"""Check the 100-card cut against HEAD and its saved original 200-card deck.

Coding is manually classified in the selection manifest, not guessed from
keywords. Module attribution is independently checked against final_M1-M6.
Git stores LF while Windows may check out CRLF; comparisons with HEAD ignore
only that transport difference. Every byte outside the cards value must match.
"""

import json
import subprocess
import sys
from collections import Counter

sys.dont_write_bytecode = True
from modsim_deck100_build import (
    HERE, ORIGINAL, PAYLOAD, ROOT, SELECTION, cards_span, field_span,
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check():
    head_bytes = subprocess.check_output(
        ["git", "show", "HEAD:AndyHub Export/payload_modsim_final.json"], cwd=ROOT,
    )
    head = json.loads(head_bytes)
    text = PAYLOAD.read_bytes().decode("utf-8")
    payload = json.loads(text)
    original = json.loads(ORIGINAL.read_bytes())
    selection = json.loads(SELECTION.read_bytes())
    require(len(original["cards"]) == 200, "Original deck must contain 200 cards")
    require(original == head["decks"][0], "Saved original deck differs from HEAD")
    cards = payload["decks"][0]["cards"]
    require(len(cards) == 100, "Deck must contain exactly 100 cards")
    require(len(selection) == 100, "Selection must contain exactly 100 entries")
    questions = [card["question"] for card in cards]
    require(len({" ".join(q.casefold().split()) for q in questions}) == 100,
            "Duplicate questions")
    require(questions == [item["question"] for item in selection],
            "Deck questions or ordering differ from selection")
    originals = {card["question"]: card for card in original["cards"]}
    for card in cards:
        question = card["question"]
        require(card == originals.get(question), f"Card changed or added: {question}")
        require(card["type"] == "multiple_choice", f"Wrong type: {question}")
        options = json.loads(card["options"])
        require(isinstance(options, list) and len(options) == 4
                and all(isinstance(option, str) and option.strip() for option in options),
                f"Expected four nonempty text options: {question}")
        require(len({" ".join(option.casefold().split()) for option in options}) == 4,
                f"Duplicate options: {question}")
        require(options.count(card["correct_answer"]) == 1,
                f"Answer must match exactly one option: {question}")

    modules = {}
    for number in range(1, 7):
        module = f"M{number}"
        source = json.loads((HERE / f"final_{module}.json").read_bytes())
        modules[module] = {card["question"] for card in source["cards"]}
    for item in selection:
        module = item["module"]
        require(module in modules and item["question"] in modules[module],
                f"Incorrect module attribution: {item['question']}")
        require(type(item["coding"]) is bool, "Coding classification must be Boolean")
        require(isinstance(item["reason"], str) and bool(item["reason"].strip())
                and len(item["reason"].splitlines()) == 1,
                f"Expected a one-line selection reason: {item['question']}")
    counts = Counter(item["module"] for item in selection)
    require(all(counts[module] >= 10 for module in modules),
            "Each of M1-M6 must have at least 10 cards")
    coding_count = sum(item["coding"] for item in selection)
    require(coding_count >= 30, "At least 30 coding cards required")

    head_text = head_bytes.decode("utf-8").replace("\r\n", "\n")
    current_text = text.replace("\r\n", "\n")
    old_start, old_end = cards_span(head_text)
    new_start, new_end = cards_span(current_text)
    require(head_text[:old_start] == current_text[:new_start]
            and head_text[old_end:] == current_text[new_end:],
            "Payload bytes outside decks[0].cards changed (ignoring checkout CRLF)")
    old_start, old_end = field_span(head_text, "notes")
    new_start, new_end = field_span(current_text, "notes")
    require(head_text[old_start:old_end] == current_text[new_start:new_end]
            and payload["notes"] == head["notes"], "Reviewer notes changed")
    for path in (ORIGINAL, SELECTION, HERE / "modsim_deck100_build.py",
                 HERE / "modsim_deck100_check.py"):
        require("\u2014" not in path.read_bytes().decode("utf-8"),
                f"Em dash found in new file: {path.name}")
    print("PASS: exactly 100 unchanged original multiple-choice cards")
    print("Cards per module: " + ", ".join(f"{m}={counts[m]}" for m in modules))
    print(f"Coding cards: {coding_count}; reviewer and deck metadata unchanged")


if __name__ == "__main__":
    try:
        check()
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
