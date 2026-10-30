# Reproduce a bounded runtime trial

Use [README.md](README.md) for case selection, withheld criteria and the
usefulness gate. The optional [runner](run_codex_case.py) executes one staged
case through an already installed Codex CLI; it is development tooling and is
not exported with either skill. It neither installs software nor grades outputs.
Check `codex --help`, `codex exec --help` and `codex login status` against the
installed version before using the recorded flags. A changed CLI contract needs
a reviewed adaptation, not an unpinned upgrade during a trial.

Runtime access is separate from a paid seat and from distribution intake.
Awesome Copilot's [quality gates](https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/CONTRIBUTING.md#L254-L270)
include a Copilot CLI installation smoke test, whose
[implementation](https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/eng/external-plugin-quality-gates.mjs#L435-L485)
does not run inference. They do not require an author-owned paid Copilot seat
or prescribe our controlled comparison. Upstream still asks for useful content
tested with Copilot; a package pass does not establish that behavior.

Copilot CLI also supports [user-configured BYOK](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/authenticate-copilot-cli#unauthenticated-use)
without GitHub authentication. An already-authorized working provider can test
that CLI/provider/model combination; it does not prove GitHub-hosted model
access. Verify the installed CLI's contract, provider access and authorized
usage before a bounded preflight. On October 30 no such ready route was
verified, so no new Copilot inference probe ran. Keep account and provider
details private. The Codex runner below uses an existing ChatGPT login; it does
not configure a Copilot provider or transfer credentials between runtimes.

## Stage the inputs

The extra skill is now deferred. Its entrypoint is retained only as
[SKILL.md.txt](candidate/SKILL.md.txt), and current tools/procedures live outside
plugin discovery. The paths and revision in `fixtures.json` describe the
historical trials. Check out that exact revision for a historical replay; do
not assume those old plugin paths exist on current `main`. Explicitly staging
a new candidate from current tools and procedures requires its own input hashes
and evaluation authority. This change does not uninstall historical copies.

Create a new disposable project and a separate new receipt directory. Copy only
the selected input block into `prompt.txt`, with the fixtures described in the
case README. Record a SHA-256 inventory before the run. Keep the expected
criteria, past outputs and reviewer decisions outside the project.

For the recorded editorial trials, a reviewed `skills` CLI 1.7.4 installed the
canonical folder into a temporary template using this command, with both
`DISABLE_TELEMETRY=1` and `DO_NOT_TRACK=1` set for the installer process:

```sh
node /absolute/reviewed/skills/bin/cli.mjs add /absolute/reviewed/editorial-writing \
  --skill editorial-writing --agent codex --copy --yes
```

The installer ran with the template as its working directory. Its installed
folder inventory was compared with the reviewed source. A separate copy of
that template was made for each fresh trial. A separate invocation of that same
reviewed installer actually installed `skill-delivery` for meta-skill and
helper-arm trials. The baseline has no copy
of the candidate skill or helper. The recorded paired inputs also supplied the
same already available authoring scripts and official-source snapshots to both
arms; their hashes and original locations are retained in each input inventory.
Do not download an authoring package or expose unrelated private files merely
to reproduce that environment.

For a fresh clone, use the candidate revision and canonical paths recorded in
[fixtures.json](fixtures.json). Copy the editorial directory to
`source/editorial-writing` and its owning `plugin.json` to
`source/existing-plugin.json`. Copy the already reviewed local `skill-creator`
folder to `existing-authoring`, retaining its license, without registering it as
a skill. Supply these inspected upstream files under `official-sources`:

| Local input name | Official repository and path | Recorded revision |
| --- | --- | --- |
| `skills-creating.md` | `vercel-labs/skills`, `docs/creating-skills.md` | `92a9a34ac3bf88e695e468b90c7bf32f163d32c8` |
| `skills-commands.md` | `vercel-labs/skills`, `docs/commands.md` | Same revision |
| `awesome-contributing.md` | `github/awesome-copilot`, `CONTRIBUTING.md` | `5269f7ea2d6c3a9bfda5ed878b6726cf509121fd` |
| `awesome-instructions.md` | `github/awesome-copilot`, `AGENTS.md` | Same revision |
| `awesome-external-plugin.yml` | `github/awesome-copilot`, `.github/ISSUE_TEMPLATE/external-plugin.yml` | Same revision |

Keep all grading material outside the project. The exact historical document
and authoring-tool byte hashes are in the case input inventories and
[upstream notices](results/upstream-notices/README.md); resolve any path/version
drift against those records before claiming an identical rerun. The historical
source fixtures also contained two generated Python cache files. They are
excluded from every selected public payload. A clean-clone rerun should omit
caches, record that fixture difference and hash its own inputs; do not recreate
private machine-dependent bytecode merely to match historical fixture hashes.

For T3, copy the canonical source to both `source/old/editorial-writing` and
`source/new/editorial-writing`, append `t3_new_example_append` from fixtures.json
to the new `references/examples.md`, and make `source/old.zip` from the old
copy plus the declared fictional extra file. E-F1 uses
`editorial_review_draft` as `draft.md`; E-F2 uses an independently created
synthetic draft under `restricted/draft.md`. For F2, copy the editorial source
under `restricted/editorial-writing` before denying all its file reads. Hash
fixtures before applying the mode restriction. Archive timestamps and machine
paths need not reproduce historical bytes: record the new exact archive/input
hashes and preserve the same semantics and balanced arms.

Before inference, create `input-inventory.json` with SHA-256 of every staged
regular file except that inventory itself; do not include a prior `receipt`
directory. Use `hashlib.sha256(path.read_bytes()).hexdigest()` with paths relative
to the disposable project. The runner binds the inventory's own hash into its
receipt. For a correction, make a fresh copy of the original project including
its output, omit its old receipt/inventory, supply only the reviewer's narrow
prompt and recompute the inventory. Never replace the original attempt.

For missing-Python trials, create a test-only command directory containing
symlinks to the ordinary read/file utilities needed by the case, but no Python
command. Verify `/bin/zsh -c 'command -v python3'` fails with that directory as
the process PATH. Pass its absolute path as `--command-path` to the runner.
Record this as **Python unavailable on the controlled command PATH**, not
absence of every interpreter on the host. Preserve any actual attempted command
and failure; a narrated restriction alone does not prove execution behavior.

For read-denial trials on a POSIX host, write the synthetic file first, record
its hash, then set that fixture file's mode to `000`. Verify a direct read fails
under the evaluator identity. No permission change or alternate copy is allowed
to the evaluator. Do not restrict the installed skill itself. A user running
with privileges that bypass those modes needs a different enforced fixture;
do not count an ineffective setup as a passing failure case.

## Execute and preserve

```sh
python3 evals/skill-delivery/run_codex_case.py \
  --project /absolute/disposable-project \
  --prompt /absolute/prompt.txt \
  --output /absolute/new-receipt-directory --timeout 300 \
  --model gpt-6.1-sol --reasoning-effort medium --capture-session
```

The receipt directory must be new and outside the evaluator project. The model
and effort above are explicit requested values, not evidence of availability
or provider identity. Do not silently substitute a model after a failure.

The runner checks for an existing ChatGPT login before inference and refuses
an API-key login, unavailable authentication or a failed CLI version check. It
does not log authentication output. It retains only ordinary existing process
environment variables, excluding API keys, provider overrides and parent-agent
session variables. It preserves the existing HOME value and does not copy
credentials. It enumerates the home skill directories, `/etc/codex/skills` and
ancestor `.agents/skills` directories, following installed links and recording
both alias and canonical paths. Cycles, dangling links, unreadable entries,
enumeration overflow or a staged skill aliasing a disabled host skill cause
refusal before inference. Process-only settings request that these skills,
plugins, apps, hooks, memories and subagents be disabled; sandboxing and approval
denial remain enabled. The exact command and disabled paths stay in private
run metadata. Inspect the actual execution context independently: an inventory,
configuration flags or a debug preview is not proof of execution isolation.

The output contains the complete prompt, final answer when available, JSONL
events, stderr, exit/deadline status, CLI version and input-inventory hash. The
runner records requested model/effort separately from the runtime's recorded
values. Omitting the model still uses the CLI default, as in the historical
trials; do not retroactively assign those runs a model identity.

`--capture-session` is opt-in: it omits ephemeral mode, leaving the ordinary
local session in the existing Codex state directory, and copies only this run's
UUID-bound rollout to the private receipt directory. The capture checks session,
project and CLI identities and rejects linked, stale or oversized rollouts.
Without the flag, the run remains ephemeral and no rollout copy is requested.
Capture failure or missing model/effort leaves identity unknown; a mismatch
remains a mismatch. `matches_runtime_record` means the requested values agree
with the runtime rollout, not a provider-returned backend model identity.
Neither capture success nor model agreement assigns an isolation pass.

The [October 30 context diagnostic](results/editorial-context-check-20261030/README.md)
captured unrelated user instructions despite the isolation settings. Preserve
that result; the controlled comparison remains held until execution context is
independently acceptable. Its raw session remains private because it contains
private context. A sanitized answer alone cannot resolve that limitation.

A deadline sends termination only to the evaluation's own process group and
retains the interrupted attempt. Do not resume a different case in that session.

Before public retention, review every output for private content. Keep original
hashes and disclose redactions. Store generated Markdown as `.md.txt` snapshots
where its original relative links or intentional broken-link fixtures would
otherwise be interpreted as repository documentation. An artifact map must
identify original names/hashes, snapshot names/hashes and every transform.
Never rewrite a failed artifact to make catalog validation pass. Binary archives
with private machine paths stay in private evidence; retain a safe member/hash
inventory and clearly state that limit. Reviewers can inspect the original
authorized artifacts independently.

Before a public evidence push, run the bounded host-path regression against the
staged/committed evidence and wait for independent privacy review of that exact
revision. It checks both macOS temporary-path forms, common home prefixes and
capped ZIP members. It does not establish rights or comprehensive privacy:

```sh
python3 -m unittest discover -s evals/skill-delivery -p test_evidence_privacy.py -q
```

The check selects Git-tracked paths and reads current checkout bytes. Stage new
evidence first; require a clean working tree at the reviewed commit. Preserve
raw originals privately, update snapshot transforms/hashes after redaction, and
do not describe a corrective commit as recall of earlier public copies.

The runner's synthetic, offline regression tests cover its authentication guard,
skill enumeration and session evidence handling:

```sh
python3 -m unittest discover -s evals/skill-delivery -p test_runtime_runner.py -q
```

These stub tests exercise no provider and do not establish live access or
behavior. The recorded Copilot denial is retained separately; do not change
account policy, copy credentials or purchase access merely to fill a runtime
matrix. Any separately authorized access work has its own evidence and scope.
