"""Run R1-R7 against the local School Library API Simulator and save redacted response evidence.

Local DEVASC simulator only. The lab credentials are read with getpass and never written to disk;
the temporary token is replaced with <redacted> in every saved file, and each file is checked for
the password and token before it is written.

Usage (inside the DEVASC VM):
    python3 capture_evidence.py [base_url]      # default http://library.demo.local
"""

from __future__ import annotations

import getpass
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://library.demo.local").rstrip("/")
OUT = Path(__file__).parent / "evidence"
TIMEOUT = 10
BOOK = {"id": 901, "title": "Packets Beneath the Acacia", "author": "Lorna Villaverde",
        "isbn": "978-0-000-00901-0"}
BOOK_R7 = {"id": 902, "title": "Packets Beneath the Acacia, Second Printing",
           "author": "Lorna Villaverde", "isbn": "978-0-000-00902-0"}

secrets: list[str] = []
results: list[dict[str, Any]] = []


def redact(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: redact(v) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v) for v in value]
    if isinstance(value, str):
        for s in secrets:
            if s:
                value = value.replace(s, "<redacted>")
    return value


def summarize(body: Any) -> Any:
    if isinstance(body, list) and len(body) > 5:
        return {"total_items": len(body), "first_5_items": body[:5]}
    return body


def run(rid: str, filename: str, label: str, method: str, path: str, expected: int, *,
        params: dict[str, str] | None = None, headers: dict[str, str] | None = None,
        body: dict[str, Any] | None = None, auth: tuple[str, str] | None = None,
        shown_headers: dict[str, str] | None = None) -> requests.Response:
    r = requests.request(method, BASE + path, params=params, headers=headers, json=body,
                         auth=auth, timeout=TIMEOUT)
    try:
        resp_body: Any = r.json()
    except ValueError:
        resp_body = r.text[:500]
    record = {
        "request_id": rid,
        "label": label,
        "captured_at": datetime.now().isoformat(timespec="seconds"),
        "method": method,
        "url": r.url,
        "request_headers": shown_headers or {},
        "request_body": body,
        "expected_status": expected,
        "status": r.status_code,
        "reason": r.reason,
        "matches_expected": r.status_code == expected,
        "response_content_type": r.headers.get("Content-Type"),
        "response_body": summarize(resp_body),
    }
    text = json.dumps(redact(record), indent=2)
    assert not any(s and s in text for s in secrets), "secret found in evidence, not written"
    (OUT / filename).write_text(text + "\n", encoding="utf-8")
    results.append(redact(record))
    print(f"{'OK  ' if r.status_code == expected else 'DIFF'} {rid:4} {method:6} {r.url} -> "
          f"{r.status_code} (expected {expected})")
    return r


def main() -> int:
    OUT.mkdir(exist_ok=True)
    user = input("Lab username: ")
    password = getpass.getpass("Lab password: ")
    secrets.extend([password])
    json_h = {"Content-Type": "application/json"}

    run("R1", "R1_list_books.json", "List all books", "GET", "/api/v1/books", 200)
    run("R2", "R2_isbn_sorted.json", "Books with ISBN, sorted by author", "GET", "/api/v1/books",
        200, params={"includeISBN": "true", "sortBy": "author"})
    r3 = run("R3", "R3_login_basic.json", "Obtain temporary token (Basic Auth)", "POST",
             "/api/v1/loginViaBasic", 200, auth=(user, password),
             shown_headers={"Authorization": "Basic <redacted>"})
    token = str(r3.json().get("token", "")) if r3.status_code == 200 else ""
    if not token:
        print("R3 did not return a token; stopping. Check the credentials and base URL.")
        return 1
    secrets.append(token)
    # R3 was written before the token was known; rewrite it with the token redacted.
    r3_file = OUT / "R3_login_basic.json"
    r3_file.write_text(json.dumps(redact(json.loads(r3_file.read_text())), indent=2) + "\n",
                       encoding="utf-8")
    results[-1] = redact(results[-1])
    key_h = {"X-API-KEY": token}
    key_shown = {"X-API-KEY": "<redacted>"}

    run("R4", "R4_add_book.json", "Add fictional book", "POST", "/api/v1/books", 200,
        headers={**json_h, **key_h}, body=BOOK, shown_headers={**json_h, **key_shown})
    run("R5", "R5_get_book_by_id.json", "Get new book by ID", "GET", "/api/v1/books/901", 200)
    run("R6", "R6_delete_book.json", "Delete new book", "DELETE", "/api/v1/books/901", 200,
        headers=key_h, shown_headers=key_shown)
    run("R6b", "R6_verify_deleted.json", "Confirm book 901 is gone (expect not 200)", "GET",
        "/api/v1/books/901", 404)
    run("R7a", "R7_401_missing_key.json", "Add book with X-API-KEY omitted", "POST",
        "/api/v1/books", 401, headers=json_h, body=BOOK_R7, shown_headers=json_h)
    run("R7b", "R7_401_invalid_key.json", "Add book with an altered X-API-KEY", "POST",
        "/api/v1/books", 401, headers={**json_h, "X-API-KEY": "invalid-key-for-r7"}, body=BOOK_R7,
        shown_headers={**json_h, "X-API-KEY": "invalid-key-for-r7 (deliberately wrong)"})
    run("R7c", "R7_fixed_200.json", "Add book with the valid key restored", "POST",
        "/api/v1/books", 200, headers={**json_h, **key_h}, body=BOOK_R7,
        shown_headers={**json_h, **key_shown})
    run("R7d", "R7_cleanup_delete.json", "Cleanup: delete book 902", "DELETE",
        "/api/v1/books/902", 200, headers=key_h, shown_headers=key_shown)

    lines = ["# Response Evidence Summary", "",
             f"Captured {datetime.now():%Y-%m-%d %H:%M} against the local simulator at `{BASE}`.",
             "Credential and token values are redacted in every file.", "",
             "| Request | Method | URL | Expected | Actual | Match |", "|---|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r['request_id']} | {r['method']} | `{r['url']}` | {r['expected_status']} | "
                     f"{r['status']} {r['reason']} | {'yes' if r['matches_expected'] else 'NO'} |")
    summary = "\n".join(lines) + "\n"
    assert not any(s and s in summary for s in secrets)
    (OUT / "evidence_summary.md").write_text(summary, encoding="utf-8")
    mismatches = [r["request_id"] for r in results if not r["matches_expected"]]
    print("\nAll statuses matched." if not mismatches else f"\nStatus differed for: {mismatches}")
    return 0 if not mismatches else 2


if __name__ == "__main__":
    raise SystemExit(main())
