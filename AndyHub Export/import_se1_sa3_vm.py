"""On the VM: python import_se1_sa3_vm.py <payload.json> [apply].

Payload: {"notes": [{title, subject, module_ids, content}], "decks": [{name, subject, modules_included, cards}]}.
Dry run is the default and rolls back. A note or deck whose name already exists is skipped, never replaced.
`andy deploy` backs up reviewer.db before the apply step.
"""
import json
import sqlite3
import sys
import time

DB = "/home/andreipamesa20/School-Works/All In One Reviewer/Database/reviewer.db"


def main():
    if len(sys.argv) not in (2, 3) or (len(sys.argv) == 3 and sys.argv[2] != "apply"):
        raise SystemExit("Usage: python import_se1_sa3_vm.py <payload.json> [apply]")
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    apply = len(sys.argv) == 3
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    con = sqlite3.connect(DB, timeout=30)
    try:
        existing_notes = {r[0] for r in con.execute("select title from notes")}
        existing_decks = {r[0] for r in con.execute("select name from decks")}
        con.execute("begin immediate")
        for note in data["notes"]:
            if note["title"] in existing_notes:
                print("SKIP note exists", note["title"])
                continue
            con.execute(
                "insert into notes (title, subject, module_ids, content, created_at, updated_at) values (?,?,?,?,?,?)",
                (note["title"], note["subject"], json.dumps(note["module_ids"]), json.dumps(note["content"], ensure_ascii=False), now, now),
            )
            print("INSERT note", note["title"], len(note["content"]["sections"]), "sections")
        for deck in data["decks"]:
            if deck["name"] in existing_decks:
                print("SKIP deck exists", deck["name"])
                continue
            cursor = con.execute(
                "insert into decks (name, modules_included, subject) values (?,?,?)",
                (deck["name"], deck["modules_included"], deck["subject"]),
            )
            for card in deck["cards"]:
                con.execute(
                    "insert into cards (deck_id, type, question, correct_answer, options, times_missed) values (?,?,?,?,?,?)",
                    (cursor.lastrowid, card["type"], card["question"], card["correct_answer"], card["options"], card["times_missed"]),
                )
            print("INSERT deck", deck["name"], len(deck["cards"]), "cards")
        if apply:
            con.commit()
            print("COMMITTED")
        else:
            con.rollback()
            print("DRY RUN, rolled back")
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()


if __name__ == "__main__":
    main()
