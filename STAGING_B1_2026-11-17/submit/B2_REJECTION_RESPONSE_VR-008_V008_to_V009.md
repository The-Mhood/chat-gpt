# REJECTION RESPONSE — VR-008 SEALED QUARTER
## `B2_CAND_VR-008_SEALED_QUARTER_V009_2560x1440.png` — answers `REJECTION_REPORT_VR-008_SEALED_QUARTER_V008.md`

**Asset:** `VR-008` / `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_SEALED_QUARTER` — character-in-environment composition
**Candidate:** 2560×1440 PNG · 2,777,400 B · MD5 `b0c962b8a65b3c8bd0ad462efc73f32f` · SHA-256 `0b3b535d747d7f919472c95f089ef731083acedcfc40fc5eb63715961e7e38bb`
**Status:** `REVIEW REQUIRED` — visual development asset, unapproved, establishes no story event or canon
**Sources:** approved `ENV_..._SEALED_QUARTER_V003` (environment, untouched) · approved `CHAR_ADANNA_MASTER_REFERENCE_V001` (OAD-02, character lock) · `WEAPON_ADANNA_PRIMARY_BLADE_V001`

---

## 1. Item 1 — the pauldron is gone

The metal shoulder cap occupied `(1012,562)–(1152,698)`. It was removed by retouching that shoulder region and compositing the result back through a rounded-feather footprint mask, colour-matched to the surrounding skin (median shift `−7,−10,−4`).

The shoulder now reads as **bare brown skin crossed only by the plain dark-brown leather strap**, which is what `OAD-02` specifies: bare shoulders, plain leather strap, no metal armour of any kind. The strap crosses over the shoulder rather than stopping at the cap edge — the defect that made `V008` read as armoured.

**Bounding honest note:** the armlet sits just inside the blend feather. 191 px along its top edge move by up to 28 levels. That is mask edge, not a rebuild — coil count, thickness, tone and anatomical position are `V008`'s.

---

## 2. Item 2 — chrome

| Field | `V008` | `V009` |
|---|---|---|
| Header | `…_HAND_ON_SEAL_V008` | `…_HAND_ON_SEAL_V009` |
| `SOURCES` character line | `REF_ADANNA_MASTER_PORTRAIT_APPROVED_V001` | `CHAR_ADANNA_MASTER_REFERENCE_V001 (OAD-02)` |
| `ASSESSMENT` | "SUBMITTED FOR REVIEW. Supersedes V004, which is kept." | "SUBMITTED FOR REVIEW. Version 9. Bare shoulder and plain leather strap restored per OAD-02. V006–V008 are preserved, not deleted; this sheet supersedes V008 only." |
| `KNOWN ISSUES` | "…framing is a little tighter than V004." | "…Framing is carried from V008. Coiled armlet on an untitled young woman stays open (RQ-10-1); the hand-on-seal gesture is FICTIONAL and is not a documented Igbo ritual (U-11)." |
| Provenance | none | new `PROVENANCE` block: V009 version, pauldron removed per OAD-02, environment untouched from approved `SEALED_QUARTER_V003`, `V006–V008` preserved in `16_REJECTED_DESIGNS`, no story event or canon claimed |

Every stale `V004` reference is gone from the sheet. `LOCATION`, `SCABBARD CHECK` and the footer's visual-development disclaimer are unchanged — they were accurate.

---

## 3. Item 3 — verified gains preserved

| Gain named in the report | State |
|---|---|
| Warm natural skin tone (not `V007`'s ashen cast) | preserved |
| Natural braided silhouette with brass rings | preserved |
| Bare right shoulder | preserved |
| Left-upper-arm coiled bronze armlet, correct anatomical position | preserved (191 px of mask feather at its top edge only) |
| Untouched approved `V003` Sealed Quarter walls, seals, atmosphere | **0 px changed** |
| `FICTIONAL` / non-ritual framing (`U-11`), `RQ-10-1` open | preserved and now stated on the sheet |

---

## 4. Audit (`V008` → `V009`)

| Zone | `>2` | `>12` | max |
|---|---|---|---|
| Pauldron footprint `(1000,555)–(1170,710)` | 22,801 | **12,834** | 195 |
| Armlet band `(1020,700)–(1140,762)` | 863 | 191 | 28 |
| Art, figure `(700,300)–(1200,1300)` | 23,182 | 12,834 | 195 |
| Art, environment left `(35,152)–(700,1300)` | **0** | **0** | 0 |
| Art, environment right `(1200,152)–(1930,1300)` | **0** | **0** | 0 |
| Chrome column `(1932,160)–(2560,1300)` | 206,421 | 117,126 | 233 |
| Footer band `y 1300–1440` | **0** | **0** | 0 |

Sheet total 148,467 px `>12`. The environment is bit-identical to `V008`, which is itself the untouched approved `V003`. All art change is inside the shoulder footprint.

---

## 5. Files

| File | Size | MD5 |
|---|---|---|
| `B2_CAND_VR-008_SEALED_QUARTER_V009_2560x1440.png` | 2,777,400 B | `b0c962b8a65b3c8bd0ad462efc73f32f` |
| `B2_COMPARE_VR-008_V008_vs_V009.jpg` | shoulder, armlet and chrome comparison | — |
| `B2_REJECTION_RESPONSE_VR-008_V008_to_V009.md` | this document | — |
| `B2_REGISTER_LEDGER_v12_2026-11-17.md` | queue state after this pass | — |

`V006`, `V007`, `V008` preserved untouched in `16_REJECTED_DESIGNS`. Nothing promoted, nothing deleted.

*Filed to `PENDING/ASSISTANT_VA_SUBMISSIONS` for independent Our Eyes inspection and an exact-version Research report on `V009`.*
