---
name: human-voice
license: Apache-2.0
description: Review and rewrite reader-facing copy to remove stock AI wording and stiff formulas, in the project's own voice. Use for websites, product pages, and interface text; not as an authorship test or a substitute for editorial judgment.
---

# Human voice

Flag stock AI wording and stiff formulas in reader-facing copy, then rewrite in the project's own voice. Keep facts, legal disclosures, brand terms, and accessibility text intact. This is a style lint and a rewrite guide. It is not an authorship test, a "human-sounding" score, or proof that AI was or was not used.

The editorial-writing skill still governs audience, medium, and project voice. Use this skill when the job is to catch clichés and formulaic phrasing and to rewrite them. If a project voice brief exists, follow it; do not impose a generic "friendly" tone.

## What to check

Run the bundled linter on the files that readers will see (pages, interface strings, metadata), not on private notes or test fixtures unless they are themselves published:

```sh
node <skill-directory>/scripts/voicelint.mjs
# optional: --config path/to/voicelint.config.json
# optional: --json
```

The linter looks for:

1. **Stock words and phrases** listed in [words and patterns](references/words-and-patterns.md), including *seamless*, *elevate*, *unlock*, *unleash*, *empower*, *curated*, *leverage*, *delve*, *tapestry*, and *testament*.
2. **Formulas**: "not just X, it's Y"; "it's not about X, it's about Y"; Title Case Slogans in headings; vague rule-of-three lists ("fast, reliable, and intuitive"); stacked exclamation marks; heavy em-dash use in headings or dense passages.

Inspect every flag in context. A genuine use can stand: a game that literally unlocks a door, a museum that literally curates a collection, or a proper name. Record allowed exceptions in `voicelint.config.json` with a reason. A clean run is not a quality certificate.

If Node.js or the linter is unavailable, do the same review by hand against the word and pattern lists, and say that the linter was not run.

## How to rewrite

Follow [rewrite guidance](references/rewrite-guidance.md). Say the concrete thing the reader can do or will get. Cut padding. Prefer ordinary verbs. Keep the project's rhythm rather than swapping one cliché for another. Do not invent claims, customers, or results to sound warmer. Do not add lived experience you do not have.

## Limits

- Do not claim to detect whether a person or a model wrote the text. Automated detectors have error rates, and many of these words appear in ordinary human writing. Wikipedia's field guide, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), makes the same point: the signs are observations, not proof, and they are not a substitute for fixing deeper problems such as unsourced claims.
- Do not rewrite quotations, legal or medical wording, or an approved brand line without asking.
- Do not publish private briefs or examples in this skill.

Cite the sources in [sources](references/sources.md) when you describe why a pattern is flagged. Deliver the revised copy or a passage-level review in the format requested.
