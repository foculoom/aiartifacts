# Public Skills

**Advisory / dry-run only, no deploys.** App Store review is advisory and
must not submit. Cloudflare skills are dry-run only; do not run
`wrangler deploy`, Pages deploys, or any production publish. Deploy and
store submission stay owner-only.

Pinned copies of public upstream skills approved for studio use. This plugin
is the central install point so other repositories do not need their own
copies. The marketplace catalog points here:
[`.agents/plugins/marketplace.json`](../../.agents/plugins/marketplace.json).

Install from this repository's marketplace:

```
codex plugin marketplace add foculoom/aiartifacts
```

Then install **Public Skills**. Pin the consuming project to a reviewed tag or
commit SHA of this repository. Appearing in the catalog does not publish the
plugin to a universal directory.

## Studio rules for this snapshot

- **Advisory / dry-run only, no deploys.** See the notice at the top of this
  file.
- Official Stripe skills are **not** in this snapshot; see
  [PROVENANCE.md](PROVENANCE.md) for why.
- `turnstile-spin` is omitted because its instructions tell agents to run
  scripts that create Turnstile widgets and secrets.

Skill bodies are copied from upstream without edits. License texts travel with
each skill. Pins, licenses, and `SKILL.md` hashes are in
[PROVENANCE.md](PROVENANCE.md).
