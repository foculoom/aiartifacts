# Public Skills

Pinned copies of public upstream skills approved for studio use. This plugin is
the central install point so other repositories do not need their own copies.

Install from this repository's marketplace:

```
codex plugin marketplace add foculoom/aiartifacts
```

Then install **Public Skills**. Pin the consuming project to a reviewed tag or
commit SHA of this repository. Appearing in the catalog does not publish the
plugin to a universal directory.

## Studio rules for this snapshot

- Do **not** run scripts shipped inside these skills. They are kept only for
  provenance and review. See [PROVENANCE.md](PROVENANCE.md).
- Cloudflare skills are **dry-run only**. Do not run `wrangler deploy`, Pages
  deploys, or any production publish. Deploy remains owner-only.
- App Store review is **advisory**. Do not submit builds or store listings.
- Official Stripe skills are **not** in this snapshot; see PROVENANCE for why.

Skill bodies are copied from upstream without edits. License texts travel with
each skill.
