# Words and patterns

These are review candidates for reader-facing copy. They are not a list of forbidden English, and a hit is not evidence of authorship.

## Stock words and phrases

The bundled linter flags these forms (including ordinary inflections such as *unlocks* or *seamlessly*):

- delve, elevate, seamless, unlock, unleash, empower
- curated, tailored, robust, leverage
- journey, realm, embark, "navigate the", "in today's"
- ever-evolving, game-changer, effortless, "dive in", "look no further"
- "whether you're", crafted, meticulous, testament, tapestry
- supercharge, "transform your", harness, streamline, cutting-edge
- revolutionize, plethora, myriad
- "more than just", "to the next level", "say goodbye to"
- "perfect blend", "at the end of the day", "stand out from the crowd"

Allow a hit when the word is literal, is a proper name, or is required by the brief. Record the file, the phrase, the rule, and the reason in `voicelint.config.json`.

## Formulas

- **Not-just contrast.** Constructions such as "this is not just X, it's Y" or "it's not about X, it's about Y".
- **Title Case Slogan.** A short heading in which every significant word is capitalised, unless the words are a proper name the project already uses.
- **Vague rule of three.** A list of three items where at least two are empty quality words (*fast*, *simple*, *powerful*, *innovative*, and similar). Concrete lists ("coffee, tea and cocoa") are fine.
- **Exclamation stacking.** Two or more exclamation marks close together.
- **Em-dash habit.** An em dash in a heading, two or more in one passage, or a high density across a file.

## Related observations, not extra lint rules

Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) documents further patterns that are useful in a manual review, including puffed claims of significance, canned "challenges and future outlook" closings, and avoidance of plain *is* / *are* in favour of *serves as* or *stands as*. That page also records that the fashionable "AI vocabulary" has shifted across model eras, so this skill's list should be revisited; it is not a permanent dictionary. Those observations are not all encoded in the linter. Use them when they help the rewrite, and do not treat them as proof of authorship.
