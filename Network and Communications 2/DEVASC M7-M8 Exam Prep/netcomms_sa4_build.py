"""Build the NetComms 2 Summative 4 reviewer (DOCX + PDF) and the AndyHub payload (one note, one deck).

Run: python netcomms_sa4_build.py
"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCHOOL = os.path.dirname(HERE)
EXPORT = os.path.join(os.path.dirname(SCHOOL), "AndyHub Export")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(SCHOOL, "DEVASC M3-M4 Exam Prep"))
sys.path.insert(0, r"D:\School-Works\Software Engineering 1\SE1 Exam Prep")
sys.path.insert(0, r"D:\Personal Projects\All In One Reviewer")

from notes_lib import Notes
from notes_to_andyhub import Rec
from notes_to_andyhub_v2 import convert_v2
from andyhub_api.schemas import NoteContent
from netcomms_sa4_notes import sa4
from netcomms_sa4_cards import CARDS
from netcomms_sa4_bankcards import bank_cards

TITLE = "NetComms 2 Summative 4 Reviewer: Modules 7 and 8"
SUBTITLE = ("CS0016 Network and Communications 2 (DevNet Associate). Study notes for Module 7 (Infrastructure and "
            "Automation) and Module 8 (Cisco Platforms and Development), built from DEVASC_Module_7 and DEVASC_Module_8. "
            "The blue boxes are memory aids I made; they are not from the slides.")
SUBJECT = "Network and Communications 2"
SOURCES = ["DEVASC_Module_7", "DEVASC_Module_8"]


def deck_cards():
    """The 52 literal bank questions first (they rank highest), then 28 slide-based cards to make 80."""
    bank = bank_cards()
    seen = {q for q, _, _ in bank}
    extra = [c for c in CARDS[::3] + CARDS[1:2] if c[0] not in seen][:80 - len(bank)]
    return bank + extra


def check_cards():
    seen = set()
    cards = deck_cards()
    for q, correct, wrong in cards:
        assert len(wrong) == 3, q
        assert len({correct, *wrong}) == 4, ("duplicate option", q)
        assert q not in seen, ("duplicate question", q)
        seen.add(q)
    return len(cards)


def build_docx():
    notes = Notes(TITLE, SUBTITLE)
    sa4(notes)
    return notes.save(os.path.join(SCHOOL, "PAMESA - NetComms 2 Summative 4 Reviewer.docx"))


def build_note():
    rec = Rec(TITLE, SUBTITLE)
    sa4(rec)
    sections, cram = convert_v2(rec.ops, SOURCES)
    content = NoteContent.model_validate({"sections": sections, "formula_sheet": [], "self_check": [], "cram_sheet": cram})
    return {"title": "NetComms 2 Summative 4 Reviewer", "subject": SUBJECT, "module_ids": [],
            "content": content.model_dump(mode="json")}


def build_deck():
    rnd = random.Random(11)
    cards = []
    for question, correct, wrong in deck_cards():
        options = [correct] + wrong
        rnd.shuffle(options)
        cards.append({"type": "multiple_choice", "question": question, "correct_answer": correct,
                      "options": json.dumps(options), "times_missed": 0})
    return {"name": "NetComms 2 Summative 4 Flashcards", "subject": SUBJECT, "modules_included": "M7, M8", "cards": cards}


if __name__ == "__main__":
    print("cards ok:", check_cards())
    payload = {"notes": [build_note()], "decks": [build_deck()]}
    with open(os.path.join(EXPORT, "payload_netcomms_sa4.json"), "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, ensure_ascii=False)
    note = payload["notes"][0]["content"]
    print("note sections", len(note["sections"]), "cram rows", len(note["cram_sheet"]), "cards", len(payload["decks"][0]["cards"]))
    print("pdf", build_docx())
