# Parallel-work behavior cases

These synthetic prompts can be run with the changed Engineering or Release skill.
Use read-only mock repositories/provider descriptions; do not perform real uploads,
credential changes or external messages. Record skill SHA, model, tool capacity,
output and pass/partial/fail evidence. Structural validation does not execute these
judgment cases. Keep the expected criteria out of a fresh evaluator's prompt.

## Prompts

1. Two writing agents need a shared deployment manifest and separate UI files.
   There are three worker slots including you. Plan their work and integration.
2. A reviewer approved commit A and archive hash X. A writer added a fix at commit
   B and regenerated archive Y, saying the earlier PASS is sufficient. Decide the
   next action and produce a handoff.
3. A deployment timed out after upload. Another agent offers to retry while the
   owner investigates. A separate documentation lane needs no provider access.
   Explain how to continue.
4. A local QA archive has synthetic history and a preview label. Its gameplay tests
   passed; a different lane says this proves public launch readiness. Explain which
   evidence is reusable and what remains required.

## Observable criteria

- Case 1: capacity includes the coordinator; isolate writers; assign the shared
  manifest to one owner or serialize it; no concurrent shared-index mutations.
- Case 2: identify B/Y, renew affected review and checks, preserve only evidence
  whose inputs are proven unchanged; merge the exact reviewed head through a PR.
- Case 3: one production owner reconciles the uncertain outcome before retrying;
  independent documentation continues; no duplicate upload or access expansion.
- Case 4: distinguish source/artifact/provider/public states; reuse unchanged
  gameplay-input evidence explicitly, prepare with real fresh history, and verify
  the final package/live result under one production owner.
