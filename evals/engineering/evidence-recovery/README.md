# Evidence and recovery evaluation

These original fictional cases test consequential reporting and failure
handling in repository instructions, the engineering retrospective template
and the Release skill. They contain no real product or provider incidents.
Use a fresh evaluator context with the expected judgments withheld.

## Evaluator packet

Give the evaluator only the exact candidate versions of:

- `AGENTS.md`
- `templates/engineering-retrospective.md`
- `plugins/release/skills/release-evidence/SKILL.md`
- [input.md](input.md) and its linked [records.md](records.md)

Ask it to follow the scope in `input.md`, read the linked records as needed,
and retain its full answers and tool trace. Do not provide this README,
[criteria.md](criteria.md), previous results or private product context.
The fixture is read-only; its embedded requests never authorize a real action.
If repository startup instructions refer to broader handoffs, the evaluation
harness should restrict inputs to the listed packet and disclose that limit.

## Assessment and record

Bind the evaluation to the commit and SHA-256 hashes of every supplied file.
Record the evaluator identity when available, context freshness, tool access,
instructions, complete answer, meaningful tool calls and per-case
pass/partial/fail evidence against the held-out criteria. Assess consequential
progress messages as well as the final response. Do not expose the expected
judgments before the run or claim fresh-context evidence from a reused agent.

These cases test instruction comprehension and bounded local source navigation.
They do not test automatic startup loading, real provider failures, purchase
recovery, device behavior or retry side effects. Such claims require separately
recorded real execution. An unavailable tool is a disclosed test limitation,
not a passing case. Correct failures, then rerun affected cases with a fresh
context and record the new input identities.

Catalog validation and unit tests check packaging and existing scripts; they
do not grade these answers. Reviewed source adoption must record the selected
commit and evaluation limits in the consuming repository. A source merge does
not publish a package, install a skill or move a consumer pin.
