# What is left: run it in the DEVASC VM (about 15 minutes)

Everything else is done. The only part that has to happen in the VM is running the requests and taking
the screenshots.

1. Start the DEVASC VM and the School Library API Simulator. Open the docs page and check the base
   URL the simulator shows. The collection assumes `http://library.demo.local`.
2. Postman: Import, then choose `it0123-m4-ai-rest-api/IT0123_M4_Library_API.postman_collection.json`.
3. Open the collection, go to the Variables tab, and type the instructor's lab username and password into
   `labUser` and `labPass` (Current value only). Fix `baseUrl` if step 1 showed something different.
4. Send each request in order, R1 to R7d, and screenshot each one with the URL, status and Test Results
   visible. Blur the token in R3 and the `X-API-KEY` value in R4, R6 and R7. Save the screenshots in
   `it0123-m4-ai-rest-api/evidence/` using the names in `POSTMAN_EVIDENCE_CHECKLIST.md`, then tick the
   boxes.
5. Optional, but it covers the Try It Out step: run R1 and R2 once in the simulator's own docs page too.
6. Clear `labUser`, `labPass` and `apiKey` in Postman. Do not export the collection after the run.
7. Run `python make_submission.py`. It re-runs the validator and builds
   `Pamesa_DawnAndrei_IT0123_M4_AI_REST_API.zip`.

If any collection test fails (for example the simulator returns 201 for R4, or 403 for R7b), tell
Claude what it returned. The log and plan record 200, 200 and 401 as the observed results, so they
would need updating to match what the simulator actually does.
