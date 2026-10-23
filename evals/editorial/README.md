# Editorial skill forward tests

These small cases test whether the editorial skill chooses the right task and
adapts its advice to the reader and medium. All names, products, and passages
in [cases.md](cases.md) are invented. They are not customer copy, book excerpts,
or evidence of a human editorial review.

## Run manually

1. Install or enable the version of the editorial skill being evaluated. Record
   its tag or commit SHA and the model/tool version.
2. Start a fresh session for each case. Copy only the text inside that case's
   `Prompt` block. Do not show the model the expectations below.
3. Save the complete response and note whether the skill was loaded or invoked.
   If invocation is not observable, record `unknown` rather than guessing.
4. Compare the response with the case's expected behavior. Record exact evidence
   for a success or failure and turn a real failure into a regression case.

Run positive cases with ordinary skill discovery. The negative cases check that
the skill does not take over unrelated or exact-preservation work. These cases
can also be run by explicitly invoking the skill to test its scope boundary,
but record that as a separate run.

## Review rubric

For each positive case, mark each dimension `pass`, `partial`, or `fail` with a
short example from the response. Do not compute a “human voice” score.

| Dimension | Pass means |
| --- | --- |
| Task and scope | It does the requested edit or review without changing the assignment. |
| Voice fit | It fits the specified audience, medium, and project brief; it does not impose one universal tone. |
| Substance | It improves clarity or usefulness while preserving the stated facts, constraints, and purposeful repetition. |
| Honesty | It does not invent experience, evidence, outcomes, or authority. |
| Handoff | It returns the requested artifact, with concise editorial notes only when useful. |

For a negative case, record whether the requested task was completed and whether
any unsolicited prose rewrite, style lecture, or extra editorial deliverable
appeared. A failure in either is actionable. A passing pattern checker alone is
not proof that prose is effective or human-authored.

## Expected behavior by case

| ID | What to inspect |
| --- | --- |
| P1 | Tightens an adult nonfiction explanation, carries the calculation through, and removes an unsupported claim of personal experience without inventing numbers. |
| P2 | Keeps a six-year-old reader and read-aloud rhythm in view, preserves the intentional refrain and child agency, and avoids an adult business-book voice. |
| P3 | Makes a website offer and action easy to scan, removes an unsupported guarantee, and preserves the supplied eligibility and price. |
| P4 | Produces short, actionable game UI copy within the character limit, preserving the actual control and failure state. |
| P5 | Keeps two game characters distinct and the branch fact consistent; it does not flatten every line into generic plain prose. |
| P6 | Reviews rather than silently rewriting, quotes a specific issue, proposes a focused fix, and does not claim the whole work is validated. |
| N1 | Fixes the code bug and runs or explains an appropriate check; does not add a prose review. |
| N2 | Transcribes exactly, including awkward wording, without editing it. |
| N3 | Extracts the requested factual value only; does not rewrite the surrounding copy. |
