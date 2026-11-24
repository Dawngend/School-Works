import sys
sys.dont_write_bytecode = True

import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
SCHOOL = os.path.dirname(HERE)
ROOT = os.path.dirname(SCHOOL)
EXPORT = os.path.join(ROOT, "AndyHub Export")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(SCHOOL, "DEVASC M3-M4 Exam Prep"))
sys.path.insert(0, os.path.join(ROOT, "Software Engineering 1", "SE1 Exam Prep"))
sys.path.insert(0, r"D:\Personal Projects\All In One Reviewer")

from notes_lib import Notes
from notes_to_andyhub import Rec
from notes_to_andyhub_v2 import convert_v2
from andyhub_api.schemas import NoteContent
from netcomms_final_cards import final_cards, load

TITLE = "NetComms 2 Final Reviewer"
SUBJECT = "Network and Communications 2"
INTRO = "These are the literal exam-bank questions and answers from ITExamAnswers."
DOCX = os.path.join(SCHOOL, "PAMESA - NetComms 2 Final Reviewer.docx")
PDF = os.path.splitext(DOCX)[0] + ".pdf"
PAYLOAD = os.path.join(EXPORT, "payload_netcomms_final.json")
GROUPS = [("course_final", "Course Final Exam"), ("practice_final", "Practice Final Exam")]
GROUPS += [(f"m{number}", f"Module {number}") for number in range(1, 9)]


def _row(item):
    question = item["question"]
    if item["exhibit_text"]:
        question += " " + item["exhibit_text"]
    choices = [f"{chr(65 + index)}. {choice}" for index, choice in enumerate(item["choices"])]
    answers = [choice for choice in item["choices"] if choice in item["correct"]]
    if item["explanation"]:
        answers.append(item["explanation"])
    return ["\n".join([question] + choices), "\n".join(answers)]


def final_section(n):
    items = load()
    n.h1(TITLE)
    n.p(INTRO)
    for source_page, heading in GROUPS:
        n.h2(heading)
        rows = [_row(item) for item in items if item["source_page"] == source_page]
        n.table(["Question", "Correct Answer"], rows, [3.4, 3.1])


def check_cards():
    items = load()
    cards = final_cards()
    assert len(items) == len(cards) == 200
    assert len({item["id"] for item in items}) == 200
    for item, (question, correct, wrong) in zip(items, cards):
        options = [correct] + wrong
        assert len(options) in (3, 4), item["id"]
        assert len(set(options)) == len(options), item["id"]
    return len(cards)


def build_docx():
    notes = Notes(TITLE, SUBJECT)
    final_section(notes)
    return notes.save(DOCX)


def build_note():
    rec = Rec(TITLE, SUBJECT)
    final_section(rec)
    sections, cram = convert_v2(rec.ops, [])
    tables = iter(op[2] for op in rec.ops if op[0] == "table")
    # The converter flattens table line breaks and invents empty-section summaries.
    for section in sections:
        if section["comparisons"]:
            section["summary"] = section["heading"]
            for table in section["comparisons"]:
                table["rows"] = next(tables)
    content = NoteContent.model_validate({
        "sections": sections, "formula_sheet": [], "self_check": [], "cram_sheet": cram,
    })
    return {"title": TITLE, "subject": SUBJECT, "module_ids": [],
            "content": content.model_dump(mode="json")}


def build_deck():
    rnd = random.Random(11)
    cards = []
    for question, correct, wrong in final_cards():
        options = [correct] + wrong
        rnd.shuffle(options)
        cards.append({"type": "multiple_choice", "question": question, "correct_answer": correct,
                      "options": json.dumps(options, ensure_ascii=False), "times_missed": 0})
    return {"name": "NetComms 2 Final Flashcards", "subject": SUBJECT,
            "modules_included": "M1 to M8, Practice Final, Course Final", "cards": cards}


def main():
    check_cards()
    payload = {"notes": [build_note()], "decks": [build_deck()]}
    with open(PAYLOAD, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, ensure_ascii=False)
    print("pdf", build_docx())


if __name__ == "__main__":
    main()
