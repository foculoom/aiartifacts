---
name: roblox-rojo-headless-build-test
description: Build and test a Roblox project from Luau source on a Linux box with no Roblox Studio, using Rojo, Lune, TestEZ, Selene and StyLua, including a round-trip check of 3D Instances in the built place file. Use when a Roblox repo must be verified headlessly; not for publishing or Studio playtests.
---

# Roblox headless build and test (Rojo + Lune)

> Verified on 2026-11-27 (America/Los_Angeles) on a CPU-only Linux box (Debian 13, 8 vCPU, no GPU) with Rojo 7.7.1, Lune 0.11.1, Selene 0.32.0, StyLua 2.6.0, Wally 0.3.2 and TestEZ 0.4.1: lint, 21 unit specs, a Lune-built `.rbxm` mounted by Rojo, and a place round-trip check all passed, and two deliberate reverts (blocked doorway in the data, dropped `Anchored` in the builder) each made the run exit non-zero. Nothing in that run exercised the Roblox engine itself.

Roblox Studio does not run on Linux. Rojo and Lune do, so you can lint, unit-test, build a `.rbxl`, and inspect the 3D Instances inside it without Studio, an account, or a GPU.

## What this proves, and what it does not
- Proves: Luau lints and formats; pure-logic specs pass; the Rojo project builds; the built place contains the Instances you expect with the right properties.
- Does not prove: physics, Humanoid movement, replication, rendering, lighting, or device behaviour. Say so in every PR. Those need a Studio Server & Clients run (Windows/macOS) or the Open Cloud Luau Execution API, which needs an API key from the experience owner and still does not run physics.

## Install (no root)
1. Pin tools in `rokit.toml` (or `aftman.toml`). `rokit install` calls the GitHub API and can hit unauthenticated rate limits (HTTP 403). Fallback: download each pinned release zip from `https://github.com/<owner>/<repo>/releases/download/<tag>/<asset>` into a local `tools/bin` and put it first on `PATH`. Check versions match the pins.
2. `wally install` for TestEZ (dev dependency).

## Run
```bash
stylua --check src tests tools
selene src tests                       # std = "roblox+testez"
lune run tools/run-tests.luau          # TestEZ via virtual ModuleScript nodes
lune run tools/build-model.luau        # optional: build Instances with @lune/roblox -> .rbxm
rojo build default.project.json -o build/place.rbxl
lune run tools/check-place.luau build/place.rbxl
```

## Pattern for 3D content
1. Describe geometry as plain data (parts with name, role, position, size, colour, material, anchored, collide; markers for spawn points and pickups).
2. Write pure rules over that data: part budget, all anchored, inside bounds, no overlapping collidable parts, doorways clear, and a grid flood fill from the entry marker proving every marker is reachable with a player-sized box.
3. Write a builder that takes an injected API table (`Instance`, `Vector3`, `CFrame`, `Color3`, `Enum`) so it runs both in Studio and in Lune (`require("@lune/roblox")`). In Lune, set `CFrame`, not `Position`.
4. In Lune, build the model, `roblox.serializeModel({ model })` to `.rbxm`, and mount it in `default.project.json` (`"Workspace": { "$className": "Workspace", "Room": { "$path": "build/Room.rbxm" } }`).
5. After `rojo build`, `roblox.deserializePlace(fs.readFile(path))`, find the model in Workspace, rebuild the data from the real Instances, and re-run the same rules. This catches builder bugs that pure-data tests miss.

## Proof of work
- Paste the exact commands, versions, pass/fail counts and the place file SHA-256.
- Include one deliberate-revert proof: break the data (e.g. block the doorway) and break the builder (e.g. drop `Anchored`), show CI exits non-zero, restore, show green.
- Keep build outputs out of git (`build/`, `*.rbxl`, `*.rbxm`).

## Gates
- Publishing a place, creating Open Cloud keys, or uploading assets needs the experience owner's explicit approval and their account. Never put cookies or API keys in a repo or PR.
