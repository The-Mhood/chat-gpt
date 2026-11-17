# CANDIDATE REGISTER — B2 (staged-master batch)
**Five candidates produced from verified full-resolution masters. Two tasks stopped on a stated non-access blocker. One Batch‑1 claim withdrawn.**
**Nothing is approved, uploaded, promoted or filed. Every original and every prior version is preserved.**

Companion documents: `STAGING_LEDGER.md` (filenames, Drive IDs, parents, sizes, dimensions, MD5/SHA‑256 for every source, staged copy and candidate).

---

## 0. Three corrections to my own Batch 1 record — read this first

Working from the proofs led me to two wrong statements. They are withdrawn here, not quietly dropped.

1. **VR‑008 "the costume drifted, restore the bare midriff".** There was no costume drift. The V004 and V005 boards both show the same blue top with the torso covered; my reading of the 949×488 panel invented a difference. Batch 1 therefore made a change the CD never asked for — precisely the "unrelated design change" I was told not to make. **The Batch 1 VR‑008 proof is superseded and its costume change is void.** *[Amendment, 2026‑11‑17 — this paragraph is itself wrong and is left visible. The rejection report for V006 establishes that the bare midriff **is** a real defect in V005, and that my "same full tunic" reading was a thumbnail artefact. See §9.]* The master also lists only two issues: the crack is hard to see, and the sheath hangs slightly forward.
2. **VR‑007 "bare blade on the bed corrected".** That was V003's fault, not V002's. V002 has no blade on the platform and never did. The Batch 1 proof invented a defect to fix alongside the real one.
3. **A Drive ID was transcribed short.** `1j2kAFeCyh0ejCss53o3wrUcIKgTXvR` → correct `18j2kaAFeCyh0ejCss53o3wrUcIKgTXvR`. It returns a 404 and stopped the first staging call. Corrected in `B1-04` and in `CANDIDATE_REGISTER_BATCH1.md`. **Every ID in this batch was re-found by search and re-verified by `get_file` before use; none was taken from my own notes.**

The lesson is on the record: proofs at review-board resolution are not adequate for judging detail on a figure.

## 1. Two requested versions do not exist

The authorisation names an **Establishing V006 master** and a **Wall of Houses V004 master**. Neither exists in Drive. A name search returns V001–V005 for Establishing (highest V005) and V001–V003 for Wall of Houses (highest V003). V006 and V004 are the *target* version numbers named on the boards themselves, not sources. I treated the highest existing master as the source and the requested number as the output version, and say so on both comparison boards. If the CD intended something else, both tasks stop here.

## 2. Staging controls — met

| Control | Result |
|---|---|
| Exact canonical file, ID verified before download | Yes — all eight re-found by name search, IDs copied from the result |
| Separate copy, canonical untouched | Yes — connector download; no move, rename, overwrite or re-upload |
| Filename preserved | Yes, in `masters/` |
| MD5 source vs staged | **8 of 8 exact matches** |
| SHA‑256 | Recorded for every staged copy and candidate. Drive does not expose SHA‑256 through this connector, so MD5 is the source-side check |
| Dimensions | 8 of 8 at 2560×1440; artwork panel identical on all eight: `(60,152)–(1961,1321)` = 1901×1169 |

## 3. Method — and why it matters for how you read the candidates

The panel box is the artwork at native size; the rest of the 2560×1440 file is board chrome, metadata column and palette. I corrected **the panel**, then re-inserted it into the untouched master frame. Pixel comparison outside the panel returns **0 changed pixels** on all five candidates, so nothing but the artwork moved.

Two different methods were used, and the difference is the honest headline:

- **Hand retouch (VR‑008).** I edited the master's own pixels. Costume, face, light, framing and every object are bit-identical outside the crack. This is the only candidate in the batch with no generative drift at all.
- **Generative pass (the other four).** The generative editor was given the master panel as reference and an exact instruction. It returns a 1301×800 render that I resample to the 1901×1169 panel. **It cannot preserve pixels.** Every candidate from this method therefore has secondary drift, listed per asset. This is not a defect of the brief; it is the limit of the tool.

## 4. Delivered candidates

### VR‑008 · `COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL` · V005 → **V006 candidate**
| | |
|---|---|
| Source | V005 `1VO2hsx_J3u-qD174V-5M-SWRJPtu8Gxu`, MD5 `a94a084af0f7fb6d8016a6e33d44dc62` |
| Candidate | `final/CAND_VR-008_2560x1440.png` · 2560×1440 · MD5 and SHA‑256 in the ledger |
| Defect addressed | master board: *"the crack in the seal is hard to see"* |
| Change | the faint existing fracture was deepened, displaced sideways, branched and given a lit lip — a real fracture across the plaster, below and beside her palm |
| Drift | **none.** 8,811 changed pixels confined to x 408–553, y 450–995. Outside that region the maximum difference is JPEG noise |
| Residual | the crack is now more prominent than "subtle legibility". If the CD wants it quieter, that is a tone pass on one layer |
| Recommendation | **CANDIDATE READY FOR REVIEW** — the strongest item in the batch |

Reviewers: is the crack unmistakable at normal size, without reading the title? Is it still a crack in mud plaster rather than damage to the building? Is her right hand still flat on the seal? Is the costume unchanged from V005?

### VR‑010 · `ENV_HOME_SETTLEMENT_WASHING_PLACE` · V002 → **V003 candidate**
| | |
|---|---|
| Source | V002 `1hhIXVq3wj3JPkfBHIMwrNLPAyr0JByWh`, MD5 `8e31b7c4200a375a90157f195b1e0c0e` |
| Candidate | `final/CAND_VR-010_2560x1440.png` |
| Defect addressed | master board: *"the drain still runs across open ground"* |
| Change | the channel now ends in a stone-lined culvert mouth at the foot of the compound wall and passes under it; the open yard floor is unbroken damp earth |
| Drift | the palm-frond screen weave is more open and more regular; the wall reads slightly redder; the background tree line is more visible; jar and cup positions and the chewing sticks shifted slightly |
| Preserved | standing stone, leaf-and-soap, sponge, screen height above head on both sides |
| Recommendation | **CANDIDATE READY FOR REVIEW.** The *filing* question is untouched: D13 and the board's location outside the canonical folder are separate and still open |

### VR‑011 · `ENV_GATES_DEAD_LANDING_OF_UNCLAIMED` · V001 → **V002 candidate**
| | |
|---|---|
| Source | V001 `1RCfI7x3fOF2dWFV27luo1-EFBIPVi3yN`, MD5 `2e94fd13ae204c1b9e0de795de31df51` |
| Candidate | `final/CAND_VR-011_2560x1440.png` |
| Defects addressed | all three on the master board: cloth reading as flags; canoes fewer than "hundreds"; river too bright against the bank |
| Change | every strip now hangs straight down from its pole as limp rectangular cloth; the canoe field is far denser in overlapping receding rows; the water is darker and calmer |
| Drift / residual | the strips read as uniform pale cloth and their rhythm is more regular than a hand-tied line; poles are barely visible; the far edge of the canoe field is still findable; the foreground canoe's cargo has changed |
| Standing | Chapter 7 remains **PROPOSED**. No claim about burial practice or belief is made by this image or by me |
| Recommendation | **CANDIDATE READY FOR REVIEW** |

### ESTABLISHING · `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING` · V005 → **V006 candidate**
| | |
|---|---|
| Source | V005 `1qi7TsLi5v8pfM4mHYLWvJEaSdPPyl_qW`, MD5 `6f32d454bb7b6f15ce31e3bffa136385` |
| Candidate | `final/CAND_ESTABLISHING_2560x1440.png` |
| Defects addressed | *"the mound is still too regular a cone and does not yet match WALL_OF_HOUSES_V003"*; *"the one house in warm daylight (Nneka's) is not visible"* |
| Change | the mound is rebuilt as an irregular stack of individual houses with stepped shoulders, jutting blocks, ladders and stair runs; one low house carries warm low sunlight while the rest stay in haze |
| **Additional change declared** | the generative pass placed a small standing figure in a yard. "Figureless by client decision (OAD‑40)." I removed it by hand — a change beyond the brief, made to keep the asset compliant, not a design decision |
| Drift | the overhead reflection of the settlement is more abstract than V005; palette warmer; foreground compound layout differs |
| Recommendation | **CANDIDATE READY FOR REVIEW** — still EXPLORATORY, NOT APPROVED CANON |

### WALL OF HOUSES · `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_WALL_OF_HOUSES` · V003 → **V004 candidate**
| | |
|---|---|
| Source | V003 `1LxVWK8D6nNYUF8oqC0pCMxsrBEK_XspN`, MD5 `1ee728c2bae54ae5284959ca5e747943` |
| Candidate | `final/CAND_WALL_OF_HOUSES_2560x1440.png` |
| Defects addressed | *"several houses are two-storey blocks"*; *"the first settlement at the foot is not distinct"*; *"sealed doorways do not read at this distance"* |
| Change | every building is single-storey with one roof and one opening; the foot of the mound carries separate freestanding houses with gaps and paths; the sealed doorways are pale plastered panels, one with a clear fracture |
| Drift | fog heavier at the top than V003; palette redder; mound silhouette broader |
| Recommendation | **CANDIDATE READY FOR REVIEW** — still EXPLORATORY, NOT APPROVED CANON |

## 5. Stopped tasks — VR‑007 and VR‑006

Both masters were retrieved and verified. **The blocker is method, not access, and it is specific.**

The required change is a *shortened sheathed weapon on an approved figure*. Two things are true:

1. **The generative editor will not do it.** I gave it the full master panel and an explicit geometric instruction twice per asset. VR‑007 came back with the sheath turned into a **bare tapered blade** plus a diagonal chest strap and arm bands that are not on the character. VR‑006 came back with the weapon **longer**, still blade-like, the figure pushed to the frame edge and the costume changed. Both attempts are retained in `cand_panels/` and are **offered as nothing**. The CD's own board already records this: *"The image generator did not shorten it when asked"* and *"Correct the scabbard by hand on this image, since two edits have not shortened it enough."*
2. **A hand retouch of this object is beyond what I can do without risking the approved image.** The sheath, its bronze band, its tapered tip and the spiral chape disc overlap skirt folds, belt, platform shadow and — in VR‑006 — the mortar. Removing the lower section means rebuilding cloth and shadow behind it. I could produce something, but not something I would put in front of a reviewer as an improvement on an approved figure.

So instead of a bad candidate, two **retouch guides** carrying the measurements a retoucher needs, so the job takes minutes rather than another round of briefing:

- `guides/RETOUCH_GUIDE_VR-007.jpg` — pommel (1545,690); chape disc (1357,940); sheath 383 px ≈ a 90–100 cm blade; **target tip on y 865** (≈70% of current length, above mid‑thigh); re‑seat the chape at the new tip; rebuild skirt and platform shadow behind the removed section.
- `guides/RETOUCH_GUIDE_VR-006.jpg` — hilt (1560,622); current tip (1760,782), angled back behind the mortar; **target: vertical from the hilt, tip at or above (1600,880)**, mortar and pestle untouched and in front.

Also not attempted, and not needed to unblock anything else: the blade board's status is still **CQ‑9 unresolved**, so I have not treated `WEAPON_ADANNA_PRIMARY_BLADE_V001` as approved even though every master board footer calls it that. F4 shields remain blocked on **CQ‑8** (decide OAD‑18 first).

## 6. Status of every item

| Asset | Status |
|---|---|
| VR‑008 V006 candidate | CANDIDATE READY FOR REVIEW |
| VR‑010 V003 candidate | CANDIDATE READY FOR REVIEW |
| VR‑011 V002 candidate | CANDIDATE READY FOR REVIEW |
| ESTABLISHING V006 candidate | CANDIDATE READY FOR REVIEW |
| WALL OF HOUSES V004 candidate | CANDIDATE READY FOR REVIEW |
| VR‑007 | CORRECTION IN PROGRESS — blocked on retouch method; guide issued |
| VR‑006 | CORRECTION IN PROGRESS — blocked on retouch method; guide issued |
| Batch 1 proofs, all five | SUPERSEDED by this batch — retained, not deleted |
| VR‑008 Batch 1 costume change | WITHDRAWN — it was never a defect |
| F4 shields | RESEARCH REVIEW REQUIRED (CQ‑8) — untouched |
| Field of Cloth | RESEARCH REVIEW REQUIRED (RQ‑01) — untouched |

No candidate inherits approval from its predecessor. A rejected version stays rejected. Nothing here entered a canonical collection, and nothing will without CD approval **and** separate filing authorisation.


---

## 9. VR‑008 V007 — revision produced after rejection (2026‑11‑17)

V006 was **REJECTED — REVISION REQUIRED**. The response is a new version, V007, produced by targeted hand retouch on the V005 master panel with no generative pass. Full defect-by-defect answer: `B2_REJECTION_RESPONSE_VR-008_V006.md`.

| | |
|---|---|
| Source | V005 `1VO2hsx_J3u-qD174V-5M-SWRJPtu8Gxu`, MD5 `a94a084af0f7fb6d8016a6e33d44dc62` (re-verified) |
| Midriff donor | V004 `1WnpmzTUhiHxjepd_iasZHRoJsGbO64jg` — **same frame** as V005 (landmark correlation 0.805 at scale 1.01, offset +6,+6), so the bare midriff is a copy‑back, not a painting |
| Candidate | `final/CAND_VR-008_V007_2560x1440.png` · 2560×1440 · 3,126,132 B · MD5 `8e493590c632a545ff8d198316cd67b5` · SHA‑256 `0763fd75a9982c2237238b5e7cc35b7e21dc12d2fc63ce297048c3f7667dd9a7` |
| Defects answered | A synthetic crack → plaster fracture grown from the authentic lower‑right fissure; B missing bare midriff → restored from V004; C missing armlet → five‑coil dull aged‑bronze armlet on the LEFT upper arm only; D stale chrome → header V007, obsolete crack line removed, READ now true, footer no longer claims an approved blade board |
| Pixel proof | 13,618 changed pixels, **all** inside the three masks (fracture 1,504 · midriff 8,481 · armlet 3,633); **0** outside. Chrome 18,794 px, enumerated separately |
| Drift | none generative. The only non‑pixel‑exact transfer is the 1 % resample used to align V004 into V005 |
| Known limitation | the armlet is a **painted reconstruction** — the approved reference has no clean multi‑coil band to transfer (its "armlet" detail plate renders a spiral disc). A dedicated armlet plate is needed if a photographic armlet is required |
| Status | **CANDIDATE — REVIEW REQUIRED.** Not approved, not canon, not filed, not a master |

**Retraction of my retraction.** V006's rejection proves defect B was real. My statement that "V004 and V005 both show the same blue top with the torso covered" was wrong, it caused the midriff to be dropped from V006, and it is the reason V006 was rejected. It stays on the record here and in §0.

**VR‑010 stays stopped.** No rejection report for it exists anywhere in Drive (rejected area holds three files; `search_files 'REJECTION'` returns one report). Correcting it now would mean inventing its defect list — the failure that produced V006.
