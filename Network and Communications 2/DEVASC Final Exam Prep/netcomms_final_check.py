import sys
sys.dont_write_bytecode = True

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import netcomms_final_build as build
from docx import Document


def main():
    build.main()
    items = build.load()
    with open(build.PAYLOAD, encoding="utf-8") as fh:
        payload_text = fh.read()
    payload = json.loads(payload_text)
    assert len(payload["notes"]) == len(payload["decks"]) == 1
    cards = payload["decks"][0]["cards"]
    assert len(items) == len(cards) == 200, "Expected 200 items and 200 cards"
    assert len({item["id"] for item in items}) == 200, "Duplicate item ID"
    for item, card in zip(items, cards):
        expected = "; ".join(choice for choice in item["choices"] if choice in item["correct"])
        options = json.loads(card["options"])
        assert isinstance(options, list), item["id"]
        assert card["correct_answer"] == expected, item["id"]
        assert expected in options, item["id"]
        assert len(options) in (3, 4), item["id"]
        assert len(set(options)) == len(options), item["id"]
        question = item["question"]
        if item["exhibit_text"]:
            question += " " + item["exhibit_text"]
        assert card["question"] == question, item["id"]

    content = payload["notes"][0]["content"]
    build.NoteContent.model_validate(content)
    tables = [table for section in content["sections"] for table in section["comparisons"]]
    assert [table["title"] for table in tables] == [heading for _, heading in build.GROUPS]
    rows = [row for table in tables for row in table["rows"]]
    assert len(rows) == 200, "Expected 200 grouped table rows"
    note_text = "\n".join(cell for row in rows for cell in row)
    for item in items:
        assert item["question"] in note_text, item["id"]
    for (source_page, _), table in zip(build.GROUPS, tables):
        expected_rows = [build._row(item) for item in items if item["source_page"] == source_page]
        assert table["rows"] == expected_rows, source_page
    assert "\u2014" not in payload_text, "Em dash in payload"

    assert os.path.isfile(build.DOCX), "Missing DOCX"
    doc = Document(build.DOCX)
    docx_text = "\n".join(
        [paragraph.text for paragraph in doc.paragraphs]
        + [cell.text for table in doc.tables for row in table.rows for cell in row.cells]
    )
    assert "\u2014" not in docx_text, "Em dash in DOCX"
    assert os.path.isfile(build.PDF), "Missing PDF"
    pdf_size = os.path.getsize(build.PDF)
    assert pdf_size > 0, "Empty PDF"
    with open(build.PDF, "rb") as fh:
        assert fh.read(4) == b"%PDF", "Invalid PDF header"
    print(f"{len(cards)} cards; PDF size: {pdf_size} bytes")


if __name__ == "__main__":
    main()
