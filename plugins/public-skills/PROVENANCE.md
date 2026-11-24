# PROVENANCE

Pinned vendor snapshot of approved public skills, recorded on
November 24, 2026, from the studio box in America/Los_Angeles.
Skill bodies are byte-identical to the listed upstream commits.
**Advisory / dry-run only, no deploys.** App Store review is advisory
and must not submit. Cloudflare skills are dry-run only. Deploys and
store submissions stay owner-only.

## playwright-cli

- Upstream: https://github.com/microsoft/playwright/tree/99d4c415db3794d1c989be16ac4987f4529e3220/packages/playwright-core/src/tools/skills/playwright-cli
- Commit: `99d4c415db3794d1c989be16ac4987f4529e3220` (November 20, 2026, 11:10 AM PT)
- License: Apache-2.0 (`LICENSE` and `NOTICE` copied from the Playwright repository)
- Local path: `skills/playwright-cli/`
- Scripts: none. SKILL.md may tell an agent to install `@playwright/cli`; do not treat that as a hook in this snapshot.
- SKILL.md sha256: `ec07841c9c47b311d9c20111397e69411004e7ea46481aa12f7b9e0510195aa7`

## frontend-design

- Upstream: https://github.com/anthropics/skills/tree/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/frontend-design
- Commit: `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f` (September 3, 2026, 9:37 AM PT)
- License: Apache-2.0 (`LICENSE.txt` in the skill folder)
- Local path: `skills/frontend-design/`
- Scripts: none
- SKILL.md sha256: `d91970639e9f5c37682ac7ab60094d35f1c7c1f38d731bd56396563aee10c1d3`

## security-best-practices

- Upstream: https://github.com/openai/skills/tree/5c8f1e26803bcfaffeceef1e7accbcf7e388417a/skills/.curated/security-best-practices
- Commit: `5c8f1e26803bcfaffeceef1e7accbcf7e388417a` (February 2, 2026, 7:58 AM PT)
- License: Apache-2.0 (`LICENSE.txt` in the skill folder)
- Local path: `skills/security-best-practices/`
- Notes: The openai/skills catalog is deprecated; this is a vendored copy of the last path commit. Docs and references only.
- Scripts: none
- SKILL.md sha256: `7b3dae1ffc5434d890f3c65c8f552af52d0307fab3b35dec13013c9ca3844c4f`

## verification-before-completion (Superpowers, selected skill only)

- Upstream: https://github.com/obra/superpowers/tree/3be5aad3dd2400ef23b15680969f4bcd3b6d7b8b/skills/verification-before-completion
- Commit: `3be5aad3dd2400ef23b15680969f4bcd3b6d7b8b` (July 23, 2026, 5:27 PM PT)
- License: MIT (`LICENSE` copied from the Superpowers repository)
- Local path: `skills/verification-before-completion/`
- Scripts: none
- Not included: the rest of Superpowers (`using-superpowers`, `finishing-a-development-branch`, and other skills).
- SKILL.md sha256: `2befe7fc55bcadaa3d97dd9e8efeb633d2561c0ebe74c5a8b17c4d9e7e4520b3`

## requesting-code-review (Superpowers, selected skill only)

- Upstream: https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/requesting-code-review
- Commit: `bb92a77741419a4ab5f06e711a283343f1ada0c3` (October 9, 2026, 5:28 PM PT)
- License: MIT (`LICENSE` copied from the Superpowers repository)
- Local path: `skills/requesting-code-review/`
- Scripts: none. Includes the companion `code-reviewer.md` template from the same commit.
- SKILL.md sha256: `2180e14a448e9410bec88e6646a2d1f0ce7fdd58de27388c1e052e929679d2bc`

## app-store-review (advisory)

- Upstream: https://github.com/safaiyeh/app-store-review-skill/tree/7197cff003728b660542b37d6b6d0167fe2ec1ed
- Commit: `7197cff003728b660542b37d6b6d0167fe2ec1ed` (October 16, 2026, 5:17 PM PT)
- License: MIT (`LICENSE` in the skill folder)
- Local path: `skills/app-store-review/`
- Layout: the root `SKILL.md` plus `rules/` (the nested pointer skill was omitted so catalog links resolve).
- Scripts: none. Advisory only; do not submit apps or store listings.
- Not copied: `.github/`, `.claude-plugin/`, `.codex-plugin/`, `.agents/`, and the upstream README installer instructions.
- SKILL.md sha256: `6499f09f671ce01c68c0460e3ae4ca5056960b10775a2314bd3775e82f53419b`

## Cloudflare official skills (dry-run only)

- Upstream: https://github.com/cloudflare/skills
- Commit: `14472d57ac968d1a0322a568077277209b259183` (November 23, 2026, 4:24 PM PT)
- License: Apache-2.0 (`LICENSE` copied into `licenses/cloudflare/` and each skill folder)
- Policy: **dry-run only**. Do not run `wrangler deploy`, Pages deploys, or any production publish. Deploy remains owner-only.
- Skills vendored (21): `agents-sdk`, `basin`, `cf-cli`, `cloudflare`, `cloudflare-app-bootstrap`, `cloudflare-email-service`, `cloudflare-one`, `cloudflare-one-migrations`, `durable-objects`, `frameworks-on-cloudflare`, `gateway-workers`, `k2`, `nextjs-on-cloudflare`, `sandbox-migrate-to-next`, `sandbox-next`, `sandbox-stable`, `web-perf`, `workers-best-practices`, `workers-development`, `workers-profiling`, `wrangler`
- No executable scripts are shipped in this snapshot.
- **Not included:** `turnstile-spin`. Its SKILL.md tells agents to run scripts that create Turnstile widgets and secrets (`auth-probe.sh`, `widget-create.sh`, `persist-skill.sh`). That is owner-only infrastructure work, so the skill is omitted rather than left discoverable with a "do not run" note.

## Official Stripe skills (not vendored)

- Intended upstream: https://docs.stripe.com/skills and https://docs.stripe.com/.well-known/skills/index.json
- Index fetched: November 24, 2026, 5:16 AM PT (11 skills listed; all advertised files downloaded for inspection only, then left out of this repository)
- License: **not published**. `LICENSE` URLs under `https://docs.stripe.com/.well-known/skills/` returned 404, and skill frontmatter has no license or SPDX field.
- Decision: this public Apache-2.0 repository does not distribute files with unknown rights (see `docs/skill-delivery/packaging.md`). The official Stripe skills remain available on Grok Bot through the existing Stripe plugin.
- Not recorded as a pin: no commit SHA is published for the docs.stripe.com pack.

## What this snapshot does not include

- Upstream `.github/` workflows, git hooks, installer plugins, or `npx skills add` / `stripe agent setup` / curl-pipe installers.
- The full Superpowers framework.
- `turnstile-spin` (see the Cloudflare section).
- Anything from the avoid list.

## Pin records

These rows are the catalog pin records. Every vendored skill appears exactly
once with a 40-character lowercase hex commit, a `SKILL.md` sha256, and a
license file path that must exist in this plugin. `scripts/validate_catalog.py`
enforces that the hashes match the files on disk.

| skill | commit | skill_md_sha256 | license |
| --- | --- | --- | --- |
| `agents-sdk` | `14472d57ac968d1a0322a568077277209b259183` | `9bda4bd3adc5ab09e30c19ea6b9a0bf673f0a4b190bf7624fc1b0dc5f1fcf9c1` | `skills/agents-sdk/LICENSE` |
| `app-store-review` | `7197cff003728b660542b37d6b6d0167fe2ec1ed` | `6499f09f671ce01c68c0460e3ae4ca5056960b10775a2314bd3775e82f53419b` | `skills/app-store-review/LICENSE` |
| `basin` | `14472d57ac968d1a0322a568077277209b259183` | `5f62ae9b86544c352db2829e1f28009b1e97e9549e10bb3081a09a08d060ef1e` | `skills/basin/LICENSE` |
| `cf-cli` | `14472d57ac968d1a0322a568077277209b259183` | `868b100095aefbaa83d8f08892044e2a6f2428760bdc12490517aab98c289bce` | `skills/cf-cli/LICENSE` |
| `cloudflare` | `14472d57ac968d1a0322a568077277209b259183` | `7eadb373863b7550bad9411f33af44ca6ef3c545d2a653383db61488cb0419ee` | `skills/cloudflare/LICENSE` |
| `cloudflare-app-bootstrap` | `14472d57ac968d1a0322a568077277209b259183` | `0e844a5d3fc39f922a51b906b4e48892610132a207c5e994521a8b0eb7535d91` | `skills/cloudflare-app-bootstrap/LICENSE` |
| `cloudflare-email-service` | `14472d57ac968d1a0322a568077277209b259183` | `3f0448eb0f9f98e1762cb5e9bedb60531587ba003d8809b3e082f6dd82cb5912` | `skills/cloudflare-email-service/LICENSE` |
| `cloudflare-one` | `14472d57ac968d1a0322a568077277209b259183` | `5e9b81bfe4ebd1737346123679eaca0004b9d3ab9a0239729103b442e0f89614` | `skills/cloudflare-one/LICENSE` |
| `cloudflare-one-migrations` | `14472d57ac968d1a0322a568077277209b259183` | `3ecfe6dba6056996af6ba0b7b7f7d180640bea1fd7a5b3187623494ce1297868` | `skills/cloudflare-one-migrations/LICENSE` |
| `durable-objects` | `14472d57ac968d1a0322a568077277209b259183` | `ef690603d7d998a25ba9748c79f399bb75d943fe1955ba258167116c101ef98c` | `skills/durable-objects/LICENSE` |
| `frameworks-on-cloudflare` | `14472d57ac968d1a0322a568077277209b259183` | `0edfc9c8090988c32b76a0be007264073a67be1c8623b72c172976d510eccda4` | `skills/frameworks-on-cloudflare/LICENSE` |
| `frontend-design` | `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f` | `d91970639e9f5c37682ac7ab60094d35f1c7c1f38d731bd56396563aee10c1d3` | `skills/frontend-design/LICENSE.txt` |
| `gateway-workers` | `14472d57ac968d1a0322a568077277209b259183` | `63f3d183f531ceba625b33761b993264c29c3fc00dbd982e2180767d1e9fb768` | `skills/gateway-workers/LICENSE` |
| `k2` | `14472d57ac968d1a0322a568077277209b259183` | `94c199923bd4d3eb836dbdd360a37d254b2249ed9f1cb3e20421ed2d34996587` | `skills/k2/LICENSE` |
| `nextjs-on-cloudflare` | `14472d57ac968d1a0322a568077277209b259183` | `2e7d42b5a42a871a9ac3f1f638ac4d44e612650544058480164bd4994251a7dd` | `skills/nextjs-on-cloudflare/LICENSE` |
| `playwright-cli` | `99d4c415db3794d1c989be16ac4987f4529e3220` | `ec07841c9c47b311d9c20111397e69411004e7ea46481aa12f7b9e0510195aa7` | `skills/playwright-cli/LICENSE` |
| `requesting-code-review` | `bb92a77741419a4ab5f06e711a283343f1ada0c3` | `2180e14a448e9410bec88e6646a2d1f0ce7fdd58de27388c1e052e929679d2bc` | `skills/requesting-code-review/LICENSE` |
| `sandbox-migrate-to-next` | `14472d57ac968d1a0322a568077277209b259183` | `a3afd0eccaf4100ff48613f985c201469365fa58b1747006c49486aecdc5564c` | `skills/sandbox-migrate-to-next/LICENSE` |
| `sandbox-next` | `14472d57ac968d1a0322a568077277209b259183` | `86e00416e89acf7f77b4d3926301345725abbc6e3dedec81493fd62ee69f1104` | `skills/sandbox-next/LICENSE` |
| `sandbox-stable` | `14472d57ac968d1a0322a568077277209b259183` | `be65d5c94fc2baf862b5025a9782188af226778e1a2126dfe8681e2501d8ae0a` | `skills/sandbox-stable/LICENSE` |
| `security-best-practices` | `5c8f1e26803bcfaffeceef1e7accbcf7e388417a` | `7b3dae1ffc5434d890f3c65c8f552af52d0307fab3b35dec13013c9ca3844c4f` | `skills/security-best-practices/LICENSE.txt` |
| `verification-before-completion` | `3be5aad3dd2400ef23b15680969f4bcd3b6d7b8b` | `2befe7fc55bcadaa3d97dd9e8efeb633d2561c0ebe74c5a8b17c4d9e7e4520b3` | `skills/verification-before-completion/LICENSE` |
| `web-perf` | `14472d57ac968d1a0322a568077277209b259183` | `0160c9e7f1b73eb80347efd899a6082219d43bb9de30424667c8017628a48469` | `skills/web-perf/LICENSE` |
| `workers-best-practices` | `14472d57ac968d1a0322a568077277209b259183` | `01c452fd0b6b3caeb4c3b06f87893e52d8e95e32f691911c1644060e00dafa0e` | `skills/workers-best-practices/LICENSE` |
| `workers-development` | `14472d57ac968d1a0322a568077277209b259183` | `322df9f4013457c2a3ff2790ab7b553e301c418d8de7e5b6e2d560e5ac800b1e` | `skills/workers-development/LICENSE` |
| `workers-profiling` | `14472d57ac968d1a0322a568077277209b259183` | `fec05a080c90f019e1e93e5e1ca3416bb89362655dfc158458301f461cb29839` | `skills/workers-profiling/LICENSE` |
| `wrangler` | `14472d57ac968d1a0322a568077277209b259183` | `a39de5c69f50e88759736a6ec7ad07f402c15f7a58a3224bcf979dce42013b13` | `skills/wrangler/LICENSE` |


## Gitleaks note

`gitleaks detect` reports a generic-api-key hit on
`skills/workers-best-practices/references/configuration.md` line 82. That line is
an official Cloudflare anti-pattern example (a short placeholder in a "Secret in
version control" snippet), byte-identical to the pinned upstream commit. It is
allowlisted in the repository `.gitleaksignore`. No live credential is included.
