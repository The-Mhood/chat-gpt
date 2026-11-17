# STAGING LEDGER — B2 isolated master-image staging (authorised)

Every source below is the exact canonical master named in the authorisation. Each was downloaded by the Drive connector as a **separate copy** into this workspace; no canonical file was moved, renamed, overwritten or re-uploaded. Staged copies live in `STAGING_B1_2026-11-17/masters/` under their original filenames.

**Verification method.** Google Drive exposes `md5Checksum` for stored files but not SHA-256 through this connector, so MD5 is the source-side check; SHA-256 is computed locally on the staged copy for chain-of-custody. Every staged MD5 matched the Drive-reported MD5 exactly. All eight are 2560×1440 RGB JPEG.

## 1. Source and staged copy

| Asset | Source filename | Drive ID | Parent folder | Bytes | Drive MD5 | Staged MD5 | Match | Staged SHA-256 |
|---|---|---|---|---|---|---|---|---|
| VR-007 | `COMP_ADANNA_NNEKAS_HOUSE_INTERIOR_V002.jpg` | `18j2kaAFeCyh0ejCss53o3wrUcIKgTXvR` | `1ywTZAOGDsIa7Ia713CT21IV2CyWUiVZO` | 631,098 | `19c82fb19c5a8be767c382a46b9a071f` | `19c82fb19c5a8be767c382a46b9a071f` | YES | `973c6783faac7c3317303e60a7893828efcb222b52772d82cfdcfbacd524ab5a` |
| VR-008 | `COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005.jpg` | `1VO2hsx_J3u-qD174V-5M-SWRJPtu8Gxu` | `1QzLoG2XG-SGDJZI_mZf7zyPXU2ovnyiM` | 627,020 | `a94a084af0f7fb6d8016a6e33d44dc62` | `a94a084af0f7fb6d8016a6e33d44dc62` | YES | `a5f8f021f4859ab2a336e5d42a3de4834a18533fffd910ea81fa7da3dbc90f06` |
| VR-008 | `COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V004.jpg` | `1WnpmzTUhiHxjepd_iasZHRoJsGbO64jg` | `1ywTZAOGDsIa7Ia713CT21IV2CyWUiVZO` | 653,046 | `222329587e39160d9a95bea007ed08df` | `222329587e39160d9a95bea007ed08df` | YES | `d028ef2aa1f5b0d80187832920e50dcd415c5da994adab1ec51a74b23cf8c330` |
| VR-006 | `COMP_ADANNA_MOTHERS_COURTYARD_V003.jpg` | `1JQzfDO4dCs9zdo6fQMAFRXrtCfmTT16q` | `1QzLoG2XG-SGDJZI_mZf7zyPXU2ovnyiM` | 690,106 | `c92555108b92887b4f932c9a3649048a` | `c92555108b92887b4f932c9a3649048a` | YES | `0ef555e036d12224aba31fd1048360db2509b503d2d830d0f4ea6e67d0f70361` |
| VR-010 | `ENV_HOME_SETTLEMENT_WASHING_PLACE_V002.jpg` | `1hhIXVq3wj3JPkfBHIMwrNLPAyr0JByWh` | `1ehkUK118Xozncy8LbTOcqTlMD-ZrR0hk` | 697,266 | `8e31b7c4200a375a90157f195b1e0c0e` | `8e31b7c4200a375a90157f195b1e0c0e` | YES | `32c615205d5813f300845e36908520320076e21d9649a9703932f166fd13b41b` |
| VR-011 | `ENV_GATES_DEAD_LANDING_OF_UNCLAIMED_V001.jpg` | `1RCfI7x3fOF2dWFV27luo1-EFBIPVi3yN` | `1W99nZFbPYLEF7PtpRbYv2sJ3U6Y62uCY` | 601,986 | `2e94fd13ae204c1b9e0de795de31df51` | `2e94fd13ae204c1b9e0de795de31df51` | YES | `bcd5b8744e9d482d1906cd2f32e7fceee8278acbefb7fd3fcb0540d2f6a1d9bd` |
| ESTABLISHING | `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg` | `1qi7TsLi5v8pfM4mHYLWvJEaSdPPyl_qW` | `1lV4NCvrj9wNdEVKiV1kYd-xl5SMU2PYR` | 786,106 | `6f32d454bb7b6f15ce31e3bffa136385` | `6f32d454bb7b6f15ce31e3bffa136385` | YES | `5f8e0a9b9a8621d8daa0ebe22757d62f9f1610a816e6d3067c0e5c169ecc4c98` |
| WALL_OF_HOUSES | `ENV_LAST_DAUGHTER_ANCESTRAL_REALM_WALL_OF_HOUSES_V003.jpg` | `1LxVWK8D6nNYUF8oqC0pCMxsrBEK_XspN` | `1lV4NCvrj9wNdEVKiV1kYd-xl5SMU2PYR` | 664,200 | `1ee728c2bae54ae5284959ca5e747943` | `1ee728c2bae54ae5284959ca5e747943` | YES | `9b860820ac2b0f5583962a9c72f02336f3840cdc9a663f22155d629d83ca0c3e` |

Note: each master exists in more than one tree with an identical MD5 (canonical copy plus mirror). The ID recorded above is the copy taken; because the MD5s agree, the trees hold the same bytes.

## 2. Candidates produced

| Asset | Candidate file | Proposed version | Bytes | Dimensions | MD5 | SHA-256 | Defect addressed |
|---|---|---|---|---|---|---|---|
| VR-008 | `final/CAND_VR-008_2560x1440.png` | V006 candidate | 3,153,214 | 2560×1440 | `cf577a3510f8b93af757d49949b7b325` | `bcce368267b3e90546179841abfb630c31832f02e714d20569075a68df9addf7` | hand retouch — crack made legible |
| VR-010 | `final/CAND_VR-010_2560x1440.png` | V003 candidate | 3,443,296 | 2560×1440 | `7f958f1ca19fa5e675971aa01025ccb6` | `1646d77a9238d07a4630da008f26dc1cb3be86525d549ab604c86ec01e719138` | generative — drain discharges under the wall |
| VR-011 | `final/CAND_VR-011_2560x1440.png` | V002 candidate | 2,487,843 | 2560×1440 | `f27c1b98e2d4b415c99cb9326210eef6` | `1b784fff49310cae9a5773150c1df7b0ef4a73bcb6c5827f026aa00d3c5ed482` | generative — strips hang, canoe field denser, water calmed |
| ESTABLISHING | `final/CAND_ESTABLISHING_2560x1440.png` | V006 candidate | 3,797,015 | 2560×1440 | `fd5f9558bed5d616149c4de0b2f255b2` | `2da1406da711bf40c20dd49e423660d853696f903bb66792b7a2e8ca4e8b0f82` | generative — irregular mound + one sunlit house, figure removed by hand |
| WALL_OF_HOUSES | `final/CAND_WALL_OF_HOUSES_2560x1440.png` | V004 candidate | 3,177,724 | 2560×1440 | `d8480938099a9c4dc4eb40449ee0abb0` | `46f015937475795d67263d2ca8ee28b355cbacd7a442f7aa5739051870f60d47` | generative — single-storey houses, distinct foot settlement, legible seals |

### Retouch layers (side artefacts, not candidates)

- `work/VR-008_crack_panel_v2.png` — 1901×1169, 2,310,648 B, MD5 `03a321e0b3acf235c21cfd818fe3a276`. The corrected 1901×1169 artwork panel for VR-008 before re-insertion into the board frame.

### Guides and boards

- `guides/RETOUCH_GUIDE_VR-007.jpg` — 901,594 B, MD5 `0837a24ad66067361655192b42fb0227`
- `guides/RETOUCH_GUIDE_VR-006.jpg` — 950,629 B, MD5 `23e113720ad6d37476bf53e23a2f6be9`
- `boards/COMPARE_VR-008.jpg` — 422,578 B, MD5 `b8e293546275eee5967595cc68528f38`
- `boards/COMPARE_VR-010.jpg` — 510,497 B, MD5 `665fd425d0b6fb7bd1cd5436bf27b34b`
- `boards/COMPARE_VR-011.jpg` — 408,974 B, MD5 `1be8450ca37c5d60654d95c78747e4aa`
- `boards/COMPARE_EST.jpg` — 526,257 B, MD5 `1cd0a2fb4d4eb45a662213f486dafa9b`
- `boards/COMPARE_WALL.jpg` — 425,152 B, MD5 `ff0afa1674baf4951e5e1d46fb36ba76`

## 3. Integrity of the frame

Each candidate is a 2560×1440 copy of its master with the artwork panel box `(60,152)–(1961,1321)` replaced. Pixel comparison against the master outside that box returned **0 changed pixels and max channel-sum difference 0** for all five candidates, so the board chrome, metadata column and palette strip are untouched. This does not make a candidate approved, canon, or a version of record.

## 4. Attempts retained, not offered as candidates

- `cand_panels/CAND_VR-007_NNEKAS_INTERIOR_V004_PANEL.jpg` — generative attempt. **Set aside:** the sheath became a *bare tapered blade* and the costume gained a diagonal chest strap and arm bands. Contradicts the brief on both counts.
- `cand_panels/CAND_VR-006_MOTHERS_COURTYARD_V004_PANEL.jpg` — generative attempt. **Set aside:** the weapon came back longer and blade-like, the figure drifted to the frame edge, and the costume changed.
- Both are kept as evidence so the failure is not repeated, and neither is put forward for review.


---

## 5. VR‑008 V007 — revision package (2026‑11‑17)

Produced after the rejection of V006. Source re‑verified before use; every artefact hashed after write.

| Item | Path | Bytes | MD5 | SHA‑256 |
|---|---|---|---|---|
| Source master (unchanged) | `masters/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005.jpg` | — | `a94a084af0f7fb6d8016a6e33d44dc62` | — |
| Midriff donor panel | `panels/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V004_PANEL.jpg` | — | `9d6dce30bb25641efe43c25e4c195132` | — |
| Retouched panel (side artefact) | `work2/V007_panel.png` | — | — | — |
| **Candidate** | `final/CAND_VR-008_V007_2560x1440.png` | 3,126,132 | `8e493590c632a545ff8d198316cd67b5` | `0763fd75a9982c2237238b5e7cc35b7e21dc12d2fc63ce297048c3f7667dd9a7` |
| Comparison board | `submit/B2_COMPARE_VR-008_V005_vs_V007.jpg` | 765,180 | `ad788e8f6c871f3e99104fc467e950d1` | — |
| Difference map | `submit/B2_PIXELDIFF_VR-008_V007.jpg` | 346,459 | `242fc74f89f384ac870877d866c059da` | — |

### Edit inventory — every changed region, with pixel counts

| Region | Coordinates (panel, 1901×1169) | Changed px | Authorised by |
|---|---|---|---|
| A fracture | x 425–528, y 512–862 | 1,504 | report defect A |
| B midriff | x 852–1000, y 614–764 | 8,481 | report defect B |
| C armlet | x 996–1076, y 536–628 | 3,633 | report defect C |
| outside all three | — | **0** | — |
| Chrome — header `V005`→`V007` | frame (2481,33)–(2504,63) | 329 | report defect D |
| Chrome — KNOWN ISSUES, crack sentence erased | frame (2266,963)–(2552,993) and (1996,992)–(2552,1024) | 4,185 | report defect D |
| Chrome — footer line 2 re‑set | frame (962,1358)–(2560,1390) | 7,979 | report defect D |
| Chrome — V007 note added | frame (968,1399)–(2560,1421) | 6,301 | report defect D |

Chrome typeface disclosure: the board's original typeface is unavailable offline, so the re‑set footer line and the added note are set in DejaVu Sans. The header digit and all erasures use the board's own background colour (9,13,24); no new glyph was introduced into the metadata column.

### Disclosed limits of the measurement

1. The rejection report's quoted boxes do not coincide with the features at full resolution (midriff and armlet boxes are offset ≈ +85 x / +45 y; the armlet box lands on the hut wall). I matched the described features and recorded the discrepancy in `B2_REJECTION_RESPONSE_VR-008_V006.md` §3.
2. The midriff transfer is resampled by 1 % because V004 and V005 are aligned at scale 1.01 — the transferred skin is marginally softer than its surroundings.
3. The armlet is a painted reconstruction; no approved armlet patch exists to transfer.
4. Difference threshold for "changed" is sum|ΔRGB| > 12, i.e. above JPEG quantisation noise; sub‑threshold changes inside the masks are not counted.

---

## 6. VR-008 V008 — armlet transfer (2026-11-17)

| Item | Path / ID | Bytes | MD5 | SHA‑256 |
|---|---|---|---|---|
| Reference source | `refs/CHAR_ADANNA_MASTER_REFERENCE_V001.jpg` · `1FY3hw3602iB-1405RgUIO3ih2USmck_Y` | — | `901a5009ab5ff44a81fb3799c7e6de6d` | — |
| Working panel | `work2/V008_panel.png` | — | — | — |
| **Candidate** | `final/CAND_VR-008_V008_2560x1440.png` | 3,129,530 | `a41548911b4d991e7e05aad6474441aa` | `cfc2788fa7c0762b86d76f24c6b7cebb214cf9cc4242b51c9a778365f4e3df4e` |
| Comparison board (with references) | `submit/B2_COMPARE_VR-008_V005_to_V008_with_references.jpg` | 730,009 | `cdf09d5f7bf0ee321c971db371516c61` | — |

### Edit inventory

| Region | Coordinates (panel 1901×1169) | Changed px vs V005 |
|---|---|---|
| A fracture (unchanged from V007) | x 425–528, y 512–862 | 1,504 |
| B midriff (unchanged from V007) | x 852–1000, y 614–764 | 8,481 |
| C armlet (transfer, replaces V007's painting) | x 996–1080, y 533–632 | 2,209 |
| outside all three | — | **0** |
| V007 → V008 | x 998–1076, y 545–620 | 4,092, all inside C |

Chrome for V008: header `V007`→`V008` (320 px), KNOWN ISSUES erasure reused (4,185 px), footer line 2 re-set (8,108 px), footer note rewritten for the transfer (9,714 px). No other pixel of the frame differs from V005.

### Transfer parameters (reproducible)

Source crop `(580,1010)–(800,1140)` of the master; rotate −7.6°; take `(45,46)–(200,110)` of the rotated crop; resample to 74×29; grade source mean 23.9 → 31.4 (= 0.86 × local arm mean 36.6); bow 2.6 px; edge fade 6 px horizontally, 2.5 px vertically; occlusion 0.45 at 1.6 px blur.

### Disclosed limits

1. The band is downscaled ≈3× from the close-up portrait to this arm's width, so the finest groove detail is softened — inherent to the size difference, not a defect of the transfer.
2. The band's ends fade into the arm rather than showing a clasp; the reference does not expose a clasp at this angle either.
3. Chrome typeface remains DejaVu Sans for the re-set footer and note (board typeface unavailable offline).
