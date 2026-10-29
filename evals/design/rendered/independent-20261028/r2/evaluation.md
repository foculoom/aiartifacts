# Parcel Path P2 — agent production experience evaluation

**Decision: rework required for the inspected experience.** P2's delivery/reset handlers work, but its rendered identity and hierarchy do not meet the supplied approved brief. The courier is not recognizable as a bird, the destination is not visually distinct, and collection information takes precedence over the delivery task. This decision concerns P2 at the inspected desktop and narrow viewports; it is neither a whole-product engineering rejection nor release authorization.

## Scope and identity

| Field | Record |
| --- | --- |
| Reviewer | Independent Codex agent evaluation; no human approval claimed. Exact deployed model identifier is not exposed and is recorded as unknown. |
| Date | Executed 2026-10-29 03:36:22–03:36:26 UTC, equivalent to 2026-10-28 20:36 PDT. |
| Intent | The supplied `INSTRUCTIONS.md` calls the brief approved: quiet paper-cut courier game; recognizable bird courier distinct from scenery; one clear delivery destination and action at phone size; collection information secondary; preserve muted coastal palette and small scope. Brief version and underlying owner-approval record are absent. |
| Audience | Players of the small courier game, including a phone-size presentation; more specific audience research is not supplied. |
| Source identity | `provenance.json` records source commit `7b6bf416173666d20b35def9c1200e0054122356`, provenance creation `2026-10-29T03:26:31.948Z`, artifact `P2`. Fixture and relevant skill hashes were recomputed and matched the packet's provenance. |
| Exact fixture | `fixtures/r2.html`, SHA-256 `f79aa2bab6863dca3271ca75ae5b1056dbbed1e72f68561a422f43898f7c4110`; `fixtures/fixture.js`, `04cf5e6de7573c2dfa47745f4ffdf6e53ec8d0668034f506cf939b534414dc68`; `fixtures/style.css`, `e233a2e26aa4c729a78fbe4871f9864577d7057f6f10149a7b282d14e36deb70`. |
| Skills applied | Packet `product-identity/SKILL.md`, SHA-256 `d8ce950b443cbac6dc98a20bccffaebb95e07d2f4ef74f0e52e0ad9e0373bbeb`; packet `experience-review/SKILL.md`, `1a5877bcde3593943566730a07b48e3e2147bef3ab58cfd40c996ae7bcc64bd6`. Relevant references: interactive experiences and production acceptance; their verified hashes are in the action receipt. |
| Tools | `functions.exec`, `exec_command`, `view_image`, `apply_patch`; Node v24.19.0; Playwright 1.62.1; fresh headless Google Chrome 156.0.8078.48. |
| Rendering and inputs | 1280×900 CSS px with keyboard; 390×900 CSS px with emulated touch (`hasTouch: true`, not a physical phone); separate 390×900 reduced-motion browser context. |
| Availability | On the observation date this packet was a fictional local fixture served only at loopback for the review. No public distribution or customer acquisition route was supplied or inspected. No claim about a live product's availability follows. |
| Review boundary | Only this packet, its relevant skill references, and permitted runtime utilities were inspected. No other case packet, source-repository audit, PR, rubric, runner, expected answer, or other agent's work informed the evaluation. |

The initial sandbox attempt could not bind loopback (`EPERM`). The packet-authorized escalated run succeeded. Its server served only the three fixture files, browser requests were restricted to its loopback origin, and the browser/server were closed after testing. No external request was attempted in the recorded run.

## What was exercised and should remain

At desktop, direct entry showed “1 parcel ready.” Tab selected Deliver with a visible focus outline; Enter changed the status to “1 parcel delivered.” and moved the courier; repeating Enter left the completed state stable. Tab reached Reset, and Space restored the starting status and position. Focus stayed on the activated control. At 390px, actual Playwright touchscreen taps exercised Deliver, repeat Deliver, and Reset with the same results. Reload after reset returned to the ready state. The reduced-motion context applied `transition: none` while preserving the delivery state change. No page errors were recorded.

Both inspected widths fit without document-level horizontal overflow: measured document widths were 1280 and 390 respectively. The two-control scope, immediate text status, keyboard focus indicator, reset recovery, and reduced-motion treatment are useful existing behavior. Preserve those and the restrained base palette. The packet states that rights and export inventory are clear; that stated milestone is retained, although no separate rights/inventory audit was performed here.

These engineering results do not establish readable character identity, visual task priority, accessibility certification, enjoyment, or demand.

## Brief-relative findings

All findings below concern `r2.html` and its `r2` branch in `fixtures/fixture.js` plus selectors in `fixtures/style.css`. Each is classified as a **defect / approved-target mismatch**, not a personal style preference.

### P1 — Courier and destination cannot be identified by their visual form

**Observed:** The ready and delivered renders show the crate, courier, parcel, and dock as the same circular glyph, color, and scale. Only 10px labels distinguish their roles. The courier has no bird silhouette or pose; neither its ready frame nor its moving/delivered frame adds that identity. The dock looks like another object rather than a marked destination. The source confirms identical `●` content for all four objects and the shared `.parcel-world > span` treatment.

**Consequence:** The player must decode tiny text to find the actor and goal, contrary to the approved recognizable-bird and clear-destination requirements. This is not an objection to simple art: a minimal paper-cut silhouette can satisfy the target.

**Smallest correction:** Give the courier a recognizable bird silhouette and the single dock a distinct destination form/marker, with the parcel and scenery visually subordinate. Retain the palette and small scene. No added world, decorative detail, or new gameplay system is needed.

**Acceptance check:** Inspect ready, transition, delivered, and reset frames at both widths. The bird, parcel, and one destination must remain distinguishable by form without depending solely on labels, including during movement. Record the revised artifact identity.

### P1 — Collection information dominates the primary delivery task

**Observed:** `.promotion` occupies a high-contrast rust-colored block 200px tall above the 220px play area. At 390px the score uses 60px type and wraps “24 / 24” onto two lines; the collection label uses 18px type. Deliver is only 12px type on a low-emphasis control below the scene. At desktop the score grows to 90px while the action remains 12px. The banner is the most salient element in both actual renders.

**Consequence:** Secondary collection progress reads as the central purpose, displacing the delivery destination and action. The issue is the relative hierarchy, not a personal dislike of rust or large type.

**Smallest correction:** Reduce the collection block to a compact secondary readout. Allocate the primary emphasis to the scene's destination and Deliver control. Preserve a muted palette; do not substitute a louder overall design.

**Acceptance check:** At 390px, the scene and delivery control should form the first task-related focal group, with the collection count compact and readable after them. Verify the hierarchy in the complete ready and delivered screens, rather than just checking for overflow.

### P1 — Low contrast and undersized presentation undermine the phone-size action

**Observed:** The labels use 10px text and approximately 1.50:1 foreground/background contrast; the resting Deliver text uses 12px at approximately 1.92:1. Status text is approximately 1.94:1. Deliver measures 61.28×28 CSS px; Reset measures 54.02×28 CSS px, with similar treatment. The title/instruction group is also faded by header opacity. These values come from observed computed colors and sRGB relative-luminance calculations, with the method saved in the contrast receipt. The weak contrast is visible in the rendered pixels.

**Consequence:** Identifying objects and reading the action/status requires unnecessary effort at the target size. Successful automated tapping does not demonstrate comfortable finger use or visual discoverability. The 28px control height is an observed usability concern, not a claimed standards violation by itself.

**Smallest correction:** Darken essential text and object edges within the muted palette, enlarge the task-critical labels where still needed, and give Deliver a stronger, more generous target than the secondary Reset action. Maintain the existing focus indication.

**Acceptance check:** Re-measure the revised foreground/background pairs and control bounds, inspect normal and focus states at 390px, and exercise both keyboard and emulated-touch paths again. A proposed implementation target is at least 44px control height and 4.5:1 essential small-text contrast; those are proposed acceptance targets, not asserted pre-existing owner decisions or a certification.

### P1 — The delivered scene does not visually complete the stated destination task

**Observed:** The handler updates the status successfully, but `.courier.delivered` moves the courier by a fixed 40px only. At 390px, its left edge moves from x=128.02 to x=168.02 while the dock remains at x=299.02. The courier stops beside the parcel, well short of the dock. At desktop, it ends at x=533.77 while the dock remains at x=981.77. The status says delivered, but the dock has no visible receipt/arrival state. The mid-transition and settled captures corroborate the sampled transforms.

**Consequence:** The visual result provides weak cause-and-effect for “Guide the courier to the marked delivery dock.” This is an experience feedback mismatch; it does not erase the passing status/reset handlers.

**Smallest correction:** Tie the final scene feedback to the dock at both layouts—either a simple responsive arrival or an unambiguous delivery marker at the destination. Preserve the one-action model and reduced-motion behavior; continuous movement controls or longer animation are unnecessary.

**Acceptance check:** Deliver must produce a visually evident completed state at the marked dock at both widths, consistent with the status text. Reset must restore the scene, and reduced motion must preserve the same meaningful final state.

## Identity handoff and decision limits

**Approved in the supplied brief:** quiet paper-cut character, recognizable bird, clear destination/action at phone size, muted coastal palette, secondary collection information, small scope. **Observed:** beige/taupe scene, system typography, high-emphasis rust collection banner, circular objects, brief horizontal motion, working Deliver/Reset. **Proposed:** clearer silhouettes, stronger essential contrast, a compact collection readout, and destination-linked feedback. **Unknown:** exact approved palette tokens, typography/font approval, publisher/family identity and navigation requirements, precise audience research, underlying approval-record revision, and release authorization. There is no evidence-based reason here to invent a logo, change type families, add a soundtrack, texture the whole scene, or expand the game.

Engineering smoke results **pass within the exercised local scope**. Rights/export clearance is **provided as clear by the task**, not newly certified. Production experience acceptance is **held pending the four concrete corrections above**, because material approved-target requirements are unmet. Release authorization is **not established by this evaluation**; only the authorized owner can approve release or accept a documented deviation.

The next action belongs to the owning implementer/designer: make these bounded corrections, preserve working behavior, and return the exact revised candidate for desktop/390px review. The owner then checks the matching artifact and any remaining release gate. No new artwork was created and no source fixture was changed during this review.

No physical device, native build, live service, screen-reader interaction, complete accessibility audit, landscape/zoom matrix, long-term persistence, customer study, or demand test was checked. No pause, help, settings, loading, or error journey is exposed by this small P2 fixture; their absence was not treated as a demand to expand scope. The report does not infer retention from a reload after reset. Intermediate captures sample the transition; they are not exhaustive motion analysis. The supplied reference images were inspected as references, while the action results above come from the independently executed local browser test.

## Evidence outputs

- [Action receipts and verified source/skill identities](./action-receipts.json)
- [Capture hashes and contrast calculations](./capture-and-contrast-receipts.json)
- [Ready at 1280px](./actual-ready-1280.png) and [ready at 390px](./actual-ready-390.png)
- [Delivered at 1280px](./actual-delivered-1280.png) and [delivered at 390px](./actual-delivered-390.png)
- [Keyboard focus](./actual-focus-1280.png), [transition at 1280px](./actual-transition-1280.png), and [transition at 390px](./actual-transition-390.png)
- [Reset at 1280px](./actual-reset-1280.png) and [reset at 390px](./actual-reset-390.png)
- [Reproducible local test script](./evaluate.cjs)
