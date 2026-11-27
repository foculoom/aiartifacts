# Moderation, community standards and young players

Checked 2026-11-27 (America/Los_Angeles). Source numbers refer to [sources.md](sources.md). Audio-specific moderation notes are in [audio.md](audio.md) §2.3.

## How asset moderation works

- Every imported asset must pass a moderation check before users can see or interact with it in a published game [R11]. Until audio passes, only the uploader can hear it [R7]. Open Cloud reports `Reviewing`, `Rejected` or `Approved` [R14].
- Assets are judged on their own. "Realistic or excessive depictions of violence, blood, crude humor, or romantic themes may be moderated regardless of your game's content ratings" [M3]. Public-facing material for age-restricted games (description, thumbnails, videos) must suit general audiences [M4].
- Roblox "may also proactively delete or archive assets if we suspect that the content may be infringing on someone's intellectual property rights" [M1].
- Audio songs also go through copyright checks before they can appear on a game's details page [R7].

## What gets rejected (Community Standards [M1], applied to assets)

| Area | Examples that fail |
| --- | --- |
| Profanity | Swearing in any language, text, images or uploaded audio, including misspellings to evade detection and profane lyrics |
| Sexual and romantic | Nudity or partial nudity; sexually suggestive assets, clothes or settings; romantic or flirtatious content |
| Violence and gore | Realistic or real-world extreme gore, graphic violence or death; depicting abuse or torture of humans, animals or fictional creatures |
| Real-world sensitive events | Recreating mass violence, specific real disasters, sensational crimes, rights violations |
| Extremism, hate, harassment | Extremist iconography; discrimination; threats |
| Political figures and entities | Current or recent officials, candidates, parties and their material |
| Illegal and regulated goods | Drugs, alcohol, tobacco, vaping and paraphernalia; intoxication |
| Self-harm | Depicting or promoting suicide, self-injury or eating disorders |
| Personal information | Emails, addresses, phone numbers, handles not linked to Roblox, credentials |
| Off-platform direction | URLs or calls to visit external sites or services (only the Social Links feature is allowed) |
| Advertising | Paid promotion or calls to action for off-platform products without meeting the Advertising Standards |
| Misleading and spam | Content "confusingly similar" to other creators' to drive discovery; "repeatedly uploading content identical or nearly identical to existing content" |
| Intellectual property | Third-party copyrighted or trademarked material (logos, characters, songs, artist likeness) without permission |

AI-specific checks before upload: garbled pseudo-text, logo-like marks, accidental faces or bodies in textures, artist-style music that could match a real recording, and voice clones of real people.

## Appeals and account risk

- Moderation notices say whether to appeal through **Violations & Appeals** (roblox.com/report-appeals) or the **Support form**; content appeals need the username, a short reason, the asset id and a link [M2].
- Appeal within **30 days** of the action (EU users: **6 months** under the Digital Services Act). A decision that has been reviewed can't be reviewed again; only the account owner can appeal [M2].
- Game-level violations are on the Creator Dashboard under Safety → Issues & appeals [M3].
- Actions Roblox may take: warnings; blocking, removing or deleting UGC; restricting access; suspending or terminating the account; contacting law enforcement [L1 §4.2]. A **group owner** is responsible for all UGC associated with the group and can lose ownership, have the group restricted, or have their account suspended [L1 §5.2.2–5.2.3]. Inaccurate content ratings also put the game and account at risk [M3].
- So every rejected upload is a strike risk for the company group. Fix and re-check before any retry, and never upload near-duplicates to test the filter.

## Young-player rules (from roblox-3d-play-pass)

The **roblox-3d-play-pass** skill (section 8, Young-player safety, and section 3, Camera comfort) is the authority for the play pass. The parts that apply to individual assets:

| Rule from roblox-3d-play-pass | What it means for an asset |
| --- | --- |
| Assume players as young as 5. Content must match the declared maturity label; Minimal and Mild are eligible for Roblox Kids (5–8) and Select (9–15). A mismatch is High | Each mesh, texture, sound and video must sit at or below the declared label |
| "Scary" (non-realistic monsters, mild tension, ominous music) differs from "horrifying" (jumpscares, sustained tension, psychological horror, eerie audio); frequent scary elements push the rating up | Threat sounds swell in rather than sting; no jumpscare audio or visuals; creature art stays non-realistic |
| Flashing: more than 3 flashes in any second over 25% or more of the screen, or any flashing sequence longer than 5 seconds, is High | Check emissive animations, VFX textures and every video |
| The experience page (title, thumbnail, description) must suit all ages | Thumbnails and icons are assets too: same checks |
| No purchase-pressure copy; Roblox's examples replace "GET IT NOW" and "LAST CHANCE" with "View Item", "See Price", "Open Shop"; no fake timers or scarcity | No urgency or scarcity wording baked into shop images, signs or UI art |
| Games for under-16s exclude free-form drawing; building from moderated 3D assets is fine | Player-placed decorations must come from moderated, pre-uploaded assets |
| No in-game ask for real names, ages, schools, addresses, phone numbers, photos or social handles | No images that show or request personal data, QR codes or handles |
| Essential text contrast at least 4.5:1; color and sound non-reliance | UI images and icons meet contrast; every gameplay sound has a visual twin |
| Use test accounts for each age band; don't sign in, buy Robux or change settings without the owner's authorization | Upload and review only through the owner-authorized group path |

Publishing to under-16s also needs ID verification, two-step verification, a fee or subscription and an evaluation [M5]; those are owner tasks, not asset tasks.
