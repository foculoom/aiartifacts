# Editorial distribution candidate

Prepared locally on 2026-10-30. This is a reviewable candidate, not a release or installation receipt.

- `standalone/skill.zip`: 11-file standalone editorial-writing skill; extract into a folder named `editorial-writing` when installation is separately authorized.
- `plugin/skill.zip`: 14-file editorial plugin with root `plugin.json` and standard `skills/editorial-writing/` discovery. Existing version 0.1.1 and `extensions.com.openai` preserved byte for byte.
- `inventory.json`: exact package file selection, source mapping, file hashes, modes, archive hashes and verification results.
- Each package contains `payload/`, `manifest.json`, and `export-config.json` outside the ZIP. Only payload files are in the ZIP.
- `VALIDATION.md`: checks, limits, dependencies, provenance, and next steps.
- `distribution-drafts.md`: unsubmitted Awesome Copilot intake and skills.sh preparation instructions.
- `evidence/`: actual validation output, runtime versions, and before/after source snapshots.
- `runtime-trials.json`: input-only trial plan; not executed or graded.
- `prepare.py`: reproducible local build procedure; requires fresh `standalone/` and `plugin/` output directories.

The source folder was not modified. No software was installed, permissions changed, or external submission/publication performed. Tests and caches are excluded from the installable payloads; the development tests remain in the source and their results in evidence.
