---
name: roblox-asset-pipeline
description: >-
  Take an AI-generated or code-generated asset (3D mesh, image or decal, audio,
  video) from licence check to approved Roblox upload: per-source licence check
  before generating (fal model licences, Suno plan rights, code and its
  inputs), a provenance receipt per asset, Roblox format/size/quota limits,
  moderation and young-player rules, prep and measurement, and the owner and
  spend gates. Use before generating, preparing, importing or uploading any
  asset for a Roblox experience; not for avatar/Marketplace items or for
  in-scene audio wiring (use roblox-spatial-audio).
---

# Roblox asset pipeline (generated assets)

One asset moves through six gates in order: **licence → spend → generate → prep and measure → owner yes → upload under the group**. Skip none. If a gate cannot be passed, stop and write down why.

Facts were checked on create.roblox.com, the Roblox Terms, fal model pages and Suno's terms on 2026-11-27 (America/Los_Angeles). They change; re-check anything you are about to quote in a PR or an approval request. Details and links are in the references:

- [Licence check per source](references/licence-check.md) (fal model table, Suno, code-generated)
- [Roblox asset specs and limits](references/roblox-asset-specs.md)
- [Moderation, community standards and young players](references/moderation-and-young-players.md)
- [Audio: licences, Roblox audio limits, loudness and prep](references/audio.md), by the audio owner, with [audio sources](references/audio-sources.md)
- [Provenance receipt](references/provenance-receipt.md) and its one shared [receipt template](references/receipt-template.json)
- [Sources](references/sources.md)

**Audio is co-owned with the audio owner; their sections are authoritative.** [audio.md](references/audio.md) was merged as written: its §1 (Suno, fal audio licences, receipt fields) belongs under step 1 here, its §2 (Roblox audio formats, quotas, moderation, privacy, upload licence) under steps 4 and 6 and the specs reference, and its §4 (loudness, mixer, the 6 dB guardrail, prep) under step 5.3. Where this file and audio.md differ on audio, audio.md wins.

## 1. Licence check, before generating anything

Do this before the first paid call, per asset type and per tool. A licence you cannot find is a **no**.

1. **fal models.** Open the model's own fal page (`https://fal.ai/models/<endpoint-id>`). fal says each model has its own licence: a **Commercial use** badge allows commercial use; **Research only** is non-commercial. Record the badge, the page URL and the date. Then:
   - If the page links an upstream licence (GitHub, Hugging Face, vendor), read it too. Commercial on fal does not remove upstream conditions such as territory exclusions, revenue caps, registration or attribution. See the table for known cases (for example Hunyuan3D 2.x excludes the EU, UK and South Korea, which a worldwide game cannot honour).
   - The model page's badge is what counts. If the page shows no badge, treat the model as unverified and don't use it until the owner decides. (fal's catalog API sometimes leaves `license_type` empty for a model whose page shows a badge; record the page.)
   - Never use a Research-only model, or one whose upstream licence is non-commercial, for anything that may ship, including concept images that feed a shipped mesh.
   - Audio models: follow the audio owner's table in [audio.md](references/audio.md) §1.2. Scope rules for a shipped game: no MMAudio (upstream weights CC BY-NC); no ElevenLabs Music (self-serve plans exclude Studio Games); no Pre-GA models such as Lyria 3; Stable Audio Open only once the owner clears its $1M Community License cap; Suno under the strict reading only; the owner listens to every generated clip. SFX: ElevenLabs Sound Effects v3 (or v2) and hosted Stable Audio 3 Small SFX are usable, embedded in the game and never shipped as a standalone library; CassetteAI SFX is caution; Sonilo SFX is an owner question.
2. **Suno** (full ruling in [audio.md](references/audio.md) §1.1). Only songs made while the account was on a paid Pro or Premier plan carry commercial rights. Free/Basic songs are personal and non-commercial, and subscribing later does not license them retroactively. Commercial use also needs a permitted download through Suno's own download channel; don't strip Suno's watermark or metadata; Remixes made with Suno's remix features are non-commercial on every plan; don't use lyrics or audio you don't own. Working rule: create on Pro or Premier **and** take a permitted Download while subscribed; a free-plan song never gains rights after an upgrade. Record the plan at creation and the Download.
3. **Code-generated assets** (numpy audio, procedural textures, scripted meshes). The output is the project's own, but list every input that is not: sample packs, impulse responses, fonts, HDRIs, noise or texture images, presets, scanned models and third-party code that is copied into the asset. Each needs its own licence entry. Tool licences (Blender, ffmpeg, numpy) do not normally attach to their output; note the versions anyway.
4. **Other sources** (stock, Creator Store, commissioned work): the asset needs a written licence that allows use in a commercial Roblox game *and* lets you grant Roblox the upload licence in step 6.3. Creator Store assets are used by ID, not re-uploaded.
5. Open a [provenance receipt](references/provenance-receipt.md) for the asset now, from the one shared [template](references/receipt-template.json), with the licence fields filled in. No receipt, no generation.

## 2. Spend gate

1. Write a cost table (model × tries, per-call price from the model page, cleanup and remesh calls, any Roblox fees such as 2,000 Robux per video upload).
2. Ask the owner for a fixed cap. Generation starts only after a **recorded** spend approval (who, cap, scope, date). Record the approval reference in each receipt.
3. Use only the project's designated generation account. Keep account names, keys and request ids out of public records.

## 3. Generate

1. Follow the asset type's skill: [fal-image-to-3d](../fal-image-to-3d/SKILL.md) for meshes (concept image → image-to-3D with a polycount target). Images, audio and video follow the prompt rules in their own project skills.
2. Prompt for content that passes moderation and the declared rating from the start (see section 4): no real people, brands, logos, real-world text or URLs, gore, romance, profanity, political or real-world tragedy references.
3. Fill in the receipt: tool, model or plan, date and time with time zone, full prompt, negative prompt, seed, input image hashes, output file names and their SHA-256, and the cost.

## 4. Moderation and audience check

Every uploaded image, mesh, audio and video file is moderated, and the assets you upload are judged on their own, separately from the experience's content rating. Before asking for the owner's yes, check each asset against [the moderation list](references/moderation-and-young-players.md):

1. **Community Standards**: no profanity in any language, text, image or audio (lyrics included); no sexual or suggestive content; no realistic gore; no real-world sensitive events, extremist or political figures or entities; no regulated goods (alcohol, tobacco, vaping, drugs); no personal information; no URLs or off-platform calls to action; no third-party IP.
2. **Rating fit**: the asset must not push the experience above its declared content rating. For a young audience, use the rules in **roblox-3d-play-pass** section 8: scary is not horrifying (no jumpscares, sustained dread or eerie stingers), no flashing over 3 per second, no urgency or fake-scarcity copy on any image, and nothing above Mild for Kids (5–8) and Select (9–15).
3. **AI artifacts**: look for garbled text or letterforms that read as words, logo-like marks, faces in textures, and accidental body shapes. Regenerate rather than upload anything ambiguous.
4. Re-uploading the same or near-identical content counts as spam under the Community Standards. Fix the asset; don't retry the upload in a loop.

## 5. Prep and measure

### 5.1 Meshes (3D)

1. Run the cleanup in [fal-image-to-3d](../fal-image-to-3d/SKILL.md) section 3 in headless Blender: apply transforms, scale in studs, decimate to the budget from **roblox-3d-art-direction**, Weighted Normal for stylized shading, one UV set in 0–1 space, one material per mesh, watertight with no n-gons and no zero-thickness faces. Export glTF/GLB or FBX.
2. Hard limits: **≤ 20,000 triangles per mesh**; meshes import through the 3D Importer (`.fbx`, `.gltf`/`.glb`, `.obj`) or Open Cloud as a `Model` (packages, ≤ 20 MB per call).
3. Bake PBR maps for SurfaceAppearance: Albedo RGB, Normal **OpenGL tangent space**, Roughness, Metalness and Emissive mask as 8-bit greyscale; ≤ 1024² per map as the working cap, smaller for small props (256 for about 5×5 studs, 512 for 10×10).
4. LODs: Roblox does not take authored LOD chains for a MeshPart. Set `RenderFidelity = Automatic` (switches detail by distance) and keep `Precise` for hero meshes only. With streaming on, `Model.LevelOfDetail = SLIM` gives distant models a lightweight mesh. Use `CollisionFidelity` Box or Hull, or invisible collider Parts.
5. Run [3d-visual-gate](../3d-visual-gate/SKILL.md) on the imported asset in its room (fixed shots, phone and low-quality captures, L* contrast, triangles, draw calls, memory, and the review-only vision check).

### 5.2 Images, decals and texture maps

1. Format `.png` (alpha), `.jpg`, `.tga` or `.bmp`. Roblox supports up to 4096² textures and Open Cloud images must be under 8000×8000, but size for screen use: 256/512/1024 by object size, power-of-two sides, and 1024² as the SurfaceAppearance map cap.
2. Alpha: export straight (not premultiplied) alpha. For `AlphaMode = TintMask`, keep colour in the transparent areas. For hard cut-outs (foliage, lace) set `MeshPart.Transparency = 0`; for soft gradients set it to at least 0.02.
3. A Decal upload also creates a separate Image asset, and texture properties in scripts need the **image** id.
4. UI images: check contrast (≥ 4.5:1 for text and essential icons) and that no image carries baked text that needs localising or filtering.

### 5.3 Audio — co-owned with the audio owner; their skills are authoritative

Follow [audio.md](references/audio.md) §4 as written. In short:

1. Render or export a lossless WAV (prefer 48 kHz, 24-bit); mono for one positional emitter, stereo for a 2D bed. Upload limits: `.mp3`, `.ogg`, `.wav` or `.flac`, one track, < 20 MB, < 7 minutes, ≤ 48 kHz. Per **roblox-spatial-audio**, there is no runtime synthesis in a shipped game, so code-generated audio is an offline render that you upload.
2. Measure with **audio-pr-proof-of-work** (LUFS-I, true peak, clipping, loop wrap, review-only second opinion). That skill sets no numbers; the targets are the audio owner's table in audio.md §4.1 (project recommendations, not Roblox rules), with true peak ≤ −3 dBTP on the file for transcode headroom.
3. Remember the mixer (audio.md §4.2): Volume properties are linear 0–10, not dB; measure the output.
4. Guardrail (audio.md §4.3): no new cue more than 6 dB above the bed with a sharp attack (10–90% rise < 10 ms), measured where the player stands; ducks ≤ 6 dB. If the asset changes how the scene sounds, also record **3d-feel-proof-of-work** section 4.
5. Post-transcode gate (owner-machine step): the ≤ −3 dBTP file target is enough for now. After the first upload, re-download or capture the transcoded asset on the owner's own computer, measure it once, and only then treat ≤ −1 dBTP after transcode as verified.
6. Fill the receipt. fal and Suno audio stop for the owner's listen on the exact file; code-generated audio is pre-approved but still needs measurement, a receipt, the group and a per-asset upload yes.

### 5.4 Video

1. Prefer not to use video in a young-audience pilot: each upload costs 2,000 Robux (a spend gate), uploads need a 13+ ID-verified uploader, and a VideoFrame plays only in a ScreenGui, SurfaceGui or BillboardGui, with at most two videos playing at once.
2. If approved: `.mp4` or `.mov`, ≤ 5 minutes, ≤ 4096×2160, < 3.75 GB, no alpha (ignored), at most 20 uploads a day. Use `VideoFrame`, or `VideoPlayer` wired to a `VideoDisplay`. Check flashing (≤ 3 per second). The soundtrack follows audio.md §4.1 by role (music, SFX or speech), is measured as audio and goes on the receipt as audio, under the same owner-listen rule.

## 6. Owner yes, then upload under the group

1. **Owner's explicit yes per asset**, before import or upload (`owner_upload_yes` in the receipt; generated meshes, images, video and fal/Suno audio also need the owner's look or listen first). Show the exact files with their SHA-256 hashes, the receipt, the measurements and the moderation check. Another agent's or reviewer's approval is not the owner's yes. A changed file needs a new yes.
2. **Upload only under the company's Roblox group**, never a personal account. In Open Cloud, the `creationContext` must be the group; the API key must be one the owner created with group asset permissions. Group owners are responsible for all content associated with the group, so the group's standing is at stake on every upload.
3. **Upload licence: original assets only.** Uploading grants Roblox a worldwide, perpetual, irrevocable, sublicensable licence to the content, including for promotion and for training AI models; audio adds the Audio Upload License Agreement (you warrant that you hold every needed licence and indemnify Roblox). Accept these only for assets the project originated (code-generated, or generated with a commercially licensed tool from the project's own prompts and inputs). For anything else (third-party inputs, a licence that does not allow sublicensing to the platform, unclear terms), get a separate owner decision first.
4. **Privacy.** Before the first upload, decide with the owner whether to enable Asset Privacy for the group: without it, new Images, Decals and Meshes are **Open Use**, and Open Use cannot be reversed. Audio and video are private to the creator until permission is granted. Grant access to the experience (universe), not to people. Game grants are permanent.
5. **Quotas.** Audio, by path (audio.md §2.2): Creator Hub / Studio 2,000 free imports per 30 days if ID-verified, 100 if not; Open Cloud 100 per month if ID-verified, 10 if not. When uploading by API, plan for the lower Open Cloud figure. Whether a group upload counts against the member or the group is an open item until the first upload: record it in `roblox.quota_counted_against`. No Robux price is published for audio. Video: 20 per day, 2,000 Robux each.
6. After upload, record in the receipt: asset id, asset type, owning group, upload path, moderation state (`Reviewing`, `Approved` or `Rejected`), privacy grants. Until it is Approved, only the uploader can see or hear it; don't ship a build that depends on an asset still in review.
7. **If rejected:** don't re-upload variations. Read the moderation notice, and appeal through Violations & Appeals or Support with the asset id within 30 days (6 months in the EU) if the decision is wrong. A reviewed decision can't be reviewed again. Repeated violations risk warnings, removal, and suspension of the account or group.

## Report

Paste a short table per asset into the PR or approval request:

```
| Asset | Type | Source / model or plan | Licence (link, date) | Receipt | SHA-256 | Checks | Owner yes | Asset id / state |
```

Keep private details (accounts, keys, request ids, private names) in the project's private records, not in public files.
