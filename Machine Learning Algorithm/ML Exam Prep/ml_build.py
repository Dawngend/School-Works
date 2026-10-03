import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUBJECT_DIR = os.path.dirname(HERE)
HUB = r"D:\Personal Projects\All In One Reviewer"
sys.path.insert(0, HERE)

from build_lib import Q, build, to_pdf
from ml_cards import DECK, MOCK

path = os.path.join(SUBJECT_DIR, "PAMESA - ML Midterm Mock Exam.docx")
n, key = build(
    path,
    "Machine Learning Mock Exam: Modules 1 and 2",
    "30 choice items built from the Module 1 and Module 2 slides. Answer key at the end.",
    [("Multiple Choice", [Q(*c) for c in MOCK])],
    seed=31,
)
print("mock items:", n, "->", os.path.basename(to_pdf(path)))

if os.environ.get("SKIP_DB"):
    sys.exit(0)

os.chdir(HUB)
sys.path.insert(0, HUB)
import database
from repositories import NewCard

database.init_db()


def make_deck(name, cards):
    r = random.Random(5)
    new = []
    for q, correct, wrong, _ in cards:
        opts = [correct] + list(wrong)
        r.shuffle(opts)
        new.append(NewCard("multiple_choice", q, correct, opts))
    return database.create_deck_with_cards(name, "M1-MAIN-1.pdf, M2 - Supervised Learning - Main.pdf",
                                           "Machine Learning Algorithm", new)


ids = {
    "deck": make_deck("ML Modules 1 and 2 (Verified)", DECK),
    "mock": make_deck("ML Midterm Mock Exam (Verified)", MOCK),
}
print("deck ids", ids)

with open(os.path.join(HERE, "andyhub_ml_verified.json"), "w", encoding="utf-8") as fh:
    json.dump({"deck": DECK, "mock": MOCK}, fh, indent=1)
