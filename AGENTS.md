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

Apply the same evidence check to intermediate updates. Bind a material claim to
its source, observation date, exact target or candidate, environment and stage.
Keep retrieval outcomes separate from product outcomes: a failed lookup does
not establish an outage, missing capability, zero activity or a completed
cancellation. Use source indexes or search to discover paths; reread relevant
truncated sections before interpreting them. Distinguish failed, untested,
indeterminate, access blocked, pending review and not applicable.

When a cause remains uncertain, preserve the symptom, competing explanations
and next discriminating check. Do not turn a plausible explanation into a
verified cause to complete a report. After an ambiguous mutating operation,
reconcile its identity and resulting state before retrying; continue independent
authorized work while the affected outcome remains unresolved.

Retain unresolved consequential operations across restarts and account changes
under the owning contract. A timer, empty history or restarted process does not
establish cancellation. Use the [synthetic evidence-recovery cases](evals/engineering/evidence-recovery/README.md)
to evaluate this guidance with expected judgments withheld.

These are repository reporting instructions, not installed skill behavior.
Use only public or cleared evidence here; private project decisions, reports and
receipts stay in their owning project. Changing these instructions does not
release a plugin, alter a package version or update a consuming project's pin.

## Toolkit production-quality acceptance

For material guidance changes, state the intended user task and the scope that
would justify acceptance. Extend existing skills and use synthetic or cleared
evaluations. When the change concerns rendered experience judgment, inspect
actual renders and relevant interactions; a text scenario or structural pass
alone cannot establish that behavior. Give independent evaluators input-only
cases and retain complete answers, exact input/skill identities, tools, evidence
and limits before assessing against held-out criteria. Use the existing
[production-acceptance method](plugins/design/skills/experience-review/references/production-acceptance.md)
and [toolkit audit](docs/quality-audit-20261028.md) proportionally; do not impose
visual or game review on unrelated changes. Record source review, behavior
acceptance and package-release authorization separately. Hold unresolved
required release gates without erasing previous public releases.

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

## Cloud execution when feasible

For repository work, prefer the existing authorized cloud computer and connected
tools. If it cannot satisfy a specific dependency, check another already
available, authorized cloud environment before using an authorized local
computer for that step. Check actual toolchains, runtime, network access,
provider access and signing requirements; a supported cloud Mac can satisfy a
macOS requirement. A platform requirement alone does not require the owner's Mac.

Keep environment selection within existing authority. Do not provision paid
infrastructure, broaden permissions, transfer sensitive credentials or change
security controls to make a task run. The macOS Keychain runner remains a
specific implementation with native access requirements, not a default for all
automation. Its portable synthetic tests do not establish live Keychain access.

Record the selected environment, capability evidence and its date, exact
commands/results, and verified limits separately from assumptions or untested
alternatives. If a capability is conclusively unavailable, do not repeat the
attempt without materially new evidence. Isolate the smallest dependent step;
continue independent cloud preparation and record its completed work, blocker,
required environment or owner, and next executable action in the handoff.
A policy change or hosted check does not prove all agents adopted this choice.

## Portable handoff and release evidence

Start from the current default branch and record its exact revision and working-tree state; preserve existing changes. Read [README.md](README.md), [HANDOFF.md](HANDOFF.md), and [CHANGELOG.md](CHANGELOG.md) before changing source or claiming release state. Dated checkpoints are evidence to recheck, not proof of current external state. Changes on main are unreleased source until a separately reviewed tag and release; installed consumers keep their explicit pins.

For material work, update the repository handoff in the same PR with reproducible setup and check commands, exact source and reviewed head, actual test results, artifact inventory, deployed and live revision/time where applicable, missing evidence, remaining gates, and the next action. Keep it usable from a fresh clone: credentials, private captures or data, ignored files, absolute machine paths, browser sessions, and local automations do not travel with Git.

Use a focused branch and PR, independent review of its exact head, and required checks before merge. Identify an agent review as such; obey any stricter reviewer-identity rule. Source merge, built artifact, provider deployment, and live readback are separate states. Follow the owning release runbook with one release owner, verify a fresh artifact and exact live result where applicable, and hold unresolved gates. For reusable lessons from product work, contribute only generic, synthetic examples through a separate reviewed PR. Preserve published tags and explicit consumer pins unless their owners separately review an update.
