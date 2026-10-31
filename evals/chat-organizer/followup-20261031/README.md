# Predeclared follow-up comparison — October 31, 2026

This supplementary three-pair suite measures the existing Chat Organizer
candidate without changing its skill instructions. The first comparison's one
improvement and two ties remain in the [original result](../results-20261031/README.md)
and do not disappear if this suite performs better. The first tasks were small
and explicit; this suite includes a larger, mixed inventory closer to the
intended chat-organization workload. Run this suite once. Keep ties and failures.

An agent who did not read the skill, prior outputs or original cases drafted
the [input-only cases](cases.md) and separate [held-out criteria](criteria.md).
An independent preregistration review found the three [fictional fixtures](fixtures/)
internally consistent and requested clarification of permitted pin changes,
scoring and the ChatGPT access limit; those corrections were made before any
model trial. The candidate `SKILL.md` SHA-256 is
`cd664af43f4b96d6dd31d65f0bdbd88dc2d3f078479872b468f52f177b18be05`.

For each pair, initialize two fresh projects with [chatctl.py](../chatctl.py),
stage its identical CLI and fixture state, then stage the candidate skill in
only one project. Give both sessions the same user prompt, model, reasoning
setting, budget and tool instructions. Keep the criteria inaccessible to both
trial sessions. Capture each session's answer, tool calls, action receipts and
final state outside this public repository. Randomize A/B labels for an
independent reviewer. Compare practical outcome, preservation and user effort;
the two-pair improvement gate and severe-failure hold in `criteria.md` apply.

The fixture's ChatGPT side is a partial user-supplied export with no connected
ChatGPT tool. This suite tests Codex organization and honest manual handoff,
not direct ChatGPT runtime compatibility. No real account data or credentials
belong in these files or public results.

The completed [result](results.md) retains all three practical ties and the
continued release hold.
