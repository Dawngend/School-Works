"""Apply the reviewed 100-question selection without rewriting the reviewer.

Run this file, then modsim_deck100_check.py. The selection JSON documents module,
manual coding classification, and the exam value of each retained question.
History, product trivia, repeated definitions, and special-case examples lose
priority to reviewer traps, general formulas, and MATLAB/Simulink practice.
The original 200-card deck was captured from git show HEAD before this cut.
"""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
PAYLOAD = ROOT / "AndyHub Export" / "payload_modsim_final.json"
ORIGINAL = HERE / "modsim_deck200_original.json"
SELECTION = HERE / "modsim_deck100_selection.json"


def field_span(text, field, start=0):
    """Locate an object field's JSON value, preserving surrounding whitespace."""
    decoder = json.JSONDecoder()
    position = start + 1
    while True:
        while text[position].isspace() or text[position] == ",":
            position += 1
        if text[position] == "}":
            raise ValueError(f"Missing JSON field: {field}")
        key, position = decoder.raw_decode(text, position)
        while text[position].isspace():
            position += 1
        if text[position] != ":":
            raise ValueError("Expected a JSON field separator")
        position += 1
        while text[position].isspace():
            position += 1
        value_start = position
        _, position = decoder.raw_decode(text, position)
        if key == field:
            return value_start, position


def cards_span(text):
    start, _ = field_span(text, "decks")
    position = start + 1
    while text[position].isspace():
        position += 1
    return field_span(text, "cards", position)


def build():
    original = json.loads(ORIGINAL.read_bytes())
    selection = json.loads(SELECTION.read_bytes())
    questions = [item["question"] for item in selection]
    if len(questions) != 100 or len(set(questions)) != 100:
        raise ValueError("Selection must contain exactly 100 unique questions")
    by_question = {card["question"]: card for card in original["cards"]}
    cards = [by_question[question] for question in questions]
    text = PAYLOAD.read_bytes().decode("utf-8")
    start, end = cards_span(text)
    newline = "\r\n" if "\r\n" in text else "\n"
    replacement = json.dumps(cards, ensure_ascii=False, indent=2).replace("\n", newline)
    PAYLOAD.write_bytes((text[:start] + replacement + text[end:]).encode("utf-8"))
    print(f"Selected {len(cards)} original cards; only decks[0].cards replaced.")


if __name__ == "__main__":
    build()
