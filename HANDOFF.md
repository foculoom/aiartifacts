# Maintainer handoff

## Chat Organizer 0.1.0 source candidate — October 31, 2026

The owner approved a focused Chat Organizer plugin for Codex and ChatGPT users,
with one `organize-chats` skill, an AI Artifacts catalog entry, and standalone
skill/plugin ZIPs from the same reviewed source. The public Plugins Directory is
outside this delivery. The skill uses available account tools, supports an
authorized export when they are absent, and preserves transcripts, archive
states, project boundaries and automation settings. Consumer inventories and
receipts remain private; only synthetic cases belong in this repository.

Behavior source `ce892d26ac6509f439cf9cb518532471a1a27942` passed the
six fictional preservation cases. The corrected package source
`e34b75babcedc99407a494b2659c06e9da3761f9` has identical skill behavior
files and passed catalog and skill checks plus isolated five-file skill and
eight-file plugin export verification. The
[October 31 evaluation](evals/chat-organizer/results-20261031/README.md)
records exact hashes and runtime limits. Codex CLI discovery, explicit
invocation and unrelated non-activation were observed; a ChatGPT private-plugin
runtime was not tested. The independent blinded matched comparison yielded
one skill improvement and two ties, with no material regression. This **fails
the required two-pair usefulness gate**. No defect was demonstrated that
would justify a targeted rerun.

Hold distribution and source merge while that gate remains unmet. Draft
[PR #35](https://github.com/foculoom/aiartifacts/pull/35) exposes source for
review; independent review found and prompted correction of an inaccurate
marketplace-availability sentence in the package README. CI and exact-head
review remain pending. As observed October 31, Chat Organizer is not on the
default-branch catalog and is not publicly listed; no consumer installation or
live-account compatibility is established.
The v0.5.0 toolkit tag and consumer pins remain unchanged. Next: preserve the
candidate and complete PR checks/review, then use a newly predeclared
evaluation or an explicit revised acceptance decision before release. A
catalog entry alone is not a release or proof of account compatibility.

## Agent Supply Chain pilot — October 30, 2026

The owner replaced Editorial as the active distribution pilot with an
improvement to Awesome Copilot's existing `agent-supply-chain` skill. This
supersedes the earlier Editorial-only selection below. Keep the extra authoring
skill deferred and preserve all earlier Editorial packaging/acquisition and
runtime-attempt evidence. PRs #30–#32, public GitHub acquisition on October 30,
v0.5.0 and consumer pins remain unchanged.

The implementation is in the public contribution fork at
[`74d289660e954dbe03342bf0c3d8241b007b5125`](https://github.com/hellofoculoom/awesome-copilot/commit/74d289660e954dbe03342bf0c3d8241b007b5125),
based on upstream `5269f7ea2d6c3a9bfda5ed878b6726cf509121fd`. It adds one
standard-library helper, strict v2/explicit legacy verification, bounded
no-follow file access, scoped CI and a package-local MIT notice. There is no
second installed Foculoom skill or copied implementation here.

The [pilot procedure](evals/skill-delivery/agent-supply-chain/README.md) and
[dated receipts](evals/skill-delivery/agent-supply-chain/results-20261030/README.md)
record 47 passing helper tests, official static validation, five-file exact
exports, both local installation routes and independent source/privacy review.
The owner called the recorded verification output “Useful and clear”; this
is feedback on helper output, not human runtime execution. Initial candidate
8c0ef34 and its review-discovered path defects remain in history.

The [runtime follow-up](evals/skill-delivery/agent-supply-chain/results-20261030-runtime/README.md)
adds 47 passing local Linux helper tests (zero skips), alongside the earlier
macOS checks. An existing cached image ran without network access or downloads;
hosted Python 3.11 CI remains unperformed. A separate supported Codex profile
and normal owner sign-in resolved the observed company-context contamination.
The runner now supports that explicit profile and external measurement records.
Its 22 offline tests pass; the prior default behavior remains reproducible.

One explicit Codex diagnostic and the corrected six positive/three negative
cases passed independent functional review with observed loading/non-loading,
unchanged inputs and fixed runtime-recorded gpt-6.1-sol/medium. Three paired
tasks also completed; an independent reviewer rated all three as ties, below
the predeclared two-pair benefit requirement. No material regression was
demonstrated. This does not establish added skill value. Preserve all twelve
first attempts: their measurement inventory was visible and P4's read boundary
was ambiguous. Those attempts do not establish comparative benefit. The rerun
uses external inventories and matched, clarified task inputs. Backend identity
remains unreported; actual session context and tool schemas were reviewed.

No upstream PR was sent. The usefulness gate was not met; Copilot fixed-model
access and enforced model failure cases remain incomplete. No unchanged denied Copilot
request was repeated. No saved cloud environment was listed; work used the
authorized local runtime without purchases or credential copying.
Offline denied-access preparation preserves all three attempts, including an
allowed-path hardlink exposure and a later scoped pass with an alias-free
fixture. It does not establish F2 model behavior or other-tool confinement;
F1 interpreter confinement remains unproven. Do not restart favorable-outcome
searching or submit upstream merely because static/functional checks passed.

Public availability on October 30: the original upstream skill is cataloged
and the reviewed fork source is public; the improved candidate has local-source
installation receipts only. Awesome Copilot acceptance and skills.sh indexing
for the candidate are unverified. After full acceptance, recheck parallel work
and requirements, submit one ordinary upstream update PR, and verify public
acquisition at the merged SHA. Do not send the old Editorial intake packet.

## Editorial runtime evidence and access boundaries — October 30, 2026

The owner retained the full Copilot functional/usefulness gate and separated
account provisioning from the skill project. Continue Editorial 0.1.1 at
`c6fd52080ee50165ac673c72d5dd7adbe0b43e3c`; no exported content changed. PRs
[#30](https://github.com/foculoom/aiartifacts/pull/30) and
[#31](https://github.com/foculoom/aiartifacts/pull/31), existing package checks
and exact twelve-file public GitHub acquisition remain achieved October 30.
The extra skill remains deferred, and v0.5.0/consumer pins remain unchanged.

The [runtime procedure](evals/skill-delivery/runtime.md) adds explicit model and
reasoning arguments, bounded linked-skill enumeration and opt-in private capture
of only the evaluation's own local session. Requested values, runtime-resolved
configuration, backend identity and context acceptance are separate fields.
Reproduce offline runner checks with
`python3 -m unittest discover -s evals/skill-delivery -p test_runtime_runner.py -q`.

The [dated diagnostic](evals/skill-delivery/results/editorial-context-check-20261030/README.md)
records one fresh P2 baseline using existing ChatGPT access and CLI
0.166.0-alpha.5.1. Its runtime record confirms gpt-6.1-sol/medium, but the actual
initial context contains an unrelated user-global overlay despite the requested
isolation settings. Independent agent review confirmed the failure. The other
five comparison trials were held; usefulness remains unmeasured. Preserve the
diagnostic and private rollout. Establish a supported clean-context execution
route before restarting all six runs; never clear the gate from flags alone.

Copilot 1.0.54 supports BYOK without a paid seat, but no already-authorized
fixed-model route with verified included usage was established. No new Copilot
inference probe ran. Keep account/provider diagnostics private. Human editorial
feedback, Copilot behavior and its controlled comparison remain required before
the conditionally authorized external-plugin submission. No public issue was sent.

At 14:18 Pacific October 30 the rendered skills.sh candidate URL displayed 404
despite HTTP 200; it is not a usable listing. Indexing elsewhere remains
unverified. Public GitHub acquisition remains achieved, and Awesome Copilot
submission/acceptance remain pending. No saved cloud environment was available;
this bounded diagnostic used the authorized local runtime. Tooling/evidence
changes follow their own reviewed PR/CI path and do not release a plugin.

## Editorial-only distribution preparation — October 30, 2026

The owner requested a rubber-duck review and continuation of the minimal pilot.
Use existing Editorial only; keep the extra skill deferred. Preparation began
on clean default-branch `c6fd52080ee50165ac673c72d5dd7adbe0b43e3c`:
[PR #30](https://github.com/foculoom/aiartifacts/pull/30) is merged and
[main CI](https://github.com/foculoom/aiartifacts/actions/runs/41107455838) passed
157 Python methods and ten JavaScript tests. Those integration checks are done.

The [dated readiness record](evals/skill-delivery/pilot/editorial-readiness-20261030.md)
pins fresh twelve-file skill/fifteen-file plugin exports to that merged source,
retains exact manifests/configs, and updates the unsent intake packet. All
Editorial bytes/modes match the evaluated `211ad9d` candidate. New public GitHub
acquisition using existing skills CLI 1.7.4 resolved the full SHA and installed
twelve exact files/modes in one shared project skill folder for the two selected
agent targets. This is remote acquisition evidence, not two runtime tests or a
directory listing. Installer telemetry was disabled; raw machine paths remain
private and sanitized full installer output/hash maps travel with the receipt.

Rubber-duck review does not establish Editorial's uplift over the base model:
prior Codex task passes remain achieved, while a controlled Editorial comparison
and Copilot task behavior remain unverified. No saved cloud environment was
available; local Copilot remains 1.0.54. Its already-retried provider policy denial
was not retried unchanged. Next: use an already-authorized working Copilot
runtime for existing activation, negative and safe-failure cases, then review
actual task quality, provenance/rights and upstream submission decisions.

Public source acquisition is verified October 30; Awesome Copilot listing was
absent from inspected catalogs and skills.sh listing remains unverified. Existing
v0.5.0 was released October 24, with metadata last checked October 30 and archive
acquisition October 28. No new release, external submission or consumer pin
change follows. The prior evidence-redaction incident/history limits still apply.
This follow-up changes records only; existing Ubuntu CI and independent review
cover its source integration through the owning PR.

## Skill delivery tooling fallback — October 30, 2026

The owner selected **integrate the tested tooling and documentation; keep the
extra skill deferred**. The canonical exporter, license and portable tests are
now under `scripts/skill-delivery/`; current procedures are under
`docs/skill-delivery/`. The evaluated entrypoint is retained byte-for-byte only
as [SKILL.md.txt](evals/skill-delivery/candidate/SKILL.md.txt), outside ordinary
skill discovery. Engineering's original 0.1.2 manifest is restored; its existing
platform-boundary skill is unchanged. Editorial 0.1.1's packaging improvements
remain. No historical result, payload, source pin or privacy record was erased.

Reproduce current preparation with the
[pilot commands](evals/skill-delivery/pilot/README.md). Run the portable suite
with `python3 -m unittest discover -s scripts/skill-delivery/tests -q`, repository
checks with `python3 -m unittest discover -s evals/skill-delivery -p 'test_*.py' -q`,
and `python3 scripts/validate_catalog.py`. Expected discovery is seven plugins
and eight skills. Local macOS checks use a canonical temporary directory;
existing Ubuntu CI runs the same source checks. The new discovery regression
guards the deferral; model/provider tests are not repeated for a path-only
tooling move and removal of the installed entrypoint.

[PR #30](https://github.com/foculoom/aiartifacts/pull/30) owns the final source
review, checks and normal merge receipt for this selected scope. Source
integration is authorized; extra-skill adoption, release, external submission
and consumer updates remain separate. The previous experiment and its verified
outcomes are preserved below. Its failure to demonstrate incremental benefit
does not hold the independently useful tooling and documentation indefinitely.

## Skill delivery experiment — October 30, 2026

Work started from clean default-branch source
`1ce208bf7fb4b102bac8f31b192bc378790ed712`. The initial Engineering 0.2.0 proposal
added the [skill-delivery workflow](evals/skill-delivery/candidate/SKILL.md.txt),
three focused references and a standard-library exporter. Editorial 0.1.1 is
the real shared-source pilot: plugin and standalone-skill license text,
dependency declarations and explicit missing-tool/access behavior. See the
[pilot](evals/skill-delivery/pilot/README.md) for exact selection configs,
fresh export commands and the unsent external-plugin packet. No separate
instruction fork, generator, evaluation service or runtime dependency was added.

Portable preparation used the existing authorized local macOS environment after
no attached or listed authorized cloud environment was available. Bundled Python
3.12.14 and Node 24.19.0 worked; the default Homebrew Node had a missing simdjson
library and was not used. The existing Ubuntu CI now discovers the new exporter
tests. Runtime evaluation uses existing sign-in; no paid API fallback, credential
transfer or policy change is authorized by the toolkit.

The [evaluation procedure](evals/skill-delivery/README.md) keeps prompts and
held-out criteria separate. The [evidence index](evals/skill-delivery/results/README.md)
links dated receipts, independent reviews and selected-file hashes: the original
base SHA alone does not identify changed candidate bytes. The implemented source
at `211ad9da8b7a3d0740d1896a74c018ed3ad097be` passed 148 Python tests,
10 JavaScript tests and both hosted Ubuntu checks. Separate reviewers covered
the exporter/integration and authored skill references. Final scoped independent
reviews accepted head `4592a641d9fc6ea39e055d943a8dc71521442060`, and both
[hosted checks](https://github.com/foculoom/aiartifacts/actions/runs/41104482894)
passed there: 156 Python methods and 10 JavaScript tests. Those review and
validation milestones are complete. Fresh installed-file
comparison and runtime behavior are separate evidence. Copilot CLI 1.0.54 successfully installed the isolated
local Editorial plugin, but its unrelated connectivity probe returned
`Access denied by policy settings` before any skill evaluation. Copilot behavior
remains access-blocked; the cause beyond that observed denial is unverified.
A bounded retry after restored workspace usage returned the same provider denial.
Eleven Codex Editorial outcomes pass independent task grading within their
recorded scope; initial instruction isolation and exact model identity remain
unverified. Original failed sandbox setup attempts remain in the record.

Source review, hosted checks, independent behavioral grading and paired usefulness
results must be read at their exact recorded identities before claiming acceptance.
The initial PR #30 experiment was held as a draft because the paired trials
did not support adoption: baseline/helper corrections
were 1/0, 0/0 and 0/1, favoring the helper in one of three pairs against the
predeclared two-pair threshold. Full context/model controls remain unverified.
All six meta tasks reach scoped acceptance after one finishing correction;
explicit invocation diagnostics pass. Preserve those achieved outcomes and the
original failures. Retain reusable tooling/documentation; defer the extra skill.

A final test-layout correction removes the standalone suite's dependency on
other repository files. All 23 portable tests pass in an isolated installed
layout; three integration tests stay in `evals/`. The final local checks pass
152 Python methods and 10 JavaScript tests, with instructions/exporter unchanged.
Historical runtime receipts retain their old test hashes and 22/25 result.
The [evidence-redaction record](docs/skill-delivery-evidence-redaction-20261030.md)
documents temporary paths found after the first evidence push, the corrected
current packet, and the fact that earlier public history has not been erased.
Source/packages and the adoption hold are unchanged by that correction.
Four new offline host-path regression tests pass and are picked up by the
existing evaluation-test CI command. The prior 152-test receipt is retained;
these checks add bounded retention coverage rather than a privacy certificate.
The extra skill remains deferred because adoption has not met its stated
threshold; final review and checks at the recorded head are not pending work.
The tooling-only follow-up above has its own review/checks. The release owner
separately resolves remaining runtime/usefulness gates and rights review before
any tag or external submission. The prepared packet is not sent automatically.

Public availability is unchanged: v0.5.0 was published October 24; release
metadata was rechecked October 30 and archive acquisition was last explicitly
verified October 28. This candidate is unreleased, with no Awesome Copilot
submission or listing created and skills.sh public listing/acquisition still
unverified. Local telemetry-disabled installations do not establish public
discovery. Preserve all published tags and consumer pins.

## Strict Release manifest integration — October 30, 2026

The [red–green–refactor record](evals/release/manifest-validation-20261030.md)
reproduces silent inventory/hash loss from duplicate JSON members in the
anonymous static verifier at baseline `8b7d4fd92c361cb0ba8697322e50a5b7878efffa`.
Red commit `c6915d147017c219703404d51f8dc07ae091213e` has 8 failing subcases;
correction `a6cbba40941a95fc07796bd8802237c051b59392` passes all 10 Release
methods. The final refactor separates complete validation from network readback.
Release 10/10 and neighboring Design 11/11 pass in cloud Linux/Python 3.12.14.
The record includes exact commands and the local catalog setup limitation:
the connector text snapshot omits existing rendered PNGs. Reviewed
[PR #29](https://github.com/foculoom/aiartifacts/pull/29) merged on October 30
at 08:13:08 UTC as `1ce208bf7fb4b102bac8f31b192bc378790ed712`.
The [default-branch validation](https://github.com/foculoom/aiartifacts/actions/runs/41024980232)
passed. Those source review, integration and hosted checks are achieved.

No instruction evaluation, consumer compatibility, deployment or live customer
path is claimed. Maintainer owns source integration; consumer owners separately
review adoption. Existing v0.5.0 is still the latest non-draft release in the
October 30 GitHub metadata readback; no package/tag/version or consumer pin
changes. Archive download, native/provider acceptance and new publication are
not part of this work. Next: a consumer owner may review explicit adoption;
any package publication remains a distinct owning workflow.

## Evidence and recovery source integration — October 29, 2026

The [evaluation record](evals/engineering/evidence-recovery/results-20261029.md)
now retains the original six passes/one partial, the second F partial under the
original criterion, independent identification of an over-specific criterion,
and a third blinded F pass against its corrected general requirement. Earlier
answers were not silently relabeled. [PR #27](https://github.com/foculoom/aiartifacts/pull/27)
merged on October 29 at 22:52:46 UTC as
`f44c5284c3124c1006b91fc0244ddabf126eaaf3`, after
[independent agent review](https://github.com/foculoom/aiartifacts/pull/27#issuecomment-6510390903)
of exact head `de1426ff254658b920856f5b0d2b2a4ef2655d58`.
The [default-branch validation](https://github.com/foculoom/aiartifacts/actions/runs/40969157279)
passed both hosted Ubuntu jobs. These are source integration and cloud CI
receipts, not a new all-seven evaluation, installed adoption, live-provider
recovery or package release. The dated initial structural checkpoint below
remains evidence for its original revision.

This candidate extends repository reporting instructions, the engineering
retrospective template and the existing Release skill with dated claim evidence,
retrieval/product-state separation, ambiguous-operation reconciliation and
bounded causal analysis. Seven original fictional
[evidence-recovery cases](evals/engineering/evidence-recovery/README.md) keep
evaluator inputs separate from expected judgments. Actual product incidents,
private correlation and provider receipts remain in their owning repositories.

Historical candidate base: `7bacdfe91e80f670b41eddef859afddb6ffd9ad1`.
Preserve the evaluation's exact source and input hashes; a later checkout's
`git rev-parse HEAD` identifies that checkout, not the earlier evaluated input.
Local checks on October 29 passed: catalog validation (seven plugins/eight
skills and local Markdown references), the five-test Release verifier suite,
the packet's local link check, the skill-authoring frontmatter validator and
`git diff --check`. Reproduce the existing
checks using the commands in **Start on a new computer** below. These are
structural/script results. The [initial behavioral assessment](evals/engineering/evidence-recovery/results-20261029.md)
at `67ad0d77f188ad679170cea0f74792649cef194e` reports six passes and one
partial: the contradictory-diagnostics answer kept uncertainty but did not
specify a sufficiently controlled, bounded comparison. The sanitized result
retains the partial and trace/metadata limits. Later guidance and criterion
corrections, the third blinded F pass and final-head review are recorded above
and in the evaluation record; do not reopen those completed steps.
No automatic startup-loading or consumer-adoption pass is claimed.

Next: a consuming project may review the integrated source and explicitly
record its chosen source commit and evidence limits. Any new source changes
need their own affected checks and exact-head review. This source integration
cannot alter installed pins or authorize package publication.

Public acquisition is unchanged by this candidate: **v0.5.0 was last verified
available October 28**, as recorded below. No fresh provider readback is claimed
here. The new safeguards remain unreleased source; no plugin/package version,
tag, installation or consumer pin changed, and no toolkit publication is part
of this work.

## Production-quality source integration — October 29, 2026

The [initial toolkit quality audit](docs/quality-audit-20261028.md) records the
current source baseline, actual checks, new rendered inputs and remaining
acceptance. This focused candidate extends the existing Design and Release
skills with a brief-relative production target, reviewer/evidence scope and an
explicit bounded decision. It introduces no new art plugin or universal style.

Four original [rendered cases](evals/design/rendered/README.md) now have a real
local browser receipt: 35 fixture assertions and 22 captures at 1280×900 and
390×900, completed October 28 at 20:26 PDT. The captures and manifest travel with
the repository; only synthetic, original interfaces appear in them. The
assertions verify the test fixtures, not design quality. Four fresh independent
agent evaluations subsequently ran at source
`7b6bf416173666d20b35def9c1200e0054122356` on October 28, 20:31–20:43 PDT.
All four pass the held-out behavior criteria; the
[complete public-safe record](evals/design/rendered/independent-20261028/README.md)
retains full answers, input/skill hashes, new action receipts and captures,
unsuccessful exploratory checks and scoped limits. R3's native-select keyboard
gap remains unverified; no physical-device or universal quality claim follows.
The source-review agent reported no blockers at that evaluated head. This
evidence/contributor-instruction follow-up received
[final independent agent review](https://github.com/foculoom/aiartifacts/pull/26#pullrequestreview-5692683397)
at `2c364be7cf241cd0006a20a4053b6326be85a038` and passing hosted checks.
[PR #26](https://github.com/foculoom/aiartifacts/pull/26) merged October 29 at
04:00:34 UTC as `7bacdfe91e80f670b41eddef859afddb6ffd9ad1`.
Evaluated skills, references, prompts and fixtures were unchanged by that
follow-up. The audit retains reproduction commands and historical limits;
source adoption and package publication remain separate decisions.

Public acquisition: **v0.5.0 remains available**, with its October 24 publication
and latest-release/archive readback reverified October 28. New Design 0.1.1,
Release 0.1.1, Engineering 0.1.2 and Performance 0.1.0 remain unreleased source;
this candidate changes no tag, package, installed plugin or consumer pin.
Publication of a new toolkit package is held pending required acceptance and
owner release authorization. Reviewed source adoption is a deliberate separate
decision and must record the exact reviewed commit. Preserve earlier achieved
releases and their evidence while closing the current gaps.

## Distribution readiness and conditional forecast — October 27, 2026

AI Artifacts is a supporting toolkit; paid implementation or support is a
separate proposal. Foculoom LLC owns release and service decisions. For a new
toolkit version, source and synthetic tests establish a candidate; a release
packet also needs exact-revision review, version/catalog, license, security and
documentation checks. A tag and hosted release receipt establish distribution.
For paid support, an owner-approved offer and working customer path are further
gates. These stages do not follow an app-store submission process.

| Channel | Achieved milestone and evidence | Present public acquisition | Remaining work and next action |
| --- | --- | --- | --- |
| Free v0.5.0 toolkit | Released October 24 after 69 recorded tests and catalog review; the GitHub release was rechecked October 27. This is an acquirable baseline for explicitly pinned consumers. | **Available** as the existing [v0.5.0 release](https://github.com/foculoom/aiartifacts/releases/tag/v0.5.0), verified October 27. | Preserve the tag and current pins. Prepare and review a distinct release packet before offering newer source. |
| Design 0.1.1 source | Strict manifest parsing and Design CI registration merged through reviewed PRs #7 and #10 on October 27; #23 added stateful review guidance. The source can be evaluated and packaged deliberately. | **No newer Design release** was observed October 27; these main-branch changes are not an installed consumer update. | Review version, catalog, license, security, consumer behavior and exact source before a separately authorized release. |
| Proposed paid implementation/support | A conditional planning proposal exists; no offer or activation receipt is recorded in this handoff. | **No paid service or customer acquisition path** is recorded as of October 27. | Owner defines scope, price, rights, staffing, support, privacy, cost and customer path before any offer or activation. |

The date for another toolkit release or any paid-service activation remains
unresolved until scope, reviewer and owner capacity, hosted checks and operating
assumptions are measured. PR #9 proposed sizing the remaining work by October
30 and revisiting a conditional forecast weekly; those are planning suggestions
for the owner, not a release commitment or approval to sell or spend. The
existing v0.5.0 release does not authorize moving its tag or updating consumers.

The October 24 hosted readback of the now-superseded Design CI [PR #8](https://github.com/foculoom/aiartifacts/pull/8)
at exact head `afa3523c758cd88c37baa42525a245add483e987` found successful
Actions run `40107693307`, job `120912691716`, including 11 synthetic Design
tests and catalog validation. That is a dated receipt for the old head only.
The same Design test command is registered on `main` through merged PR #10;
no separate CI behavior from PR #8 is needed.

## Strict Design manifest parsing — 27 October 2026 source reconciliation

[PR #7](https://github.com/foculoom/aiartifacts/pull/7) makes the unreleased
Design 0.1.1 export checker reject duplicate JSON members at every object level
and require integer version `1`. After reconciliation with the October 27
`main`, its 11 synthetic Design tests, catalog validation, the 27-test Editorial
suite and the 10-test Performance suite passed locally. Its final head passed
hosted checks and independent review, then merged as
`f08d1d29d789d699e9593d97a253ab5783229b09`. It changes no released tag,
installed plugin, or consumer pin. Reviewed [PR #10](https://github.com/foculoom/aiartifacts/pull/10)
merged as `c4093e699872d4fd8a00eb99c4ddf195698bc22a` and registers the
Design suite in CI.

## Stateful experience-review source follow-up — October 27, 2026

An unreleased Design 0.1.1 guidance candidate at source commit
`38ce770ca8885d47bdf1fd10bf832627f61ea1b5` adds four-state review
(starting, active, overview/pause, recovery) and an exact released/source/
candidate comparison to the existing experience-review skill. Fictional D9
exercises a navigation and paused-action divergence across three artifacts;
fictional D10 preserves an already-correct booking form without importing game
rules. No product data, plugin package, tag or consumer pin changed.

From the repository root on October 27, `python3 scripts/validate_catalog.py`
passed (six plugins, seven skills), the Design export checker suite passed
(seven tests), and `git diff --check` passed. The new D9/D10 model-behavior
evaluations ran on October 27 against exact head
`33347aec63e53f6226a64e0905db2f4a15f96123`, with expected judgments withheld:
an initial paired-context run and separate fresh-session runs for D9 and D10.
Both cases passed the observable criteria in `evals/design/README.md`. The
[evaluation record](evals/design/stateful-review-20261027.md) preserves all four
answers, inputs, context/tool limits and agent assessments. The exact model
identifier was unavailable; no rendered UI, real booking, native/device test or
cross-model study is claimed. The evidence-only follow-up reran the same catalog,
Design and diff checks successfully without changing the evaluated inputs.

Reviewed [PR #23](https://github.com/foculoom/aiartifacts/pull/23) subsequently
merged as `fcf44212172ec6817c601490ca8ab9776b64d86e` on October 27. Design
0.1.1 remains unreleased source; no package, tag or consumer pin changed, and
this source merge did not publish Design or update consumers.

Engineering 0.1.2 source integration — 27 October 2026: reviewed
[PR #21](https://github.com/foculoom/aiartifacts/pull/21) head
`ff6a1767ea19c5e8dedc8c3c33299031228c1a82` merged to `main` as
`2319cab3f152960bf0b119b30af97a4b7e31bc7a`; the
[default-branch validation](https://github.com/foculoom/aiartifacts/actions/runs/40488088102)
passed. The optional `js-import-graph` guard parses declared JavaScript
modules with locked Acorn 8.18.0. It is separate from the Python inventory
and does not install Node in other plugin workflows. From
`plugins/engineering/skills/platform-boundaries/scripts/js-import-graph`, run
`npm ci --ignore-scripts` and `npm test` (ten synthetic tests passed locally on
Node 24.19.0). The existing Python boundary suite passed 28 tests, and catalog
validation passed six plugins/seven skills. The evaluated dependency-cruiser
18.5.0 did not report nonliteral dynamic imports or malformed JavaScript; see
the adoption reference for exact limits. Forticle subsequently adopted this
source pin in reviewed [PR #52](https://github.com/foculoom/forticle/pull/52),
merged to its `main` as `56ed398d2dbdc2a9182eee96051fe4feda1725e0`;
that product owns its policy and CI. No AI Artifacts tag, plugin package release
or installed consumer pin changed. Publishing an updated plugin remains a
separate version/release decision.

Source ownership guard candidate: `check_inventory.py` adds explicit-file ownership
within declared roots/extensions, expired/unused exception rejection and symlink
rejection. `python3 -m unittest discover -s plugins/engineering/skills/platform-boundaries/scripts -q`
passes 28 synthetic tests (12 lexical, 16 inventory). It does not parse import
graphs or change hosted protection. Existing CI already discovers this suite.
No new dependency, plugin version/tag or installed consumer pin is changed.
Independent exact-head PR review and explicit consumer adoption are required.

Checkpoint: **v0.5.0 was published on 24 October 2026**. Preserve that existing tag and release; do not recreate or move it. The Design and Release 0.1.1 guidance below is unreleased source. This public document contains reusable-method context only. Product/private account decisions, reports, manuscripts and credentials belong in their owning repositories.

## Start on a new computer

Apply [environment selection](AGENTS.md#cloud-execution-when-feasible) before
choosing a host. Record actual capability and access limits; the native
Keychain step does not prevent portable checks from running in cloud CI.

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
whole puzzle expansion. Browser evidence supports browser guidance. Native
claims require the owning project's native acceptance evidence, including the
exact packaged candidate, runtime and device profile. Use simulators where the
owning policy accepts them; require physical hardware only for a specific
claim or provider requirement that needs it. Browser emulation is not native
testing. Source merge, native submission and public availability remain
distinct milestones.

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

## Reuse audit source — October 26, 2026

Unreleased Engineering source now includes a narrow [reuse-decision reference](plugins/engineering/skills/platform-boundaries/references/reuse-decisions.md)
and synthetic cases for shared renderers and storage failure contracts. It helps
callers compare behavior, versioning and failure paths before extraction; it
does not move product code, change installed consumer pins or certify any
product release. PR #19 records the source review; verify its final head and
required checks before merging. A source merge remains separate from a plugin
tag or a consumer pin.

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
no new tag or dependency was introduced at this checkpoint. The Design suite
was local only when this section was written; PR #10 registers it in CI as a
separate reviewed change. Re-run it against the exact candidate before a release.

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

## Performance 0.1.0 source candidate

[PR #10](https://github.com/foculoom/aiartifacts/pull/10) added advisory browser
measurement, a dependency-free comparator, synthetic tests, and CI registration
for the Design export suite. It merged as
`c4093e699872d4fd8a00eb99c4ddf195698bc22a` on October 27 after an
independent agent review and passing checks. No release tag or installed
consumer pin changed with this source integration.
