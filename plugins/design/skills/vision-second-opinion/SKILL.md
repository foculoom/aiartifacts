---
name: vision-second-opinion
description: Run a structured, repeatable vision-model review of screenshots from an exact build, as a second opinion beside human visual sign-off. Use for release candidates; not as a verdict, a design generator, or a substitute for measured contrast.
---

# Vision second opinion

Ask a vision-capable model to review screenshots of a specific build, then treat its output as a second opinion. A person decides. The model's notes may raise at most a Medium on their own; a High still needs a human confirmation or a measured contrast failure.

## Keep the check reproducible

1. Capture screenshots from the exact artifact under review (the same commit or build the release names), served the way a visitor would see it, including the project's content security policy. Do not photograph a different branch, a stale cache, or a mock.
2. Use a fixed set of viewports and pages, the same ones on every run for that product.
3. Use one prompt template per product, changed only by a short factual context block (product name, intended audience, what the page is for). Do not improvise a new rubric mid-review.
4. Use only the project's designated vision account and model. Do not create a new vendor account to run the check, and do not put API keys, account names, or request tokens in a public record.
5. Record the source SHA, artifact hash if you have one, model identifier, request ids, timestamp, and the image files you sent.

A public example of a vision routing endpoint is [fal.ai's OpenRouter vision router](https://fal.ai/models/openrouter/router/vision). This skill does not require that vendor. Whatever you use, keep the model id and prompt stable across runs so later checks are comparable.

## How to read the result

- Re-check any contrast or colour claim with a measurement. Model comments about "low contrast" are hypotheses.
- Discard findings that do not repeat when you rerun the same images and prompt, unless a human can see the issue in the screenshot.
- Do not import images, copy, or layout the model generates into the product without an explicit owner yes.
- Cost and request ids belong in the private evidence note. The public or PR summary is a short table: SHA, viewports, model, High/Medium/Low counts, and whether a human confirmed each High or Medium.

This check sits beside [visual sign-off](../visual-signoff/SKILL.md) and does not replace it. See [sources](references/sources.md).
