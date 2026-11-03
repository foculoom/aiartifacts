---
name: experience-review
description: Review a rendered website or interface against its product and identity brief, with evidence-based usability, visual hierarchy, and customer-journey findings. Use for experience audits or persona-based product testing across apps and games, not authorship detection or automatic redesign.
---

# Experience review

Inspect the actual experience before judging it. Establish the audience, intended action, approved identity, release status, requested scope, and source revision. Record the skill revision and brief revision, using unknown when unavailable. A screenshot supports visual observations; it does not prove links, keyboard behavior, delivery, or responsiveness.

## Inspect the relevant journey

Use the available browser or rendering tools and follow navigation and direct-entry paths. Select only relevant references:

- [Publisher sites](references/publisher-sites.md): a portfolio with products at different release stages.
- [Product pages](references/product-pages.md): audience, value, availability, and conversion paths.
- [Interactive experiences](references/interactive-experiences.md): state, feedback, help, input, and return paths.
- [Product-testing personas](references/product-testing-personas.md): reusable behavior lenses, accessibility/context overlays and app/game scenarios. Use when persona-based coverage is requested or would address a specific audience risk, not for every small correction.
- [Operational status](references/operational-status.md): public health claims, incident states, and private measurement views.
- [Production acceptance](references/production-acceptance.md): a requested production-quality decision, material visual/game-art change, or owning-project acceptance gate. It is not required for every small edit.

Compare with approved identity decisions and the project's voice brief. Review hierarchy, product differentiation, availability labels, action semantics, responsive layouts, and applicable accessibility behavior. Inspect desktop and narrow renders when available. Test focus, keyboard paths, labels, contrast, reduced motion, and error states only where tools and authorization permit; describe exactly what was measured or exercised. If rendering is unavailable, provide a source-only review and leave visual conclusions unverified.

For a stateful experience, inspect starting, active, paused or overview, and recovery states separately. Compare the controls shown with actions that actually work in each state, including keyboard focus and touch affordances. When a released experience, canonical source, and candidate build differ, identify each exact revision or artifact and test the relevant journey in each; a source diff does not establish what visitors receive. Follow the [interactive experience reference](references/interactive-experiences.md) for the bounded state and artifact comparison.

For persona-based testing, select lenses from the product's actual audience and requirements; record simulated analysis, scripted execution, agent-operated UI and human sessions separately. Use the owning test/finding record rather than creating a parallel gate. Personas never supply missing human evidence or authorize real-world actions.

Do not submit live forms, make purchases, alter settings, or publish content without task authorization. Use local fixtures for destructive or externally visible states. Never infer delivery from a submit button, a public release from a marketing page, or privacy compliance from the absence of an obvious analytics script.

## Use evidence suited to each medium

For each relevant journey, identify the visual, audio and synchronized feedback
that carry the product's meaning. Before accepting a lane, inspect the final
artifact with an available, authorized capability that can actually perceive that
medium: a vision-capable reviewer for captured renders, and an audio-capable
reviewer or human listener for recorded sound. Do not infer perceptual quality
from source, transcripts, event logs, waveforms or file presence alone.

Check that the capture path retains the relevant output, using an authorized
known-good fixture or a direct comparison where available. A silent audio track,
black frame or dropped cue may be a recording or routing problem. Record that
sanity check before attributing missing or distorted media to the product; if
capture integrity is unresolved, keep the product finding inconclusive.

For visuals, inspect the intended sizes, meaningful states and transitions. For
audio that exists or is promised, sample representative ambience, music, speech
and action/error cues as applicable; assess intelligibility, balance, abrupt or
missing cues, repetition and timing against the brief. Check supported mute,
volume and interruption behavior and necessary non-audio alternatives. Inspect
synchronized audiovisual evidence when judging cue timing or cause and effect;
a detached sound asset does not establish runtime playback. Do not add sound to
an intentionally silent product or require irrelevant sensory checks.

Record the artifact, capture provenance, device/output context, clip timestamps
or frames inspected, actual tools/capabilities, reviewer type and model/version
only when verifiable. Distinguish measured signal checks from perceptual findings
and source predictions. Mark unavailable media, capture or review capabilities
unverified, with the smallest next check. Do not install tools, use paid services,
upload media or expand data sharing without authorization. Multiple persona
prompts do not imply multiple models or independent listeners. Reuse the owning
acceptance record; this adds evidence coverage, not another release gate or a
guarantee of quality, enjoyment or accessibility.

## Report useful findings

For each actionable finding, provide the URL or component, source file when verified, observed evidence, consequence for the visitor, classification, proposed correction, and testable acceptance criterion. Classify findings as defect, strategic tradeoff, aesthetic preference, or hypothesis; do not disguise preference as a failure. Use the owning project's severity scale. If it has none, prioritize critical broken journeys or exposure as P0, important usability/clarity problems as P1, and optional refinements as P2. Do not manufacture findings or numerical quality scores.

State what works and should remain. Separate observed facts from inferred causes and proposed changes. Include coverage and untested states. A passing automated check is not accessibility certification; clicks are not demand or purchases; a polished forecast interface is not accuracy evidence. Do not invent uplift, customers, measurements, or test results.

When an acceptance decision is required, make it explicit and bounded to the
artifact, brief and inspected scope. A technically correct export can still need
visual rework; a restrained design can meet its brief without more decoration.
Do not turn "no findings" in one review lane into whole-product approval.

Recommend the smallest correction supported by the findings. Prose revisions can use an available editorial skill and the project voice brief, but this review remains independently usable. Record affected revisions so later changes can invalidate the relevant findings without pretending that an old report covers new work.
