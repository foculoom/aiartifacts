# Editorial distribution readiness — October 30, 2026

## Decision after rubber-duck review

Use the existing Editorial skill as the single pilot. A second demonstration
skill would add maintenance before this delivery loop is complete. The
`skill-delivery` entrypoint remains deferred and outside discovery.

Preparation starts from clean default-branch source
`c6fd52080ee50165ac673c72d5dd7adbe0b43e3c`. [PR #30](https://github.com/foculoom/aiartifacts/pull/30)
is merged; its independent reviews and [post-merge Ubuntu checks](https://github.com/foculoom/aiartifacts/actions/runs/41107455838)
are achieved: 157 Python methods and ten JavaScript tests. This follow-up changes
preparation records only, with no Editorial instruction, helper or version change.

Three questions prevent a misleading demonstration:

1. **Does installation establish useful behavior?** No. A format pass and copied
   files establish different things from activation and task completion.
2. **Do the prior trials demonstrate Editorial's benefit over the base model?**
   No. Eleven bounded Codex outcomes passed their task criteria, but the prompts
   specify many expected constraints themselves. There was no controlled
   Editorial-versus-default comparison. The separate meta-skill's one-of-three
   result must not be attributed to Editorial.
3. **Does a public GitHub install establish marketplace acceptance?** No.
   Awesome Copilot has external review, while skills.sh is a telemetry-backed
   directory. Neither installation nor ranking proves quality or demand.

Editorial is a plausible candidate because it combines medium-specific checks
with a Markdown-aware, optional deterministic warning checker. These are
candidate differentiators, not a demonstrated uplift or promised acceptance.
The current [Awesome Copilot contribution policy](https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/CONTRIBUTING.md)
rejects generic submissions without meaningful uplift. Its
[review guidance](https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/.github/skills/code-review/SKILL.md)
also explains why AI-only synthetic/non-Copilot tests are weak evidence alone.
That reviewer guidance is distinct from the automated intake checks.
The external-plugin intake's Copilot smoke test installs a plugin; it does not
run model inference or grade task completion. The runtime/rights holds in this
repository's packet are its own readiness decisions. A controlled comparison is
useful evidence, not a newly invented upstream A/B acceptance requirement.

## Exact candidate and achieved evidence

The prepared candidate is the existing plugin root `plugins/editorial`, version
`0.1.1`, at the full SHA above. Standalone installation selects
`plugins/editorial/skills/editorial-writing` at the same SHA. Keep Apache-2.0,
one canonical instruction source, package-local licenses and optional Python
3.9+ lint. No MCP server, provider SDK, product repository or credential is needed.

The [fresh packaging receipt](../results/editorial-readiness-20261030/packaging.json)
and manifests record the twelve-file skill and fifteen-file plugin, ZIP hashes,
normalized modes and exact selected-source comparisons. All selected files
match both current `c6fd520` and the earlier evaluated `211ad9d` source.
Therefore historical lint, installation and behavioral receipts remain relevant
within their original scopes; they have not been rerun or upgraded by repinning.
Generated ZIPs stay under ignored `build/skill-delivery/editorial-readiness-20261030/`;
the committed configs/manifests allow reconstruction and verification from a
fresh clone. No hosted ZIP release was created.

The export helper names its staging directory `payload`. Running upstream
standalone skill lint directly on that generic folder fails the directory/name
match. Retain that failure, then place the identical selected files in a folder
named `editorial-writing` for standalone lint or installation. The nested plugin
already uses that name. This layout check is distinct from content changes.

The [public acquisition receipt](../results/editorial-readiness-20261030/acquisition.json)
records a new check using the already reviewed skills CLI 1.7.4 and Node 24.19.0:

```sh
DISABLE_TELEMETRY=1 DO_NOT_TRACK=1 node <REVIEWED_SKILLS_CLI> add \
  https://github.com/foculoom/aiartifacts/tree/c6fd52080ee50165ac673c72d5dd7adbe0b43e3c/plugins/editorial/skills/editorial-writing \
  --skill editorial-writing --agent codex github-copilot --copy --yes --json
```

Run only in a new disposable project. The CLI resolved the full SHA and copied
exactly twelve matching files, including modes, without symlinks. Both selected
agent targets share `.agents/skills/editorial-writing`; this is one installation,
not two runtime passes. Complete installer stdout/stderr snapshots are retained,
with the disposable absolute path redacted and original/snapshot hashes recorded.
No new executable was installed, no inference ran, and telemetry was disabled.
`security: null` is not a passing security audit. Recheck installed tool help and
source before reusing these flags; do not substitute an unpinned download.

## Remaining evidence and next executable action

No saved cloud environment was listed on October 30. Local Copilot remains
1.0.54. Its [earlier provider denial](../results/copilot-probe-20261030/README.md)
was already retried after restored workspace usage; no materially different
authorized runtime was found. This follow-up did not repeat that unchanged
inference request. It does not establish the current policy's cause or resolution.

When an already-authorized Copilot runtime is available:

- Install the exact candidate in an isolated project and verify its files.
  Run the existing six positive/three negative [Editorial cases](../../editorial/cases.md)
  in separate fresh sessions, with [grading criteria](../../editorial/README.md)
  withheld. Record actual CLI/model versions, context-isolation limits and
  observable skill loading separately from useful task completion.
- Run the existing E-F1/E-F2 [failure cases](../inputs.md): missing optional
  Python must permit useful manual work with lint explicitly unperformed;
  denied source access must produce a bounded explanation without bypass or
  fabricated review. Retain actual denials rather than prompt-only restrictions.
- Test explicit invocation separately. For editorial-versus-default value,
  compare matched sessions using the same input/tool/model conditions, with
  independent review and full outputs. Reuse P2/P4/P6 as an initial diagnostic;
  do not call three synthetic pairs statistical proof. Record whether the
  medium profiles/checker improve outcomes or merely repeat prompt constraints.
  Obtain actual human testing/feedback before claiming human validation.

Do not remove a model-access restriction, provision another paid runtime or
copy credentials to close this matrix. An authorized environment with working
inference is the missing input. Keep the packet unsent while its recorded
runtime/rights decisions remain unresolved; human maintainers control upstream
acceptance. The next preparation step is recorded evidence, not another skill.

## Present acquisition status

As observed October 30, public source is available at the pinned GitHub SHA and
remote acquisition through skills CLI is verified above. Foculoom was absent
from the inspected Awesome Copilot internal/external plugin catalogs; no issue
or listing was created. The skills.sh Foculoom page could not be retrieved, so
directory listing/ranking remains unverified. This acquisition test did not
enable telemetry or manufacture install counts. See the [directory FAQ](https://skills.sh/docs/faq).

Existing v0.5.0 remains the achieved October 24 public release: metadata was
last checked October 30 and archive acquisition October 28. Editorial 0.1.1 is
an unreleased source candidate; no tag, ecosystem submission or consumer pin
changed. These records do not claim revenue or customer demand.
