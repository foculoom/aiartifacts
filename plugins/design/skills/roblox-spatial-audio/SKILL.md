---
name: roblox-spatial-audio
description: Design, wire, and verify positional and ambient audio in Roblox experiences with the Audio API (AudioPlayer, AudioEmitter, AudioListener, Wire, faders and effects), including attenuation curves, buses, reverb, ducking, voice budgets, and the asset upload path for code-generated audio. Use when adding or changing sound in a 3D Roblox scene; not for measuring clip loudness (use audio-pr-proof-of-work) or for camera and movement feel (use 3d-game-feel-tuning).
---

# Roblox spatial audio

Use this skill to plan and build 3D sound in a Roblox scene, and to check it. Facts here were checked against create.roblox.com on 2026-11-27; see `references/sources.md`. Re-check anything marked *beta* or *pending* before relying on it.

## 1. Know the hard limits first
- **No runtime sample synthesis in shipped games.** `AudioStreamWriter` (Luau buffers → audio stream, 48 kHz Float32) is Studio-only, does not work in Team Create, and is pending as of release 747. Every sound a player hears comes from an uploaded audio asset or from `AudioTextToSpeech`.
- **Code-generated audio is therefore an offline render that you upload.** Generate it in code (for example Python/numpy), measure it, then import it. Write down how your project's approval rules treat these uploads. If the rules don't say, ask the owner rather than assume. Either way, keep the measured proof in the pull request.
- **Import rules.**
  - Format: `.mp3`, `.ogg`, `.wav` or `.flac`, one track.
  - Each file under 20 MB and under 7 minutes, sample rate ≤ 48 kHz, channels mono, stereo, 3.0 or 5.1.
  - Allowance: 2,000 imports per 30 days if ID-verified, 100 if not.
  - Every import is transcoded and moderated. Until it passes, only the uploader can hear it.
- **Privacy.** A new audio asset is usable only by its creator until they grant access. Upload under the group that owns the experience, or grant the experience permission in Creator Dashboard. Otherwise it plays in your Studio session and nowhere else.
- **Voices.** Staff guidance caps concurrent playing audio files at about 400 per client, and AudioPlayers count toward it while AudioEmitters do not. 30 is comfortable; 100 is a conservative mobile bound. One AudioPlayer can feed many emitters.
- **`SoundService.AmbientReverb` and `VolumetricAudio` affect only legacy `Sound`.** In the Audio API, use `AudioReverb`, and use several emitters for a large source.

## 2. Choose the system
Prefer the **Audio API**. Roblox now discourages `Sound`, `SoundGroup` and `SoundEffect`. Keep legacy `Sound` only in a project that already uses it, and don't mix the two for one category, because their reverb and volume paths differ.

## 3. Wire the graph
- **2D** (beds, music, UI): `AudioPlayer → Wire → AudioDeviceOutput`.
- **3D**: `AudioPlayer → Wire → AudioEmitter` (parented to a Part or Attachment), then `AudioListener → Wire → AudioDeviceOutput`.
- **Listener.** For third person, set `SoundService.DefaultListenerLocation = Character`: you hear from the character's position, oriented with the camera. Use `None` when you build listeners yourself (see the buses below).

```lua
local function wire(source: Instance, target: Instance, targetPin: string?)
	local w = Instance.new("Wire")
	w.SourceInstance = source
	w.TargetInstance = target
	if targetPin then w.TargetName = targetPin end -- e.g. "Sidechain"
	w.Parent = target
	return w
end

-- One positional source. curve maps studs -> linear volume (up to 400 keys).
local function addEmitter(host: Instance, assetId: string, curve: {[number]: number}, looping: boolean)
	local player = Instance.new("AudioPlayer")
	player.Asset = assetId -- "rbxassetid://<id>"
	player.Looping = looping
	player.Parent = host
	local emitter = Instance.new("AudioEmitter")
	emitter:SetDistanceAttenuation(curve)
	emitter.Parent = host
	wire(player, emitter)
	return player, emitter
end
```

## 4. Attenuation
- Write curves in studs, and design them from the room's real dimensions. The preset `DistanceAttenuationBounds` default is `[4, 10000]`, which is far too long for interiors.
- Starting points *(tune by ear, then measure)*:

| Source type | Full volume to | Half (≈ −6 dB) at | Silent at |
|---|---|---|---|
| Small object (lantern, switch) | 3 | 10 | 30 |
| Room feature (brazier, fountain) | 6 | 18 | 40 |
| Doorway draft / spot ambience | 4 | 14 | 36 |
| Threat telegraph (enemy hum) | 8 | 20 | 40 |
| Distant landmark (bell tower) | 20 | 80 | 200 |

- Put the "silent at" distance at or inside the point where the source stops mattering to play. Out-of-range sources then cost nothing and don't leak through walls.
- If the sound must not carry through walls, enable acoustic simulation, or add a zone check that lowers `AudioPlayer.Volume` when the listener is in another room.
- For directional sources (a horn, a mouth), use `SetAngleAttenuation`.

## 5. Buses and player volume settings
- A shared `AudioFader` placed before several emitters would merge their sources, so don't put faders there. For per-category volume on 3D sound, use **one listener per category**:
  - Give each category's emitters an `AudioInteractionGroup` (for example `"Ambience"` or `"SFX"`).
  - Create one `AudioListener` per group on the character, each with the matching group.
  - Wire each listener → its category `AudioFader` → `AudioDeviceOutput`.
- 2D players wire straight into their category fader.
- Expose each fader's `Volume` (0–10, linear; 1 = unity) in Settings. Minimum categories: Ambience, SFX, Pings/UI, Music.
- *Check this in Studio for your engine version:* each extra listener multiplies spatialisation work. Keep the categories to 3–5.

## 6. Reverb, ducking, variation
- **Reverb.** Put an `AudioReverb` on the listener path per room type. A small stone room is roughly DecayTime 1.2–1.8 s and WetLevel −16 to −10 dB. Crossfade the wet level over ≥ 250 ms on room entry by tweening the property.
- **Ducking.** Use an `AudioCompressor` on the ambience bus, fed by a second Wire from the SFX fader into its `Sidechain` pin. Interaction cues should duck by 3–6 dB, attack 10–30 ms, release 300–600 ms.
- **Variation without synthesis:**
  - Upload 2–4 variants per frequent one-shot.
  - Jitter `PlaybackSpeed` by ±3–5%.
  - Randomise intervals for sparse one-shots (drips, creaks).
  - Layer loops of coprime lengths: 12 s and 17 s repeat only every 204 s.
  - Schedule tight sequences with `AudioPlayer:Play(SoundService:GetMixerTime() + t)`.
- **Threat telegraphs for young or mild-rated audiences.** Let the sound swell in (attack ≥ 500 ms), with no stinger and no sudden loud hit. Pair it with a steady visual cue that does not flash. Silence (stopping the small ambient one-shots) builds tension without startling.
- **Mix guardrail.** A cue with a sharp attack (10–90% rise < 10 ms) should not sit more than your project's limit above the bed, for example 6 dB. Check where the player normally stands, not only on the raw file.

## 7. Asset pipeline for code-generated audio
1. Render from a committed script with a fixed seed. Use 48 kHz; mono for positional sources, stereo for 2D beds.
2. Measure with audio-pr-proof-of-work: LUFS-I, true peak, loop seams. Also measure mono cues as dual-mono (the same signal on both channels), since an emitter feeds both ears.
3. Check the upload preconditions: the project's approval rule for code-generated audio, the group that will own the asset, and the owner's acceptance of the platform's audio upload licence terms. If any of these is missing, stop before uploading.
4. Upload under the owning group (Asset Manager, Creator Dashboard, or Open Cloud `POST /assets/v1/assets` with an API key held by the owner). Record the asset ID, owner, privacy grants and moderation status.
5. Preload the assets the scene needs before it starts. Wait for `AudioPlayer.IsReady`, or play optimistically and accept a short delay on the first play.

## 8. Verify (Studio)
- In Play Solo, read `AudioEmitter:GetAudibilityFor(listener)` at min, mid and max distance and 5 studs past max. Compare with your curve.
- `AudioAnalyzer.PeakLevel` / `RmsLevel` give client meters. They always read 0 on the server.
- Count the peak number of playing AudioPlayers against the budget.
- Mute everything and complete the scene. Every gameplay-relevant sound needs a visual twin: a caption with direction, an icon, or a light pulse.
- In Server & Clients with 2+ players, other players' cues should come from their positions with no doubled playback.
- Check that no Studio-only API ships: `rg "AudioStreamWriter|AudioStreamReader" src`.
