# Prepare an exact, reviewable export

Keep one canonical source. Choose a standalone skill or an existing plugin
according to the target's actual install contract. Copy only reviewed files;
do not export an entire repository to avoid deciding what belongs in the skill.

## Before export

- Review the selected instructions and every reachable script. Include required
  references and resources; reject broken links and paths escaping the package.
- Record source URLs/revisions, authorship, modifications and applicable
  licenses/notices for copied code, prose and assets. Unknown rights block
  distribution of the affected file; a license string alone is insufficient.
- Include license text and applicable attribution in each independently
  installed payload. A repository-root notice does not travel with a skill-only
  or plugin-subdirectory install unless included there.
- Declare required and optional dependencies with tested versions, acquisition
  sources, license, network/credential needs and unavailable-tool behavior.
  Use existing lockfiles; do not install a remote tool or vendor its code merely
  to inspect it. Record any reviewed external validator version separately.
- Inspect the allowlist for credentials, private links/context, identifying
  fixtures, local paths, logs, caches and unrelated product files. Use synthetic
  or cleared examples. Keep the complete review evidence outside the payload.

## Optional standard-library helper

The repository [exporter](../../scripts/skill-delivery/export_skill.py) requires
Python 3.9+ and does not fetch, install, execute payload scripts, submit or
publish. Run these commands from the repository root. Both source root and
output must be absolute; output must be new.

```sh
python3 scripts/skill-delivery/export_skill.py export \
  --source-root "$SOURCE_ROOT" --config "$EXPORT_CONFIG" --output "$EXPORT_DIR"
python3 scripts/skill-delivery/export_skill.py verify \
  --manifest "$EXPORT_DIR/manifest.json" --archive "$EXPORT_DIR/skill.zip"
```

Use task-specific variables containing reviewed paths. The JSON config has
exactly these fields; `source_commit` is the full lowercase 40-character source
commit, and `files` maps explicit destination paths to source-relative paths:

```json
{
  "version": 1,
  "name": "example-skill",
  "kind": "skill",
  "source_commit": "0123456789abcdef0123456789abcdef01234567",
  "files": {
    "SKILL.md": "skills/example-skill/SKILL.md",
    "LICENSE": "LICENSE",
    "DEPENDENCIES.md": "skills/example-skill/DEPENDENCIES.md"
  }
}
```

This is a synthetic mapping, not a repository path to assume exists. Discover
and review the actual files. Use `kind: "plugin"` for a plugin-root payload,
including its `plugin.json`, `skills/<name>/SKILL.md`, license and dependencies.
Do not use globs or broaden the selection after a rejected path.

Outputs are `payload/`, deterministic `skill.zip`, and `manifest.json` with file
inventory, hashes and normalized modes. Each manifest file entry records
`source`, `sha256` and `mode` (`0644` or `0755`). Any executable source bit becomes
`0755`; other files become `0644`, in both staged files and archive metadata.
Ownership, ACLs and extended attributes are not preserved. The commit is a
caller-supplied label; it does not prove
that a dirty checkout matches that commit. Record working-tree state and review
the exact per-file hashes. The helper's path/link and limited sensitive-content
checks do not establish legal clearance, absence of secrets or runtime safety.

After a separately authorized installation, verify the exact installed folder:

```sh
python3 scripts/skill-delivery/export_skill.py verify \
  --manifest "$EXPORT_DIR/manifest.json" --installed-root "$INSTALLED_ROOT"
```

Verification compares inventory, hashes and modes. An installer may intentionally
add provenance metadata or change permissions. Record that transform and compare
it separately; do not silently ignore a mismatch or call the files identical.
Rebuild to a new directory after changes, rerun validation, and bind
review to the resulting manifest. A ZIP integrity pass alone can miss extra or
obsolete entries; compare the full inventory and hashes.
