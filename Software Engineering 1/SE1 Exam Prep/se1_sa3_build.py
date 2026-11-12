"""Build the SE1 Summative 3 reviewer (DOCX + PDF) and the AndyHub payload (one note and one deck).

Run from this folder: python se1_sa3_build.py
"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCHOOL = os.path.dirname(HERE)
EXPORT = os.path.join(os.path.dirname(SCHOOL), "AndyHub Export")
sys.path.insert(0, HERE)
sys.path.insert(0, r"D:\School-Works\Network and Communications 2\DEVASC M3-M4 Exam Prep")
sys.path.insert(0, r"D:\Personal Projects\All In One Reviewer")

from notes_lib import Notes
from notes_to_andyhub import Rec
from notes_to_andyhub_v2 import convert_v2
from andyhub_api.schemas import NoteContent
from se1_sa3_notes import sa3
from se1_sa3_cards import CARDS

TITLE = "SE1 Summative 3 Reviewer: Modules 5, 6 and 7"
SUBTITLE = ("CS0025 Software Engineering 1. Study notes for Module 5 (OOAD, Procedural Programming, Methodologies), "
            "Module 6 (Development Strategies, UML), and Module 7 (Strategic Trends). The blue boxes are memory aids I made; "
            "they are not from the slides.")
SUBJECT = "Software Engineering 1"
SOURCES = ["CS0025-M5S1", "CS0025-M5S2", "CS0025-M5S3", "CS0025-M6S0", "CS0025-M6S1", "CS0025-M6S2", "CS0025-M7S1"]


def build_docx():
    notes = Notes(TITLE, SUBTITLE)
    sa3(notes)
    return notes.save(os.path.join(SCHOOL, "PAMESA - SE1 Summative 3 Reviewer.docx"))


def build_note():
    rec = Rec(TITLE, SUBTITLE)
    sa3(rec)
    sections, cram = convert_v2(rec.ops, SOURCES)
    content = NoteContent.model_validate({"sections": sections, "formula_sheet": [], "self_check": [], "cram_sheet": cram})
    return {"title": "SE1 Summative 3 Reviewer", "subject": SUBJECT, "module_ids": [],
            "content": content.model_dump(mode="json")}


def build_deck():
    rnd = random.Random(7)
    cards = []
    for question, correct, wrong in CARDS:
        options = [correct] + wrong
        rnd.shuffle(options)
        cards.append({"type": "multiple_choice", "question": question, "correct_answer": correct,
                      "options": json.dumps(options), "times_missed": 0})
    return {"name": "SE1 Summative 3 Flashcards", "subject": SUBJECT, "modules_included": "M5, M6, M7", "cards": cards}


if __name__ == "__main__":
    payload = {"notes": [build_note()], "decks": [build_deck()]}
    with open(os.path.join(EXPORT, "payload_se1_sa3.json"), "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, ensure_ascii=False)
    print("note sections", len(payload["notes"][0]["content"]["sections"]),
          "cram rows", len(payload["notes"][0]["content"]["cram_sheet"]), "cards", len(payload["decks"][0]["cards"]))
    print("pdf", build_docx())
