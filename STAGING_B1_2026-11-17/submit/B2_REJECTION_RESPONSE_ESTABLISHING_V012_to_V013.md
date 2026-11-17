# B2 — REJECTION RESPONSE: ESTABLISHING `V012` → `V013`

**Asset:** `CH08-SUB-001` Ancestral Realm, Establishing View
**Supersedes:** `V012` (rejected; brief `REJECTION_REPORT_ESTABLISHING_V012.md`, `1l4zcjiDg-9M7Mff9BHFDJWfAxz_RG-fT`).
**Status of `V013`: UNAPPROVED — REVIEW REQUIRED.** Candidate only; no client ruling recorded.
**Date:** 2026-11-17 · **Branch** `arena/90e15011-chat-gpt`

---

## 1. Item-by-item against the authorised `V013` brief

| # | Brief item | `V013` state |
|---|---|---|
| 1 | Margin bleed + wall warmth (measurable) | **Done, measured.** The `RGB(0,20,38)` / `RGB(0,14,28)` cyan band below the art is gone: the bottom margin now reads `RGB(8,12,23)` at both `x=300` and `x=1900`, matching the clean left margin. The lower-right wall band was re-ramped to warm daylight: `RGB(37,8,4)`–`(56,17,7)` typical, against `V012`'s `RGB(44,23,23)` and cooler. |
| 2 | Cloth-line seam + `NNEKAS_HOUSE_V004` side cloth | **Done.** The hard cut edge and pale wedge at the right end of the cloth line were re-rendered as hanging fabric; the pale wedge is gone. The approved striped indigo-and-cream side cloth now hangs on the right wall of Nneka's house, as in `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_NNEKAS_HOUSE_V004.jpg`. |
| 3 | Smudged right roof gable + back-middle plot stake (`x ≈ 1400`) | **Done.** The house was re-rendered through a bounded pass: thatch gable reads crisp strand by strand and the back plot stakes stand clean against the yard, no clone smudge. |
| 4 | Foreground right-compound house scale (CD Option A retained) | **Done.** House reduced about 15 % in frame (measured 227 px → 193 px of wall-and-roof height across `x 1240-1680`), with more bare yard around its base; roof pitch, doorway and wall mass unchanged relative to each other. Warm-daylight unbuilt staked plot preserved beside it. |
| 5 | Basal hill hut scale + left-flank mask edge | **Not done, stated.** See §2. |
| 6 | Chrome, provenance, FICTIONAL labels, research note | **Done.** `EXPLORATORY — NOT APPROVED CANON`, `STATUS: REVIEW REQUIRED`, `CHAPTER 8`, `FICTIONAL` labels for the stacked hill and the aerial river, `OAD-40` figureless (0 figures), `V013` filename badge, changelog block `CHANGED SINCE V012`, `VERSIONS KEPT: V005 base, V006 – V012 preserved`. No claim of a fix that was not made. |

## 2. Why item 5 is stated rather than faked

Two parts, two different reasons:

- **Basal hut scale.** The brief gives no measurable target, and the basal huts sit inside the landmark silhouette of an approved base plate. Re-proportioning them by eye is the class of edit that produced `V012`'s introduced defects. Left as approved, and named as open on the sheet.
- **Left-flank edge.** I probed it instead of assuming: horizontal luminance profiles across the flank at `y = 580, 640, 700, 760` show **roof and wall detail** (max step 8–96, irregular), not a uniform multi-pixel alpha ramp, so what reads as softness is the atmospheric haze of the approved `V005` base, not a compositing feather. The brief says to sharpen the edge *without altering the approved silhouette*; sharpening haze would alter it. Preserved, and named as open on the sheet.

If Our Eyes wants either changed regardless, that is a CD call on an approved base plate and I will execute it as specified.

## 3. What was preserved

- `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg` (`1qi7TsLi5v8pfM4mHYLWvJEaSdPPyl_qW`, MD5 `6f32d454bb7b6f15ce31e3bffa136385`) and `…_NNEKAS_HOUSE_V004.jpg` (`1JIoAiQ20goibDA-ujYr95iyihBTLKZWj`, MD5 `8eec0c112ea14a8aa1d8328ed10004e7`): both untouched, used as references only.
- Hall of Posts geometry and lighting, warm daylight key, aerial river composition, existing compounds and lane — unchanged.
- Zero human figures (`OAD-40`) verified: 0.
- No approved folder written to. Nothing approved, deleted or relabelled canon.

## 4. Research status

Still `research-incomplete`: no `RR_ESTABLISHING_V013_*` exists. The five carried-forward qualifications are repeated verbatim in the plate's chrome. **An exact-version Research report is required before review can conclude.**

## 5. Files submitted

| File | Bytes | MD5 |
|---|---|---|
| `CAND_ESTABLISHING_V013_2560x1440.png` (2560×1440) | 3,931,605 | `b4986e76bac7497d4890f3616c2b6339` |
| `B2_COMPARE_ESTABLISHING_V012_vs_V013.jpg` (2118×2456) | 935,882 | `a4d954d2e931f7649482968395f487d8` |

Build notes: `V013` = `V012` raster + three bounded passes (frame-margin and wall re-tone; cloth-edge repaint; house re-render pasted through a feathered footprint) + chrome rebuild. Every pass was inspected at 1:1 before filing. `V012` remains intact in `16_REJECTED_DESIGNS`.
