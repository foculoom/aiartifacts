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
once with a 40-character lowercase hex commit, a per-skill file manifest
sha256, a license file path, and any NOTICE paths that must exist.
`scripts/validate_catalog.py` checks that narrative `- Commit:` lines agree
with this table, that listed LICENSE and NOTICE files are present, and that
the manifest hash matches every regular file in the skill folder (not only
`SKILL.md`). The manifest is the SHA-256 of sorted lines
`path<NUL>file-sha256<NUL>mode\n`, where mode is `0755` if any execute bit
is set and `0644` otherwise.

| skill | commit | manifest_sha256 | license | notice |
| --- | --- | --- | --- | --- |
| `agents-sdk` | `14472d57ac968d1a0322a568077277209b259183` | `c15093574e99161c1bb9279b83ec8c91f30c3e05b0bdcc6313d0c3ab5a289f40` | `skills/agents-sdk/LICENSE` | |
| `app-store-review` | `7197cff003728b660542b37d6b6d0167fe2ec1ed` | `ff075858f5c228d5f005bcf4ea145b37adf6384768605840640b39e540dbe82c` | `skills/app-store-review/LICENSE` | |
| `basin` | `14472d57ac968d1a0322a568077277209b259183` | `6db555159c9855d141ea45acd2f55e5fc7d7b20709bd840ebe3fbc6fab90f44a` | `skills/basin/LICENSE` | |
| `cf-cli` | `14472d57ac968d1a0322a568077277209b259183` | `bf93841304901b9af1300c53cbf3ff5da05e10f40f2abaffc2be115644fbab10` | `skills/cf-cli/LICENSE` | |
| `cloudflare` | `14472d57ac968d1a0322a568077277209b259183` | `a9b58245fc23cd96d99feef351c5731b95f454f64268249d5282f811bdc53000` | `skills/cloudflare/LICENSE` | |
| `cloudflare-app-bootstrap` | `14472d57ac968d1a0322a568077277209b259183` | `81460010490cce500de0b59f5c9914a3d8ed292bfe0620993d5f63035c6830e9` | `skills/cloudflare-app-bootstrap/LICENSE` | |
| `cloudflare-email-service` | `14472d57ac968d1a0322a568077277209b259183` | `a91ab52792799e1341391af7d0c838786bb555428631b2d370605942962ad551` | `skills/cloudflare-email-service/LICENSE` | |
| `cloudflare-one` | `14472d57ac968d1a0322a568077277209b259183` | `d60e177e65ea82398b68e53d65ae233381ce1752be8258b8117e28e366af3839` | `skills/cloudflare-one/LICENSE` | |
| `cloudflare-one-migrations` | `14472d57ac968d1a0322a568077277209b259183` | `76a1b3f60e933cf3cfc87f8b49037873ecf36b46441007d4ce5aabcb296653d3` | `skills/cloudflare-one-migrations/LICENSE` | |
| `durable-objects` | `14472d57ac968d1a0322a568077277209b259183` | `32f9b8260f3fd0f1a06478d3ef1bd0e888333229e816a8437c6f6ddf723595ff` | `skills/durable-objects/LICENSE` | |
| `frameworks-on-cloudflare` | `14472d57ac968d1a0322a568077277209b259183` | `d7a7293d2410000b8e962b7b2a2bf23e9434749894243ce8b9ab6cf60447fa55` | `skills/frameworks-on-cloudflare/LICENSE` | |
| `frontend-design` | `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f` | `1493db36e9bd1ec97016d781912cfa9cb45ec85f5ec47d587213dd9fef7019eb` | `skills/frontend-design/LICENSE.txt` | |
| `gateway-workers` | `14472d57ac968d1a0322a568077277209b259183` | `7c36ab1ffb4fd002d9477daf98e321d9480987716f7171fbffe65eab953b474c` | `skills/gateway-workers/LICENSE` | |
| `k2` | `14472d57ac968d1a0322a568077277209b259183` | `6c5df0b1455f38944c9a6a815f0f84b71b91ea5e5a87febbb83992a92f01f023` | `skills/k2/LICENSE` | |
| `nextjs-on-cloudflare` | `14472d57ac968d1a0322a568077277209b259183` | `fac3b00e0bf31ac245c19e30d1882725cec803df01b3bbbc8e9687c4e17c3b29` | `skills/nextjs-on-cloudflare/LICENSE` | |
| `playwright-cli` | `99d4c415db3794d1c989be16ac4987f4529e3220` | `fa1525492e65e7b1dd6269ebf44dd08febcabf9b2af8a82996ac618a22745c9c` | `skills/playwright-cli/LICENSE` | `skills/playwright-cli/NOTICE, licenses/playwright/NOTICE` |
| `requesting-code-review` | `bb92a77741419a4ab5f06e711a283343f1ada0c3` | `694d2402cc10b14af0afb2c4025d20a8b9d33971f2b483f464f58fac4597c8b0` | `skills/requesting-code-review/LICENSE` | |
| `sandbox-migrate-to-next` | `14472d57ac968d1a0322a568077277209b259183` | `a8030db83aaf217ddd85aab9991f4fc0c747f2603b6a9e9e340ca1a2a191bde4` | `skills/sandbox-migrate-to-next/LICENSE` | |
| `sandbox-next` | `14472d57ac968d1a0322a568077277209b259183` | `fac710633b734512f529d880699849a121f3738e2f30f9f33cde4d80f59ac036` | `skills/sandbox-next/LICENSE` | |
| `sandbox-stable` | `14472d57ac968d1a0322a568077277209b259183` | `99006ff3b6240de0e157e762daa3e05fd6c95604c7e255d674283da713d34bac` | `skills/sandbox-stable/LICENSE` | |
| `security-best-practices` | `5c8f1e26803bcfaffeceef1e7accbcf7e388417a` | `bc209f6dfc0ec6a3042a0fb7c206f4d37d127fff74a6e27e1c844d612d197e01` | `skills/security-best-practices/LICENSE.txt` | |
| `verification-before-completion` | `3be5aad3dd2400ef23b15680969f4bcd3b6d7b8b` | `f70bc4fba7bcbb832ae42c87b5449bafd0f3303380389bffda89d7d073cfdc71` | `skills/verification-before-completion/LICENSE` | |
| `web-perf` | `14472d57ac968d1a0322a568077277209b259183` | `b32489e5568dc4c69d7c81baa44a2024494c00cf09e542bebc1cd8c0e9dba91a` | `skills/web-perf/LICENSE` | |
| `workers-best-practices` | `14472d57ac968d1a0322a568077277209b259183` | `819de30a59182f6476a1d98783ed6ad1ebcd8945383c7feacf71c2daef0e8dcb` | `skills/workers-best-practices/LICENSE` | |
| `workers-development` | `14472d57ac968d1a0322a568077277209b259183` | `c8a89329ddc7129506262947138d57ca48f041e2df2b07fb78928f1b661c2178` | `skills/workers-development/LICENSE` | |
| `workers-profiling` | `14472d57ac968d1a0322a568077277209b259183` | `b7bd8a2462a9bcf13aa4f038f6c74ff52617508c6b286fd894f20ce7439e2ec3` | `skills/workers-profiling/LICENSE` | |
| `wrangler` | `14472d57ac968d1a0322a568077277209b259183` | `7a3dfefbe4da7f8f6d1d280617d56ae0a149f8610b861cdcd3451a27f890ee3f` | `skills/wrangler/LICENSE` | |

## License copies

Top-level copies under `licenses/` are convenience copies of upstream
license texts. They are not a substitute for the per-skill LICENSE files.
`scripts/validate_catalog.py` requires each listed path to exist and the
directory manifest (same format as the per-skill manifests) to match.

- licenses/ manifest sha256: `66c1c1fd81ecf858aa146eb93951a59afcabdd2aafacec9a6b45a5ee84d78bca`

| path |
| --- |
| `licenses/app-store-review/LICENSE` |
| `licenses/cloudflare/LICENSE` |
| `licenses/frontend-design/LICENSE.txt` |
| `licenses/playwright/LICENSE` |
| `licenses/playwright/NOTICE` |
| `licenses/security-best-practices/LICENSE.txt` |
| `licenses/superpowers/LICENSE` |

## Gitleaks note

`gitleaks detect` reports a generic-api-key hit on
`skills/workers-best-practices/references/configuration.md` line 82. That line is
an official Cloudflare anti-pattern example (a short placeholder in a "Secret in
version control" snippet), byte-identical to the pinned upstream commit. It is
allowlisted in the repository `.gitleaksignore`. No live credential is included.
