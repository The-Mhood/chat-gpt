# VERIFICATION — environment rebuilds: Establishing V007 and Wall of Houses V005
**What was measured, on which files, and what the numbers cannot tell you.**
Status: CANDIDATE ONLY · REVIEW REQUIRED · not approved, not canon, not filed.

---

## 1. Files verified

| Asset | Base (verbatim master) | Base MD5 | Candidate | Candidate SHA-256 |
|---|---|---|---|---|
| Establishing | `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg` | `6f32d454bb7b6f15ce31e3bffa136385` | `B2_CAND_ESTABLISHING_V007_2560x1440.png` | `12c96f52a21b9d6f68db8e8bbf01ea79bb5b2d389d4e51f3fc457a7636f1fe6b` |
| Wall of Houses | `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_WALL_OF_HOUSES_V003.jpg` | `1ee728c2bae54ae5284959ca5e747943` | `B2_CAND_WALL_OF_HOUSES_V005_2560x1440.png` | `71fbf901dd3bc5fe936e765aa7a8d19606f1cf1114a3deb71c60ac69e0f90f79` |

Candidate MD5s: EST `d176595797b04432c9aa08f3a41e6d2a` · WALL `a2298fe5270e6f4737e89228f1b2fc70`.
Both candidates are 2560×1440, same frame geometry as their bases; artwork panel `(60,152)–(1961,1321)` = 1901×1169.

Comparisons: `B2_COMPARE_ESTABLISHING_V005_vs_V007.jpg` (MD5 `4cc128da650b6a34641e9d22e14f8442`), `B2_COMPARE_WALL_OF_HOUSES_V003_vs_V005.jpg` (MD5 `022f4b27099b9e4ae462ba40828e0581`).

## 2. Method, stated plainly

Neither candidate is a hand retouch. Each is a **masked architectural repaint**:

1. The 1901×1169 artwork panel was cut from the verified master.
2. The generative editor was given that panel as reference and returned a 1301×800 render.
3. The render was aligned to the panel by an exhaustive translation search on luminance (reported below), then blended through a hand-drawn polygon mask with a Gaussian feather.
4. The composite panel was pasted back into the untouched master frame and the metadata column was re-set in the frame's own typography.

**Consequence:** inside the mask the pixels are the generator's, not the master's. This method cannot preserve surface grain, micro-detail or light direction the way a hand retouch can. Everything outside the mask is the master's own bit-identical pixels.

| | Establishing V007 | Wall of Houses V005 |
|---|---|---|
| Alignment offset applied | `(dx, dy) = (−4, +2)` | `(dx, dy) = (0, +10)` |
| Mean absolute difference at best alignment | 5.35 | 6.44 |
| Mask feather | Gaussian, 26 px | Gaussian, 30 px |
| Panel pixels inside mask | 365,251 | 1,180,944 |
| Total changed pixels vs base | 441,432 | 1,234,163 |
| **Changed pixels outside mask + metadata column** | **0** | **0** |
| Saturated bright-red pixels in artwork panel | see §4 | **0** |

"Changed" = summed RGB channel difference greater than 12, i.e. a deliberately strict threshold; the outside-mask result is 0 under it, not merely small.

## 3. What the pixel audit proves and does not prove

**Proves:** the aerial river, the Hall of Posts, the inverted overhead settlement, the foreground compound and both frame edges are the master's own pixels, unmodified — verified numerically, not by eye. It also proves the two V004/V006-only defects (red bars and glyphs; the wall smear) cannot be present, because every pixel that could carry them was either outside the repainted mask or never existed in the source.

**Does not prove:** that the repainted architecture is correct, that the houses read as intended, that the door states are legible, or that the surfaces match the series. Those are judgements for the reviewer, and the comparison boards are supplied so they can be made against the base at full resolution rather than against my description.

## 4. Known residuals, disclosed rather than smoothed over

**Establishing V007**
1. **Surfaces read flatter than V005's.** The rebuilt houses are lighter and less granular than the master's own mid-ground. They do not yet match `WALL_OF_HOUSES` material weight.
2. **The mask edge sits in haze on both flanks.** It is soft, not invisible. The aerial river's left termination is slightly softer than V005's: in the master the river thins into mist before the mound; in the candidate it thins a little earlier, because the feather crosses it.
3. **The mound silhouette now rises into the overhead settlement** — that is the intended cone replacement, but it means the sky band above the mound is not bit-identical to V005 (about 19,000 px change where the new rooftops meet the mist).
4. **Nneka's House.** The foreground compound — the house's position in this composition — is **V005's own untouched pixels; 0 changed pixels** in that region. A separate generative pass was made for a warm-daylight house and was **not used**: placing it would have lit a hazy distance wrongly and repeated the V006 spotlight defect. The house is therefore unaltered, not re-integrated.
5. **The "saturated red" metric is meaningless on this plate.** The whole scene is oxide-red earth; a bright-red filter returns ~15,600 px of natural shadowed earth. No red marks were introduced, but the metric cannot prove that on this image — the reviewer's eye must. (On Wall of Houses the same filter returns 0.)

**Wall of Houses V005**
1. **Ladder routes are fewer than V003's** and read less clearly as one continuous climb.
2. **The mound sits slightly lower and broader**, and the upper right slope is hazier and emptier than V003's — the two-storey cluster was removed there and fog took its place.
3. **The whole built mound is a masked repaint**, so its surfaces differ from V003's photoreal grain outside the mask.
4. The oldest-settlement row at the foot, the lit/dark/plain-sealed door triad and the absence of red bars, glyphs or painted symbols were confirmed by direct inspection of the exported PNG at 1.5× and 3×, not from the generator's render.

## 5. Metadata column

Both metadata columns were re-set in DejaVu Sans / DejaVu Sans-Bold, labels 15 pt at x=1995 in the frame's tan `(164,139,93)`, body 16 pt at x=1995 in `(226,225,217)`, 23 px leading, on the frame's navy `(9,13,24)`. This is a **re-set**, not the original typeface: glyph shapes differ slightly from the master's chrome even at matched widths. A width assertion (`1995 + textwidth < 2548`) guarantees no line leaves the gutter; it was enforced at build time and every line was visually confirmed after export.

Header version digits were changed V005→V007 and V003→V005 by repainting the digit box and redrawing the numeral at the frame's own header position.

## 6. Reproducibility

Scripts in `work2/`: `comp_est.py`, `comp_wall.py` (alignment, mask, composite), `compose_env.py` (chrome), `verify_env.py` (the audit in §2), `boards_env.py` (comparison boards). The audit is deterministic and re-runs to the same counts. The generative renders are **not** reproducible: a re-run returns different architecture. That is a limitation of the method, and it is why the mask boundary and the audit matter.

## 7. Status

Both files are candidates for review. Nothing here is approved, promoted, filed or canon. V005 (Establishing) and V003 (Wall of Houses) are preserved untouched, as are the rejected V006 and V004. If either candidate is rejected, the correction path is a new version number from the same preserved base — not an edit of these files.
