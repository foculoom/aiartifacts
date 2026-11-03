# Audiovisual guidance evaluation — November 3, 2026

## Scope and method

Base source: `e9b57c18dd01d8f5b5871e4c60653999fc0f13b1`. Candidate skill and
template hashes are retained in [evidence.sha256](evidence.sha256). This is
bounded source-guidance verification, not rendered or auditory acceptance.

A fresh independent agent read only the candidate experience-review SKILL.md
and [input cases](../inputs.md). It was asked to answer AV1–AV7, record exact
input identities, actual tools and limits, and read no other files or linked
references. The [complete answer](answer.md) was fixed before assessment. It
was not given [expected criteria](../assessment.md), this report or private
product context. All seven inputs were handled in one session; this is not
seven independent reviewers, human participants or distinct model trials.

The evaluator used text/file tools for hashing and reading its two inputs and
writing its answer. No image/audio artifact was supplied or perceived, no browser
or product was exercised, and no external action was taken. The exact backend
model/version was not independently verifiable. The author then assessed the
fixed answer against criteria prepared before evaluation; that assessment is not
an independent human judgment or a second blinded trial.

## Bounded assessment

All seven text-case criteria passed on the first retained answer:

| Case | Result | Answer evidence |
| --- | --- | --- |
| AV1 | Pass | Separates permitted screenshot inspection from unverified audio, transitions and runtime feedback; source calls do not accept playback. |
| AV2 | Pass | Limits transcript and signal-summary claims; rejects voice, mix and runtime conclusions from a text-only tool. |
| AV3 | Pass | Preserves silent puzzle and text/exit-code CLI scope; relevant checks remain unperformed rather than passed. |
| AV4 | Pass | Plans synchronized timestamp review tied to the brief, capture provenance and actual capabilities; invents no observations or model/device/human result. |
| AV5 | Pass | Keeps audio unverified and requests only a bounded authorized listening path; no purchase, installation, upload or transcription-as-listening. |
| AV6 | Pass | Separates capture failure from product failure and event logs from audible proof; proposes known-cue/direct-output discrimination and a candidate retest. |
| AV7 | Pass | Covers local speech playback, pause/resume and interruption with capture checks; does not send/upload or infer human comprehension, and explicitly checks visual capability separately. |

These outcomes establish comprehension of the described evidence boundaries.
They do not establish actual media perception, detection accuracy, improved
testing, runtime routing, native speaker behavior, accessibility or enjoyment.
No baseline comparison or user study was run. Existing rendered-case results
retain their original artifacts and do not automatically validate this addition.

## Source verification and integration

The [independent source review](source-review.md) found no blocking issue in the
guidance and synthetic cases, with its preliminary coverage explicitly bounded.
Final review must inspect the published exact head, full answer and evidence
manifest; the PR records that readback and hosted-check results before merge.

Preparation used exact GitHub text files and a complete canonical tree inventory,
not a full local clone. Checks verified baseline Git blob identities, clean patch
application, added-line whitespace, changed-file links, seven input/criterion
pairs, and a narrow public-file allowlist. Manual review plus selected private
marker checks found no private product/participant material in the publication
set. Plugin metadata, catalog, workflow files and consumer pins are unchanged.
Existing hosted CI, not these local structural checks, owns full repository
validation. The source commit/PR must be read back before integration is claimed.

From a checkout of the candidate, run:

```sh
git diff --check
python scripts/validate_catalog.py
sha256sum -c evals/design/audiovisual/results-20261103/evidence.sha256
```

For another behavioral trial, give a fresh evaluator only the candidate skill
and inputs, preserve the complete first answer and exact identities, then assess
against the held-out criteria. To claim actual audiovisual quality, inspect
relevant authorized media and interactions with capable reviewers and valid
capture paths under the existing production-acceptance method.

Public source integration is authorized through a protected PR. Package release,
consumer-pin adoption and private product acceptance are not part of this change.
Published v0.5.0 and unrelated release holds remain unchanged.
