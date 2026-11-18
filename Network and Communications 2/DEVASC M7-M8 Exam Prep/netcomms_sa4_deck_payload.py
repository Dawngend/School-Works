"""Write the deck-only AndyHub payload (80 cards) used to replace the production deck."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, r"D:\Personal Projects\All In One Reviewer")

from netcomms_sa4_build import build_deck, check_cards

EXPORT = os.path.join(os.path.dirname(os.path.dirname(HERE)), "AndyHub Export")

print("cards ok:", check_cards())
deck = build_deck()
path = os.path.join(EXPORT, "payload_netcomms_sa4_deck.json")
with open(path, "w", encoding="utf-8") as fh:
    json.dump({"notes": [], "decks": [deck]}, fh, indent=1, ensure_ascii=False)
print("deck", deck["name"], len(deck["cards"]), "->", path)
