# Contributing

Keep each artifact focused and independently usable. An agent template, plugin,
skill, and project voice brief serve different purposes; avoid duplicating one
set of editorial instructions across them.

## Public material

Only submit material you have the right to publish under this repository's
Apache-2.0 license. Use synthetic or cleared examples in tests and evaluations.
Do not include unpublished manuscripts, private product voice briefs, customer
material, credentials, or internal review records. Product-specific guidance
belongs in the consuming project.

## Changes to editorial guidance

Describe the medium and audience the change serves. Add a small, cleared example
and a behavioral evaluation case for a new profile or a meaningful change to an
existing one. Check that the change preserves facts, deliberate repetition, and
the requested voice where appropriate. Warning-checker findings are prompts for
review; a clean result is not a quality or authorship certificate.

Run:

```sh
python3 -m unittest discover -s plugins/editorial/skills/editorial-writing/tests -q
```

Keep repository and plugin versions in sync for the first release. Later plugins
may use independent versions when they have distinct release cycles.
