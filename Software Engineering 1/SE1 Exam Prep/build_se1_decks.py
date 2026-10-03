import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HUB = r"D:\Personal Projects\All In One Reviewer"
sys.path.insert(0, HERE)
sys.path.insert(0, HUB)
from se1_cards import KEEP_M3_IDX, KEEP_M4_IDX, M3_NEW, M4_NEW

raw = json.load(open(os.path.join(HERE, "andyhub_se1_decks.json"), encoding="utf-8"))
m3_raw = raw["SE1 Module 3 Agile Methodologies"]["cards"]
m4_raw = raw["SE1 Module 4 System Models and Requirements"]["cards"]


def kept(cards, idx):
    out = []
    for i in idx:
        c = cards[i]
        opts = json.loads(c[5])
        out.append((c[3], c[4], [o for o in opts if o != c[4]], "Scenario question; matches the slides"))
    return out


os.chdir(HUB)
import database
from repositories import NewCard

database.init_db()


def make_deck(name, modules, cards):
    r = random.Random(7)
    new = []
    for q, correct, wrong, _ in cards:
        opts = [correct] + list(wrong)
        assert len(opts) == 4 and len(set(opts)) == 4, q
        r.shuffle(opts)
        new.append(NewCard("multiple_choice", q, correct, opts))
    return database.create_deck_with_cards(name, modules, "Software Engineering 1", new)


m3 = M3_NEW + kept(m3_raw, KEEP_M3_IDX)
m4 = M4_NEW + kept(m4_raw, KEEP_M4_IDX)
a = make_deck("SE1 Module 3 (Verified)", "CS0025-M3S1.pdf, CS0025-M3S2.pdf", m3)
b = make_deck("SE1 Module 4 (Verified)", "CS0025-M4S1.pdf, CS0025-M4S2.pdf", m4)
print("deck ids", a, b, "counts", len(m3), len(m4))
