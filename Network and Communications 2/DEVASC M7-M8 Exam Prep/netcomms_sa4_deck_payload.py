"""Write the full AndyHub payload (note and the 80-card deck) used to replace both on production."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "DEVASC M3-M4 Exam Prep"))
sys.path.insert(0, r"D:\School-Works\Software Engineering 1\SE1 Exam Prep")
sys.path.insert(0, r"D:\Personal Projects\All In One Reviewer")

from netcomms_sa4_build import build_deck, build_docx, build_note, check_cards

EXPORT = os.path.join(os.path.dirname(os.path.dirname(HERE)), "AndyHub Export")

print("cards ok:", check_cards())
payload = {"notes": [build_note()], "decks": [build_deck()]}
path = os.path.join(EXPORT, "payload_netcomms_sa4_deck.json")
with open(path, "w", encoding="utf-8") as fh:
    json.dump(payload, fh, indent=1, ensure_ascii=False)
print("note sections", len(payload["notes"][0]["content"]["sections"]), "cards", len(payload["decks"][0]["cards"]), "->", path)
print("pdf", build_docx())
