# 3D style guide template (Roblox)

Copy into the owning project and fill in. Keep private briefs in that project.

## Style decision

| Criterion | Stylized low-poly | Stylized PBR | Winner and why |
| --- | --- | --- | --- |
| Mobile readability at phone size, quality 1 | | | |
| Roblox caps (20k tris/mesh, ≤1024² maps) | | | |
| Draw calls and instancing | | | |
| Team capacity (who models, who bakes) | | | |
| AI-generation fit | | | |
| Survives quality < 4 (no shadows) | | | |

## Shape language

Safe shapes / mystery shapes / threat shapes, bevel minimum (studs), proportion scale vs a ~5-stud R15 avatar, silhouette test (recognizable as a flat shape at 64 px tall).

## Texel density

| Tier | px per stud | Map size |
| --- | --- | --- |
| Hero (≤3 per room) | 64 | 1024² |
| Standard | 32 | 512² |
| Small (<5 studs) | 32–48 | 256² |
| Architecture | MaterialVariant tiling (StudsPerTile) | shared |

Use one shared palette atlas for low-poly props so they instance.

## Materials

Max MaterialVariants per place, max full-PBR sets per room, which surfaces may use Neon or emissive, and banned materials for gameplay-critical parts (e.g. Glass, ForceField).

## LOD and collision

RenderFidelity Automatic (Precise only with sign-off); SLIM for distant models when streaming; CollisionFidelity Box/Hull; CastShadow off on parts < 2 studs or far from play.

## Starting budgets (calibrate after first measurement)

On-screen tris, draw calls, unique meshes, unique textures, GraphicsTexture MB, GraphicsMeshParts MB, p95 frame time on reference devices, shadow-casting lights (usually 1), lights in view, live particles.
