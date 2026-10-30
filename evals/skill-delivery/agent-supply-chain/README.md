# Agent Supply Chain pilot

Owner-selected October 30, 2026: improve the existing Awesome Copilot
`skills/agent-supply-chain` resource rather than submit Editorial or create a
duplicate Foculoom plugin. Canonical source belongs upstream; this directory
contains development fixtures, export configuration and cleared receipts only.
Historical Editorial packaging and public acquisition remain achieved. See the
[October 30 preparation receipts](results-20261030/README.md) for the reviewed
candidate, tests, installation evidence and remaining gates.

## Prepare and evaluate

From this repository, stage one fresh input with Python 3:

```sh
python3 evals/skill-delivery/agent-supply-chain/prepare_case.py \
  --case P2 --output /absolute/new/project
```

The parent directory must already exist. Staging does not install a skill,
enforce permissions or run an agent. Do not copy this directory into a trial.
Install only the reviewed upstream skill into the skill arm, using the
[existing runtime procedure](../runtime.md); keep criteria.md, preparation
source, previous outputs and other skills outside the model-visible context.
Use P1–P6, N1–N3, F1–F2 and the separate X1 diagnostic in fresh Copilot and
Codex sessions. [Evaluator criteria](criteria.md) define the prospective gate.

Before execution, record the exact source/installed inventory, installer and
runtime versions/hashes, requested and observed model/effort, tools, permissions
and actual model-visible catalog/context. Use Codex gpt-6.1-sol with medium
reasoning and existing ChatGPT access. Freeze one authorized explicit Copilot
model/provider; no Auto, silent fallback or additional spending. A successful
preflight does not excuse contaminated context or unknown model identity.

F1 needs a disposable environment in which the agent genuinely cannot execute
or obtain Python, including alternate absolute paths. F2 needs a payload that
the agent cannot read or make readable with its granted tools. Verify the
restrictions before inference and retain that evidence. Prompt instructions,
PATH hiding and user-changeable mode bits alone are insufficient. Do not relax
managed security controls to build the harness. Without such an environment,
mark these cases unexecuted rather than simulating a behavioral pass.

## Packaging and distribution

Use the existing [exporter](../../../scripts/skill-delivery/export_skill.py)
with the reviewed upstream checkout as source root and the explicit allowlist
in export.json. The source_commit identifies committed source, while recorded
file hashes identify the bytes actually tested. Build into a new ignored
build/skill-delivery directory, verify archive inventory and inspect provenance
and public contents. Keep evidence outside the installed skill.

Use reviewed existing installers in disposable project directories. GitHub
CLI's local-source installation injects source-tracking frontmatter; retain
the exact private diff and publish only a sanitized account of it. Do not claim
that the resulting SKILL.md is byte-identical. The skills installer can place
both agent targets in one .agents/skills directory; placement does not prove
two runtime passes. Disable installer telemetry.

After acceptance, recheck duplicate work and current upstream contribution
requirements. This is an ordinary update PR to Awesome Copilot main, not an
external-plugin intake issue. Preserve MIT notices and obtain exact-revision
privacy/provenance review before pushing evidence. Reuse development tools
without copying Apache-licensed code into an MIT-only contribution.
Maintainers control approval/merge. Repeat public acquisition against the
merged SHA, account for installer transforms, and check skills.sh separately.

## Current gates

The October 30 preflight found no saved authorized cloud environment. Previous
Copilot fixed-model access and Codex context-isolation failures remain unresolved;
no unchanged denied request should be repeated. Offline work and local-source
installation checks do not clear these gates. Human task feedback is also
recorded for the helper example, while runtime acceptance remains outstanding.
No upstream submission or new release is authorized before the
selected acceptance conditions pass. Preserve the extra-skill deferral, existing
release tags and consumer pins.
