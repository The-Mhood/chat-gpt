# CANDIDATE REGISTER & STAGING LEDGER — **v5 addendum, 2026-11-17**
## VR‑010 Washing Place → **V004 candidate**, plus the correction-queue audit demanded by the standing protocol

Supersedes nothing. All rows in `B2_CANDIDATE_REGISTER_v4_2026-11-17.md` (`1Wwsibgrlr8bJevMjkRclaQ-iJ-SFgbE_`) and `B2_STAGING_LEDGER_v4_2026-11-17.md` (`1fNCoel_Z7KnlrMzMBUutBiJEDJ2X9nj0`) stand.

---

## 1. Correction queue audit — `16_REJECTED_DESIGNS` (`1x5T4V3R-hnuUNCIFBIb1TBIezjlT0Q6c`)

Folder now holds **9 files**: five images, four rejection reports. Ordered by the date the file entered the rejected area (oldest first), with each file's status under the first-attempt-before-second-attempt rule:

| # | Rejected asset | Entered | Report | First correction attempt | Status |
|---|---|---|---|---|---|
| 1 | `COMP_ADANNA_NNEKAS_YARD_FULL_FIGURE_V001.jpg` | 2026‑11‑15 18:32 | **none exists** | — | **BLOCKED — missing rejection report.** No defect list exists to work from; a name search for `REJECTION`* and for `NNEKA` returns no report for this asset. Position preserved, not skipped permanently. |
| 2 | `B2_CAND_VR-008_SEALED_QUARTER_V006` | 2026‑11‑17 10:54 | `REJECTION_REPORT_VR-008…` | done → V007, then V008 | awaiting CD verdict on V008 |
| 3 | `B2_CAND_VR-010_WASHING_PLACE_V003` | 2026‑11‑17 10:54 | `REJECTION_REPORT_VR-010…` | **done this round → V004** | awaiting review |
| 4 | `B2_CAND_ESTABLISHING_V006` | 2026‑11‑17 10:54 | `REJECTION_REPORT_ESTABLISHING_V006.md` | done → V007 | awaiting review; asset frozen |
| 5 | `B2_CAND_WALL_OF_HOUSES_V004` | 2026‑11‑17 10:54 | `REJECTION_REPORT_WALL_OF_HOUSES_V004.md` | done → V005 | awaiting review; asset frozen |

Every file that has a report now has a first attempt. The only unwritten file is #1, and its blocker is the absence of a report, not a lack of work. The two environment assets stay frozen until their candidates are reviewed, per the CD's standing instruction.

## 2. New files this round

Folder: `PENDING/ASSISTANT_VA_SUBMISSIONS` = `16p2TYXn16u9UNdMlJzjTK873YK_Fk7Ab`.

| # | Filename | Drive ID | Type | Bytes | MD5 | SHA‑256 |
|---|---|---|---|---|---|---|
| 1 | `B2_CAND_VR-010_WASHING_PLACE_V004_2560x1440.png` | `196uxAIaLdRGsqA0M0ALk9_Zps_A81XNt` | image/png · 2560×1440 | 3,353,277 | `93ece632db86191f05d74403f68cc238` | `0e1d0dc636fa3cc1e77ed786d5af4fb5c43908c88753802bd592b7d3cc4cda3b` |
| 2 | `B2_COMPARE_VR-010_WASHING_PLACE_V002_vs_V004.jpg` | `1Hl40ep9LfPsb2JqQCFjq6TCtTVrwtKnT` | image/jpeg · 2200×1252 | 849,845 | `ebd609bd2c9255a5b5752e32d4599d8d` | `1318f2f08111affad24b8c8831b2183e5e23387ee0e63406b8d94fabd77adbda` |
| 3 | `B2_REJECTION_RESPONSE_VR-010_V003_to_V004.md` | `1RO7-agpxO92Vp7ifjB34WEjXCJ5MXobA` | text/markdown | 6,232 | `01d752589d5f03d51518821c2218f7a9` | — |
| 4 | `B2_REGISTER_LEDGER_v5_2026-11-17.md` | *(this file)* | text/markdown | — | — | — |

Drive's returned MD5 matched the local value on both binaries before filing.

## 3. Source rows used

| Asset | Drive ID | Bytes | MD5 |
|---|---|---|---|
| Washing Place **V002** (visual authority) | `1hhIXVq3wj3JPkfBHIMwrNLPAyr0JByWh` | 697,266 | `8e31b7c4200a375a90157f195b1e0c0e` *(staged copy verified exact)* |
| Washing Place V001 (untouched) | `1qAf3rfpMC3w1AxtWrJC4l044ZnYuIRx7` | 617,315 | `c8f192a79e57e1a1174b1e461d85fe3f` |
| Washing Place **V003** (rejected, untouched, not used as a master) | `1LFW0r2B2fR9OAaR5HsqeqAwsH9tFwR65` | 3,443,296 | `7f958f1ca19fa5e675971aa01025ccb6` |

## 4. What V004 changes, in one line

The bright exposed runoff channel that crossed the yard in V002 is removed; the ground reads as plain damp earth with a flush grade. Everything the report named — slab, trough, pot and dipper, splash earth, screens, posts, wall — is V002's own pixel data. Declared deviation: **no wall-base pass-through is drawn**, because the only boundary in this camera is the woven screen and drawing an opening would mean inventing a recess or architecture that V002 does not contain.

## 5. Audit

| | VR‑010 V004 |
|---|---|
| Frame | 2560×1440, panel `(60,152)–(1960,1244)` = 1900×1092 |
| Alignment of the generative render to the crop | `(dx,dy) = (0,0)` |
| Changed px vs V002 | 113,314 |
| Inside repaint corridor | 46,197 |
| **Outside corridor + metadata column** | **0** |
| Slab / pots / screens / wall / sky | **0 changed px each** |

I certify the numbers, not the art. Approval, rejection or a dependency hold is the CD's call.
