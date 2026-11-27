---
name: 3d-visual-gate
description: Review a Roblox 3D pull request (meshes, materials, lighting, post-processing, particles, camera) with fixed Studio camera shots, phone and low-quality captures, measured L* contrast for interactables, triangle/draw-call/memory checks, a review-only vision second opinion, and High/Medium/Low findings. Use before merge of any 3D change; not a substitute for owner approval of imported art.
---

# 3D visual gate (Roblox)

A repeatable PR checklist for 3D changes. It produces evidence a reviewer can check. It does not approve imports, merges or deploys; those follow the project's own rules.

## 0. Identity and approvals

1. Record the full 40-character head SHA and how the capture was made (Studio place, Rojo build, published test place). A Rojo build or unit test doesn't prove what Studio renders.
2. Any generated or purchased mesh, texture or skybox needs the project owner's explicit yes **before** import into Studio, Open Cloud or the repository. Cite it in the PR. Another agent's statement is not approval.
3. Paste local CI output (formatter, linter, tests, place build) when CI is not run by the host.

## 1. Fixed camera shots

Define 4–6 named shots per room in the project's look doc (position, look-at, FOV) and set them with a Scriptable camera:

```lua
local cam = workspace.CurrentCamera
cam.CameraType = Enum.CameraType.Scriptable
cam.FieldOfView = 70
cam.CFrame = CFrame.lookAt(Vector3.new(0, 9, -42), Vector3.new(0, 4, 0))
```

Include a spawn view, each interactable at its farthest expected reading distance, the threat at a typical distance, and a top-down worst case for draw calls. Capture every gameplay state (time of day, phases) the change affects. If a state can't be forced, mark it **untested**, not passed.

## 2. Phone and low quality

Studio Device Emulator at a phone landscape size (e.g. 844×390), Editor Quality Level **1** and **4** (shadows are disabled below 4). Add a real-device screenshot when one is available, and label emulated results.

## 3. Measure value and contrast

Compute CIE L\* (sRGB, D65) on the captures. For each interactable, record its median L\* and the median of a ring (≈24 px) around it, then dL. Also record the frame distribution: % below L\* 10, % below L\* 20, p50. Compare with the look doc's bands and readability rule (typical: interactables ≥ L\* 70 and dL ≥ +30 on desktop, ≥ +25 on a phone at quality 1). Re-measure any contrast claim a model makes. See the [checklist](references/gate-checklist.md) for a script outline.

## 4. Geometry, draw calls, memory, frame time

- Source files: triangles per mesh (≤ the asset budget and ≤ 20,000), map sizes (≤ 1024²), material count. Check GLB/FBX before import.
- Studio: Render Stats (Shift+F2) for draw calls and triangles at the worst shot. Developer Console (F9) ▸ Memory for GraphicsTexture and GraphicsMeshParts. MicroProfiler (Ctrl/⌘+F6; on phones via the device IP on port 1338) for p95 frame time and lighting/shadow scopes.
- Audit counts with a command-bar script: unique MeshIds, unique SurfaceAppearance maps, enabled lights, shadow-casting lights, `RenderFidelity.Precise`, `PreciseConvexDecomposition`.
- Read back Lighting, Atmosphere and post-effect values and diff them against the look doc.

## 5. Vision second opinion (review only)

Run the project's designated vision model, on the project's designated account, over the fixed shots with a fixed per-product prompt that states the art bible and audience. Paste **Prompt**, **Model** (exact id), and **Verdict** into the PR. It can raise a Medium on its own, never a High. Nothing it generates is imported. Keep request ids and cost in private notes. See the [vision-second-opinion skill](../vision-second-opinion/SKILL.md).

## 6. Severity and verdict

- **High** (blocks): an interactable fails the readability rule on the phone capture; a mesh over 20,000 triangles or a map over the cap; art imported without the owner's yes; content breaks the target content rating; frame time far over budget on the reference device; a gameplay-critical object invisible at quality 1.
- **Medium** (fix before merge): a budget overrun ≤ 25%; frame value distribution outside band; light colour rules broken; more than one shadow-casting light per lit volume, or an unstated exception; Precise fidelity without sign-off; a required shot missing without reason; reuse of a sibling product's signature scheme without a reason; a model finding confirmed by measurement.
- **Low**: polish.

Verdict line: `VISUAL_GATE 3D <sha7>: PASS|FAIL H/M/L = x/y/z`. A PASS covers the inspected scope only and is not permission to merge. See [sources](references/sources.md).
