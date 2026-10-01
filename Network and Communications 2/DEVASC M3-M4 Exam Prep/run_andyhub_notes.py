import json
import os
import sys
import time

HUB = r"D:\Personal Projects\All In One Reviewer"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HUB)
os.chdir(HUB)

import database
import generator
from andyhub_api.services import validate_generated_note

SUBJECT = "Network and Communications 2"
database.init_db()
out = {}

for n, name in ((3, "Module 3 Software Development and Design"), (4, "Module 4 Understanding and Using APIs")):
    path = os.path.join(HERE, f"DEVASC_Module_{n}.pdf")
    prep = generator.prepare_custom_deck([path], report=print)
    client = generator._get_client()
    prompt = generator.get_andy_note_prompt("standard", list(prep.selected_files))
    raw = []
    for chunk in prep.chunks:
        raw.append(generator._query_note(client, chunk + generator.get_historical_context(chunk, SUBJECT), prompt))
        time.sleep(2)
    content, received, valid = validate_generated_note(raw)
    print(name, "sections received/valid", received, valid)
    out[name] = content.model_dump(mode="json")

with open(os.path.join(HERE, "andyhub_notes.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)

mock = generator.generate_custom_deck(
    [os.path.join(HERE, "DEVASC_Module_3.pdf"), os.path.join(HERE, "DEVASC_Module_4.pdf")],
    "DEVASC Mock Exam Modules 3 and 4",
    SUBJECT,
    50,
    "multiple_choice",
)
cards = database.get_cards_for_deck(mock) if mock else []
with open(os.path.join(HERE, "andyhub_mock.json"), "w", encoding="utf-8") as fh:
    json.dump({"deck_id": mock, "cards": [list(c) for c in cards]}, fh, indent=1, default=str)
print("DONE notes + mock", mock, len(cards))
