# Reusable product-testing personas

Use this reference to plan or conduct a persona-based review of an app, game,
website or other interactive product. It extends experience review; it is not
a second QA system, a set of real participants, or release authority. Use the
owning project's existing requirements, finding IDs and acceptance record.

## Select a small, relevant panel

1. Read the current product brief, intended audience, promised task and exclusions.
   Record its revision, the exact candidate, supported surfaces and permissions.
2. Map each selected lens below to a real target audience and a requirement or
   acceptance criterion. These are reusable behavior hypotheses, not invented
   customer research. If the audience or criterion is unknown, label the assumption.
3. Consider novice, experienced user and the highest-risk context; select only
   lenses relevant to the requested scope or a distinct risk. There is no fixed
   persona count, session duration, numerical score or universal pass threshold.
4. Select only applicable product scenarios below. Agree observable outcomes
   before testing. Do not add cloud sync, audio, game controls, purchase flows or
   other features merely because another product has them.
5. Use a fresh first-use state for a novice. A reviewer who already read the
   implementation cannot claim an uncontaminated first encounter. Record that
   limitation; reset product state without pretending to reset reviewer knowledge.

Stable IDs let later products reuse these lenses without copying their full
definitions. Keep completed mappings, participants, data and results private in
the owning project. Record the exact toolkit commit and any local override.

## Shared lenses

### P1 — First-time novice

- **Goal:** Complete one meaningful task without knowing the product's terms.
- **Context and behavior:** Starts from the advertised entry point with a fresh
  state, reads prominent cues and asks for help only after attempting the task.
- **Probe:** Identify the primary action, explain the visible state, make the
  first action, recover from one ordinary error and recognize completion.
- **Evidence:** Record the action sequence, unclear labels, wrong turns, help
  used, expected result and actual result. A coached completion is not unassisted.
- **Risk:** Familiarity or implementation knowledge can conceal onboarding gaps.

### P2 — Experienced user / veteran player

- **Goal:** Reach value efficiently and understand the product's depth and limits.
- **Context and behavior:** Knows the relevant category, uses familiar shortcuts
  and repeats meaningful work. For games, tests learned rules and strategic choice.
- **Probe:** Repeat a core task, inspect relevant advanced controls, recover a
  mistaken action and compare the experience with the product's actual promise.
- **Evidence:** Record repeated steps, supported shortcuts, state changes and
  concrete friction. Mention a category convention as a comparison, not a mandate.
- **Risk:** Expert fluency does not establish novice comprehension, broad appeal,
  long-term retention, replayability or willingness to pay.

### P3 — Critical evaluator / game critic

- **Goal:** Test whether the experience honestly delivers its stated promise.
- **Context and behavior:** Skeptical but fair; follows an advertised journey and
  inspects craft, coherence, feedback and fit for the stated audience.
- **Probe:** Compare the offer with actual capability, examine a representative
  success and failure state, and distinguish defects from taste or positioning.
- **Evidence:** Cite the promise, exact observed mismatch and user consequence;
  retain successful choices. Price/value opinions are hypotheses unless supported
  by actual participant research, not synthetic purchase intent.
- **Risk:** Do not impersonate a named critic, invent endorsements or assign
  pseudo-objective quality scores. A short or intentionally quiet product is not
  defective merely for lacking another product's length, audio or decoration.

### P4 — Practitioner / gamer-developer

- **Goal:** Find reproducible failures in a realistic working or playing journey.
- **Context and behavior:** Understands the category and implementation risks.
  Performs the visible user journey before consulting code to explain a symptom.
- **Probe:** Repeated input, state boundaries, undo/cancel, interruption and
  recovery. Use disposable fixtures for failure injection and saved-state tests.
- **Evidence:** Separate UI actions from internal method calls; retain exact
  steps, artifact, inputs, logs and verified state. Label inferred causes.
- **Risk:** Direct calls, debug controls and forced completion flags do not prove
  a working user input path, a discoverable task or a genuinely completed tutorial.

### P5 — Rushed / impatient user

- **Goal:** Finish a meaningful task with little time and minimal reading.
- **Context and behavior:** Skims, uses the most prominent action, repeats a click
  when feedback is unclear, and may cancel or navigate away early.
- **Probe:** Rapid repeated input, clear in-progress feedback, Back/Cancel,
  accidental selection and protection against duplicate consequential actions.
- **Evidence:** Record actual input timing when measured, visible feedback,
  resulting records/state and recovery. Test charges or sends only with specific
  authorization; otherwise use local or sandbox fixtures.
- **Risk:** Arbitrary reaction-time or error probabilities are test parameters,
  not measured human behavior or evidence that a real user is careless.

### P6 — Distracted / returning user

- **Goal:** Resume safely after attention moves elsewhere.
- **Context and behavior:** Stops mid-task, returns later, forgets a detail and
  relies on visible context rather than remembered instructions.
- **Probe:** Background/resume, refresh or relaunch where relevant, interrupted
  onboarding or editing, expired sessions and the route back to help.
- **Evidence:** Record the checkpoint, interruption type, actual elapsed time if
  relevant, restored data, focus and next action. Use synthetic expired-session
  fixtures rather than calling a brief pause a multi-day return study.
- **Risk:** One simulated interruption does not establish long-term retention,
  every lifecycle event or the experience of a diagnostic group.

### P7 — Cautious explorer

- **Goal:** Understand consequences and keep control before committing.
- **Context and behavior:** Inspects labels, help and permission explanations;
  declines optional access, takes a reversible route and checks recovery.
- **Probe:** Preview versus commit, Cancel/Undo, denied permissions, destructive
  warnings, visibility of saving or sharing, and unavailable-service explanations.
- **Evidence:** Record what the interface promised, what changed, what remained
  private and which operations were not exercised. Verify state after cancellation.
- **Risk:** Clear copy does not prove privacy, authorization or deletion. A test
  persona never grants permission to submit, pay, share or alter real data.

## Accessibility and context overlays

Combine a relevant overlay with any lens; accessibility is not a single persona.
Describe functional needs and actual input/support settings, not a stereotype or
diagnosis. Do not claim to reproduce a disabled person's lived experience.

- **Keyboard, switch or alternative input:** Task reachability, order, visible
  focus, traps, dialog entry/exit and alternatives to drag or precise gestures.
- **Screen reader or low vision:** Semantic names, reading order, announced
  changes, zoom/text enlargement, clipping and meaningful nonvisual alternatives.
  Use the actual assistive technology when available; source markup is not a run.
- **Color perception or hearing:** Information not conveyed by color or sound
  alone, useful contrast and captions/text cues where the product relies on audio.
- **Motor or timing needs:** Target size, accidental activation, adjustable timing
  where promised, repeated input and recovery without unnecessary precision.
- **Motion or sensory needs:** Actual reduced-motion behavior, distracting changes
  and control of optional effects. Do not expose people to known unsafe stimuli.
- **Cognitive, reading or attention needs:** Plain instructions, manageable steps,
  recognition rather than recall, preserved context and recoverable mistakes.
- **Context constraints:** Small viewport, touch, localization/long strings,
  intermittent connectivity or low-resource runtime when supported and relevant.

Record unsupported tooling as untested or blocked, not a pass or an automatic
whole-product failure. Automated checks and agent inspection do not certify
accessibility. Use the owning acceptance policy for simulator/device coverage;
do not invent a physical-hardware gate. Human accessibility research, when required
or proposed, remains a separate activity with consent and appropriate recruitment.

## Product-specific scenario menu

Use realistic synthetic data. Choose the smallest set that covers the promised
journey and its material risks; mark irrelevant scenarios with a reason.

| Product | Example journey | Observable outcomes to define |
| --- | --- | --- |
| Productivity, notes or creative app | Start, create/edit, cancel/undo, save, leave and return; export if promised | Correct retained content; no silent loss or duplicate records; understandable saved/unsaved state; exported content matches the selected data |
| Search, reading or information app | Form a query, inspect results, open a source, handle empty/error states and return | Relevant navigation; source/date/uncertainty visible where promised; empty differs from unavailable; reading position or state behaves as specified |
| Communication or collaboration app | Prepare a draft, inspect audience, cancel, then use an authorized sandbox send; handle stale or conflicting edits | Intended audience and draft state; no accidental send; honest pending/delivered/failed states; conflict behavior follows the contract |
| Service, account or commerce app | Compare an offer, decline optional access, use a permitted test checkout or booking, recover from interruption | Clear total/commitment where applicable; no duplicate action; correct pending/success/failure; verified sandbox state, never an invented real receipt |
| Game | Discover controls, learn a mechanic, attempt a representative challenge, make an error, pause/help, recover and resume | Understandable cause/effect and state; working supported input; rules/timing match the brief; progress and recovery work as promised; no universal content-length or score threshold |
| Developer tool or nonvisual app | Install/use an already-authorized fixture, complete its documented task, handle invalid input and recover | Correct output/exit status, useful errors, data preservation and reproducible commands; no compulsory screenshot or game-art judgment for a surface that has no UI |

For a new genre or product category, define its own task and expected outcome
instead of forcing it into the closest row. Platform-specific checks belong to
the owning product's existing test plan.

## Execution and evidence boundaries

Record the evidence mode for each journey, not just for the whole report:

- **Agent analysis / simulated persona:** A hypothetical review from supplied
  source, screenshots or a scenario. It proposes risks; it is not a participant.
- **Scripted execution:** Deterministic actions actually executed against a named
  build. Record seeds/parameters and internal calls separately from real UI input.
- **Agent-operated UI test:** An agent actually interacted with the rendered
  product using recorded tools, runtime and input. It is execution evidence,
  still not a human playtest, natural comprehension or market validation.
- **Human session:** A consenting person actually attempted the task. Record
  recruitment fit, task, assistance, duration, build and observations privately.
  One person adopting several lenses is one participant, not several people.

First record the visible action, observation and artifact. Then separately state
the interpretation, consequence and next check. A screenshot cannot prove
delivery, persistence or interactive accessibility. An unrendered script cannot
establish visual craft. A simulator can establish the exercised runtime behavior
within its named limits; it is not simulated-human evidence merely because the
device is virtual. Do not collapse these different meanings of simulation.

For an automated harness, inspect that measurements depend on the claimed event.
Use a known-failure or controlled perturbation to show the harness detects the
failure it purports to test. A constant success flag, model parameter disconnected
from the behavior, or direct method bypass cannot certify the missing path. Keep
the original failing result and bounded fix evidence; do not rerun until favorable
and discard the other trials.

Do not invent quotations, satisfaction, enjoyment, comprehension, demand,
retention, sales, human approvals or universal quality scores. A persona's
prediction is a hypothesis even when several agents agree. Multiple prompts to
one model are not independent human samples. Human playtesting required by the
owning project remains required until that owner explicitly changes the gate.

## Record and close findings

Reuse the project's existing acceptance/finding record. If none exists, use the
[session template](../assets/product-testing-session.md) inside the owning project.
Record selected lenses/overlays and why, mapped requirement/outcome, setup,
evidence mode, exact candidate/toolkit identity, steps, actual results, limits,
assistance, finding IDs and next owner/action. Distinguish observed defect,
agreed-target mismatch, preference and hypothesis; apply the project's severity
scale rather than a second scale.

Keep outcomes separate: persona coverage, executed checks, human research,
experience acceptance, source review and release authorization. Passing all
selected scenarios accepts only that scope if the owning rules permit it. Keep
existing holds, published versions and consumer pins unchanged. After a material
change, rerun affected journeys against the final artifact; do not erase valid
evidence for unaffected work. Contribute back only generic methods and synthetic
examples, never private participant records or product status.
