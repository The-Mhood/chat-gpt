# ERRATA & V008 — VR-008 `COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL`

**Filed 2026-11-17, after V007 was submitted and before any review verdict on it.**
This document records an error in my own V007 submission package and the new version that corrects it. Nothing here is an approval, and nothing here withdraws V007 — the reviewer decides which record stands.

---

## 1. What I got wrong

In `B2_REJECTION_RESPONSE_VR-008_V006.md` §2C and in the V007 register and ledger I wrote:

> "the armlet is a **painted reconstruction** — the approved character sheet has no usable multi-coil band to transfer (its 'armlet' detail plate renders a spiral disc)."

**That statement is false, and I have corrected it.**

Two separate things are true:

1. The **detail plate on `CHAR_ADANNA_MASTER_REFERENCE_V001` captioned "COILED BRONZE ARMLET" is mislabelled.** At native resolution (`x 1145–1545, y 915–1265` of the 2560×1440 sheet) it shows a rivetted leather strap and a spiral bronze stud plate — not coils. That much of my note was right.
2. **The master portrait itself carries a clean, usable multi-coil armlet** at native resolution, `x ≈ 590–800, y ≈ 1045–1120`, on Adanna's left upper arm. Roughly nine wires, sharp specular crests, dull aged patina, and the far end already falling into shadow.

I inspected the detail plate and concluded "no transferable patch" **without checking the portrait's own arm**. That is exactly the thumbnail-versus-full-resolution error I had already been corrected for once in this project, repeated in a different form. The correct statement should have been: *the detail plate is mislabelled, but the portrait supplies a transferable band.*

## 2. What that did to V007

V007's armlet is a five-coil painted band. The approved master shows about nine finer coils and a distinctly different crest/groove rhythm. Defect C of the rejection report asks the armlet to match the master's **coil count, width, dull aged patina and overcast sheen**. V007 does not meet the coil-count requirement. It was not merely "reconstructed": **it was reconstructed from a reference I failed to find.**

## 3. V008 — the correction

| | |
|---|---|
| File | `B2_CAND_VR-008_SEALED_QUARTER_V008_2560x1440.png` |
| Size | 2,560 × 1,440 · 3,129,530 B |
| MD5 | `a41548911b4d991e7e05aad6474441aa` |
| SHA-256 | `cfc2788fa7c0762b86d76f24c6b7cebb214cf9cc4242b51c9a778365f4e3df4e` |
| Status | **CANDIDATE — REVIEW REQUIRED.** Not approved, not canon, not filed, not a master. |

**Only the armlet changed.** V008 is V007 with the painted band removed and a transfer put in its place:

- Source: `CHAR_ADANNA_MASTER_REFERENCE_V001.jpg` (`1FY3hw3602iB-1405RgUIO3ih2USmck_Y`, MD5 `901a5009ab5ff44a81fb3799c7e6de6d`), crop `(580, 1010)–(800, 1140)`.
- The band is levelled by **7.6°** (measured from its own top edge), cut to `(45, 46)–(200, 110)` of the rotated crop, then scaled to this arm's width — 74 × 29 px — because in V005 the arm is a third the width it is in the close-up portrait.
- Graded to the scene: source mean luminance 23.9 → 31.4, set to 0.86 × the local arm mean so the metal sits in the overcast shade rather than glowing.
- Masked to the arm, faded over 6 px at each silhouette edge, with a 2.6 px bow so the rings dip as the arm turns away, plus a soft occlusion above and below so it sits *in* the arm.

**Fracture (A) and bare midriff (B) are unchanged from V007.** The chrome is re-issued for V008: header reads `V008`, and the footer note states that the armlet is now a transfer rather than a painting.

## 4. Verification — measured on the exported file, not on the working layers

| Check | V007 | V008 |
|---|---|---|
| Changed px vs V005 | 13,618 | **12,194** |
| — inside fracture mask | 1,504 | 1,504 |
| — inside midriff mask | 8,481 | 8,481 |
| — inside armlet mask | 3,633 | **2,209** |
| — **outside the three masks** | **0** | **0** |
| face + head | 0 | 0 |
| braids, 3 cuffs, 2 coral beads | 0 | 0 |
| right hand flat on the seal | 0 | 0 |
| bowl + pot | 0 | 0 |
| skirt and belt below the hip | 0 | 0 |
| right-side huts | 0 | 0 |
| left doorway and plaster | 0 | 0 |

**V007 → V008 = 4,092 changed pixels, all inside the armlet mask, bounding box `(998,545)–(1076,620)`.** Nothing else moved.

## 5. Provenance corrections required by the report's §8 addendum

The updated rejection report adds a provenance clarification that my earlier documents did not carry. It is now recorded here and in the register and ledger:

| Version | Drive ID | Provenance | Status |
|---|---|---|---|
| **V005** — working visual base | `1VO2hsx_J3u-qD174V-5M-SWRJPtu8Gxu` | **Handover branch only**: `20_PREVIOUS_VISUAL_AGENT_WORKSPACE_HANDOVER` (`17ZOOMRXHYWE1DKBYJUG9rdhjCrapFB1X`) → `THE_DISOBEDIENT_DAUGHTER_ART_BIBLE` → `15_EXPLORATORY_DESIGNS` → `Chapter_08_Character_Compositions` | **Not canonical.** 627,020 B, MD5 `a94a084af0f7fb6d8016a6e33d44dc62`. Must not be described as canonical; not to be refiled without separate CD/TD authorisation. |
| **V004** — canonical exploratory copy | `1WnpmzTUhiHxjepd_iasZHRoJsGbO64jg` | Canonical `15_EXPLORATORY_DESIGNS` (`1S3KUeDS9nU6FBPFP3akG5YlJpVZvMdzM`) → `Chapter_08_Character_Compositions` (`1ywTZAOGDsIa7Ia713CT21IV2CyWUiVZO`) | 653,046 B, MD5 `222329587e39160d9a95bea007ed08df`. Unapproved exploratory version. |
| **V004** — handover duplicate | `16skVffhrXaNJ83Na0myt6bYdB6PEGSHQ` | Handover branch, same path | Byte-identical to the canonical copy |

My midriff donor was a **derived panel crop** (`panels/…_V004_PANEL.jpg`, MD5 `9d6dce30bb25641efe43c25e4c195132`) taken from the canonical V004; the crop is a working artefact, not a source of record.

## 6. Rejected-area state — monitored, corrections not started

At the time of this filing, `16_REJECTED_DESIGNS` (`1x5T4V3R-hnuUNCIFBIb1TBIezjlT0Q6c`) holds **five** files:

1. `B2_CAND_VR-008_SEALED_QUARTER_V006_2560x1440.png` (`1hIHmhNA…`) — with its report.
2. `REJECTION_REPORT_VR-008_SEALED_QUARTER_V006.md` (`1GvAyGki…`) — **updated to 18,150 B, MD5 `4218a8af…`**, now including the §8 provenance addendum.
3. `B2_CAND_ESTABLISHING_V006_2560x1440.png` (`145yfHTW…`) — **moved** here from the submissions folder; **no report yet**.
4. `B2_CAND_WALL_OF_HOUSES_V004_2560x1440.png` (`18ofv4cJ…`) — **moved** here from the submissions folder; **no report yet**.
5. `COMP_ADANNA_NNEKAS_YARD_FULL_FIGURE_V001.jpg` (`1FOjWc2E…`).

The submissions folder is therefore down from 23 to 21 files; both candidates kept their IDs and MD5s, and their comparison boards remain in place.

**Establishing V006 → V005 base and Wall of Houses V004 → V003 base are NOT started.** The candidates have been filed but the governing reports do not yet exist, so starting now would mean inventing the defect list — which is the failure that produced V006. I will begin the moment either report appears.

## 7. Files in this filing

| File | MD5 |
|---|---|
| `B2_CAND_VR-008_SEALED_QUARTER_V008_2560x1440.png` | `a41548911b4d991e7e05aad6474441aa` |
| `B2_COMPARE_VR-008_V005_to_V008_with_references.jpg` — V005 base, V004 midriff reference, CHAR armlet reference, V007 painted vs V008 transferred, fracture pair | `cdf09d5f7bf0ee321c971db371516c61` |
| `B2_ERRATA_VR-008_V007_ARMLET.md` | this document |
| `B2_CANDIDATE_REGISTER_v3_2026-11-17.md` | register, §10 |
| `B2_STAGING_LEDGER_v3_2026-11-17.md` | ledger, §6 |

V007 (`1-aBDr85OMCOluCSfOUwvIPk-eNcm9i3z`) remains in the submissions folder untouched. **Neither V007 nor V008 is approved; both stand as candidates and the reviewer decides which one the record follows.**
