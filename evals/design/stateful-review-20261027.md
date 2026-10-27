# Stateful experience-review behavior evidence — 2026-10-27

## Evaluation identity and method

- Evaluated source head: `33347aec63e53f6226a64e0905db2f4a15f96123`.
- Skill: `plugins/design/skills/experience-review/SKILL.md` and
  `plugins/design/skills/experience-review/references/interactive-experiences.md`
  at that head.
- Input brief revision: D9 and D10 in `evals/design/cases.md` at that same head.
  These are fictional fixtures, not evidence about a released product.
- Evaluator: a Codex agent. The exact model/deployment identifier was not
  exposed in the evaluation context and is recorded as unknown.
- Tools: read-only local shell reads and `git rev-parse HEAD`. No browsing,
  rendered interfaces, actual input/device tests, external mutations, or source
  edits were used to produce the responses.
- The initial run loaded the skill and interactive reference, then only D9 and
  D10. The evaluator did not read `evals/design/README.md`, previous evaluation
  records, or expected behavior before returning both complete answers.
- That initial run used one fresh evaluator context for both cases. It was not
  a separate fresh session per case. Isolated follow-ups are recorded below to
  distinguish the procedure in the [evaluation instructions](README.md).
- After the initial answers were fixed, the recording agent read the expected
  behavior and assessed them. These are agent assessments of synthetic answers,
  not human user studies, repeated cross-model trials, automatic skill-routing
  tests, or independent review of the later commit recording this evidence.

The following two sections preserve the complete initial case answers, with
heading levels adapted to this record. No product tests were performed by the
evaluator: statements about controls and artifacts rest on the supplied cases.

## Initial D9 answer

The two supported corrections concern C9's misleading enabled appearance before
Start and in Overview. Preserve its working controls and P7's existing navigation
while checking the remaining state and device gaps.

Review record:

- Skill revision: `33347aec63e53f6226a64e0905db2f4a15f96123`.
- Brief revision: unknown; supplied Lantern Gallery fixture.
- Artifacts: released payload hash `P7`, canonical source commit `S8`, unpublished
  candidate ZIP `C9`. A separate C9 digest was not supplied.
- Audience: browser-game players; specific target devices and approved identity
  brief unknown.
- P7 observation date: today, **2026-10-27**. Dates for the other supplied checks
  are unknown.
- This is a review of reported evidence. No source files or rendered builds were
  independently inspected.

### Starting

- **P7:** Start and room-menu screens have no active link to the archived
  prototype. Its direct `/archive/` route remains reachable.
- **S8:** Canonical source contains the active archive link. That establishes a
  source difference; it does not establish what a deployed S8 build would
  currently show.
- **C9:** Before Start, Move and Restart look enabled but do nothing. The fixture
  does not describe the primary Start action, help, settings, or keyboard focus.

### Playing

- **C9:** Move and Restart work during play, and the candidate adds touch
  controls. Preserve that functionality. The fixture does not specify the input
  method used for these action checks, device, focus behavior, or repeated-input
  results.
- **P7/S8:** Active-play behavior is untested in the supplied evidence.

### Overview

- **C9:** Move and Use look enabled but do nothing. Undo and Restart still work
  and should remain available.
- The whole Overview board fits a **390px browser-emulated viewport**. That
  establishes fitting, not readability or physical-phone usability. No phone
  player identified its mechanisms or demonstrated the exit route.
- The resume route, keyboard behavior, and other viewport behavior remain
  unverified. P7/S8 Overview behavior is also unverified.

### Recovery

- **C9:** Undo and Restart work in Overview; Restart also works during play.
  Their effects on saved progress and focus were not supplied.
- Reload was checked only in C9's local browser. Its outcome was not reported,
  so persistence, restoration, and successful recovery cannot be claimed.
- Recovery behavior in P7 and a rendered S8 build remains unknown.

### Actionable findings

1. **P1 defect — C9 starting controls imply unavailable actions are usable.**
   Component: pre-Start Move and Restart; source file unverified. Evidence: both
   look enabled and do nothing. This gives players an inaccurate action cue.
   Smallest correction: make these controls visibly and semantically unavailable
   before Start, or hide them in that state. Preserve usable help and the primary
   entry action. Acceptance: before Start, their unavailable state is clear for
   applicable input methods; after Start, their existing working behavior
   remains available.
2. **P1 defect — C9 Overview exposes misleading Move and Use controls.**
   Component: Overview actions; source file unverified. Evidence: Move and Use
   look enabled but do nothing, while Undo and Restart work. Players cannot
   reliably distinguish available actions. Smallest correction: mark only Move
   and Use unavailable, or hide them in Overview. Preserve Undo and Restart.
   Acceptance: Overview accurately communicates available actions; Undo and
   Restart retain their working behavior, and players can identify and exercise
   the return-to-play route.

The S8/P7 archive-link difference is an observed artifact discrepancy, not yet a
demonstrated visitor defect. Confirm the intended navigation before reconciling
it. Preserve the working direct `/archive/` route; this review supplies no reason
to promote it into primary navigation.

### Smallest next checks

- Record C9's digest, observation date, and the actual artifacts used for
  subsequent checks.
- In a safe C9 build, check the corrected starting and Overview affordances using
  keyboard and touch separately, including focus and the resume route.
- Record what reload actually restores in C9, then check the relevant recovery
  path in P7 and a build corresponding to S8 without overwriting saved progress.
- Ask a target-phone player to identify a relevant Overview mechanism and exit.
  Record device, input, artifact, and result.
- Compare the affected routes and actions across P7, rendered S8, and C9 before
  a release decision. Review the navigation intention alongside that comparison.

### Public availability

As reported on **2026-10-27**, **P7 is the current public payload**, and its direct
`/archive/` route is reachable. C9 is unpublished and therefore unavailable to
public users. S8 is canonical source, not evidence of a separately available
public build. Full public gameplay and recovery were not tested here.

C9's working in-play controls and working Overview Undo/Restart are demonstrated
candidate functionality worth preserving. No acceptance or release approval was
supplied. The remaining release decision concerns C9 after the bounded checks
and affordance corrections above.

## Initial D10 answer

No defect is established in the supplied booking flow. Preserve its existing
action availability and recovery behavior.

Review record:

- Skill revision: `33347aec63e53f6226a64e0905db2f4a15f96123`.
- Brief revision: unknown; supplied library-booking fixture.
- The released page, canonical source, and candidate reportedly match by
  recorded hashes. The actual hash values and observation dates were not
  supplied.
- Scope: selection, Submit availability, confirmation-dialog cancellation, and
  local keyboard/touch behavior. No broader booking journey was reviewed.

Before a selection, Submit is visibly disabled and excluded from sequential
focus, while Help remains usable. This correctly communicates that submission
is unavailable and preserves assistance.

After selection, Submit becomes operable. Preserve that relationship between
selection state and action availability.

While the confirmation dialog is open, form actions are disabled. Cancel
restores both focus and the selection. Preserve this recovery path: the user can
back out without losing the choice or their place.

The supplied local keyboard and touch tests passed. Those results support the
tested flow; they do not establish coverage of unspecified devices, browsers,
assistive technologies, or every accessibility behavior. Dialog focus entry and
containment, labels, contrast, and error handling were not individually
documented.

No real booking was submitted. Submit becoming operable does not establish
booking creation, confirmation delivery, or a successful customer transaction.
If transaction behavior needs validation within this flow, exercise it against
a safe local fixture and record the result.

The matching artifact hashes support consistency among the three recorded
artifacts. Include their actual values and dates in the review record so later
changes can be distinguished. No source file was verified here.

The fixture identifies a released page, but supplies no availability observation
date. Successful public booking remains unverified. No redesign or control
change is supported by the supplied evidence.

## Initial assessment against the withheld expectations

The recording agent read the [expected behavior](README.md) only after the
initial answers had been returned.

| Case | Decision | Evidence from the fixed answer |
| --- | --- | --- |
| D9 | Pass for the expected observable behavior | Separates public P7, source S8 and unpublished C9; preserves the working archive route and P7 navigation; flags only the misleading pre-Start and Overview affordances; preserves working Move/Restart in play and Undo/Restart in Overview; proposes a phone-player item-identification and exit check; leaves physical-device/native usability and persistence unverified. |
| D10 | Pass for the expected observable behavior | Preserves disabled Submit before selection, working Help, enabled Submit after selection, disabled actions during confirmation, and Cancel's focus/selection restoration. Finds no supported defect, claims no real booking, and introduces no movement, turn-timing, or Overview rules. |

The initial run alone is partial compliance with the prescribed execution
procedure because both prompts shared one fresh evaluator session. These pass
decisions describe the answers, not independent per-case execution or a release
gate. The source and prompt revisions are known even though the answers correctly
leave the fictional products' own brief revisions unknown.

## Isolated per-case follow-ups

Each follow-up used a newly spawned evaluator with no parent conversation
history. Each received only the repository path, exact expected source head,
the two skill paths, and an instruction to extract its single case and respond.
Expected behavior, other cases, handoffs, prior records, browsing, UI tests and
edits were explicitly excluded. Both requested source files and the case file
remained unchanged at the evaluated head. The recording agent's pending evidence
file was outside the allowed evaluator reads. The exact model/deployment
identifier was unavailable in each evaluator context.

### Isolated D9 complete answer

Source HEAD: `33347aec63e53f6226a64e0905db2f4a15f96123` — verified and matches the
requested revision. The loaded skill and interactive-experiences reference are
from that checkout. Exact model identifier: unavailable. Brief: D9, “Four states,
three artifacts”; separate brief revision unknown.

This is a read-only review of the supplied fictional evidence. I read only the
two requested skill files and extracted D9. I did not browse, execute UI tests,
inspect other cases or expected behavior, or edit files. Statements below report
the fixture's observations, not tests I performed.

Lantern Gallery's candidate has two state-dependent control problems: actions
appear available before Start and in Overview even though their handlers do
nothing. The smallest correction is to make those specific unavailable actions
visibly unavailable while preserving the actions that work.

| Artifact | Supplied observation and date | Public availability |
| --- | --- | --- |
| Public payload `P7` | Read today, **2026-10-27**. Start and room-menu screens have no active archive link. Direct `/archive/` access still works. | `P7` is publicly served, and visitors can reach `/archive/` directly. Complete public gameplay was not established by these observations. |
| Canonical source `S8` | Contains an active archive link. Observation date unspecified; rendered behavior not supplied. | No evidence establishes that an `S8` build is currently served. Its source content does not override the observed `P7` behavior. |
| Candidate ZIP `C9` | Adds touch controls; state observations are detailed below. Observation date unspecified. | Unpublished. Public visitors cannot obtain these candidate changes through the documented release. |

The audience is browser-game players; the primary entry action is Start.
Approved identity, detailed audience/device requirements, and a separate brief
revision were not supplied. These limits prevent an identity or visual-style
judgment.

**Starting.** In `P7`, the absence of an archive link from Start and the room menu
is an observed public milestone worth preserving; the direct archive route
remains available. In `C9`, Move and Restart look enabled before Start but do
nothing.

- **P1 defect — `C9`, pre-Start controls.** The supplied appearance and behavior
  disagree, inviting ineffective input and leaving players uncertain whether
  the game responded. Source files are unverified. Make Move and Restart visibly
  unavailable until their actions are usable, with appropriate programmatic
  state for the control implementation. Keep usable help reachable.
- **Acceptance:** Before Start, unavailable actions are clearly conveyed; after
  Start, Move and Restart become usable. Check this with keyboard and touch
  separately. The behavior of Start itself, help, settings, and initial focus
  remains unverified.

**Playing.** In `C9`, Move and Restart work during play. Preserve that working
behavior and the candidate's touch-control addition. The fixture does not
identify which input method exercised them, so it does not establish working
touch gameplay, keyboard parity, or behavior in `P7` or an `S8` build.

The smallest next check is to exercise those controls once through touch and
once through keyboard in the exact candidate, checking resulting state,
feedback, repeat behavior, and focus. Also verify the route to Overview and back
to help/settings.

**Overview.** In `C9`, Move and Use look enabled but do nothing; Undo and Restart
still work.

- **P1 defect — `C9`, Overview controls.** Move and Use misrepresent availability.
  Make those actions visibly unavailable in Overview while preserving functional
  Undo and Restart.
- **Acceptance:** Move and Use communicate their unavailable state; Undo and
  Restart still produce their intended results; the route back to play is clear
  and operable, with predictable focus. Do not disable the whole control group.

At a **390px browser-emulated viewport**, the board fits. This establishes layout
containment only. Mechanism recognition and physical-phone usability remain
unknown. The smallest legibility check is to ask a target-phone player to
identify a relevant mechanism and exit Overview, recording the actual device,
input, artifact, and result. No redesign is supported by the current evidence.

**Recovery.** `C9`'s working Undo and Restart in Overview are useful recovery
capabilities and should remain. Reload was checked only in `C9`'s local browser;
the fixture supplies no reload outcome or retained-state result. Persistence,
recovery focus, instructions, and public recovery therefore remain unverified.

For the next check, establish a known game state, exercise Undo and Restart
separately, then reload and compare the actual state with the documented
retention/reset rules. Record focus and instructions after each transition.
Local `C9` results must not be generalized to `P7`.

The archive-link difference is an **unresolved source/release divergence**, not
enough evidence by itself to call either artifact defective. Before release,
reconcile the intended navigation with the owner's requirements and determine
whether `S8` or `C9` would reintroduce the link. Preserve the working direct
`/archive/` route; its existence does not justify adding it to primary navigation.

Complete the bounded comparison across publicly served `P7`, a build pinned to
`S8`, and ZIP `C9`: Start, play, Overview, recovery, and archive access. Record
each exact artifact identifier, observation date, viewport/device, and input
method. The outstanding release decision is whether a corrected and checked
`C9` should be published. Nothing supplied establishes that decision, release
approval, or public availability of its touch controls.

### Isolated D10 complete answer

Source HEAD verified: `33347aec63e53f6226a64e0905db2f4a15f96123`. Skill revision:
that repository revision. Exact model identifier: unavailable. Brief revision
and fixture observation date: unknown.

I used `experience-review` and its interactive-experiences reference. This was a
read-only review of D10's fictional evidence; I did not browse, run UI tests,
submit a booking, or inspect other cases.

The supplied evidence supports keeping this booking flow. No actionable defect
is established, and no correction is recommended.

- Before a selection, Submit is visibly disabled and skipped by keyboard focus.
  Preserve this correspondence between availability and behavior, together with
  working Help.
- After a selection, Submit becomes operable. Preserve that clear transition.
- While confirmation is open, the form actions are disabled. Preserve this
  restriction.
- Cancel restores both focus and the selection. Preserve this recovery behavior
  so visitors can continue without repeating their work.

The fixture reports matching released-page, source, and candidate hashes, so it
identifies no divergence among those artifacts. The actual hashes are not
supplied, however; the verified repository HEAD above identifies the evaluation
materials, not the fictional booking artifacts.

The reported local keyboard and touch tests passed. Their viewport, device,
browser, detailed checks, and observation dates are unspecified, so they do not
establish physical-device usability or comprehensive accessibility. Dialog focus
containment, accessible names and announcements, visual contrast, responsive
layout, and error states remain unverified. No real booking was submitted;
successful booking delivery and persistence are therefore unproven. The review
covers only the selection, confirmation, and cancellation flow described.

### Isolated follow-up assessment

| Case | Decision | Evidence against the withheld expected behavior |
| --- | --- | --- |
| D9 | Pass | Separates all three artifacts and public availability; preserves P7 navigation and direct archive access; limits corrections to misleading starting/Overview controls while retaining working recovery; proposes a target-phone item-identification and exit check; explicitly leaves touch gameplay, physical-device/native behavior and persistence unproven. |
| D10 | Pass | Preserves every supplied working transition, Help, focus and selection restoration; recommends no correction; distinguishes reported local tests from independently exercised behavior and successful real booking; introduces no game-specific controls or timing. |

These follow-ups satisfy the separate-fresh-session procedure for D9 and D10.
Their pass decisions are made by the recording agent after receiving the fixed
outputs; the evaluators did not receive the expected criteria. Neither case
establishes cross-model reliability, actual interface usability, public booking
delivery, or independent review of the commit adding this record.

## Guidance observations

The evaluator found no substantial contradiction affecting these answers. It
noted two minor interpretation points, neither of which warrants changing
general guidance on this evidence:

- “Exercise each supported input” and compare “every visible action” can sound
  exhaustive alongside representative-input sampling. A bounded review should
  identify its sampled actions and untested coverage.
- Comparing canonical source alongside released and candidate artifacts does
  not explicitly say to build or render that source revision. The source-only
  limitation supplies the necessary boundary: source differences do not prove
  rendered interaction results.

No skill text, package version, tag, consumer pin, or CI configuration changes
as part of recording this evaluation. The evaluated head predates this evidence
file; independent review of the final PR head remains a separate gate.

## Recording-change validation

The initial worktree at `33347aec63e53f6226a64e0905db2f4a15f96123` was clean.
The fetched default branch remained
`8a07a07af79c90bec07629b8b9d52ec67968f31d`. This follow-up changes only this
evidence file and `HANDOFF.md`; the evaluated skill, reference, cases and rubric
are unchanged. From the repository root on 2026-10-27:

```sh
python3 scripts/validate_catalog.py
python3 -m unittest discover -s plugins/design/skills/product-identity/tests -q
git diff --check
```

Results: catalog and local Markdown references passed for six plugins and seven
skills; all seven Design export-checker tests passed; diff whitespace checks
passed. These structural and synthetic unit checks are separate from the four
recorded model responses. The existing CI still does not run the Design suite.
Final-head independent PR review and required CI remain integration gates;
neither a recorded evaluation nor a source merge publishes Design 0.1.1.
