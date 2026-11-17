# REJECTION RESPONSE — ESTABLISHING VIEW (ANCESTRAL REALM)
## `B2_CAND_ESTABLISHING_V012_2560x1440.png` — answers `REJECTION_REPORT_ESTABLISHING_V009.md`

**Asset code:** `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING` (`CH08-SUB-001`)
**Candidate:** 2560×1440 PNG · 4,034,861 B · MD5 `a692ca36e917c40ec0940f70310c78c4` · SHA-256 `6213c8785b222676a7cbb44dbd1060ee8950d80a7b2bfbbf5012a5b4cd831a9c`
**Status:** `REVIEW REQUIRED` — `EXPLORATORY — NOT APPROVED CANON`. Candidate only.
**Sources worked from:** untouched `V005` base (`1qi7TsLi…`), approved `NNEKAS_HOUSE_V004` (`1JIoAiQ…`), approved `HALL_OF_POSTS_V004`, approved `SEALED_QUARTER_V003`. No rejected version used as a master.

---

## Version note, stated plainly

The brief asks for `V010`. `V010` and `V011` already exist and were built **before** this report was read — `V010` answered the older `REJECTION_REPORT_ESTABLISHING_V008`, `V011` corrected chrome only. Neither executes the eight-point brief below. This file is the first candidate that does, so it is numbered **`V012`** rather than overwriting a filed artefact. `V009`, `V010`, `V011` are preserved unchanged.

---

## Item-by-item against §6

| # | Brief item | Status in `V012` |
|---|---|---|
| 1 | Scale Nneka's House proportionally | **NOT DELIVERED** — see §2 |
| 2 | Remove mask halo and the vertical blend seam near `x ≈ 1400` | Delivered |
| 3 | Remove the unauthorised wooden paling, restore the draped striped cloth per `V005` | Delivered |
| 4 | Remove the lower-right blue bleed | Delivered |
| 5 | Scale down summit dwellings, keep `V009`'s lifted haze, no regression to dark blacks | Delivered in `V010`, carried forward |
| 6 | Replace stale chrome; accurate metadata; explicit `FICTIONAL` disclaimer | Delivered |
| 7 | Preserve Requirement D placement, approved-plate fidelity, inanimate stakes | Preserved; stakes verified inanimate at 1:1 |
| 8 | Preserve Hall of Posts, left compound, overhead settlement, river margins, silhouette | Preserved — grain-level change only |

---

## 1. What was corrected, and how

- **Halo (item 2).** A median-based pull over the band `(1228,772)–(1478,940)` reduces only pixels exceeding their local 13-px median by more than 7 levels, at 0.7 weight. The pale rim that made the house read as a pasted cut-out is gone; no edge was redrawn.
- **Vertical seam (item 2).** The band `x 1382–1426, y 768–968` — where the re-staged yard met the untouched base — was cross-blended (70 % locally blurred, 30 % original) so ground, shadow and grain run continuously across the old boundary. No hard edge remains at `x ≈ 1400`.
- **Paling (item 3).** The plank fence occupied `(1420,826)–(1526,922)`. Three deterministic inpainting attempts were made and **discarded** — a band-shift clone, a two-band clone, and a horizontal mirror of the neighbouring wall (the mirror produced a symmetrical twin of the pots and shelf, obvious at 1:1). A generative in-context patch was then run on that region alone and composited back through a feathered footprint mask, colour-matched to the wall. The wall and the swept ground continue; nothing new was introduced.
- **Cloth (item 3).** The `V005` cloth line is restored whole at its own `V005` coordinates: the missing pieces (centre striped cloth, right-end striped cloth) were pulled from the untouched base and composited on a mask derived from the cloth's own silhouette — `V005` luminance below the current plate's by more than 14 levels, dilated and feathered — so no rectangular patch and no invented placement. The line now reads as it does in `V005`: terracotta, striped, cream, striped.
- **Blue bleed (item 4).** The pale blue cast sat on the foreground wall face, `(1380,1044)–(1901,1169)`. Channel ratios were matched to the same wall's warm left-hand run (R ×1.05, G ×0.95, B ×0.95), feathered at the edges. The band now reads as warm earth, and its `>12` pixel delta is **zero** — the correction is under 12 levels everywhere, which is the honest description: a cast removal, not a repaint.
- **Summit (item 5).** Carried from `V010`: dwellings ~30 % smaller and ~2× as numerous, composited inside the `V008` silhouette mask eroded 20 px / feathered 22 px, original high-frequency detail carried back at 0.38. The `V009` haze and lifted shadows are untouched.
- **Chrome (item 6).** Header `…_V012`, badge `12`, `STATUS: REVIEW REQUIRED`, `EXPLORATORY — NOT APPROVED CANON · CHAPTER 8`; `CLIENT REVIEW` reads `PENDING. No client ruling is recorded on this version; it is a candidate only.`; `CHANGED SINCE V009` and `KNOWN ISSUES` describe what is actually in the frame; a new `FICTIONAL ELEMENTS` block states that **the aerial river and the stacked mound of houses are fictional game-world conceits, not documented Igbo settlement forms**; footer carries the version register.

---

## 2. Item 1 — not delivered, and why (not a request, a statement)

Nneka's House still reads large for the yard. Reducing it means shrinking a house that is already composited into a photographed yard: a geometric scale leaves the vacated footprint and its cast shadow behind, and the ground, wall and veranda posts around it would have to be re-made anyway. That is a re-render in context, not a transform, and it is the one item I did not attempt rather than attempt badly. It is recorded on the sheet's own `KNOWN ISSUES` block, in the same words.

Two honest options for the next pass, both within the brief: re-render the house at correct scale in the yard with the approved plate as reference (the method that worked for the paling), or re-stage the yard at a slightly wider camera so the existing house scale sits correctly. I will take the first unless directed otherwise.

---

## 3. Verified audit (`V011` → `V012`, panel)

| Zone | `>2` | `>12` | `>20` | Reading |
|---|---|---|---|---|
| Paling footprint | 10,116 | 8,814 | 6,464 | the correction itself |
| Hut halo band | 20,675 | 9,974 | 5,803 | halo pull |
| Seam band `x 1382–1426` | 8,138 | 3,282 | 1,485 | seam blend |
| Cloth line | 7,957 | 5,086 | 3,534 | `V005` cloth restored |
| Blue-cast band | 38,619 | **0** | **0** | cast shifted <12 levels everywhere |
| Hall of Posts | 4,652 | 0 | 0 | max delta **6** — grain only |
| Left compound | 7,491 | 0 | 0 | max delta **5** — grain only |
| Frame bottom | 9,461 | 0 | 0 | max delta **8** — grain only |
| Hill bbox | 14,083 | 0 | 0 | max delta **5** — grain only |

Panel totals: 19,602 px `>12`; panel max 178. The whole panel was re-grained at `N(0,1.0)` so no region sits in a different noise regime from its neighbours; that is why sub-threshold counts are non-zero in untouched zones and their maxima are 5–8. **No structural change exists outside the five named correction zones.**

---

## 4. Files

| File | Size | MD5 |
|---|---|---|
| `B2_CAND_ESTABLISHING_V012_2560x1440.png` | 4,034,861 B | `a692ca36e917c40ec0940f70310c78c4` |
| `B2_COMPARE_ESTABLISHING_V011_vs_V012.jpg` | correction board, 5 zones | — |
| `B2_REJECTION_RESPONSE_ESTABLISHING_V012.md` | this document | — |
| `B2_REGISTER_LEDGER_v11_2026-11-17.md` | queue re-tallied against the canonical disposition register | — |

No plate moved into `14_APPROVED_DESIGNS`. No version deleted. Nothing relabelled canon.

*Filed to `PENDING/ASSISTANT_VA_SUBMISSIONS` for independent Our Eyes inspection and for an exact-version Research report on `V012`.*
