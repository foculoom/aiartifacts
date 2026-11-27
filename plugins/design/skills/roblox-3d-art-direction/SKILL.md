---
name: roblox-3d-art-direction
description: Write implementable 3D art direction for a Roblox experience (style choice, palette with measured L*, Lighting/Atmosphere/post-processing values, light plan, value structure, asset triangle and texture budgets) within Roblox's documented engine limits. Use when starting or revising a 3D room or level look; not for avatar/UGC items or for 2D UI.
---

# Roblox 3D art direction

Produce a look document an engineer can type into Studio without guessing: every colour is a hex, every light has numbers, and every asset has a triangle and texture budget. The document is direction, not approval. Generated or purchased art still needs the project owner's explicit yes before import.

## 1. Ground it in the project

1. Read the product's requirements, premise, audience, rating target, and any approved concept art. Record the repo, branch and commit you read.
2. Find the room's real structure in source (sizes in studs, positions of interactables, spawn, enemy paths, phases or time-of-day states). Direction that ignores the graybox gets ignored.
3. Write the **emotional target** in one line, and a **colour script**: one row per gameplay beat, with trigger, dominant and accent colours, share of frame, and emotion.

## 2. Choose a style with reasons

Compare **stylized low-poly** (flat or gradient albedo, few maps) against **stylized PBR** (painted albedo plus normal, roughness and metalness) on: mobile readability, Roblox caps, draw-call instancing, team capacity, AI-generation fit, and how the look survives graphics quality below 4 (no shadows there). Most small teams shipping to phones should pick low-poly with "light PBR" and keep full PBR for 1–3 hero assets per room. See [style-guide template](references/style-guide-template.md).

## 3. Respect the engine (verify each time; see [sources](references/sources.md))

- One mesh ≤ **20,000 triangles** (import cap). One material per mesh.
- SurfaceAppearance maps: ColorMap, NormalMap (**OpenGL tangent space**), RoughnessMap, MetalnessMap, EmissiveMask. Work at ≤ **1024²**: the docs cite 1024 for texture maps even though uploads up to 4096 are accepted. Size maps to object size (≈256² for 5 studs, 512² for 10, 1024² for 20).
- MaterialVariant for Parts and Terrain; SurfaceAppearance for MeshParts.
- `Lighting.Technology` is **deprecated**. Set `LightingStyle` (Realistic/Soft) and `PrioritizeLightingQuality` instead (old Future = Realistic + true). Both are Studio-only.
- Local light Range is clamped to 120 studs. Brightness doesn't extend range. Shadows are expensive and are disabled below graphics quality 4.
- RenderFidelity Automatic (Highest < 250 studs). Avoid Precise. CollisionFidelity Box or Hull for decoration.
- Instancing needs identical MeshContent and identical SurfaceAppearance. Upload each mesh once, then duplicate.

## 4. Specify the look

1. **Palette table**: role, hex, CIE L\*, where it's used. Compute L\* (sRGB D65) rather than guessing. Reserve saturated warm or bright hues for things the player should notice.
2. **Lighting service per state**: LightingStyle, PrioritizeLightingQuality, Ambient, OutdoorAmbient, ColorShift_Top/Bottom, Brightness, ExposureCompensation, EnvironmentDiffuseScale, EnvironmentSpecularScale, GlobalShadows, ShadowSoftness, ClockTime, GeographicLatitude. Add tween durations between states.
3. **Atmosphere** (Density, Offset, Color, Decay, Glare, Haze) and **Sky** per state. Keep Density low enough that the far wall of the play space still reads.
4. **Post-processing** per state: ColorGradingEffect preset, Bloom (set Threshold so only emissive/Neon blooms), ColorCorrection, SunRays. DepthOfField off during gameplay unless the design needs it; Blur only behind full-screen UI.
5. **Light plan**: key, fill (often ambient only), one hero practical as the **only** shadow caster, practicals without shadows. Give Color, Brightness, Range, Angle and Shadows for each, plus caps on enabled lights and lights in view.
6. **Value structure**: on-screen L\* bands (deep, environment low/mid, light pools, interactive) and a frame distribution target (% below L\* 10 and 20, p50).
7. **Gameplay readability rule**: interactables get a minimum on-screen L\* and a minimum dL against a ring around them, on desktop and on a phone at low quality; hue cues always come with a shape or pulse cue.
8. **Asset list**: count, unique meshes, triangles each, map size, PBR or atlas, collision. Total the room.
9. **Performance budget**: on-screen triangles, draw calls, GraphicsTexture and GraphicsMeshParts memory, p95 frame time on a reference phone, streaming settings. Label them starting points until the first measurement.
10. **Distinctness**: a table comparing this product with sibling products. Don't reuse another product's signature colours without a stated reason.

## 5. Close

List what needs the owner's yes (palette, spend, each generated asset, skybox). Hand off to the [3D visual gate](../3d-visual-gate/SKILL.md) for PR review, and to [fal image-to-3D](../fal-image-to-3d/SKILL.md) if assets will be generated.
