# Initial toolkit quality audit — October 28, 2026

## Scope and evidence

Implementing-agent initial audit with subsequent independent behavior evidence;
not human approval or whole-toolkit certification. Source
baseline: `283f8360090c1b8e62b27e018246e376c61ea70d`. This audit covers the
toolkit's current source/distribution distinction, existing Design and Release
guidance, documentation routing, and the new original rendered evaluation
fixtures. It does not certify every skill, consumer, native device or release.
The focused candidate is tracked by [issue #25](https://github.com/foculoom/aiartifacts/issues/25);
its [PR #26](https://github.com/foculoom/aiartifacts/pull/26) final head and
independent review are required before source adoption. The initial audit is
complete for this stated scope; unresolved broader acceptance remains explicit.

The [v0.5.0 release](https://github.com/foculoom/aiartifacts/releases/tag/v0.5.0)
was published October 24, 2026 and remained the latest public release on the
October 28 readback. Its source archives are available for public acquisition.
The earlier recorded 69-test release validation remains an achieved milestone;
this audit neither repeats it nor converts newer source into released bytes.
Current main contains seven plugins/eight skills, including unreleased Design
0.1.1, Release 0.1.1, Engineering 0.1.2 and Performance 0.1.0 source. Reading or
merging source does not install those versions in a consumer.

## Findings and disposition

| Finding | Evidence and disposition | Next action |
| --- | --- | --- |
| Existing review/evidence controls are present | Design already requires rendered hierarchy, state and evidence limits; Release already separates source, artifact and live readback. Keep these workflows. | Extend the existing skills, not a duplicate art plugin. |
| Production-experience acceptance needed an explicit bounded decision | This candidate adds target, artifact, reviewer lane, evidence, disposition, limits and owner deviations. Independent R1–R4 behavior evaluations pass at source `7b6bf416173666d20b35def9c1200e0054122356`; technical correctness is not treated as whole-product approval. | Review the final evidence/source head and required checks. |
| Prior model coverage was largely text-based | D9/D10 retain their recorded text-scenario passes. Four fresh independent agents now inspected actual R1–R4 pixels and local interactions, with complete answers and scoped limits recorded. | Preserve the dated coverage; do not infer native, cross-model or universal creative capability. |
| Source documentation overstated unfinished CI work | Design export CI already merged through PR #10. README now acknowledges it; historical dated counts remain historical. | Preserve the existing CI registration; no replacement CI PR. |
| Rendered fixture integrity and bounded model behavior are verified | The author ran 35 assertions/22 captures. Fresh independent evaluations then generated their own action receipts and renders; all four pass the held-out behavior criteria. The failing fictional interfaces remain failing, as intended. | Retain the independent answers and assessment separately from fixture assertions and final PR review. |
| New package acceptance and distribution remain incomplete | No new package, tag, installation or consumer pin is produced by this change. | Keep publication held until required acceptance and owner release authorization; prepare a separate reviewed release packet. |

## Reproducible candidate verification

The local render run completed at `2026-10-29T03:26:31.948Z` (October 28,
20:26 PDT), with Node 24.19.0, Playwright 1.62.1 and installed Google Chrome
156.0.8078.48 in headless mode. The loopback server served only original fixtures
and external requests were blocked. Viewports were 1280×900 and 390×900, with
reduced motion selected. The [manifest](../evals/design/rendered/evidence-20261028/manifest.json)
records input/output SHA-256 identities, actual state measurements, and all 35
assertions; its 22 PNGs contain no account or product material. The
[runner instructions](../evals/design/rendered/README.md) reproduce the check
using an already installed runtime. Font/raster differences can change PNG
hashes on another machine; each run records its own artifacts.

Affected verification commands:

```sh
python3 scripts/validate_catalog.py
python3 -m unittest discover -s plugins/design/skills/product-identity/tests -q
python3 -m unittest discover -s plugins/release/skills/release-evidence/scripts -q
node evals/design/rendered/run.mjs --output /path/to/new-evidence-directory
git diff --check
```

Catalog validation passed with seven plugins/eight skills; Design passed 11
tests and Release passed five. The three edited skill entrypoints passed the
available skill-structure validator. The render runner and the final source
diff check are separate from model-behavior evaluation. No package dependency
or hosted workflow was added.

The independent-record follow-up passed catalog/reference validation, exact
public inventory and all 75 retained-file hashes, JSON parsing, path/private
context exclusion, and staged whitespace checks. Evaluated skills, references,
prompts, fixtures and runner were byte-unchanged from the evaluated commit, so
the existing browser receipt remains applicable; no new browser pass is claimed
for this documentation/evidence follow-up.

## Acceptance and adoption boundary

Current decision for the **new Design guidance**: **accepted within the R1–R4
behavior-evaluation scope**, assessed against the held-out criteria after four
fresh input-only agent runs on October 28, 20:31–20:43 PDT. The
[complete record](../evals/design/rendered/independent-20261028/README.md)
preserves exact evaluated head `7b6bf416173666d20b35def9c1200e0054122356`,
skill/input/capture hashes, full answers, actions, tools and the model-identifier
unknown. No rubric or earlier answer was supplied to those evaluators. It also
preserves unsuccessful exploration and distinguishes it from passing evidence.
No skill, reference, prompt or fixture change was needed after evaluation.

R3 preserves an explicit native-select keyboard and modal-traversal evidence
gap; R4 preserves the earlier N4 milestone while rejecting N5's changed narrow
layout. These limits are part of the result, not removed to make the score pass.
No physical-device, full accessibility, human taste, demand or universal
art-direction capability is claimed. The Release gate wording has source review
and existing verifier-test coverage, not a live-publication behavior study.

The independent source-review agent reported no blockers at `7b6bf416173666d20b35def9c1200e0054122356`;
the evidence and contributor-instruction follow-up still needs review at its
final exact head and required checks. These milestones do not authorize release.
A consumer may then deliberately adopt that reviewed commit with an explicit
scope, checksum where vendored, its own acceptance evidence and release holds.
Do not label reading source as installation or silently replace an existing pin.
Public package publication remains a later, separately authorized step: review
version/catalog consistency, license/security/docs, the exact packaged file set
and release evidence; preserve v0.5.0 and all earlier tags. A public release
receipt and acquisition readback would establish that later milestone.
