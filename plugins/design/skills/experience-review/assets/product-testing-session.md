# Product-testing session template

Copy only when the owning project lacks an equivalent record. This is a blank
planning template, not completed evidence or a release gate. Keep completed
records and participant data in the owning private project. Replace placeholders
and omit irrelevant rows with a reason; do not fabricate missing values.

## Scope

- Product and intended audience: [fill in]
- Task / promised outcome / excluded scope: [fill in]
- Brief and requirements revision: [fill in]
- Toolkit repository and exact commit: [fill in]
- Candidate source and build/payload hash: [fill in]
- Public, private, local or sandbox target; observation date/time: [fill in]
- Existing acceptance policy / release owner / holds: [fill in]
- Test authority and permitted mutations; safe fixture/reset route: [fill in]

## Selected lenses and contexts

| Stable lens ID | Actual audience mapping and why relevant | Overlay/input/context | Requirement and acceptance criterion | Journey ID |
| --- | --- | --- | --- | --- |
| [P1–P7] | [supported audience or labeled assumption] | [exact setting] | [existing IDs or exact criterion] | [stable ID] |

Not selected / not applicable and why: [fill in]. No minimum persona count is
implied. Reference shared definitions rather than creating a second persona list.

## Journey record (repeat for each planned journey)

- Journey ID, lens and goal: [fill in]
- Reviewer identity/type; implementer; independence limits: [fill in]
- Evidence mode: [agent analysis / scripted execution / agent-operated UI / human]
- Actual runtime/version, viewport/device profile, input and assistive tools: [fill in]
- Start state, fixture, parameters/seed, knowledge and help supplied: [fill in]
- Expected observable outcome and requirement: [fill in before execution]
- Steps actually attempted and time observed: [fill in]
- Actual result and verified state after completion/cancel/recovery: [fill in]
- Evidence references and hashes; capture scope; safe access location: [fill in]
- Assistance/coaching or divergence from the planned procedure: [fill in]
- Result: [passed / failed / blocked / untested / not applicable]
- Rationale, untested behavior and next discriminating check: [fill in]
- Findings linked to the owning issue/audit; classification and impact: [fill in]
- Responsible owner and next action/review date: [fill in]

For human sessions, retain consent, relevant recruitment fit and observations
privately with minimal participant identifiers. Record actual participant count;
several lenses used by one person are not several participants. Use exact quotes
only when actually recorded and permitted. Do not invent elapsed duration.

For a scripted harness, link the known-failure/perturbation check and identify
measurements, internal method calls or test shortcuts that limit the conclusion.

## Bounded summary

- What works and must remain: [fill in]
- Completed coverage versus planned / blocked / untested scope: [fill in]
- Observed defects versus hypotheses and preferences: [fill in]
- Correction/retest evidence and unresolved finding IDs: [fill in]
- Experience decision and exact accepted scope, if authorized: [fill in]
- Required human/accessibility research status: [fill in or justified not applicable]
- Source review, deployment/release permission and consumer pin changes: [state separately]
- Next owner/action and stopping condition: [fill in]

Do not treat an empty finding list as product approval. Carry evidence modes and
limitations into summaries. A source-only review remains source-only; a passing
agent-operated test is not a human playtest or customer-demand result.
