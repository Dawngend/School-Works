# AI Usage and Validation Log

Student name: Dawn Andrei C. Pamesa
Section: TS31
Course: CS0016, Network and Communications 2 / IT Specialization 7: Development Network
Module: Module 3, AI-Assisted Git Workflow and Python Data Parsing
AI tool used: Claude Code (Anthropic), agentic CLI

## Pre-AI predictions (Task 3)

Written after reading `network_config.xml`, `devices.json` and `maintenance.yaml` directly, and
before sending any prompt about the implementation.

### XML, `network_config.xml`

The default namespace is `urn:ietf:params:xml:ns:netconf:base:1.0`, declared as an unprefixed
`xmlns` attribute on the root `<rpc>` element. An unprefixed declaration applies to that element
and to every descendant that does not override it, so `<edit-config>`, `<default-operation>` and
`<test-option>` are all in the NETCONF namespace even though none of them names it.

- `<edit-config>` is the only child of `<rpc>`.
- `default-operation` should read `merge`.
- `test-option` should read `test-then-set`.
- Both come back as `str`, since ElementTree does no type coercion on element text.

The part I expect to cause trouble is that there is a *second* default namespace further down.
`<interface xmlns="urn:example:network">` inside `<config>` re-declares the default for its own
subtree, so `<name>` and `<enabled>` belong to `urn:example:network` and not to NETCONF. Any
approach that strips namespaces globally to make the lookup easier would flatten two genuinely
different namespaces into one, which is wrong even though this particular file is small enough
that it would still return the right two strings.

ElementTree expands every tag into Clark notation, so the element I actually need is
`{urn:ietf:params:xml:ns:netconf:base:1.0}default-operation`. I predict `root.find("default-operation")`
returns `None` and `root.findall(".//default-operation")` returns an empty list, because neither
matches the expanded name.

### JSON, `devices.json`

Two top-level keys, `site` and `devices`. `site` is `"FEU-Tech-Lab"`. `devices` is a list of three
objects, each carrying the same four fields: `hostname`, `management_ip`, `role`, `enabled`.

- `enabled` is a JSON boolean, so `json.load` yields Python `True` and `False` rather than the
  strings `"true"` and `"false"`. R1 and SW1 are `True`, AP1 is `False`.
- `device_count` should be `3`, taken from `len()` of the list rather than an incrementing counter.
- `enabled_devices` should be `["R1", "SW1"]`.
- `roles` should be `["router", "switch", "wireless-ap"]`.

One thing this fixture cannot settle: order of first appearance and alphabetical order produce the
identical `roles` list here, so the data gives me no way to tell which one the docstring wants, and
both would pass. I will preserve order of first appearance, because sorting would be an assumption
the docstring never makes. The three roles are also all distinct, so a missing de-duplication step
would go unnoticed by this data even though it would still be a defect.

### YAML, `maintenance.yaml`

`yaml.safe_load` should return a dict with three top-level keys: `window`, `devices` and `action`.

- `window` is a nested mapping, so its values sit one level down rather than at the top.
- `window["name"]` is `"Saturday-Lab"` as `str`. It is unquoted in the file, yet YAML resolves it to
  a string because it is neither a number nor a boolean.
- `window["approved"]` is Python `True` as `bool`. The test compares against `True`, so a `"true"`
  string would fail it.
- `window["duration_minutes"]` is `90` as `int`, so no conversion is needed.
- `devices` is `["R1", "SW1"]` and it is top-level, not inside `window`.
- `action` is `"validate-configuration"` as `str`. The hyphens do not make it anything else.

The quiet trap here is that the YAML `devices` list and the JSON `enabled_devices` list both hold
`["R1", "SW1"]`, from two unrelated files. `test_combined_summary` asserts on
`result["yaml"]["devices"]`, so feeding the JSON value into the YAML slot would still pass every
test in the suite. I expect that to be the easiest silent defect in this lab.

### Combined summary

`build_summary` should return exactly the keys `xml`, `json` and `yaml`. The test compares
`set(result)` for equality rather than checking membership, so adding anything extra, a timestamp
or a source path for instance, fails it.

I expect seven tests to run, and I expect all seven to fail with `NotImplementedError` before any
implementation exists.

## Entry 1 - XML parsing

Prompt:

> I am completing an authorized classroom Python lab.
> Review this function stub and the supplied fictional XML structure.
> Recommend an implementation that returns exactly the keys described in the docstring.
> Explain namespace handling, data types, error risks, and each library function used.
> Do not invent files, credentials, network calls, or expected test results.
> I will validate your recommendation using unit tests and Git diffs.
> Function stub:
> `def parse_xml(path: str | Path) -> dict:` with the docstring "Return default_operation and
> test_option from the NETCONF-style XML."
> Relevant fictional data: the supplied `network_config.xml`, pasted in full and unmodified.

AI recommendation summary:

Bind the NETCONF namespace URI to a local prefix in a dictionary and pass that dictionary as the
second argument to `find`, because ElementTree matches on the expanded `{namespace}tag` form and an
unprefixed default namespace cannot be searched for unless it is bound to something first. Walk down
through `edit-config` rather than searching from the root with `.//`, so the two values are read from
the element that actually contains them instead of from anywhere in the document. Read `.text` off
each result and return the two strings. The reply also flagged that `<interface>` re-declares a
different default namespace over its own subtree, and that stripping namespaces globally would erase
that distinction.

Decision: modified

The namespace handling was correct and I kept it exactly as recommended. What I changed was the error
behavior. The recommendation read `.text` straight off the result of `find`, and `find` returns `None`
when nothing matches, so a missing or renamed element fails with
`AttributeError: 'NoneType' object has no attribute 'text'`. That names a Python type rather than the
element that was actually missing, which is the least useful thing to be told. I moved the lookup into
a `_required_text` helper that checks for `None` twice, once for an element that is absent and once for
an element that exists but carries no text, and raises a `ValueError` naming the path it was searching
for. The prompt asked for error risks specifically, and this was the one risk the reply did not cover.

Validation evidence:

- I tested four lookup approaches against the real file before implementing anything. A named prefix,
  Clark notation, and an empty-string prefix map all resolve correctly. The empty-string form has
  worked since Python 3.8, which corrected an assumption I had carried into the activity.
- The global tag-stripping shortcut does return the correct two strings on this file, because no local
  name appears in both namespaces. I rejected it regardless, for the reason already recorded in my
  predictions, which is that it merges two vocabularies the file deliberately keeps apart.
- `test_xml_default_operation` and `test_xml_test_option` both report `ok`.
- Error path checked directly. I built an `<edit-config/>` with no children and confirmed the output is
  `ValueError: required NETCONF element 'nc:default-operation' is missing` rather than the
  `AttributeError`.
- Predictions confirmed. `default-operation` is `merge`, `test-option` is `test-then-set`, and both come
  back as `str`.

## Entry 2 - JSON parsing

Prompt:

> I am completing an authorized classroom Python lab.
> Review this function stub and the supplied fictional JSON structure.
> Recommend an implementation that returns exactly the keys described in the docstring.
> Explain namespace handling, data types, error risks, and each library function used.
> Do not invent files, credentials, network calls, or expected test results.
> I will validate your recommendation using unit tests and Git diffs.
> Function stub:
> `def parse_json(path: str | Path) -> dict:` with the docstring "Return site, device_count,
> enabled_devices, and roles from the JSON."
> Relevant fictional data: the supplied `devices.json`, pasted in full and unmodified.

AI recommendation summary:

Open the file inside a `with` block and call `json.load` on the handle, which maps the JSON object to a
dict, the array to a list, and the JSON booleans to real Python `True` and `False` rather than to the
strings `"true"` and `"false"`. Take `site` straight off the top level. Take `device_count` from `len()`
of the device list instead of counting in a loop. Build `enabled_devices` with a list comprehension
filtered on the `enabled` flag. For `roles`, de-duplicate with a set, since a set removes repeats in one
step and roles could repeat in a larger inventory.

Decision: modified

Everything except the `roles` line was correct and I kept it. The set is where I disagreed. A set does
de-duplicate, however it has no defined iteration order, and CPython randomizes string hashing per
process unless `PYTHONHASHSEED` is fixed, so the order that comes out of it changes between runs. The
list that `test_json_roles` compares against is order-sensitive, so that construct does not produce a
test that passes or fails on merit. It produces a test that passes sometimes. I replaced it with
`dict.fromkeys`, which de-duplicates the same way but keeps order of first appearance, because
dictionaries have preserved insertion order since Python 3.7.

I considered `sorted(set(...))`, which is also deterministic and also passes. I did not use it, for the
reason recorded in my predictions: the docstring asks for `roles` and never asks for sorted roles, and
in this file the file order and the alphabetical order are identical, so sorting would be an assumption
that this data cannot justify and that a future inventory could break.

Validation evidence:

- I ran `list(set(roles))` under six different values of `PYTHONHASHSEED`. It produced the order the test
  expects in one run out of six, and a different order in the other five. That is the measurement the
  decision rests on, rather than my opinion about sets.
- I re-ran the finished implementation under the same six seeds. It returned
  `['router', 'switch', 'wireless-ap']` every time.
- `test_json_device_count`, `test_json_enabled_devices` and `test_json_roles` all report `ok`.
- Predictions confirmed. Two top-level keys, three device objects, `enabled` arriving as `bool` for all
  three devices, `device_count` of 3, and `enabled_devices` of `["R1", "SW1"]`.
- The gap I predicted is still real. All three roles in this file are distinct, so the de-duplication step
  is never actually exercised by the supplied data. It is correct, and this fixture does not prove it.

## Entry 3 - YAML parsing and integration

Prompt:

> I am completing an authorized classroom Python lab.
> Review this function stub and the supplied fictional YAML structure.
> Recommend an implementation that returns exactly the keys described in the docstring.
> Explain namespace handling, data types, error risks, and each library function used.
> Do not invent files, credentials, network calls, or expected test results.
> I will validate your recommendation using unit tests and Git diffs.
> Function stub:
> `def parse_yaml(path: str | Path) -> dict:` with the docstring "Return name, approved,
> duration_minutes, devices, and action from YAML.", followed by the `build_summary` stub.
> Relevant fictional data: the supplied `maintenance.yaml`, pasted in full and unmodified.

AI recommendation summary:

Use `yaml.safe_load` rather than `yaml.load`, because the safe loader resolves only standard YAML tags
and cannot be made to construct arbitrary Python objects from the document. The loader returns a plain
dict, and the flattening is the only real work: `window` is a nested mapping so its three values need one
more level of indexing, while `devices` and `action` sit at the top level and do not. YAML resolves the
scalars by shape rather than by quoting, so `true` becomes a `bool`, `90` becomes an `int`, and the
unquoted `Saturday-Lab` and `validate-configuration` stay `str` because neither matches a number or a
boolean pattern. For `build_summary`, call the three parsers and nest each result under `xml`, `json` and
`yaml`, returning nothing else, since the test compares the key set for equality rather than membership.

Decision: modified

The parsing approach was correct and I kept all of it. I made one defensive change rather than a
correction: the recommendation returned `data["devices"]` directly, which hands the caller the same list
object the parsed document holds, so anything that mutates the returned summary also mutates the parsed
document. I return `list(data["devices"])` instead. This is hardening, not a bug fix, and I am labelling
the entry modified rather than accepted because what I committed is not what was recommended verbatim.

Validation evidence:

- Every predicted type came back as predicted: `name` as `str`, `approved` as `bool` `True`,
  `duration_minutes` as `int` `90`, `devices` as a `list`, and `action` as `str`. Nothing needed
  converting.
- `test_yaml_window` and `test_combined_summary` both report `ok`, and the full suite is 7 of 7.
- The trap I predicted is real, and I measured it instead of assuming it. I took a throwaway copy of the
  project, deliberately rewired `build_summary` so that the YAML `devices` value was sourced from the
  JSON `enabled_devices` field, and ran the suite. All seven tests still reported `ok`. The two lists
  both hold `["R1", "SW1"]` by coincidence, so the supplied tests cannot tell the two sources apart.
- That result is the reason `build_summary` carries a comment naming the coincidence, and the reason I
  checked the parser output field by field against the three source files by hand rather than treating a
  green suite as proof. The throwaway copy was deleted after the check and never entered the repository.

## Controlled merge-conflict line

Validation status: AI reviewed and tests passed

## Final reflection

The suggestion I changed was the set-based de-duplication of `roles` in `parse_json`. It was a reasonable
recommendation and it would have passed on the machine I wrote it on, which is exactly what makes it worth
writing up.

A set removes duplicates in one step, so reaching for it is the natural instinct, and the reply gave a
sound reason for it: roles could repeat in a larger inventory. What the reply did not account for is that
`test_json_roles` compares against an ordered list while a set has no defined iteration order. CPython
randomizes string hashing per process, so the order a set yields is not stable between runs.

The evidence was a measurement, not an argument. I ran `list(set(roles))` under six different values of
`PYTHONHASHSEED` and it produced the order the test expects in one run out of six. Five runs produced a
different order. A construct that passes one time in six is not a correct implementation that occasionally
misbehaves, it is an incorrect implementation that occasionally agrees with the answer, and it would have
failed on whichever machine hashed differently from mine. I replaced it with `dict.fromkeys`, which
de-duplicates while preserving order of first appearance, and re-ran the finished implementation under the
same six seeds to confirm it returned the same list every time.

The wider lesson from this lab is the same one twice. The set was wrong in a way that looked right six
times out of ten, and the deliberate wrong-file defect I planted in `build_summary` was wrong in a way the
entire test suite could not see. Both would have shipped on the strength of a green run. What caught them
was deciding in advance what the data should contain, and then checking the result against the files
rather than against the tests.
