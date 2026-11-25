"""Check the cut against the pinned pre-cut commit, including after committing.

Coding is manually classified in the selection manifest, not guessed from
keywords. Module attribution is independently checked against final_M1-M6.
Git stores LF while Windows may check out CRLF; baseline comparisons ignore
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

BASELINE_COMMIT = "506fc2529d5a8ae2c1fc77c0ba9a318ef80686ef"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_original(original, baseline):
    missing = sorted(baseline.keys() - original.keys())
    extra = sorted(original.keys() - baseline.keys())
    require(not missing and not extra,
            f"Saved original deck keys differ: missing={missing}, extra={extra}")
    for key in baseline.keys() - {"cards"}:
        require(original[key] == baseline[key],
                f"Saved original deck field differs: {key}")
    require(len(original["cards"]) == len(baseline["cards"]),
            "Saved original card count differs from baseline")
    for index, (saved, expected) in enumerate(zip(original["cards"], baseline["cards"]), 1):
        fields = sorted(key for key in saved.keys() | expected.keys()
                        if key not in saved or key not in expected
                        or saved[key] != expected[key])
        require(not fields,
                f"Saved original card {index} differs in {fields}: {expected['question']}")


def check():
    baseline_bytes = subprocess.check_output(
        ["git", "show", f"{BASELINE_COMMIT}:AndyHub Export/payload_modsim_final.json"],
        cwd=ROOT,
    )
    baseline = json.loads(baseline_bytes)
    text = PAYLOAD.read_bytes().decode("utf-8")
    payload = json.loads(text)
    original = json.loads(ORIGINAL.read_bytes())
    selection = json.loads(SELECTION.read_bytes())
    require(len(original["cards"]) == 200, "Original deck must contain 200 cards")
    check_original(original, baseline["decks"][0])
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

    baseline_text = baseline_bytes.decode("utf-8").replace("\r\n", "\n")
    current_text = text.replace("\r\n", "\n")
    old_start, old_end = cards_span(baseline_text)
    new_start, new_end = cards_span(current_text)
    require(baseline_text[:old_start] == current_text[:new_start]
            and baseline_text[old_end:] == current_text[new_end:],
            "Payload bytes outside decks[0].cards changed (ignoring checkout CRLF)")
    old_start, old_end = field_span(baseline_text, "notes")
    new_start, new_end = field_span(current_text, "notes")
    require(baseline_text[old_start:old_end] == current_text[new_start:new_end]
            and payload["notes"] == baseline["notes"], "Reviewer notes changed")
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
