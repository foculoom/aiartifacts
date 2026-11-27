# Foculoom AI Artifacts

**Last reviewed: 2026-11-26 (America/Los_Angeles).** The next monthly upstream review is due 2026-12-07; see [upstream maintenance](docs/skill-delivery/upstream-maintenance.md). This catalog review added first-party skills for human-voice copy, visual sign-off, vision second opinions, usefulness review, exact-SHA owner approval, and audio PR proof of work. They are unreleased source: the published `v0.5.0` tag and existing consumer pins are unchanged.

For the latest cross-session checkpoint, read [HANDOFF.md](HANDOFF.md) before dated historical notes.

The [toolkit PRD](docs/PRD.md) is the authoritative requirements entry point.
Repair missing, stale or contradictory requirements before implementation;
see [contributor instructions](AGENTS.md#requirements-before-implementation).

Reusable AI workflows from Foculoom live in one repository. A plugin is an installable bundle, a skill is a focused workflow inside a plugin, and an agent is an optional role configuration. Product-specific voice, unpublished writing, and private examples stay with the product that owns them.

## Skill delivery tooling

The [export helper](scripts/skill-delivery/export_skill.py) and
[packaging guide](docs/skill-delivery/packaging.md) prepare explicit distribution
payloads without adding an installed authoring skill. The active
[Agent Supply Chain pilot](evals/skill-delivery/agent-supply-chain/README.md)
improves an existing Awesome Copilot skill upstream; this repository retains
only preparation fixtures and evidence. The earlier
[Editorial pilot](evals/skill-delivery/pilot/README.md) and its verified public
source acquisition remain preserved. Editorial 0.1.1 adds package-local Apache
licenses, dependencies and missing-tool guidance.
[Evaluations](evals/skill-delivery/README.md) distinguish
metadata, isolated installation, runtime behavior and usefulness.

These are source candidates. The Editorial submission packet remains unsent,
and the upstream improvement awaits runtime acceptance before a PR;
no ecosystem listing, package release or consumer update follows from this work.
The published v0.5.0 tag and existing consumer pins remain unchanged.
The [October 30 evaluation](evals/skill-delivery/results/README.md) did not meet
the incremental-usefulness threshold. Its [archived entrypoint](evals/skill-delivery/candidate/README.md)
is an evaluation fixture, outside normal skill discovery. Engineering 0.2.0 source retains platform-boundaries and adds the pinned
[test-driven-development skill](plugins/engineering/skills/test-driven-development/SKILL.md).
See its [dependency record](plugins/engineering/DEPENDENCIES.md) for provenance
and bounded validation. This is unreleased source, not an installed update.

## Available artifacts

| Artifact | Purpose | Location |
| --- | --- | --- |
| Editorial plugin | Reviews and revises writing for its audience and medium | [`plugins/editorial/`](plugins/editorial/) |
| Editorial writing skill | Applies the editorial method and the selected writing profile | [`plugins/editorial/skills/editorial-writing/`](plugins/editorial/skills/editorial-writing/) |
| Human-voice skill | Lints reader-facing copy for stock AI wording and stiff formulas, then rewrites in the project's voice. Not an authorship test. | [`plugins/editorial/skills/human-voice/`](plugins/editorial/skills/human-voice/) |
| Editorial reviewer agent template | Optional review-only second pass in Codex | [`agents/codex/editorial_reviewer.toml`](agents/codex/editorial_reviewer.toml) |
| Project voice brief | Private project overlay to copy into a product repository | [`templates/project-voice-brief.md`](templates/project-voice-brief.md) |

The editorial method is shared. Voice is chosen for the actual work: long-form nonfiction, children's writing, a website, game interface text, and game dialogue have different reader needs. Audience and medium profiles guide the review; a project's own brief supplies its brand, characters, terminology, and approved examples. The human-voice skill flags stock wording and stiff formulas; a clean lint is not a quality or authorship certificate, and it does not replace a human editor or reader.

## Design plugin

The optional [Design plugin](plugins/design/) includes `product-identity` for brand-family briefs, `experience-review` for evidence-based interface audits, `visual-signoff` for palette and contrast gates, `vision-second-opinion` for a repeatable vision-model review of exact-build screenshots, `audio-pr-proof-of-work` for loudness and second-opinion checks on audio changes, `roblox-3d-art-direction` for implementable Roblox room looks (palette with measured L*, Lighting/Atmosphere/post values, light plan, triangle and texture budgets), `3d-visual-gate` for fixed-shot, phone, luminance and performance checks on 3D pull requests, `fal-image-to-3d` for an approval-gated image-to-3D asset pipeline, and `roblox-3d-play-pass` for evidence-first Roblox playtests (first 60 seconds, camera comfort, readability, controls per input, frame time, lag, young-player safety and monetization, fun rubric, High/Medium/Low). Use the [identity brief template](templates/project-identity-brief.md) beside the project voice brief. Keep completed product briefs and private mockups in their owning repositories. The [dependency register](plugins/design/DEPENDENCIES.md) distinguishes reviewed candidates from tested dependencies; neither skill requires an external design skill. [Behavior cases](evals/design/README.md) cover preservation, audience fit, availability, and evidence limits.

The Design plugin's 3D feel skills cover how a 3D Roblox scene behaves. `3d-game-feel-tuning` sets camera and movement targets, `roblox-spatial-audio` covers Audio API wiring, attenuation, buses and the asset upload path, and `3d-feel-proof-of-work` records measured camera, movement, spatial-audio and accessibility checks on a pull request, beside `audio-pr-proof-of-work`.

Repository tag v0.2.0 pinned Design 0.1.0 with Editorial 0.1.0. Later tags and the unreleased source on `main` supersede those plugin versions; see [Current snapshot: v0.5.0](#current-snapshot-v050) and the changelog.

## Gamedev plugin

The optional [Gamedev plugin](plugins/gamedev/) includes `roblox-rojo-headless-build-test` for linting, unit-testing and building a Roblox place from Luau with Rojo and Lune, including a round-trip check of 3D Instances in the built place, and `godot-headless-3d-render-export` for software-rendered Godot 4 frames, golden-image diffs and Web exports on a machine without a GPU. Both say what a headless run does not prove: engine physics, players and networking, real-GPU rendering and performance still need a playtest on the target platform. They complement the Design plugin's Roblox 3D skills, which cover art direction, visual gates and play passes.

## Public Skills plugin

The optional [Public Skills plugin](plugins/public-skills/) vendors pinned copies of approved public upstream skills (Playwright CLI, frontend design, security best practices, selected Superpowers review skills, advisory App Store review, and official Cloudflare skills). It is [advisory / dry-run only, no deploys](plugins/public-skills/README.md). See [PROVENANCE.md](plugins/public-skills/PROVENANCE.md) for upstream URLs, commits, and licenses. Official Stripe skills and `turnstile-spin` are not in this snapshot.

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
plugins/editorial/                  Editorial writing and human-voice lint
plugins/design/                     Identity, experience, visual sign-off, vision, audio and Roblox 3D checks
plugins/release/                    Release evidence, usefulness review, exact-SHA owner approval
plugins/reporting/                  Private decision reports
plugins/automation/                 Local scoped credential runner
plugins/engineering/                Platform boundaries and test-driven development
plugins/performance/                Advisory runtime regression checks
plugins/gamedev/                    Headless 3D build, test and render checks
plugins/public-skills/              Pinned, licensed copies of approved upstream skills
agents/codex/                       Opt-in Codex agent templates
evals/                              Public or cleared regression cases
templates/                          Reusable project setup documents
docs/                               Requirements, CI, and skill-delivery guides
```

Additional skills, agents, or plugins can be added here without creating a repository per artifact. Keep each plugin self-contained and give it its own version. A release tag pins the full catalog snapshot. A consuming project should record the tag or commit SHA it tested, especially when an editorial review must be reproduced later.

## Contributing

Open a focused pull request with the behavior you want to change and a public or cleared example that demonstrates it. Add meaningful positive and negative evaluation cases when a skill's routing or review judgment changes. Do not submit unpublished manuscripts, customer data, credentials, private project briefs, or examples whose publication rights are unclear. Keep prose checks advisory and trace findings to exact passages; do not turn stylistic signals into claims about who wrote the text.

This repository's original code is licensed under [Apache-2.0](LICENSE), with vendored MIT (and other third-party) files under [plugins/public-skills](plugins/public-skills/) per [PROVENANCE.md](plugins/public-skills/PROVENANCE.md). See the [changelog](CHANGELOG.md) for release notes.

## Release plugin

Release 0.1.0 added `release-evidence`: reuse existing signed-in access, check history before upload, avoid duplicate deployment retries, compare packaged/live hashes, and publish sanitized evidence. Unreleased Release 0.2.0 source adds `usefulness-review` (a VALUE_GATE report for an exact commit) and `owner-sha-approval` (an owner yes must cite that same 40-character SHA). Its optional Python 3.9+ verifier writes a manifest with `--root PAYLOAD --output MANIFEST`, or reads public HTTPS assets with `--manifest MANIFEST --origin https://example.com --output REPORT`. Reports must remain outside the payload. It never deploys, requests credentials, or accepts unexplained host rewrites. Repository snapshot v0.3.0 adds this plugin; Design and Editorial remain at 0.1.0.

## Reporting plugin

Reporting 0.1.2 source adds [source-acquisition guidance](plugins/reporting/skills/decision-reporting/references/source-acquisition.md) and an exact local-week window helper. It preserves the offline report contract and the published v0.5.0 consumer pin. Provider collection still needs separately authorized access; project identities, QA ledgers and reports remain private.

[Reporting 0.1.0](plugins/reporting/) adds the [decision-reporting skill](plugins/reporting/skills/decision-reporting/SKILL.md) and a dependency-free Python 3.9+ aggregate report generator. Separate normalized Tally, Gmail, and analytics adapters distinguish incomplete evidence from zero, exclude tagged QA and linked notifications, and keep message text out of reports. Collection uses separately authorized connectors/exports; this plugin does not authenticate, schedule, or send messages. Project inputs and reports stay private. The synthetic fixture is the public regression input. Repository snapshot v0.4.0 adds Reporting; other plugin versions are unchanged.

## Current snapshot: v0.5.0

[Automation 0.1.0](plugins/automation/) adds a local credential-runner skill, macOS Keychain task launcher, scoped 1Password resolver and synthetic tests. A fixed reviewed profile pins tasks and code; credentials stay out of arguments, logs and reports. Actual Keychain/provider execution must be validated on the consuming Mac. This toolkit grants no release, financial or broader access authority and does not install or schedule itself.

[Reporting 0.1.1](plugins/reporting/) adds optional self-reported free/paid use context and allowlisted edition/build counts. Legacy records remain `unknown`; QA and owner testing are excluded. These are submission counts, never unique-customer or verified-purchase claims. Editorial, Design and Release remain 0.1.0. Pin the published repository tag `v0.5.0`; the earlier sections document previous snapshots.

## Unreleased Design source candidate

Design 0.1.1 adds [design-kit export guidance](plugins/design/skills/product-identity/references/export-handoff.md)
and an optional read-only standard-library checker for explicit roots, new
output paths, exact website inventories and hashes. It separates final-raster
QR decoding from physical/vendor proof. This is an unreleased source candidate;
existing v0.5.0 tags and consumer pins remain unchanged. The Design export suite
is registered in CI through merged PR #10; no replacement CI change is needed.

The same source candidate includes scoped
[production-experience acceptance](plugins/design/skills/experience-review/references/production-acceptance.md)
and [four original rendered evaluation fixtures](evals/design/rendered/README.md).
These extend the existing Design skills. They add no art-direction plugin,
universal visual style or automatic quality certificate. The
[initial quality audit](docs/quality-audit-20261028.md) distinguishes structural
verification, independent evaluation, source review and publication.

The same unreleased Design source includes an
[operational-status review reference](plugins/design/skills/experience-review/references/operational-status.md)
and [fictional evaluation case D8](evals/design/cases.md). Release 0.1.1 source
adds an [exact ZIP-inventory rule](plugins/release/skills/release-evidence/SKILL.md)
and [synthetic archive case](evals/release/archive-inventory.md). These are
generic methods for judging status claims and release evidence. Their presence
on `main` does not update an installed plugin, a published tag or a consuming
project's pinned version. For fresh-machine setup, exact revisions and
validation commands, start with [HANDOFF.md](HANDOFF.md).

## Reusable product-testing personas (unreleased source)

The existing Design experience-review skill includes
[shared product-testing lenses](plugins/design/skills/experience-review/references/product-testing-personas.md)
for apps, games, websites and nonvisual tools. Select relevant novice, experienced,
critic, practitioner, rushed, returning and cautious perspectives, with separate
accessibility/context overlays and product-specific scenarios. A portable
[session template](plugins/design/skills/experience-review/assets/product-testing-session.md)
fits the owning project's existing test record. These are behavior hypotheses,
not recruited participants; simulated analysis, executed checks and human research
remain distinct. No extra plugin, automatic release gate or consumer update is added.
[Synthetic cases](evals/design/personas/README.md) test the bounded guidance.

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

## Unreleased Editorial, Design and Release 0.2.0 source

Editorial 0.2.0 adds the [human-voice skill](plugins/editorial/skills/human-voice/SKILL.md)
and a dependency-free Node linter for stock wording and formulas. Design 0.2.0 adds
[visual sign-off](plugins/design/skills/visual-signoff/SKILL.md),
[vision second opinion](plugins/design/skills/vision-second-opinion/SKILL.md) and
[audio PR proof of work](plugins/design/skills/audio-pr-proof-of-work/SKILL.md).
Release 0.2.0 adds [usefulness review](plugins/release/skills/usefulness-review/SKILL.md)
and [owner SHA approval](plugins/release/skills/owner-sha-approval/SKILL.md).
These are source candidates. They do not change the published `v0.5.0` tag or
consumer pins. A clean lint or second opinion is not a quality, authorship or
accessibility certificate, and it is not permission to merge or deploy.

## Performance 0.1.0 source candidate

The [performance-regression skill](plugins/performance/skills/performance-regression/SKILL.md)
adds advisory browser sampling and a dependency-free comparison script. The
Design export suite is registered in CI. This source candidate has no release
tag and does not update an installed consumer pin.
