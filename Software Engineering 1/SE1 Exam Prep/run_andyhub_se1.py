import json
import os
import sys

HUB = r"D:\Personal Projects\All In One Reviewer"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HUB)
os.chdir(HUB)

import database
import generator

D = r"C:\Users\Dawn\Downloads"
RUNS = [
    ("SE1 Module 3 Agile Methodologies", [f"{D}\\CS0025-M3S1.pdf", f"{D}\\CS0025-M3S2.pdf"]),
    ("SE1 Module 4 System Models and Requirements", [f"{D}\\CS0025-M4S1.pdf", f"{D}\\CS0025-M4S2.pdf"]),
]
database.init_db()
out = {}
for name, paths in RUNS:
    deck_id = generator.generate_custom_deck(paths, name, "Software Engineering 1", 40, "multiple_choice")
    cards = database.get_cards_for_deck(deck_id) if deck_id else []
    out[name] = {"deck_id": deck_id, "cards": [list(c) for c in cards]}
with open(os.path.join(HERE, "andyhub_se1_decks.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1, default=str)
print("DONE", {k: (v["deck_id"], len(v["cards"])) for k, v in out.items()})
