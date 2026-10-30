# Editorial writing distribution candidate

Prepared 2026-10-30. The distributable is `editorial-writing-candidate.zip`; `editorial-writing/` is its unpacked equivalent. Only these contain the distribution payload. All adjacent files are delivery evidence and tooling, not package contents.

- `package-inventory.json`: exact relative paths, byte sizes and SHA-256 for all 12 payload files.
- `package-files.sha256`: checksum list for the unpacked payload, relative to output/.
- `SHA256SUMS`: every delivery file under output/ except SHA256SUMS itself.
- `comparison.json` and `source-changes.diff`: old/new/archive comparisons, exact inventories and patch.
- `CHANGE-AND-PROVENANCE.md`: inclusion decisions, source identity and the changed examples hash.
- `VALIDATION-AND-REMAINING-WORK.md`, `validation.json`, and three `.log` files: checks, evidence and limits.
- `input-verification.json`: verified original source hashes.
- `prepare.py`: explicit allowlist and local preparation/validation procedure. It requires the supplied workspace and refuses to overwrite a populated package. It creates package/evidence files; narrative reports and final delivery-wide SHA256SUMS are maintained separately.

To verify all delivered files from output/, use `shasum -a 256 -c SHA256SUMS`. No installation is necessary. Nothing was published and no input was modified.
