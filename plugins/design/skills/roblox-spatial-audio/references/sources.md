# Sources (verified 2026-11-27)

- Roblox, "Audio objects": https://create.roblox.com/docs/audio/objects. Covers the 2D/3D graphs, ListenerLocation, and the note that Sound/SoundGroup/SoundEffect are discouraged.
- Roblox, "Audio assets": https://create.roblox.com/docs/audio/assets. Covers formats, the 20 MB / 7 min / 48 kHz limits, the 2,000 / 100 imports per 30 days, transcoding, moderation, and song vs sound-effect visibility.
- Roblox, "Asset privacy": https://create.roblox.com/docs/projects/assets/privacy. Covers grants to friends, groups and experiences. Audio keeps its own defaults.
- Roblox, "Audio effects": https://create.roblox.com/docs/audio/effects
- Roblox class reference: AudioEmitter, AudioListener, AudioPlayer, AudioFader, AudioAnalyzer, AudioReverb, AudioCompressor (Input and Sidechain pins), AudioLimiter, AudioEqualizer, Wire, SoundService, Sound. Each is at https://create.roblox.com/docs/reference/engine/classes/<Name>
- Roblox enums: DistanceAttenuationMode (https://create.roblox.com/docs/reference/engine/enums/DistanceAttenuationMode), ListenerLocation (https://create.roblox.com/docs/reference/engine/enums/ListenerLocation), RollOffMode (https://create.roblox.com/docs/reference/engine/enums/RollOffMode).
- Roblox, AudioStreamWriter: https://create.roblox.com/docs/reference/engine/classes/AudioStreamWriter. Studio-only; not usable in Team Create.
- Roblox DevForum, Release Notes for 747 (Nov 10, 2026), staff reply on page 3: https://devforum.roblox.com/t/release-notes-for-747/4985911. The flag is disabled and the API is not broadly available.
- Roblox DevForum, staff reply on concurrent audio files (Jan 20, 2025): https://devforum.roblox.com/t/new-audio-api-features-directional-audio-audiolimiter-and-more/3282100?page=4. A 400-file cap; emitters are not counted.
- Roblox DevForum, staff reply on mobile voice counts (Oct 29, 2025): https://devforum.roblox.com/t/new-audio-api-beta-elevate-sound-and-voice-in-your-experiences/2848873?page=28
- Roblox, "Sound design" (Beyond the Dark): https://create.roblox.com/docs/resources/beyond-the-dark/sound-design. Covers a 2D bed plus spot ambiences, coprime loop layering, and sidechain ducking.
- Roblox, "Design dark soundscapes" (Mystery of Duvall Drive): https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/design-dark-soundscapes

The attenuation table, reverb ranges and ducking numbers are starting points chosen by the author, not Roblox defaults.
