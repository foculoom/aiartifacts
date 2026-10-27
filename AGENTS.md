# Contributor instructions

## Planning and status reports

Apply this section to planning, progress/status reports and their final summaries
or delegated handoffs. Start with [HANDOFF.md](HANDOFF.md), then the owning
release record and its exact tag or revision; use [CHANGELOG.md](CHANGELOG.md)
to distinguish released artifacts from source candidates. Compare dates,
revisions and merge state before using older checkpoints. Resolve conflicting
records through the current project owner; historical messages do not supply
missing current authority.

For each material outcome in scope, carry forward the achieved milestone,
its date and evidence, what it means for the goal or next decision, the remaining
or unknown state, and the next action. Keep source changes, channel approval,
public availability and qualifying receipts separate; one does not establish
another.

Before classifying scope, inspect the relevant current owner decision evidence,
including requirements and handoffs in current PRs. Documented owner approval
can coexist with an unmerged implementation; report those facts separately.
An open PR alone establishes neither owner approval nor lack of approval.
A newer proposal does not replace adopted scope.

For each material channel, explicitly state whether users can acquire, download
or use the product, with the evidence date and any uncertainty. Do not leave
present availability implicit in a future release action. Distinguish a public
listing or preview from the availability of the product itself.

If live access is unavailable, retain the last verified achievement with its
date and source, state what cannot currently be rechecked, and identify the next
verification. Do not erase a completed milestone or report it as still pending
because a later stage or fresh readback is unavailable. Use newer authoritative
evidence to supersede earlier records, preserving the historical scope.

Before sending a final status summary or a delegated planning/status handoff,
check coverage against the material outcomes requested: include achieved
milestones as well as remaining work, evidence dates and limits, and the next
action. Keep this proportional to the request; it adds no separate ceremony to
routine coding tasks.

These are repository reporting instructions, not installed skill behavior.
Use only public or cleared evidence here; private project decisions, reports and
receipts stay in their owning project. Changing these instructions does not
release a plugin, alter a package version or update a consuming project's pin.

## Engineering incident learning

For a material engineering failure or near miss, use the
[engineering retrospective template](templates/engineering-retrospective.md)
in the owning repository. Record dated impact, verified causes separately from
hypotheses, the detection gap, recovery, and actions with owners and verification.
Keep routine review fixes and owner-directed design iteration proportional; they
do not each require an incident report. Contribute a reusable lesson here only
as a separate reviewed change with synthetic
[behavior cases](evals/engineering/incident-learning.md). Do not copy private
receipts or customer data into this public repository.

## Portable handoff and release evidence

Start from the current default branch and record its exact revision and working-tree state; preserve existing changes. Read [README.md](README.md), [HANDOFF.md](HANDOFF.md), and [CHANGELOG.md](CHANGELOG.md) before changing source or claiming release state. Dated checkpoints are evidence to recheck, not proof of current external state. Changes on main are unreleased source until a separately reviewed tag and release; installed consumers keep their explicit pins.

For material work, update the repository handoff in the same PR with reproducible setup and check commands, exact source and reviewed head, actual test results, artifact inventory, deployed and live revision/time where applicable, missing evidence, remaining gates, and the next action. Keep it usable from a fresh clone: credentials, private captures or data, ignored files, absolute machine paths, browser sessions, and local automations do not travel with Git.

Use a focused branch and PR, independent review of its exact head, and required checks before merge. Identify an agent review as such; obey any stricter reviewer-identity rule. Source merge, built artifact, provider deployment, and live readback are separate states. Follow the owning release runbook with one release owner, verify a fresh artifact and exact live result where applicable, and hold unresolved gates. For reusable lessons from product work, contribute only generic, synthetic examples through a separate reviewed PR. Preserve published tags and explicit consumer pins unless their owners separately review an update.
