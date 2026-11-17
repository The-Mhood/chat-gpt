# CD RULING RESPONSE — ESTABLISHING · V008 → **V009 candidate**
**Answers the CD ruling of 2026-11-17: Option A for Requirement D, plus the five Our Eyes defects.**
Status: CANDIDATE ONLY · **UNAPPROVED — REVIEW REQUIRED** · not canon.

---

## 1. Provenance

| Role | File | Drive ID | Bytes | MD5 |
|---|---|---|---|---|
| Superseded candidate (preserved untouched) | `B2_CAND_ESTABLISHING_V008_2560x1440.png` | `1914IgQKxE-6uU8AuFIe_lcbj1yn9tzN9` | 3,864,414 | `575f44b95f4fbf6af0b27d87a7b4c399` |
| Approved house design (Requirement D reference) | `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_NNEKAS_HOUSE_V004.jpg` | `1gw8oqjET…` | — | `8eec0c11…` |
| **This candidate** | `B2_CAND_ESTABLISHING_V009_2560x1440.png` | *(uploaded this round)* | 3,978,156 | `cf385d3e793314e2db6a2b12bf79955a` |
| Comparison board | `B2_COMPARE_ESTABLISHING_V008_vs_V009.jpg` | *(uploaded this round)* | 1,785,731 | `0d84d948bfb06352314a51c14b4079f0` |

SHA‑256 of the candidate: `e3436510315e0108f848c806dec54d366720d3a3c7b5f6ef7b168cf469e98474`.

## 2. Requirement D — Option A, delivered

The CD directed a **re-stage of the foreground compound**, replacing or widening the cramped right foreground longhouse as necessary, so Nneka's House and its staked unbuilt plot sit naturally within the compound in warm daylight.

What was done, in order, with the reason for each step:

1. **The cramped corner was re-staged, not patched.** A generative pass over the right-hand compound region (frame x 1180–1901, y 500–1130) set the longhouse back into a longer, lower range and opened a swept yard in front of it. This removes the condition that had defeated every earlier attempt: there was no ground plane to receive a house, so any insert read as a pasted card.
2. **The house was placed against the approved design, supplied as a reference.** The second pass carried the approved `NNEKAS_HOUSE_V004` plate as an image reference, so the roof pitch, veranda with its two timber posts, door, shuttered window and the pot/broom/mortar group follow the approved design rather than being invented. It stands in the yard, bedded into the ground, lit from the same direction, with a soft cast shadow.
3. **The plot is drawn as the design intends:** a rectangle of short timber stakes joined by string, bare swept earth inside, nothing built on it.

This is the first version of the asset in which Requirement D is present rather than declared undeliverable. It is a **generative re-stage**, and the sheet says so in KNOWN ISSUES in plain words.

## 3. The five Our Eyes defects

| Defect | What changed | Evidence |
|---|---|---|
| Mound shadows and atmospheric perspective do not match the dusty aerial haze | Distance-graded warm haze inside the mound mask, alpha 0.03 at the foot rising to 0.22 at the summit, plus a shadow lift at the same gradient. The mound now sits at the same depth as the plain instead of reading as a darker, contrastier mass | board row A |
| Base seam | A noise-modulated dust drift band carries the mound foot into the plain; the hard edge is gone | board row A |
| Lower-right mist artefact | The pale grey veil in front of the lower-right houses is colour-corrected to warm dust and its local contrast restored, so it reads as haze behind the roofs | board row B |
| Stray roof-post stubs | Two independent scans were run across the full width: (a) narrow skyline peaks, (b) thin vertical columns rising more than 6 px above the local roof envelope. **Both returned nothing** — V008 has no isolated protruding stub on the mound. The thin items on the roofs are ladder rails and batten ends, which are correct detail and were kept | — |
| Inaccurate "hundreds" description | Removed. No dwelling count is asserted anywhere on the sheet; the READ describes only what is in frame | sheet, right column |

## 4. Not done, and stated as not done

**The summit dwellings still read large for the distance.** Genuinely reducing them means re-rendering the heap. Two attempts were made this round and both were discarded rather than shipped:

- a full re-render of the mound region — it rebuilt the silhouette into a smooth dome and washed the haze across the whole frame;
- a crest-only edit — it drifted the rooflines and could not be composited without a visible halo against the sky.

A radial scale-down of the existing heap was also tested and discarded: it compresses the silhouette into a regular dome, which is a worse failure than the size problem. This is the one CD item **not** delivered, and it is flagged as such on the sheet.

## 5. Integrity audit — what the change did and did not touch

Structural diff against V008 (threshold |Δ| > 2, before the unifying grain pass):

| Region | Pixels changed |
|---|---|
| **Hall of Posts** | **0** |
| **Left compound** | **0** |
| **Frame bottom strip** | **0** |
| Sky band (mound summit haze) | 17,317 |
| Mound (haze, shadow lift, dust drift) | 283,557 |
| Right compound (the ordered re-stage) | 467,451 |
| **Total** | **688,971 = 31.0 % of frame** |

Both changed zones are exactly the two the ruling names. No approved element outside them was altered.

## 6. Status

Candidate only. UNAPPROVED — REVIEW REQUIRED, returned for fresh Our Eyes inspection and CD verdict. V008 preserved byte-identical. Nothing was promoted, moved or approved.
