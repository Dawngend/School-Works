"""Convert the reviewer notes (notes_lib calls) into AndyHub NoteContent JSON, validated against the real schema.

The current AndyHub note layout has no memory-aid box, table, or cram sheet, so:
  table rows         -> key_terms   (term = first cell, definition = "Header: value; ...")
  list items         -> key_terms   (term = "<list label> N")
  Memory Aid boxes   -> properties  ("Memory Aid: <where>")
  Watch Out boxes    -> common_mistakes
  paragraphs         -> summary     (newlines are not rendered by the page, so they are joined with spaces)
  cram sheet section -> a normal section of key_terms
"""
import json
import os
import re
import sys

HUB = r"D:\Personal Projects\All In One Reviewer"
NC = r"D:\School-Works\Network and Communications 2\DEVASC M3-M4 Exam Prep"
SE = r"D:\School-Works\Software Engineering 1\SE1 Exam Prep"
sys.path.insert(0, NC)
sys.path.insert(0, SE)
sys.path.insert(0, HUB)

import netcomms_notes as nc
import se1_notes as se
from notes_lib import Notes
from andyhub_api.schemas import NoteContent


class Rec(Notes):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.ops = []

    def h1(self, t):
        self.ops.append(("h1", t)); super().h1(t)

    def h2(self, t):
        self.ops.append(("h2", t)); super().h2(t)

    def h3(self, t):
        self.ops.append(("h3", t)); super().h3(t)

    def p(self, t):
        self.ops.append(("p", t)); return super().p(t)

    def bullets(self, items):
        self.ops.append(("list", items)); super().bullets(items)

    def numbered(self, items):
        self.ops.append(("list", items)); super().numbered(items)

    def table(self, header, rows, widths=None):
        self.ops.append(("table", header, rows)); super().table(header, rows, widths)

    def box(self, label, text, fill="F2F2F2"):
        self.ops.append(("box", label, text)); super().box(label, text, fill)

    def memory(self, text):
        self.ops.append(("memory", text)); super().memory(text)

    def watch(self, text):
        self.ops.append(("watch", text)); super().watch(text)

    def pagebreak(self):
        pass

    def save(self, path):
        pass


def clean(t):
    t = t.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", t).strip()


def flat(items):
    out = []
    for it in items:
        out.extend(flat(it) if isinstance(it, (list, tuple)) else [it])
    return out


def uniq(seen, key):
    k, i = key, 2
    while k in seen:
        k = f"{key} ({i})"
        i += 1
    seen.add(k)
    return k


def convert(ops, source_refs):
    sections, cur, label = [], None, "List"

    def start(heading):
        nonlocal cur, label
        cur = {"heading": clean(heading), "summary": [], "key_terms": [], "properties": [],
               "worked_examples": [], "common_mistakes": [], "source_refs": source_refs,
               "_kt": set(), "_pr": set()}
        sections.append(cur)
        label = "List"

    pending_h1 = None
    for op in ops:
        kind = op[0]
        if kind == "h1":
            pending_h1 = op[1]
            cur = None
            continue
        if kind == "h2":
            start(op[1])
            pending_h1 = None
            continue
        if cur is None:
            start(pending_h1 or "Overview")
        if kind == "h3":
            label = clean(op[1])
        elif kind == "p":
            cur["summary"].append(clean(op[1]))
        elif kind == "list":
            for n, item in enumerate(flat(op[1]), 1):
                cur["key_terms"].append({"term": uniq(cur["_kt"], f"{label} {n}"), "definition": clean(item)})
        elif kind == "table":
            header, rows = op[1], op[2]
            for row in rows:
                cells = [clean(c) for c in row]
                if not cells[0]:
                    continue
                parts = [f"{clean(h)}: {c}" if clean(h) else c for h, c in zip(header[1:], cells[1:]) if c]
                cur["key_terms"].append({"term": uniq(cur["_kt"], cells[0]), "definition": "; ".join(parts) or cells[0]})
        elif kind == "memory":
            cur["properties"].append({"name": uniq(cur["_pr"], f"Memory Aid: {label if label != 'List' else cur['heading']}"),
                                      "statement": clean(op[1])})
        elif kind == "watch":
            cur["common_mistakes"].append(clean(op[1]))
        elif kind == "box" and op[1] not in ("Memory Aid", "Watch Out"):
            cur["properties"].append({"name": uniq(cur["_pr"], clean(op[1])), "statement": clean(op[2])})
    out = []
    for s in sections:
        if not s["summary"]:
            s["summary"] = [f"{s['heading']}: the key points are listed below."]
        s["summary"] = " ".join(s["summary"])
        s.pop("_kt"); s.pop("_pr")
        out.append(s)
    return out


def build(mod, fn, title_subject, refs):
    rec = Rec("x", "y")
    getattr(mod, fn)(rec)
    return convert(rec.ops, refs)


NOTES = [
    ("SE1 Module 3 Reviewer Notes", "Software Engineering 1", [], se, "m3", ["CS0025-M3S1.pdf", "CS0025-M3S2.pdf"]),
    ("SE1 Module 4 Reviewer Notes", "Software Engineering 1", [], se, "m4", ["CS0025-M4S1.pdf", "CS0025-M4S2.pdf"]),
    ("DevNet Module 3 Reviewer Notes", "Network and Communications 2", ["mod_ebea8118445b47e795619880665e5d18"], nc, "m3", ["DEVASC_Module_3.pdf"]),
    ("DevNet Module 4 Reviewer Notes", "Network and Communications 2", ["mod_8cba853c59b44508b2eb8ab45082e8e1"], nc, "m4", ["DEVASC_Module_4.pdf"]),
]

if __name__ == "__main__":
    out = []
    for title, subject, mids, mod, fn, refs in NOTES:
        secs = build(mod, fn, subject, refs)
        content = NoteContent.model_validate({"sections": secs, "formula_sheet": [], "self_check": []})
        out.append({"title": title, "subject": subject, "module_ids": mids, "content": content.model_dump(mode="json")})
        print(title, "sections", len(content.sections), "terms", sum(len(s.key_terms) for s in content.sections),
              "memory aids", sum(len(s.properties) for s in content.sections))
    json.dump(out, open(r"C:\Users\Dawn\AppData\Local\Temp\claude-out\notes_export.json", "w", encoding="utf-8"), indent=1)
