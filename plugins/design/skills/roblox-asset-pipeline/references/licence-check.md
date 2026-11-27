# Licence check per source

Checked 2026-11-27 (America/Los_Angeles). Licences and badges change: re-open the page on the day you generate, and copy the badge and date into the asset's receipt. This table is a dated snapshot, not legal advice and not a licence review; the owner decides on anything flagged.

## How fal marks licences

fal's FAQ: "Each model has its own license. Most models on fal are available for commercial use and are marked with a `Commercial use` badge on the model page. Models marked `Research only` are restricted to non-commercial use." fal's model-search API exposes the same field as `license_type` (`commercial`, `research` or `private`), but it is sometimes empty for models whose page shows a badge. The page badge is the record.

fal's Terms of Service (8 Sep 2026) don't assign output ownership or warrant non-infringement (§4.3), and third-party model terms may still apply (§14.2); see [audio.md](audio.md) §1.2. A fal badge covers what fal offers. Where a page or catalog entry links an upstream licence, that licence's conditions still apply to you (territory, revenue cap, registration, attribution, acceptable-use policy).

Method used for this snapshot: read-only fetch of each `https://fal.ai/models/<endpoint-id>` page (badge and embedded `licenseType`/`licenseUrl`) and of `https://api.fal.ai/v1/models?category=<category>` for the 3D, image, audio and video categories. No model was run.

## fal models

Legend: **OK** = Commercial use badge, no extra upstream conditions found. **Conditions** = commercial on fal, but an upstream licence adds terms. **Avoid** = Research only, or an upstream licence a worldwide Roblox game can't meet. **Unverified** = no badge.

### 3D (image-to-3D, text-to-3D, cleanup)

| Endpoint (page) | fal badge | Upstream licence linked | Verdict |
| --- | --- | --- | --- |
| [meshy/t2/image-to-3d](https://fal.ai/models/meshy/t2/image-to-3d) | Commercial use | none | OK |
| [meshy/t2.5/image-to-3d](https://fal.ai/models/meshy/t2.5/image-to-3d) | Commercial use | none | OK |
| [meshy/v7.1/image-to-3d](https://fal.ai/models/meshy/v7.1/image-to-3d) | Commercial use | none | OK |
| [fal-ai/meshy/v6/image-to-3d](https://fal.ai/models/fal-ai/meshy/v6/image-to-3d) | Commercial use | none | OK |
| [tripo3d/h3.1/image-to-3d](https://fal.ai/models/tripo3d/h3.1/image-to-3d) | Commercial use | none | OK |
| [tripo3d/p2/image-to-3d](https://fal.ai/models/tripo3d/p2/image-to-3d) | Commercial use | none | OK |
| [tripo3d/tripo/remesh](https://fal.ai/models/tripo3d/tripo/remesh) | Commercial use | none | OK |
| [hyper3d/lowpoly/image-to-3d](https://fal.ai/models/hyper3d/lowpoly/image-to-3d) | Commercial use | none | OK |
| [fal-ai/hyper3d/rodin/v2.5](https://fal.ai/models/fal-ai/hyper3d/rodin/v2.5) | Commercial use | none | OK |
| [fal-ai/hyper3d/rodin](https://fal.ai/models/fal-ai/hyper3d/rodin) (v1) | Commercial use on the page; catalog `license_type` empty | none | OK (record the page) |
| [fal-ai/trellis-2](https://fal.ai/models/fal-ai/trellis-2) | Commercial use | none | OK |
| [fal-ai/trellis](https://fal.ai/models/fal-ai/trellis) (v1) | Commercial use | [MIT](https://github.com/microsoft/TRELLIS/blob/main/LICENSE) | OK |
| [fal-ai/hunyuan-3d/v3.1/pro/image-to-3d](https://fal.ai/models/fal-ai/hunyuan-3d/v3.1/pro/image-to-3d) | Commercial use | none linked | Conditions: fal says commercial; Tencent's own terms for 3.x aren't linked. Ask the owner before shipping; prefer another model for a worldwide game |
| [fal-ai/hunyuan-3d/v3.1/rapid/image-to-3d](https://fal.ai/models/fal-ai/hunyuan-3d/v3.1/rapid/image-to-3d) | Commercial use | none linked | Conditions: as above |
| [fal-ai/hunyuan3d/v2](https://fal.ai/models/fal-ai/hunyuan3d/v2) (and its mini, turbo and multi-view variants) | Commercial use | Tencent Hunyuan 3D 2.0 Community License ([LICENSE](https://github.com/Tencent-Hunyuan/Hunyuan3D-2/blob/main/LICENSE)) | **Avoid**: the licence "does not apply in the European Union, United Kingdom and South Korea", and you "must not use, reproduce, modify, distribute, or display … Output … outside the Territory". A Roblox game is shown worldwide |

### Images (concepts, textures, decals, UI art)

| Endpoint (page) | fal badge | Upstream licence linked | Verdict |
| --- | --- | --- | --- |
| [fal-ai/flux/dev](https://fal.ai/models/fal-ai/flux/dev) | Commercial use | none | OK (as offered on fal) |
| [fal-ai/flux/schnell](https://fal.ai/models/fal-ai/flux/schnell) | Commercial use | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0.txt) | OK |
| [fal-ai/flux-pro/v1.1](https://fal.ai/models/fal-ai/flux-pro/v1.1) | Commercial use | none | OK |
| [fal-ai/recraft/v3/text-to-image](https://fal.ai/models/fal-ai/recraft/v3/text-to-image) | Commercial use | none | OK |
| [fal-ai/ideogram/v3](https://fal.ai/models/fal-ai/ideogram/v3) | Commercial use | none | OK |
| [fal-ai/nano-banana](https://fal.ai/models/fal-ai/nano-banana) | Commercial use | none | OK |
| [fal-ai/bytedance/seedream/v4/text-to-image](https://fal.ai/models/fal-ai/bytedance/seedream/v4/text-to-image) | Commercial use | none | OK |
| [fal-ai/stable-diffusion-v35-large](https://fal.ai/models/fal-ai/stable-diffusion-v35-large) | Commercial use | [Stability AI Community License](https://stability.ai/community-license-agreement) | Conditions: free commercial use only while the licensee and affiliates make under US $1M a year; commercial users must register with Stability AI; attribution ("Powered by Stability AI") and a Notice file when distributing the model or a derivative |
| [fal-ai/fast-sdxl](https://fal.ai/models/fal-ai/fast-sdxl) | Commercial use on the page; catalog `license_type` empty | [SDXL licence](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/LICENSE.md) (CreativeML Open RAIL++-M) | Conditions: use restrictions in the RAIL licence apply; read before use |
| fal-ai/face-to-sticker | **Research only** (catalog; deprecated) | — | **Avoid** |

### Audio (SFX, music, speech, review)

The audio owner's full model-by-model findings, with quotes and upstream licences, are in [audio.md](audio.md) §1.2 and are authoritative.

**Audio scope rules for a shipped game:** no MMAudio; no ElevenLabs Music; no Pre-GA models (such as Lyria 3); Suno under the strict reading of its terms only (created on Pro or Premier **and** a permitted Download while subscribed); and the owner listens to every generated clip before upload.

Highlights:

| Endpoint (page) | fal badge | Upstream / extra terms | Verdict | Source |
| --- | --- | --- | --- | --- |
| [fal-ai/mmaudio-v2](https://fal.ai/models/fal-ai/mmaudio-v2) and its text-to-audio variants | Commercial use | Upstream checkpoints are **CC BY-NC 4.0** ("non-commercial purposes only"); the authors "do not guarantee that the pre-trained models are suitable for commercial use" | **Do not use** | [MMAudio model card](https://huggingface.co/hkchengrex/MMAudio) · [MMAudio README](https://github.com/hkchengrex/MMAudio/blob/main/README.md) · [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |
| [elevenlabs/music](https://fal.ai/models/elevenlabs/music), [v2](https://fal.ai/models/elevenlabs/music/v2), [v2.5](https://fal.ai/models/elevenlabs/music/v2.5) | Commercial use | ElevenLabs Music Terms, Exhibit A (last updated 9 Oct 2026): every **self-serve plan**, Business included, allows commercial use "except film, TV, radio, and Studio Games"; only Enterprise Music drops the exception. A Studio Game is a public, monetised game that isn't an Indie Game (Indie: under $500,000 lifetime revenue, publisher under $1M games revenue the prior year) | **Do not use** in a commercial Roblox game without an Enterprise Music agreement or a written Indie Game determination | [ElevenLabs Music Terms](https://elevenlabs.io/music-terms) |
| [fal-ai/stable-audio](https://fal.ai/models/fal-ai/stable-audio) (Stable Audio Open) | Commercial use | Stability AI Community License: free commercial use only while the licensee and affiliates make **under US $1,000,000 a year**; the licence terminates above that; commercial users must register; attribution | **Do not use** until the owner clears the Community License question (audio owner's ruling); prefer the hosted Stable Audio 2.5 / 3 endpoints | [Stability AI Community License](https://stability.ai/community-license-agreement) · [licence overview](https://stability.ai/license) |
| [fal-ai/stable-audio-25/text-to-audio](https://fal.ai/models/fal-ai/stable-audio-25/text-to-audio), [fal-ai/stable-audio-3/medium/text-to-audio](https://fal.ai/models/fal-ai/stable-audio-3/medium/text-to-audio) | Commercial use | Hosted path: Stability's ToS and AUP; games permitted as embedded assets | Usable (receipt, owner listen) | [Stable Audio commercial licensing](https://kb.stability.ai/knowledge-base/stable-audio-commerical-and-usage-licensing) |
| [fal-ai/elevenlabs/tts/eleven-v3](https://fal.ai/models/fal-ai/elevenlabs/tts/eleven-v3) and other ElevenLabs speech | Commercial use | Paid-plan commercial licence, not Beta Services; no cloning of a real person's voice without a recorded right | Usable for speech | [ElevenLabs publishing help](https://elevenlabs.io/docs/help-center/legal/can-i-publish-the-content-i-generate-on-the-platform) |
| [fal-ai/ace-step](https://fal.ai/models/fal-ai/ace-step) | Commercial use | Apache-2.0 upstream | Usable (re-check weights licence on the day) | [ACE-Step LICENSE](https://github.com/ace-step/ACE-Step/blob/main/LICENSE) |
| [fal-ai/minimax-music/v2](https://fal.ai/models/fal-ai/minimax-music/v2), [cassetteai/music-generator](https://fal.ai/models/cassetteai/music-generator) | Commercial use | Vendor terms add conditions (keep embedded identifiers; unclear game coverage for CassetteAI) | See [audio.md](audio.md) §1.2 | [audio-sources.md](audio-sources.md) |
| [fal-ai/lyria3](https://fal.ai/models/fal-ai/lyria3), [fal-ai/lyria3/pro](https://fal.ai/models/fal-ai/lyria3/pro) | Commercial use | Google Lyria 3 is Preview / Pre-GA; SynthID watermarking | **Not in a shipped game** (Pre-GA scope rule) | [Lyria 3 docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3) |
| [elevenlabs/sound-effects/v3](https://fal.ai/models/elevenlabs/sound-effects/v3) | Commercial use | ElevenCreative Terms, Exhibit 4 (updated 9 Oct 2026): SFX may be incorporated into games where the plan permits commercial use; the Music Terms' Studio Games exclusion doesn't apply to SFX. No standalone resale or sound library | **Usable.** Embed in the game; never ship a standalone SFX library or pack | [ElevenCreative Terms](https://elevenlabs.io/creative-terms) · [ElevenLabs Sound Effects](https://elevenlabs.io/sound-effects) |
| [fal-ai/elevenlabs/sound-effects/v2](https://fal.ai/models/fal-ai/elevenlabs/sound-effects/v2) | Commercial use (Partner API) | Same Exhibit 4 terms as v3 | **Usable** on the same terms; prefer v3 | [ElevenCreative Terms](https://elevenlabs.io/creative-terms) |
| [fal-ai/stable-audio-3/small/sfx/text-to-audio](https://fal.ai/models/fal-ai/stable-audio-3/small/sfx/text-to-audio) | Commercial use | Through fal's hosted endpoint: Stability's ToS/AUP, no revenue test, embedded game use permitted. Self-hosting the Small weights falls under the Community License US $1M cap | **Usable** through the hosted endpoint; don't self-host without checking the cap | [Stable Audio commercial licensing](https://kb.stability.ai/knowledge-base/stable-audio-commerical-and-usage-licensing) · [Core Models](https://stability.ai/core-models) |
| [cassetteai/sound-effects-generator](https://fal.ai/models/cassetteai/sound-effects-generator) | Commercial use | CassetteAI Terms (13 Feb 2023) don't clearly cover games and put redistribution responsibility on the user | **Caution.** Prefer the options above | [CassetteAI Terms](https://cassetteai.com/terms) · [CassetteAI Pro](https://cassetteai.com/pro) |
| [sonilo/v1.1/text-to-sound-effects](https://fal.ai/models/sonilo/v1.1/text-to-sound-effects) | Commercial use | Sonilo Terms (3 Nov 2026) §6.2 reserve "studio games" for Premium or Enterprise; "indie" means under US $200,000 combined revenue and funding in the prior 12 months | **Owner question.** Avoid unless studio-game rights for fal generations are confirmed in writing | [Sonilo Terms](https://sonilo.com/terms) · [Sonilo licensing](https://sonilo.com/licensing) |
| [fal-ai/audio-understanding](https://fal.ai/models/fal-ai/audio-understanding) | Commercial use | — | Review only; produces no asset | fal page |
| fal-ai/kokoro/*, fal-ai/f5-tts (TTS) | catalog `license_type` empty; pages not checked | — | Unverified | fal catalog API |

### Video

| Endpoint (page) | fal badge | Verdict |
| --- | --- | --- |
| [fal-ai/ltx-video](https://fal.ai/models/fal-ai/ltx-video) and fal-ai/ltx-video/image-to-video (LTX Video preview) | **Research only** | **Avoid** |
| fal-ai/minimax/video-01 family, fal-ai/vidu/* | catalog `license_type` empty; pages not checked | Unverified |

Catalog summary on 2026-11-27: every image-to-3D, text-to-3D and 3D-to-3D endpoint in fal's catalog was listed as commercial except `fal-ai/hyper3d/rodin` (empty field; its page shows Commercial use). The only `research` entries in the 3D, image, audio and video categories were `fal-ai/face-to-sticker`, `fal-ai/ltx-video` and `fal-ai/ltx-video/image-to-video`.

## Suno

| Plan when the song was made | Rights | Source |
| --- | --- | --- |
| Pro or Premier (paid) | You own the song and have commercial-use rights, which you keep after cancelling. Commercial use explicitly includes "film, tv, or video games". Suno makes no warranty that copyright vests in the output | [Help: Does Suno own the music I make?](https://help.suno.com/en/articles/2416769) (edited 7 Jan 2026); [Help: paid subscription rights](https://help.suno.com/en/articles/9601665) (edited 3 Sep 2026); [Terms of Service](https://suno.com/terms) (last revised 10 Aug 2026, effective 3 Sep 2026) |
| Free / Basic | Suno owns the song; personal, non-commercial use only; can't be monetised. Free-plan trial downloads carry no commercial rights | [Help: free plan rights](https://help.suno.com/en/articles/9601601) (edited 17 Dec 2025); [Upcoming Changes FAQ](https://help.suno.com/en/articles/13614785) (edited 25 Nov 2026) |
| Free song, then upgrade | **Never gains rights.** "Subscribing to a Pro or Premier plan does not give you retroactive commercial use licensing for the songs made with a free plan by default." (Suno may offer it for specific songs; not guaranteed.) Don't use a later paid Download of a free-plan song | [Help: songs made before subscribing](https://help.suno.com/en/articles/2425729) (edited 17 Dec 2025); [Help: distribution](https://help.suno.com/en/articles/2410177) (edited 17 Dec 2025) |

The audio owner's full Suno ruling, with quotes, is in [audio.md](audio.md) §1.1 and is authoritative. Working rule: create the song on Pro or Premier **and** take a permitted Download while still subscribed. Terms that matter for a game, from the Terms of Service:

- **Permitted Commercial Use** needs a permitted **Download** through Suno's own download channel, within the plan's monthly download allocation (Pro 20, Premier 60 a month per the FAQ). Recording or stream-ripping is prohibited. Rights in a permitted Download are perpetual, even after cancelling.
- Don't remove, alter or obscure Suno's fingerprint, watermark or metadata. Format conversion and editing are allowed "to the extent such use is incidental".
- **Remixes** made with Suno's remix features are joint works and personal, non-commercial only, on every plan.
- You warrant that your inputs (lyrics, uploaded audio) are yours. Suno's help pages warn not to monetise songs that use someone else's lyrics.

Record in the receipt: plan at creation, song id or link (privately), download date and channel, and whether any uploaded audio or lyrics were used.

## Code-generated assets

Code-generated output (offline numpy/SciPy audio renders, procedural textures, scripted meshes) is the project's own. The licence work is about **inputs**:

| Input | Needs |
| --- | --- |
| Samples, loops, impulse responses, soundfonts | Their own licence allowing commercial game use and redistribution inside a platform |
| Fonts rendered into images | Font licence allowing embedding in images or games; Roblox fonts can't be imported (use the Creator Store fonts) |
| HDRIs, photos, scanned textures, noise images | Licence allowing commercial use and modification |
| Code copied into the generator | Its licence; keep notices in the repo if the licence requires it |
| Tools (Blender, ffmpeg, numpy) | Note versions; their licences don't normally attach to output |

Seed every random generator and commit the script, so the asset can be rebuilt and its hash checked.

## Roblox's side (applies to every source)

- Uploading grants Roblox a worldwide, non-exclusive, royalty-free, perpetual, irrevocable, sublicensable and transferable licence, including for promotion and for "developing, improving, or training any AI or machine learning models" (Terms of Use, User Terms 3.2). You must have the right to grant it (3.1).
- Audio adds the [Audio Upload License Agreement](https://en.help.roblox.com/hc/en-us/articles/23359485439124-Audio-Upload-License-Agreement): you warrant you own or have paid for every licence needed (including public performance), Roblox owes no royalties, you must withdraw audio when a licence ends, and you indemnify Roblox.
- So a source licence must allow sublicensing to the platform. Accept these terms only for assets the project originated; anything else needs its own owner decision.
