# CANDIDATE REGISTER — B2 — **v4 addendum, 2026-11-17**
## The two environment rebuilds: Establishing **V007** and Wall of Houses **V005**

Supersedes nothing. Rows for the other five candidates (VR‑008 V008, VR‑010, VR‑011 and the superseded V006/V004 environment candidates) stand as recorded in `B2_CANDIDATE_REGISTER_v3_2026-11-17.md`.
**Nothing here is approved, promoted, filed or canon. Every prior version is preserved. Status of both new files: REVIEW REQUIRED.**

---

## 1. Authorisation and sources

| | Establishing | Wall of Houses |
|---|---|---|
| Authorised output | **V007** | **V005** |
| Rejected version (not used as a master) | V006 `145yfHTWz104ZIV60iHo8PSinj_uhTN9B` | V004 `18ofv4cJnj7Uvme-WzTebWftIobJQ1U0u` |
| Rejection report answered | `1jyqlHvl8pGvRDzCaqukkSKfieHnRDuaz` | `1xeqHXmYujiusXlAjY5Rrq07lduBGxU3L` |
| **Base actually built from** | **V005** `1qi7TsLi5v8pfM4mHYLWvJEaSdPPyl_qW` · MD5 `6f32d454bb7b6f15ce31e3bffa136385` | **V003** `1LxVWK8D6nNYUF8oqC0pCMxsrBEK_XspN` · MD5 `1ee728c2bae54ae5284959ca5e747943` |
| Output file | `B2_CAND_ESTABLISHING_V007_2560x1440.png` · 2560×1440 · SHA‑256 `12c96f52…fe6b` | `B2_CAND_WALL_OF_HOUSES_V005_2560x1440.png` · 2560×1440 · SHA‑256 `71fbf901…0f79` |
| Drive ID (this upload) | `1pc3_bN06af5aSndq6aesxtwtg6Vnp6_R` | `1kWWiwfizR_PmKDicntGnnUHFZeAdJ5Rd` |
| Comparison board | `1A10-FlflAwN3yuI_OVpgRSPS_nl0eCk0` | `1T9Eziwd_5UcVfBXgxdi_-7Cvr1XYkT3J` |

Both bases were used from the staged copies whose MD5 was checked against Drive at the start of the batch; neither base was edited, moved, renamed or re-uploaded.

## 2. Defect-by-defect response

### Establishing V006 → V007 candidate
| Report point | What the file now shows | Basis |
|---|---|---|
| **A** cone-like symmetrical mass | Gone. The mound is an irregular, asymmetrical accumulation of separate single-storey houses with uneven shoulders, jutting clusters, staggered ridges, ladders and worn stair runs. | Repainted mask, EST polygon, see verification §2 |
| **B** foreground-house smear and its artefacts | Absent by construction: the foreground compound is untouched V005, and V005 never had the smear. No hand-retouch blurs were applied anywhere. | 0 changed px in `(380,760)–(820,1080)` panel coords |
| **C** false claims in the V006 metadata/comparison | The V006 claims are not repeated. The chrome and the comparison board describe only what the exported PNG contains, and the pixel figures quoted are the audit output. | `B2_VERIFICATION…` §2–§3 |
| **D** Nneka's House (clothesline through gable, eaves clip, spotlight) | **Deliberate deviation — see §3.** The compound is V005's own pixels, unaltered, so the three V006 faults do not exist. A separate warm-daylight generative pass was produced and **not used**. | 0 changed px in the house's region |
| **E** stale chrome | Digits and copy re-set: header V005→V007, `CLIENT REVIEW`, `CHANGED SINCE V005`, `KNOWN ISSUES` all rewritten for this build; STATUS: REVIEW REQUIRED and EXPLORATORY — NOT APPROVED CANON retained. | Visual check of the exported gutter |
| Preservation | Hall of Posts, aerial river, inverted overhead settlement, foreground compound, zero glow, figureless composition | Outside-mask changed pixels: **0** |

### Wall of Houses V004 → V005 candidate
| Report point | What the file now shows | Basis |
|---|---|---|
| **A** two-storey blocks | Every dwelling in the exported image is single-storey with one roof and one ground-level door. | Visual, 1.5× and 3× crops |
| **A** red bars, red glyphs, invented symbols | None. Bright-red pixel count in the artwork panel: **0**. | `verify_env.py` |
| **C** fresh bottom huts / ladder blocked by the left hut | A distinct older, more eroded first settlement stands at the foot with worn paths, gaps and pale-sealed doors; no dwelling blocks a ladder. | Visual |
| **D** lost lit/dark/sealed doorway distinction, Sealed-Quarter language | Triad reads: warm hearth-lit doorways, several dark openings, plain-sealed doors in warm-pale mud plaster with dry-mud crazing and wedged timber. | Visual, 3× crop |
| **E** false claims | Metadata and board restricted to what is in the file. | `B2_VERIFICATION…` |
| **F** stale chrome | Header V003→V005; all three copy blocks rewritten; status retained. | Visual |
| Preservation | Sky, mist, frame edges, palette | Outside-mask changed pixels: **0** |

## 3. The one deviation I am declaring up front

The report's point **D** asked for Nneka's House to be *integrated naturally*. I did not paste the separate warm-daylight house into the frame, and I am not claiming it was integrated:

- In V007's composition that house sits in the **foreground compound**, which is outside the repainted mask. Those are V005's own pixels — unmodified, and already correct. The V006 faults (clothesline through the gable, clipped eaves, spotlight glow) were V006-only artefacts of a generative pass over that compound.
- Pasting a warm-daylight render into the hazy distance would have reproduced the exact failure the client rejected: an over-lit object sitting unnaturally against the recessive haze.

So the honest reading is: **the house is unaltered, not re-integrated.** If the CD wants the approved Nneka's House asset (`1JIoAiQ2…`) resized and placed into the compound explicitly, that is a further authorised change and needs a new version number — it is not in V007.

## 4. Method limitation restated (it applies to both files)

Both candidates are masked architectural repaints from a generative pass, not hand retouches. Inside the mask the pixels are the generator's; the alignment was solved by exhaustive translation search (EST `(−4,+2)`, mean abs diff 5.35; WALL `(0,+10)`, 6.44) and the seam blended with a 26/30 px Gaussian feather. The renders are not reproducible — a re-run yields different architecture. Surfaces inside the mask therefore read flatter and less granular than the masters'. This is disclosed on each frame's `KNOWN ISSUES`, in the comparison boards, and in `B2_VERIFICATION_ENVIRONMENT_REBUILDS_2026-11-17.md` (`1sRagEJxToeZFTWy7Anx60dVonXRNvDSR`).

## 5. What is still open, unchanged by this upload

- **VR‑010** remains blocked on its missing brief. Not touched, not invented.
- Outstanding client questions CQ‑4, 6, 7, 8, 9, 10, 11, 12; CQ‑2 partial; U‑11, U‑18. Unchanged.
- Review recommendations D1/D2 (KEEP), D3 (KEEP V004), D5 (Hall of Posts `1mRSsIHU…` ACCEPT FOR UPLOAD — recommendation only, **not acted on**), D6/D8 (REVISE), D7 (confirm REJECT) — all untouched by this upload.
- Both environment assets are now **frozen pending independent review** of these two candidates. No further changes to either until that review lands.
