# Editorial

Review or revise reader-facing prose for its audience, medium and project voice.
The [editorial-writing skill](skills/editorial-writing/SKILL.md) supports websites,
game text and longform writing. Product briefs remain with their owners.

This is an Agent Plugins package with the editorial-writing skill. The OpenAI UI
extension is optional client metadata. Other clients can use the shared skill
without an OpenAI connector, another plugin, an API key or a provider account.

A further unreleased skill, `human-voice`, is maintained in this repository at
`plugins/editorial/skills/human-voice`. It lints reader-facing copy for stock AI
wording and stiff formulas. It is listed in the catalog README, is not an
authorship test, and is not part of the earlier Editorial distribution allowlist
under `evals/skill-delivery/pilot/`.

## Install a reviewed revision

Use an immutable reviewed Git commit or release tag and inspect its contents
before enabling it. A plugin-capable client installs this repository's
`plugins/editorial` subdirectory. A standalone skill installer uses
`plugins/editorial/skills/editorial-writing` from the same revision. Do not
silently substitute `main` for the revision you tested. Installation commands
and accepted source syntax vary by client; record the actual CLI version,
source and installed file hashes.

The package is prepared for Awesome Copilot external-plugin review and the
skills.sh installer. Preparation is not acceptance, a listing or evidence that
every supported client can perform the workflow. No marketplace submission or
automatic public indexing is performed by this package.

## Dependencies and evidence

Read [the skill dependency and provenance record](skills/editorial-writing/DEPENDENCIES.md).
Python is optional for editorial-writing; Node.js is optional for the separate
human-voice linter. Editorial work remains possible without the advisory linters.
The linters' tests assess code behavior, not prose quality or authorship. Check ordinary
activation, unrelated requests, useful outputs and unavailable-tool handling
in the runtime you actually use. Agent review does not establish human reader
testing, authorship, factual accuracy or commercial results.

Apache-2.0: [package license](LICENSE). The editorial-writing skill carries its own identical
license for standalone installation. No automatic update, publication, telemetry
or customer-data collection is implemented here; an installer may have its own
telemetry and update settings.
