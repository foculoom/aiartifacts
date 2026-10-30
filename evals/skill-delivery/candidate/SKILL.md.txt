---
name: skill-delivery
description: Author, evaluate, and package reusable agent skills, or prepare their distribution through awesome-copilot and skills.sh. Use when creating or adapting a skill or checking its release readiness. Do not use for routine app changes, ordinary prose editing, or publishing a customer's product.
license: Apache-2.0
---

# Skill delivery

Produce the smallest useful skill and a reviewable distribution candidate.
Reuse the repository's authoring, validation, evaluation, and release tools.
This workflow prepares evidence; it does not authorize installation, submission,
publication, purchases, permission changes, or updating consumers' pins.

## Establish the task

Read the target repository's instructions, current handoff, existing skills,
tests, and release workflow. Confirm the actual owner, repository, paths and
source revision. Inspect relevant pending owner decisions before calling work
out of scope. Preserve existing work and published artifacts.

Resolve these inputs from the request and repository before asking for more:

- The repeated task, intended users, useful output, and requests that should
  not activate the skill; one real workflow and cleared example inputs.
- Canonical source, target ecosystems and agent runtimes, permitted files and
  side effects, and the available tools, access, time and evaluation budget.
- Publication rights, license and attribution, required dependencies, and the
  owner of each remaining review or release decision.

If an existing skill or template already solves the task, improve or reuse it.
Create new instructions only for a demonstrated gap; do not duplicate general
model capabilities or introduce a framework to deliver one skill.

## Author once

Keep a canonical skill directory with `SKILL.md`, required `name` and
`description`, and only useful supporting resources. Make the description
discriminate real activation from nearby unrelated tasks. Keep the body focused
on decisions the agent would otherwise get wrong. Use relative references and
progressive disclosure; reuse an available initializer when it helps.

Retain shared instructions across targets. Add an adapter only for an observed
format, installation, or runtime difference; do not create separate prose forks
for directory listings. Preserve applicable upstream notices and record sources
and modifications. Do not change a license merely to fit a submission route.

Declare required versus optional tools, language/OS versions, network access,
credentials, permissions, and how to proceed when each is absent. Put portable
environment requirements in `compatibility` when useful and explain practical
dependencies in a bundled reference. Optional client metadata is not a portable
dependency installer. Avoid broad shell preapproval in `allowed-tools`.

Prefer an already authorized cloud environment for portable checks. Keep
provider-specific tool names or native capabilities at the smallest boundary.
If access is missing, complete independent local preparation, report the exact
unperformed check, and stop that dependent step without broadening permissions.

## Validate behavior and distribution separately

Use [evaluation.md](references/evaluation.md) for structural checks, independent
input-only trials, activation/non-activation, useful completion, and safe failure.
Run the target repository's existing checks before inventing replacements.
Valid metadata, clean lint, and a successful install are separate evidence from
a working skill in a particular runtime.

Use [packaging.md](references/packaging.md) for explicit file selection, license
and provenance review, the optional export helper, and exact inventory checks.
Keep secrets, private organization context, manuscripts, customer data, local
credentials and unrelated product dependencies out of exported files. Automated
scans are bounded checks, not proof of privacy or publication rights.

Read only the relevant route in [ecosystems.md](references/ecosystems.md).
Recheck its official sources before submission: a skill format, runtime,
installer, curated collection, directory and plugin marketplace have different
contracts. Never infer external acceptance, public availability, paid
distribution, or revenue from a valid package or a preparation command.

## Deliver a reviewable candidate

Return the canonical skill changes, selected export and inventory/hashes,
dependency and license/provenance records, actual validation and behavior
results, and the target-specific installation/submission draft. Keep private
evaluation evidence in its owning workspace; publish only cleared evidence.

Identify exact source and payload identity, tool/runtime/model versions,
observation date, completed checks, failures, untested claims and next action.
Separate source review, package integrity, installation, runtime behavior,
external review, listing and user acquisition. Preserve earlier achieved stages
when a later stage is pending.

Review authority at the actual boundary. Existing authorization remains valid;
otherwise obtain owner approval before an external submission, release, account
change or paid execution. Maintainers decide curated acceptance. A source merge
does not release a package or update a consumer. Retain an earlier pin for
rollback and rerun affected checks when the skill or target contract changes.
