# Sources (verified 2026-11-27)

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

The damping, FOV, shake, acceleration and landing numbers are the author's starting points, not Roblox defaults.
