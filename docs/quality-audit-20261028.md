# Initial toolkit quality audit — October 28, 2026

## Scope and evidence

Implementing-agent audit, not independent acceptance or human approval. Source
baseline: `283f8360090c1b8e62b27e018246e376c61ea70d`. This audit covers the
toolkit's current source/distribution distinction, existing Design and Release
guidance, documentation routing, and the new original rendered evaluation
fixtures. It does not certify every skill, consumer, native device or release.
The focused candidate is tracked by [issue #25](https://github.com/foculoom/aiartifacts/issues/25);
its final PR head and independent review are required before source adoption.

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
| Production-experience acceptance needs an explicit bounded decision | Technical/export correctness and narrow review can be overread as whole-product quality. This candidate adds target, artifact, reviewer lane, evidence, disposition, limits and owner deviations. | Independently evaluate the changed guidance and review its exact head. |
| Prior model coverage was largely text-based | D9/D10 retain their recorded fresh-session text-scenario passes; they were not rendered interaction studies. | Exercise the new original R1–R4 interfaces independently. |
| Source documentation overstated unfinished CI work | Design export CI already merged through PR #10. README now acknowledges it; historical dated counts remain historical. | Preserve the existing CI registration; no replacement CI PR. |
| Rendered fixture integrity is verified, model judgment is pending | The implementing agent ran 35 assertions and generated 22 desktop/narrow captures, then inspected representative PNGs. This verifies the test inputs, including deliberate defects, not acceptance of the interfaces or the skill's judgment. | Fresh input-only evaluator runs, then separate assessment and source review. |
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

## Acceptance and adoption boundary

Current decision for the **new guidance**: **unverified for independent
production-experience acceptance**. Implementing-agent checks establish a
reviewable source candidate; they do not satisfy independent evaluation or PR
review. R1–R4 must each use a fresh context with only the relevant revised
skills, case brief, raw fixture and render evidence. Keep the held-out rubric,
runner assertions and previous answers out of that context. Retain complete
answers and tools/model identity, then record an assessor's result separately.
Missing required interaction is partial coverage, not a screenshot-derived pass.

After evaluation fixes, review the final exact source head and required checks.
A consumer may then deliberately adopt that reviewed commit with an explicit
scope, checksum where vendored, its own acceptance evidence and release holds.
Do not label reading source as installation or silently replace an existing pin.
Public package publication remains a later, separately authorized step: review
version/catalog consistency, license/security/docs, the exact packaged file set
and release evidence; preserve v0.5.0 and all earlier tags. A public release
receipt and acquisition readback would establish that later milestone.
