---
name: editorial-writing
description: Draft, revise, or review reader-facing prose using the intended medium, audience, and project voice. Use for books, websites, and game text when clarity, rhythm, continuity, or editorial judgment matters.
---

# Editorial writing

Help the intended reader understand, feel, decide, or act as the work requires. Do not treat “human voice” as a universal style or an authorship test. Preserve the user's brief, factual claims, technical terms, accessibility requirements, and requested form. Do not invent lived experience, research, quotations, customers, or endorsements. Fiction and clearly framed hypothetical examples are fine.

## Choose the voice in context

Use the available brief and surrounding material to identify the reader, purpose, medium, and project-specific voice. Ask only if an unanswered choice would materially change the work. Select the relevant profiles below; a piece can require more than one, such as game dialogue and interface text. Do not choose solely by file extension.

- [Longform](references/medium/longform.md): books, chapters, substantial essays, and sustained narrative or instruction.
- [Web](references/medium/web.md): pages, product copy, help, and short online articles.
- [Game UI](references/medium/game-ui.md): labels, prompts, state messages, and accessible interface copy.
- [Game dialogue](references/medium/game-dialogue.md): characters, narration, choices, and branching scenes.
- [Adult](references/audience/adult.md): writing intended for adults; the brief still determines expertise and register.
- [Early reader](references/audience/early-reader.md): writing intended for children beginning to read or for adults reading to them. For other age bands, use the project's age-specific brief rather than applying this profile by default.

The project's own voice brief, character canon, terminology, and approved examples belong with that project. Apply them where provided; do not publish private source material in this skill. The profiles are decision aids, not templates that force every passage into one sound.

## Work on the passage

For revision, read enough neighboring material to understand what this passage adds. Keep its meaning and necessary detail. Start with the subject rather than a generic announcement; carry useful examples far enough to show what happens; cut repetition that adds no new effect. Preserve deliberate repetition when it supports rhythm, recall, play, or a character's voice. Choose headings, lists, dialogue, and paragraph lengths because they help this reader, not to satisfy a fixed pattern.

For review, identify the most consequential issue first. Point to the exact passage, explain the effect on this reader in this medium, and propose a specific edit. If the text works, say so narrowly. Do not manufacture findings, assign a “human-sounding” score, or claim to detect whether AI was used. [Synthetic examples](references/examples.md) show the level of diagnosis expected.

For a substantial or assembled work, also check transitions, repeated explanations, shifts in voice, factual consistency, and the parts a reader encounters outside the main text. Record the reviewed scope and source revision when the project needs a durable handoff; material changes make the affected review stale. Distinguish agent review from actual human editorial or reader testing, and never infer the latter from a clean automated check.

For substantial saved Markdown or plain text, run the bundled [prose warning checker](scripts/prose_lint.py) when available: `python3 <skill-directory>/scripts/prose_lint.py <path>`. Inspect each warning in context; keep precise terms or purposeful repetition when justified. The checker does not rewrite text, verify facts, or assess authorship, and a clean run does not establish editorial quality.

Deliver the requested prose or review in the requested format. Keep production notes out of reader-facing copy unless asked for them.
