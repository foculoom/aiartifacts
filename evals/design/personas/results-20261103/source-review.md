# Independent source review: reusable product-testing personas

Reviewed 2026-11-03 UTC against the supplied partial exact-content snapshot of public `foculoom/aiartifacts` main `7618ac6a52f9da5190cf475136959e8e5005ab69`. This is an independent agent source review, not rendered-product testing, human research, integration approval or publication authorization. Candidate files were not edited. `_source-tree.json` is excluded. The blinded evaluator answer was not opened.

## Result and actionable findings

**Source review accepted within the stated scope after one correction.** No unresolved blocking source finding; no critical safety, privacy or evidence-inflation defect found in the reviewed additions.

1. **Resolved P2: contradictory severity instructions.** `plugins/design/skills/experience-review/SKILL.md:31` unconditionally prescribes P0/P1/P2, while the new reference's “Record and close findings” section says to apply the project's severity scale rather than a second scale. Both are loaded for the same task. A project with an existing different scale can receive a parallel or inconsistent classification despite the intended reuse. Make the SKILL.md severity mapping a fallback when no owning-project scale exists, and explicitly prefer the existing project scale. The old instruction predates this change, but the conflict is introduced by the new integration. Acceptance check: a project using its own severity labels retains those labels; a project without a scale can still use the default. Rechecked at 09:07 UTC: the parent changed SKILL.md to explicitly prefer the owning project scale and use P0/P1/P2 only if none exists. The revised text resolves this source conflict. Historical reviewed SKILL.md hash: `6fd8c0ed69eece95c8edabb2b61e6880c0e08f9c49635d34c71bf54231c74808`.

2. **Resolved optional wording improvement:** the selection step “Start with novice, experienced user and the highest-risk context” can read like a three-lens minimum even though surrounding text, template and evaluations reject a fixed count and allow a cautious-only CLI plan. Prefer “Consider novice, experienced user and the highest-risk context; select only those relevant to the requested scope.” This would make compact two-lens and explicitly one-lens plans unambiguously valid. Rechecked at 09:08 UTC: selection step 3 now says “Consider novice, experienced user and the highest-risk context; select only lenses relevant to the requested scope or a distinct risk.” This resolves the suggestion. Historical reference hash: `49fcea73baa48e97a00cc45dfa704a1371e50ec6da2c86d6c8f502c1f8455d02`.

## Reviewed strengths

- Shared P1–P7 behavior lenses plus separate overlays are reusable across apps and games; concrete scenarios include notes, search, communication, commerce, games and nonvisual tools. No mandatory game controls, cloud features, audio, length or scores are imposed.
- Conditional routing, an optional fallback template and reuse of existing findings/acceptance records avoid a second installed skill or QA system.
- Accessibility guidance concerns functional needs and actual tools rather than diagnoses or impersonated lived experience. It separates source analysis, assistive execution and human research, and avoids automatic hardware gates.
- Evidence modes explicitly separate hypothetical persona analysis, deterministic execution, actual agent UI operation and consenting human sessions. Simulators are not confused with simulated people. Familiarity, coaching, fabricated quotes and false participant counts are handled.
- The harness guidance requires causal/known-failure checks and preserves failures rather than permitting favorable reruns. Existing human gates and release authority remain owned by the project.
- Real sends, bookings, purchases, permissions and destructive tests require authorization; personas cannot supply it. Synthetic fixtures and cancellation-state verification are encouraged.
- The added public material contains generic synthetic examples, not private participants, private product status, account identifiers, receipts or machine paths. Completed records stay with their owning project.
- Evaluation inputs and criteria are separate and cover the important scope/evidence failures. Their README expressly limits text-case claims and calls for rendered app/game evidence before asserting improved actual testing.

## Structural checks and limitations

- All newly introduced relative Markdown links resolve within the supplied candidate snapshot. Existing unresolved links are unchanged baseline references to files omitted from the partial snapshot; they were not treated as new broken links.
- Plugin manifest and existing acceptance reference are unchanged. No new plugin, version bump, public publication, merge or consumer pin change is present in this reviewed delta.
- Full catalog discovery, repository CI, packaging, runtime routing and rendered journeys were not run: this is a partial source snapshot, not a full checkout. Thus structural review does not prove those outcomes.
- Existing HANDOFF.md was read as repository context and remains unchanged at review time. Any later handoff/results additions or fixes require separate scoped review and updated hashes.
- The candidate is local and unpublished under the parent task's boundary. This review did not independently inspect current remote release availability. Existing public milestones are neither revoked nor newly verified here.

## Exact reviewed candidate content

SHA-256 values identify all changed/new files in the reviewed delta:

- `CHANGELOG.md`: `f6470e03484135da0ccae2e5e2d8b3db7c8529553f8af54761fc0150ee09f241`
- `README.md`: `cbb8e476bfd88369243afb2da6cacc78b979b7e75a13293671a1dae925542f17`
- `evals/design/README.md`: `2b3ce4bec9d52d0cbe9f5081be3e70bbe2634ae6fdebe6911300a8a47bf6c4c2`
- `evals/design/personas/README.md`: `9fd4e9ed5bbdce93ae849389e48ac4fed1ec1fade6f02ffb95ebe51d1310e5d6`
- `evals/design/personas/assessment.md`: `7157783629bfbf854b3ebfafcd01d476b89932aa602424f0bf387a65534d8611`
- `evals/design/personas/inputs.md`: `4db99f3d526c5a64eb650eda2431f9b4d59a9dcfa83fa9917975d7693e421d2a`
- `plugins/design/skills/experience-review/SKILL.md`: `811314153a04b9e0d3318c7b67fa22623658614f8420926e2f09d078ca6dcad3`
- `plugins/design/skills/experience-review/assets/product-testing-session.md`: `029c60c4a1c472fec2c9c599b209554899e8b3880c624ee9a63b5b10051768c1`
- `plugins/design/skills/experience-review/references/interactive-experiences.md`: `6339fa9dbc6f063deb61b1d92a4b37974c57dadbde7f1104ec469ac981413412`
- `plugins/design/skills/experience-review/references/product-testing-personas.md`: `aaadff05583f54d3d1bb5f08da62048e2f73a1ac8a981da0f5c6574cb2ec88a6`

## Newly added link checks

- PASS: `README.md` → `plugins/design/skills/experience-review/references/product-testing-personas.md`
- PASS: `README.md` → `plugins/design/skills/experience-review/assets/product-testing-session.md`
- PASS: `README.md` → `evals/design/personas/README.md`
- PASS: `evals/design/README.md` → `personas/README.md`
- PASS: `evals/design/personas/README.md` → `inputs.md`
- PASS: `evals/design/personas/README.md` → `assessment.md`
- PASS: `evals/design/personas/README.md` → `../../../plugins/design/skills/experience-review/references/production-acceptance.md`
- PASS: `plugins/design/skills/experience-review/SKILL.md` → `references/product-testing-personas.md`
- PASS: `plugins/design/skills/experience-review/references/interactive-experiences.md` → `product-testing-personas.md`
- PASS: `plugins/design/skills/experience-review/references/product-testing-personas.md` → `../assets/product-testing-session.md`

Next action: review any further changed hashes, including later handoff/results additions, before extending this acceptance. Retain the independent behavior evaluation and any later rendered evidence separately from this source result. Public integration/publication remains outside this review authority.
