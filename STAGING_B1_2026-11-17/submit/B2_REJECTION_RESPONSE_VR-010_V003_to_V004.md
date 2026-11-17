# REJECTION RESPONSE — VR‑010 WASHING PLACE · V003 → **V004 candidate**
**Answers `REJECTION_REPORT_VR-010_WASHING_PLACE_V003.md` (`1fGDPQyyAmCkSrAB_sHIaqQns50sRmZDS`), joint CD/TD verdict REJECTED — REVISION REQUIRED.**
Status: CANDIDATE ONLY · REVIEW REQUIRED · not approved, not canon, not filed.

---

## 1. Provenance

| Role | File | Drive ID | Bytes | Size | MD5 | SHA‑256 |
|---|---|---|---|---|---|---|
| **Visual authority (base)** | `ENV_HOME_SETTLEMENT_WASHING_PLACE_V002.jpg` | `1hhIXVq3wj3JPkfBHIMwrNLPAyr0JByWh` | 697,266 | 2560×1440 | `8e31b7c4200a375a90157f195b1e0c0e` | `5f8e…` *(staged copy verified)* |
| Rejected candidate (**not** used as a master) | `B2_CAND_VR-010_WASHING_PLACE_V003_2560x1440.png` | `1LFW0r2B2fR9OAaR5HsqeqAwsH9tFwR65` | 3,443,296 | 2560×1440 | `7f958f1ca19fa5e675971aa01025ccb6` | per report |
| Earlier version (untouched) | `ENV_HOME_SETTLEMENT_WASHING_PLACE_V001.jpg` | `1qAf3rfpMC3w1AxtWrJC4l044ZnYuIRx7` | 617,315 | 2560×1440 | `c8f192a79e57e1a1174b1e461d85fe3f` | — |
| **This candidate** | `B2_CAND_VR-010_WASHING_PLACE_V004_2560x1440.png` | `196uxAIaLdRGsqA0M0ALk9_Zps_A81XNt` | 3,353,277 | 2560×1440 | `93ece632db86191f05d74403f68cc238` | `0e1d0dc636fa3cc1e77ed786d5af4fb5c43908c88753802bd592b7d3cc4cda3b` |
| Comparison board | `B2_COMPARE_VR-010_WASHING_PLACE_V002_vs_V004.jpg` | `1Hl40ep9LfPsb2JqQCFjq6TCtTVrwtKnT` | 849,845 | 2200×1252 | `ebd609bd2c9255a5b5752e32d4599d8d` | `1318f2f08111affad24b8c8831b2183e5e23387ee0e63406b8d94fabd77adbda` |

The staged copy of V002 was MD5‑verified against Drive before use (`8e31b7c4…` exact). V003 was inspected only to understand the rejection; nothing from it was copied. V001 and V002 are untouched; V003 stays exactly as rejected.

## 2. Method and its limit

A **masked repaint**, not a hand retouch. The artwork panel `(60,152)–(1960,1244)` (1900×1092) was cut from V002; one generative pass was given a 860×572 crop of the *wet ground only* (panel `760,520`–`1620,1092`) and instructed to replace the bright runoff line with plain damp earth — no channel, ditch, trench, rut, hole, cavity, niche, object or figure. The render came back at 1264×841, aligned to the crop at offset `(0,0)` (no shift needed; framing preserved), tone-matched per channel on a plain-earth patch (`(45.4, 30.0, 21.0)` before and after), and composited through a 46 px-wide band mask drawn on the measured channel centreline, feathered 22 px. Mask footprint 102,873 px (48,583 at full strength).

**Inside that corridor the pixels are the generator's.** It is damp earth, so the repaint is low-risk, but it is not V002's grain and the disclosure stands.

## 3. Defect-by-defect closure

| # | Report defect | What the exported file shows | Evidence |
|---|---|---|---|
| 1 | Slab shrunk, recessed, darkened | Full-scale flat stone slab, unmoved and unaltered | **0 changed px** across the slab |
| 2 | Enclosed dark recess / shrine-like cavity at wall base | No recess, niche, alcove or cavity anywhere in the frame | No such form exists; region inspected 1:1 |
| 3 | Objects inside the recess | None added. No vessel, stone or object at any drainage point | 0 changed px in pots / dipper / leaf / sticks / straw |
| 4 | Lost trough, bucket, splash-ground | Water pot, dipper, leaf, chewing sticks, straw and damp splash earth all V002 | **0 changed px** |
| 5 | Left screen / compound-wall drift | Screens, posts and wall unaltered | 0 changed px across every screen face |
| 6 | Excess excavated trench | Bright line gone; plain damp earth, no ditch, trench, groove or rut | Corridor before/after on the board |
| 7 | Stale `V002` header on a `V003` board | Header reads `ENV_HOME_SETTLEMENT_WASHING_PLACE_V004`; `STATUS: REVIEW REQUIRED`; `CORRECTED SINCE V002` and `KNOWN ISSUES` rewritten; footer states the outlet is a fictional choice, not documented Igbo precedent | Chrome crop; width assertion at build time |

## 4. Declared deviation — read this before judging the drain

The report asks for the runoff to grade into **"a plain, open, low, ground-level drainage pass-through / gap at the base of the compound wall"**. No such pass-through is drawn, and I am not claiming otherwise:

- In this camera the drain's exit is bounded by the **woven palm-mat screen**, not by a mud compound wall. The only mud wall in frame is far left, up-slope from the water, and grading the runoff toward it would be physically false.
- Cutting a gap or opening into the screen base, or inventing a wall base to open, would mean drawing either a recess (explicitly prohibited) or architecture that V002 does not contain.
- So the correction is the authorised half only: **the exposed channel is removed and the yard reads as a flush damp grade that seeps into the screen's shadow.** The outlet is off-frame.

If the CD wants a visible low gap at the screen base, or the camera re-staged so a wall base is in shot, that is a further authorised change and needs its own version number.

## 5. Chrome and cultural honesty

- Header `…_V004`, status `REVIEW REQUIRED` — never approved.
- Footer rewritten: *"Any plain open wall-base drain outlet is a fictional design choice, not documented Igbo precedent: Basden records distant water sources and surface catch-pits, not wall outlets."* The board no longer implies ethnographic documentation for the outlet.
- Column and footer typography are re-set in DejaVu Sans at the measured metrics (labels 19 px bold, body 19 px, footer 13 px auto-wrapped); glyph shapes differ slightly from the original typeface even where widths match. Width limits asserted at build time (`<2545` column, `<1945` footer) and confirmed visually.

## 6. Verification

- Total changed pixels vs V002: **113,314**. Inside the repaint corridor: **46,197**. Outside corridor + metadata column: **0**.
- Protected zones re-measured at zero change: stone slab, pots/dipper/leaf/sticks/straw, screens, left mud wall, sky/bamboo.
- The candidate is 2560×1440, same frame geometry as V002; the panel box is unchanged.

## 7. Status

Candidate only. Review required. Nothing here is approved, promoted, filed or canon. V002 remains the visual authority; V003 remains rejected and untouched; V001 preserved.
