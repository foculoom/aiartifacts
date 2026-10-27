# Maintainer handoff

Checkpoint: **v0.5.0 was published on 24 October 2026**. Preserve that existing tag and release; do not recreate or move it. The Design and Release 0.1.1 guidance below is unreleased source. This public document contains reusable-method context only. Product/private account decisions, reports, manuscripts and credentials belong in their owning repositories.

## Start on a new computer

Install Git and Python 3.9 or later. These commands use `python3`; on Windows,
use an equivalent Python 3 command. From a fresh checkout, record the exact
source revision before applying any unreleased guidance:

```sh
git clone https://github.com/foculoom/aiartifacts.git
cd aiartifacts
git fetch origin --tags
git switch main
git pull --ff-only origin main
git status --short
git rev-parse HEAD
python3 scripts/validate_catalog.py
python3 -m unittest discover -s plugins/release/skills/release-evidence/scripts -q
```

Read this handoff, README, CONTRIBUTING, CHANGELOG and the specific skill and
evaluation before changing shared guidance. `main` contains unreleased source
candidates; published `v0.5.0` remains the tested release snapshot. Reading a
reference from `main` does not install or release that candidate in a consuming
product. Record the exact repository commit and any installed plugin version
separately. Keep the product's deployment commands, credentials and live
evidence in its owning repository or private operations storage.

## Pending input and controls guidance

Decision recorded October 26, 2026: extend the existing skills after the
[Quiet Below controls requirements](https://github.com/foculoom/quietbelow/blob/main/docs/PRD_CURRENT.md)
have been implemented and validated. The October 26 requirements checkpoint below is historical. Recheck the owning
product candidate and acceptance records before drawing reusable lessons; later
implementation or release evidence does not change a published plugin by itself.

The requirements and next-agent sequence were merged in
[Quiet Below PR #64](https://github.com/foculoom/quietbelow/pull/64), at
`862fe709f75e2a897b1cff42506bd5da9917054c`. Its
[controls plan](https://github.com/foculoom/quietbelow/blob/862fe709f75e2a897b1cff42506bd5da9917054c/docs/CONTROLS_UPDATE_PLAN.md)
records the reproduced findings and acceptance checks. This is the requirements
baseline; a later corrective implementation PR must supply passing evidence.

For this follow-up, a successful game update means a corrected, reviewed source
candidate with reproducible before/after evidence and passing gameplay and
browser checks. It does not require commercial success or completion of the
whole puzzle expansion. Browser evidence supports browser guidance; native
claims require separate packaged-app and physical-device evidence. Source merge,
native submission and public availability remain distinct milestones.

| Existing skill or profile | Candidate reusable guidance |
| --- | --- |
| [Experience review](plugins/design/skills/experience-review/SKILL.md) and its [interactive experiences reference](plugins/design/skills/experience-review/references/interactive-experiences.md) | Exercise keyboard-only, pointer-only, touch and mixed-input journeys separately. Check visible focus, repeated button activation, dialogs, modifier shortcuts, landscape/safe-area layout, fullscreen access to controls and recovery. |
| [Game UI](plugins/editorial/skills/editorial-writing/references/medium/game-ui.md) | Match instructions to supported input, keep alternative controls discoverable, and explain action effects and unavailable states. Screen width alone does not establish which input devices a player has. |
| [Platform boundaries](plugins/engineering/skills/platform-boundaries/SKILL.md) | Keep shared gameplay actions and outcomes separate from device bindings and presentation. Test input adapters against the same behavior while preserving platform-specific accessibility and lifecycle needs. |

The next agent should complete these steps in order:

1. Read the game's current PRD and handoff; verify its corrective PR and exact
   tested source revision. Record the reproduced problem, expected behavior,
   actual result and test command for each pattern proposed for reuse. Retain
   product audit logs, screenshots and device records in the owning project's
   private or local evidence storage under its retention rules, outside tracked
   source and shared skills.
2. Confirm gameplay regressions and complete keyboard-only, pointer-only and
   touch journeys pass, including start, play, hints, undo/restart, overview,
   pause/dialog return and reload. Include mixed-input switching, modifier keys,
   focus retention and input-repeat behavior. Mark missing native/device or
   assistive-technology checks explicitly; do not convert browser emulation into
   physical-device evidence or accessible buttons into nonvisual gameplay.
3. Add narrowly scoped guidance to the existing skills and synthetic positive
   and negative behavior evaluations. Cases should catch hidden pointer controls,
   focus stolen after button activation, browser shortcuts changing game state,
   controls covering feedback, and unsupported claims from limited evidence.
   Include a case that preserves an already-correct interface and a non-game
   case that rejects importing game-specific control rules.
4. Run affected plugin tests, catalog/skill validation and the new behavior
   evaluations, following their recorded evaluation procedure. Have an independent
   reviewer inspect the exact candidate diff, examples, references and evidence
   limits before the focused PR is merged. Record actual results and unresolved
   gaps; automated passes do not establish enjoyment or universal accessibility.
5. Advance affected plugin versions and changelog only with the implemented
   guidance. Publish a tested repository snapshot through the normal release
   process, preserving existing tags. A consuming product adopts and records
   that tested revision explicitly; do not silently replace its current pin.

Keep exact key bindings, directional movement, turn/repeat policy, puzzle rules,
hint defaults, pricing, purchases, saves and release holds in Quiet Below. The
shared skills should teach how to inspect and validate those decisions, not
impose them on other products. Use synthetic or explicitly cleared examples and
primary references; do not copy private playtest responses or internal records.

## Reuse audit candidate — October 26, 2026

Unreleased Engineering source now includes a narrow [reuse-decision reference](plugins/engineering/skills/platform-boundaries/references/reuse-decisions.md)
and synthetic cases for shared renderers and storage failure contracts. It helps
callers compare behavior, versioning and failure paths before extraction; it
does not move product code, change installed consumer pins or certify any
product release. Validate the catalog, the skill and the synthetic criteria
before a separately reviewed source merge.

## Architecture and release state

One repository holds independently versioned plugins, skills, agent templates, synthetic evaluations and templates. Do not create one repo per product or writing medium. In the released v0.5.0 snapshot, Editorial, Design, Release and Automation are 0.1.0, and Reporting is 0.1.1. The unreleased source adds Design 0.1.1 as described below. The catalog is `.agents/plugins/marketplace.json`. Repository tags pin the combined tested snapshot; they do not imply installation or listing in a universal plugin directory.

- Editorial: shared review method with audience/medium profiles and project voice brief. Never certify human authorship from lint or replace a human editor with a score.
- Design: product-identity and experience-review; shared publisher frame versus product identity, preserve approved choices, distinguish defects/preferences/hypotheses and record observed scope/revisions. Product briefs/artwork stay with their owners.
- Release: serialized release evidence, source/package/provider/live separation, sanitized hash checks; it does not grant deployment authority.
- Reporting: normalized Tally/Gmail/analytics adapters, private aggregate report format, QA and linked-notification exclusions, stale/missing/partial evidence, minimal text-free outputs. Acquisition, authentication, scheduling and retention are consumer responsibilities. Do not imply the offline generator itself connects to providers.
- Reporting 0.1.1 retains unknown context for legacy input and counts self-reported free/paid use, edition and build separately; QA and owner testing stay excluded. No purchase or identity inference.
- Automation: reviewed local tasks with a compiled Keychain launcher, exact service-account/vault checks, task-specific credentials and fresh boolean evidence. No arbitrary command/secret export, cloud runner, automatic rotation or authority expansion. The current Mac consumer demonstrated repeated read-only execution with desktop 1Password locked; that does not prove every task, Keychain lock state or provider write scope. Private evidence remains with the consumer.

v0.4.0 merged at `38b86df9513df3b5a65f02fa1acc4f949dd3e9a9`; tested tree matched the tag:15 reporting, 27 editorial and 5 release tests passed, plus catalog/skill validation. Preserve that historical tag. The v0.5.0 snapshot adds Automation 0.1.0 and advances Reporting to 0.1.1.

## Continue safely

Read README, CONTRIBUTING, CHANGELOG and the relevant plugin/skill before edits. Preserve Apache-2.0 and applicable attribution. Use synthetic or explicitly cleared fixtures. Record upstream source, tested commit, installation and license; do not silently vendor or auto-update. Add an agent configuration only after testing demonstrates a role the skills cannot cover.

For behavior changes run that plugin's tests and structural/catalog validation, update plugin version and changelog as appropriate, then tag the tested repository snapshot after review. Preserve existing tags. Consumers pin and record revisions; they should not silently switch to main.

## Future automation lessons

Prefer narrow existing connectors/service-account access, sanitized durable result files and a single deployment owner. A transient terminal PASS without target/hash/context is insufficient handoff evidence. Credential field-shape diagnostics must never print values. Browser sign-ins and provider scope limits remain explicit dependencies; a skill cannot override credential handoffs or approve broader access. Keep provider-specific normalizers strict and tested rather than accepting any HTML with a build marker.

## Resume and update discipline

Read this checkpoint before the dated history. Fetch the canonical remote, inspect branch/status and preserve other work. Dates below are observations, not a promise that external systems remain unchanged. Recheck provider status before a new release or availability claim. A merged PR is not a deployment; passing tests are not customer demand or commercial clearance. Prefer existing scoped access and service-account helpers; never store credentials in Git or chat. Keep user decisions separate from implementation and external approval. Update this checkpoint and its linked evidence when a milestone changes. Keep historical evidence rather than rewriting it as a new pass.

## v0.5.0 validation

The candidate passed 17 automation, 20 reporting, 27 editorial and 5 release tests (69 total), plus catalog validation for five plugins/six skills and skill structure validation. On macOS run the editorial suite with `TMPDIR=/private/tmp`: its no-symlink input policy deliberately rejects the default `/var` symlink path. The first run under the default temporary path failed for that environmental reason; the canonical-path rerun passed. No editorial behavior was changed.

The consumer's existing private profile also passed the final compiler guards. Live Keychain/provider evidence remains in the owning consumer, as do its exact configuration and task identities. Synthetic error cases do not claim live revocation/expiry tests.

CI initially rejected its group-writable toolcache Python as a reviewed executable. Synthetic child-process tests now use the system interpreter; a regression test explicitly preserves rejection of group-writable files. Production runner guards were not relaxed.

## Unreleased Design 0.1.1 source candidate

Design's product-identity skill now links a reusable export handoff and an
optional Python standard-library checker. Seven synthetic tests cover explicit
source roots, output preservation, linked entries, exact inventory and hash
mismatches; no product files or provider access are used. The checker establishes
local file identity only. Final-raster QR decoding and physical/vendor checks
remain separately observed actions, not results of the checker.

Run `python3 -m unittest discover -s plugins/design/skills/product-identity/tests -q`
and `python3 scripts/validate_catalog.py`. This source candidate is unreleased;
no new tag, dependency or CI configuration is introduced. The existing CI does
not yet invoke the new Design test suite, so preserve its local validation record
and register the command through the normal reviewed CI change before release.

## Unreleased operational-status and release-evidence source

The operational-status review guidance and exact ZIP-inventory rule merged in
[PR #14](https://github.com/foculoom/aiartifacts/pull/14) at
`1c95239d7662a37b560b836dab5bdb482cf13a38`. The reusable review entry
point is [experience-review](plugins/design/skills/experience-review/SKILL.md)
and its [operational-status reference](plugins/design/skills/experience-review/references/operational-status.md).
Use [Design case D8](evals/design/cases.md) and its
[evaluation criteria](evals/design/README.md) to check claim scope, unknown
states, metric provenance and public/private boundaries. The release entry
point is [release-evidence](plugins/release/skills/release-evidence/SKILL.md);
its [archive-inventory cases](evals/release/archive-inventory.md) catch an old
ZIP that retains an extra file while `unzip -t` still succeeds.

The Release verifier tests run with the command in the fresh-computer section.
Design case D8 and the archive-inventory cases are model-behavior evaluations,
not unit tests or live deployment evidence. Run each case in a fresh session
using the exact changed skill revision, with expected criteria withheld, and
record the model, tool access, output and pass/partial/fail evidence. These
sources contain fictional examples only; do not import account data, private
metrics, credentials or captures from a consuming project. This contribution
did not tag a new release or change any consumer's existing v0.5.0 pin.

## Engineering source candidate

Engineering 0.1.0 adds the [platform-boundaries skill](plugins/engineering/skills/platform-boundaries/SKILL.md) and a dependency-free, bounded lexical guard with synthetic failure tests. Source candidate only; existing release tags and consumer pins are unchanged. The guard does not certify dependency graphs, device behavior, purchases or store readiness.

## Unreleased parallel-work source candidate

Engineering and Release 0.1.1 add conditional parallel-preparation guidance and an
Engineering handoff template. Both plugins remain independently usable; references
stay inside their own package. The method separates isolated writing/review lanes
from serialized integration and production ownership. See
[synthetic cases](evals/engineering/parallel-work.md) for evaluation prompts and
observable criteria. This is source guidance, not an orchestrator, global lock or
permission grant. Existing release tags and consumer pins are unchanged.
