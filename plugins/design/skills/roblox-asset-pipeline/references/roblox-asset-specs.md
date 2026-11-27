# Roblox asset specs and limits

Checked on create.roblox.com on 2026-11-27 (America/Los_Angeles). Each row cites the page it came from; source numbers refer to [sources.md](sources.md). Where two Roblox pages disagree, both figures are shown: plan for the stricter one until Roblox confirms.

## Meshes and models

| Topic | Limit | Source |
| --- | --- | --- |
| Triangles | "Individual meshes can not exceed 20,000 triangles." Avatar items have their own budgets | [R1] |
| Geometry rules | Watertight (no exposed holes or backfaces); no n-gons (quads where possible); no zero thickness | [R1] |
| Rigs | Bones frozen at scale 1 and rotation 0; root at 0,0,0; ≤ 4 influences per vertex; no influences on the root | [R1] |
| Animation | One animation track per `.fbx` export | [R1] |
| Import formats (Studio 3D Importer) | `.fbx`, `.gltf`/`.glb`, `.obj`. FBX and glTF carry hierarchies, basic and PBR textures, cages, rigs and vertex colours; OBJ is a single basic mesh. glTF imports as a Model per mesh with one MeshPart per primitive | [R2] |
| Open Cloud upload | Asset type `Model`: `.fbx`, `.gltf`, `.glb`, `.rbxm`, `.rbxmx`, uploaded **as packages**; ≤ 20 MB per call; only `.fbx` content can be updated later. Asset type `Mesh` accepts only content downloaded from the Asset Delivery API (use the Importer instead) | [R3] |
| Materials | One material per mesh object | [R4] |
| Level of detail | `MeshPart.RenderFidelity`: Automatic (default) lowers detail with distance; Precise always highest (costly); Performance may drop appearance. With streaming, `Model.LevelOfDetail = SLIM` renders a lightweight SLIM mesh at distance | [R12][R13] |
| Collision | `CollisionFidelity` Box or Hull for props; PreciseConvexDecomposition is the most expensive; collision geometry stays in memory even with CanCollide off | [R13] |
| Instancing | Meshes with the same mesh content and identical SurfaceAppearance batch into one draw call; upload each mesh once and duplicate in Studio | [R13] |

## Textures, decals and SurfaceAppearance

| Topic | Limit | Source |
| --- | --- | --- |
| Formats (texture files uploaded separately) | `.png`, `.jpg`, `.tga`, `.bmp` (the Importer also lists `.gif` for images) | [R4][R2] |
| Resolution | "Roblox supports up to 4096×4096 pixel texture resolutions (4K)", and the UV section says "Roblox supports up to 1024×1024 pixel spaces for texture maps". Guidance: 256² for about 5×5-stud objects, 512² for 10×10, 1024² for 20×20. Parts show 1024² per 8×8-stud face; terrain 512² per 8×8 studs | [R4] |
| Open Cloud images | Asset types `Decal` and `Image`: `.png`, `.jpeg`, `.bmp`, `.tga`; "must be smaller than 8000x8000 pixels"; ≤ 20 MB per call; can't be updated. A Decal upload also creates a separate Image asset, and texture properties need that image's id | [R3] |
| SurfaceAppearance maps | Albedo RGB 24-bit; Normal RGB 24-bit, **OpenGL tangent space only**; Roughness, Metalness and Emissive mask single-channel 8-bit greyscale | [R4] |
| UVs | One UV set; 0–1 space; overlaps allowed | [R4] |
| Runtime | SurfaceAppearance properties generally can't be changed by scripts at runtime; `SurfaceAppearance.Color` tint is a free multiplier, so author tintable maps near-white | [R5] |
| Alpha modes | Opaque (ignore alpha), Overlay (reveal MeshPart.Color), Transparency (cut-outs), TintMask (alpha controls tint). Hard cut-outs: MeshPart.Transparency 0; soft gradients: ≥ 0.02. For TintMask keep colour in transparent areas and avoid pre-multiplied alpha | [R5] |
| Texture streaming | On automatically for MeshPart, SurfaceAppearance, Texture, Decal, MaterialVariant, Beam, ParticleEmitter and base materials; prefer individual textures over atlases unless the atlas is on batchable parts; keep near-uniform texel density | [R4] |
| Textures vs decals | A Texture tiles (StudsPerTileU/V, offsets, tweenable); a Decal stretches to the face. Both must follow the Community Rules and Terms of Use | [R6] |

## Audio

The audio owner's section, [audio.md](audio.md) §2, is authoritative for audio (formats, quotas, moderation, privacy grants, upload licence). This table is the cross-check.

| Topic | Limit | Source |
| --- | --- | --- |
| Rights | "You have the legal rights to that audio asset"; follows the Community Rules and Terms of Use | [R7] |
| Format | One track/stream: `.mp3`, `.ogg`, `.wav` or `.flac` | [R7][R3] |
| Size and length | < 20 MB and < 7 minutes | [R7][R3] |
| Sample rate and channels | ≤ 48 kHz; mono, stereo 2.0, 3.0 or 5.1 | [R7] |
| Quota | **Creator Hub / Studio** (Asset Manager, Creator Dashboard): 2,000 free imports per 30 days if ID-verified, 100 if not ("If a daily import limit exists, it's removed and replaced with a simplified monthly limit") [R7]. **Open Cloud** (Assets API): up to 100 uploads per month if ID-verified, 10 total per month if not [R3]. Plan for the lower Open Cloud figure when uploading by API. Whether a group upload counts against the member or the group is undocumented: open until the first upload; record it on the receipt | [R7][R3] |
| Cost | Free within the allowance ("free audio assets") | [R7] |
| Processing | Imports are transcoded (invalid headers or frames are rejected) and moderated | [R7] |
| Privacy | "You are initially the only one who can view and use private audio assets"; grant use to specific friends, groups and experiences. The Asset Privacy setting does not change audio or video defaults | [R7][R8] |
| Song visibility | Uploads are classified as sound effect or song. A song can appear on the game details page if it passes moderation and copyright checks, meets play and age thresholds, has a meaningful title, the uploader is ID-verified and has accepted the Audio Terms. Toggle visibility on the asset's Configure page | [R7] |
| Updating | Audio content can't be updated through Open Cloud | [R3] |

## Video

| Topic | Limit | Source |
| --- | --- | --- |
| Who can upload | 13+ ID-verified users, through the Asset Manager, Creator Dashboard or Open Cloud | [R9][R3] |
| Format | `.mp4` or `.mov`; ≤ 5 minutes; ≤ 4096×2160; < 3.75 GB; alpha ignored | [R9][R3] |
| Cost and quota | **2,000 Robux per video upload**; at most 20 videos a day | [R9][R3] |
| Playback | `VideoFrame` must be parented to a ScreenGui, SurfaceGui or BillboardGui; "a maximum of two videos can play simultaneously". The newer `VideoPlayer` (property `VideoContent`, wired output) drives a `VideoDisplay` inside a GUI container | [R9][R10] |
| Rights | You must have the legal rights; Community Standards and Terms of Use apply | [R9] |

So video is usable, but it costs Robux per upload, needs a 13+ ID-verified uploader, and is limited to two simultaneous streams. Treat every video as a spend decision.

## Ownership, privacy and upload paths

| Topic | Rule | Source |
| --- | --- | --- |
| Moderation first | Imported assets must pass a moderation check before users can see and interact with them in published games | [R11] |
| Owner | An asset uploaded through Open Cloud "belongs to the user or group in the `creationContext`". Group models appear under Group Packages | [R3] |
| API key | Group asset keys need the matching group permissions, the `assets` access permission, and read/write on the chosen experience; OAuth apps use `asset:read` and `asset:write` | [R3] |
| Moderation state | Open Cloud reports `moderationState`: `Reviewing`, `Rejected` or `Approved` | [R14] |
| Default privacy | Images, Decals and Meshes are created **Open Use** unless Asset Privacy is enabled for the user or group (then Restricted). Audio, Video, Models, MeshParts, Animations and Packages have their own defaults | [R8] |
| Irreversible steps | "Open Use is irreversible." "Game grants are permanent." | [R8] |
| Group grants | Granting to a group needs the Edit experiences permission in that group; group members with Edit access can then use the asset in the group's games | [R8] |
| Group owner duty | A group owner is responsible for all UGC "owned by, or associated with the Group", including content they didn't create | [L1] |
| Fonts | Fonts can't be imported; use Creator Store fonts | [R11] |

## Open Cloud Assets API asset types (create)

| Type | Formats | Limits |
| --- | --- | --- |
| Animation | `.rbxm`, `.rbxmx` | Files edited outside Studio may fail |
| Audio | `.mp3`, `.ogg`, `.wav`, `.flac` | ≤ 7 min; 100/month ID-verified, 10/month unverified; not updatable |
| Decal, Image | `.png`, `.jpeg`, `.bmp`, `.tga` | < 8000×8000 px; not updatable |
| Mesh | Roblox mesh data only | Only Asset Delivery downloads; not updatable |
| Model | `.fbx`, `.gltf`, `.glb`, `.rbxm`, `.rbxmx` | Uploaded as packages; only `.fbx` updatable |
| Video | `.mp4`, `.mov` | ≤ 5 min, ≤ 4096×2160, ≤ 3.75 GB, 20/day if 13+ and ID-verified; not updatable |

Every create or update call is limited to one asset and 20 MB [R3]. (The video limit of 3.75 GB is listed for the Video row on the same page; confirm which applies to Open Cloud before relying on large uploads.)
