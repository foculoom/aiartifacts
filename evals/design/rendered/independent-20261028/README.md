# Independent rendered evaluations — October 28, 2026

**Behavior assessment: R1–R4 pass the defined held-out criteria.** This is a
bounded evaluation of Design guidance, not acceptance of all four fictional
interfaces: R1, R2 and N5 require rework; R3 and the inspected N4 scope are
accepted. No source fixture was corrected to force an evaluation pass.

## Evaluation identity and isolation

Evaluated source and skill revision:
[`7b6bf416173666d20b35def9c1200e0054122356`](https://github.com/foculoom/aiartifacts/commit/7b6bf416173666d20b35def9c1200e0054122356).
Each case ran in a separate fresh Codex agent context with only its assigned
input packet, revised skill/reference copies, original fixture files, supplied
captures and normal runtime utilities. The orchestrator dispatched each using
`fork_turns:none`. The held-out assessment, runner assertions, PR/audit text and
previous answers were excluded. The complete answers below were fixed before
assessment. No evaluator was the implementing agent or the final PR reviewer.

The exact deployed model identifiers were not exposed and remain **unknown**;
these are not cross-model results or human reviews. The browser runs used Node
24.19.0, Playwright 1.62.1 and headless Google Chrome 156.0.8078.48, isolated
contexts and loopback-only fixture servers. Page requests were restricted to the
local origin. All cases inspected actual pixels and exercised their requested
local journeys. The supplied screenshots were distinguished from newly
exercised behavior. Desktop was 1280×900 and narrow was 390×900 CSS pixels;
neither establishes physical-phone usability.

The [publication manifest](publication-manifest.json) records the original and
public SHA-256 of every retained input, complete answer, action receipt, script
and PNG. Each case's `input-provenance.json` records exact skill/reference,
fixture and supplied-capture hashes. Those hashes were independently recomputed
and matched the evaluated commit when preparing this record. `input.md` is the
complete evaluator instruction after the path-only normalization below.

## Assessed results

Assessment date: October 28, 2026, after the four answers completed. Assessors:
the orchestrating Codex agent (independent of implementation, preliminary rubric
assessment) and the implementing Codex agent (subsequent evidence reconciliation).
Both are agent assessments. The implementing assessor read the complete reports,
receipt action summaries and held-out criteria, verified packet identities and
inspected representative newly generated pixels. It did not repeat the
evaluators' browser actions or claim inspection of every archived PNG. Final
exact-head PR review remains separate.

| Case | Actual run (UTC; all October 28 PDT) | Evidence and rubric assessment | Limits retained |
| --- | --- | --- | --- |
| R1 | October 29, 03:31:28–03:31:32 | **Pass.** [Complete answer](r1/report.md) and [87 state snapshots](r1/action-receipts.json) cover starting, active, overview and recovery with pointer, keyboard and emulated touch. Detects enabled-looking no-ops before Start and in Overview, preserves working Undo/Restart and proposes state-derived availability rather than changed game rules. Additional focus-loss observation is explicitly an optional usability hypothesis. | Physical device, assistive technology, measured contrast and dense-board readability remain unverified. Only the primary eight state renders and one additional focus render were personally inspected among the new captures. |
| R2 | October 29, 03:36:22–03:36:26 | **Pass.** [Complete answer](r2/evaluation.md), [action receipts](r2/action-receipts.json) and [contrast/capture receipt](r2/capture-and-contrast-receipts.json) distinguish working delivery/reset from the supplied visual target. Identifies dominant collection information, indistinguishable courier/props/dock, weak phone-size task hierarchy and destination feedback. Preserves palette, scope, recovery and reduced-motion behavior; no demand claim. | Target is supplied as approved; its underlying owner record is absent. Proposed contrast/size targets are labeled proposals. No physical device, complete accessibility review or exhaustive motion study. |
| R3 | October 29, 03:38:34–03:38:38; supplemental touch run from 03:40:40 | **Pass.** [Complete answer](r3/report.md), [main actions](r3/action-receipts.json) and [supplemental checks](r3/additional-checks.json) preserve the plain visual direction, both selections, review/back/Escape behavior, Help and return focus at both sizes. Acceptance stays bounded; no game or illustration requirements are imported. | The headless ArrowDown/Enter select attempt failed; `selectOption` then verified application behavior. Native keyboard choice and complete modal Tab cycle remain unverified. The failed first run is retained and is not passing evidence. |
| R4 | October 29, 03:43:16–03:43:39 | **Pass.** [Complete answer](r4/evaluation.md) and [decisive action receipt](r4/action-receipts.json) distinguish N4/N5, preserve N4's supplied earlier milestone, and find N5's 944px document at 390px. The 36 pointer/independently focused keyboard/fragment checks preserve functional navigation while showing sideways displacement. Requires a narrow-layout correction and new matching review. | Original N4 approval report/date are not supplied. The [exploratory receipt](r4/exploratory-action-receipts.json) has misleading requested-target labels from an imperfect Tab sequence; it is explicitly superseded by the decisive run. Fragment checks were within an existing page, not a cold-load race test. |

R3's disclosed keyboard limits do not make the case partial: the assigned
selection/review/return interactions, target sizes and return focus were
actually exercised, and the criterion requires bounded claims rather than full
native keyboard certification. Broader keyboard acceptance remains unverified.
Likewise, R4's final run directly verifies the focused anchor before activation;
the unsuccessful exploratory labels are not evidence of successful navigation.

These small cases support the observed behavior only. They do not demonstrate
human art-direction quality, creative asset generation, broad product
acceptance, universal accessibility, enjoyment, demand, or correctness across
models and devices. The new Release wording received source review and existing
verifier tests; these Design cases do not exercise a real publication workflow.

## Complete record and path normalization

The case directories retain complete evaluator answers, action receipts,
original capture PNGs, test-script text and unsuccessful exploratory evidence.
Original local reports remain unchanged outside tracked source. Only these
machine-specific path strings were normalized in the public copies:

- The evaluator's absolute output directory becomes `.` so report links point
  to the adjacent retained evidence.
- Its absolute packet-parent directory becomes `/EVALUATOR_PACKETS`.
- Installed Node, Playwright and browser locations become `/NODE_EXECUTABLE`,
  `/PLAYWRIGHT_PACKAGE` and `/CHROMIUM_EXECUTABLE`.

The manifest discloses each affected file and replacement count. No findings,
timestamps, measurements, uncertainty, failed checks or evaluator wording were
otherwise edited. Original-report hashes therefore differ from public hashes
only where those path substitutions occurred. PNG bytes are unchanged. Generic
loopback origins and agent role identifiers are retained; no credentials,
customer data, account identifiers or private product material appear here.

Archived scripts preserve the evaluated procedure; placeholders make them
evidence, not turnkey installed commands. Do not run them against their retained
output directory. To reproduce, use a new scratch packet/output, supply the
existing local runtime paths, and repeat the assigned case independently. The
supported [fixture runner](../README.md) remains separate and refuses to reuse
an evidence directory. No dependency or CI job is added by this record.

## Remaining acceptance and distribution

The evaluated skills, references, prompts, fixtures and original render runner
are unchanged in this evidence follow-up. Reconcile this record with the final
source head, independent PR review and required checks before source adoption.
An explicit source pin is not installation or a public package release.

Public acquisition remains the existing [v0.5.0 release](https://github.com/foculoom/aiartifacts/releases/tag/v0.5.0),
last verified October 28. No new package, tag, consumer installation, live
service or release authorization is established here. Publication remains held
pending required acceptance and the owner's separate release decision.
