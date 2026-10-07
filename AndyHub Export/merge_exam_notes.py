"""Merge the per-module AndyHub notes into one note per exam (Dawn, 2026-10-07: never per module).

Reads the existing note exports, joins their sections in module order (heading prefixed with the module), and writes
notes_per_exam.json for import_ml_notes_vm.py. No AI step; every section is copied as is.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, r"D:\Personal Projects\All In One Reviewer")
from andyhub_api.schemas import NoteContent  # noqa: E402

SOURCES = [
    HERE / "notes_statana_mobprog.json",
    HERE / "notes_se1_netcomms_modsim.json",
    Path(r"C:\Users\Dawn\AppData\Local\Temp\claude-out\notes_export_v2.json"),
]

EXAMS = [
    ("StatAna Summative 2 Reviewer", "Statistical Analysis and Modeling", "StatAna", [3, 4]),
    ("StatAna Midterm Reviewer", "Statistical Analysis and Modeling", "StatAna", [1, 2, 3, 4]),
    ("MobProg Midterm Reviewer", "Mobile Programming", "MobProg", [1, 2, 3, 4, 5]),
    ("SE1 Midterm Reviewer", "Software Engineering 1", "SE1", [1, 2, 3, 4]),
    ("DevNet Midterm Reviewer", "Network and Communications 2", "DevNet", [1, 2, 3, 4]),
    ("ModSim Midterm Reviewer", "Modeling and Simulation", "ModSim", [1, 2, 3]),
]


def load_notes():
    notes = {}
    for path in SOURCES:
        for note in json.loads(path.read_text(encoding="utf-8")):
            notes[note["title"]] = note
    return notes


def merge(notes, prefix, modules):
    merged = {"sections": [], "formula_sheet": [], "self_check": [], "cram_sheet": []}
    for n in modules:
        content = notes[f"{prefix} Module {n} Reviewer Notes"]["content"]
        for section in content["sections"]:
            merged["sections"].append({**section, "heading": f"Module {n}: {section['heading']}"})
        for key in ("formula_sheet", "self_check", "cram_sheet"):
            merged[key].extend(content.get(key) or [])
    return NoteContent.model_validate(merged).model_dump(mode="json")


def main():
    notes = load_notes()
    out = []
    for title, subject, prefix, modules in EXAMS:
        content = merge(notes, prefix, modules)
        out.append({"title": title, "subject": subject, "module_ids": [], "content": content})
        print(f"{title}: modules {modules}, sections {len(content['sections'])}")
    (HERE / "notes_per_exam.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
