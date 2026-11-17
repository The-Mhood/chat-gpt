# ADDENDUM B2-A — CQ-9 IS NO LONGER AN OPEN QUESTION ABOUT BUREAUCRACY
**It is now an evidenced blocker on VR-006 and VR-007, and it changes the diagnosis.**
**Read with:** `B2_CANDIDATE_REGISTER.md` §5, `B2_RETOUCH_GUIDE_VR-007_BLOCKED.jpg`, `B2_RETOUCH_GUIDE_VR-006_BLOCKED.jpg`

---

## 1. What I did

Rather than attempt a third generative pass on the sheathed weapon, I went to the only blade reference in Drive and read it as **evidence**, not as approval. File: `WEAPON_ADANNA_PRIMARY_BLADE_V001.jpg`, Drive ID `1V12Sq2BZdIqjsgkx5GRpzGxc3nS3Gbac`, parent `06_WEAPONS_AND_ARMOUR` `1hSAxthJ96jfgSIUVpglHw26OSVrJQ-6Q`, 521,776 B, 2560×1440, MD5 `bbeb0788667643d86e9adfde0326399e` (staged copy matched exactly). A second copy with the same MD5 sits in `1bJ9zhzfh5BKqedvj4HwGmWsYPQ7CBAJG`.

**CQ-9 is still open. I have not treated this board as approved, here or anywhere.**

## 2. What the board actually says — quoted, because the wording matters

- **Header, top right:** `STATUS: REVIEW REQUIRED`
- **Type:** "Short leaf-bladed iron sword. One-handed. OGU (blade) discipline."
- **Construction:** "Forged iron blade with raised mid-rib and visible hammer marks. Hardwood grip under leather cord. **Cast bronze pommel. Stitched leather scabbard with indigo cord.**"
- **Scale:** "Approx. 60 cm overall; blade about 42 cm. **To be confirmed against the character model.**"
- **Known issues:** "Pommel is too bright; dull to match aged bronze standard. **No hand-scale view yet.**"

## 3. Three consequences, and the third is the one that matters

**First: the master boards are quoting an unapproved reference as approved.** Every Adanna composition board carries `Blade: WEAPON_ADANNA_PRIMARY_BLADE_V001` and its footer says "blade from the approved blade board". The board itself says REVIEW REQUIRED. That does not make the compositions wrong — it means the word "approved" in those footers has no file behind it. It should be corrected in the board template whenever those boards are next revised, because every agent reading them will take the claim at face value. **This is also why my CQ-9 caution was correct rather than pedantic.**

**Second: the reference cannot supply a length.** Its own scale line defers to "the character model", and its own known-issues line admits "No hand-scale view yet". So the "about 60 cm" that the master boards cite is a number that the source of the number has already declined to certify. **My earlier targets — tip on y 865 for VR-007, tip at or above (1600,880) for VR-006 — were my own reading of "above mid-thigh", not a derived figure. I am withdrawing them as authority and marking them provisional.**

**Third, and this is the real finding: the weapon drawn in the compositions does not match the reference's construction.** The reference specifies a **cast bronze drum-shaped pommel** and a **brown stitched leather scabbard with indigo cord**, ending in a tapered stitched point — no disc at the tip. The compositions show a **flat spiral disc at the top and an identical spiral disc at the bottom**, and a **dark grey, not brown, scabbard**. Compare `RETOUCH_GUIDE_VR-007` at the hip: two matching spirals.

So VR-007 and VR-006 are **not length errors**. They are **design-reconciliation errors against a reference that is itself unapproved**. If I shortened the existing object I would deliver a weapon that is the right length and still contradicts the only blade reference in Drive — and if I instead rebuilt it to match the reference, I would be promoting an unapproved design onto an approved character. **Either action invents authority I do not have.** That is the exact method blocker, stated as precisely as I can.

## 4. What this does not change

- VR-008, VR-010, VR-011, Establishing View and Wall of Houses are unaffected. None of them turns on the weapon.
- The masters are correctly staged and verified; nothing about this finding impugns the bytes.
- The rest of the correction queue keeps moving. F4 remains blocked on CQ-8 for the same class of reason — an absent reference, not an absent decision.

## 5. Next viable correction approach — no generative pass

Stated as a sequence, because steps 1 and 2 are prerequisites and cannot be skipped by working harder on step 3.

**Step 1 — resolve CQ-9 (CD).** One decision: is `WEAPON_ADANNA_PRIMARY_BLADE_V001` the design authority for Adanna's weapon, accepting its own two known issues, or does it need its own correction pass first?

**Step 2 — produce the missing hand-scale view (whoever holds the character authority).** The blade board asks for it and does not have it. Without a weapon drawn to scale against a figure, nobody — me, a retoucher, or the Original VA — can derive a defensible length. Once it exists, the target stops being my judgement and becomes a measurement.

**Step 3 — non-generative retouch, which is the only method left that preserves the approved figure.** The pipeline I would run, in order:
1. hand-authored alpha matte of the existing sheath, refined against the local edge gradient — the object is high-contrast against the indigo skirt, so this is tractable;
2. anisotropic rescale of the object along its own axis about the hilt anchor, which keeps its materials and its existing texture rather than inventing new ones;
3. **patch-based exemplar inpainting** of the background behind the removed section, sourced from the immediately adjacent skirt folds and platform shadow — these regions are low-detail and largely in shadow, which is why this specific retouch is feasible where a figure-level regeneration is not;
4. contact-shadow restoration under the new tip so the object sits on the surface rather than floating;
5. re-composite, then verify by the same rule I use on every candidate: diff outside the retouched region must be zero.

**I have not executed step 3.** Executing it before step 1 would mean choosing a weapon design on the CD's behalf. What I can do on request, without touching design, is a **background-reconstruction test**: remove the lower sheath entirely and reconstruct the skirt and shadow behind it, to prove step 3's tooling holds up, with the weapon left out until CQ-9 resolves. Say the word and it is a short job.

## 6. What I need

One of:
1. **CQ-9 resolved** in favour of the blade board → I execute step 3 to the reference's 60 cm and construction, submitted as new versions;
2. **CQ-9 resolved against it** → the weapon's design goes back to the CD first, and VR-006/VR-007 stay `CORRECTION IN PROGRESS` until a design exists;
3. **A hand-scale view** supplied from any authority → I derive the length from it and proceed without resolving CQ-9 at all.

Until one of those lands, VR-007 and VR-006 are correctly blocked, and I will not put a fourth generative attempt in front of anyone.
