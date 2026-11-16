# FAULT F4 — GATE GUARD SHELTER: SHIELDS STILL MORE PATTERNED THAN THE GUARD SHEET
**Board:** ENV_HOME_SETTLEMENT_GATE_GUARD_SHELTER_V002 (supersedes V001, which is kept) — **SUBMITTED FOR REVIEW (post-sync 2026-11-16)**
**Drive:** `1fVQqu3W3Pqguf0qZi5xweNtG0P2dz2z3` · [open](https://drive.google.com/file/d/1fVQqu3W3Pqguf0qZi5xweNtG0P2dz2z3/view) · 02_LOCATIONS/Home_Settlement · 2560×1440 · 644,379 B · modified 2026-11-15T22:18:39Z
**Local copy (MD5-checked):** `.arena/home_settlement_handoff/src/ENV_HOME_SETTLEMENT_GATE_GUARD_SHELTER_V002.jpg` · `88f0af5cd11424790716d889004db986`
**Register refs:** CH01-INT-013 · scene CH01-SCN-019 · PROPOSED addition · UNIFORM: palace guard uniform (OAD-18); villager clothing rule does not apply to guards
**Status:** REVIEW REQUIRED + **SUBMITTED FOR REVIEW**. **Not approved. Not actioned.**

## Fault (verbatim sources)
Sheet, KNOWN ISSUES panel:
> "The gates board it matches is itself in review, not approved. Shields are still more patterned than on the guard sheet. Lower source resolution."

Register/index note (`ART_BIBLE_MASTER_INDEX_POST_SYNC_2026-11-16.md` line ~244; `ART_BIBLE_INDEX_POST_SYNC_2026-11-16.md` line ~207):
> "Post-sync reconciliation 2026-11-16; SUBMITTED FOR REVIEW; no approval status change; Gateposts now match gates board; shields still more patterned; gates board in review"

V001 note (same subject, superseded): "Oversized gateposts; shields too patterned" — the gateposts were fixed in V002; the shield patterning persists.

## What is wrong
The two oval shields hanging on the shelter's back wall carry dense all-over geometric patterning. The approved guard sheet (guard costume/identity reference, OAD-18 uniform family) shows comparatively plain shields. The board exceeds its own approved reference — a continuity break with an approved asset class, not a stylistic preference.

## Documented fix direction (not applied)
Simplify the shield ornament toward the guard-sheet patterning (sparser, restrained geometry). Do not redesign the guard, the uniform, the lean-to, the log bench, spears, cone-and-hide shields, water pot, slit drum for the alarm, or the game scratched in the earth. Do not touch the gateposts (already corrected to match the gates board).

## Dependency note
The board is consistent with **ENV_HOME_SETTLEMENT_GATES_V002** (`1URKeKJBrQW_DMT0txZSREK0V-WjkNLMD`, in review), which is itself **not approved**. Any correction to the shields assumes the gates board survives review unchanged; if the gates board is rejected or further revised, the shelter/gate correspondence must be re-checked before correction is finalised. The approved reference is the **guard sheet**, not the gates board.

## Severity / engineering impact
- Severity: **Major** (continuity with approved guard design; visible, central wall objects; repeated across V001→V002).
- Blocks engineering greybox? **No.** Shelter layout, lean-to, bench, wall mounts are unaffected.
- Blocks board approval/promotion? **Yes — documented open defect on a SUBMITTED FOR REVIEW board, dependent on gates-board outcome.**
- MOODBOARD: Level 2 `CH01-INT-013 The Gate Guard Shelter: CH01-SCN-019` (outstanding). Fixing F4 does not retire that moodboard item.

## Guardrails
Correction, when authorised, happens as a **local candidate only**; V002 preserved; no upload; no status change; CD decides keep/reject after the gates board's own review settles. Do not promote shield fidelity beyond the guard sheet — match, don't enrich.
