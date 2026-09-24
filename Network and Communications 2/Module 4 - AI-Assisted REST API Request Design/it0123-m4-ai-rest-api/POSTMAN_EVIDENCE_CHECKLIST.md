# Postman Evidence Checklist

Student: Dawn Andrei C. Pamesa  Section: TS31

Submit screenshots or exported responses only after redacting credential values.

- [ ] R1: GET all books, with URL and 200 status visible (`evidence/R1_list_books.png`)
- [ ] R2: GET books using `includeISBN=true` and `sortBy=author` (`evidence/R2_isbn_sorted.png`)
- [ ] R3: Basic Auth request and 200 status; token value fully hidden (`evidence/R3_login_basic.png`)
- [ ] R4: POST a fictional book, with JSON body and 200 status visible (`evidence/R4_add_book.png`)
- [ ] R5: GET the newly added book by ID (`evidence/R5_get_book_by_id.png`)
- [ ] R6: DELETE the newly added book by ID (`evidence/R6_delete_book.png`)
- [ ] R7: Intentional local failure showing 401 with key values hidden (`evidence/R7_401_missing_key.png`)
- [ ] Final successful verification after correcting R7 (`evidence/R7_fixed_200.png`)
- [ ] Offline validator output showing all checks passed (`validator_output.txt`)

The requests were built as the Postman collection `IT0123_M4_Library_API.postman_collection.json`,
which carries a status-code test for every step, so each screenshot also shows the test result.
The collection's credential and token variables are blank in the submitted copy.

Never export or submit a live Postman environment containing secrets.
