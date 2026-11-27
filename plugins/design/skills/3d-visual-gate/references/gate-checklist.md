# 3D gate checklist (paste into the PR)

```text
Head SHA: <40 chars>      Capture: Studio <version> / place <id or file> / emulator <device>
Owner yes for imported art: <link + date> | none imported
Local CI: <command> → <pass/fail>

Shots (file names <sha7>-<shot>-<state>-<device>-q<level>.png)
| Shot | States captured | Desktop | Phone q1 | Phone q4 |

Value (CIE L*, ring 24 px)
| Shot/state | %<L10 | %<L20 | p50 | Interactable | median L* | dL | pass |

Geometry and performance
| Check | Measured | Budget | pass |
| Max tris per mesh (source) | | ≤ asset budget, ≤ 20,000 | |
| Max map size | | ≤ 1024² | |
| On-screen tris / draw calls (worst shot) | | | |
| GraphicsTexture / GraphicsMeshParts MB | | | |
| p95 frame time (device) | | | |
| unique meshes / textures / lights / shadow lights | | | |
| Precise RenderFidelity / PreciseConvexDecomposition | | 0 / 0 | |

Lighting readback vs look doc: <diff or "matches">

Vision second opinion
Prompt: <template id + hash>
Model: <exact id>
Verdict: <one line>

Findings: High … / Medium … / Low …
VISUAL_GATE 3D <sha7>: PASS|FAIL H/M/L = x/y/z
```

## L\* measurement outline (Python, numpy + Pillow)

```python
import numpy as np
from PIL import Image
def lstar(rgb):
    c = rgb / 255.0
    lin = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    y = lin @ np.array([0.2126, 0.7152, 0.0722])
    f = np.where(y > (6/29) ** 3, np.cbrt(y), y / (3 * (6/29) ** 2) + 4/29)
    return 116 * f - 16
L = lstar(np.asarray(Image.open("shot.png").convert("RGB"), dtype=float))
x, y, w, h, r = 900, 500, 60, 60, 24                # interactable box, ring width
roi = L[y:y+h, x:x+w]
ring = np.zeros_like(L, dtype=bool)
ring[max(0, y-r):y+h+r, max(0, x-r):x+w+r] = True; ring[y:y+h, x:x+w] = False
print(np.median(roi), np.median(L[ring]), np.median(roi) - np.median(L[ring]), (L < 10).mean() * 100)
```
