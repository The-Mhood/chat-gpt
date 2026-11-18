# B2 REGISTER LEDGER — v17 — 2026-11-17
## Adanna turnaround: FRONT and THREE_QUARTER corrected to **V004**

Supersedes nothing. LEFT_SIDE V003 and BACK V003 are untouched and stand as filed at `v15`.
**Nothing here is approved, promoted or canon. Status of both new files: REVIEW REQUIRED.**
Both V003 plates remain in place, unedited and un-moved; V004 sits beside them as a distinct candidate.

---

## 1. Sources and outputs

| | FRONT | THREE_QUARTER |
|---|---|---|
| Source (V003, immutable) | `B2_CAND_CHAR_ADANNA_TURNAROUND_FRONT_V003_2560x1440.png` · 2,288,349 B · MD5 `f766197875d01884ee4077128b9aa072` | `…_THREE_QUARTER_V003_2560x1440.png` · 2,431,960 B · MD5 `39d2227f17d91476f04aab674e36daf0` |
| V003 Drive ID | `1nNFdXOcJYpojq1PYmRsOuZTn5wBRBIq8` (re-read this pass: 2,288,349 B, MD5 `f766197875d01884ee4077128b9aa072`) | as filed at `v15` — see note ¹ |
| Authorised output | **V004** (one correction) | **V004** (two corrections) |
| Output file | `B2_CAND_CHAR_ADANNA_TURNAROUND_FRONT_V004_2560x1440.png` · 2560×1440 · 2,290,525 B · MD5 `4231e27e25a259e2083ba8878779b99d` · SHA-256 `ae7e1bf7…ffdc67` | `…_THREE_QUARTER_V004_2560x1440.png` · 2560×1440 · 2,436,291 B · MD5 `a578b7c16be6d4ba8b5c6fae39d02fdd` · SHA-256 `dd5d2b13…fce176` |
| Drive ID (this filing) | `1MA20ws6ujgQazDb66BgDOHIjrNgfT29x` | `1JWX8z0UcLpqUXouXMJzSyWvMsVxTjxPI` |
| Verified parents | `16p2TYXn16u9UNdMlJzjTK873YK_Fk7Ab` (`PENDING/ASSISTANT_VA_SUBMISSIONS`) | same |

MD5 on Drive re-read with `get_file` after upload; both match the local files byte for byte.

¹ The THREE_QUARTER V003 Drive ID is **not restated here**. A transcribed copy of it returned 404 twice this pass, so the identifier recorded in `v15` stands and the file is pinned instead by name, exact byte count (2,431,960 B) and MD5 `39d2227f17d91476f04aab674e36daf0`. The V004 file's Drive description carries the same pin rather than a possibly wrong ID. Correcting the stored ID is a `v15` erratum, not a re-filing.

## 2. Corrections applied

| # | Point | FRONT | THREE_QUARTER |
|---|---|---|---|
| 8 | Pendant cord did not reach the neck | **Fixed.** Two continuous braided strands drawn from the pendant shoulders to the throat: `(1064,452)→(1052,402)` and `(1067,450)→(1071,403)`, taper 1.60→1.15 px, alpha 0.88 with braid modulation, colour `(104,74,52)`, top fade so the cord ghosts into the neck shadow rather than clipping. | **Fixed.** `(1073,432)→(1066,400)` and `(1076,430)→(1081,401)`, same parameters, colour `(96,70,50)`. |
| 9 | Rectangular tonal / texture patch on the near upper arm | not raised on this plate | **Re-laid.** Generated skin crop (`p_armtq_v4_new.png`) mapped into box `(890,435)–(1050,575)`, skin-masked (`R>G>B`, `R−B>15`, lum 25–175), eroded 7 px, feathered 16 px, clipped to rect `(898,447)–(1043,563)`. Gain-matched per channel `1.04 / 1.00 / 0.94`, offset `+4 / −1 / −3`, then host grain re-seeded at 0.22 strength so the new skin is not smoother than the rest of the body. Mask 3,041 px. |

Changed-pixel audit against V003 (threshold 3/255):

* FRONT — artwork changes confined to **x1050–1074, y403–455** (683 px): the cord only.
* THREE_QUARTER — confined to **x928–1083, y402–574** (3,708 px): cord plus arm patch.

Silhouette, hair, bustier, wrap, sandals, backdrop and figure scale are untouched on both plates.

## 3. What is stated plainly, not papered over

The V003 report called the arm defect a "rectangular tonal/texture patch". Measured on the V003 plate at the stated boundary (`x906/1035`, `y455/555`), the low-frequency step across each cited edge is **3.97 / 3.91** against **5.46 / 5.27** on control lines 20 px away — i.e. no tonal seam is detectable there, and the same holds after V004. What reads as a rectangle is therefore not a seam: it is the re-laid skin differing in *character* from the host (a large render downsampled into a small window is smoother and less saturated). V004 addresses that cause directly — content re-laid, gain and offset matched, grain restored — rather than blending a seam that measurement says is not there. If the reviewer still reads a patch at 100%, the remaining route is a full re-render of that arm, which is a raster regeneration of the plate and needs a CD call.

The baldric on both plates is still copy-corrected only, not repainted (carried from V003, item 5). The pendant is FICTIONAL; `CQ-9` blade and `RQ-10-1` coiled armlet remain OPEN. No blade or scabbard is depicted.

## 4. Chrome

Both plates carry `EXPLORATORY — NOT APPROVED CANON.  STATUS: REVIEW REQUIRED.  UNAPPROVED — PENDING REVIEW.`, the chapter tag, the FICTIONAL note, `OAD-40` figures 0 (one figure per plate by design), badge **V004**, and the footer `VERSIONS KEPT: V001 rejected, V002 rejected, V003 corrected, V004 this sheet. Nothing has been moved to 14_APPROVED_DESIGNS.` Index column lists all nine corrections, split V003 (1–7) / V004 (8–9).

## 5. Live candidates in PENDING (unapproved)

`ADANNA TURNAROUND V004` ×2 (this filing) · `ADANNA TURNAROUND V003` ×4 (superseded on FRONT and THREE_QUARTER, kept as the correction source) · `ESTABLISHING V013` · `VR-011 LANDING V002` (HOLD).

## 6. Next

1. CD/TD verdict on the two V004 plates.
2. FRONT and THREE_QUARTER are on their **first** correction attempt as V004; no further attempt is made until this one is answered.
3. `COMP_ADANNA_NNEKAS_YARD_FULL_FIGURE_V001` remains **BLOCKED** (no approved full-figure Adanna).

*No plate moved into `14_APPROVED_DESIGNS`. No version deleted. Nothing relabelled canon.*
