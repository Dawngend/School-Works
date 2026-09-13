# CS0016 DevNet Resource Validation Plan

## Student and Project

- Name: Dawn Andrei C. Pamesa
- Section: TS31
- Course: CS0016, Network and Communications 2 / IT Specialization 7: Development Network
- Module: Module 2, The DevNet Developer Environment
- Repository name: `cs0016-devnet-resource-plan`

## Purpose

Choosing the right DevNet resource before starting a network-automation task matters because
each resource answers a different question, and picking the wrong one wastes the limited time a
task usually has. An Always-On Sandbox that is grabbed for a configuration test will block the
change or spill it onto other users, while a Reservation Sandbox booked for a simple read-only
API call means waiting for provisioning that was never needed in the first place. Selecting the
resource first, and confirming it against official Cisco documentation, keeps the environment
matched to the actual requirement instead of to whichever option was fastest to reach.

## Validated Resource Decisions

The four selections below come from `student_plan.json`. All four were checked against pages on
`developer.cisco.com` before being written into the plan.

### UC1, Quick read-only API exploration

- **Selected resource:** `always-on-sandbox`
- **Decisive requirement:** the team cannot wait for provisioning, and only needs safe read-only
  requests with no administrative changes.
- **Official evidence:** https://developer.cisco.com/docs/sandbox/
- **Verification status:** verified

A Reservation Sandbox would also have worked on paper, yet it fails the one requirement that
actually decides the case, which is the waiting time.

### UC2, Private configuration testing

- **Selected resource:** `reservation-sandbox`
- **Decisive requirement:** administrative control inside a private environment, with scheduling,
  VPN, and setup time already accepted by the team.
- **Official evidence:** https://developer.cisco.com/docs/sandbox/
- **Verification status:** partially-verified

The resource type held up, however the AI's wording about privileges was broader than what the
documentation supports, so the status was qualified rather than marked verified.

### UC3, Guided API concept practice

- **Selected resource:** `learning-lab`
- **Decisive requirement:** structured, step-by-step content is the immediate need, and the goal
  is guided practice rather than access to administrative devices.
- **Official evidence:** https://developer.cisco.com/learning/
- **Verification status:** partially-verified

A Learning Lab is learning content and is not a substitute for an execution environment, so the
selection is correct only for this stage. A sandbox becomes the right follow-up once the beginner
moves on to the independent activity.

### UC4, Reusable automation example

- **Selected resource:** `code-exchange`
- **Decisive requirement:** existing community and Cisco-maintained repositories have to be
  examined before a new solution is designed, so the need is source code and not a device.
- **Official evidence:** https://developer.cisco.com/codeexchange/
- **Verification status:** rejected

This is the one case where the AI recommendation was replaced entirely. Cisco has also
consolidated Automation Exchange into Code Exchange, so Code Exchange is the correct current term.

Both sandbox decisions cite the same documentation page on purpose, because that page is where
Cisco documents the Always-On and Reservation access models side by side, and the decision
between UC1 and UC2 is precisely a decision between those two models.

## AI Evaluation

**Rejected, UC4.** The AI recommended `always-on-sandbox` and argued it clearly, saying the
developer could start immediately and run the automation code against real devices without a
booking. The reasoning was internally consistent, however it answered a requirement the scenario
never made. UC4 asks for community and Cisco-maintained repositories to be examined *before* a
new solution is designed, which is a request for existing code, not for somewhere to execute it.
The Cisco Code Exchange page documents it as the curated index of exactly those repositories, so
I discarded the recommendation and selected `code-exchange` instead. A sandbox would only matter
later, after a repository is picked and the code has to be reviewed and tested.

**Modified, UC3.** The AI chose `learning-lab`, which was right, but it also claimed the labs
give the learner their own admin-level devices that remain available after the lab finishes. I
could not support that claim, and it contradicts the module's own decision guide, which states
that a Learning Lab is learning content and not a substitute for choosing an execution
environment. I kept the resource type and recorded the status as `partially-verified` rather than
accepting the full answer just because the label was correct.

**Modified, UC2.** The AI chose `reservation-sandbox` correctly, but stated that a reservation
always grants full administrator rights on every device in the pod. Privilege detail is documented
per individual sandbox rather than as one blanket guarantee, so the status was recorded as
`partially-verified`.

**Accepted, UC1.** Every claim the AI raised, meaning no reservation needed, shared rather than
isolated, and limited administrative privileges, matched the documented Always-On access model,
so this one was accepted as `verified`.

The pattern I noticed across all four is that the AI was most convincing exactly where it was
wrong, since the UC4 answer was the best-written one of the set and still solved the wrong problem.

## Validation Evidence

- **Validator result:** VALIDATION COMPLETE: 9/9 checks passed. Full output saved in
  `validator_output.txt`.
- **Command used:** `python validate_plan.py`
- **Official Cisco pages reviewed:**
  - DevNet Sandbox documentation, https://developer.cisco.com/docs/sandbox/
  - DevNet Learning Labs, https://developer.cisco.com/learning/
  - Cisco Code Exchange, https://developer.cisco.com/codeexchange/

No reservation was created, no VPN was connected, no API request was sent, and no sandbox was
modified. All exploration stayed read-only, as required by Section 4 of the activity.

## Git Evidence

- **Initial commit message:** `Set up Module 2 workspace with DevNet starter files and README skeleton`
- **Validation commit message:** `Validate all four DevNet resource decisions against Cisco docs, 9/9 checks passed`
- **Output of `git log --oneline`:**

```
a60491d Validate all four DevNet resource decisions against Cisco docs, 9/9 checks passed
64b86d9 Set up Module 2 workspace with DevNet starter files and README skeleton
```

## AI-Use Disclosure

**Tool used:** Claude (Anthropic).

**Type of assistance received:** The AI was given one prompt per scenario, following the prompt
pattern in Section 8 of the activity sheet. Each prompt asked for exactly one resource type out
of the four allowed labels, the requirement that drove the choice, and any access, isolation,
setup, or privilege claim that I should verify. The full prompts and the reply excerpts are
recorded in `ai_prompt_record.md`.

**What was independently checked:** Every recommendation was treated as provisional until an
official page on `developer.cisco.com` supported it. I opened the DevNet Sandbox documentation
for UC1 and UC2, the Learning Labs page for UC3, and the Code Exchange page for UC4, and I
compared each AI claim against the resource description, the access model, and the intended use
before recording a status.

**What was revised:** Three of the four answers were changed in some way. UC4 was rejected
outright and replaced with `code-exchange`. UC3 and UC2 kept the recommended resource type but
had unsupported privilege claims stripped out, and both were recorded as `partially-verified`
instead of `verified`. Only UC1 survived unchanged. The rationales, the README, and the
reflection answers are my own wording, written after the verification step rather than copied
from the AI replies.

**What was not shared with the AI:** No usernames, passwords, keys, tokens, reservation emails,
private repository content, or personal data were pasted into the tool. Only the fictional
scenarios supplied in `devnet_use_cases.json` were used.

## Note on the course code

The activity handout is written against the generic placeholder code IT0123. The live class code
is CS0016, Network and Communications 2, so this repository and all of my own files use CS0016.
The starter file `devnet_use_cases.json` is left byte for byte as it was supplied, including its
internal `IT0123` course string, so that the provided files remain unmodified.

## Files in this repository

| File | Purpose |
| --- | --- |
| `student_plan.json` | The completed plan with all four validated decisions |
| `README.md` | This file, covering decisions, evidence, Git record, and AI disclosure |
| `ai_prompt_record.md` | Prompt and reply excerpts for each of the four scenarios |
| `reflection.md` | Answers to the four reflection questions in Section 11 |
| `validator_output.txt` | Saved validator output showing 9/9 checks passed |
| `validate_plan.py` | Starter validator, unchanged |
| `devnet_use_cases.json` | Starter scenarios, unchanged |
| `student_plan_template.json` | Starter template, unchanged |
