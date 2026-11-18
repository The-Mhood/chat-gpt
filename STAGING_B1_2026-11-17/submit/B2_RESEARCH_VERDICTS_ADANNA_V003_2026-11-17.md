# RESEARCH VERDICTS ON ADANNA V003 — CHIRALITY ANSWER AND ONE ASSET-INCIDENT FLAG

**Programme:** *The Disobedient Daughter* · **Date:** 2026-11-17
**In answer to:** `REFRESH_PASS7_ADDENDUM_2026-11-17.md` (`1xYV94nXvLb60MKA5fvodgViKpr6H-mig`) §6, §8
and the four exact-version reports on `CHAR_ADANNA_TURNAROUND_V003`.

## 1. Verdicts received

| Plate | File ID | Research verdict |
|---|---|---|
| FRONT | `1nNFdXOc…` | PASS WITH QUALIFICATIONS |
| LEFT SIDE | `14uOMGJY…` | PASS WITH QUALIFICATIONS |
| BACK | `11MmHTZ-…` | PASS WITH QUALIFICATIONS — **chirality conflict recorded as OPEN** |
| THREE QUARTER | `1nYt7Tvo…` | PASS WITH QUALIFICATIONS |
| `ESTABLISHING V013` | `1MuhupyL…` | PASS WITH QUALIFICATIONS |

All four were inspected at the filed versions (v2, MD5s matching). Nothing was regenerated in
response to a research pass; a research verdict is not a fix instruction.

## 2. BACK viewer-left / anatomical side — the geometry settled by measurement

Research's BACK report says: *"In a back view the figure faces away from the viewer, so viewer-left
is her RIGHT side."* That sentence is inverted, and it is the only basis for the conflict flag.

**The rule.** Facing the camera, a subject's left hand appears on the viewer's right. Facing away,
the same left hand appears on the viewer's **left**. In BACK, viewer-left is anatomical LEFT.

**The measurement.** Armlet centroid, detected on the filed V003 plates as brass pixels
(R > 120, G 85–175, B < 115, R−B > 45, R−G > 12) inside a hand-set window per plate; body centre
measured independently as the mid-point of the figure's column extent (panels are 1870 px wide at
x = 60, so panel centre is x = 995 on the plate):

| Plate | Body centre x | Armlet centroid x | Offset from body centre |
|---|---|---|---|
| FRONT | 1008 | 1189 | **+181** (viewer-right) |
| LEFT SIDE | 1025 | 1171 | +146 |
| BACK | 1006 | 971 | **−35** (viewer-left) |
| THREE QUARTER | 1005 | 1200 | +195 |

The armlet sits on opposite screen sides in FRONT (+181) and BACK (−35). A single fixed arm
seen from the front and from behind **must** swap screen side in exactly this way. Research's
reading — viewer-left = her RIGHT in BACK — would put the armlet on the same screen side in both
plates, which is not what the pixels show, and would move the locked LEFT armlet onto her right
arm in the back view alone.

**Conclusion:** the plate's statement, the TD ruling and the OAD-02 LEFT lock are internally
consistent; the research sentence is a wording error, not an artwork defect. The armlet, the wrap
tie and the baldric end all read viewer-left in BACK because that is her LEFT in a back view.
This is stated as evidence, not as a ruling: if CD and TD prefer to restate the convention, the
artwork does not have to move.

## 3. THREE QUARTER turn direction

Research asks Our Eyes to confirm the turn against the master. The master
(`CHAR_ADANNA_MASTER_REFERENCE_V001`) is a bust and detail crops; it does not carry a turn arrow, so
it cannot settle this on its own. The plate's own geometry does, and it is consistent:

- The near upper arm is **bare**, the far arm carries the armlet at viewer-right (centroid x 1200,
  +195 from body centre).
- The beaded LEFT temple reads at the **viewer-right edge** of the head, partly hidden behind the
  braid mass — a far-side position.
- The baldric leaves the same shoulder it leaves in FRONT (viewer-right), which is her LEFT.

Taken together: the near side is her RIGHT, the far side is her LEFT, and she is turned to her
right. That is what the plate states in chrome. No change made or needed.

## 4. Status of the seven corrections against the research reading

| # | Correction | Research reading | Note |
|---|---|---|---|
| 1 | Armlet medallion out, plain coils | accepted on all four | V003 also removed the second, wrongly-placed ornament on her RIGHT arm in the 3Q plate |
| 2 | Spiral pendant restored (F/LS/3Q) | accepted, FICTIONAL | — |
| 3 | Scar to anatomical LEFT cheekbone (3Q) | accepted, not independently verified vs master | the master bust does not show the scar's position at this scale |
| 4 | BACK braid-tip beads out | accepted, "no braid-tip beads visible" | — |
| 5 | Baldric copy LEFT shoulder → RIGHT hip | accepted as copy-only | both reports repeat that the strap is the V002 raster |
| 6 | Plate index 1–4 | accepted, recorded | — |
| 7 | Near-side and wrap-tie notes | accepted | — |

## 5. Asset incident — `ENV_CH03-EXP-001_THE_WALL_TOP_WALK_V001.jpg`

Research's addendum §4 discloses that `update_file_content` was called with the **candidate's** ID
instead of the report's, replacing the artwork with report text. Verified this pass:

- `1SsRkI8jhMeKC_VOSmRugvuMx3mo5O8uI` now reports `mimeType text/markdown`, **2,537 B**,
  MD5 `314681784166f5cd747f7f933f92b300`, parent `1YUCfczTDGsdcMGz3favvphMabMR9q9PJ` (ORIGINAL VA).
- The artwork was JPEG v2, **337,726 B**, MD5 `bce36fd7b0192e77b6f2de64b4e4be65`.

**What I could not do, and did not fake.** This connector exposes no revisions list and no restore
call; `download_file` on that ID returns the text, and there is no second copy of that filename
anywhere in Drive (`name contains 'WALL_TOP_WALK'` returns one file). The only route is Drive's own
*File → Version history*, which the file owner must run. I did **not** upload a placeholder or a
re-render as that filename, because a new ID or a new image under the old name would destroy the
audit trail.

**Recommended action (owner):** restore version 2 of `1SsRkI8j…`, then confirm MD5
`bce36fd7b0192e77b6f2de64b4e4be65` / 337,726 B before anyone re-issues the EXP-001 correction.
Research advises doing this before any other action on that candidate; I agree.

## 6. Still open on my side

- **CQ-9** blade and scabbard: OPEN, no blade depicted.
- **RQ-10-1** coiled armlet: OPEN, not captioned as regalia.
- **Pendant:** FICTIONAL, no Igbo provenance.
- **Baldric:** copy corrected in V003; the painted strap is the V002 raster. A repaint is a `V004`
  raster change and needs a CD call first.
- **`ESTABLISHING V013` item 5** (basal hut scale, flank edge): awaits a CD call on the approved base.
- **`COMP_ADANNA_NNEKAS_YARD_FULL_FIGURE_V001`:** still BLOCKED — no approved full-figure Adanna.

*No plate moved into `14_APPROVED_DESIGNS`. No version deleted. Nothing relabelled canon.*
