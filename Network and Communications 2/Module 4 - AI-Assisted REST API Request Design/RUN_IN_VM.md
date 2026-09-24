# What is left: one command in the DEVASC VM (about 5 minutes)

1. Start the DEVASC VM and the School Library API Simulator.
2. Copy this module folder into the VM, open a terminal in `it0123-m4-ai-rest-api`, and run:

   ```
   python3 capture_evidence.py
   ```

   Type the instructor's lab username and password when asked. The password is read with getpass and
   never saved. The script sends R1 to R7 (plus the cleanup deletes), and writes one redacted response
   file per step to `evidence/`, plus `evidence/evidence_summary.md`. If the simulator uses a different
   base URL, pass it: `python3 capture_evidence.py http://<host>`.
3. It prints OK or DIFF per step. If every line is OK, tick the boxes in `POSTMAN_EVIDENCE_CHECKLIST.md`.
   If any line says DIFF, send Claude the printed status so the log and plan can be corrected to match.
4. Run `python3 make_submission.py` to build `Pamesa_DawnAndrei_IT0123_M4_AI_REST_API.zip`.

Optional: give the `evidence/` folder back to Claude to render the JSON files as screenshot images.
The Postman collection is still included if you prefer to click through it in Postman instead.
