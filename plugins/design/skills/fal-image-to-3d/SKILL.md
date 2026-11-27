---
name: fal-image-to-3d
description: Plan and run an approved fal.ai image-to-3D pipeline for Roblox props (concept image, image-to-3D with a polycount target, decimate and UV, bake ≤1024 PBR maps, import via Studio or Open Cloud) with cost estimates and approval gates. Use when a project wants AI-assisted 3D assets; not for avatar items or for running paid generations without a recorded spending approval.
---

# fal image-to-3D for Roblox

Turn an approved concept image into a Roblox-ready MeshPart with SurfaceAppearance. Every paid call needs a recorded spending approval, and every generated asset needs the owner's explicit yes before import.

## 0. Before anything costs money

1. Use only the project's designated fal account. Don't create a new account, and keep account names, keys and request ids out of public records.
2. List candidate models read-only (catalog browse for `image-to-3d` and `3d-to-3d`, model schema, pricing). Partner models are often priced in credits; take the per-call price from the model page and say where it came from.
3. Write the cost table (concepts × tries, 3D × tries, cleanup) and ask for a fixed cap. No cap, no calls.

## 1. Concept image (gate: owner yes)

One object per image, 3/4 view, flat mid-grey background, even light, no cast shadows or rim glow, whole object in frame, ≥1024 px. Baked lighting in the concept ends up baked into the albedo. Use the project's palette hexes in the prompt. Get the owner's yes on the image before converting it.

## 2. Image to 3D (gate: spend cap)

Prefer models with a **polycount control** and **PBR output** (see [model notes](references/fal-3d-models.md)):

- Smart-topology triangle output with `target_polycount` 1,500–6,000 for props.
- A `face_limit` model when budget matters most.
- A dedicated low-poly endpoint with `face_count` for a faceted look.

Avoid models whose minimum face count exceeds the 20,000-triangle Roblox cap unless you plan to remesh. Save the GLB and maps, and record the model id, seed, request id and cost privately.

## 3. Check, then decimate and UV

1. Check every mesh's triangle count and every map's size before touching it (a dependency-free GLB parser is enough: sum index counts / 3 per primitive).
2. If it's over budget: headless Blender (`blender -b -P script.py`) with a Decimate modifier to the target ratio, Weighted Normal for stylized shading, Smart UV Project if the UVs broke, glTF export. Installing Blender or `bpy` is large (on Debian, `apt-get install --no-install-recommends blender` is a ~91 MB package but pulls ~525 MB with dependencies), so get a yes first. After installing, smoke-test it: `blender -b --version`, then a script that adds a UV sphere, applies Decimate and exports a GLB, then run the triangle check on that GLB. Blender 4.3 does all of this headless with no display. Without Blender, use a paid remesh endpoint with texture baking (still under the cap).

## 4. Bake to SurfaceAppearance maps

Bake from the original to the low mesh: Color (no lighting), Normal in **OpenGL tangent space** (flip green if the source is DirectX), Roughness and Metalness as 8-bit greyscale, optional Emissive mask. Target ≤ 1024² (smaller for small props). Remove baked highlights; keep a light AO multiply in creases if the style wants it.

## 5. Import (gate: owner yes on exact files)

Record SHA-256 hashes of the GLB/FBX and maps, then get the owner's yes on those files.

- Studio 3D Importer (FBX/glTF/OBJ): set RenderFidelity Automatic, CollisionFidelity Box or Hull, add SurfaceAppearance, CastShadow off on small props.
- Open Cloud Assets API (`assetType: Model`, `.fbx`/`.gltf`/`.glb`): needs a group-scoped API key the owner creates; models arrive as packages.

Upload each mesh once and duplicate in Studio so instancing works. Then review with the [3D visual gate](../3d-visual-gate/SKILL.md).

See [sources](references/sources.md).
