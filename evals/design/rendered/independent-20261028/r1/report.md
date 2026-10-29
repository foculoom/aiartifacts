# Signal Garden G1 — independent agent evaluation

**Decision: rework required for the brief’s clear-available-actions requirement.** At both inspected widths, controls look enabled and remain keyboard-focusable when their handlers silently do nothing. The game’s restrained visual treatment, readable board, working play loop and recovery paths should remain. This is a bounded agent evaluation, not whole-product approval or release authorization.

## Identity, intent and evidence

- **Artifact:** local `fixtures/r1.html`, rendered artifact marker **G1**, title **Signal Garden**. The supplied `provenance.json` records source commit `7b6bf416173666d20b35def9c1200e0054122356` and packet creation `2026-10-29T03:26:31.948Z`. That source identity is supplied provenance; no repository or public deployment was consulted.
- **Fixture bytes, independently hashed:** `r1.html` SHA-256 `1eec1080b0f24ea98f5e77f9a57672306935b9c1bf8fa531d5991f2378d11182`; `fixture.js` `04cf5e6de7573c2dfa47745f4ffdf6e53ec8d0668034f506cf939b534414dc68`; `style.css` `e233a2e26aa4c729a78fbe4871f9864577d7057f6f10149a7b282d14e36deb70`. All match the supplied provenance.
- **Brief:** packet `INSTRUCTIONS.md`: clear available actions in starting, active, overview and recovery states; desktop and 390px review; no game redesign. Separate brief revision, detailed audience research and approved identity record are **unknown/not supplied**. The on-screen instruction defines a small planning game in which players water the next bed and undo an action.
- **Skill:** supplied `skills/experience-review/SKILL.md`, with `interactive-experiences.md` and `production-acceptance.md`. Named skill version is unknown; its provenance hash is `1a5877bcde3593943566730a07b48e3e2147bef3ab58cfd40c996ae7bcc64bd6`.
- **Reviewer/tools:** Codex agent; exact model identifier **unknown** (environment describes a GPT-6-based agent). Playwright **1.62.1**, Node **v24.19.0**, headless Google Chrome **156.0.8078.48**, fresh isolated browser contexts. Pixels inspected with the image-view tool. No shared CUA/provider browser was used.
- **Observation:** `2026-10-29T03:31:28.414Z`–`03:31:32.766Z`, equivalent to October 28, 2026 in America/Los_Angeles. Temporary loopback URL `http://127.0.0.1:59006/r1.html`; server stopped after testing. Browser-context requests were restricted to that local origin. The initial sandbox attempt was blocked at loopback binding; the authorized escalated run completed.
- **Availability:** this was a local synthetic fixture on the observation date. Public availability, released bytes and customer acquisition are unknown; this packet establishes none of them.

The new screenshots and `action-receipts.json` record my own browser exercise, distinct from the supplied reference captures. I inspected all eight new starting/active/overview/recovery renders at **1280×900** and **390×900**, plus the 390px keyboard-focus render. I also inspected two supplied captures (`r1-start-390.png` and `r1-overview-1280.png`) as reference evidence only.

## Findings

### F1 — P1 defect: visible availability does not match the current state

**Component/location:** G1’s action row, `#water`, `#overview`, `#undo`, `#restart`; verified source `fixtures/fixture.js:10–17`, especially render function line 12 and handler guards at lines 14–17.

Every sampled button had `disabled=false` and no `aria-disabled`. Starting Tab order includes Start, Water, Overview, Undo and Restart. The renders show the same enabled button treatment; there is no unavailable label or explanation for the no-op actions.

| State and action actually exercised | Observed result | Consequence |
| --- | --- | --- |
| Starting: click Water, Overview, Undo or Restart, at both widths | Status remains “Ready to start · 0 beds watered”; board unchanged | Four apparent choices cannot do their advertised work, obscuring the only entry action, Start. |
| Overview after watering twice: click Water at both widths, keyboard Space at both widths, and emulated touch at 390px | Remains paused with two watered beds | A prominent play action appears usable while paused; the player gets no response explaining the restriction. |
| Active immediately after Start: click Undo at both widths | Remains playing with zero watered beds | Undo offers no indication that no history exists. |
| Active after all three beds are watered: click Water again at both widths | Remains playing with three watered beds | The interface still invites a next bed when none is available. |

**Evidence:** `start-1280.png`, `start-390.png`, `overview-1280.png`, `overview-390.png`; the action receipt entries named “Starting: click …”, “Overview: click Water”, “Overview: Shift+Tab to Water, Space”, “Active with empty history: click Undo”, and “Active: water toward/at cap, click 3”. The source explains the observed mismatch: `show()` changes the status, Start visibility and Overview label, but never updates availability to reflect handler guards or history.

**Smallest correction:** make control availability track the existing rules. Before Start, hide or visibly and semantically disable the four unavailable controls. Enable Water only in active mode with a remaining bed; communicate the paused or completed condition in the existing status if useful. Enable Undo when history exists, including during overview. Keep Resume available in overview and preserve the working Restart behavior. Do not blanket-disable the overview action row.

**Acceptance check:** at 1280×900 and 390×900, repeat the same pointer and keyboard journey. The rendered appearance and semantic state must identify every unavailable action; no enabled-looking control should silently promise an unavailable operation. Check the initial state, empty history, overview, three-bed cap, and return from Undo/Restart. After pausing at two beds, Water must be unavailable while Undo still changes two to one and Resume retains that one-bed state. Restart and Undo of Restart must retain their current working behavior.

### F2 — P2 hypothesis / optional refinement: starting removes the focused control

**Component/location:** `#start`; `fixtures/fixture.js:12–13`.

At both widths, Tab to Start then Enter starts play and hides Start, leaving `document.activeElement` at `BODY` with no focused button. The next Tab correctly reaches Water and shows its outline, so this is **not a keyboard trap**. The loss of the focus cue is observed; whether the extra Tab materially disrupts players is an untested usability hypothesis.

**Correction/acceptance check:** when Start is activated by keyboard, move focus to the first available play action, Water, or another intentionally chosen visible destination. Verify that the focus indicator is visible immediately and Enter/Space performs the expected next action. This refinement is separate from the P1 availability gate.

## What works and should remain

- **Readable, restrained board:** numbered beds and the words Seed/Watered distinguish state independently of the fill-color and dashed/solid-border change. The title, short instructions, status and controls form a clear sequence. No richer art treatment is required by the supplied brief.
- **Responsive layout:** the actual 390px renders retain all three readable bed labels and wrap the controls into two rows without clipping. Overview status wraps onto two readable lines. Recorded document width equals the viewport width in every sampled state; all visible button rectangles are 55 CSS pixels high. These are browser observations, not proof of physical-device usability.
- **Active feedback:** Water changes zero to one, then two, then three watered beds with matching board text. Focus stays on Water during repeated keyboard activation. Enter and Space both worked in the exercised keyboard sequence.
- **Overview and recovery:** Overview becomes Resume and explicitly says planning is paused. Undo works while paused, reducing two beds to one without resuming. Restart resets to zero while retaining overview; Undo restores the previous count. Resume returns to play with the recovered count. Active Undo, Restart and Undo of Restart also work, retaining focus on the activated recovery control. Preserve these behaviors.
- **Keyboard and touch affordances:** Tab/Shift+Tab reach the controls; the visible keyboard outline was inspected at 390px. A separate emulated-touch context successfully exercised Start, Water, Overview, Undo, Resume, Restart and Undo of Restart. The persistent short instructions remain visible in all four states.

## Scope, acceptance and next action

**Engineering observations:** the exercised transitions produced the recorded states and no page errors were captured. This was targeted browser exercise, not a repository test-suite, security or performance acceptance. Reload was also exercised: it returns to the starting state with zero watered beds. No persistence requirement was provided, so that result is recorded without labeling it a defect.

**Experience decision:** **rework required** for action availability in this exact G1 artifact. The visual layout and successful recovery behavior are retained findings; the P1 does not justify redesigning the game. Recheck affected states against the corrected artifact and record its new identity.

**Release decision:** no publication authorization or human approval is supplied or granted by this review. Public availability remains unknown. The product’s authorized owner retains release and deviation decisions.

**Next action:** implementation owner (not named in the packet) should make the minimal state-derived availability correction and rerun F1’s acceptance checks; optionally improve the Start focus transition. The release/experience owner can then assess the matching revised artifact. No need to change game rules, add real-time behavior, or expand the world.

**Limits:** no physical phone/tablet, native browser integration, target-user readability study, screen reader, accessibility certification, measured color-contrast audit, zoom/text-scaling, cross-browser matrix, settings/help dialogs, live service, public deployment, purchase, customer receipt or demand test. No detailed visual identity approval was supplied. Source-only observations were not used to claim interaction success. The provided three-bed overview is not a dense-board usability test. New artifact changes invalidate only the affected conclusions and require matching new evidence.

## Saved evidence

- `action-receipts.json`: timestamped states, focus, button semantics and bounds for 87 snapshots across mouse, keyboard and emulated-touch runs.
- `check.cjs`: the local-only capture/exercise script.
- `start-{1280,390}.png`, `active-{1280,390}.png`, `overview-{1280,390}.png`, `recovery-{1280,390}.png`: primary rendered evidence inspected for this decision.
- `keyboard-focus-{1280,390}.png`, `overview-undo-{1280,390}.png`, `cap-{1280,390}.png`: additional captures. Only the 390px keyboard-focus image among these additional captures was visually inspected; action receipts independently record all corresponding states.
