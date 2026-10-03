"""Convert the reviewer notes into the NEW AndyHub note format (memory_aids, comparisons, cram_sheet).

Run from the AndyHub repo so andyhub_api imports. Output: Temp\\claude-out\\notes_export_v2.json
"""
import json
import re

from notes_to_andyhub import NOTES, Rec, clean, flat, uniq
from andyhub_api.schemas import NoteContent


def lines(text):
    return "\n".join(clean(x) for x in text.split("\n") if clean(x))


def convert_v2(ops, source_refs):
    sections, cram = [], []
    cur, label, pending_h1 = None, None, None

    def start(heading):
        nonlocal cur, label
        cur = {"heading": clean(heading), "summary": [], "key_terms": [], "properties": [],
               "worked_examples": [], "common_mistakes": [], "source_refs": source_refs,
               "memory_aids": [], "comparisons": [], "_pr": set()}
        sections.append(cur)
        label = None

    for op in ops:
        kind = op[0]
        if kind == "h1":
            pending_h1, cur = op[1], None
            continue
        if kind == "h2":
            start(op[1]); pending_h1 = None
            continue
        if cur is None:
            start(pending_h1 or "Overview")
        in_cram = "cram sheet" in cur["heading"].lower()
        if kind == "h3":
            label = clean(op[1])
        elif kind == "p":
            cur["summary"].append(clean(op[1]))
        elif kind == "list":
            items = flat(op[1])
            body = "\n".join(f"{n}. {clean(i)}" if False else f"\u2022 {clean(i)}" for n, i in enumerate(items, 1))
            cur["summary"].append((f"{label}:\n" if label else "") + body)
        elif kind == "table":
            header, rows = op[1], op[2]
            if in_cram:
                cram.extend({"topic": clean(r[0]), "remember": clean(r[1])} for r in rows if clean(r[0]))
                continue
            cols = [clean(h) or "Point" for h in header]
            body = [[clean(c) for c in r] for r in rows if clean(r[0])]
            cur["comparisons"].append({"title": label or cur["heading"], "columns": cols, "rows": body})
        elif kind == "memory":
            cur["memory_aids"].append({"label": label or cur["heading"], "text": lines(op[1])})
        elif kind == "watch":
            cur["common_mistakes"].append(clean(op[1]))
        elif kind == "box" and op[1] not in ("Memory Aid", "Watch Out"):
            cur["properties"].append({"name": uniq(cur["_pr"], clean(op[1])), "statement": clean(op[2])})
    out = []
    for s in sections:
        if "cram sheet" in s["heading"].lower():
            continue
        s["summary"] = "\n\n".join(s["summary"]) or f"{s['heading']}: key points are below."
        s.pop("_pr")
        out.append(s)
    return out, cram


if __name__ == "__main__":
    result = []
    for title, subject, mids, mod, fn, refs in NOTES:
        rec = Rec("x", "y")
        getattr(mod, fn)(rec)
        secs, cram = convert_v2(rec.ops, refs)
        content = NoteContent.model_validate({"sections": secs, "formula_sheet": [], "self_check": [], "cram_sheet": cram})
        result.append({"title": title, "subject": subject, "module_ids": mids, "content": content.model_dump(mode="json")})
        print(title, "sections", len(content.sections), "tables", sum(len(s.comparisons) for s in content.sections),
              "memory aids", sum(len(s.memory_aids) for s in content.sections), "cram", len(content.cram_sheet))
    json.dump(result, open(r"C:\Users\Dawn\AppData\Local\Temp\claude-out\notes_export_v2.json", "w", encoding="utf-8"), indent=1)
