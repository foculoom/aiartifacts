# Production experience acceptance

Use when the task asks whether an experience is production-ready, changes a
material visual treatment, or the owning project requires this gate. Respect
existing scope and approved choices; routine corrections need proportional
verification, not a new art-direction exercise. The project owns the release
decision. This reference supplies neither publication authority nor a universal
style or numerical quality score.

## Establish the target and inspect the artifact

Read the current brief, audience, intended tasks, approved visual target and
constraints. If the target is missing, distinguish observable usability defects
from an aesthetic judgment that needs owner direction. Keep technical correctness,
rights clearance, experience quality and release authorization separate.

Inspect the actual candidate at its intended sizes and relevant states. Record
source revision, payload/build identity, render or capture provenance, viewport
or device, input method and date. Compare released, candidate and reference
artifacts by exact identity when they differ. An old screenshot or a source diff
cannot accept a changed render. If rendering or a required device is unavailable,
mark that scope unverified rather than treating absence of findings as a pass.

Judge composition, hierarchy, legibility, product identity, copy and feedback
against the brief. Identify concrete evidence and its consequence; classify
defects, target mismatches, preferences and hypotheses. Preserve successful
minimalism and deliberate constraints. Do not copy a reference's distinctive
assets or treat its expense, detail or popularity as the required solution.

For an interactive game, inspect actual play frames and relevant transitions:

- Can the player, available action and meaningful state be distinguished at the
  target size? Fitting the board is not proof that its objects can be identified.
- Do silhouettes, materials, light and motion support the intended identity and
  readable cause and effect? Judge designed poses and object relationships, not
  merely file resolution, texture quantity or animation existence.
- Does feedback explain the action's consequence while preserving the game's
  timing, recovery and accessibility contract? Do not import realtime movement,
  camera behavior, world scope or control rules from another game.
- Do promotional images faithfully represent the accepted experience? A correct
  crop, authentic screenshot or cleared asset is not automatically excellent
  promotional art, and a concept painting is not native gameplay evidence.

## Record a bounded decision

Use the project's record if it already carries these fields; otherwise record:

| Field | Required meaning |
| --- | --- |
| Intent | Brief/target revision, audience, task and permitted scope |
| Artifact | Exact source and payload/build identities, date and availability |
| Review | Lane, reviewer identity/type, independence, tools and inspected scope |
| Evidence | Actual renders/journeys, target sizes, results and evidence references |
| Findings | Classification, consequence, correction and acceptance check |
| Decision | Accepted within scope, rework required, or unverified; explain why |
| Limits | Untested states/devices and any explicit owner-accepted deviation |
| Next action | Owner, unresolved gate and the smallest relevant verification |

State independently whether engineering checks passed, the experience meets its
target, and release is authorized. An agent review must be labeled agent review;
do not call it human approval. A narrower reviewer cannot accept uninspected
lanes. Independent review must concern the final relevant artifact. Changes to
that artifact reopen affected judgments, not unrelated completed checks.

If required evidence or a material acceptance condition remains unresolved, hold
that acceptance decision. Only the authorized owner can accept a documented
deviation or change the target; a skill invocation or CI pass cannot do so.
When the project requires this record before release, its release owner checks
the decision and matching artifact. Automation may check presence and identity,
but must not certify artistic merit, enjoyment, accessibility or customer demand.
