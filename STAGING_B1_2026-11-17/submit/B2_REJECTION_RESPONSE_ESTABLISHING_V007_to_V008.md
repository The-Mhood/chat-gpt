# REJECTION RESPONSE — ESTABLISHING VIEW · V007 → **V008 candidate**
**Answers `REJECTION_REPORT_ESTABLISHING_V007.md` (`1NEy7cAufVGW0FnWGstUJZGB1cZ3UX0qz`), CD/TD verdict TARGETED REVISION.**
Status: CANDIDATE ONLY · REVIEW REQUIRED · EXPLORATORY — NOT APPROVED CANON.

---

## 1. Provenance

| Role | File | Drive ID | Bytes | MD5 | SHA‑256 |
|---|---|---|---|---|---|
| Working base (authority) | `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg` | `1qi7TsLi5v8pfM4mHYLWvJEaSdPPyl_qW` | 786,106 | `6f32d454bb7b6f15ce31e3bffa136385` | `5f8e0a9b…c4c98` |
| Rejected V007 (comparison only, not a master) | `B2_CAND_ESTABLISHING_V007_2560x1440.png` | `1pc3_bN06af5aSndq6aesxtwtg6Vnp6_R` | 3,729,703 | `d176595797b04432c9aa08f3a41e6d2a` | `12c96f52…fe6b` |
| Approved reference for Requirement D (unused, intact) | `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_NNEKAS_HOUSE_V004.jpg` | `1JIoAiQ20goibDA-ujYr95iyihBTLKZWj` | 580,415 | `8eec0c112ea14a8aa1d8328ed10004e7` | — |
| **This candidate** | `B2_CAND_ESTABLISHING_V008_2560x1440.png` | `1914IgQKxE-6uU8AuFIe_lcbj1yn9tzN9` | 3,864,414 | `575f44b95f4fbf6af0b27d87a7b4c399` | `957ff0cc9044e69c0777099eab32aafa68fbc4f80b1b4f620f71fe723e51d976` |
| Comparison board | `B2_COMPARE_ESTABLISHING_V005_vs_V008.jpg` | `1lXvNjgnJpWxAlGsRzozDYvVUrd_6gums` | 931,459 | `6ed2698acf07f25541c457a4339ec855` | `fc718686b3f4be8885d3b7981f2b21aa31ff7cf35fcf13347d922282184768ae` |

V006 and V007 are preserved exactly as rejected. V001–V005 untouched. The Nneka's House reference was downloaded and MD5‑verified but **no pixel of it entered this file** — see §3.

## 2. Defect closure (report §4–§5)

| Report defect | What V008 does | Evidence |
|---|---|---|
| **2a** houses 2.5×–3× overscaled | Mound rebuilt as a dense accumulation of hundreds of small single‑storey dwellings at the same scene scale as the village below its foot | Board detail pair; 1:1 inspection |
| **2b** flat / painterly surface | Detail pass taken from the render itself returns granular mud and ragged-thatch microtexture inside the mask. Closer to V005's weight — **not identical**, and disclosed as such | 1:1 crops |
| **2c** stray poles across the river; blurred left flank; stacked porch block | No pole, strut or mast crosses the aerial river; the river thins into mist at the mound's flank with a crisp edge; no two‑tier porch block anywhere | River detail pair |
| **3** blank `CLIENT REVIEW` block | Populated. Root cause owned: my V007 compose script drew the CLIENT REVIEW copy under an unhandled block type (`L2`), so the rectangle was cleared and nothing was written. Fixed by drawing it as a normal label+body block | Chrome crop |
| Chrome version | Header digit → `V008`; `CHANGED SINCE V005` and `KNOWN ISSUES` rewritten to match these bytes; `STATUS: REVIEW REQUIRED` and `EXPLORATORY — NOT APPROVED CANON` retained | — |
| Preserved anchors | Hall of Posts, foreground compound and frame edges: **0 changed pixels** | Audit §4 |

## 3. Requirement D — **SPECIFICATION REQUIRED**, not delivered

I am not claiming D. Three integration attempts were made and none is shippable:

1. **Generative pass, approved house supplied as design reference** (`work4/EST_nneka_yard.png`) — returned a clean, bright CGI dwelling with corrugated‑metal neighbours: wrong material language for this settlement, would have clashed on sight.
2. **Generative pass, scene only as reference** (`work4/EST_nneka_yard2.png`) — better styled but still CGI‑clean against V005's gritty haze, and it re‑drew the surrounding walls.
3. **Pixel composite of the approved house** (`work4/EST_V008_house2.png`) — a 170×146 insert in the courtyard: the ground plane fights the courtyard's viewing angle and the patch reads as pasted.

What is missing is a **decision, not a render**: either an approved integration method (a perspective‑matched plate, or authorisation to re‑stage the compound), or authorisation to place Nneka's House on a dedicated mid‑ground plate instead of this dense yard. Per the eligibility standard I am not inventing either. The approved reference is untouched and ready.

## 4. Audit

| | V008 |
|---|---|
| Frame / panel | 2560×1440 · panel `(60,152)–(1961,1321)` = 1901×1169 |
| Alignment of render to panel | `(dx,dy) = (−5, 0)` |
| Total changed px vs V005 | 406,016 |
| Inside the mound mask | 332,417 |
| **Outside mask + metadata column** | **0** |
| Hall of Posts / foreground compound / frame bottom | 0 / 0 / 0 changed px |
| Sky band `y 152–282` | 12,288 px — the old apex is replaced by mist; inside the mask |

Method limit, unchanged: inside the mask the pixels are a generative repaint with a self‑detail pass; outside it they are V005's own bytes.

## 5. Status

Candidate only. Review required. No approval, no promotion, no filing. The asset stays `EXPLORATORY — NOT APPROVED CANON`.
