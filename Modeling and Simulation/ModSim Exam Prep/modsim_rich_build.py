"""Build the final DOCX, PDF, and AndyHub note from rich_M1.json through rich_M6.json.

Run this script, then modsim_rich_check.py. Only the payload's notes value is
replaced; existing deck bytes, including checkout line endings, remain untouched.
Examples distinguish slide code from our executable completions. Source errors
and cropped-image uncertainties are explained in the notes rather than hidden.
"""
import json
import re
import sys
from pathlib import Path

from docx.shared import Pt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUTPUT = HERE.parent / "PAMESA - ModSim Final Reviewer"
PAYLOAD = ROOT / "AndyHub Export" / "payload_modsim_final.json"
TITLE = "ModSim Final Reviewer"
CONTENT_FIELDS = ("sections", "formula_sheet", "self_check", "cram_sheet")
sys.path.insert(0, str(ROOT / "Network and Communications 2" / "DEVASC M3-M4 Exam Prep"))
sys.path.insert(0, "D:/Personal Projects/All In One Reviewer")
from notes_lib import Notes
from modsim_notes import save_pdf
from andyhub_api.schemas import NoteContent


def load_modules():
    return [json.loads((HERE / f"rich_M{number}.json").read_text(encoding="utf-8-sig"))
            for number in range(1, 7)]


def combined_content(modules):
    content = {field: [item for module in modules for item in module[field]]
               for field in CONTENT_FIELDS}
    return NoteContent.model_validate(content).model_dump(mode="json")


def field_span(text, field):
    """Locate one top-level JSON value, leaving all surrounding bytes intact."""
    decoder = json.JSONDecoder()
    position = text.index("{") + 1
    while True:
        while text[position].isspace() or text[position] == ",":
            position += 1
        if text[position] == "}":
            raise ValueError(f"Missing payload field: {field}")
        key, position = decoder.raw_decode(text, position)
        while text[position].isspace():
            position += 1
        if text[position] != ":":
            raise ValueError("Expected a JSON object field")
        position += 1
        while text[position].isspace():
            position += 1
        start = position
        _, position = decoder.raw_decode(text, position)
        if key == field:
            return start, position


def write_box(notes, label, text):
    # Separate cell paragraphs survive save_pdf as explicit line breaks.
    lines = text.splitlines() or [""]
    for start in range(0, len(lines), 18):
        chunk = []
        for line in lines[start:start + 18]:
            line = line.expandtabs(4)
            indent = len(line) - len(line.lstrip(" "))
            chunk.append("\u00a0" * indent + line[indent:] if line else "\u00a0")
        notes.box(label if start == 0 else label + " (Continued)", "\n".join(chunk))


def write_text(notes, text):
    for index, part in enumerate(re.split(r"```(?:[A-Za-z][\w+-]*)?[ \t]*\n(.*?)```", text,
                                         flags=re.DOTALL)):
        if not part.strip():
            continue
        if index % 2:
            write_box(notes, "Code Or Printed Output", part.rstrip("\n"))
        elif "\n" in part.strip():
            write_box(notes, "Notes", part.strip())
        else:
            notes.p(part.strip())


def write_section(notes, section):
    notes.h2(section["heading"])
    notes.p(section["summary"])
    if section["key_terms"]:
        notes.table(["Term", "Meaning"],
                    [[item["term"], item["definition"]] for item in section["key_terms"]],
                    [1.6, 4.9])
    for item in section["properties"]:
        notes.h3(item["name"])
        write_text(notes, item["statement"])
    for table in section["comparisons"]:
        notes.h3(table["title"])
        notes.table(table["columns"], table["rows"],
                    [6.5 / len(table["columns"])] * len(table["columns"]))
    for example in section["worked_examples"]:
        notes.h3("Worked Example")
        notes.p("**Problem:** " + example["problem"])
        for number, step in enumerate(example["steps"], 1):
            notes.p(f"**Step {number}:**")
            write_text(notes, step)
        notes.p("**Answer:**")
        write_text(notes, example["answer"])
    for item in section["memory_aids"]:
        notes.memory(item["label"] + ": " + item["text"])
    for trap in section["common_mistakes"]:
        notes.watch(trap)
    notes.p("Sources: " + "; ".join(section["source_refs"]))


def write_module_sheets(notes, number, module):
    notes.h2(f"M{number}: Formula Sheet")
    for item in module["formula_sheet"]:
        notes.p("**" + item["name"] + ":** " + item["expression"])
        notes.p(item["when_to_use"])
    notes.h2(f"M{number}: Self-Check")
    notes.numbered([item["question"] + " Answer: " + item["answer"]
                    for item in module["self_check"]])
    notes.doc.add_page_break()
    notes.h2(f"M{number}: Cram Sheet")
    notes.table(["Topic", "Remember"],
                [[item["topic"], item["remember"]] for item in module["cram_sheet"]],
                [1.3, 5.2])


def replace_note(content):
    original = PAYLOAD.read_bytes()
    text = original.decode("utf-8")
    payload = json.loads(text)
    if len(payload["notes"]) != 1 or payload["notes"][0]["title"] != TITLE:
        raise ValueError("Expected exactly the existing ModSim Final Reviewer note")
    note = dict(payload["notes"][0], content=content)
    start, end = field_span(text, "notes")
    replacement = json.dumps([note], ensure_ascii=False, indent=2)
    updated = (text[:start] + replacement + text[end:]).encode("utf-8")
    deck_start, deck_end = field_span(text, "decks")
    new_text = updated.decode("utf-8")
    new_start, new_end = field_span(new_text, "decks")
    if text[deck_start:deck_end].encode("utf-8") != new_text[new_start:new_end].encode("utf-8"):
        raise ValueError("Deck bytes changed")
    PAYLOAD.write_bytes(updated)


def build():
    modules = load_modules()
    content = combined_content(modules)
    notes = Notes(TITLE, "CS0019 | Modules 1 To 6 | Saturday, November 28, 2026 | 7 AM")
    notes.p("Read the explanations first, compare the tables, then trace the MATLAB examples. "
            "Blue memory aids are ours, not the slides; red boxes flag exam traps and slide errors. "
            "MATLAB commands require no import statements. Printed outputs are checked by modsim_rich_check.py.")
    notes.h1("What Is Inside")
    notes.numbered([
        "Module 1: Introduction To Modeling And Simulation",
        "Module 2: Discrete Event Simulation",
        "Module 3: Modeling Continuous Systems",
        "Module 4: Monte Carlo Simulation",
        "Module 5: Systems Modeling",
        "Module 6: Visualization And VV&A",
    ])
    notes.p("Each module includes comparison tables, code references, worked examples, "
            "a formula sheet, six self-checks, and a one-page cram sheet.")
    notes.h1("Fast Memory Map")
    notes.table(["Module", "Focus"], [
        ["M1", "Represent A System; MATLAB Arrays And Operators"],
        ["M2", "Probability, Random Inputs, Events, And Queues"],
        ["M3", "Continuous State Equations; MATLAB Programs"],
        ["M4", "Repeated Random Samples And Monte Carlo Estimates"],
        ["M5", "Model Types And Simulink Block Diagrams"],
        ["M6", "Visualize, Verify, Validate, And Accredit"],
    ], [0.8, 5.7])
    for number, module in enumerate(modules, 1):
        notes.doc.add_page_break()
        notes.h1(f"Module {number}")
        for section in module["sections"]:
            write_section(notes, section)
        write_module_sheets(notes, number, module)
    notes.doc.styles["Normal"].font.size = Pt(12)
    notes.doc.save(str(OUTPUT.with_suffix(".docx")))
    save_pdf(notes.doc, OUTPUT.with_suffix(".pdf"))
    replace_note(content)
    print(f"Built {len(content['sections'])} sections; DOCX, PDF, and payload note updated; deck bytes unchanged.")


if __name__ == "__main__":
    build()
