# fal 3D models: notes for Roblox props

Catalog snapshot from fal's public model pages and catalog API, 2026-11-27. Prices and parameters change, so re-check before asking for approval. No model was run to make this table.

| Endpoint | Published price per call | Formats | Polycount control | PBR |
| --- | --- | --- | --- | --- |
| `meshy/t2/image-to-3d` | $0.20 untextured, $0.60 textured | GLB, FBX, OBJ, USDZ, STL | `target_polycount` ≤ 15,000 (default 4,000), triangle-only | yes |
| `meshy/t2.5/image-to-3d` | $0.80 per generation (catalog rate) | as above | ≤ 30,000 (default 15,000) | yes |
| `meshy/v7.1/image-to-3d` | $0.80 untextured, $1.20 textured | GLB, FBX, OBJ, USDZ, STL | `target_polycount` (default 30,000), quad/tri | yes |
| `tripo3d/h3.1/image-to-3d` | $0.20 / $0.30 standard texture / $0.40 HD; +$0.20 detailed geometry; +$0.05 quad | GLB (FBX quad) | `face_limit` | yes |
| `tripo3d/p2/image-to-3d` | $1.00–$1.30 by texture tier | GLB or FBX | `face_limit` 48–50,000 | yes, optional de-lighting |
| `hyper3d/lowpoly/image-to-3d` | $0.20 per generation (page) | FBX, GLB, OBJ, STL, USDZ | `face_count` (default 4,000) | PBR / Shaded / Hybrid, 2K–4K maps |
| `fal-ai/hyper3d/rodin/v2.5` | $0.40 (`/fast` $0.10) | GLB, USDZ, FBX, OBJ, STL | preset meshes incl. 2K and 20K triangles | PBR or Shaded |
| `fal-ai/hunyuan-3d/v3.1/pro/image-to-3d` | $0.375 + options ($0.15 each) | GLB, OBJ | `face_count` 40,000–1,500,000 (over the cap) | optional |
| `fal-ai/hunyuan-3d/v3.1/rapid/image-to-3d` | $0.225 (+$0.15 PBR) | GLB / OBJ | none | optional |
| `fal-ai/trellis-2` | $0.25–$0.35 by resolution | GLB | `decimation_target` (vertices) | textured, `texture_size` 1024–4096 |

Cleanup endpoints: `tripo3d/tripo/remesh` (`face_limit` 500–20,000, texture bake), `hyper3d/lowpoly/mesh-to-3d` (`face_count`, texture transfer), retexture endpoints (Meshy, Trellis 2).

For stylized props under ~6,000 triangles, start with a smart-topology or `face_limit` model at a textured tier with PBR on, then check and downscale the maps to ≤ 1024².
