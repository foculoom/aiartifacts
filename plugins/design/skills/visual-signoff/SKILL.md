---
name: visual-signoff
description: Review a site or product interface against its approved color tokens and brand brief, measure contrast, and record a visual sign-off before release. Use for palette changes and brand-distinctness checks; not as a certificate of accessibility or artistic quality.
---

# Visual sign-off

Compare the rendered interface with the project's approved palette and identity brief before a visual change is merged or shipped. This skill is a review gate. It does not replace a human art director, and a clean contrast check is not WCAG certification.

## Before you look

1. Record the exact source revision (full 40-character commit SHA), the brief or token file revision, and the widths you will inspect.
2. Load the project's token list (background, surface, text, link, accent, focus ring, and any reserved status colours). If a token is missing, mark it unknown; do not invent an approved hex value.
3. Identify what must stay distinct: this product versus others in the same brand family, and light versus dark if both exist.

## What to measure

Inspect the actual render at the project's agreed widths (include a narrow phone width, a mid width, and a wide desktop width when those are in scope). For each token used on the page:

- **Text contrast** against its real background, including hover and visited states, using [WCAG 2.2 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum): 4.5:1 for ordinary text, 3:1 for large text.
- **Non-text contrast** for controls, borders that identify a control, and focus rings, using [WCAG 2.2 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast) and [Focus Appearance](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance): 3:1 against adjacent colours, and a visible focus indicator.
- **Overflow and wrapping** at the narrowest in-scope width, including type that sits on a coloured panel.
- **Brand distinctness**: the page should still read as this product, not as a sibling with the same chrome and a different logo.

Take cropped evidence of any failing control, not only a full-page screenshot. A screenshot does not prove keyboard behavior, motion, or live contrast after a theme switch you did not exercise.

## Sign-off

Classify each finding as High (illegible or misleading at intended sizes), Medium (clear contrast or layout issue that should be fixed before release), or Low (optional). Residual Lows do not block a sign-off when the owning project says so; Highs do.

Write a short record: SHA, widths, tokens checked, contrast ratios you actually measured, findings, and a verdict of PASS or FAIL. A PASS is a visual sign-off of the inspected scope only. It is not permission to merge or deploy; that still needs the project's release rules and, where they apply, an owner yes on the same SHA.

See [sources](references/sources.md) for the contrast criteria. Keep private brand bibles and unreleased mockups in the owning project.
