# AI-Use Disclosure

**Student:** Pamesa, Dawn Andrei
**Course / Module:** CS0016 — Module 1, AI Code Debugging
**Date:** 3 September 2026

---

## 1. Tool used

Claude (Anthropic), accessed through the web chat interface. No other AI assistant
was used for this activity. No credentials, personal data, institutional secrets or
private source code were entered into the tool — only the provided starter file, which
contains fictional documentation-range IP addresses (192.0.2.0/24, RFC 5737).

## 2. Prompts sent

Three focused prompts were sent, each following the pattern in section 7 of the
activity sheet. Each one contained the observed error or wrong result, the expected
behavior from section 6, and only the single relevant function — not the whole file.

1. **TypeError in `build_report()`** — supplied the traceback and the failing line,
   asked for the root cause, the Python concept, and the smallest correction.
2. **Reversed labels from `classify_device()`** — supplied the observed
   classification for the 12 ms, 25 ms and 150 ms devices and the expected rule.
3. **Wrong average in `average_online_latency()`** — supplied the printed 37.40 ms,
   the expected 62.33 ms, and the three online latency values.

Each prompt explicitly asked the tool not to rewrite the whole program and to state
how the correction could be verified independently.

## 3. Assistance received

The tool identified root causes and minimal corrections for seven defects:

| # | Function | Defect | Correction |
|---|----------|--------|-----------|
| 1 | `count_online` | Compared status against `"UP"` while the data stores `"up"` | Compare against `"up"` |
| 2 | `average_online_latency` | Divided the sum by `len(devices)` instead of the filtered list | Divide by `len(online_latencies)` |
| 3 | `find_slow_devices` | Used `<` threshold, returning fast devices | Use `>` threshold |
| 4 | `classify_device` | `<= threshold` returned `"SLOW"`, inverting the labels | `> threshold` returns `"SLOW"` |
| 5 | `render_device_lines` | `range(len(devices) - 1)` skipped the last device | `range(len(devices))` |
| 6 | `render_device_lines` | Misspelled dictionary key `"ip_adress"` | `"ip_address"` |
| 7 | `build_report` | `"Total devices: " + len(devices)` concatenated str and int | f-string |

Defects 1, 5 and 6 were surfaced during the same conversation but were not written up
as separate records, since section 8 requires a minimum of three.

## 4. Checks performed

- Ran `python3 network_inventory.py` after each individual correction and recorded
  what changed, rather than applying all fixes at once.
- Hand-calculated the expected average, `(12 + 150 + 25) / 3 = 62.333`, before editing
  `average_online_latency()`, so the fix was confirmed against my own arithmetic and
  not only against the tool's explanation.
- Traced the three online devices against the section 6 requirement table by hand to
  confirm the classification logic was inverted.
- Ran `python3 -m unittest -v test_network_inventory.py` until all six tests reported
  `ok`. Output saved as `test_results.txt`.
- Performed the manual output check in step 8: totals, average, slow-device count and
  all five device lines compared against section 6. Output saved as
  `program_output.txt`.

## 5. Revisions made to AI output

- One reply returned a full rewritten version of `average_online_latency()` including a
  renamed variable and a restructured comprehension. This was **modified** down to the
  single-line divisor change, because the guard clause and comprehension were already
  correct and replacing untested working code would have risked new defects.
- All explanations in the activity sheet were rewritten in my own words. No raw AI
  output was submitted as an explanation.
- Suggested corrections were applied one at a time with a re-run in between, rather
  than accepted as a batch, so that each change could be attributed to a specific
  observed behavior.
