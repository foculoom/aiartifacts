# Distribution routes

Official documentation checked **2026-10-30**. Recheck the linked contracts
before an external action; record the tool version and source revision used.
Commands below illustrate separately authorized checks or installation using
already reviewed tools. They do not authorize downloading executables, enabling
telemetry, installing globally, submitting, or publishing.

Inspected source snapshots: [Awesome Copilot `5269f7e`](https://github.com/github/awesome-copilot/tree/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd)
and [skills CLI `92a9a34`](https://github.com/vercel-labs/skills/tree/92a9a34ac3bf88e695e468b90c7bf32f163d32c8).
These identify the documentation review, not installed or behavior-tested tools.

## Shared source and runtime boundary

[Agent Skills](https://agentskills.io/specification) defines the skill folder
and `SKILL.md` format. [Agent Plugins](https://agent-plugins.org/specification)
defines a package with root `plugin.json`, standard `skills/` discovery and
optional MCP configuration. Neither certifies a skill's runtime behavior.
Copilot, Codex and other agents are runtimes with their own discovery, tools and
permissions. Optional client metadata does not make those features portable.

Use the existing plugin when it already satisfies a target. Keep the same skill
source for standalone installation. Do not add an MCP server, marketplace, or
API adapter unless the actual workflow requires it.

## Awesome Copilot

[`github/awesome-copilot`](https://github.com/github/awesome-copilot) is a
curated resource collection and plugin marketplace. Read its current
[instructions](https://github.com/github/awesome-copilot/blob/main/AGENTS.md),
[contribution policy](https://github.com/github/awesome-copilot/blob/main/CONTRIBUTING.md)
and [external-plugin form](https://github.com/github/awesome-copilot/blob/main/.github/ISSUE_TEMPLATE/external-plugin.yml).

For an existing public plugin, prepare an **external-plugin issue draft** with
name, description, public `owner/repo`, plugin-root `source.path`, semver,
author, license, keywords and immutable tag and/or full commit SHA. If both
locators are supplied they must agree. Do not open an initial PR editing
`plugins/external.json` directly. Intake runs metadata, Agent Plugins manifest,
Vally skill/reference lint, version consistency and Copilot install checks;
human maintainers decide acceptance, then automation prepares a listing PR.
Listed-version changes use reviewed PRs; periodic re-review is also documented.

Use the tool interface actually installed. `@microsoft/vally@0.20.0` is a
library, not the `@microsoft/vally-cli` executable package. The upstream
[quality-gate implementation](https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/eng/external-plugin-quality-gates.mjs)
calls `runLint({ rootPath })`; it does not need model inference. In an already
reviewed tool workspace resolving that exact library version, the equivalent
bounded check is:

```sh
node --input-type=module - "$CANDIDATE_ROOT" <<'JS'
import { runLint, LintConsoleReporter } from '@microsoft/vally';
const result = await runLint({ rootPath: process.argv[2] });
await new LintConsoleReporter({ verbose: true, stream: process.stdout }).report(result);
process.exitCode = result.passed ? 0 : 1;
JS
```

Pin and review the tool workspace's dependencies first. This command only lints;
the manifest-schema check, installation smoke test and behavior evaluation remain
separate. Do not install a different package merely to make a guessed binary run.

The public Editorial pilot already has its plugin root at
[`foculoom/aiartifacts/plugins/editorial`](https://github.com/foculoom/aiartifacts/tree/main/plugins/editorial).
Use `source.repo: foculoom/aiartifacts` and `source.path: plugins/editorial` at
the reviewed immutable revision. Retain Apache-2.0 and the existing
`extensions.com.openai` metadata: conforming clients ignore unsupported
extension namespaces. Include notices and all dependencies within the selected
plugin subtree. This is a preparation route, not a claim of listing or tested
Copilot behavior.

For a skill with no reusable plugin, the alternative is a direct contribution
under upstream `skills/<name>/` through a PR to `main`. That route accepts
contributions under MIT and requires meaningful usefulness beyond general model
capabilities. Reuse upstream `npm run skill:create`, `npm run skill:validate`,
`npm run build` and line-ending normalization when applicable in an approved
upstream checkout. Do not relicense third-party material without rights. The
[submission gate](https://github.com/github/awesome-copilot/blob/main/docs/maintainers/submission-gate.md)
distinguishes blocking structural checks from advisory/completion-only lint.

[Copilot's plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference)
documents direct source installation and marketplace installation separately:

```sh
copilot plugin install foculoom/aiartifacts:plugins/editorial
copilot plugin marketplace browse awesome-copilot
```

The direct command follows source resolution; it is not an immutable candidate
receipt. For candidate tests, use the reviewed local plugin directory in an
isolated runtime, record the resolved bytes, and test actual task behavior.
After verified listing, the marketplace form is `NAME@awesome-copilot`.
Catalog refresh and installed-plugin update are separate operations.

GitHub also documents [`gh skill`](https://cli.github.com/manual/gh_skill) in
public preview (GitHub CLI 2.90.0+). It can preview/install/update standalone
skills; [`gh skill publish --dry-run`](https://cli.github.com/manual/gh_skill_publish)
validates without publishing. Plain `gh skill publish` creates a GitHub release,
not Awesome Copilot acceptance. Do not run `--fix` as a read-only check. Updates
can modify installed files and need separate scope; preserve explicit pins.

## skills.sh

[skills.sh](https://skills.sh/docs) is a directory/leaderboard backed by the
[open `skills` CLI](https://github.com/vercel-labs/skills). It installs skill
files into agent-specific locations; it is not an agent runtime. Its
[creating guide](https://github.com/vercel-labs/skills/blob/main/docs/creating-skills.md)
documents discovery layouts and optional `skills.sh.json` paths. Prefer an
explicit skill URL when a repository contains unrelated plugins.

Using an already reviewed, version-pinned CLI in an isolated project:

```sh
DISABLE_TELEMETRY=1 skills add "https://github.com/foculoom/aiartifacts/tree/main/plugins/editorial/skills/editorial-writing" --list
DISABLE_TELEMETRY=1 skills add ./reviewed-editorial-skill --skill editorial-writing --agent github-copilot --copy
```

The first command discovers without installing; replace `main` with the reviewed
immutable revision for a candidate and confirm the CLI's resolved source. The
second is a synthetic local path to the reviewed skill payload, not a path to
assume exists. Explicit agent/project selection avoids broad global installs.
Use installed hashes and lock/provenance records to establish what was tested.

The [CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
documents `skills find`, `skills list`, `skills check`, and `skills update`.
Select and record a reviewed published version and its Node requirement rather
than running an unpinned `npx skills`. Verify installed `skills --help` before
using a documented command: the 2026-10-30 preparation found that skills 1.7.4
help omitted `check` despite its presence in source documentation. Do not claim
that command was exercised from a documentation lookup. Updates fetch new
content; they do not renew behavioral acceptance automatically.

The [FAQ](https://skills.sh/docs/faq) describes leaderboard discovery through
installation telemetry. A successful install does not prove the page is already
indexed, ranked, audited, or curated; verify each claimed public state and date.
The [CLI troubleshooting guide](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md)
documents telemetry controls. Keep telemetry disabled for isolated checks;
do not manufacture installs to influence rankings.

The documented [catalog API](https://skills.sh/docs/api) supplies read endpoints,
not a general skill-publishing endpoint. No pack, Vercel account, paid service,
or API integration is required for this single-skill route. Do not claim paid
distribution or revenue from discovery metrics. Maintainers own source updates;
external directory/audit behavior remains outside the package's control.
