---
name: usefulness-review
description: Judge whether a product preview is actually useful to its named audience, with a fact check, a hero-versus-data check, and a written VALUE_GATE result for an exact commit. Use before production release; not as a visual audit or a deploy step.
---

# Usefulness review

A page can be reachable, accessible, and on-brand, and still be of no use: an empty list behind a confident headline, a price with no source, a tool that does not do what it offers. This skill records that judgment for one exact commit.

## Scope

Review a private or otherwise access-controlled preview of the exact 40-character commit proposed for release. Do not treat a passing link check, a green build, or a visual PASS as usefulness.

Name the audience in one line (who this is for, and what they are trying to do). Then use the product as that person would: follow the main journey, try a few honest searches or filters, and open a representative detail page.

## What must be true

- **Standalone value.** A first-time visitor in the named audience can complete the main job, or the report must say they cannot.
- **Hero versus data.** The headline, counts, and promises on the page must match the data the page actually shows. If the hero says "16 upcoming price deadlines" and the list is empty or counts something else, that is a gap.
- **Sourced facts.** Prices, dates, names, and similar claims are checked against the project's cited sources on the day of the review. Unsourced or invented facts fail the gate.
- **Honest limits.** If the product does not show prices, or a filter does nothing without JavaScript, the copy must not imply otherwise.

Classify issues as High (blocks usefulness or misleads), Medium (should be fixed before release), or Low (optional). Highs and uncorrected Mediums fail the gate unless the owner has already accepted that specific limitation in the brief.

## The report

Write a `REPORT.md` that contains each of these lines exactly once, on its own line:

```text
Commit: <40-character lowercase SHA>
Target audience: <who, and the job>
VALUE_GATE: PASS
Hero-vs-data gap: none
```

Use `VALUE_GATE: FAIL` when the preview is not useful enough to ship, and name the gap in `Hero-vs-data gap:` instead of `none`. The optional helper `scripts/check_report.py` confirms the lines are present, unique, and well-formed; it does not judge usefulness.

A PASS is not permission to merge or deploy. Combine it with the project's [owner SHA approval](../owner-sha-approval/SKILL.md) on the same commit.

Keep raw notes, credentials, and private preview URLs out of public records.
