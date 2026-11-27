# Sources (verified 2026-11-27)

Camera, movement and accessibility sources come first; audio sources follow.

- Roblox, "Customize the camera": https://create.roblox.com/docs/workspace/camera. Covers zoom, occlusion modes, movement modes and Scriptable.
- Roblox, Camera class: https://create.roblox.com/docs/reference/engine/classes/Camera. FieldOfView is vertical, 1–120, default 70.
- Roblox, Humanoid class: https://create.roblox.com/docs/reference/engine/classes/Humanoid. Covers WalkSpeed 16, JumpPower 50, JumpHeight 7.2, UseJumpPower and MaxSlopeAngle 89.
- Roblox, Workspace class: https://create.roblox.com/docs/reference/engine/classes/Workspace. Gravity is 196.2 studs/s².
- Roblox, GroundController and ControllerManager: https://create.roblox.com/docs/reference/engine/classes/GroundController and https://create.roblox.com/docs/reference/engine/classes/ControllerManager
- Roblox, Character Controller Library (beta): https://create.roblox.com/docs/characters/character-controller-library and https://create.roblox.com/docs/characters/character-controller-library/quick-start
- Roblox, Accessibility guidelines (ReducedMotionEnabled, sound non-reliance, volume groups): https://create.roblox.com/docs/production/publishing/accessibility
- Squirrel Eiserloh, "Math for Game Programmers: Juicing Your Cameras With Math", GDC 2016: http://www.mathforgameprogrammers.com/gdc2016/GDC2016_Eiserloh_Squirrel_JuicingYourCameras.pdf. Covers trauma², Perlin noise, and rotation-only shake in 3D.
- Microsoft, Xbox Accessibility Guideline 117: https://learn.microsoft.com/xbox/accessibility/xbox-accessibility-guidelines/117
- Game Accessibility Guidelines, camera/controller movement difference: https://gameaccessibilityguidelines.com/avoid-or-provide-option-to-disable-any-difference-between-controller-movement-and-camera-movement/
- W3C, WCAG 2.2 SC 2.3.1, Three Flashes or Below Threshold: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html
- Celeste source, `JumpGraceTime = 0.1f`: https://github.com/NoelFB/Celeste/blob/master/Source/Player/Player.cs. Input buffering is 4 frames: https://celeste.ink/wiki/Tech

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

The numeric targets in the checklist (damping, FOV, shake, acceleration, coyote and buffer windows, attenuation tolerances, duck depth) are the author's starting points, not Roblox defaults. Projects should replace them with their own.
