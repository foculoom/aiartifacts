---
name: roblox-3d-play-pass
description: Run an evidence-first play pass on a 3D Roblox experience across touch, desktop, gamepad and low-end devices, covering the first 60 seconds, camera comfort, readability, controls, frame time, lag, young-player safety, monetization and fun, with High/Medium/Low findings. Use for playtests, release gates or build comparisons of Roblox or similar kid-audience 3D games; not for writing game code, choosing a content rating, or legal advice.
---

# Roblox 3D play pass

> This is a generic, public method. It contains no product-specific data. Keep real playtest records, screenshots, device lists and account details in the owning project. The Roblox policy and tool details summarized here change often; recheck the cited pages before relying on them. Sources were last checked on 2026-11-27 (America/Los_Angeles).

A play pass is evidence-first. Every finding names the build, the device and input, what was done, what was seen, and whether it was **measured** (a number from a tool), **observed** (seen by a person on a device), or **inferred** (from source, docs or emulation only). Never present an inferred result as observed.

Sources are cited as [S#] and listed at the end. Thresholds marked **(rule of thumb)** are the tester's working limits, not published requirements.

## 0. What a tester can and cannot do

Roblox experiences run only in the Roblox client (phone, tablet, desktop, console, VR) or in Roblox Studio. Studio runs on Windows and macOS only [S1]. A plain browser or a Linux machine cannot play the experience. Plan coverage honestly:

| Coverage | How | Can measure | Cannot prove |
| --- | --- | --- | --- |
| Static (any machine) | Read the source (for example a Rojo/Git project), the experience page and public APIs | Text filtering call sites, PolicyService gates, purchase prompt copy, camera scripts (FieldOfView, shake, bob), maturity label and pass prices | How it looks, feels or performs |
| Headless cloud run | Open Cloud Luau Execution runs scripts against a specific place version [S2] | Scripted unit and integration checks, data and economy invariants | Rendering, input, comfort |
| Studio emulation (Windows/Mac) | Device Simulator (phone tiers, tablet, desktop, console, headset), Controller Emulator, Network Simulator, Player Emulator, Server & Clients multi-client test [S3, S4, S5, S6] | Layout at real physical size, touch-gesture stand-ins, gamepad focus paths, lag behavior, policy variants by region, MicroProfiler frame times on the dev machine | Real thumb reach, real device heat and frame rate, real motion sickness |
| Real devices | Published or private test place played in the Roblox client on owned test devices | Everything above, plus device MicroProfiler (mobile via the LAN web UI) and Developer Console (F9) [S7, S8] | Population-level performance (use the Performance dashboard after launch [S9]) |

A tester limited to a Linux box can do the static and headless-cloud rows, prepare the checklist and report, and must mark every comfort, controls, readability and performance item as **not run** until someone runs Studio on Windows/Mac or plays on a device. Do not sign in to accounts, buy Robux or change experience settings without the owner's explicit authorization. Use test accounts for each age band, never real children's accounts.

## 1. Set up

1. Record: experience and place ID, place version or commit, the test date and time zone, tester, and the skill revision.
2. Record the declared content maturity rating and descriptors, the target audience (Roblox Kids 5–8, Roblox Select 9–15, Roblox 16+) and the PolicyService features the game uses [S10, S11].
3. Choose the matrix (below). One person on one device is a data point, not a population.
4. Prepare a comfort log: tester, prior motion-sickness susceptibility (yes/no), screen size, viewing distance.

### Test matrix

Run every row the experience claims to support. Phone touch is mandatory: Roblox says most sessions are on mobile [S12].

| ID | Device / input | Studio stand-in | Real-device suggestion | Orientation |
| --- | --- | --- | --- | --- |
| P-S | Small phone, touch | Device Simulator, Phone > Entry level, Physical size scaling [S3] | A small, older Android phone | Landscape (Roblox default LandscapeSensor) [S12] plus portrait if supported |
| P-L | Large phone, touch | Phone > Flagship | A recent large iPhone or Android | Same |
| T | Tablet, touch | Phone category tablet device | Any iPad or Android tablet | Landscape and portrait if Sensor |
| D | Desktop keyboard and mouse | Desktop device, 1280x720 and 1920x1080 | Windows or Mac laptop | n/a |
| G | Gamepad | Controller Emulator or a real Xbox/PlayStation pad [S4] | Pad on PC, or a console | n/a |
| LE | Low-end performance | Entry-level phone in Simulator (layout only; it does not throttle the CPU) | The weakest phone you support, at least 10 minutes so heat builds | Landscape |
| VR | Headset (only if VR is enabled) | Headset device in Device Simulator [S5] | Quest | n/a |
| NET | Lag profile | Network Simulator presets: Home Wi-Fi, Standard Mobile (4G/LTE), Bad Connection (3G) [S6] | Phone on mobile data | n/a |

## 2. The first-60-second test

Use a fresh test account for each age band, with no saved data. Start a timer when the loading screen ends. Do not coach the tester. Record video if allowed.

| Second | Pass if | Fail looks like |
| --- | --- | --- |
| 0–10 | The player knows where they are and what they are (who they are, what this place is) without reading a paragraph | Wall of text, an unexplained menu, a purchase prompt or a shop popup |
| 10–30 | They have performed the core verb at least once (plant, run, hatch, take an order, light a lantern) with a visible, audible response | Still in menus, or waiting with nothing to do |
| 30–60 | They have a reward and a next goal they could state in one sentence | Lost, idle, or told to buy something to continue |

Also check: does it work with chat off? Roblox Kids accounts (5–8) have chat off by default and users who have not completed an age check cannot chat [S13]. Does it work with the sound off? Does it work in the tester's language if localized?

Score: Pass (all three windows), Partial (one window missed), Fail (two or more missed, or any purchase prompt before the first reward). A Fail is Medium; a purchase prompt before the first reward for an under-13 audience is High.

## 3. Camera comfort and motion sickness

Background: motion sickness is common even on ordinary screens. In one lab study 42% to 56% of participants became sick while playing off-the-shelf console games for up to 50 minutes [S14]. The cause is a mismatch between seen and felt motion, made worse by camera movement the player did not initiate [S15, S16]. Desktop FOV results are mixed, so do not rely on FOV alone [S17].

### Checks

| Check | How | Pass / fail |
| --- | --- | --- |
| Field of view | Read Camera.FieldOfView in source and watch it in play. Roblox's FOV is vertical, defaults to 70 and is clamped to 1–120; Roblox warns that very low or very high values disorient [S18] | Pass: stays near the default; any gameplay FOV change (sprint, zoom) is brief, eased and ideally has an option. Fail (Medium): sustained FOV above 90 or below 50 vertical **(rule of thumb)**, or FOV pulsing. For reference, 70 vertical is about 102 degrees horizontal at 16:9 (computed). GAG suggests about 60 for TV and 90 for monitors as defaults [S19], but it does not state which axis |
| Head bob, camera shake, sway, motion blur, chromatic effects | Play 5 minutes of the core loop and 2 minutes of the most intense moment | Pass: none, or each can be turned off or reduced in a game setting [S15, S16]. Fail (Medium): any of them without an off switch. Fail (High) if they are always on and a tester has to stop |
| Camera moves without input (auto-rotate, auto-center, cutscene snaps, forced look-at) | Watch for the camera moving when sticks, mouse and touch are idle | Pass: none outside short, signposted cutscenes, or there is an option to disable it [S15]. Fail (Medium) otherwise |
| Acceleration | Starting, stopping, falling, launch pads, vehicles | Pass: no repeated sharp camera accelerations; the camera does not lag far behind and then snap. Fail (Medium) **(rule of thumb)** |
| Third-person collision and occlusion | Walk against walls, into corners and under low ceilings; check DevCameraOcclusionMode [S20] | Pass: the character never disappears for more than about 1 second **(rule of thumb)**, and the camera never clips inside geometry or pops repeatedly. Fail (Medium) |
| Reduced Motion setting | Turn on Roblox Settings > Reduce Motion (GuiService.ReducedMotionEnabled) [S21] | Pass: UI tweens and non-essential camera effects are cut or reduced. Fail (Low), or Medium if shake persists |
| Flashing | Scan effects, lightning, explosions, UI flashes | Fail (High): more than 3 flashes in any second covering 25% or more of the screen, or any flashing sequence longer than 5 seconds [S22] |
| VR (if enabled) | Use Roblox comfort settings (Vignette, Stepped Rotation, 3rd Person Fixed Camera) [S5] | Pass: the game works with all comfort settings on; frame rate is constant at 72 fps or more on Quest [S5]. Snap turns of about 30 degrees are a GAG example [S23]. Fail (High): forced smooth rotation or camera motion the player did not cause |

### Comfort measure

Ask each tester for a Fast Motion Sickness Scale (FMS) rating from 0 (no sickness at all) to 20 (frank sickness) once a minute during a 15-minute session. FMS is a validated, fast measure that correlates with the Simulator Sickness Questionnaire [S24]. **Rule of thumb:** a peak of 5 or more from any tester is Medium; a tester stopping because of discomfort is High. Ask about lingering symptoms 10 minutes after.

## 4. Readability

Check on P-S at Physical size scaling and on a real small phone. Pixel size alone is misleading on phones [S3].

| Check | Pass / fail |
| --- | --- |
| Text size | Pass: body text reads comfortably at arm's length on P-S. Apple suggests 17 pt default and 11 pt minimum text on iOS [S25]; GAG cites 28 px at 1080p as a TV minimum, not a target [S26]. Fail (Medium): essential text (goals, prices, prompts) below about 11 pt on a phone **(rule-of-thumb mapping of [S25])** |
| Player text size | Set Roblox Text Size to Largest (GuiService.PreferredTextSize). TextScaled text does not respond to this setting, and UITextSizeConstraint caps it [S21]. Pass: essential text grows and nothing is clipped. Fail (Low/Medium) |
| Contrast | Pass: text and essential icons are at least 4.5:1 against their background [S27, S25], measured on screenshots in bright and dark scenes. Fail (Medium) for essential text |
| Background transparency | Set Roblox Background Transparency to opaque (GuiService.PreferredTransparency) [S21]. Pass: panels become more opaque |
| Color and sound non-reliance | View in grayscale and with sound off. Pass: rarity, team, danger and objective cues carry a shape, label or icon as well as color, and a visual as well as sound [S21]. Fail (Medium) if a core cue is color-only or sound-only |
| Icon clarity | Show each HUD icon alone to a tester from the target age; ask what it does. Pass: at least 4 of 5 testers name it, or it has a label **(rule of thumb)** |
| Safe areas | Pass: nothing important sits under the notch, the Roblox top bar or the home indicator [S28] |
| Localization | Use Player Emulator Pseudolocalize to find untranslated text and overflow [S29] |

## 5. Controls per input type

### Touch (P-S, P-L, T)

- **Button size:** 44x44 pt is Apple's default and 28x28 pt its minimum [S25]; Android asks for at least 48x48 dp [S30]. Fail (Medium) if a core action button is below about 44 pt or 48 dp on P-S.
- **Thumb reach:** core actions sit in the lower-right arc reachable by the right thumb while the left thumb is on the movement stick. Rare actions can go higher **(rule of thumb)**.
- **Jump/camera conflict:** dragging the camera from a point near the jump button must not jump; tapping jump while the camera is dragging must work; no action button sits on top of the thumbstick area. Test with two thumbs at once.
- **Gestures:** pinch zoom and two-finger pan if used (Device Simulator maps these to Alt+drag and Alt+Shift+drag) [S3].
- **Orientation:** rotate mid-session; UI must not break [S12].
- **Hold and mash:** no essential action that requires a long hold or rapid mashing without an alternative [S31].

### Keyboard and mouse (D)

- Default Roblox bindings work and reserved keys (Esc, F9, F11, F12, PrintScreen) are not taken over [S32].
- Every action has a key, and the HUD shows key hints when keyboard is the preferred input [S28].
- Mouse lock or shift-lock does not trap the cursor in menus.

### Gamepad (G)

- Every action, including every menu, shop and dialog, works with a pad alone [S33].
- UI navigation: a selection highlight is visible on every screen; GuiService.SelectedObject lands on a sensible default when a menu opens; the D-pad and stick reach every control; B backs out [S34, S35].
- Conventions: A accepts or jumps, B cancels, left stick moves, right stick moves the camera [S35].
- Switching input mid-session (touch to pad, pad to mouse) swaps the hints and on-screen buttons (UserInputService.PreferredInput) [S32].
- Camera sensitivity respects the player's Roblox gamepad camera sensitivity setting [S36].

## 6. Frame rate and memory

Record numbers, not impressions.

| What | Tool | Record | Target |
| --- | --- | --- | --- |
| Frame time | MicroProfiler: Ctrl+F6 (Cmd+F6) on desktop and Studio; on mobile, turn it on in Settings and open the LAN web UI [S7] | Median and worst frame time over a 2-minute core-loop capture and a 1-minute busiest scene; count frames over budget; note orange (jobs), blue (render) or red (GPU) bars | 16.67 ms per frame is 60 fps [S7]. Consistency matters: one 410 ms frame is a visible stutter even at 60 fps [S7]. **Rule of thumb:** P-L and D hold 60 fps; LE holds 30 fps or more with no frame over 100 ms in normal play |
| Client memory | Developer Console (F9, or /console in chat) > Memory and Luau heap [S8] | Memory at start, after 10 minutes and after 30 minutes; any steady climb | No steady climb (a leak). The Performance dashboard tracks memory use as a percentage of device memory and out-of-memory exits after launch [S9] |
| Script cost | Developer Console > Script Profiler [S8] | Top 3 scripts by CPU time | Client CPU time must be under 16 ms per frame for 60 fps [S9] |
| Server health | Developer Console server view (owner or edit access) and the Performance dashboard [S9] | Server frame rate (capped at 60) and server memory | Server stays near 60; memory below 50% of server memory, or below 3 GB as Roblox's rough guide [S9] |
| Heat and battery | Real LE device, 20 minutes | Frame time at minute 1 vs minute 20, device temperature by touch, battery drop | **Rule of thumb:** no more than 25% frame-time degradation |
| Loading | Stopwatch | Time from join to first control, on Wi-Fi and 4G | **Rule of thumb:** under 15 s on P-L Wi-Fi |

After launch, compare each place version on the Performance dashboard (frame rate, crash rate, out-of-memory exits by platform). The charts need at least 100 daily active users [S9].

## 7. Network and lag

Use Network Simulator presets in a Server & Clients test with at least 2 clients [S6, S5]:

| Preset | Inbound latency / jitter / loss | Outbound latency / jitter / loss |
| --- | --- | --- |
| Home Wi-Fi | 30 ms / 12 ms / 0.20% | 30 ms / 15 ms / 0.30% |
| Standard Mobile (4G/LTE) | 45 ms / 20 ms / 0.40% | 55 ms / 30 ms / 0.50% |
| Bad Connection (3G) | 150 ms / 70 ms / 0.50% | 180 ms / 90 ms / 0.50% |

These are Roblox's preset values [S6]. Check under each preset:

- Every server-confirmed action (buy, plant, hatch, trade, save) shows immediate local feedback and a pending state, never a dead button.
- There are no double purchases or double rewards when tapped twice under lag.
- Rubber-banding of the character or camera does not cause discomfort (re-run the comfort log on 3G).
- Join and leave mid-round, and leave mid-purchase or mid-trade: no item lost or duplicated.
- Rejoin restores saved progress, and DataStore failures produce a friendly message and retry, not lost progress.

## 8. Young-player safety

Assume players as young as 5. Many checks are policy, so cite the Roblox page. Record each check as pass, fail or not applicable.

### Audience and label fit

- **Maturity label:** the content matches the declared rating. Minimal and Mild are eligible for Roblox Kids (5–8) and Select (9–15); Moderate is eligible for Select and 16+ [S10]. "Scary" elements (non-realistic monsters, mild tension, ominous music) differ from "horrifying" ones (jumpscares, sustained tension, psychological horror, eerie audio), and frequent scary or horrifying elements push the rating up [S10]. A mismatch is High: inaccurate ratings are moderated [S10].
- **Kids and Select eligibility:** games for under-16s go through additional review; social hangouts, free-form drawing and sensitive-issue themes are excluded [S13, S10]. Free-form user creation (freehand drawing, painting, writing, pixel canvases) is 16+ only, while building from moderated 3D assets is fine [S10]. Games that let players view content captured from other games are 13+ [S10]. Extended generative-AI interaction (cross-session memory, or open-ended AI chat as the main purpose) is 18+ [S10].
- **Experience page:** the title, thumbnail and description suit all ages [S37]. Social media links are shown only to age-checked users 16 or older [S13].
- **Publishing gates** (owner tasks, not tester tasks): ID verification, two-step verification, a fee or subscription, and an evaluation that needs 100 unique plays from highly engaged players in the last 60 days [S11, S38].

### Chat and user-generated text

- Chat uses TextChatService. Conversations held through other text features trigger temporary text limits [S39].
- Every displayed text the game does not fully control (pet names, signs, plot names, nicknames, text from a web server, randomly generated words) passes TextService:FilterStringAsync, with GetNonChatStringForBroadcastAsync for everyone or GetNonChatStringForUserAsync for one user [S39]. Text stored in a DataStore is filtered again when shown [S39]. Unfiltered user text is High; Roblox can remove the game [S39].
- Custom chat features check TextChatService:CanUserChatAsync and CanUsersChatAsync [S40]. Parental controls apply only to Roblox's experience chat and direct chat, not to chat features a creator adds [S41], so the game must enforce them itself.
- Test with a chat-off account: the game stays fully playable, and social features use preset emotes, pings or quick messages.

### Social features

- Friend, party and trade flows do not let strangers follow, message or trade with a young player beyond what Roblox allows.
- Trading: a confirmation screen shows both sides, there is a cooldown or a learn-first gate, and there is trade history and a report button. Paid items can be traded only when PolicyService IsPaidItemTradingAllowed is true [S11, S42].
- Private spaces: there are no enclosed private rooms in a social game. A social hangout with private spaces is 18+ age-verified only [S10].
- Sharing: in-game media sharing is gated by IsContentSharingAllowed and is 16+ [S10, S11].

### Monetization pressure and dark patterns

Roblox's rules [S43]:

- A discount must be genuine and must not last only a very short time.
- No false "almost out of stock" or "limited time" claims.
- No countdowns that are inaccurate or reset for the same item.
- Players must never be misled, confused or pressured.
- With minors, avoid urgent copy. Roblox's own examples replace "GET IT NOW", "LAST CHANCE, ACT NOW" and "BUY BEFORE IT'S GONE!" with "View Item", "See Price" and "Open Shop".

Since 4 May 2026, rewarded ad formats are not permitted for under-13 users [S44]. Research on Roblox found that developers knowingly use predatory designs: UI manipulation and psychological tactics that reinforce each other [S45].

| Check | Pass | Fail |
| --- | --- | --- |
| Purchase prompts | Appear only after the player chooses a shop or item, and show a clear price and a cancel option of equal size | Prompt on join, on death, mid-task, or repeated after cancel (Medium; High for under-13) |
| Copy | Neutral (View Item, See Price) | Urgency, guilt or shame copy (Medium) |
| Timers and stock | Real, stated and the same for everyone | Fake or resetting timers or scarcity (High: breaks Roblox rules [S43]) |
| Pay-to-skip and frustration | Waiting is short and optional to skip | Difficulty or waiting tuned so paying is the only reasonable path (Medium) |
| Currency obfuscation | Prices in Robux are shown alongside any premium currency | Multiple layered currencies hiding real cost (Medium) |
| Ads | No rewarded ads for under-13 [S44] | Rewarded ads shown to under-13 test account (High) |
| Spend limits | Purchases fail gracefully when a parent spend limit blocks them [S13] | Error, lost item or retry loop (Medium) |

### Paid random items

Anything bought with Robux, or with currency bought with Robux, that gives a random outcome counts. That includes eggs, spins, crates, random-duration potions, luck boosts and pity systems [S42]. Tester's reading, not Roblox's wording: a paid restock that rerolls random shop stock probably counts too, so treat it as a paid random item unless the owner confirms otherwise.

- All outcomes and their numerical odds are shown before purchase, as percentages that sum to 100%. Pop-up details need a descriptive word, not just an (i) icon [S42].
- Odds-changing items (luck) state their effect numerically, and the displayed odds update while active [S42].
- No outcome loses the player's payment [S46].
- PolicyService ArePaidRandomItemsRestricted is honored. Test with Player Emulator regions (for example UK under 18). Restricted players get an earnable path, a fixed disclosed order, or direct purchase [S42, S29].
- **Tester recommendation:** for under-13 audiences, prefer no paid random items at all. Any missing odds or a missing PolicyService gate is High.

### Data

- No in-game form asks for real names, ages, schools, addresses, phone numbers, photos or social handles. Filtering exists partly to remove personal information like phone numbers [S39].
- Analytics and DataStores keep only what gameplay needs. Nothing personal goes to external HTTP endpoints.
- Photo-to-Avatar, camera or voice features check the PolicyService flags that apply [S11].

## 9. Fun and stickiness rubric

Score each item 0 (absent), 1 (weak) or 2 (strong), with one sentence of evidence. It is derived from public analyses of top kids' experiences [S47]–[S53]. A total under 10 of 20 is a design concern, not a bug: report it, but do not block on it.

| # | Item | Looks like (public-source example) |
| --- | --- | --- |
| 1 | Core verb in 30 seconds | A starter seed or starter egg in hand at once |
| 2 | Short, repeatable loop (1–5 minutes) | Survive one disaster round; fill one order |
| 3 | Visible progress that persists | A house, a garden or a pet that grows, even while offline |
| 4 | A reason to come back tomorrow | A daily reward or a real restock or event schedule, without fake urgency |
| 5 | Play together without chat | Interdependent jobs; a bonus for friends in the server; shared spectacle |
| 6 | Self-expression for free | Outfits, homes and decoration available without paying |
| 7 | Collection with a twist | Combine 4 of a pet into a rarer one; mutations |
| 8 | Stories worth retelling or streaming | Emergent roleplay; "the tornado took my house" |
| 9 | Live cadence and anticipation | Teased updates; a regular event rhythm |
| 10 | Trust and fairness | A trade-safety quiz; fair odds; no losing purchases |

## 10. Severity

Only High and Medium block. Severity is a playtest recommendation; the owner decides what ships.

- **High (blocks):** a crash, softlock or progress loss; a core loop that cannot be finished on a supported input; a Roblox policy breach (unfiltered user text, missing odds or PolicyService gate, fake timers, rewarded ads for under-13, content above the declared rating, banned features in a Kids/Select game); a flashing breach [S22]; a tester stopping because of motion sickness; a purchase prompt before the first reward for under-13s.
- **Medium (blocks):** a failed first-60-second test; camera effects without an off switch; FMS peak of 5 or more; essential text or buttons below the size floors or contrast below 4.5:1; jump/camera conflicts; gamepad dead ends; frame-time targets missed on P-L, D or LE; a memory climb; duplicated or lost actions under lag; pressure copy or pay-to-skip tuning.
- **Low (does not block):** polish, nice-to-have settings, rubric scores, wording, small layout issues on one device.

When in doubt between two levels, pick the lower one and explain what evidence would raise it.

## 11. Report

Copy the [report template](assets/report-template.md). Put the verdict line first: `PLAY_PASS <sha7>: PASS|FAIL H/M/L = x/y/z`. A PASS covers only the devices and inputs listed as run; it is a playtest recommendation, not permission to merge or ship. The owner decides.

## Sources and cases

Citations [S1]–[S53] are listed in [sources](references/sources.md). Synthetic behavior cases are in [evals/design/roblox-play-pass](../../../../evals/design/roblox-play-pass/README.md).
