"""On the VM: python import_replace_decks_vm.py <payload.json> [apply].

Payload: {"decks": [{name, subject, modules_included, cards}]}.
A deck whose name already exists is REPLACED (its cards are deleted first). Dry run is the default and rolls back.
`andy deploy` backs up reviewer.db before the apply step.
"""
import json
import sqlite3
import sys

DB = "/home/andreipamesa20/School-Works/All In One Reviewer/Database/reviewer.db"


def main():
    if len(sys.argv) not in (2, 3) or (len(sys.argv) == 3 and sys.argv[2] != "apply"):
        raise SystemExit("Usage: python import_replace_decks_vm.py <payload.json> [apply]")
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    apply = len(sys.argv) == 3
    con = sqlite3.connect(DB, timeout=30)
    try:
        con.execute("begin immediate")
        for deck in data["decks"]:
            for (deck_id,) in con.execute("select id from decks where name = ?", (deck["name"],)).fetchall():
                removed = con.execute("delete from cards where deck_id = ?", (deck_id,)).rowcount
                con.execute("delete from decks where id = ?", (deck_id,))
                print("DELETE deck", deck["name"], deck_id, removed, "cards")
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
