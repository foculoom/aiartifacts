# Editorial delivery pilot

One canonical workflow serves both channels: the existing Editorial plugin for
Awesome Copilot external-plugin intake, and its `editorial-writing` folder for
the skills.sh installer. No source copy, MCP server or provider dependency is
introduced. The two JSON files are explicit export allowlists, not permissions
to publish. They include the linter tests because a source-directory installer
copies those files too; caches are never included.

## Prepare an exact candidate

From the repository root, record `git status --short` and the actual source
revision. The checked-in configs retain the implementation base as a historical
label; generate an ignored config with the revision being evaluated before use:

```sh
mkdir -p build/skill-delivery
python3 - <<'PY'
import json, pathlib, subprocess
revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
for kind in ('skill', 'plugin'):
    source = pathlib.Path('evals/skill-delivery/pilot') / ('editorial-' + kind + '.json')
    record = json.loads(source.read_text())
    record['source_commit'] = revision
    target = pathlib.Path('build/skill-delivery') / ('editorial-' + kind + '.json')
    with target.open('x') as output:
        json.dump(record, output, indent=2)
        output.write('\n')
PY
python3 scripts/skill-delivery/export_skill.py export \
  --source-root "$PWD" --config build/skill-delivery/editorial-skill.json \
  --output "$PWD/build/skill-delivery/editorial-skill"
python3 scripts/skill-delivery/export_skill.py export \
  --source-root "$PWD" --config build/skill-delivery/editorial-plugin.json \
  --output "$PWD/build/skill-delivery/editorial-plugin"
python3 scripts/skill-delivery/export_skill.py verify \
  --manifest build/skill-delivery/editorial-plugin/manifest.json \
  --archive build/skill-delivery/editorial-plugin/skill.zip
```

Use a new output/config path for another candidate; do not overwrite a retained
receipt. A caller-supplied commit label does not prove the working tree equals
that commit. Preserve actual selected-file hashes and changed-file status, then
compare the committed candidate before review. Reports contain relative paths,
not machine locations, environment contents or private source text.

## Gates

Run existing catalog/editorial tests and the new exporter suite. Run pinned
upstream Agent Skills and plugin validators; do not replace a real YAML parser
with the catalog's basic checks. Test isolated installations from the same
candidate and compare their exact file inventory using `verify --installed-root`.
Turn installer telemetry off during testing. Preserve candidate identity,
runtime/model/installer versions, full public-safe responses, invocation evidence
and unknowns. See the parent evaluation procedure for held-out behavior cases.

The package carries Apache-2.0 at both independent install boundaries. Compare
both copies to the repository license. Review ownership of each new file,
borrowed material, private links, credentials and dependency notices; an automated
pattern scan cannot prove rights or absence of private context.

## Submission remains unsent

Use the [external-plugin packet](external-plugin-submission.md) after independently
reviewing the immutable candidate. Its source points to `plugins/editorial`, not
to a generated whole-repository archive. No extra wrapper or MIT relicensing is
needed. Submission, approval, listing, installation and runtime acceptance are
separate receipts. Preserve the existing v0.5.0 tag and all installed pins.

For skills.sh, an authorized public install may affect discovery telemetry;
do not manufacture install counts. Public indexing and security audit readback
must be observed separately. No paid offering or revenue assumption is included.
