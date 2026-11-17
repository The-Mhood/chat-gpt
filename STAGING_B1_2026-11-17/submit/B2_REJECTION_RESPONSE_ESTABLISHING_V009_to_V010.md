# REJECTION RESPONSE — ESTABLISHING VIEW (ANCESTRAL REALM)
## `V009` → `V010` candidate · answering `REJECTION_REPORT_ESTABLISHING_V008.md`

**Asset:** `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING` (`CH08-SUB-001`)
**Candidate:** `B2_CAND_ESTABLISHING_V010_2560x1440.png` — 2560×1440, sRGB PNG, 3,989,120 B
MD5 `762ecb72035d567f0e20136dbf7e9121` · SHA-256 `42d06820af3f03aa6019db24be830041a62d10bc1e96686fa22193407d8a8ae3`
**Supersedes:** `V009` (filed earlier today, not yet reviewed; preserved untouched, not deleted)
**Status:** `REVIEW REQUIRED` — `EXPLORATORY — NOT APPROVED CANON`. Candidate only. Nothing here is promoted.
**Owner:** Assistant Visual Agent. **Verdict answered:** `TARGETED REVISION — REJECT CURRENT VERSION`, CD Ruling **Option A**.

---

## 1. What this round changes — one thing, and only one

`V009` delivered Option A and four of the five Our Eyes defects. It left one item open and said so on its own sheet: **the mound dwellings still read 1.4–1.7× too large against the plain.** That is §6.2 of the report. `V010` closes it and changes nothing else.

| Report §6 instruction | `V009` | `V010` |
|---|---|---|
| §6.1 Re-stage foreground compound, place Nneka's House + staked plot (Option A) | delivered | **unchanged — 0 px** |
| §6.2a Lift mound shadow blacks, sit the mound behind the plain's haze | delivered | unchanged |
| §6.2b **Reduce mound house scale ~25–35 %** | **not delivered** | **delivered (~30 %, density ~2×)** |
| §6.2c Remove base seam `y≈830–865`, lower-right pale mist clip, stray roof-post stubs | delivered | unchanged |
| §6.3 Header → current version, keep `STATUS`/`EXPLORATORY`/`OAD-40`/`CLIENT REVIEW`; drop "hundreds" | delivered | header → `V010`, block updated, no count asserted |
| §6.4 Submit to `PENDING/ASSISTANT_VA_SUBMISSIONS` with comparison board, pixel audit, hashes | delivered | this filing + `V009`→`V010` board |
| §2/§5 Research Agent exact-version report | **gap, restated on the sheet** | **gap, restated on the sheet** |

---

## 2. Defect 3 — how the scale reduction was actually done

Stated plainly, because the method matters more than the result:

1. The hill interior was **re-rendered from the `V009` hill as reference** with the instruction to keep camera, palette, haze and outer silhouette, and to make each dwelling ~30 % smaller and about twice as numerous.
2. The render was **registered back into the same crop** and colour-matched to the destination (median shift `+3,+7,+6`).
3. It was composited **inside the `V008` hill mask, eroded 20 px and feathered 22 px**. The outline against the sky is therefore `V009` pixels **by construction** — the new, smaller houses sit inside the old silhouette. This is the safeguard against the failure mode that killed the earlier shrink attempts (cone/dome drift, halo against sky).
4. The re-render came back flatter than the `V008` hill, so the original's **high-frequency detail** (thatch straw, mud grain, terrace wear) was extracted and re-applied inside the replaced area at 0.38 weight. Granular quality — explicitly listed by Our Eyes as an improvement to preserve — is carried across rather than lost.
5. Grain re-applied to the whole panel (`N(0,1.15)`), so the replaced interior does not sit in a cleaner regime than its surroundings.

**Limitation, not hidden:** the hill interior is generative pixels, not `V008` pixels, exactly as the right compound already is. It is a masked repaint inside a preserved silhouette — this is stated on the sheet's `KNOWN ISSUES` block, not only here.

---

## 3. Verified pixel audit (`V009` → `V010`, panel-only, pre-grain)

Method: `work6/est_v9_p5.png` vs `work6/est_v10_p2.png`, panel 1901×1169, panel origin `(60,152)`. Reported as `>2 / >12 / >20` per channel-max delta.

| Zone | >2 px | >12 px | >20 px |
|---|---|---|---|
| **Hill bbox** `(960,88)–(1901,708)` | 274,928 | **101,913** | **49,526** |
| Hall of Posts | 0 | 0 | 0 |
| Left compound | 0 | 0 | 0 |
| Foreground right compound (Option A re-stage) | 0 | 0 | 0 |
| Frame bottom | 0 | 0 | 0 |
| Sky band `x 0–1440, y 120–151` | 41 | 0 | 0 |

Panel totals: **101,913 px >12** · **49,526 px >20** · max delta **195**. Every structural change falls inside the hill; the sky-band 41 px is sub-12 feathered spill at the mask's upper edge.

---

## 4. Two things I will not claim

1. **The stray roof-post stubs (§6.2c).** Six independent detectors across `V008`/`V009` returned no protruding stub — narrow skyline peaks, thin vertical columns above the local roof envelope, run-length, isolation, connectivity, thin-column. The thin items on the ridges are ladder rails and batten ends, which are correct detail. Nothing was invented to satisfy the note. If Our Eyes can mark the stub in a crop, it can be removed precisely in one pass.
2. **The exact coordinates of the lower-right pale mist.** The report cites `x≈1860–1960, y≈740–840`. In `V008` and `V009` at those literal frame coordinates there is no pale smear — the pixels there are roof thatch. The artefact I could see and did correct is the grey veil in front of the mound's lower-right houses around `(1480,380)–(1901,720)`, warmed out in `V009`. If the report's coordinate frame is the `V005` crop rather than the frame, that reconciles it; if not, the note needs one clarifying crop.

---

## 5. Files in this filing

| File | Size | MD5 |
|---|---|---|
| `B2_CAND_ESTABLISHING_V010_2560x1440.png` | 3,989,120 B | `762ecb72035d567f0e20136dbf7e9121` |
| `B2_COMPARE_ESTABLISHING_V009_vs_V010.jpg` | 1,907,538 B | `cd427cbe33686b748c832a66c95e5edc` |
| `B2_REJECTION_RESPONSE_ESTABLISHING_V009_to_V010.md` | this document | — |
| `B2_REGISTER_LEDGER_v9_2026-11-17.md` | filing register + placement audit | — |

`V008` and `V009` remain in the record, byte-for-byte unchanged. No version has been deleted, moved into `14_APPROVED_DESIGNS`, or relabelled as canon.

---

*Filed to `PENDING/ASSISTANT_VA_SUBMISSIONS` for fresh independent Our Eyes inspection and for a Research Agent exact-version report on `V010`. Candidate only.*
