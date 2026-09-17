# Reflection Questions

## 1. Which AI recommendation did you modify or reject, and what evidence guided your decision?

The JSON one, and specifically the `roles` line. The recommendation de-duplicated the roles with a set,
which is the obvious instinct because a set removes repeats in a single step and roles genuinely could
repeat in a larger inventory. The problem is that `test_json_roles` compares against an ordered list, and
a set has no defined iteration order.

What decided it was a measurement rather than an argument. I ran `list(set(roles))` under six different
values of `PYTHONHASHSEED`, since CPython randomizes string hashing per process, and it produced the
order the test expects in one run out of six. Five of the six runs produced a different order. That is
not a test that passes or fails on merit, it is a test that passes sometimes, and the failure would
appear on whichever machine happened to hash differently, which could easily be the grader's rather than
mine. I replaced it with `dict.fromkeys`, which de-duplicates the same way while keeping order of first
appearance, because dictionaries have preserved insertion order since Python 3.7. Re-running the finished
implementation under the same six seeds returned the same list every time.

I also turned down `sorted(set(...))`, which is deterministic and would also pass. The docstring asks for
`roles` and never asks for sorted roles, and in this particular file the file order and the alphabetical
order happen to be identical, so sorting would have been an assumption the data cannot justify and that a
future inventory would quietly break.

## 2. How did the unit tests complement manual inspection of the parser output?

They caught different things, and the lab has a clean example of each.

The tests caught what I could not see. Seven assertions ran on every change, so when I edited one parser
I found out immediately whether I had disturbed another, and they held me to exact values rather than to
values that looked about right. `test_combined_summary` checking `set(result)` for equality rather than
membership is the kind of constraint I would not have re-verified by eye after every edit.

Manual inspection caught what the tests structurally could not. The YAML `devices` list and the JSON
`enabled_devices` list both hold `["R1", "SW1"]`, from two unrelated files, by coincidence. I predicted
before implementing that this made a wrong-source bug invisible, and then I proved it: I took a throwaway
copy of the project, deliberately rewired `build_summary` so the YAML device list was sourced from the
JSON file, and ran the suite. All seven tests reported `ok`. The code was reading from the wrong file and
the test suite had no way to say so, because both files agree on that value.

So the tests prove the values are correct and the manual check proves they came from the right place.
A green suite is evidence about outputs, not evidence about provenance, and this lab is built so that the
difference between those two things actually costs you something.

## 3. What information did the Git history preserve that a final code file alone would not show?

The order, which is the whole basis for claiming the AI was evaluated rather than copied.

The predictions commit is the clearest case. It sits in the history before any implementation exists, so
it is verifiable that I wrote down what I expected the three files to contain before I asked for a
recommendation. Read from the finished `parser_template.py` alone, those predictions would be worthless,
because nothing would distinguish a prediction from a description written afterwards to look like one.
The commit timestamp and its position in the graph are what make it evidence.

The same applies to the decisions. The final file shows `dict.fromkeys` and nothing else. It does not show
that a set was recommended first, that I measured the set across six hash seeds, and that the replacement
happened because of the measurement. The history separates the XML, JSON and YAML work into commits that
each pair a code change with the log entry justifying it, so a reviewer can see which reasoning produced
which line.

The branch topology preserves something a file cannot represent at all. A file has one state. The graph
shows that `main` and `docs/ai-note` held two different values for the same line at the same time, and
that a human decided which text survived. The resolved line reads
`Validation status: AI reviewed and tests passed`, and only the history shows that this was a decision
between two real alternatives rather than something typed once.

## 4. How did you recognize and resolve the controlled merge conflict?

Git announced it, and I read the announcement instead of guessing. Merging `docs/ai-note` into `main`
printed `CONFLICT (content): Merge conflict in AI_USAGE_LOG.md` and stopped with
`Automatic merge failed; fix conflicts and then commit the result`, so the merge was left open rather
than completed. Running `git status` confirmed it, showing `AI_USAGE_LOG.md` as `UU`, which means both
sides modified the same file and neither side won automatically.

The cause was deliberate and I knew what it was, because I had created it. Both branches edited the same
single line. `docs/ai-note` changed `Validation status: PENDING` to `Validation status: AI reviewed`, and
`main` changed the identical line to `Validation status: Tests passed`. Git merges by hunk and cannot
choose between two edits to one line, so it wrote both into the file between `<<<<<<< HEAD`, `=======`
and `>>>>>>> docs/ai-note` markers and handed the decision back.

Resolving it meant treating the markers as scaffolding and not as text. I deleted the whole block, both
competing lines and all three marker lines, and wrote the one required line in its place:
`Validation status: AI reviewed and tests passed`. I then grepped the file for any remaining marker to be
certain none survived, since a leftover `=======` would sit in the file as valid Markdown and nothing
would complain. After staging and committing the resolution I re-ran the full suite and all seven tests
still reported `ok`.

The part I want to remember is that the conflict was never the difficult bit. Git told me the file, the
status, and the exact lines. What it could not do was know that both statements were true at once, which
is why the resolution is a sentence containing both rather than a choice between them.
