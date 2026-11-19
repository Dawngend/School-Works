"""Renders the literal question bank (devasc-m7-m8-question-bank.json) into the reviewer, verbatim."""
import json
import os

BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "devasc-m7-m8-question-bank.json")


def load():
    text = open(BANK, encoding="utf-8").read().replace(" \u2014 ", ", ").replace("\u2014", "-")
    return json.loads(text)["items"]


def _row(item):
    q = item["question"].strip()
    if item.get("exhibit_image_url"):
        q += " (the exam shows an exhibit image here)"
    return [q, "\n".join(a.strip() for a in item["correct_answers"])]


def bank_section(n):
    items = load()
    n.h1("Question Bank: Literal Exam Questions And Answers")
    n.p("**Start here.** These are the real question-and-answer items for Modules 7 and 8 that Dawn pulled from the "
        "Cisco exam and quiz banks, copied word for word. Your prof's items are expected to look like these. Where "
        "the item says (Choose two.) or (Choose three.), every answer listed is correct and you must pick all of them.")
    for module, title in ((7, "Module 7 Infrastructure and Automation"), (8, "Module 8 Cisco Platforms and Development")):
        for bank_type, label in (("exam", "Exam Items"), ("quiz", "Quiz Items")):
            rows = [_row(i) for i in items if i["type"] == "mcq" and i["module"] == module and i["bank_type"] == bank_type]
            if not rows:
                continue
            n.h2(f"{title}: {label}")
            n.table(["Question", "Correct Answer"], rows, [3.4, 3.1])
    n.h2("Flashcard Terms From The Bank")
    for module, title in ((7, "Module 7"), (8, "Module 8")):
        rows = [[i["term"].strip(), i["definition"].strip()] for i in items if i["type"] == "flashcard" and i["module"] == module]
        if rows:
            n.h3(f"{title} Terms")
            n.table(["Term", "Definition"], rows, [2.0, 4.5])
