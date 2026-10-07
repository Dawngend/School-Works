"""On the VM: python import_decks_vm.py <decks.json> [apply].

General deck importer for any verified-deck payload. Dry run is the default. Apply backs up reviewer.db first.
A deck whose name already exists is skipped, never replaced.
"""
import json
import os
import sqlite3
import sys
import time

DB = "/home/andreipamesa20/School-Works/All In One Reviewer/Database/reviewer.db"
BAK = os.path.expanduser("~/andyhub-backups")


def main():
    if len(sys.argv) not in (2, 3) or (len(sys.argv) == 3 and sys.argv[2] != "apply"):
        raise SystemExit("Usage: python import_decks_vm.py <decks.json> [apply]")
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    if not data or any(not d.get("name") or not d.get("cards") for d in data):
        raise ValueError("Every deck needs a name and at least one card")
    apply = len(sys.argv) == 3
    con = sqlite3.connect(DB, timeout=30)
    con.row_factory = sqlite3.Row
    try:
        dcols = {r["name"] for r in con.execute("pragma table_info(decks)")}
        ccols = {r["name"] for r in con.execute("pragma table_info(cards)")}
        existing = {r["name"] for r in con.execute("select name from decks")}
        if apply:
            os.makedirs(BAK, exist_ok=True)
            backup = os.path.join(BAK, "reviewer-before-deck-import-%d.db" % time.time_ns())
            with sqlite3.connect(backup) as target:
                con.backup(target)
            print("backup", backup)
        con.execute("begin immediate")
        try:
            for deck in data:
                name = deck["name"]
                if name in existing:
                    print("SKIP exists", name)
                    continue
                row = {key: deck[key] for key in ("modules_included", "subject", "module_ids") if key in dcols}
                row["name"] = name
                keys = list(row)
                cursor = con.execute(
                    "insert into decks (%s) values (%s)" % (",".join(keys), ",".join("?" * len(keys))),
                    [row[key] for key in keys],
                )
                for card in deck["cards"]:
                    values = {key: card[key] for key in ("type", "question", "correct_answer", "options", "times_missed") if key in ccols}
                    values["deck_id"] = cursor.lastrowid
                    keys = list(values)
                    con.execute(
                        "insert into cards (%s) values (%s)" % (",".join(keys), ",".join("?" * len(keys))),
                        [values[key] for key in keys],
                    )
                print("INSERT", name, len(deck["cards"]), "cards")
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
