# Editorial writing preparation packet

Prepared 2026-10-30. Ready for owner review of packaging; runtime and submission readiness remain open. Nothing was submitted, published, installed, or changed under `source/`.

The existing skill was reused byte for byte. It already supplies four medium profiles, two audience profiles, synthetic editorial examples, explicit factual/voice preservation rules, an optional advisory checker, dependencies, tests, and Apache-2.0 license text. No instruction fork, adapter, initializer, new dependency, MCP server, marketplace, or account is needed for this preparation.

| Review item | Location |
| --- | --- |
| Standalone skill: 12 selected files, archive, exact inventory/hashes | [skill-export/](skill-export/manifest.json), [ZIP](skill-export/skill.zip), [payload](skill-export/payload/) |
| Existing plugin candidate: 15 files, retained manifest and extension | [plugin-export/](plugin-export/manifest.json), [ZIP](plugin-export/skill.zip), [payload](plugin-export/payload/) |
| Actual checks, failures, and limits | [VALIDATION.md](VALIDATION.md), [raw evidence](evidence/) |
| Source identity, license, dependency and privacy review | [PROVENANCE.md](PROVENANCE.md) |
| skills.sh sharing and awesome-copilot issue drafts | [DISTRIBUTION.md](DISTRIBUTION.md) |
| Input-only runtime trials and separately held criteria | [evaluation/README.md](evaluation/README.md) |
| Official documentation reviewed | [OFFICIAL-SOURCES.md](OFFICIAL-SOURCES.md) |

The source record labels the base as `211ad9da8b7a3d0740d1896a74c018ed3ad097be` in `foculoom/aiartifacts`, at `plugins/editorial/skills/editorial-writing`. All 14 recorded source files, including two excluded caches, match their supplied hashes. This workspace has no Git checkout; the base label is not independently authenticated. The manifests bind the selected local bytes, not a claim that these reconstructed layouts exist at that remote commit.

Completed preparation enables review of the exact proposed payloads and future isolated checks. The standalone export contains the skill at its archive root; place that folder under the name `editorial-writing` for discovery. The plugin export contains `plugin.json` and `skills/editorial-writing/`. Both are review artifacts, not installed products. The plugin export reuses the supplied `existing-plugin.json` as `plugin.json` and copies existing license/dependency records to its root as well as retaining them in the skill.

Remaining decisions, in order:

1. Source maintainer: confirm redistribution authority, authorship/notices, public repository access, and that the chosen remote plugin subtree contains the reviewed files and self-contained notices. The workspace describes the candidate as cleared; no independent legal or remote-history audit was performed.
2. Source maintainer: select the immutable release revision and decide whether the retained `0.1.1` manifest version is appropriate after integrating any packaging changes. Do not invent a tag or submit the supplied base SHA without comparing its full subtree.
3. Runtime evaluator: run the prepared input-only cases in fresh target sessions, with held-out review and a baseline for useful uplift. Address any demonstrated defect; preserve this snapshot and rebuild a new candidate after edits.
4. Tooling owner: use an already reviewed, pinned working CLI environment for installer discovery, Vally library lint, manifest schema validation and Copilot smoke tests. Local Node currently cannot start. No dependency installation is authorized here.
5. Owner: review the completed results and authorize any later external action. Awesome Copilot maintainers decide acceptance. The user explicitly excluded submission and publication from this task; this packet does not request either now.

As observed on 2026-10-30, this session produced local review artifacts only. Existing public source availability, skills.sh indexing/acquisition, and Awesome Copilot listing/acquisition were not verified. No customer install, acquisition or revenue is established by these checks; do not describe those states as absent or achieved.

`prepare.py` records the export/check commands and can reproduce them from the workspace root when the two export directories are new. It deliberately refuses to overwrite existing export directories. Use a new preparation destination for another candidate; retain the current hashes and evidence. `packet-inventory.json` inventories this packet except itself; `evidence/package-hashes.json` identifies both archives and manifests. Publish only a separately reviewed payload, not the complete preparation workspace or its internal logs.
