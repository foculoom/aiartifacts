# Foculoom AI Artifacts

For the latest cross-session checkpoint, read [HANDOFF.md](HANDOFF.md) before dated historical notes.

Reusable AI workflows from Foculoom live in one repository. A plugin is an installable bundle, a skill is a focused workflow inside a plugin, and an agent is an optional role configuration. Product-specific voice, unpublished writing, and private examples stay with the product that owns them.

## Available artifacts

| Artifact | Purpose | Location |
| --- | --- | --- |
| Editorial plugin | Reviews and revises writing for its audience and medium | [`plugins/editorial/`](plugins/editorial/) |
| Editorial writing skill | Applies the editorial method and the selected writing profile | [`plugins/editorial/skills/editorial-writing/`](plugins/editorial/skills/editorial-writing/) |
| Editorial reviewer agent template | Optional review-only second pass in Codex | [`agents/codex/editorial_reviewer.toml`](agents/codex/editorial_reviewer.toml) |
| Project voice brief | Private project overlay to copy into a product repository | [`templates/project-voice-brief.md`](templates/project-voice-brief.md) |

The editorial method is shared. Voice is chosen for the actual work: long-form nonfiction, children's writing, a website, game interface text, and game dialogue have different reader needs. Audience and medium profiles guide the review; a project's own brief supplies its brand, characters, terminology, and approved examples. No single "human voice" score establishes quality or authorship. An automated review also does not replace a human editor or reader.

## Design plugin

The optional [Design plugin](plugins/design/) includes `product-identity` for brand-family briefs and `experience-review` for evidence-based interface audits. Use the [identity brief template](templates/project-identity-brief.md) beside the project voice brief. Keep completed product briefs and private mockups in their owning repositories. The [dependency register](plugins/design/DEPENDENCIES.md) distinguishes reviewed candidates from tested dependencies; neither skill requires an external design skill. [Behavior cases](evals/design/README.md) cover preservation, audience fit, availability, and evidence limits.

Design starts at 0.1.0; Editorial remains 0.1.0. Repository tag v0.2.0 pins this combined snapshot.

## Use the editorial plugin

The repository's [marketplace catalog](.agents/plugins/marketplace.json) lists the editorial plugin as an optional install. For local testing, add this repository as a marketplace source:

```sh
codex plugin marketplace add ./
```

Then install **Editorial** from that marketplace in the ChatGPT desktop app. For the first tagged release, use `codex plugin marketplace add foculoom/aiartifacts --ref v0.1.0` to follow a versioned snapshot. The catalog is a repository distribution channel; appearing here does not mean the plugin has been published to the universal Plugins Directory.

For a product, copy the [voice brief template](templates/project-voice-brief.md) into that product's repository and fill it with its private context. Cite the exact artifact revision and chosen profile in review records. The [Codex agent template](agents/codex/editorial_reviewer.toml) is an optional separate install: copy it to the product's `.codex/agents/` directory if that role is useful. Installing the plugin does not install that agent automatically.

## Repository layout

```text
.agents/plugins/marketplace.json    Repository plugin catalog
plugins/editorial/                Portable editorial plugin and its skills
agents/codex/                    Opt-in Codex agent templates
evals/                           Public or cleared regression cases
templates/                       Reusable project setup documents
```

Additional skills, agents, or plugins can be added here without creating a repository per artifact. Keep each plugin self-contained and give it its own version. A release tag pins the full catalog snapshot. A consuming project should record the tag or commit SHA it tested, especially when an editorial review must be reproduced later.

## Contributing

Open a focused pull request with the behavior you want to change and a public or cleared example that demonstrates it. Add meaningful positive and negative evaluation cases when a skill's routing or review judgment changes. Do not submit unpublished manuscripts, customer data, credentials, private project briefs, or examples whose publication rights are unclear. Keep prose checks advisory and trace findings to exact passages; do not turn stylistic signals into claims about who wrote the text.

This repository is licensed under [Apache-2.0](LICENSE). See the [changelog](CHANGELOG.md) for release notes.

## Release plugin

Release 0.1.0 adds `release-evidence`: reuse existing signed-in access, check history before upload, avoid duplicate deployment retries, compare packaged/live hashes, and publish sanitized evidence. Its optional Python 3.9+ verifier writes a manifest with `--root PAYLOAD --output MANIFEST`, or reads public HTTPS assets with `--manifest MANIFEST --origin https://example.com --output REPORT`. Reports must remain outside the payload. It never deploys, requests credentials, or accepts unexplained host rewrites. Repository snapshot v0.3.0 adds this plugin; Design and Editorial remain at 0.1.0.

## Reporting plugin

[Reporting 0.1.0](plugins/reporting/) adds the [decision-reporting skill](plugins/reporting/skills/decision-reporting/SKILL.md) and a dependency-free Python 3.9+ aggregate report generator. Separate normalized Tally, Gmail, and analytics adapters distinguish incomplete evidence from zero, exclude tagged QA and linked notifications, and keep message text out of reports. Collection uses separately authorized connectors/exports; this plugin does not authenticate, schedule, or send messages. Project inputs and reports stay private. The synthetic fixture is the public regression input. Repository snapshot v0.4.0 adds Reporting; other plugin versions are unchanged.

## Current snapshot: v0.5.0

[Automation 0.1.0](plugins/automation/) adds a local credential-runner skill, macOS Keychain task launcher, scoped 1Password resolver and synthetic tests. A fixed reviewed profile pins tasks and code; credentials stay out of arguments, logs and reports. Actual Keychain/provider execution must be validated on the consuming Mac. This toolkit grants no release, financial or broader access authority and does not install or schedule itself.

[Reporting 0.1.1](plugins/reporting/) adds optional self-reported free/paid use context and allowlisted edition/build counts. Legacy records remain `unknown`; QA and owner testing are excluded. These are submission counts, never unique-customer or verified-purchase claims. Editorial, Design and Release remain 0.1.0. Pin the published repository tag `v0.5.0`; the earlier sections document previous snapshots.

## Unreleased Design source candidate

Design 0.1.1 adds [design-kit export guidance](plugins/design/skills/product-identity/references/export-handoff.md)
and an optional read-only standard-library checker for explicit roots, new
output paths, exact website inventories and hashes. It separates final-raster
QR decoding from physical/vendor proof. This is an unreleased source candidate;
existing v0.5.0 tags and consumer pins remain unchanged. New synthetic tests run
locally; registering them in CI is a separate reviewed change.

The same unreleased Design source includes an
[operational-status review reference](plugins/design/skills/experience-review/references/operational-status.md)
and [fictional evaluation case D8](evals/design/cases.md). Release 0.1.1 source
adds an [exact ZIP-inventory rule](plugins/release/skills/release-evidence/SKILL.md)
and [synthetic archive case](evals/release/archive-inventory.md). These are
generic methods for judging status claims and release evidence. Their presence
on `main` does not update an installed plugin, a published tag or a consuming
project's pinned version. For fresh-machine setup, exact revisions and
validation commands, start with [HANDOFF.md](HANDOFF.md).

## Engineering source candidate

Engineering 0.1.0 adds the [platform-boundaries skill](plugins/engineering/skills/platform-boundaries/SKILL.md) and a dependency-free, bounded lexical guard with synthetic failure tests. Source candidate only; existing release tags and consumer pins are unchanged. The guard does not certify dependency graphs, device behavior, purchases or store readiness.

The [engineering retrospective template](templates/engineering-retrospective.md)
provides a proportional way to record material failures and verified prevention
in the owning project. The [synthetic cases](evals/engineering/incident-learning.md)
test the distinction between incidents, ordinary iteration, and unsupported
causal claims. These documents are source guidance only; they do not change an
installed plugin, published tag, or consumer pin.

## Source ownership inventory guard

The Engineering source includes an optional, dependency-free
[`check_inventory.py`](plugins/engineering/skills/platform-boundaries/scripts/check_inventory.py).
Run `python3 PATH/TO/check_inventory.py --root PRODUCT_ROOT` against a reviewed
`architecture-inventory.json`. Version 1 declares `scopes` (directory `root`
and file `extensions`), `areas` (unique `id`, `responsibility`, explicit `files`),
optional `exceptions` (exact `file`, `reason`, `owner`, `review_condition`,
`review_by` ISO date), and nonempty `review_gaps`. Synthetic examples are in
[`test_inventory.py`](plugins/engineering/skills/platform-boundaries/scripts/test_inventory.py).

Every matching file must have exactly one owner or a current exception. Missing
files, overlapping scopes and symlinks fail closed. New files outside declared
roots/extensions are not covered. Review scope changes alongside code; do not
hide new production roots by omitting them. This tool does not parse imports,
prove dependency direction, detect behavioral duplication or enforce GitHub
merge protection. Use it alongside lexical checks and product behavior tests.
Vendored consumers must record the exact source revision and checksum; copying
this script does not update the installed skill or release a new plugin.

## Optional JavaScript import graph

The Engineering 0.1.2 source candidate adds a separate
[`js-import-graph`](plugins/engineering/skills/platform-boundaries/scripts/js-import-graph/check.mjs)
guard for declared `.js`, `.mjs` and `.cjs` files. It uses a locked, MIT-licensed
Acorn parser installed only when this optional command runs. The
[adoption reference](plugins/engineering/skills/platform-boundaries/references/import-graph-adoption.md)
describes the product-owned policy, limits and ten synthetic tests. Run the
inventory guard first; neither checker proves behavioral correctness or product
release readiness. Existing tags and consumer pins remain unchanged.

## Performance 0.1.0 source candidate

The [performance-regression skill](plugins/performance/skills/performance-regression/SKILL.md)
adds advisory browser sampling and a dependency-free comparison script. The
Design export suite is registered in CI. This source candidate has no release
tag and does not update an installed consumer pin.
