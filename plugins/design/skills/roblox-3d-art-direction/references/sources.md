# Sources

All verified 2026-11-27 on create.roblox.com (pages last updated 2026-11-24).

- General modeling specifications: per-mesh 20,000-triangle cap, watertight, no N-gons. <https://create.roblox.com/docs/art/modeling/specifications>
- Texture specifications: formats, sizing guidance, 1024² texture-map note, OpenGL normal maps, single UV set, Part/Terrain texel density. <https://create.roblox.com/docs/art/modeling/texture-specifications>
- PBR textures (SurfaceAppearance): maps, AlphaMode, tinting, emissive mask. <https://create.roblox.com/docs/art/modeling/surface-appearance>
- Materials and MaterialVariant. <https://create.roblox.com/docs/parts/materials> · <https://create.roblox.com/docs/reference/engine/classes/MaterialVariant>
- Global lighting, LightingStyle, PrioritizeLightingQuality; Technology deprecated. <https://create.roblox.com/docs/environment/lighting> · <https://create.roblox.com/docs/reference/engine/classes/Lighting> · <https://devforum.roblox.com/t/let-there-be-unified-light-unified-lighting-is-fully-live/3401512>
- Atmosphere. <https://create.roblox.com/docs/environment/atmosphere>
- Post-processing effects, ColorGradingEffect. <https://create.roblox.com/docs/environment/post-processing-effects> · <https://create.roblox.com/docs/reference/engine/classes/ColorGradingEffect>
- Light sources (PointLight, SpotLight, SurfaceLight); range clamp 120 studs. <https://create.roblox.com/docs/effects/light-sources> · <https://create.roblox.com/docs/reference/engine/classes/Lighting>
- Flicker limit: WCAG 2.3.1 Three Flashes or Below Threshold. <https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html>
- Performance: draw calls, instancing, shadows off below quality 4, RenderFidelity, CollisionFidelity, texture memory. <https://create.roblox.com/docs/performance-optimization/improve>
- Instance streaming. <https://create.roblox.com/docs/workspace/streaming>
- MeshPart RenderFidelity distances. <https://create.roblox.com/docs/reference/engine/classes/MeshPart>

These pages describe the engine; they change. Re-read the relevant page before quoting a number in a PR.
