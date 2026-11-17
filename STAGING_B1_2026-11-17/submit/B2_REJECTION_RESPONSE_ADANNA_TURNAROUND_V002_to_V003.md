# REJECTION RESPONSE — CHAR_ADANNA_TURNAROUND_V002 → V003

**Programme:** *The Disobedient Daughter*
**Asset:** `CHAR_ADANNA_TURNAROUND` — four-plate 4-view turnaround (FRONT · LEFT SIDE · BACK · THREE QUARTER)
**Supersedes:** `V002` (four plates rejected 17 Nov 2026: `RR_ADANNA_TURNAROUND_FRONT`, `LEFT_SIDE`, `BACK`, `THREE_QUARTER`)
**Status:** `UNAPPROVED — PENDING REVIEW` · `EXPLORATORY — NOT APPROVED CANON` · `STATUS: REVIEW REQUIRED`
**Date:** 17 Nov 2026

## 1. Method, and what was preserved

V003 is built from the **four V002 plate rasters**, not from a new generation. Each of the seven
corrections is a bounded edit inside the art panel; the panel, pose, framing and orthographic scale
of each V002 plate are carried through untouched, and the chrome is re-rendered around them.

Measured on the V003 files (panel 1870 × 1180 at offset 60, 130; backdrop threshold max-channel
difference > 34 from RGB 209, 209, 207):

| Plate | Crown row | Floor row | Figure height |
|---|---|---|---|
| 1 FRONT | 57 | 1159 | 1103 px |
| 2 LEFT SIDE | 57 | 1158 | 1102 px |
| 3 BACK | 57 | 1155 | 1099 px |
| 4 THREE QUARTER | 57 | 1157 | 1101 px |

Spread: crown **0 px**, floor **4 px**, height **4 px** — inside the V002 envelope you specified
(crown row 57, floor rows 1155–1159, height 1099–1103 px). All four files are 2560 × 1440.
No blade or scabbard is depicted (CQ-9 stays OPEN). The spiral pendant carries a FICTIONAL label.

## 2. The seven corrections

**1 — Armlet: medallion removed, plain concentric coils.** *Done, all four plates.*
A second defect turned up while doing it: in V002 the **three-quarter plate carried an arm
ornament on both upper arms** — thin coils on her near (anatomical RIGHT) arm and a wide hammered
cuff with a hanging spiral medallion on her far (anatomical LEFT) arm. The medallion you flagged
was on the near arm; the locked LEFT arm was the one that kept its medallion. V003 leaves the near
arm **bare** and gives the far, locked LEFT arm **four plain smooth concentric coils** with no
medallion. FRONT, LEFT SIDE and BACK likewise read as plain coils with no disc or hanging ornament.

**2 — Spiral bronze pendant on a braided cord, FRONT / LEFT SIDE / THREE QUARTER.** *Done.*
The disc is the master reference's own pendant (`CHAR_ADANNA_MASTER_REFERENCE_V001`, crop
924,686–1032,792, face only), placed through a soft ellipse mask with a contact shadow and a
3 px braided-cord strip that disappears behind the neck. Disc centres, measured on the retouched
plates: FRONT (1060, 470) 19 × 19 px · LEFT SIDE (1082, 445) 12 × 17 px · THREE QUARTER
(1074, 447) 17 × 17 px. Marked FICTIONAL in the sidebar of every plate.

**3 — Scar moved to the anatomical LEFT cheekbone (three-quarter).** *Done.*
In V002 the three-quarter plate put the scar on the near cheek, which is her RIGHT. V003 removes
it there (median infill inside a 18 × 16 px box, no tone shift) and draws it on the far
left cheekbone at (1124, 313) — a 10 px, 1.8 px-wide healed line with a soft under-shadow.

**4 — BACK: braid-tip coral beads removed.** *Done.*
The two coral beads and the pale brass rings woven into the braid ends at the shoulder strap
(plate 1012–1047 × 398–441) are gone; the braids read as uninterrupted plain braids and the
strap is clean leather. Beads remain only at the high LEFT temple, as locked.

**5 — Baldric routing: anatomical LEFT shoulder → anatomical RIGHT hip.** *Copy corrected.*
Sidebar copy and the alignment sheet now read LEFT shoulder → RIGHT hip on all four plates. The
painted strap is the V002 raster and has not been repainted: in all four plates it leaves the
shoulder that reads as her anatomical LEFT (viewer-right in FRONT and in the three-quarter, near
shoulder in the LEFT profile, viewer-left in BACK) and crosses to her RIGHT hip. Correction 5 in
the report was against the copy, and the copy is what changed.

**6 — Plate index.** *Done.* Sidebar reads `_V003 · plate 1 of 4-view set` … `plate 4 of 4-view set`,
and the alignment sheet numbers the plates 1–4.

**7 — Near-side and wrap-tie notes.** *Done.*
THREE QUARTER: "turned to her RIGHT. Her RIGHT side is the near side; the beaded LEFT temple and
the scar are on the far side, partly foreshortened." BACK: "Viewer-left is her anatomical LEFT:
the armlet reads viewer-left, and the wrap tie sits at the LEFT hip, front, not centre back."
Per your TD ruling, viewer-left in BACK is anatomical LEFT and the armlet at viewer-left is preserved.

## 3. What was not done

- **The baldric is not repainted.** Only the copy changed (see 5). If you read the painted strap as
  running the other way, that is a raster change and needs a fresh decision before V004.
- **The armlet is not a full re-sculpt.** The band silhouette is the V002 geometry with the
  medallion lifted out and plain rings read in; thickness and position are unchanged.
- **BACK strap/shoulder junction** is partly under the braid mass; nothing was drawn there.
- Chrome text density: the FRONT column runs to row 1266 of 1310, the other three to 1224–1245.

## 4. Files

| File | Bytes | MD5 |
|---|---|---|
| `B2_CAND_CHAR_ADANNA_TURNAROUND_FRONT_V003_2560x1440.png` | 2,288,349 B | `f766197875d01884ee4077128b9aa072` |
| `B2_CAND_CHAR_ADANNA_TURNAROUND_LEFT_SIDE_V003_2560x1440.png` | 2,444,893 B | `703d87e2851e179364aed3ebcfae1943` |
| `B2_CAND_CHAR_ADANNA_TURNAROUND_BACK_V003_2560x1440.png` | 2,574,938 B | `75908260a12da2a1260b105659b7d6ee` |
| `B2_CAND_CHAR_ADANNA_TURNAROUND_THREE_QUARTER_V003_2560x1440.png` | 2,431,960 B | `39d2227f17d91476f04aab674e36daf0` |
| `B2_COMPARE_ADANNA_TURNAROUND_V003_alignment.jpg` | 300,888 B | `e10c3802834c3e4d6bf80eed80ab1afe` |

V001 and V002 remain untouched in `16_REJECTED_DESIGNS`. Nothing has been moved into
`14_APPROVED_DESIGNS`. CQ-9, RQ-10-1 and the pendant's FICTIONAL status stay open.
