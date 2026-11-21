# Local CI

**GitHub Actions is disabled on this repository by owner decision on 2026-11-21** to keep GitHub spend at zero. Workflow files under `.github/workflows/` are kept for reference but no longer run. Do not re-enable Actions; run the checks below on a local machine and paste the commands and pass/fail results into each pull request.

## Run the checks locally

These are the same commands the retired workflow ran. Use Node 24 (or the version noted) and Python 3.12.

```bash
(cd plugins/engineering/skills/platform-boundaries/scripts/js-import-graph && npm ci --ignore-scripts --no-audit --no-fund && npm test)
for d in plugins/editorial/skills/editorial-writing/tests plugins/engineering/skills/platform-boundaries/scripts scripts/skill-delivery/tests plugins/release/skills/release-evidence/scripts plugins/reporting/skills/decision-reporting/scripts plugins/automation/skills/local-credential-runner/tests plugins/design/skills/product-identity/tests plugins/performance/skills/performance-regression/tests; do python3 -m unittest discover -s "$d" -q || exit 1; done
python3 -m unittest discover -s evals/skill-delivery -p 'test_*.py' -q
python3 scripts/validate_catalog.py
python3 -m json.tool .agents/plugins/marketplace.json >/dev/null && python3 -m json.tool plugins/editorial/plugin.json >/dev/null && python3 -m json.tool plugins/design/plugin.json >/dev/null
python3 -c 'import pathlib,tomllib;[tomllib.load(open(p,"rb")) for p in pathlib.Path("agents/codex").glob("*.toml")]'
```

Verified on 2026-11-21 ~02:10 PT on the studio Linux box from a fresh clone of the default branch: **all 12 steps passed**.

## Required status checks

The default branch's ruleset still requires `editorial`. It came from the retired workflow and can no longer report, so **pull requests here cannot merge until the owner removes or changes that requirement**. Changing rulesets, branch protection and required checks is the owner's decision; agents must not change them. Paste the local results above into the PR so the owner can review them.

## How this repository deploys now

No deploys. Other repos check out pinned refs of this repo for their platform-boundary tools. Their `CI.md` shows how to do that locally.
