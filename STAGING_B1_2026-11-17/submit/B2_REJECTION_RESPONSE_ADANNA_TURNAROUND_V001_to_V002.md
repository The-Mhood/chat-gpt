# B2 — REJECTION RESPONSE: ADANNA TURNAROUND V001 → V002

**Asset set:** `CHAR_ADANNA_TURNAROUND_{FRONT,LEFT_SIDE,BACK,THREE_QUARTER}`
**Supersedes:** V001 (rejected by Our Eyes). V001 is preserved, untouched, in `16_REJECTED_DESIGNS`.
**Status of the V002 set: UNAPPROVED — PENDING REVIEW.** These are candidates, not approved assets.
**Date:** 2026-11-17 · **Batch 1** · Branch `arena/90e15011-chat-gpt`

---

## 1. What was read before drawing

| Document | Drive ID |
|---|---|
| Rejection report, FRONT V001 | `1aZ6yQs1u1dt4ONAX4c6ZsISD-kOav3Dj` |
| Research assessment, FRONT V001 | `1HmTGfbIYHOauokBtsias3yL1CfPwVGWw` |
| Approved master, `CHAR_ADANNA_MASTER_REFERENCE_V001` (OAD-02) | `1k08XH8VjNJAnSoMNU4YvBPtBEUdYD20y` |

Sibling reports (LEFT_SIDE / BACK / THREE_QUARTER) were queued for the same brief; the five
correction items and the OAD-02 lock list below are the shared brief and are applied to all
four plates as one set, per item 4.

## 2. The five correction items, and what V002 does

| # | Rejected V001 defect | V002 |
|---|---|---|
| 1 | `"APPROVED"` baked into the artwork header | Removed from art. Every plate carries the neutral line **UNAPPROVED — PENDING REVIEW** in the chrome and repeated at the foot. Nothing in the artwork asserts approval. |
| 2 | Temple callout said `"Right temple"` while the lock is the LEFT temple | Callout reads **brass cuffs + coral beads, LEFT temple (viewer-right in this view)**. The beaded braids are painted on the viewer's right in FRONT and THREE QUARTER, on her left arm-side in LEFT SIDE, and left of the nape midline in BACK. |
| 3 | Baldric diagonal routed differently from view to view; scabbard contradicted its own label | One route in all four plates: **over her RIGHT shoulder, across to her LEFT hip**. No blade and no scabbard is depicted anywhere in the set — see §4. |
| 4 | Four views not orthographically aligned | All four plates built at 2560×1440 from one scale: measured **crown row 57 in all four**, floor rows 1155–1159, body height 1099–1103 px (spread 4 px = 0.4 %). Numbers in `turn_audit.json`. |
| 5 | OAD-02 locks not held across the set | Lock-by-lock check in the right-hand column of every plate; summary in §3. |

## 3. OAD-02 lock check

| Lock | Result |
|---|---|
| Facial likeness, deep brown skin | Held — generated from the approved master only. |
| Thin braids, high braided knot | Held in all four views. |
| 3 brass cuffs + 2 coral beads, LEFT temple | Held — side corrected in every view. |
| Thin scar, LEFT cheekbone | Held — visible in FRONT, LEFT SIDE, THREE QUARTER. |
| RIGHT temple and cheek plain | Held. |
| Coiled bronze armlet, LEFT upper arm | Held — single band, all four views. |
| Bare shoulders, no armour | Held — no pauldron, no piece of armour anywhere. |
| Plain dark-brown diagonal leather baldric | Held — no metal fittings added. |
| Indigo hand-woven bandeau and wrap | Held, same indigo pair across the set. |
| Leather sandals | Held. |
| Spiral bronze pendant (FICTIONAL, mother's) | **Not visible** in any of the four views — the baldric and the bandeau line sit where it hangs. Lock left intact, not removed; flagged, not invented. |

## 4. Open item: the blade — CQ-9 stays OPEN

The OAD-02 lock places the blade on her **left hip** for a right-hand cross-draw. Three
generation passes from the master reference each put the scabbard on her **right hip**, i.e.
the opposite side from both the lock and the baldric's own terminus — which is precisely the
V001 defect Our Eyes caught (a blade drawn on one side, labelled on the other).

Filing that a fifth time would repeat the defect knowingly. Instead V002 shows the baldric
only, no weapon, and puts the side to Our Eyes: **CQ-9 OPEN — blade / scabbard mechanics and
worn side.** The baldric route is drawn to the left-hip terminus, so a scabbard can be added
under a settled decision without re-routing the strap. Nothing about blade mechanics has been
invented; `WEAPON_ADANNA_PRIMARY_BLADE_V001` is untouched.

`RQ-10-1` (coiled armlet on an untitled young woman) remains open and is not asserted here.

## 5. Files submitted

| File | Bytes | MD5 |
|---|---|---|
| `CAND_CHAR_ADANNA_TURNAROUND_FRONT_V002_2560x1440.png` | 2,271,157 | `34caa613508ae109ee70c7315bed43da` |
| `CAND_CHAR_ADANNA_TURNAROUND_LEFT_SIDE_V002_2560x1440.png` | 2,424,992 | `fb3b7a8dc6ec0249473c77419dfa148e` |
| `CAND_CHAR_ADANNA_TURNAROUND_BACK_V002_2560x1440.png` | 2,551,281 | `fda3d2f0a850d5e097ff8d1c9405386f` |
| `CAND_CHAR_ADANNA_TURNAROUND_THREE_QUARTER_V002_2560x1440.png` | 2,411,772 | `c6b704775d6eb0a78eb0c4fa6fb990eb` |
| `B2_COMPARE_ADANNA_TURNAROUND_V002_alignment.jpg` (2580×823) | 277,898 | `2c2952fe5ea6b131fb68067ff7b8c652` |

Provenance: generated from `CHAR_ADANNA_MASTER_REFERENCE_V001` and the written OAD-02 locks;
the rejected V001 was read for its defect list only and was not used as a generation source.
No approved folder was written to, no canon changed, no candidate approved. Establishes no
story event.
