# Packaging and local installation evidence — 30 October 2026

The unreleased Editorial candidate passed local packaging and installed-file
verification: **12 standalone skill files and 15 plugin files**, with exact
SHA-256 inventories and normalized modes. Both existing disposable installations
match the newly generated candidate: the skills CLI project copy and the Copilot
local-marketplace plugin copy. This is not automatic skill activation, editorial
quality, public discovery, external acceptance or a release.

The [machine-readable receipt](packaging-20261030.json) retains the complete two
manifests, archive/manifest hashes, tool versions, selected meta-skill file hashes,
commands, check outputs and limits. Initial deterministic/upstream checks ran
on an **uncommitted candidate** based on
`1ce208bf7fb4b102bac8f31b192bc378790ed712`; that base does not identify the changed
bytes. The fresh export capture at 17:26:47 UTC then read committed candidate
`211ad9da8b7a3d0740d1896a74c018ed3ad097be`, with only untracked evaluation evidence
remaining. Its manifests record that actual commit. The fresh ignored artifacts
are `build/skill-delivery/editorial-skill-v3` and
`build/skill-delivery/editorial-plugin-v3`. Earlier output directories are retained;
their older manifest format or exporter revision is not silently relabeled.

## Checks actually run

| Check | Result and scope |
| --- | --- |
| Python suites | **148 passed**: Editorial 27, Engineering 28, skill delivery 25, Release 10, Reporting 20, Automation 17, Design 11, Performance 10. Python 3.12.14; canonical temporary-directory setting preserved. |
| Optional JavaScript import graph | **10 passed**, Node 24.19.0, `node --test test.mjs`; existing locked dependency only. |
| Catalog and local references | Passed, **7 plugins / 9 skills**. |
| Whitespace | `git diff --check` passed. |
| Agent Skills checks | Vally **0.20.0** `runLint({rootPath})` passed spec-compliance and valid-reference graders for Editorial and skill-delivery; no discovery/reference errors. This is deterministic lint, not a model evaluation. |
| Plugin schema | Awesome Copilot's `validateAgentPluginManifest` returned no errors for Editorial. Upstream commit `5269f7ea2d6c3a9bfda5ed878b6726cf509121fd`; no collection submission was simulated. |
| GitHub skill dry run | GitHub CLI **2.97.0**, `gh skill publish --dry-run`, exit 0. Seven existing unrelated skills received recommended-license warnings. No publishing or fix option ran. |
| Archive and staged files | Fresh exports passed exact entries, bytes and normalized-mode verification. Config allowlists exclude other plugins and repository/private context. |
| Existing installed copies | Copilot CLI **1.0.54** local-marketplace plugin: 15 matching files. `skills` **1.7.4** project copy: 12 matching files. Both byte and mode comparisons pass; neither installation was repeated by this verification. |

The export suite includes actual self-export of the delivery skill's runtime
files, standalone/plugin agreement, matching license boundaries, a directly
executed synthetic helper, changed-mode rejection, fresh-output preservation,
duplicate/tampered ZIP rejection, symlink/traversal defenses, missing references,
root/parenthesis/empty Markdown destinations and narrow secret-marker screening.
These are code tests, separate from fresh-session behavioral evaluations.

## Environment and remaining gates

This verification used the existing local macOS environment. The default
Homebrew Node 25.6.1 could not start because `libsimdjson.29.dylib` was absent;
the already available Node 24.19.0 completed the checks. No system dependency
repair, package installation, paid execution or permission change was needed.
Hosted results were separate from those initial local checks. A subsequent
GitHub readback verified successful [pull-request run 41098898432](https://github.com/foculoom/aiartifacts/actions/runs/41098898432)
and [push run 41098854729](https://github.com/foculoom/aiartifacts/actions/runs/41098854729),
both at `211ad9da8b7a3d0740d1896a74c018ed3ad097be` on 30 October.

The installed-copy checks used earlier successful disposable local installs.
Their source was a local directory, not an immutable remotely released revision.
The skills install returned no provider security-scan result. Copilot reported
one installed skill and plugin version 0.1.1. No public marketplace, directory
index or provider-review status was changed or freshly established here.

Mode preservation covers normalized 0644/0755 file permissions, not owners,
ACLs or extended attributes. The narrow scanner does not certify privacy or
rights. The full Apache license appears at both independently installed
Editorial boundaries. No actual customer or private company input is included.

Next: assess the independent runtime records and bounded usefulness comparison,
complete independent review of the exact committed candidate, then retain
the separate owner release and external maintainer-review gates. Preserve the
existing public v0.5.0 release and consumer pins.

## Independent prose review and later source readback

Agent `/root/repo_tooling` independently reviewed the skill-delivery `SKILL.md`
and all three references at commit
`211ad9da8b7a3d0740d1896a74c018ed3ad097be` on 30 October. The reviewer did not
author those files. No blocking finding remains in this scope: the instructions
preserve one canonical source, reuse existing authoring tools, distinguish
format/install/runtime/listing evidence, carry public-data and licensing
boundaries, prefer authorized cloud execution, and reserve external actions to
existing or explicit authority. The documented Vally library command executed
successfully against the actual skill with the pinned tool workspace. Root and
installed export commands match the implemented interfaces.

This is an independent agent prose review, not human approval, whole-change
source review or independent review of the reviewer's own exporter. The other
reviewer owns that code lane. A later Git readback compared the recorded
packaging/meta-skill file hashes to the committed candidate: **22 matched with
no mismatch**. The JSON records that readback. The earlier uncommitted-candidate observation
is retained rather than relabeled as a test originally run on the commit.
