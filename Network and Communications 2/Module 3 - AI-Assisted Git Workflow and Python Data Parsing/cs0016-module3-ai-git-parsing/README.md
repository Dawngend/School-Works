# AI-Assisted Git Workflow and Python Data Parsing

Student name: Dawn Andrei C. Pamesa
Section: TS31
Course: CS0016, Network and Communications 2 / IT Specialization 7: Development Network
Module: Module 3, AI-Assisted Git Workflow and Python Data Parsing
Repository name: `cs0016-module3-ai-git-parsing`

## Project purpose

This repository reads fictional network data out of three different formats and combines the results
into one dictionary, and it does that under a complete local Git workflow rather than as a single
finished file. The two halves are the point. `parser_template.py` handles a NETCONF-style XML request,
a JSON device inventory, and a YAML maintenance window, which are the three shapes network data
actually arrives in, and each one fails differently when it is read carelessly. The Git side records
the order the work happened in, so the baseline, each parser, the branch, the merge, and the resolved
conflict are all separately visible instead of being flattened into whatever the files look like at the
end. Every AI recommendation in this lab was treated as provisional until the supplied tests and a
manual comparison against the source files agreed with it.

## How to run

```bash
python3 parser_template.py
python3 -m unittest -v
```

`parser_template.py` prints the combined summary as indented JSON. The test run reports seven tests.

## Git workflow summary

Three branches were used:

- `main` holds the starter baseline, the integrated parsers, and the resolved conflict.
- `feature/data-parsers` holds the parser development work.
- `docs/ai-note` exists only to create the controlled conflict required by Task 7.

The commits, in the order they were made:

1. `chore: add parser lab starter files` establishes the baseline with the working tree clean.
2. `docs: record pre-AI predictions for the XML, JSON, and YAML formats` records what I expected each
   file to contain, committed before any implementation existed so the later decisions have something
   independent to be judged against.
3. `feat: parse NETCONF XML with explicit default-namespace binding`
4. `feat: derive device summary from JSON with order-stable role de-duplication`
5. `feat: parse maintenance YAML with safe_load and integrate build_summary`
6. `docs: record test validation status` on `main`, and `docs: record AI review status` on
   `docs/ai-note`, which are the two conflicting edits.
7. `merge: reconcile AI and test validation notes` resolves the conflict.
8. `docs: finalize validated lab evidence` adds this file, the reflection answers, and the exported
   evidence.

Commit hashes are not repeated here, because they would go stale the moment anything is amended. The
authoritative graph is in `git_history.txt`.

`git_history.txt` and `git_status.txt` were produced by the Task 8 commands, which run immediately before
the final documentation commit. That last commit is therefore the one entry they cannot contain, and
`git_status.txt` shows the evidence files as untracked because they had just been written and not yet
staged. No file can record the hash of the commit that contains it, so this is a property of the capture
order rather than an omission. Everything up to and including the conflict resolution is complete, and
running `git log --oneline --graph --decorate --all` on the submitted repository reproduces the full graph.

One detail worth naming. Merging `feature/data-parsers` into `main` produced a **fast-forward** rather
than a merge commit, because `main` had not received any commit of its own since the branch was created,
so Git could simply move the branch pointer forward. The Task 7 merge behaved differently and did create
a merge commit, because by then `main` and `docs/ai-note` had each committed a change the other did not
have, which is what divergence means and what a merge commit records. Both are in `git_history.txt`, and
the difference between them is visible in the graph.

### The controlled conflict

`docs/ai-note` changed the line `Validation status: PENDING` in `AI_USAGE_LOG.md` to
`Validation status: AI reviewed`. `main` changed the same line to `Validation status: Tests passed`.
Merging the branch produced `CONFLICT (content): Merge conflict in AI_USAGE_LOG.md`, and `git status`
reported the file as `UU`, meaning both sides modified it. Git wrote the two competing versions into the
file separated by `<<<<<<<`, `=======` and `>>>>>>>` markers. I removed the markers and both partial
lines and replaced the whole block with the single required line:

```
Validation status: AI reviewed and tests passed
```

The file was then staged, committed as the merge resolution, and all seven tests were re-run and still
reported `ok`, which confirms the resolution did not damage anything else in the repository.

## Parser results

All values below were read back from `python3 parser_template.py` and then checked line by line against
the three source files.

**XML, from `network_config.xml`.** `default_operation` is `merge` and `test_option` is
`test-then-set`, both as `str`. Both elements sit under `<edit-config>` and both inherit the unprefixed
default namespace `urn:ietf:params:xml:ns:netconf:base:1.0` declared on the root `<rpc>` element. The
file also re-declares a second, different default namespace, `urn:example:network`, on the nested
`<interface>` element, so the two vocabularies are kept apart in the implementation rather than
flattened.

**JSON, from `devices.json`.** `site` is `FEU-Tech-Lab`, `device_count` is `3`, `enabled_devices` is
`["R1", "SW1"]`, and `roles` is `["router", "switch", "wireless-ap"]`. The `enabled` field arrives as a
real Python `bool`, so AP1 is excluded by its value rather than by a string comparison.

**YAML, from `maintenance.yaml`.** `name` is `Saturday-Lab` as `str`, `approved` is `True` as `bool`,
`duration_minutes` is `90` as `int`, `devices` is `["R1", "SW1"]`, and `action` is
`validate-configuration`. The `window` mapping is nested while `devices` and `action` are top level, and
YAML resolved every scalar by shape without any conversion being needed.

**Combined.** `build_summary` returns exactly the keys `xml`, `json` and `yaml`.

## AI disclosure

**Tool used:** Claude Code (Anthropic), an agentic command-line assistant. Three separate prompts were
sent, one per format, using the prompt pattern in Task 4 of the manual. The full prompts, the summarized
recommendations, the accept or modify decisions, and the evidence behind each are recorded in
`AI_USAGE_LOG.md`.

All three recommendations were **modified** rather than accepted as written, and each modification is
backed by something I measured rather than by a preference:

- **XML.** The namespace handling was right and I kept it. The error handling was not covered, so I
  replaced a bare `.text` read with a helper that raises a `ValueError` naming the missing element,
  instead of the `AttributeError: 'NoneType' object has no attribute 'text'` that the original would
  have produced.
- **JSON.** The recommendation de-duplicated `roles` with a set. I ran that construct under six
  different values of `PYTHONHASHSEED` and it produced the expected order in one run out of six, because
  CPython randomizes string hashing per process and sets have no defined iteration order. I replaced it
  with `dict.fromkeys`, which de-duplicates and keeps order of first appearance.
- **YAML.** The parsing was correct. I changed one line to return a copy of the device list rather than
  the list object held by the parsed document, so that a caller mutating the summary cannot reach back
  into the parsed file.

The single most useful thing I did was not a code change. I built a throwaway copy of the project,
deliberately sourced the YAML `devices` value from the JSON `enabled_devices` field, and ran the suite.
All seven tests still passed, because the two lists happen to hold the same two hostnames. That is
recorded in full in `AI_USAGE_LOG.md` and it is why the parser output was checked field by field against
the source files rather than being signed off on a green test run.

## Safety statement

Only the fictional classroom data supplied with this activity was used. `network_config.xml`,
`devices.json` and `maintenance.yaml` were sent to the AI tool exactly as provided and were never
modified. The JSON file uses documentation-range addresses from `192.0.2.0/24`, which RFC 5737 reserves
for exactly this purpose, and no address in this repository refers to a real device.

No password, access token, API key, SSH key, private repository content, institutional secret or
personal data was entered into the AI tool at any point. No network connection is opened by any code in
this repository, and nothing here contacts a real device. The Git identity configured for this
repository is local to it, uses an `example.com` address as the manual requires, and my real email
address does not appear in the working tree or in the commit history. No destructive Git command was
used at any point.

## Note on the course code

The manual is written against the generic placeholder code `IT0123`. The live class code is `CS0016`,
Network and Communications 2, so this repository and all of my own files use `CS0016`, which is the same
convention I used for the Module 2 submission. The supplied starter files are left byte for byte as they
were given, including any internal course string, so that the provided files remain unmodified.

## Files in this repository

| File | Purpose |
| --- | --- |
| `parser_template.py` | The four completed parser functions |
| `test_parser.py` | Supplied test suite, unchanged |
| `network_config.xml` | Supplied fictional NETCONF request, unchanged |
| `devices.json` | Supplied fictional device inventory, unchanged |
| `maintenance.yaml` | Supplied fictional maintenance window, unchanged |
| `README.md` | This file |
| `AI_USAGE_LOG.md` | Predictions, three prompt records, decisions, and the final reflection |
| `reflection.md` | Answers to the four reflection questions in section 8 |
| `test_output.txt` | Saved run showing seven passing tests |
| `git_history.txt` | Saved branch graph across all branches |
| `git_status.txt` | Saved final repository state |
| `.gitignore` | Supplied, unchanged |
