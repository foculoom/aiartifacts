# Changelog

## Last reviewed — 2026-11-26 (America/Los_Angeles)

Catalog review of foculoom/aiartifacts at `2dac4dc` plus the source on this
branch. The published `v0.5.0` tag and existing consumer pins are unchanged.
The next monthly upstream review remains 2026-12-07.

## Unreleased — Gamedev 0.1.0 source: headless 3D build and test

- Add a Gamedev plugin with two generic skills: `roblox-rojo-headless-build-test`
  (Rojo, Lune, TestEZ, Selene and StyLua without Studio; geometry as data with
  pure rules and a reachability flood fill; a Lune-built `.rbxm` mounted by Rojo;
  a round-trip check of the built place; deliberate-revert proofs) and
  `godot-headless-3d-render-export` (Xvfb with llvmpipe or a user-space lavapipe
  Vulkan driver, deterministic frame capture, golden-image diff, Web export).
- Both were run on 2026-11-27 on a CPU-only Linux box; each skill records what
  that run did and did not prove. Documentation only: no scripts, tests, package
  release or consumer pin change.

## Unreleased — Design 0.2.0 source: Roblox 3D play pass

- Add a generic `roblox-3d-play-pass` Design skill: a test matrix (small and large
  phone touch, tablet, keyboard and mouse, gamepad, low-end, VR, network presets),
  a first-60-second test, camera comfort and motion-sickness checks (FOV, head bob,
  shake, auto-rotate, occlusion, flashing, FMS rating), readability, controls,
  MicroProfiler/Developer Console frame-time and memory capture, lag, young-player
  safety (content ratings, Kids and Select, text filtering, monetization pressure,
  paid random items, PolicyService, data), a fun rubric, High/Medium/Low severity
  and a report template. It separates source, headless, Studio-emulation and
  real-device evidence. Sources dated 2026-11-27; six synthetic, not-yet-run cases
  in `evals/design/roblox-play-pass/`. Documentation only.

## Unreleased — Design 0.2.0 source: Roblox 3D art direction

- Add three generic Design skills: `roblox-3d-art-direction` (style choice, palette
  with measured CIE L*, Lighting/Atmosphere/post-processing values per state, light
  plan, value structure, readability rule, asset and performance budgets),
  `3d-visual-gate` (fixed Studio camera shots, phone and low-quality captures,
  L* and dL measurement, triangle/draw-call/memory/frame-time checks, a
  review-only vision second opinion, High/Medium/Low), and `fal-image-to-3d`
  (concept → image-to-3D → decimate/UV → ≤1024 PBR bake → import, with spend and
  import approval gates).
- Cite Roblox Creator Hub pages verified 2026-11-27, including the deprecation of
  `Lighting.Technology` in favor of `LightingStyle` and `PrioritizeLightingQuality`,
  the 20,000-triangle per-mesh cap, the 1024² texture-map note and the 120-stud
  light range clamp. The fal model table is a dated catalog snapshot; no model was
  run. Documentation only: no scripts, tests, package release or consumer pin change.
- Refine the three skills after a first room pass: one shadow caster per lit
  volume (a second only for an unreachable interior, stated as an exception),
  smooth-noise flicker at ≤ 3 peaks/s (WCAG 2.3.1), client-side interior
  sub-key tweens on a zone shared with camera and audio, and a verified
  headless Blender 4.3 install and smoke test (decimate, GLB export, triangle check).
- Add three generic 3D feel skills: `3d-game-feel-tuning` (camera damping, zoom
  and occlusion, FOV kicks, rotation-only trauma shake, reduced motion; speed,
  acceleration, jump arc, coyote time and jump buffer), `roblox-spatial-audio`
  (Audio API graphs, attenuation curves, per-category listeners and faders,
  reverb, sidechain ducking, voice budget, upload path for code-generated audio)
  and `3d-feel-proof-of-work` (a measured PR checklist beside
  `audio-pr-proof-of-work`). Cite Roblox Creator Hub pages verified 2026-11-27,
  including the Studio-only `AudioStreamWriter`. Documentation only.

## Unreleased — Editorial, Design and Release 0.2.0 source

- Add a public, generic human-voice skill with a banned-word list, formula
  checks, rewrite guidance, and a dependency-free Node linter. Credit
  Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
  as a descriptive field guide, not as an authorship test.
- Add generic templates for visual sign-off against approved tokens and WCAG
  contrast, a repeatable vision-model second opinion of exact-build screenshots,
  a usefulness review with a VALUE_GATE report format, exact-SHA owner approval
  before merge or deploy, and audio PR proof of work (loudness, true peak, loop
  wraps, and a second opinion).
- Record that pinned public-skills copies already lag some upstreams
  (Cloudflare `cloudflare/skills` main has moved past `14472d57` with Flagship
  and Artifacts skills; Playwright's `playwright-cli` path has a later commit).
  Re-pinning those vendor copies is deferred to the 2026-12-07 review rather
  than mixed into this source increment.
- Clarify stale README snapshot wording for the v0.2.0 tag, and list the full
  plugin layout. No package release is included.


## Unreleased — Engineering 0.2.0 source

- Add a small pinned adaptation of Matt Pocock’s MIT TDD method, with original
  examples and mocking guidance, explicit requirements-derived boundaries and
  red–green–refactor including characterization-first pure refactoring.
- Record provenance, source-local loading and an offline regression replay.
  Preserve published v0.5.0 and all consumer pins; no package release is included.

## Unreleased — Reporting 0.1.2 source

- Add exact local-week UTC window calculation across daylight-saving changes and a focused acquisition procedure for Tally, Gmail, website analytics and separately reported aggregates.
- Require private source identity, pagination, filter, precision and freshness evidence before interpreting a complete window; preserve missing data and credential boundaries.
- Exercise the revised skill against a previously captured private weekly source set. This source revision does not change the published v0.5.0 tag or consumer pins.

## Unreleased — expert-source maintenance

- Add a read-only bundle comparison helper and synthetic conflict/unavailable
  cases; record a real Release skill dependency change missed by wrapper-only
  checks.
- Record Acorn 8.19.0 as available for assessment while retaining the 8.18.0
  lock, and update Awesome Copilot's moved first-party validation paths.
- Set a monthly review proposal within the existing engineering cadence.
  Preserve v0.5.0, plugin versions, installed consumers and their pins.

## Unreleased — relevant audiovisual evidence

- Extend experience-review with relevant visual, audio and synchronized evidence,
  capture-path sanity checks, capability/provenance records and explicit limits.
- Add synthetic app/game evidence-boundary cases, including deliberate silence,
  text-only tools, capture failure and non-game voice playback. These are text
  decisions, not proof of perceptual quality or human acceptance.
- Preserve package versions, release gates, consumer pins and data-sharing scope.

## Unreleased — reusable product-testing personas

- Extend the existing Design experience-review skill with shared behavior lenses, accessibility/context overlays and distinct app/game/nonvisual scenarios.
- Add a private-project session template and synthetic selection/evidence-boundary cases. Distinguish analysis, scripted execution, agent-operated UI and real human sessions without a universal persona gate.
- Preserve existing plugin versions, release tags, consumer pins and product-owned acceptance rules.

Changes to released artifacts are recorded here. The repository and each plugin can have independent versions; consuming projects should pin a tag or commit SHA.

## Unreleased — upstream Agent Supply Chain pilot

- Extend the existing evaluation runner with an explicit signed-in profile and
  external measurement receipts. Preserve contaminated first attempts; record
  corrected Codex activation/non-activation checks and local Linux helper tests
  without treating them as Copilot, usefulness or submission acceptance.
- Replace Editorial as the active pilot with a focused improvement to Awesome
  Copilot's existing skill; keep its canonical implementation in the contribution
  fork/upstream, with no duplicate Foculoom skill or marketplace listing.
- Add synthetic input preparation, held-out criteria, explicit export mapping
  and cleared receipts for 47 helper tests, static checks and local installation.
  Preserve the initial failed-review candidate and corrected path regressions.
- Record scoped human feedback and hold upstream submission for unresolved
  Copilot/Codex behavior, isolation and controlled-usefulness evidence. Retain
  the achieved Editorial acquisition, extra-skill deferral and existing pins.

## Unreleased — skill delivery tooling and Editorial 0.1.1

- Add explicit model/effort selection and opt-in session evidence to the
  development runner, with bounded linked-skill discovery and offline tests.
  Separate runtime records from backend identity and actual isolation. Retain
  the context-contaminated first comparison attempt and hold remaining trials.
  Clarify that a paid Copilot seat is not a distribution prerequisite; retain
  the full behavior/usefulness gate and unchanged Editorial candidate.

- Pin the single Editorial distribution candidate to reviewed merged source,
  retain fresh package manifests/configs and a verified public-source installer
  receipt. Distinguish remote acquisition from listing and runtime acceptance;
  keep the extra skill deferred and the external-plugin packet unsent.

- Retain skill-delivery documentation, ecosystem references and a Python
  standard-library exporter with explicit file allowlists, exact inventory,
  hashes, executable modes and bounded privacy/path checks. It never installs,
  submits, publishes or grants access.
- Reuse Editorial as the shared-source pilot. Include Apache-2.0 text at the
  plugin and skill installation boundaries, declare dependencies, and handle
  missing optional lint or denied source access explicitly.
- Add independent runtime/activation/failure cases, three paired usefulness
  tasks, exact packaging checks and an unsent Awesome Copilot intake packet.
  Record blocked and unverified gates separately from completed checks.
- Preserve v0.5.0, installed consumers and external distribution decisions.
- October 30 paired preparation trials favor the helper in one of three pairs,
  below the predeclared adoption threshold; controlled runtime/model evidence
  remains incomplete. Retain tooling/documentation and defer the extra skill.
- Keep standalone exporter tests independent of repository-only pilot fixtures;
  CI separately exercises those integration checks and an isolated tool copy.
- Apply the owner's selected fallback: keep the exporter/tests under
  `scripts/skill-delivery`, procedures under `docs/skill-delivery`, and the
  experimental entrypoint only as `evals/skill-delivery/candidate/SKILL.md.txt`.
  Restore Engineering's existing 0.1.2 metadata; no extra skill is discoverable.

## Unreleased — evidence and recovery safeguards

- Extend reporting, retrospective and Release source guidance to distinguish
  failed retrieval from product state, bind claims to dated candidate evidence,
  reconcile ambiguous operations before retrying, and stop causal analysis where
  evidence stops. Continue independent authorized work while a gate is blocked.
- Add seven fictional input cases with separate evaluator criteria for source
  navigation, partial records, inaccessible providers, completed timed-out
  actions, runtime failures, contradictory diagnostics and completed releases.
- Keep instruction comprehension, automatic startup loading, source adoption
  and public release as separate acceptance claims. No package, tag or consumer
  pin changes.

## Unreleased — scoped production-experience acceptance

- Extend existing Design 0.1.1 source guidance with a brief-relative visual
  target and a bounded acceptance record for actual renders, reviewer scope,
  evidence, deviations and unresolved checks. Preserve intentional minimalism
  and product-specific game rules; technical validity is not artistic approval.
- Add four original local rendered fixtures and an optional interaction/capture
  runner. Keep fixture assertions, independent model judgment and PR review
  separate; the dated audit records actual coverage.
- Retain four fresh independent rendered evaluations, complete answers and
  action evidence at source `7b6bf416173666d20b35def9c1200e0054122356`.
  All four meet their held-out behavior criteria; disclosed keyboard/device
  limits remain, and no publication or universal quality claim follows.
- Extend Release 0.1.1 source guidance to honor an owning project's required
  experience decision without inventing a gate for unrelated work. Existing
  packages, tags, installs and consumer pins remain unchanged.

## Unreleased — engineering retrospective source guidance

- Add a proportional incident template and fictional behavior cases for
  verified causes, evidence limits, private/public boundaries, and action
  verification. This is source guidance only; no plugin, tag, or consumer pin
  changes.

## Unreleased — Engineering 0.1.2 source candidate

- Add an optional Acorn-based JavaScript import graph guard with synthetic
  failures for forbidden edges, cycles, unresolved and nonliteral imports,
  unsupported syntax and unclassified file types. It supplements the existing
  inventory guard; no product, plugin tag or consumer pin changes automatically.
- Record the evaluated dependency-cruiser limitations and require an explicit
  coverage review before product adoption.

## Unreleased — Engineering and Release 0.1.1 candidates

- Add an optional source-ownership inventory guard with synthetic negative cases. This is scoped inventory validation, not dependency-graph enforcement or a merge guarantee.

- Add a reuse-decision reference for comparing contracts before extraction, keeping storage failures visible, and protecting frozen artifacts; add synthetic positive and negative cases. This changes shared guidance only, not product code or consumer pins.

- Require a fresh archive and exact packaged entry/hash readback; add a synthetic case for an old ZIP retaining an extra file despite passing integrity checks.
- Add parallel-work guidance and a project-owned handoff template for isolated writing lanes, explicit dependencies, exact source/artifact identity and renewed review after changes.
- Preserve one production owner through history, deployment and readback; independent preparation does not authorize parallel production mutations or broader access.
- Add synthetic behavioral evaluation cases. Existing tags, installed plugins and consumer pins remain unchanged; no deployment or hosted workflow is introduced.

## Unreleased — Design 0.1.1 candidate

- Reject ambiguous export manifests with duplicate JSON members or non-integer
  versions; add synthetic parser and CLI regressions.
- Add bounded starting, active, pause/overview and recovery-state review guidance; compare released bytes, canonical source and unpublished candidate by exact identity and date. Add fictional cases for a divergent game journey and an already-correct non-game form, without claiming native usability from browser evidence.
- Add operational-status review guidance and a synthetic case for calibrated health claims, unknown states, metric provenance and public/private boundaries.
- Add design-kit handoff guidance for explicit source roots, new output ownership, exact public payload inventories, final-raster QR checks and separate physical/vendor proofs.
- Add a dependency-free, read-only path/inventory/hash checker and synthetic regression cases. No asset generation, QR decoding, publishing or deployment authority is implied.
- This source candidate does not change the released v0.5.0 tag or consumers' pins. CI registration and public release remain separate work.

## 0.5.0 — 2026-10-24

- Add Automation 0.1.0: local Keychain bootstrap, compiled task/profile/code pins, scoped service-account resolution, sanitized fresh-result contracts, and explicit local-only limitations.
- Add synthetic failure tests for missing/malformed/revoked/inaccessible credentials, incorrect identity/scope/field type, changed files, relative interpreter inputs, unsupported tasks, missing evidence and secret-printing children. The compiled launcher has no credential-export operation.
- Update Reporting to 0.1.1 with voluntary actual-use context, edition/build aggregation, QA and owner-test exclusions, and backward-compatible unknown context for earlier records.
- Retain Apache-2.0, existing plugin versions, and product/private data separation. No additional agent role or upstream code was vendored.

## 0.4.0 — 2026-10-24

- Add Reporting 0.1.0: normalized source adapters, private aggregate reports, freshness and missing-evidence handling.
- Add synthetic regression coverage for QA, deduplication, backlog age, and sensitive-text exclusion.
- Document authorized collection, source limitations, recurring review, and aggregate retention.

## 0.3.0 — 2026-10-23

- Add Release 0.1.0 with credential-free static readback tooling and deployment evidence workflow.
- Capture session lessons: reuse signed-in browser, refresh stale history, verify host transformations, and reconcile local artifacts.

## 0.2.0 — 2026-10-23

- Add Design plugin 0.1.0 with product-identity and experience-review skills.
- Add identity/voice brief linkage, synthetic behavior cases, and optional dependency provenance.
- Preserve Editorial plugin 0.1.0 and keep product material outside the public toolkit.

## 0.1.0 — 2026-10-23

- Establish the public artifact catalog and portable editorial plugin package.
- Add medium and audience aware editorial guidance, an optional Codex reviewer agent, and public evaluation cases.

## Engineering source candidate

Engineering 0.1.0 adds the [platform-boundaries skill](plugins/engineering/skills/platform-boundaries/SKILL.md) and a dependency-free, bounded lexical guard with synthetic failure tests. Source candidate only; existing release tags and consumer pins are unchanged. The guard does not certify dependency graphs, device behavior, purchases or store readiness.

## Performance 0.1.0 source candidate

Add an advisory browser measurement helper and comparator with synthetic
behavior tests. Register the Design export suite in CI. This unreleased source
does not change a tag or installed consumer pin.
