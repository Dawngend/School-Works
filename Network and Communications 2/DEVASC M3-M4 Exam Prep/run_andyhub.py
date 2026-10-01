import json
import os
import sys

HUB = r"D:\Personal Projects\All In One Reviewer"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HUB)
os.chdir(HUB)

import database
import generator

database.init_db()
out = {}
for n, name in (
    (3, "DEVASC Module 3 Software Development and Design"),
    (4, "DEVASC Module 4 Understanding and Using APIs"),
):
    path = os.path.join(HERE, f"DEVASC_Module_{n}.pdf")
    deck_id = generator.generate_custom_deck(
        [path], name, "Network and Communications 2", 40, "multiple_choice"
    )
    cards = database.get_cards_for_deck(deck_id) if deck_id else []
    out[name] = {"deck_id": deck_id, "cards": [list(c) for c in cards]}

with open(os.path.join(HERE, "andyhub_decks.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1, default=str)
print("DONE", {k: (v["deck_id"], len(v["cards"])) for k, v in out.items()})
