"""Merge the three ML verified decks into one deck per exam (Dawn, 2026-10-07).

Summative 1 = Module 1 plus Module 2 up to Linear Regression. Midterm = all of Modules 1 and 2.
Picture-slide cards are mixed in. Writes ml_exam_decks.json for AndyHub Export/import_decks_vm.py.
"""
import json
import random
from pathlib import Path

from ml_cards import DECK, MOCK
from ml_picture_cards import PICTURE

HERE = Path(__file__).parent
SUBJECT = "Machine Learning Algorithm"
# Topics taught after Linear Regression, so outside Summative 1.
AFTER_LINEAR = ("Ridge", "Lasso", "Logistic", "LinearSVC", "Decision Tree", "Random Forest", "Gradient Boosting",
                "SVM", "Formative Q13", "Formative Q15", "Formative Q16")


def unique(cards):
    seen, out = set(), []
    for card in cards:
        if card[0] not in seen:
            seen.add(card[0])
            out.append(card)
    return out


def to_card(card, rng):
    question, answer, wrong, _tag = card
    options = [answer, *wrong]
    rng.shuffle(options)
    return {"type": "multiple_choice", "question": question, "correct_answer": answer,
            "options": json.dumps(options, ensure_ascii=False), "times_missed": 0}


def deck(name, modules, cards):
    rng = random.Random(name)
    return {"name": name, "subject": SUBJECT, "modules_included": modules, "module_ids": None,
            "cards": [to_card(c, rng) for c in cards]}


def main():
    every = unique(DECK + MOCK + PICTURE)
    summative = [c for c in every if not any(word in c[3] for word in AFTER_LINEAR)]
    decks = [
        deck("ML_Summative1_Verified", "Module 1 and Module 2 up to Linear Regression", summative),
        deck("ML_Midterm_Verified", "Modules 1 and 2", every),
    ]
    for d in decks:
        print(d["name"], len(d["cards"]), "cards")
    (HERE / "ml_exam_decks.json").write_text(json.dumps(decks, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
