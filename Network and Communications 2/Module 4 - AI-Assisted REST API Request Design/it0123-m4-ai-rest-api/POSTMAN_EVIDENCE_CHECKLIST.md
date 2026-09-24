# Postman Evidence Checklist

Student: Dawn Andrei C. Pamesa  Section: TS31

Submit screenshots or exported responses only after redacting credential values.

Evidence is exported responses: `capture_evidence.py` sends each request to the local simulator and
saves method, URL, status and a response summary per request in `evidence/`, with the password and
token replaced by `<redacted>` before anything is written. `evidence/evidence_summary.md` tabulates
expected against actual status for every step.

- [ ] R1: GET all books, with URL and 200 status visible (`evidence/R1_list_books.json`)
- [ ] R2: GET books using `includeISBN=true` and `sortBy=author` (`evidence/R2_isbn_sorted.json`)
- [ ] R3: Basic Auth request and 200 status; token value fully hidden (`evidence/R3_login_basic.json`)
- [ ] R4: POST a fictional book, with JSON body and 200 status visible (`evidence/R4_add_book.json`)
- [ ] R5: GET the newly added book by ID (`evidence/R5_get_book_by_id.json`)
- [ ] R6: DELETE the newly added book by ID (`evidence/R6_delete_book.json`)
- [ ] R7: Intentional local failure showing 401 with key values hidden (`evidence/R7_401_missing_key.json`)
- [ ] Final successful verification after correcting R7 (`evidence/R7_fixed_200.json`)
- [ ] Offline validator output showing all checks passed (`validator_output.txt`)

The requests were built as the Postman collection `IT0123_M4_Library_API.postman_collection.json`,
which carries a status-code test for every step, so each screenshot also shows the test result.
The collection's credential and token variables are blank in the submitted copy.

Never export or submit a live Postman environment containing secrets.
