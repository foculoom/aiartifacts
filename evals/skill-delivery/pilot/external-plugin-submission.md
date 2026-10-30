# Unsent Awesome Copilot external-plugin packet

Preparation only. The release owner must approve public distribution after the
exact candidate passes independent review, package, install and behavior gates.
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

Before checking the form confirmations, recheck public repository visibility,
immutable source/version agreement, duplicate or pending listings, applicable
content policies and all evidence. Automated intake and human maintainer
approval are external gates, not results produced by this packet.

Official intake: https://github.com/github/awesome-copilot/issues/new?template=external-plugin.yml

Policy: https://github.com/github/awesome-copilot/blob/main/CONTRIBUTING.md

Listed-plugin updates use reviewed listing PRs and repeat the current gates.
Retain the exact listed SHA; six-month upstream re-review can retain, request
changes to or remove a listing. The owner is responsible for maintaining this
candidate; no monitoring schedule or submission is created here.
