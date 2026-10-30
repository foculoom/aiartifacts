# Prepared runtime evaluation — unexecuted

The checker tests exercise a deterministic helper. They do not evaluate skill selection or editorial quality. All cases below are synthetic and cleared for evaluation; no customer manuscript is included. There are no trial results yet.

For each claimed target runtime (at minimum Copilot if that compatibility will be advertised), use a fresh isolated session and the reviewed package. Record runtime/model/tool versions, manifest hash, case/input hashes, permissions, discovery configuration, loaded skill evidence if exposed, full input/output, exit status, date and reviewer judgments. Do not provision paid inference or install tools under the authorization for this task.

Expose the skill through the runtime's actual discovery mechanism for selection tests. Give only the case file plus necessary raw artifacts to the evaluator; withhold this README, the other cases, reviewer criteria and any earlier conclusions. Supplying SKILL.md directly tests instruction use, not discovery. Repeat activation cases without the candidate as a baseline; compare actual usefulness and preserve both outputs. Have an independent reviewer apply `reviewer-only/criteria.md`, repeating unstable/borderline outcomes rather than hiding them.

| Case file | Intended coverage | Current result |
| --- | --- | --- |
| 01-web.txt | Implicit selection, facts and concrete action | Untested |
| 02-early-reader.txt | Explicit invocation, preserve useful repetition | Untested |
| 03-game-ui.txt | Placeholder/state preservation and scope limits | Untested |
| 04-unrelated.txt | Non-activation during routine code work | Untested |
| 05-sound-copy.txt | Contrasting unchanged writing | Untested |
| 06-no-python.txt | Optional tool unavailable; useful partial completion | Untested |
| 07-unreadable.txt | No source access; safe failure | Untested |
| 08-untrusted.txt | Quoted input instructions and privacy | Untested |

Do not present this prepared suite as completed independent testing. No fresh runtime session, baseline, automatic selection receipt, reader test or independent review was available/performed in this preparation turn. Qualification for a new runtime stays untested until its own evidence exists.
