---
name: godot-headless-3d-render-export
description: Run, render and web-export a Godot 4 3D project on a CPU-only Linux box (no GPU) using Xvfb with Mesa llvmpipe (OpenGL) or lavapipe (Vulkan), capture deterministic frames, and gate them with a golden-image diff. Use for offline 3D previews and render regression tests; not for performance claims.
---

# Godot 4 headless 3D: render, golden image, web export

> Verified on 2026-11-27 (America/Los_Angeles) on a CPU-only Linux box (Debian 13, 8 vCPU, no GPU) with Godot 4.7.2: Compatibility renderer on Mesa llvmpipe under Xvfb (about 1.3 s per capture), Forward+ on Vulkan via a user-space lavapipe install (about 13 s including shader compile), a golden-image diff of 0 changed pixels on re-render and a failing diff when one small object was removed, and a Web export (about 3 s; 39.5 MB wasm, 10.1 MB gzipped). The exported page was not opened in a browser in that run.

## Facts to know first
- `godot --headless` uses a dummy renderer: good for `--import`, scripts and exports, but it draws nothing.
- To get real frames without a GPU, run under Xvfb. Mesa llvmpipe serves the Compatibility (OpenGL 3) renderer. Forward+/Mobile need Vulkan: install Mesa lavapipe. Without it Godot logs "Required Vulkan instance extension VK_KHR_surface not found" and falls back to OpenGL.
- Software rendering is deterministic on one machine (same driver), so exact golden images work there. Do not compare across machines or drivers without a tolerance, and never quote frame rates from it.

## Steps
1. Project: `project.godot` with `renderer/rendering_method="gl_compatibility"` for the cheapest path. Main scene script builds or loads the 3D scene, waits a few frames, then saves `get_viewport().get_texture().get_image()` with `save_png()` and calls `get_tree().quit()` when a user arg such as `--capture out.png` is present.
2. Import: `godot --headless --path proj --import`.
3. Render: `Xvfb :NN -screen 0 1280x800x24 &` (record the PID, kill only it), then
   `DISPLAY=:NN godot --path proj --resolution 960x600 --rendering-driver opengl3 -- --capture out.png`.
4. Vulkan without root (Debian/Ubuntu): `apt-get download mesa-vulkan-drivers libvulkan1`, `dpkg-deb -x` each into a local dir, point an ICD JSON at it, then run with
   `LD_LIBRARY_PATH=<dir>/usr/lib/x86_64-linux-gnu VK_ICD_FILENAMES=<icd.json> godot --rendering-method forward_plus --rendering-driver vulkan ...`. Expect a long first run while shaders compile.
5. Golden image: compare against a stored PNG with a per-channel tolerance and a changed-pixel budget. Prove it: rerun gives 0 changed pixels; removing one small object exceeds the budget and exits non-zero.
6. Web export: install matching export templates (`~/.local/share/godot/export_templates/<version>/web_*.zip`), add an `export_presets.cfg` Web preset (`variant/thread_support=false` avoids needing cross-origin isolation headers), then
   `godot --headless --path proj --export-release "Web" out/index.html`. Expect a large wasm (tens of MB; gzip about a quarter). Serve it locally and check it in a browser before any deploy.

## Proof of work
Commands, Godot version, renderer line from the log (e.g. "OpenGL API ... llvmpipe"), timings, PNG paths, golden diff numbers, and export file sizes.

## Gates
Hosting the web export is a deploy and needs the project owner's approval. Imported art and audio follow the project's asset approval rules.
