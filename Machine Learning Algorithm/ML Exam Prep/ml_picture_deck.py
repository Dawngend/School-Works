"""Create the picture-slides deck in the local AndyHub DB and export all three ML decks for the VM import."""
import json
import os
import random
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HUB = r"D:\Personal Projects\All In One Reviewer"
sys.path.insert(0, HERE)
sys.path.insert(0, HUB)
from ml_picture_cards import PICTURE

os.chdir(HUB)
import database
from repositories import NewCard

database.init_db()
r = random.Random(7)
cards = []
for q, correct, wrong, _ in PICTURE:
    opts = [correct] + list(wrong)
    r.shuffle(opts)
    cards.append(NewCard("multiple_choice", q, correct, opts))
deck_id = database.create_deck_with_cards("ML Picture Slides (Verified)", "M1-MAIN-1.pdf, M2 - Supervised Learning - Main.pdf",
                                          "Machine Learning Algorithm", cards)
print("new deck id", deck_id)

con = sqlite3.connect(database.DB_PATH if hasattr(database, "DB_PATH") else "Database/reviewer.db")
con.row_factory = sqlite3.Row
out = []
for row in con.execute("select * from decks where subject = 'Machine Learning Algorithm' order by id"):
    d = dict(row)
    d["cards"] = [dict(c) for c in con.execute("select * from cards where deck_id=?", (d["id"],))]
    print(d["id"], d["name"], len(d["cards"]))
    out.append(d)
with open(r"C:\Users\Dawn\AppData\Local\Temp\claude-out\ml_decks_export.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1, default=str)
