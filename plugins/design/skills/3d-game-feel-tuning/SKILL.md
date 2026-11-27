---
name: 3d-game-feel-tuning
description: Tune and measure 3D camera feel (follow damping, zoom and occlusion, FOV kicks, rotational shake, cinematic hand-offs, reduced motion) and character movement feel (speed, acceleration, jump arc, coyote time, input buffering, landing) in Roblox, with numeric targets and Studio checks. Use when designing or changing how a 3D Roblox game's camera or character feels; not for audio wiring (use roblox-spatial-audio) or clip loudness (use audio-pr-proof-of-work).
---

# 3D game feel tuning (Roblox)

Feel is a set of numbers you can measure. Write a target for each one, tune it in Studio, and record what you measured. Roblox facts were checked on 2026-11-27 (see `references/sources.md`). The rest are starting points to tune from.

## 1. Start from the engine defaults
- **Camera.** Classic third person, `FieldOfView` 70 (vertical, clamped 1–120). Zoom range comes from `StarterPlayer.CameraMinZoomDistance` / `CameraMaxZoomDistance`. `DevCameraOcclusionMode` is either **Zoom** (pulls in for parts with Transparency < 0.25) or **Invisicam** (fades parts with Transparency < 0.75).
- **Humanoid.**
  - `WalkSpeed` 16 studs/s.
  - `JumpHeight` 7.2 studs, or `JumpPower` 50. `UseJumpPower` defaults to true.
  - `MaxSlopeAngle` 89°.
  - `Workspace.Gravity` 196.2 studs/s². A jump reaches its apex in √(2h/g), so 7.2 studs means about 0.27 s up and 0.54 s total airtime.
- **Humanoid has no acceleration setting.** For real acceleration and deceleration curves, use `ControllerManager` + `GroundController`, which have `AccelerationTime`, `DecelerationTime`, `Friction` and `TurnSpeedFactor`. The **Character Controller Library** (CCL) is another route, but it is beta; don't build on it without the project's agreement. A pilot or graybox can keep the default Humanoid and add coyote time and a jump buffer client-side (section 3).

## 2. Camera targets (starting points)
| Element | Target | Notes |
|---|---|---|
| Follow damping (scripted cameras) | τ 60–120 ms position, 40–80 ms rotation | Use `alpha = 1 - math.exp(-dt / tau)` so it behaves the same at every frame rate. |
| Interior zoom | min 6, max 15–18 studs | Keep max zoom below the ceiling height plus a margin, so the camera can't leave the room. |
| FOV kick | +2° to +4°, in ≤ 150 ms ease-out, back in 300–600 ms | Run at most one kick at a time, and clamp the total. |
| Shake | rotation only; ≤ 1.5° pitch/yaw, ≤ 0.75° roll | Use the trauma model (below), with no shake at idle. |
| Cinematic beat | ≤ 6 s, skippable, control back in ≤ 400 ms | Never pull the camera away while the player is steering. |
| Reduced motion | shake 0, FOV kick 0, cinematic moves become cuts or ≤ 300 ms fades | Read `GuiService.ReducedMotionEnabled`. |

**Shake.** Shake is trauma squared, applied as smooth noise, and rotation only. Translation shake in 3D reads badly and causes sickness.
```lua
local RunService = game:GetService("RunService")
local GuiService = game:GetService("GuiService")
local camera = workspace.CurrentCamera
local trauma, MAX_YAW, MAX_PITCH, MAX_ROLL, DECAY = 0, math.rad(1.5), math.rad(1.5), math.rad(0.75), 1.0
local function addTrauma(amount: number) trauma = math.min(1, trauma + amount) end
RunService:BindToRenderStep("FeelShake", Enum.RenderPriority.Camera.Value + 1, function(dt)
	if trauma <= 0 then return end
	trauma = math.max(0, trauma - DECAY * dt)
	if GuiService.ReducedMotionEnabled then return end
	local s, t = trauma * trauma, os.clock() * 18
	camera.CFrame = camera.CFrame * CFrame.Angles(
		MAX_PITCH * s * math.noise(t, 1.1), MAX_YAW * s * math.noise(t, 2.3), MAX_ROLL * s * math.noise(t, 3.7))
end)
```
Bind the shake after the default camera has updated (priority Camera + 1). Check in Studio that the default camera doesn't build drift from the offset over 60 s of shaking.

**Occlusion in small rooms.** Invisicam can expose what is outside the room. Prefer Zoom with a solid ceiling, or a scripted collision cast (`workspace:Spherecast` from the focus point to the desired position, with radius 0.5–1 stud) that pulls in quickly (≤ 50 ms) and eases out slowly (250–400 ms).

## 3. Movement targets (starting points)
| Element | Target | How in Roblox |
|---|---|---|
| Walk speed | project spec (default 16) | `Humanoid.WalkSpeed` |
| Accel / decel | 0.10–0.15 s / 0.06–0.10 s | `GroundController.AccelerationTime` / `DecelerationTime` (ControllerManager) |
| Jump height | fit to level geometry; ≥ 1 stud of head clearance in rooms | `JumpHeight` with `UseJumpPower = false` |
| Coyote time | 80–120 ms | client script (below), or CCL `TimedLabels` |
| Jump buffer | 80–120 ms | client script (below) |
| Landing cue | falls ≥ 4 studs: sound + dust; camera dip ≤ 0.3 studs over ≤ 150 ms (none under reduced motion) | `Humanoid.StateChanged` → Landed |

**Coyote time and buffer with a default Humanoid.** This is a client-side sketch, since the client owns its character's physics. Check it in Studio on your engine version.
```lua
local UserInputService = game:GetService("UserInputService")
local COYOTE, BUFFER = 0.10, 0.10
local humanoid: Humanoid = (game.Players.LocalPlayer.Character or game.Players.LocalPlayer.CharacterAdded:Wait()):WaitForChild("Humanoid")
local lastGrounded, jumpPressedAt, usedCoyote = os.clock(), -math.huge, false
game:GetService("RunService").Heartbeat:Connect(function()
	if humanoid.FloorMaterial ~= Enum.Material.Air then lastGrounded, usedCoyote = os.clock(), false end
end)
UserInputService.JumpRequest:Connect(function()
	jumpPressedAt = os.clock()
	local state = humanoid:GetState()
	if state == Enum.HumanoidStateType.Freefall and not usedCoyote and os.clock() - lastGrounded <= COYOTE then
		usedCoyote = true
		humanoid:ChangeState(Enum.HumanoidStateType.Jumping)
	end
end)
humanoid.StateChanged:Connect(function(_, new)
	if new == Enum.HumanoidStateType.Landed and os.clock() - jumpPressedAt <= BUFFER then
		humanoid.Jump = true
	end
	if new == Enum.HumanoidStateType.Jumping then usedCoyote = true end
end)
```

## 4. Process
1. Write the feel brief in one line per verb: "walk feels careful but never sluggish", "the door feels heavy".
2. Turn each line into numbers using the tables above.
3. Tune in Play Solo with a debug overlay that prints velocity, state, FOV, trauma and camera distance.
4. Measure with logged data, not by eye. Report time to 90% speed, airtime, and the coyote and buffer hit rates (10 tries each).
5. Test on Device Simulator (phone, gamepad). Analog sticks scale speed below WalkSpeed, so check full deflection.
6. Turn on reduced motion and repeat. The game must stay fully playable.
7. Record the results in the 3d-feel-proof-of-work table.

## 5. Comfort rules
- Never move or rotate the camera without player input during free control, except a skippable cinematic.
- No head bob by default. If you add it, give it an intensity slider with 0 as a choice.
- Lighting flicker stays at ≤ 3 flashes per second.
- FOV stays between 60 and 90 in gameplay unless the player picks another value.
