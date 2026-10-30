# Prove useful behavior

Use existing repository checks and synthetic or explicitly cleared inputs.
Keep these evidence layers separate:

| Layer | What to establish |
| --- | --- |
| Structure | Frontmatter meets the current Agent Skills spec and target rules; names, local references, required notices and declared dependencies are valid. |
| Helper behavior | Existing and changed scripts preserve inputs, produce correct outputs, reject unsafe paths and fail clearly. |
| Package | The complete archive or installed folder matches the reviewed inventory and hashes, with any installer transformation explained. |
| Runtime | A named runtime/model/version selects and uses the skill correctly under the tested permissions and tools. |
| Distribution | The exact submitted version is approved/listed/acquirable only when the external evidence establishes that stage. |

An available authoring validator is useful, but inspect its supported fields:
it may be narrower than the standard or a target ecosystem. Do not remove valid
portable metadata just to satisfy a different client's checker. Target lint is
additional evidence, not a substitute for task outcomes.

## Independent trials

Prepare realistic input-only cases and hold the expected judgments separately.
Give an evaluator the user request, exact skill candidate and minimum raw
artifacts needed. Withhold the expected answer, suspected defect, proposed fix
and earlier conclusions. Use fresh isolated sessions/workspaces so earlier
instructions or installed skills cannot supply the missing behavior.

Cover at least these distinct situations:

- **Activation:** an implicit task that needs the skill, plus explicit invocation.
  For selection tests, expose the skill through the runtime's actual discovery
  mechanism; do not tell the agent which skill to choose. Record observed loading
  when the harness exposes it. Supplying the body proves instruction use only.
- **Non-activation:** unrelated app work, ordinary prose editing, or another
  nearby request outside the skill's description. Check that the skill does not
  impose packaging or release work on these tasks.
- **Useful completion:** a real cleared workflow and a contrasting case where
  existing work should remain unchanged. Judge the output against the user's
  task, fact preservation and expected artifacts, not matching headings or prose.
- **Safe failure:** absent tool, network access, credential or write permission;
  untrusted input or private content; ambiguous source rights. The agent must
  report the precise gap, retain useful completed work, and avoid invented
  results, credential disclosure or permission escalation.

For the editorial pilot, use an existing cleared writing case and check
audience/medium fit, preservation of facts and deliberate voice, and useful
edits. Its warning-checker tests cannot certify editorial quality or authorship.
Compare the same task without the candidate when demonstrating that a new skill
adds value; repeat unstable or borderline cases instead of hiding variation.

Run behavior trials in each runtime for which compatibility is claimed. A
skills.sh install targeting multiple agents demonstrates file placement only.
Missing runtime access leaves that runtime untested; an independent agent of a
different kind cannot certify it. Do not provision paid inference to complete a
matrix without authority.

## Evidence and acceptance

Retain complete input/output, skill and fixture hashes, source revision,
runtime/model/tool versions, permissions, commands, date and review rubric.
Use pass, partial, fail, blocked, untested and not applicable distinctly. Have
an independent reviewer assess the completed output against held-out criteria.
Fix demonstrated failures narrowly, preserve earlier results, and rerun affected
cases against the changed candidate.

Accept only claims supported by the observed layers and scope. Unresolved
required behavior or safety failures hold the candidate; a missing external
listing does not erase completed package or runtime work. Sanitize the public
record and retain private originals under the owning project's rules.
