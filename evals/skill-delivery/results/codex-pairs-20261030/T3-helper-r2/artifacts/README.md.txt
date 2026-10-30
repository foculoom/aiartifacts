# Editorial-writing distribution candidate

Prepared 2026-10-30 from the supplied cleared new source, without modifying source or the old ZIP.

- `candidate/skill.zip`: fresh self-contained 11-file skill package; root SKILL.md, license, dependency record, references and optional Python helper only.
- `candidate/payload/`: exact staged equivalent of the ZIP.
- `candidate/manifest.json` and `inventory.tsv`: exact file/source/hash/mode inventory (TSV also records byte counts).
- `SHA256SUMS`: archive, manifest, reports and all other output file hashes; excludes itself.
- `CHANGE-AND-PROVENANCE.md`, `changes.diff`, `comparison.json`: changes, source/base distinction and complete old archive comparison, including excluded entries.
- `VALIDATION-AND-REMAINING-WORK.md`, `validation-results.json`, `validation/`: results, commands, limitations and next actions.
- `export-config.json`: explicit source allowlist used by the supplied exporter.
- `source-before.json`: preservation baseline for all supplied source files, including old ZIP.
- `validation-work/`: development test copy outside the distribution payload; do not distribute this as part of the skill.

The local package is verified. The checker passed 27 tests on each of old source, new source and packaged helper. Three layout-dependent exporter-suite checks did not pass; details are retained. Agent/runtime behavior and external release acceptance remain untested. No dependencies were installed and nothing was published.
