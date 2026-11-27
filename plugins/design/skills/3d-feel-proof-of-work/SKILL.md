---
name: 3d-feel-proof-of-work
description: Record measured camera, movement, spatial-audio and accessibility checks on pull requests that change how a 3D Roblox scene feels, with targets and a PR table. Use before opening or updating such a PR, next to audio-pr-proof-of-work; not for tuning itself (use 3d-game-feel-tuning) or clip loudness.
---

# 3D feel proof of work (Roblox)

Run this on every PR that changes the camera, character movement, or spatial audio in a 3D Roblox game. It sits beside **audio-pr-proof-of-work**: that skill covers the clips themselves (LUFS, true peak, loop wraps, second opinion), and this one covers how they behave in 3D space. Paste the results into the PR body under **3D feel checks**, and keep them short.

The numbers below are **starting targets**. Where the project has its own targets, write the project's number next to each measurement. A Rojo build or unit tests do not count as Studio verification, so say which checks you actually ran in Studio.

## Checklist

1. **Scene and build.** Name the place file or Rojo build, the commit, and the room or scene tested. List the devices you tested: Studio PC, Device Simulator (phone, tablet, gamepad), and real hardware if any.

2. **Camera.** Measure in Play Solo, using a debug overlay script that prints the values.
   - **Follow and zoom.** Player zoom stays inside the project's range (for example 6–18 studs in a small interior). In rooms with a ceiling, the camera never ends up inside geometry. Check by walking into every corner and every wall at max zoom; look for no clipping and no view through walls.
   - **Occlusion mode.** Write down Zoom or Invisicam and why. In small rooms with thin walls, Invisicam can reveal what is outside the room, so check for this.
   - **Scripted damping, if any.** Use a critically damped spring or exponential smoothing that does not depend on frame rate (`1 - exp(-dt / τ)`, τ ≈ 60–120 ms for position). Measure the time to 90% after a 90° stick turn at 30, 60 and 144 fps (MaxFrameRate or the Studio fps cap). Results must agree within 15 ms.
   - **FOV kicks.** Keep each kick ≤ +4° (default FOV 70, clamp 1–120). Ease out over ≤ 150 ms and return over 300–600 ms. Allow no more than one stacked kick at a time.
   - **Shake.** Rotation only. Use the trauma model (shake = trauma², with linear decay ≤ 1.0 s from full to zero) and smooth noise, not per-frame random values. Peak shake is ≤ 1.5° pitch/yaw and ≤ 0.75° roll for gameplay events. Ambient or idle shake is 0.
   - **Cinematic vs gameplay.** A cinematic camera (Scriptable) returns control within ≤ 400 ms of its end. It never moves the camera while the player is steering, unless it is skippable. Its duration is ≤ 6 s for in-room beats.
   - **Reduced motion.** With `GuiService.ReducedMotionEnabled = true`, FOV kicks and shake are 0, and cinematic moves become cuts or fades (fade ≤ 300 ms). Toggle it in the in-game Settings and record before and after.
   - **Flashing.** Lighting flicker stays at ≤ 3 flashes per second (WCAG 2.3.1).

3. **Movement.** Measure with a script that logs `HumanoidRootPart.AssemblyLinearVelocity` and Humanoid state changes.
   - **Ground speed.** WalkSpeed matches the spec (Roblox default 16 studs/s). Report the time to 90% of WalkSpeed and the time to stop. A default Humanoid is near-instant. With `GroundController`, use the project's `AccelerationTime` / `DecelerationTime` (for example 0.10–0.15 s up and 0.06–0.10 s down for a responsive feel). The measured values must be within 20 ms of the setting.
   - **Jump.** Report the jump height in studs and the airtime. At Gravity 196.2, JumpHeight 7.2 gives about 0.54 s of airtime. In interiors, head clearance at the apex must be ≥ 1 stud below the ceiling.
   - **Coyote time.** If implemented, a jump pressed ≤ 100 ms after walking off a ledge still fires, and one pressed at ≥ 150 ms does not. Test 10 tries at each timing.
   - **Jump buffer.** If implemented, a jump pressed ≤ 100 ms before landing fires on touchdown. Test 10 tries.
   - **Landing.** A landing cue (sound, dust, or a camera dip of ≤ 0.3 studs over ≤ 150 ms) fires only for falls over the project threshold (for example ≥ 4 studs). There is no camera dip under reduced motion.
   - **Slopes, stairs and analog stick.** Check walking on slopes up to `MaxSlopeAngle`, stair steps at the project height, and that gamepad and touch stick ramps reach full speed at full deflection.

4. **Spatial audio.** Use the Audio API unless the project still uses `Sound`, and say which one.
   - **Graph check.** Every 3D source goes `AudioPlayer` → `Wire` → `AudioEmitter`. The listener location is recorded (prefer **Character** for third person). Every bus has an `AudioFader` exposed to a player volume setting: Ambience, SFX, Pings/UI and Music, at minimum.
   - **Attenuation walk test.** For each emitter, read `AudioEmitter:GetAudibilityFor(listener)`, or an `AudioAnalyzer.RmsLevel` on the listener path, at 0, min, ½·max and max studs, plus 5 studs past max. Expect full volume at min, the designed value at mid (±1.5 dB), silence past max, and no steps between samples taken 1 stud apart.
   - **Panning.** With the camera facing away from the source, the source sits behind. With the source 90° left, the left channel leads. Check this on headphones.
   - **Guardrail in place.** At the player's normal standing spot, no new cue is more than 6 dB above the bed if it has a sharp attack (10–90% rise < 10 ms). Measure the max momentary level of the cue against the bed's integrated level, using AudioAnalyzer on the client or an offline render of the mix.
   - **Voice count.** The peak number of concurrent `AudioPlayer`s in the scene stays within the project budget, far under the 400 concurrent-file cap (staff guidance: 30 is fine; 100 is a conservative mobile bound). Count with a script over `GetDescendants()` where `IsPlaying` is true.
   - **Reverb and occlusion.** `SoundService.AmbientReverb` does not affect the Audio API. Record the `AudioReverb` settings per room (DecayTime, WetLevel), or whether acoustic simulation is on. Entering and leaving the room crossfades wet level over ≥ 250 ms with no clicks.
   - **Threat telegraphs.** Threat and warning sounds swell in (10–90% rise ≥ 500 ms), with no startling stinger. Their visual twin does not flash (≤ 3 flashes per second).
   - **Ducking.** For sidechain `AudioCompressor` ducks, record the depth (dB), attack and release. The duck depth is ≤ 6 dB for interaction cues.
   - **Multiplayer.** In Server & Clients with 2 or more players, each player hears another player's interaction cue from that player's position. Server-only playback does not double up.

5. **Accessibility.**
   - Every gameplay-relevant sound has a visual twin: a caption with direction, an icon, or a light pulse. Mute all audio and complete the room.
   - Captions appear within ≤ 100 ms of the sound and stay ≥ 1.5 s. They use the player's `PreferredTextSize`.
   - No meaning depends on stereo position alone. A direction arrow or world icon is the twin.

6. **Usual proof.**
   - Local CI result.
   - Audio asset list with asset IDs, upload owner (group), privacy grants and moderation status. If uploads are waiting on preconditions (owning group, licence acceptance, approval), say so and list the measured local renders instead.
   - Clip checks from audio-pr-proof-of-work.
   - Confirm no Studio-only APIs ship (`rg "AudioStreamWriter|AudioStreamReader" src`).

## PR body template
```
### 3D feel checks
Scene: <room> @ <commit> · Ran in: Studio Play Solo / Server&Clients(2) / Device Sim (phone, gamepad)
| Area | Target | Measured | Pass |
|---|---|---|---|
| Camera zoom / clip | 6–18 studs, no clip | ... | ... |
| FOV kick | ≤ +4°, ≤150 ms in | ... | ... |
| Shake peak | ≤1.5° rot, 0 under RM | ... | ... |
| Accel / decel | 0.12 / 0.08 s ±20 ms | ... | ... |
| Coyote / buffer | 100 / 100 ms (10/10) | ... | ... |
| Emitter <name> | 1.0@min, 0.5@mid, 0@max | ... | ... |
| Guardrail | ≤ +6 dB if sharp | ... | ... |
| Voices peak | ≤ N players | ... | ... |
| Muted completion | yes | ... | ... |
Reduced motion: on/off verified · Studio-only APIs: none
```
