# Independent paired grading — 30 October 2026

**These results do not support adopting the extra skill.** After two bounded
corrections, all six arms meet the applicable preparation criteria, but the
helper needed fewer distinct corrections in only one of three pairs. The
formal usefulness gate remains **unmeasured** because exact serving-model
identity and complete initial-context isolation were not established. The
observed counts also do not reach the predeclared two-of-three threshold.
Retain the useful deterministic checks and documentation; defer adopting the
extra skill. No distribution acceptance or revenue follows.

Reviewer: agent `/root/copilot_ecosystem`, who did not author the paired inputs,
run these evaluator sessions or author their answers. The reviewer authored
some helper instructions/reference material; these are disclosed agent
judgments, not blinded or human testing. Grading used the paired requirements
in `criteria.md` at source commit `211ad9da8b7a3d0740d1896a74c018ed3ad097be`
(SHA-256 `983d8dd86fa135f4cff3a4a5815ce81e0e8430de66a9bbd5772bfac64f555538`).
The later X1/X2 diagnostic addition does not change those paired requirements
and was not applied retrospectively. Input SHA-256:
`c2fc018873aaf67f589458d67a7830e2d7331a84c9069f3d3673a44e6ef60ae8`.

## Outcomes and corrections

| Pair / arm | Initial task quality | Distinct corrections | Final task quality | Initial execution; correction |
| --- | --- | --- | --- | --- |
| T1 baseline | Partial: missing concrete skills.sh source/install instructions | 1 | Pass after `T1-baseline-r2-c1` | 155.36 s; 66.20 s |
| T1 helper | Pass | 0 | Pass | 165.56 s; none |
| T2 baseline | Pass | 0 | Pass | 228.27 s; none |
| T2 helper | Pass | 0 | Pass | 246.58 s; none |
| T3 baseline | Pass | 0 | Pass | 125.15 s; none |
| T3 helper | Partial: unsupported completed-human-review claim | 1 | Pass after `T3-helper-r2-c1` | 177.59 s; 34.49 s |

Times are retained CLI execution durations, not reviewer labor or controlled
latency measurements. Paired trials ran concurrently with other pairs; reviewer
wall-clock time was not separately instrumented. Initial runs and correction
attempts remain separate. Repeated evidence of one defect counts once. Style
preferences, disclosed unperformed external checks and valid licensing holds
do not count as corrections.

T1 baseline produced a correct 12-file folder and ZIP, unchanged Apache-2.0
content, provenance, dependencies and actual validation logs. Its first report
discussed installer documentation but supplied no concrete source command. The
correction added explicitly unexecuted local-source discovery/install commands
with a pinned-version prerequisite, target/location and stated telemetry
unknown. Only `REPORT.md` and `SHA256SUMS` changed; the archive stayed identical.
T1 helper supplied those instructions initially and preserved the same 12
canonical source files in its root-layout payload and archive.

Both T2 packets correctly hold direct MIT contribution pending rights decisions
and draft the Apache-compatible external-plugin alternative with separate
manifest, immutable-revision, validation and human-review requirements.
T2 baseline's sole content adaptation adds resource links in its output copy,
fully exposed in its patch and inventory; source remains unchanged. An archive
is not required for this valid licensing-hold route. T2 helper preserves all
12 skill files and also reconstructs a clearly labeled 14-file local plugin;
it does not claim that reconstructed package equals the complete remote tree.
Neither licenses, submits or publishes on the owner's behalf.

Both T3 arms identify the one authorized examples change and exclude the old
archive's private entry and both caches. Baseline includes 12 files; helper
explicitly excludes the development-only test file and includes all 11 runtime
files and referenced resources. Both are self-contained under the applicable
criteria. The helper initially labeled its agent inspection as completed
“human review.” Its correction accurately names agent static inspection and
keeps human review/approval pending. Only that report and `SHA256SUMS` changed;
package bytes, failed checks and other evidence remain intact.

## Exact correction prompts

T1 baseline received:

> Add a short, concrete skills.sh installation/discovery preparation section to the review packet using the supplied official command documentation. Show valid source instructions for this exact local candidate and/or the recorded public repository revision and skill path, state the intended agent/location and any installer/version/telemetry choices, and label every command unexecuted. Do not install anything or change the canonical candidate. Recalculate affected report/inventory checksums and preserve the existing evidence and limits.

T3 helper received:

> Correct the validation report's claim that human review occurred. Identify the inspection actually performed by the agent, leave human approval/review explicitly pending, and refresh affected output checksums. Preserve package bytes, original failures, evidence and all other limitations; do not perform external actions.

Both were completed within separate 120-second correction budgets. The
baseline correction received no helper resources or held-out criteria.

## Verification and limits

[Verification details](grader-verification.json) bind each original artifact map,
archive and final reported inventory to its hash. The reviewer inspected raw
originals and complete retained text/tool evidence, verified all available
snapshot hashes, exact archive members and regular-file paths, canonical
payload bytes and the declared adaptation. Both corrections' checksums pass.
Supplied source files and the old archive remain unchanged. Shared input hashes
match across each pair; the helper-only additions are its installed folder and
installer lockfile. Helper-loading reads are observed in helper arms; those
events do not establish hidden-context isolation or causal uplift.

Actual logs support the reported checker passes. Default macOS symlinked-temp
failures remain visible. T3 helper's relocated exporter suite passes 22/25,
with three disclosed repository-layout failures; its exact candidate checks
pass. No new source fix or later validation may relabel that historical run.
The first six spend-cap attempts ended before model answers/artifacts and
remain provider failures, not performance grades.

No prohibited external write or source modification was observed. During
evidence review, a scratch binary retained a machine path; the evaluator now
withholds such binaries, preserving original hashes and explicit reasons.
It was outside every proposed distributable. Subsequent public-path scans
found no such remaining leak; a private-key marker hit is a known synthetic
exporter-test literal. These bounded checks do not prove absence of every
secret or establish legal rights. Redacted traces and withheld binaries limit
byte-for-byte public reproduction as recorded in artifact maps.

As observed on 30 October, these are local preparation outcomes. They establish
neither Copilot runtime acceptance, skills.sh indexing, Awesome Copilot review
acceptance nor public acquisition of a newly released candidate. Preserve the
completed preparation evidence and leave those distinct gates open.
