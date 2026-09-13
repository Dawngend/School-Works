# AI Prompt Record

Tool used: Claude (Anthropic). Four separate prompts were sent, one per scenario, using
the prompt pattern suggested in Section 8 of the activity sheet. No account names, emails,
reservation details, keys, or personal data were pasted into the tool at any point. Only
the fictional scenarios that came with `devnet_use_cases.json` were used.

The excerpts below are shortened. I kept the part of each answer that contains the actual
recommendation and the claim I was supposed to go and verify.

---

## UC1 - Quick read-only API exploration

**Prompt sent**

> I am selecting a Cisco DevNet resource for a fictional classroom use case.
> Use case: A student team needs immediate access to a shared Cisco environment to practice
> safe read-only API requests. Administrative changes are not required, and the team cannot
> wait for provisioning.
> Choose exactly one: learning-lab, always-on-sandbox, reservation-sandbox, or code-exchange.
> Explain which requirement drove your choice. State any access, isolation, setup, or
> privilege claim that I should verify in official Cisco documentation. Do not invent a
> sandbox product name, URL, account, or credential.

**Reply excerpt**

> Recommendation: always-on-sandbox. The driving requirement is that the team cannot wait for
> provisioning. Always-On sandboxes are shared and are available continuously, so no
> reservation step is involved. Claims to verify: that Always-On sandboxes require no
> reservation, that they are shared rather than isolated, and that administrative privileges
> are limited compared to a reserved environment.

**What I checked:** DevNet Sandbox documentation page. All three claims lined up with how
Cisco describes the Always-On access model.

**Outcome:** Accepted. Status recorded as `verified`.

---

## UC2 - Private configuration testing

**Prompt sent**

> Same prompt pattern as above, with the UC2 scenario pasted in: A development team must test
> configuration changes with administrative access in a private environment. The team can
> schedule access, use a VPN, and accept setup time.

**Reply excerpt**

> Recommendation: reservation-sandbox. The driving requirement is administrative access inside
> a private environment, which a shared Always-On sandbox cannot provide. When you reserve a
> sandbox you always receive full administrator rights on every device in the pod for the whole
> duration of the booking. Claims to verify: reservation requirement, VPN access, setup time,
> and the privilege level.

**What I checked:** DevNet Sandbox documentation page, specifically the description of the
reservation access model against the Always-On one.

**Outcome:** Modified. The resource type was right, but I could not confirm the blanket
"always full administrator rights on every device" wording, because privilege detail is
documented per individual sandbox instead of as one guarantee that covers all of them. I kept
`reservation-sandbox` and recorded the status as `partially-verified` so the overstated part
is not carried into the plan as if it were verified.

---

## UC3 - Guided API concept practice

**Prompt sent**

> Same prompt pattern, with the UC3 scenario pasted in: A beginner needs structured,
> step-by-step learning content before attempting an independent API activity. The immediate
> goal is guided practice rather than access to administrative devices.

**Reply excerpt**

> Recommendation: learning-lab. The driving requirement is structured step-by-step content.
> DevNet Learning Labs are built as guided modules for exactly this stage. They also provide
> the learner with their own admin-level devices that stay available after the lab is finished,
> so no separate environment is needed afterwards. Claims to verify: guided format, beginner
> orientation, and the device access described above.

**What I checked:** DevNet Learning Labs page, plus the resource decision guide in the module
handout.

**Outcome:** Modified. The guided-content part held up, but the claim about keeping admin-level
devices after the lab did not, and it also contradicts the module's own warning that a Learning
Lab is learning content and is not a substitute for choosing an execution environment. I kept
`learning-lab` because the scenario is specific that the immediate goal is guided practice, and
recorded the status as `partially-verified`.

---

## UC4 - Reusable automation example

**Prompt sent**

> Same prompt pattern, with the UC4 scenario pasted in: A developer wants to examine community
> and Cisco-maintained code repositories for an existing network-automation use case before
> designing a new solution.

**Reply excerpt**

> Recommendation: always-on-sandbox. The developer will want to try the automation code against
> real devices, and an Always-On sandbox lets them start immediately without a booking. Claims
> to verify: immediate availability and suitability for running automation scripts.

**What I checked:** Cisco Code Exchange page, then re-read the scenario wording.

**Outcome:** Rejected. The scenario never asks for an execution environment. It asks for
existing repositories to examine before a new solution is designed, and Code Exchange is
documented as the curated index of community and Cisco-maintained repositories. I replaced the
recommendation with `code-exchange` and recorded the status as `rejected`. This one is the
clearest example of why an AI answer stays provisional until it is checked, because the
recommendation was confidently worded and still solved the wrong requirement.
