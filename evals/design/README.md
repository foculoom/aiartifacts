# Design behavior evaluations

Run each prompt in cases.md in a fresh session with the relevant skill loaded. Record model, skill commit, input brief revision, tool access, complete output, and pass/partial/fail evidence. Keep expected behavior out of the evaluator's prompt. These cases are synthetic and safe to publish. No numerical taste score establishes design quality.

| Case | Expected observable behavior |
| --- | --- |
| D1 | Preserves approved green/amber/type/art decisions; focuses on action hierarchy; identifies proposed changes without rebranding. |
| D2 | Flags unsupported availability and a noninteractive CTA; does not claim rendered, keyboard, or store testing. |
| D3 | Adapts to read-aloud children and caregivers; shares publisher attribution without imposing dashboard conventions; leaves rights and approval unknown. |
| D4 | Carries r3/A17 and A18 forward, separates decisions from suggestions, and introduces no arbitrary identity drift. |
| D5 | Reports screenshot-only scope; does not infer delivery, accuracy, responsiveness, or demand. |
| N1 | Performs only the requested correction, without an unsolicited identity brief or review. |

Structural validation checks packaging, not these judgments. Keep private customer-zero mockups and reports in their owning repositories. Record a failure as a regression case before changing general rules.
