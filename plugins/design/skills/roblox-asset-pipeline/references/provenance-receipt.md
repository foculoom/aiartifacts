# Provenance receipt (one template for every asset type)

Fill one receipt per asset in [receipt-template.json](receipt-template.json) and keep a short markdown copy in the private evidence note or PR appendix. Open it at the licence check (before generating) and finish it after upload. The template is shared by audio, meshes, images, decals and video.

The template is a **superset of the audio owner's receipt** (audio receipt v1.0): every audio key is kept with the same name and meaning, so the audio examples and rules in [audio.md](audio.md) §1.3 still apply unchanged. Added for the other asset types: `asset_type`, `source.tool_versions`, `source.input_files`, `source.third_party_inputs`, `licence_basis.fal_badge`, `spend_approval`, `files` (with SHA-256), mesh, image and video fields under `measured`, `roblox.roblox_asset_type`, `roblox.upload_path`, `owner_upload_yes`, `roblox.quota_counted_against`, and the post-transcode fields `measured.post_transcode_true_peak_dbtp` and `measured.post_transcode_verified`. The audio owner approved these names on 2026-11-27; `owner_listen_approval` stays separate from `owner_upload_yes`.

## Required fields, all types

| Field | What to record |
| --- | --- |
| Tool and model or plan | `source.kind`; fal model id and version; Suno plan at creation and Download evidence; script path, commit and tool versions for code-generated |
| Date | `created_at` with time zone |
| Prompt | Full prompt, negative prompt, lyrics or tags |
| Seed | `source.seed` (every random generator, including code) |
| Inputs | Concept images and reference files with hashes; third-party inputs with their licences |
| Licence link | `licence_basis.link`, date read, fal badge, upstream licence and restrictions |
| Spend approval | Reference to the recorded approval and the cost of this asset |
| File SHA-256 | Every file to be imported or uploaded |
| Measurements | The type's checks (below) |
| Owner review | `owner_listen_approval`: listen (audio, video) or look (mesh, image), in the owner's own words. Code-generated audio: `not_required_code_generated` |
| Owner yes to upload | `owner_upload_yes`: always required, covers the listed hashes only, confirms the Roblox upload licence is acceptable (original assets only) |
| Roblox asset id | `roblox.asset_id`, type, owning group, upload path, experience grant, privacy, moderation status |

Request ids, account names and track ids go in the private receipt only, never in public files or PRs.

## Type-specific measurements

| Type | Fields | Pass rule |
| --- | --- | --- |
| Audio | LUFS-I, true peak, clipping, loop wrap, attack, level vs bed, guardrail | [audio.md](audio.md) §4 (audio owner's targets) |
| Mesh | triangles per mesh, texture map sizes, normal space, RenderFidelity, CollisionFidelity, 3d-visual-gate result | ≤ 20,000 triangles; maps ≤ 1024²; OpenGL normals; gate with no High or Medium |
| Image / decal | pixel size, alpha type, contrast for UI | Within the specs; ≥ 4.5:1 for essential UI text and icons |
| Video | duration, resolution, max flashes per second; the soundtrack is measured as audio by role (music, SFX, speech) under the audio fields, with the owner's listen | ≤ 5 min; ≤ 4096×2160; ≤ 3 flashes/s |
| All | moderation pre-check | No item from the moderation list |

## Worked example: generated mesh (private copy)

```markdown
### Receipt — prop-lantern-post-v1
- Type: mesh. Source: fal, image-to-3D model <id> (badge: Commercial use, read 2026-11-27), from concept image concept-lantern-post-v2.png (sha256 …), itself from a commercial text-to-image model (receipt concept-lantern-post-v2).
- Prompt: "<full prompt>". Seed 42. Date 2026-11-27, America/Los_Angeles.
- Spend approval: <reference>, cap <amount>; this asset <cost>.
- Edits: Blender decimate 0.31, Weighted Normal, Smart UV Project, bake 512² Color/Normal(OpenGL)/Roughness/Metalness.
- Files: lantern_post.glb (sha256 …), lantern_post_color.png (sha256 …), …
- Measured: 3,840 triangles; maps 512²; RenderFidelity Automatic; CollisionFidelity Box; 3d-visual-gate 0/0/1; moderation pre-check pass.
- Owner look: pending. Owner upload yes: pending.
- Roblox: not uploaded.
```
