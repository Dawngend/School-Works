"""Validate andyhub_ml_notes.json against AndyHub's own NoteContent schema before it goes anywhere near the VM."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"D:\Personal Projects\All In One Reviewer")
from andyhub_api.schemas import NoteContent

notes = json.load(open(os.path.join(HERE, "andyhub_ml_notes.json"), encoding="utf-8"))
for n in notes:
    c = NoteContent.model_validate(n["content"])
    code_examples = sum(len(s.worked_examples) for s in c.sections)
    print("OK", n["title"], "| sections", len(c.sections), "| code examples", code_examples,
          "| self_check", len(c.self_check), "| cram", len(c.cram_sheet))
