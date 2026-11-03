# Input-only evaluation: PT1–PT8

This is agent analysis of eight fictional cases using the supplied candidate guidance. No product was opened, no test was executed, no participant was recruited, and no external action was taken. Proposed checks below are plans, not results. Toolkit commit, brief revisions and exact artifacts are unknown unless specified in the case. Each eventual result belongs in the owning project's existing test/finding and acceptance record, with evidence mode, artifact identity, steps, actual outcomes, limits and next owner/action. No numerical quality scores or release approval are supplied.

## PT1 — Maple Notes

**Panel and requirements:** P1 first-time novice for first capture, P6 distracted/returning user for interrupted-draft recovery, and P2 experienced user for a compact repeat-capture/Undo check. These are behavior hypotheses mapped to the stated single-user desktop audience, not recruited people. The highest-risk context is interruption during autosave. Expected retained content must match the exact last saved text, while any newer unsaved edits must be distinguishable. Autosave timing and the contract for closing or restarting before saving need clarification rather than an invented promise.

**Planned checks:**
- Start with a fresh local profile. From the advertised entry point, create a note containing a known synthetic string with punctuation and line breaks. Record visible entry cues, actions, help needed, text and saved/unsaved feedback. Wait for the documented save condition and verify the saved content by reopening the note.
- Edit that text, make an ordinary mistake, use Undo and compare the resulting text with the expected exact string. Repeat capture once to inspect unnecessary steps and whether state remains understandable.
- Record a checkpoint with confirmed saved text; then add a distinguishable unsaved suffix and interrupt through a supported app lifecycle action. On return, compare restored content with the checkpoint and the documented interruption contract, inspect focus and the next available action, and check whether loss or pending saving is honestly explained. Separately test an interruption after confirmed saving. Record interruption type and elapsed time when executed; a brief pause is not a long-term return study.

**Now:** Simulated planning only. Preservation, autosave, Undo, comprehension and usability are unverified. A future novice session should use someone who has not studied implementation; resetting product state does not reset reviewer familiarity. Accounts, cloud sync, social interaction, purchases and game controls are inapplicable. No production gate is introduced just for this plan.

## PT2 — Still Pond

**Review plan:** Use P3 critical evaluator, P2 veteran player and P4 gamer/developer, each tied to the actual short, silent, turn-based brief. Treat unlimited Undo and local progress as material promises. P3 compares the promised experience with a representative success and failure journey and separates defects from taste. P2 tests learned rules, repeated choices and useful depth within the intended short format. P4 first performs the visible input journey, then investigates reproducible state-boundary failures with disposable saves and fixtures; internal calls are not substitutes for player actions.

Once an executable candidate is available, record its identity, supported input and viewport/runtime. Plan starting/control discovery, a representative challenge, an error and Undo, help/pause if supported, recovery and resumption, and verified local progress across relevant lifecycle events. Inspect actual play states and feedback against the approved visual target. Preserve silence and short duration: absence of audio, realtime movement, a large world or extended content is not a defect. An unlimited-Undo promise merits checks over repeated valid moves and recovery boundaries, not a claim that a finite sample proves all possible histories.

**Now:** Only agent analysis from a screenshot description and brief is possible. There is no actual screenshot inspection, rendered craft assessment, working-input evidence, measured play duration, verified Undo/progress, or evidence of enjoyment, replayability, demand or willingness to pay. Any risks or recommendations are hypotheses. Three reviewer lenses, whether produced by one or several agents, are not three human participants.

**Human gate:** Do not mark the human playtest complete. Obtain an actual consenting, appropriately recruited human session under the owner's policy and record build, task, assistance, duration and observations privately. If the designer intends to waive or alter a gate, confirm their authority and record that explicit policy change as a waiver/change, never as a completed human session. Any required experience acceptance remains unverified for the unavailable artifact, and release authority remains separate.

## PT3 — Orchard Booking

**Boundary:** Do not click production Reserve, even once. The approved scope is read-only and that action may create a paid booking or send a customer confirmation. Adopting P5 rushed/impatient user grants no additional authority.

**Relevant plan:** Use only the isolated local synthetic fixture, ensuring it cannot contact production services. Define a single intended reservation and a controlled five-activation sequence; record timing as a test parameter, not human behavior. Inspect pending feedback, whether repeated activation is prevented or safely consolidated, the number of synthetic records created, and success/failure state. Include a delayed-response and failed-response fixture to examine safe retry and recovery. Use a known faulty fixture or controlled duplicate-handling perturbation to demonstrate that the test detects duplicates. Preserve original failures as well as any later fix evidence.

The expected fixture outcome is one logical reservation for the one intended action, clear pending and final status, and no misleading confirmation. This is a planned scripted or agent-operated UI check depending on the tools actually used; currently nothing has run. Record which layer implements the protection rather than assuming a disabled button proves server deduplication.

**Limit:** Passing the fixture would establish only the exercised local behavior for that fixture revision. It would not prove production idempotency, provider booking creation, charges, confirmations or delivery. Provider-level proof requires separately authorized integration/sandbox tests and inspection of resulting provider records; any proposed production test needs explicit authorization covering its consequences. Do not manufacture a real receipt or treat visible success copy as delivery evidence.

## PT4 — Shelf Finder

**Selection:** P1 novice for forming a query and interpreting results, P2 experienced user for repeated search/navigation, and P6 returning user for retaining context if that behavior is supported. The highest-risk overlays are keyboard/alternative input and low vision/enlarged text, directly mapped to the brief. Screen-reader semantics and motion/sensory overlays are relevant to the source features mentioned, without assuming a single “disabled user” persona or a diagnosis.

**Source-only work:** Inspect whether labels describe their controls and whether structural focus/order, interactive elements, result-state messages and the reduced-motion rule plausibly support the intended tasks. Identify specific code-backed defects if actually demonstrated; otherwise label concerns as hypotheses. The mere presence of aria labels does not establish correct semantics, and a media query does not prove that all relevant motion is reduced. No actual source snippets are supplied in this case, so even those detailed inspections are only a plan here.

**Next evidence:** Render a named build and execute keyboard navigation through query, results, empty/error states and return paths, recording focus visibility/order, traps and dialog behavior where relevant. At the enlarged-text settings required by the brief, inspect clipping, overlap, legibility and task reachability. Exercise actual reduced-motion settings and, when available and relevant, actual assistive technology for names, reading order and announced changes. Record tool/runtime/settings and untested scope. Human accessibility research is a separate consenting activity when required or appropriate.

**Conclusion:** “Accessible for disabled users” is not established. Mark promised interactive keyboard and enlarged-text behavior unverified with current tools, not passed and not automatically a whole-product failure. Source inspection and automated checks cannot certify accessibility.

## PT5 — Parcel CLI

**Scope:** Use P7 cautious explorer only, proportionate to the owner's request. Map it to understanding command consequences, selecting an explicit input/output, recognizing failure and preserving an existing output. Do not expand to a full panel or invent graphical controls, a preview flag, Undo, accounts, payments or services.

**Document review and synthetic plan:** Review the documented invocation, input/output selection, success/error semantics and overwrite warning or refusal contract. Plan disposable local directories containing synthetic files, with an independent manifest of paths and content hashes. Include a valid input, nonexistent or otherwise invalid input, and a pre-existing output archive with known bytes. Execute only if authorized later, recording exact tool/build version, commands, inputs, stdout/stderr and process exit status. Check that invalid input produces the promised clear failure code and useful diagnosis. Verify that the pre-existing output remains byte-identical and no unintended files were changed; do not infer safety from an error message alone. For a valid transformation, inspect archive contents against the input manifest. The documented recovery path should permit correcting input or choosing an unused output without destructive steps.

**Evidence and conclusion:** The current material supports a review plan only, not verified command behavior. A documentation mismatch can be substantiated only from actual documented text; executed synthetic commands and filesystem verification would substantiate the bounded failure/no-overwrite behavior. No screenshot, visual composition, game-art, touch, purchase or provider-delivery review applies to this nonvisual local tool. Install or run nothing outside existing authorization. Keep cautious-user understanding as a hypothesis unless actual human evidence is collected; no human gate is invented for this request.

## PT6 — Tutorial harness

**Established by the supplied description:** The reported 100% measures an unconditional completion flag following a direct finish_tutorial() call, not visible tutorial completion through supported input. The accuracy setting is disconnected from the shrinking input window, so these runs cannot establish player success under the changing timing constraint. Fixed seeds make configured runs reproducible, not behaviorally valid. One author creating four persona summaries supplies one agent's synthetic analysis, not four independent participants or evidence of novice comprehension. I have not independently run or inspected this harness.

**Next discriminating checks:**
1. Preserve the original reports, seeds, parameters and exact harness/build identities. Trace each metric to its actual event and distinguish direct internal calls from UI input.
2. Add a known-failure scenario: prevent a required tutorial step, use invalid/no input, or block the completion transition in a disposable fixture. The harness should report incomplete/failure; a continuing pass demonstrates a broken measurement path.
3. Remove the unconditional success assignment and direct-completion bypass from the user-path test. Drive the supported visible inputs, record tutorial checkpoints and independently verify the actual completion state. Keep internal unit tests separately labeled.
4. Use controlled input timings near and outside the window, plus a deliberate window change with otherwise comparable conditions. Verify success/failure tracks the real acceptance boundary. If a policy accuracy model is retained, demonstrate its connection to timing and report its assumptions; do not present synthetic probabilities as measured human performance.
5. Rerun the affected scenarios with recorded seeds, action logs and visible state evidence, retaining failures and bounded fix results rather than selecting only favorable trials. A rendered agent run can verify that input path but still cannot prove natural human understanding.

**Gate:** The required actual human onboarding session is incomplete. Run and document one consenting human session on the relevant final build, with recruitment fit, assistance and observed outcomes. Harness correction or agreement among agent personas cannot satisfy that requirement. Only the authorized owner can explicitly change the gate, and such a change is not a human test result. Do not accept the tutorial or broader release based on the present completion report.

## PT7 — Narrow correction

No. A CSS comment spelling change from “widht” to “width,” with no runtime effect and no product-testing request, does not warrant a persona panel, human study or game production review. Proportional verification is a narrow diff check confirming only the intended comment changed, plus any already-required repository checks. Preserve existing acceptance decisions and holds; there is no affected interactive journey to reopen merely because of this comment. This evaluation does not perform the edit or claim a diff was inspected.

## PT8 — Correctly scoped simulator test

**Evidence classification:** The supplied record describes an agent-operated UI test, not simulated-persona analysis, scripted internal-method proof or a human session. The named build is B12; the phone simulator runtime and operator were recorded in the underlying test. Their exact identifiers, capture date and evidence references are not reproduced in this input and should be retained from that record, not invented.

**Established within that record:** On B12 in the recorded simulator with touch input and a synthetic draft, the agent exercised opening an event, canceling an edit, backgrounding, resuming and checking draft and focus state. This provides execution evidence for that particular journey and observed state checks. Record the exact before/after draft and focus assertions from the actual evidence. If those observations satisfy the owning cancellation/resumption criteria, that behavior can be accepted within this scope because the owning policy permits this simulator coverage. The description does not justify embellishing the observations with exact values it does not provide.

**Unverified:** Human comprehension or satisfaction; physical-device behavior; other simulator/runtime or build variants; keyboard or assistive-technology paths; other lifecycle conditions such as process termination, relaunch or extended return; real invitations, delivery and provider integration; broader accessibility, experience quality and release authorization. These are coverage limits, not automatically new blockers or required features. No physical-hardware prerequisite is added. Simulator execution is real execution in that runtime, and absence of a human does not invalidate the owner's accepted behavioral evidence. Any separate human or release gate remains separate.

## Provenance appendix

All five allowed inputs were read for this input-only evaluation. The parent reported one intervening change to SKILL.md; I reread its current version and confirmed that the owning project's severity scale is primary and P0/P1/P2 is only a fallback when no project scale exists. This correction changes none of the PT1–PT8 conclusions: the evaluation assigns no competing severity scale. The hashes below identify the final inputs as checked on 2026-11-03. No assessment, README or other candidate file was read.

SHA-256 (paths relative to candidate/):

- plugins/design/skills/experience-review/SKILL.md: 811314153a04b9e0d3318c7b67fa22623658614f8420926e2f09d078ca6dcad3
- plugins/design/skills/experience-review/references/product-testing-personas.md: 49fcea73baa48e97a00cc45dfa704a1371e50ec6da2c86d6c8f502c1f8455d02
- plugins/design/skills/experience-review/references/interactive-experiences.md: 6339fa9dbc6f063deb61b1d92a4b37974c57dadbde7f1104ec469ac981413412
- plugins/design/skills/experience-review/references/production-acceptance.md: c0fdf56d5287eed4468de8c1c1ce3d9c8adab12f5cd06caa2d36e4cc7403fb9d
- evals/design/personas/inputs.md: 4db99f3d526c5a64eb650eda2431f9b4d59a9dcfa83fa9917975d7693e421d2a

### Final-input recheck — 2026-11-03 09:08 UTC

Reread only the allowed product-testing-personas.md following the parent's notice of the final selection-step correction: “Consider novice, experienced user and the highest-risk context; select only lenses relevant to the requested scope or a distinct risk.” This removes any implication of a compulsory baseline panel. None of the PT1–PT8 conclusions changes. In particular, PT5 already selects only the requested cautious-user lens, PT7 introduces no panel, and the additional PT1/PT4 lenses are tied to stated tasks or conditional risks rather than a mandatory count. No held-out assessment was inspected.

Final product-testing-personas.md SHA-256: aaadff05583f54d3d1bb5f08da62048e2f73a1ac8a981da0f5c6574cb2ec88a6.

The preceding provenance entry preserves the earlier input hash (49fcea73baa48e97a00cc45dfa704a1371e50ec6da2c86d6c8f502c1f8455d02) rather than overwriting the evaluation history. The answer-file SHA-256 before this appended recheck was 0d922eba77d65d2491dd350bf952539493608f9f75580dc44f892f32dbfe5a7f. Other input hashes remain as previously recorded; they were not reread for this limited recheck. The final answer-file hash is reported separately because embedding its own hash would change it.
