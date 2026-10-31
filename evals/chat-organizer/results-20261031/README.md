# Chat Organizer 0.1.0 candidate evaluation — October 31, 2026

The behavior-tested skill comes from commit
`ce892d26ac6509f439cf9cb518532471a1a27942`. Independent source review
found that the plugin README implied current marketplace availability; commit
`e34b75babcedc99407a494b2659c06e9da3761f9` corrected that statement
without changing the skill or its supporting files. The final package
verification below uses `e34b75babcedc99407a494b2659c06e9da3761f9`.
The `SKILL.md` SHA-256 is
`cd664af43f4b96d6dd31d65f0bdbd88dc2d3f078479872b468f52f177b18be05`.
The final dependency document adds standalone installation guidance after the
first six behavior runs; the skill instructions, capability reference and
migration template did not change. Explicit activation and unrelated-task
smokes used the final dependency document. Full session traces, fictional
state and action receipts, attempted runs, and randomized review mapping are
retained outside this repository. No real chat data is included here.

## Synthetic behavior

All six [predeclared cases](../cases.md) satisfied the applicable preservation
and authorization criteria. C1 and C2 remained read-only. C3 reconciled an
ambiguous timeout by ID, skipped the completed move, moved one chat and
rearchived two (three mutation receipts). C4 deferred shared exposure and an
unsupported memory move while moving the compatible chat (one receipt). C5
reported six unique active and two archived chats observed and left the ninth
baseline ID unverified after a rate limit. C6 verified existing sections,
title, pin, automations, working directory and permissions twice without a
mutation receipt. These are fictional account transitions, not real-account
compatibility evidence.

The existing signed-in Codex CLI `0.166.0-alpha.5.1` ran these cases with
requested and runtime-recorded `gpt-6.1-sol` / `medium`; the provider did not
report a backend model identity. The runtime loaded `organize-chats` for
ordinary chat-organization tasks and an explicit `$organize-chats` invocation.
It did not load the skill for an unrelated arithmetic request. The runner
disabled other skills, apps, plugins and memories, but captured a user-level
instruction overlay despite those flags. The matched arms shared that
overlay; fully clean context was not established. A first sandbox-denied CLI
attempt was retained, then the already-authorized local runtime completed
the trials. ChatGPT private-plugin runtime invocation was not tested.

## Matched comparison

Three fresh, same-model/same-input pairs compared the skill with the same
assistant without it. An independent reviewer received randomized A/B
answers, action receipts and recovery records without arm identity. The
mapping was revealed only after the judgments were fixed.

| Pair | Blinded judgment | Deblinded result |
| --- | --- | --- |
| C1: current outcomes | B clearer on the small focus list and work/personal placement | Skill improvement |
| C3: interrupted archived move | Tie; both recovered one move and two archive states | Tie |
| C5 then C6: incomplete count and repeat run | Tie; both identified the verification gap and made no changes | Tie |

There was no material regression, but only **one** clear practical improvement,
below the predeclared two-pair requirement. This candidate is **not recommended
for release or distribution** on this evidence. The comparison showed no
functional defect to repair, so no favorable reruns were selected. Retain all
ties and first attempts. A later release decision needs a new predeclared
evaluation or an explicit change to the acceptance gate, followed by review
of the exact new source.

## Package and source checks

Catalog validation found eight plugins and nine skills with resolved local
Markdown links. The skill structure validator passed. Four focused simulator
tests, 23 exporter tests, 31 existing skill-delivery tests, ten static release
verifier tests, and 27 editorial tests passed locally (the editorial rerun used
canonical `/private/tmp` after a host temporary-path error). `git diff --check`
passed. GitHub CI and exact PR-head review remain separate gates.

The existing exporter prepared candidate packages from the source commit. The
standalone skill has five exact files; the plugin has eight. Both ZIP inventories
and isolated extracted installs passed manifest hash/mode verification. Local
candidate ZIP SHA-256 values are:

| Package | SHA-256 |
| --- | --- |
| Standalone skill | `b60f8da8bd8a5c5f5b81166576aaae1412ee21154391d39084feeace58fcff66` |
| Plugin | `e54f00ca8f987f2ebb0232ecf0918d51dd1c31b0ef6bdd067fcd07fbfb917181` |

These candidate archives stay private while the usefulness gate is unmet.
They do not imply an installed consumer, public listing or successful live
account organization. As observed October 31, [draft PR #35](https://github.com/foculoom/aiartifacts/pull/35)
exposes candidate source for review, while the new plugin is not on the
default-branch marketplace catalog. No public Plugins Directory submission or
new toolkit release was made. The existing v0.5.0 tag and consumer pins are
unchanged.
