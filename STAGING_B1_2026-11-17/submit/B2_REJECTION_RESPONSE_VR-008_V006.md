# RESPONSE TO REJECTION — VR-008 `COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL`

**Rejected candidate:** `B2_CAND_VR-008_SEALED_QUARTER_V006_2560x1440.png` (Drive `1hIHmhNA…`, MD5 `cf577a35…`) — preserved, untouched, held in `16_REJECTED_DESIGNS`.
**Report answered:** `REJECTION_REPORT_VR-008_SEALED_QUARTER_V006.md` (Drive `1GvAyGki8oJYYTLfeXiYk-OST4d6AUzvB`, 15,037 B, MD5 `c01a2c95…`).
**Verdict answered:** REJECTED — REVISION REQUIRED. Correction owner: Assistant VA. Base: V005.
**Delivered:** **V007** — a new version, new filename, new hash. V005 and V006 are both preserved unchanged; nothing was overwritten, moved or deleted.

---

## 1. What V007 is

A targeted hand retouch of the **V005 master panel**, with no generative pass anywhere in the chain.
Source master: `COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005.jpg`, Drive `1VO2hsx_J3u-qD174V-5M-SWRJPtu8Gxu`, MD5 `a94a084af0f7fb6d8016a6e33d44dc62` — re-verified against the ledger before use.

| | |
|---|---|
| File | `B2_CAND_VR-008_SEALED_QUARTER_V007_2560x1440.png` |
| Size | 2,560 × 1,440 · 3,126,132 B |
| MD5 | `8e493590c632a545ff8d198316cd67b5` |
| SHA-256 | `0763fd75a9982c2237238b5e7cc35b7e21dc12d2fc63ce297048c3f7667dd9a7` |
| Status | **CANDIDATE — REVIEW REQUIRED.** Not approved, not canon, not filed, not a master. |

## 2. Defect by defect

### A — the synthetic crack (blocking)

**Action.** The V006 crack overlay was discarded entirely and the panel was rebuilt from V005. A new fracture was painted as plaster damage: a single trunk rising **from the authentic lower-right fissure** (≈ panel x 472, y 838) up beneath her palm to ≈ (489, 527), with four hairline branches, a 1.3 px edge displacement of the far side, granular mask edges broken by plaster-grain noise, a warm dark-umber crevice (RGB ≈ 30, 22, 17 — not charcoal, not black), and 46 micro-crumbled clay chips with a lit upper edge and a hairline cast shadow.

**What is not in it.** No vector stroke, no bevel, no emboss, no outer glow, no blurred halo, no larger Gaussian, no doorway collapse, no full-height line from the top edge, no crossing of the handprints. The previous V006 trunk sliced past the left handprints and ran the whole height; this one does not reach the top edge at all.

**Evidence.** Fracture mask: 1,504 changed pixels, all inside `x 425–528, y 512–862`. See `B2_PIXELDIFF_VR-008_V007.jpg`.

### B — the missing bare midriff (blocking)

**Action.** Not painted. The approved construction was **taken from V004** by aligned crop.

I first established that V004 and V005 are the **same frame**: a landmark correlation search over the torso window gives a best score of 0.805 at scale 1.01 with offset (+6, +6). That is why the transfer is a copy-back and not an invention: V004's wrap hem, bare midriff and belt line are the same pixels seen through a 1 % resample.

The patch (panel polygon x 856–980, y 618–760, 7 px feather) reproduces the short indigo wrap hem, the bare midriff and the top of the belt/hip wrap exactly as V004 shows them.

**Declared consequence.** Because the source is 1 % larger, the crop is resampled by 1 %, so the transferred midriff is very slightly softer than the surrounding pixels. Nothing else in the region was re-lit, re-coloured or re-drawn.

**Evidence.** Midriff mask: 8,481 changed pixels, all inside `x 852–1000, y 614–764`.

### C — the missing multi-coil bronze armlet (blocking)

**Action.** A five-coil aged-bronze armlet was restored on the **LEFT upper arm only**; her right arm remains bare and untouched (0 px changed).

The rings follow the arm as a cylinder: each coil is shaded as a wire (bright crest, tight dark groove), the ring boundaries bow 9 px across the arm so they dip at the silhouette, the band inherits the arm's own luminance so it takes the overcast light and dies away at both edges, and an occlusion shadow sits above and below it. Colour is deliberately low-chroma and dark — measured mean RGB (46, 37, 28), 90th percentile (87, 72, 53) — so it reads as dull patinated bronze, **not** gold.

**Limitation — stated plainly.** This is a **painted reconstruction, not a transfer.** I looked for an approved armlet patch to copy: the character master's detail panel captioned "COILED BRONZE ARMLET" actually renders a *spiral disc* on a leather strap, and the master portrait does not expose a clean multi-coil band at a usable size and angle. There was therefore nothing authentic to transfer. If the CD wants a photographic armlet rather than a reconstruction, the reference sheet needs a dedicated armlet detail plate first.

**Evidence.** Armlet mask: 3,633 changed pixels, all inside `x 996–1076, y 536–628`.

### D — stale board chrome

| Change | Detail | Pixels |
|---|---|---|
| Header version | `…_V005` → `…_V007` | 329 |
| Obsolete known issue | sentence "The crack in the seal / is hard to see." erased; the block now ends "a little tighter than V004." | 4,185 |
| `READ` | **left exactly as it was** — "guard, armlet, braid cuffs and blade all on her left" is now true, because the armlet exists | 0 |
| Footer blade claim | line 2 re-set: "reference; blade from the blade board — REVIEW REQUIRED, CQ-9 open: not an approved source. Not approved." The phrase "approved blade board" no longer appears | 7,979 |
| V007 note | two lines in previously empty chrome recording what V007 changed and the true weapon-board status | 6,301 |
| `STATUS: REVIEW REQUIRED`, `EXPLORATORY`, non-canon disclaimer, palette | untouched | 0 |

**Disclosure.** The board's original typeface is not available offline, so the re-set footer line and the V007 note are set in DejaVu Sans. At 100 % the letterforms differ slightly from the board's own type. Everything else in the chrome is original pixels. I judged a substituted typeface the lesser error against leaving a false approval claim on the board.

## 3. The report's pixel boxes do not land on the features

Recorded rather than quietly "corrected": at full resolution the boxes quoted in the report do not frame the features they name.

| Feature | Report box | Measured on the panel |
|---|---|---|
| Crack corridor | `x 396–566, y 439–1007` | corridor `x ≈ 430–520, y ≈ 520–860` (report box is centred correctly but spans nearly twice the height) |
| Midriff | `x 955–1165, y 685–795` | `x ≈ 856–1000, y ≈ 618–762` (offset ≈ +85 x, +45 y) |
| Armlet | `x 1085–1215, y 585–660` | left upper arm `x ≈ 996–1076, y ≈ 536–628` (offset ≈ +80 x, +35 y); the reported box sits on the shadowed hut wall beside the arm |

I matched the **described features**, not the numbers, and I did not move the armlet onto the wall to satisfy a coordinate. If the report's boxes were expressed in a different frame, that should be reconciled before the next cycle so both sides measure the same way.

## 4. Preservation — verified, not asserted

| | |
|---|---|
| Changed pixels on the panel | **13,618** of 2,222,269 (0.61 %) — fracture 1,504 · midriff 8,481 · armlet 3,633 |
| Changed pixels **outside** the three masks | **0** |
| Chrome pixels changed | 18,794, enumerated in §2D |
| Untouched | face, expression, scar, braids with 3 bronze cuffs and 2 coral beads, right arm and hand flat on the seal, pose, silhouette, framing, `SEALED_QUARTER_V003` architecture, bowl and pot, mist, palette, left-hip sheathed weapon, leather belt, skirt construction |
| Not done | the minor notes (forward scabbard angle, spiral pendant) were **not** touched, per the report's instruction that they are not grounds to regenerate; `U-18` scarification remains open; no ritual reading is asserted for the hand-on-seal `[X]` |

## 5. Still true, still unresolved

- **Not approved.** A candidate returning through the normal cycle. Research `[B]` on the armlet stands; the armlet's *presence* is required by the brief, its *form* is my reconstruction.
- **CQ-9 open.** The weapon still comes from a board that is REVIEW REQUIRED. V007 does not resolve it and does not claim to.
- **My earlier disclosure stands.** My Batch-1/B2 statement that "V004 shows the same full tunic" was wrong. The rejection report's defect B was correct, and this file is the correction of my correction.

## 6. Files in this submission

| File | Purpose | MD5 |
|---|---|---|
| `B2_CAND_VR-008_SEALED_QUARTER_V007_2560x1440.png` | the candidate | `8e493590c632a545ff8d198316cd67b5` |
| `B2_COMPARE_VR-008_V005_vs_V007.jpg` | before/after board with the three detail pairs | `ad788e8f6c871f3e99104fc467e950d1` |
| `B2_PIXELDIFF_VR-008_V007.jpg` | difference map with the three masks boxed | `242fc74f89f384ac870877d866c059da` |
| `B2_REJECTION_RESPONSE_VR-008_V006.md` | this document | — |
| `B2_CANDIDATE_REGISTER.md` | register, updated §V007 | — |
| `B2_STAGING_LEDGER.md` | ledger, updated §V007 | — |

---

## 7. VR-010 — blocked, and why

**`ENV_HOME_SETTLEMENT_WASHING_PLACE` cannot be corrected in this cycle because no rejection report for it exists.**

Checked, not assumed:

- `list_files` on `16_REJECTED_DESIGNS` (`1x5T4V3R-hnuUNCIFBIb1TBIezjlT0Q6c`) returns exactly three files: the rejected V006 candidate, `COMP_ADANNA_NNEKAS_YARD_FULL_FIGURE_V001.jpg`, and the single VR-008 rejection report.
- `search_files 'REJECTION'` across Drive returns that one report and nothing else.
- No rejected VR-010/V004 candidate is present in the rejected area.

The authorisation makes the report a precondition: correct from **V002 as base**, fix the drain, remove the invented cup, leave the right-side exit alone, add no cultural or ritual objects. Without the report I would be inventing the defect list and the target version — the exact failure mode that produced V006. So VR-010 stays stopped with the blocker stated, rather than guessed at.

**Unblock action:** file the VR-010 rejection report. On sight of it I will work from V002 and answer it point by point.
