# FILING REGISTER & PLACEMENT AUDIT — `v9`
**Programme:** *The Disobedient Daughter* — Chapter 8 environment set
**Date:** 2026-11-17
**Supersedes register `v8` (`12D8gVf8cqfSQQzghzJtr026lenc38iI9`)**
**Branch:** `arena/90e15011-chat-gpt`

---

## 1. Placement audit — five live candidates were filed in the wrong folders. Corrected.

This round's check was not a version check. It was a **where-are-the-files** check, and it found a real fault.

The submission folder `PENDING/ASSISTANT_VA_SUBMISSIONS` (`16p2TYXn16u9UNdMlJzjTK873YK_Fk7Ab`) listed 42 files and **none of this round's two uploads**. Resolving parents showed the candidate PNGs had not landed where the upload was asked to put them. Auditing every live candidate in the register found five more in the same condition — including two that had been sitting in `16_REJECTED_DESIGNS` since earlier today, which is the worst possible place for a live submission: a reviewer scanning that folder reads them as rejected.

| File | Drive ID | Was in | Now in | MD5 (local = Drive) |
|---|---|---|---|---|
| `B2_CAND_ESTABLISHING_V009` | `1VkfdG0dCgsXl-Y3H98Nv4xu0FTGbHaJf` | `16_REJECTED_DESIGNS` | `PENDING/ASSISTANT_VA_SUBMISSIONS` | — |
| `B2_CAND_VR-010_WASHING_PLACE_V005` | `1s1Gx4qM0_eavWTMawEjDbajDDPafkPg2` | `Home_Settlement` | `PENDING/ASSISTANT_VA_SUBMISSIONS` | — |
| `B2_CAND_ESTABLISHING_V008` | `1914IgQKxE-6uU8AuFIe_lcbj1yn9tzN9` | `16_REJECTED_DESIGNS` | `PENDING/ASSISTANT_VA_SUBMISSIONS` | `575f44b95f4fbf6af0b27d87a7b4c399` ✓ |
| `B2_CAND_VR-010_WASHING_PLACE_V004` | `196uxAIaLdRGsqA0M0ALk9_Zps_A81XNt` | `16_REJECTED_DESIGNS` | `PENDING/ASSISTANT_VA_SUBMISSIONS` | `93ece632db86191f05d74403f68cc238` ✓ |
| `B2_CAND_VR-008_SEALED_QUARTER_V008` | `1FA2wXlDlbPmasTSc4zMmuvWt_nlTNXH-` | `16_REJECTED_DESIGNS` | `PENDING/ASSISTANT_VA_SUBMISSIONS` | `a41548911b4d991e7e05aad6474441aa` ✓ |
| `B2_CAND_WALL_OF_HOUSES_V005` | `1kWWiwfizR_PmKDicntGnnUHFZeAdJ5Rd` | `Chapter_08_Ancestral_Realm_Combined_Direction` | `PENDING/ASSISTANT_VA_SUBMISSIONS` | `a2298fe5270e6f4737e89228f1b2fc70` ✓ |
| `B2_CAND_COSTUME_BREAKDOWN_V002` | `1OcNpG55dadGkIUUar7W0Vm5Lkb2QGLJR` | `Adanna` | `PENDING/ASSISTANT_VA_SUBMISSIONS` | `bb49ee2086a617593d571f301bb5ffd6` ✓ |

Moves were `add_parents` + `remove_parents` — the file objects, revisions and IDs are unchanged; nothing was copied, re-uploaded, or re-encoded. Every MD5 above was recomputed from the workspace file and matches Drive byte-for-byte.

**Verified end state:** eight live candidate plates now sit in `PENDING/ASSISTANT_VA_SUBMISSIONS`, single-parent:

1. `B2_CAND_ESTABLISHING_V008` — `1914IgQK…`
2. `B2_CAND_ESTABLISHING_V009` — `1VkfdG0d…`
3. `B2_CAND_ESTABLISHING_V010` — this round's new candidate
4. `B2_CAND_VR-008_SEALED_QUARTER_V008` — `1FA2wXlD…`
5. `B2_CAND_VR-010_WASHING_PLACE_V004` — `196uxAIa…`
6. `B2_CAND_VR-010_WASHING_PLACE_V005` — `1s1Gx4qM…`
7. `B2_CAND_VR-011_LANDING_OF_UNCLAIMED_V002` — `1_vJFw7KN…` (was already correct)
8. `B2_CAND_WALL_OF_HOUSES_V005` — `1kWWiwfi…`
9. `B2_CAND_COSTUME_BREAKDOWN_V002` — `1OcNpG55…`

**Cause, stated honestly:** the upload path did not honour the requested parent for these binary files — some went to a default location, some to whichever folder had been touched last in the session. Companion boards and markdown from the same rounds landed correctly, which is why the earlier checks (listing the submission folder and seeing the boards there) did not reveal it. Every future filing in this programme must resolve `parents` on the uploaded file itself before the round is called complete. That check is now part of the filing step, not an optional extra.

---

## 2. `16_REJECTED_DESIGNS` — inventory and one thing that is not mine to move

`16_REJECTED_DESIGNS` (`1x5T4V3R-hnuUNCIFBIb1TBIezjlT0Q6c`) currently holds **30 items**. Fifteen are the rejection record — rejected plates and their seven reports. Two more are `/`-blocked or superseded items. **Fourteen are not rejections at all:**

- `B2_CAND_VR-008_SEALED_QUARTER_V007` (`1-aBDr85…`, 16:53) — superseded by `V008` after the armlet errata, not formally rejected by any report. Status ambiguous; left in place rather than guessed at.
- `CHAR_ADANNA_TURNAROUND_{FRONT,LEFT_SIDE,BACK,THREE_QUARTER}_V001.jpg` (16:53) — four character turnaround plates.
- `SCENE_CH01-SCN-{006,007,008,010,012,014,017,022,032,033}_V001.jpg` (16:54) — ten Chapter 1 scene plates.

These fourteen arrived at 16:53–16:54, in the same minutes as this round's uploads, and they carry the same misplacement signature. **They are not this agent's files and were not produced in this session** — so they were left exactly where they are. Moving someone else's work into or out of a decision folder is not a call an assistant makes quietly. Flagged for CD / Our Eyes: a reviewer opening `16_REJECTED_DESIGNS` will read fourteen valid-looking turnarounds and scene plates as rejected canon.

`COMP_ADANNA_NNEKAS_YARD_FULL_FIGURE_V001.jpg` (`1FOjWc2E…`) is also in this folder, still **BLOCKED**, position preserved.

---

## 3. Filed this round

| Artefact | Size | MD5 | SHA-256 |
|---|---|---|---|
| `B2_CAND_ESTABLISHING_V010_2560x1440.png` | 3,989,120 B | `762ecb72035d567f0e20136dbf7e9121` | `42d06820af3f03aa6019db24be830041a62d10bc1e96686fa22193407d8a8ae3` |
| `B2_COMPARE_ESTABLISHING_V009_vs_V010.jpg` | 1,907,538 B | `cd427cbe33686b748c832a66c95e5edc` | `2606a90e9cc7f730f824c4d128270828314b8322071633b735d992f1b90228d0` |
| `B2_REJECTION_RESPONSE_ESTABLISHING_V009_to_V010.md` | — | — | — |
| `B2_REGISTER_LEDGER_v9_2026-11-17.md` | this document | — | — |

`V010` build chain, reproducible from the workspace: `work6/est_v9_p5.png` → `mound_ref9.png` crop → generative scale pass `mound_scale1.png` → `scale_pass.py` (mask-eroded composite, colour match `+3,+7,+6`) → `detail_transfer.py` (0.38 high-frequency carry) → `compose_v10.py` (grain, chrome) → `final/CAND_ESTABLISHING_V010_2560x1440.png`.

---

## 4. Carried status of the other open candidates

| Candidate | Plate | Standing this round |
|---|---|---|
| VR-008 Sealed Quarter `V008` | `1FA2wXlD…` | live, unreviewed, now correctly placed |
| VR-010 Washing Place `V005` | `1s1Gx4qM…` | live, unreviewed; panel is `V004` pixels, 0 px changed — chrome-only correction |
| VR-011 Landing of Unclaimed `V002` | `1_vJFw7KN…` | live, unreviewed |
| WALL OF HOUSES `V005` | `1kWWiwfi…` | live, unreviewed |
| COSTUME BREAKDOWN `V002` | `1OcNpG55…` | live, unreviewed (carries the documented `700×750 / 900×620` outstanding items) |
| ESTABLISHING `V010` | new | live — answers `REJECTION_REPORT_ESTABLISHING_V008` §6.1–6.4 |

No plate has been moved into `14_APPROVED_DESIGNS`. Nothing has been deleted. Nothing has been relabelled canon.

---

## 5. Open items that block a full `PASS`

- **Research Agent exact-version reports** are outstanding for EST `V009`, EST `V010`, VR-010 `V005`, VR-008 `V008`, VR-011 `V002`, WALL `V005`. The `V008` rejection report logs the gap formally; every `PASS` on these files is contingent on it.
- **`U-40` Nsude silhouette clearance** on the rebuilt hill — the `V010` outline is `V009` pixels by construction, and the `V008` report already cleared the rounded-heap silhouette against a stepped shrine form, but the direct confirmation on the new version belongs to Research, not to me.
- **Stray roof-post stubs** — still unlocated after six detectors; needs a marked crop from Our Eyes.
- **Lower-right mist coordinates** — needs one clarifying crop (see response §4.2).
- **Fourteen non-rejection files inside `16_REJECTED_DESIGNS`** — CD/Our Eyes to re-home or confirm.
- CQ‑4, 6–12 (CQ‑2 partial), U‑11, U‑18 remain open in the programme ledger.
