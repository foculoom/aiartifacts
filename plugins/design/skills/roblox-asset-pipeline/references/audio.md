<!-- Audio sections by the audio owner, merged on 2026-11-27. Authoritative for audio; where SKILL.md and this file differ on audio, this file wins. Receipt fields now live in the unified receipt-template.json beside this file (see provenance-receipt.md for the field mapping). -->

# Audio sections for roblox-asset-pipeline (authoritative)

These blocks are the authoritative audio text for the shared `roblox-asset-pipeline` skill. Merge them under the matching numbered headings. Do not rewrite the licence conclusions without re-checking the cited primary sources (see `sources.md`). Accessed 27 November 2026, America/Los_Angeles, unless a source states an earlier revision date.

**Policy (encode in the skill):**

- Code-generated audio is pre-approved. Still measure it and fill a provenance receipt.
- Audio from fal.ai or Suno counts as imported and needs the owner's listen, in the owner's own words, for each asset. An agent's say-so is never approval.
- No uploads until the company Roblox group exists and the owner says yes to that exact asset.
- Use only the project's designated fal account. Do not use any other fal account. Keep keys and request ids out of public records; put request ids in the private receipt only.
- Re-check each model's page and the vendor's current terms on the day of generation. Badges and terms change.

---

## 1. Licence check and provenance receipt — audio

Run a licence check before any generation that is meant for a shipped experience. Record the result on the clip's provenance receipt (`receipt-template.json`). Do not generate, download, or upload a clip whose licence cannot support commercial use in a game.

### 1.1 Suno (music and songs)

Suno's current Terms of Service (last revised 10 August 2026, effective 3 September 2026) split ownership and commercial use by plan, and then further restrict commercial use to a permitted Download.

**Free / Basic — do not use for a commercial game.**

> "If you are a user of the free or basic tier of the Service then you covenant and agree that you will only use such Outputs for your lawful, personal and non-commercial purposes."
> — Suno Terms of Service, Intellectual Property Rights, "Free or Basic Tier Accounts"

The free-plan help page (edited 17 December 2025) says the same in plainer words: "Songs made on the free plan are only intended for personal, non-commercial use. These songs cannot be monetized, but can be shared using your Suno link." Free accounts also have up to 7 lifetime trial downloads; "You do not get commercial rights to trial downloaded songs" (Upcoming Changes FAQ, edited 25 November 2026).

**Upgrading does not grant rights to songs already made on the free plan.**

> "Subscribing to a Pro or Premier plan does not give you retroactive commercial use licensing for the songs made with a free plan by default. Songs made with Suno's free plan can only be used for non-commercial purposes. We may offer retroactive rights in certain cases, but this is not guaranteed and applies only to specific songs."
> — Suno help, "If I subscribe, do I get rights for the songs I made before subscribing?" (edited 17 December 2025)

The same rule is restated on the distribution help page: "starting a subscription after you made a great song will not give you a retroactive license for the song."

**Pro and Premier — assignment plus a permitted Download.**

> "Subject to your compliance with these Terms of Service, if you are a user who has subscribed to the Pro or Premier paid tier of the Service, Suno hereby assigns to you all of its right, title and interest in and to any Output owned by Suno and generated from Submissions made by you through the Service, provided such Output will remain subject to these Terms of Service including any applicable commercial use restrictions. Due to the nature of machine learning, Suno makes no representation or warranty to you that any copyright will vest in any Output."
> — Suno Terms of Service, "Pro and Premier Accounts"

Commercial use is a separate covenant, tied to a Download obtained through Suno's approved channel:

> "You may commercially exploit Output solely to the extent it adheres to Suno's Conditions of Access and Use as outlined above provided you have obtained a permitted download of that Output in accordance with the download allocations for your applicable service tier (each, a “Download”). You may not commercially exploit Output that has not been downloaded by you through an approved channel under these Terms of Service."
> — Suno Terms of Service, "Permitted Commercial Use"

The paid-plan help page (edited 3 September 2026) says: "Songs downloaded while subscribed are granted commercial use rights" and lists, among permitted uses, "Use them in film, tv, or video games." The FAQ (edited 25 November 2026) restates: "For any song that you download from the platform as a paying subscriber, you have the commercial rights to the music and can use it for commercial or personal use."

Download allotments (FAQ, 25 November 2026; blog, 10 August 2026): Pro 20 downloads per month; Premier 60 downloads per month; unused downloads do not roll over. Premier users of Suno Studio are described as having no Studio download limits. Additional downloads can be purchased. Obtaining a copy by any means other than Suno's download channel (for example recording or stream ripping) is prohibited.

Those commercial-use rights, once a permitted Download is obtained on a paid plan, are perpetual:

> "Any assignment made to you under the paragraphs above, and the commercial use rights described in this paragraph with respect to a Download you have obtained, are perpetual and are not affected by your exhaustion of your Download allotment, by any later change to allotments or pricing, or by the expiry, cancellation, downgrade or suspension of your subscription."
> — Suno Terms of Service, after "Permitted Commercial Use"

**Conservative working rule.** Generate the song while the account is on Pro or Premier, then obtain a permitted Download through Suno's approved channel while still subscribed. Record both the plan at creation and the Download. Do not use free-plan songs, trial downloads, ripped copies, or a later paid Download of a song that was created on the free plan.

There is a wording tension to flag for the owner (see open legal questions): older help articles ask "was I subscribed when I made the song?"; the September 2026 Terms and help pages emphasise a permitted Download while subscribed. Follow both conditions until the owner decides otherwise.

**Remixes are non-commercial on every plan.**

> "If you are a joint owner of a Remix generated by these Service features, and regardless of whether you are a free Service tier user or a subscriber to a paid Service tier, you additionally covenant and agree that the Remix may only be used for lawful, personal and non-commercial purposes, regardless of your subscription tier or whether the Remix is a permitted Download."
> — Suno Terms of Service, "Remixes"

**Attribution.** The distribution help page (edited 17 December 2025) says, of songs made while subscribed: "You do not have to attribute the songs to Suno, but we wouldn't mind if you let your audience know we helped you create your masterpiece!" The Terms do not impose a user-side credit duty, but they do grant Suno "the worldwide, fully paid-up, sublicensable, assignable, perpetual and irrevocable right to identify to the public (both on and off the Service) that Output (or any of it) was generated via the Service." Do not remove, alter, obscure, or circumvent any fingerprint, watermark, or metadata Suno appends.

**Platform and game uploads.** Paid-plan commercial rights expressly include video games, subject to the Conditions of Access and Use (no competing music-generation product, no training other models, no infringement, no impersonation, and the other listed restrictions). The Terms also say a third-party platform's own rules still apply; uploading to Roblox therefore also requires compliance with Roblox's Terms of Use, Community Standards, and the Audio Upload License Agreement.

**Inputs.** You must hold the rights to any lyrics or other Submissions. The distribution help page warns: "you must be the exclusive rights holder of 100% of the material. Don't try to monetize a song if you're using someone else's lyrics!"

### 1.2 fal.ai audio models

fal's own Terms of Service (last updated 8 September 2026) do **not** assign ownership of Output Content to the customer. The customer owns Customer Input. Output Content generated for the customer is treated as the customer's Confidential Information. fal does not warrant that outputs are original or non-infringing:

> "Company does not represent, warrant, or covenant that any Output Content will be original, will not infringe rights of any third party (including intellectual property rights), or otherwise entitle Company to any intellectual property rights in any Output Content. Customers' use of the AI Features is at their own risk."
> — fal Terms of Service, §4.3

Commercial use is per model, not a blanket fal grant. From fal's Model APIs FAQ:

> "Each model has its own license. Most models on fal are available for commercial use and are marked with a `Commercial use` badge on the model page. Models marked `Research only` are restricted to non-commercial use. Check the model's page for its specific license."

Third-party model terms can still apply:

> "Your access to and use of such Third-Party Materials may be subject to additional terms, conditions, and policies (including terms of service or privacy policies of the providers of such Third-Party Materials)."
> — fal Terms of Service, §14.2

Do not treat a `Commercial use` badge as the end of the check. Read the model page and the upstream licence. Do not use a model marked `Research only`, or an upstream non-commercial licence, for a commercial game.

Generated files on fal's CDN are available for at least 7 days by default and the URLs are public unless an ACL is set. Download the file immediately and keep it with the receipt. Do not rely on the fal URL as the archive, and do not put fal URLs or request ids in public pull requests.

**Model-by-model findings (pages and upstream licences read 27 November 2026):**

| Model on fal | fal badge (this date) | Upstream / extra terms | Commercial use in a Roblox game? |
| --- | --- | --- | --- |
| `fal-ai/stable-audio` (described as "Open source text-to-audio model") | Commercial use | Stability AI Community License (last updated 5 July 2024): free commercial use only if you and your affiliates are under USD $1,000,000 annual revenue, and commercial users must register; the licence terminates above that threshold. That licence governs self-hosted weights. Whether fal's hosted endpoint is fully outside it is an open legal question. | **Do not use** for a commercial game until the owner clears the Community License question. Prefer the hosted 2.5 / 3 endpoints below. |
| `fal-ai/stable-audio-25/text-to-audio` and `fal-ai/stable-audio-3/medium/text-to-audio` | Commercial use. Stable Audio 3 Medium is described as "trained on fully licensed data for safe commercial use." | Stability's commercial-usage guide: music and SFX generated through the hosted app or API may be used as embedded assets in video games, subject to Stability's Terms of Service and Acceptable Use Policy. Self-hosting is a different path (Community License). | **Usable**, subject to Stability's current ToS/AUP, a receipt, and the owner's listen. Re-check the model page on the day. |
| `fal-ai/mmaudio-v2` (and text-to-audio variants) | Commercial use. The model page also says "License: Commercial use permitted." | Hugging Face model card and the project's README: pretrained checkpoints are **CC BY-NC 4.0**, "can be used for non-commercial purposes only." The authors also write that they "do not guarantee that the pre-trained models are suitable for commercial use." | **Do not use.** Treat as non-commercial despite fal's badge, until the owner gets a legal sign-off that fal hosting somehow replaces CC BY-NC 4.0 (unlikely). |
| `fal-ai/elevenlabs/tts/eleven-v3` and other ElevenLabs speech endpoints | Commercial use; Partner API | ElevenLabs help (current): the free plan "does not include a commercial license"; "All paid plans include a commercial license, provided you're not using Beta Services." Content from a paid subscription may be used commercially indefinitely, subject to Service-Specific Terms. fal's page says "Commercial use rights included." Do not clone a real person's voice without a recorded right to do so. Beta Services cannot be used commercially. | **Usable for speech** on the same basis as a paid ElevenLabs commercial licence, subject to those Service-Specific Terms, a receipt, and the owner's listen. Confirm nothing used is a Beta Service. |
| `elevenlabs/music`, `elevenlabs/music/v2`, `elevenlabs/music/v2.5` | Commercial use | ElevenLabs Music Terms (last updated 9 October 2026), Exhibit A: on every self-serve plan including Business, Media Rights are "All online and offline commercial use permitted, **except film, TV, radio, and Studio Games**." Only Enterprise Music drops that exception. A "Studio Game" is a public, monetized interactive experience that is not an "Indie Game." An Indie Game is under $500,000 lifetime revenue and is published by an entity whose games revenue was under $1,000,000 in the prior financial year. Free–Pro plans are "For Individual Use Only." Free-plan music requires attribution and does not permit downloads. | **Do not use ElevenLabs Music in a commercial Roblox experience** unless the owner has an Enterprise Music agreement, or a written determination that the experience is an Indie Game *and* that fal usage sits on a plan that allows Indie Games. The fal badge does not cancel Exhibit A. |
| `fal-ai/minimax-music/v2` and MiniMax Music 3 (`fal.ai/minimax-music-3`) | Commercial use. Music 2.0 page: "License: Commercial use via fal partnership." Music 3 page: "Content generated through the fal.ai API can be used in commercial projects." | MiniMax Audio Music Creation Terms of Use (effective 19 June 2025, MiniMax's own app/web feature) require that you not remove embedded identifiers, and that you "clearly label AI-generated Output Content in your use to avoid misleading others." API/partnership terms may differ; keep the label rule in the receipt as a caution. | **Usable**, subject to MiniMax's current terms, any required AI labelling, a receipt, and the owner's listen. |
| `cassetteai/music-generator` | Commercial use | CassetteAI Terms & Conditions (last updated 13 February 2023): Pixl "does not claim ownership or responsibility for any content inputted into or generated by the Model"; the user "assumes all responsibility for determining the appropriateness of using or redistributing the generated content." The stated restriction is on commercially exploiting *the Model*, not clearly a grant of commercial rights in the output. The terms are old and silent on games. | **Usable only with caution.** fal's badge is commercial, but CassetteAI's own terms do not clearly grant game rights. Prefer a better-documented source unless the owner accepts this gap. |
| `fal-ai/ace-step` | Commercial use | Upstream ACE-Step repository is Apache License 2.0 (copyright 2025 Timedomain Inc. and stepfun). Apache 2.0 permits commercial use of the licensed Work. Confirm on the day that the fal endpoint is still this model and that any later weight-specific licence (some v1.5 cards have been listed as MIT) has not narrowed. | **Usable**, subject to the current upstream licence, a receipt, and the owner's listen. |
| `fal-ai/lyria3` and `fal-ai/lyria3/pro` | Commercial use | Google Lyria 3 documentation: Vertex AI preview customers "may elect to use it for production or commercial purposes, or disclose Generated Output to third-parties," subject to Google Cloud / Pre-GA terms. All outputs carry SynthID watermarking and support C2PA credentials. Do not strip watermarks. Safety filters block artist-voice mimicry. | **Usable**, subject to Google's current terms as they apply through fal, leaving SynthID intact, a receipt, and the owner's listen. Flag the Pre-GA / preview status for the owner. |

If a new audio model appears, the checklist is: fal badge, upstream licence, any plan or revenue cap, any media-type exclusion (especially games), watermark/attribution rules, and whether the account in use is the project's designated fal account.

### 1.3 Provenance receipt for each clip

Fill one receipt per clip, as JSON (`receipt-template.json`) plus a short markdown copy in the private evidence note or PR appendix. Required fields:

- **source** — one of:
  - code-generated: script path (and commit, if any) plus seed;
  - fal: model id, model version or endpoint, and request id;
  - Suno: track id, plan at creation, and Download evidence (date and that it was a permitted Download, not a trial or a rip);
- **prompt** (and negative prompt, lyrics, or tags if used);
- **date** of generation (timezone America/Los_Angeles);
- **account** (provider and account name only; never a key);
- **licence basis** with a link, the date the licence was read, commercial-use yes/no, and any restrictions;
- **edits** (trim, fade, EQ, loudness, loop seam, format conversion);
- **measured** LUFS-I, true peak (dBTP), clipping, loop wrap, attack time, level versus the bed, and guardrail result;
- **Roblox** asset id, owner group, moderation status (leave empty until uploaded);
- **owner-listen approval** — required for fal and Suno; for code-generated mark `not_required_code_generated`. When required, record who, when, and a short quote in the owner's own words.

A worked markdown example:

```markdown
### Receipt — ambience-fire-crackle-v1

- Source: code-generated. Script `audio/fire_crackle.py`, seed 1742.
- Prompt: n/a (procedural).
- Date: 2026-11-27, America/Los_Angeles.
- Account: local render, no vendor account.
- Licence basis: original code-generated audio; pre-approved under project policy. Link: this skill, §1 policy.
- Edits: 12 s loop, 80 ms equal-power fades, peak-normalised to −3 dBTP.
- Measured: −24.0 LUFS-I, −11.1 dBTP, no clipping, loop wrap pass, attack 199 ms, guardrail n/a (this is the bed).
- Roblox: not uploaded. asset id —, owner group —, moderation status not_uploaded.
- Owner-listen approval: not required (code-generated). Measurements recorded.
```

```markdown
### Receipt — dusk-underscore-suno-v1

- Source: Suno. Track id `…`. Plan at creation: Premier. Permitted Download obtained 2026-11-27 via Suno's download channel (not a trial download, not a remix, not a rip).
- Prompt: "[instrumental] evening garden, warm low pad, no vocals, no lyric…"
- Date: 2026-11-27, America/Los_Angeles.
- Account: Suno, project Premier account (name only in the private receipt).
- Licence basis: Suno Terms of Service, Pro/Premier assignment plus Permitted Commercial Use after a paid Download; games listed on the paid-plan help page. Link: https://suno.com/terms (read 2026-11-27). Restrictions: no remix-feature output; do not strip watermarks; third-party (Roblox) terms still apply.
- Edits: trim to 23 s, loop seam, loudness to −20 LUFS-I, export 48 kHz stereo WAV.
- Measured: −20.1 LUFS-I, −3.2 dBTP, no clipping, loop wrap pass, attack 140 ms, +1.2 dB vs bed (not a sharp attack), guardrail pass.
- Roblox: not uploaded.
- Owner-listen approval: pending. Required before any upload.
```

---

## 2. Roblox specs and limits — audio

Refreshed 27 November 2026 from Creator Hub pages whose front matter reads `last_updated: 2026-11-24`.

### 2.1 Formats, length, size, and sample rate

From [Audio assets](https://create.roblox.com/docs/audio/assets):

- Formats: a single track or stream in `.mp3`, `.ogg`, `.wav`, or `.flac`.
- Size and length: under 20 MB and under 7 minutes.
- Sample rate: 48 kHz or less.
- Channels: mono, or stereo 2.0, 3.0, or 5.1 surround.

You must have the legal rights to the file, and it must follow the [Community Standards](https://en.help.roblox.com/hc/articles/203313410) and [Terms of Use](https://en.help.roblox.com/hc/articles/115004647846).

Studio transcodes every import "to standardize the playback format and check for corrupt or invalid files." Invalid headers or frames are rejected during transcode. Prefer a clean 48 kHz (or 44.1 kHz) WAV or FLAC for upload so the transcode starts from a lossless original. After transcode, keep the asset id on the receipt.

Import paths: Asset Manager, Creator Dashboard, or the Open Cloud Assets API with `assetType: Audio`. For a group-owned experience, create the asset as a **group** asset (pass the group id), not under a personal account. Open Cloud needs a group-scoped API key the owner creates; do not mint or read a key.

### 2.2 Upload quotas and cost

The two Roblox pages give different figures, each for its own upload path:

- **Creator Hub / Studio** (Asset Manager, Creator Dashboard; [Audio assets](https://create.roblox.com/docs/audio/assets)): 2,000 free audio imports per 30 days if ID-verified, 100 if not. Daily caps, if any existed, have been replaced by this monthly limit.
- **Open Cloud** (Assets API; [usage guide](https://create.roblox.com/docs/cloud/guides/usage-assets)): up to 100 uploads per month if ID-verified, up to 10 total per month if not.

When uploading by API, plan for the lower Open Cloud figure.

**Open item:** whether a group-owned upload counts against the uploading member's allowance or the group's is not documented. It stays open until the first upload. Record on the receipt which account the upload counted against (`roblox.quota_counted_against`).

The Audio assets page describes these as free imports. It does not publish a Robux price or a paid overage for going past the cap. Do not invent a cost. If the cap is close, stop and tell the owner.

ID verification is also required before a classified "song" can appear on a game details page.

### 2.3 Moderation notes that apply to audio

Uploads enter a moderation queue. Until they pass, they are visible only to the uploader. After they pass, they can be reused in projects that have permission.

Uploads are auto-classified as a **sound effect** or a **song**. A song may appear on the game details page only if it passes moderation and copyright checks, meets duration, playback, and age requirements, has an appropriate title, the uploader is ID-verified, and the uploader has acknowledged the Roblox Audio Terms of Use (the Audio Upload License Agreement). That visibility can be turned off on the asset's Configure page. Prefer leaving song visibility off unless the owner asks otherwise.

The Audio Upload License Agreement requires that audio "must at all times conform to Roblox's community standards and guidelines that are part of the Roblox Legal Terms (e.g., no profanity, drug or explicitly sexual references)." This matters for any clip with lyrics, speech, or recognisable sung words, and for experiences that will be available to young players. Do not upload a cue that would fail that standard.

Roblox may refuse to publish audio it believes violates those standards. Moderation status belongs on the receipt (`not_uploaded`, `pending`, `approved`, or `rejected`).

### 2.4 Privacy and permission grants for group-owned experiences

Audio is **not** controlled by the Asset Privacy toggle (that toggle is only for Images, Decals, and Meshes). Audio has its own creation defaults.

> "Initially you are the only one who can view and use private audio assets."
> — Audio assets / asset privacy docs

Grant use to the group that owns the experience, or to that experience itself. Game grants are permanent and cannot be revoked. Upload under the company group once it exists; do not upload to a personal account and then try to patch permissions later.

"Open Use" (where it applies) is irreversible. Keep imported audio restricted and grant only the owning group and the intended experience.

### 2.5 Licence terms Roblox gets on upload

Two overlapping grants apply.

**Audio Upload License Agreement** (accepted at upload). The uploader warrants that they own or have licensed the audio and that Roblox will not owe royalties to labels, publishers, PROs (ASCAP, BMI, SESAC, SoundExchange), unions, or other participants. Then:

> "Creator hereby grant to Roblox a perpetual, worldwide license to: (a) transmit, reproduce, communicate to the public, and publicly perform, reproduce, synchronize and create derivative works from the Audio on the Platform and in all distribution channels of the Platform, (b) feature the artist name(s), writer name(s), and track title(s)) of the Audio on the Platform, (c) digitally transcode, make copies of, reproduce and otherwise process the Audio to the extent necessary to facilitate any of the foregoing rights, (d) sublicense any of the foregoing rights to developers and users of the Platform for the purposes of featuring the Audio in games, experiences, virtual merchandise on the Platform and in connection with the promotion thereof, and (e) use the Audio and related content for promotional purposes. You hereby grant users who purchase products containing Audio a perpetual license for the use of such product."

**Roblox Terms of Use** (effective 1 November 2026), User Terms §3.2, a broader UGC licence:

> "you grant to Roblox a worldwide, non-exclusive, royalty-free … perpetual, irrevocable, fully sublicensable and transferable license (including to other Users) to use, host, store, transfer, copy, reproduce, distribute, modify, adapt, prepare derivative works of, display, publicly perform, publish, and otherwise exploit the UGC provided to Roblox … for any lawful business purpose, including without limitation: (1) promoting all or part of the existing or future Services; (2) for making UGC available within the Services to other Users and audiences, … monetizing that engagement …; and (3) in connection with developing, improving, or training any AI or machine learning models."

You retain ownership "subject only to the non-exclusive license granted in the Roblox Terms." Deleted audio may still be used by Roblox and by users who already received it, because the licence is perpetual.

Do not upload until the owner has accepted that these grants will attach to that exact file, the company group exists, and the owner has said yes to the asset.

---

## 4. Prep — audio

Prep every clip before any upload ask. Follow **audio-pr-proof-of-work** for the measurement ritual (render or capture each cue, ffmpeg `ebur128` for integrated LUFS and true peak, clipping, loop-wrap check, and a fal `audio-understanding` second opinion on the project's designated fal account). That skill does not itself set numeric targets; use the targets below unless the project records different ones.

### 4.1 Loudness targets

Roblox does not publish official LUFS or true-peak targets. The numbers in this table are project recommendations, chosen so beds stay out of the way, interaction cues stay clear, transcode inter-sample peaks have headroom, and the mix stays consistent with audio-pr-proof-of-work. They are not a Roblox rule.

| Role | Integrated loudness (LUFS-I) | True peak | Notes |
| --- | --- | --- | --- |
| Beds / ambience loops | −24 to −20 | ≤ −3 dBTP | A 2D bed at −24 LUFS-I is a tested reference level. |
| Music / underscore | −23 to −18 | ≤ −3 dBTP | Sit with or slightly above the bed; avoid a sharp attack. |
| SFX / interaction | −22 to −16 | ≤ −3 dBTP | Must also pass the 6 dB sharp-attack guardrail against the bed, measured where the player stands. |
| UI | −20 to −16 | ≤ −3 dBTP | Prefer a soft attack. |
| Speech / VO | −20 to −16 | ≤ −3 dBTP | |

Leave true-peak headroom on the file because Studio transcodes on import and lossy codecs can raise peaks. After transcode, the clip must not clip; prefer to stay at or below −1 dBTP in the experience.

For now the ≤ −3 dBTP file target is enough. **Post-transcode gate (owner-machine step):** after the first upload, re-download or capture the transcoded asset on the owner's own computer, measure its true peak once, and record it on the receipt (`measured.post_transcode_true_peak_dbtp`, `measured.post_transcode_verified`). Only after that measurement passes is "≤ −1 dBTP after transcode" treated as verified; until then, say it is unverified. Report any sample at or above 0 dBFS.

### 4.2 How Roblox's mixer changes what you hear

- `AudioPlayer.Volume` and `AudioFader.Volume` are **linear amplitude**, range 0–10, not decibels. A change from 0.5 to 1.0 is not "+6 dB" by a volume-property reading alone; measure the output.
- Legacy `Sound.Volume` is also 0–10 and defaults to 0.5.
- `AudioLimiter.MaxLevel` runs from −12 to 0 dB. Use it as a safety ceiling, not as the way to hit the LUFS target.
- The player's own volume settings, and any sidechain duck, change the heard level.
- Spatial attenuation (`AudioEmitter` distance and angle curves, occlusion) lowers a 3D cue as the listener moves. A file that is safe on its own can still break the guardrail at the standing spot, or disappear at the edge of its curve.
- Measure two ways: the file (LUFS-I, true peak, loop wrap) and the mix at the player's normal standing spot (guardrail, ducking, bed-plus-cue).

### 4.3 Guardrail

**No new cue more than 6 dB above the bed with a sharp attack.** A sharp attack is a 10–90% rise shorter than 10 ms. Compare the cue's maximum momentary level to the bed's integrated level at the standing spot, not only on the dry file. A slow swell may sit a little closer; a click, slam, or stinger may not.

For sidechain ducks of the bed under an interaction cue, keep the duck at or under 6 dB, with a short attack (about 10–30 ms) and a release of about 300–600 ms, unless the project records different figures.

Record the guardrail result on the receipt and in the audio-pr-proof-of-work PR table.

### 4.4 File prep checklist

1. Render or export a lossless WAV (prefer 48 kHz, 24-bit). Mono for a single positional emitter; stereo for a 2D bed. Keep 5.1 only if the design needs it.
2. Edit: trims, fades, loop seam (an 80 ms window at the join; a negative correlation or an audible step fails), loudness to the table above, true peak ≤ −3 dBTP.
3. Measure with audio-pr-proof-of-work. Paste the table. Run the fal second opinion on the project's designated fal account only; it may raise at most a Medium, and it is review only.
4. Fill the provenance receipt. For fal and Suno, stop here until the owner listens and approves the exact file, in the owner's own words.
5. Do not upload until the company Roblox group exists and the owner has said yes to that asset. Then upload as a group audio asset, grant the experience, and write the asset id and moderation status back onto the receipt.

Code-generated audio skips the owner-listen gate but still needs measurement, a receipt, the group, and a per-asset upload yes.

**Video soundtracks.** A video's soundtrack follows §4.1 by role (music, SFX or speech). Measure it as audio and record it on the video's receipt as audio, under the same owner-listen rule.
