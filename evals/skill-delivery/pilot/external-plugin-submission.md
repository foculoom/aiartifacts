# Unsent Awesome Copilot external-plugin packet

Preparation only. The release owner must approve public distribution after the
exact candidate passes this project's independent review, package, install and
behavior gates. These are local readiness decisions, not a requirement to buy
a Copilot seat or an upstream prescription for a fixed-model comparison.
Do not send this packet, open an issue, publish a tag or edit the upstream
marketplace as part of preparation.

| Form field | Candidate value |
| --- | --- |
| Plugin name | editorial |
| Description | Review and revise writing for its audience, medium and project voice. |
| GitHub repository | foculoom/aiartifacts |
| Plugin path | plugins/editorial |
| Commit SHA | `c6fd52080ee50165ac673c72d5dd7adbe0b43e3c`; reviewed, merged source. All selected Editorial bytes/modes match the previously evaluated `211ad9d` candidate. See the dated readiness record below. Submission remains held pending runtime acceptance and owner release/rights approval. |
| Ref | Omit when using a full SHA; never substitute a mutable branch or move an existing tag. |
| Version | 0.1.1; confirm against the manifest at the submitted SHA. |
| License | Apache-2.0 |
| Author | Foculoom |
| Author URL | https://github.com/foculoom |
| Homepage | https://github.com/foculoom/aiartifacts |
| Keywords | editorial, writing, accessibility, review |

Notes for reviewers: one standard Agent Skills folder, Markdown-aware optional
Python advisory lint, UI-state checks that distinguish pending/local/cloud-save
claims, and branch-fact checks for dialogue. See the bundled
[game UI profile](../../../plugins/editorial/skills/editorial-writing/references/medium/game-ui.md),
[dialogue profile](../../../plugins/editorial/skills/editorial-writing/references/medium/game-dialogue.md)
and [synthetic examples](../../../plugins/editorial/skills/editorial-writing/references/examples.md).
These are candidate differentiators, with no demonstrated uplift over a default
model yet. The package includes local licenses and requires no MCP/provider
integration. OpenAI UI metadata is an optional extension; other clients ignore
unimplemented namespaces. Link the actual sanitized evaluation record, source
revision, tool versions and limitations. Do not describe schema or script-test
passes as editorial quality or universal runtime acceptance.

[October 30 readiness and evidence](editorial-readiness-20261030.md): fresh
12-file skill/15-file plugin packages pass exact verification; public GitHub
acquisition through skills CLI resolves this SHA and matches all twelve skill
files/modes. Historical Codex task passes and Copilot local installation remain
achieved within their recorded limits. Copilot task behavior and incremental
Editorial-versus-default benefit remain unverified. The meta-skill's failed
usefulness gate is a different experiment. Do not claim human validation from
automated evidence alone; keep the form's actual public-source, immutable-pin,
policy and duplicate-listing attestations separate from testing evidence.

The [October 30 context diagnostic](../results/editorial-context-check-20261030/README.md)
records a requested model and effort plus captured runtime context. Unrelated
user instructions were present, so this does not close the controlled
comparison or establish isolation. Runtime-recorded model identity is not
provider-returned backend identity. Historical results remain intact.

Upstream's [installation smoke test](https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/eng/external-plugin-quality-gates.mjs#L435-L485)
does not run inference or require the submitter to own a paid seat. Its
[contribution guidance](https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/CONTRIBUTING.md#L49-L59)
still calls for meaningful value and testing with Copilot. The
[review guidance](https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/.github/skills/code-review/SKILL.md#L146-L163)
allows realistic manual evaluation and treats non-Copilot-only or AI-only
synthetic evidence as weak on its own. Human validation must be reported as
such only when it occurred.

An authorized, user-configured BYOK model is a supported Copilot CLI route;
see the [runtime procedure](../runtime.md). It would establish only the tested
CLI/provider/model combination. No ready provider route was verified on
October 30, so a new Copilot preflight was not run. Keep provider/account
diagnostics private and retain the outstanding behavior/usefulness holds.

Before checking the form confirmations, recheck public repository visibility,
immutable source/version agreement, duplicate or pending listings, applicable
content policies and all evidence. Automated intake and human maintainer
approval are external gates, not results produced by this packet.

Official intake: https://github.com/github/awesome-copilot/issues/new?template=external-plugin.yml

Inspected policy (October 30): https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/CONTRIBUTING.md

Listed-plugin updates use reviewed listing PRs and repeat the current gates.
Retain the exact listed SHA; six-month upstream re-review can retain, request
changes to or remove a listing. The owner is responsible for maintaining this
candidate; no monitoring schedule or submission is created here.
