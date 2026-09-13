# Reflection Questions

## 1. Which scenario was easiest to classify, and which requirement determined your choice?

UC1 was the easiest one to classify. The scenario already gives away the answer in its last
line, which is that the team cannot wait for provisioning. Once that requirement is spotted,
the Reservation Sandbox is eliminated immediately, because reserving a sandbox is a waiting
step by definition. Learning Labs and Code Exchange were never really in the running either,
since the team wants to send actual API requests and not read a tutorial or browse repositories.
That leaves the Always-On Sandbox, and the rest of the scenario supports it too, because shared
access and read-only requests are exactly the conditions an Always-On environment is built for.

## 2. Describe one AI claim that needed correction, qualification, or rejection.

The clearest one was UC4. The AI recommended `always-on-sandbox` and explained it well, saying
that the developer could start immediately and run the automation code against real devices.
The reasoning sounded fine on its own, however it answered a requirement that the scenario
never stated. The scenario asks for community and Cisco-maintained repositories to examine
before designing a new solution, so what is needed is existing code, not a device to run it on.
I rejected the recommendation and selected `code-exchange` instead, based on the Code Exchange
page describing it as a curated index of those repositories.

A second one worth noting is UC3, where the AI got the resource right but attached a claim that
Learning Labs give the learner admin-level devices to keep afterwards. I could not support that,
and it also runs against the module's own warning that a Learning Lab is learning content and
not a substitute for an execution environment, so I recorded it as partially-verified rather
than just accepting the whole answer because the label happened to be correct.

## 3. Why is an Always-On Sandbox not automatically the best option for every API task?

Because the things that make it convenient are the same things that limit it. An Always-On
Sandbox is shared and immediately reachable, which is great when the task is read-only
exploration, yet the sharing is precisely the problem once the task involves configuration.
It is a shared environment with restricted administrative access, so a configuration change
would either be blocked outright or, worse, would land on an environment other people are using
at the same time. There is also no isolation to speak of, which means a test cannot be assumed
to be clean or repeatable, since somebody else may be working in the same place. For anything
that needs administrative control, a private environment, or a predictable starting state, the
Reservation Sandbox is the correct choice even though it costs scheduling and setup time.

I realized while doing this that "fastest to access" and "most appropriate" are two different
questions, and the second one is the one being graded.

## 4. How did Git improve the traceability of your resource-selection process?

Git made the process reviewable instead of just the final answer being reviewable. The first
commit captured the workspace before any decision existed, and the validation commit captured
the finished plan together with the validator output, so the two states can be compared and it
is visible what was actually decided at which point rather than only what the file looks like
now. Because the prompt record and the verification statuses are committed alongside the plan,
anyone checking the work can see which AI claims were accepted, which were qualified, and which
one was thrown out, and they can see that the rejection happened before the plan was validated
and not afterwards as a cleanup.

To conclude, the commits turn the plan from a single submitted file into a record that shows
the order the work was done in, which is the part that matters when the requirement is to prove
that an AI recommendation was verified and not just copied.
