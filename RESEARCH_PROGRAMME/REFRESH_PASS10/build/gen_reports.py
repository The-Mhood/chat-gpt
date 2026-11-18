import sys, re, os, importlib.util
sys.path.insert(0, '/home/user/chat-gpt/RESEARCH_PROGRAMME/REFRESH_PASS10/build')
import md_findings_pass10 as MF
MD = MF.M  # body-verified findings for every markdown candidate (ORIGINAL and ASSISTANT)
ROOT = '/home/user/chat-gpt/RESEARCH_PROGRAMME/REFRESH_PASS10'
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(ROOT, 'pass10_manifest.tsv')) if l.strip()][1:]

def look(d, i):
    hits = [k for k in d if i.startswith(k)]
    return d[max(hits, key=len)] if hits else None

# ---- image notes parse ----
def parse_notes(path):
    out = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(r'^- (\S+)\s+(.*)$', line.rstrip('\n'))
        if m:
            out[m.group(1)] = m.group(2)
    return out
notes_o = parse_notes(os.path.join(ROOT, 'notes/image_findings_batch1.md'))
notes_a = parse_notes(os.path.join(ROOT, 'notes/image_findings_assistant.md'))
def note_for(i, pool):
    hits = [k for k in pool if i.startswith(k[:10]) or k.startswith(i[:10])]
    if hits:
        return pool[hits[0]]
    return None

# manual overrides where notes ID transcription differs from manifest (E13)
NOTE_OVERRIDE = {'1xDJaz1ip1sU': '1xDJazip1sU4mNFkUpjjPFcCkOGu1d-N', '1v_Sls4vJNSV': '1v_SIs4vJNSVZHF5XV-RHEM-PQ2c9ImmV'}

# ---- assessment flags for specific candidates ----
FLAG = {
 '118DT3OivKh7': 'Comparison board only. Strips on rampart read as flags (author residual list). Relevant to HOLD H3.',
 '1_vJFw7KNJRn': 'Strips still read as flag-like on the sheet (V002 board). HOLD H3 applies per register; not released by this report.',
 '11MmHTZ-CawZ': 'Open: CQ-9 blade and scabbard (none depicted); RQ-10-1 coiled armlet; pendant FICTIONAL. Chirality of BACK disputed in prior research output (see E5).',
 '14uOMGJYXucA': 'Open: RQ-10-1 armlet; pendant FICTIONAL. Blade and scabbard not drawn (CQ-9 open).',
 '1nNFdXOcJYpo': 'Open: CQ-9 blade and scabbard; RQ-10-1; OAD-40. Baldric LEFT shoulder to RIGHT hip (see E5).',
 '1nYt7Tvoyn7Q': 'Open items as FRONT. Far-side beaded temple and scar partly foreshortened.',
 '1MA20ws6ujgQ': 'Open: CQ-9 blade/scabbard; RQ-10-1 armlet; OAD-40. Baldric over LEFT shoulder to RIGHT hip (see E5).',
 '1JWX8z0UcLpq': 'Open: CQ-9 blade and scabbard (none depicted); RQ-10-1 coiled armlet.',
 '1566AiHfIYW0': 'Board states item 5 (basal hut scale) NOT done; V013 unapproved.',
 '1Muhup': 'Item 5 (basal hut scale) recorded on sheet as NOT FIXED. Client review pending. Flag carried: basal scale not fixed.',
 '1MuhupyLWP2f': 'Item 5 (basal hut scale) recorded on sheet as NOT FIXED. Client review pending. Flag carried.',
 '1lPnwpnYUXts': 'RETOUCH GUIDE, not artwork. Marks an object correction on the VR-006 base. BLOCKED (CQ-9 blade authority). Not a candidate.',
 '1C_jk77ERIws': 'RETOUCH GUIDE, not artwork. Marks a correction on the VR-007 base. BLOCKED (CQ-9 blade authority). Not a candidate.',
 '1lXvNjgnJpWx': 'Board footer: requirement D (foreground house) unresolved, "needs a decision".',
 '1gcB6yB2ERgf': 'Board footer quotes "NO V004 EXISTS IN DRIVE"; pixel footer not verified in this view.',
 '1T9Eziwd_5Uc': 'Single-storey repaint of the mound (V005 candidate). REVIEW REQUIRED. Pixel proof per board: 1,234,163 px changed.',
 '1oGedLDNFIWE': 'Board: fracture now more prominent than "subtle legibility" (author residual).',
 '1bs7I2_iPaWQ': 'Author note (batch 6) flags a faint signature-like scrawl bottom-right on the related SUB-006 text; not confirmed in this reduced view.',
 '1OB-WeC6Z6hr': 'Figures 0 (OAD-40). Board FICTIONAL. Earthen idiom.',
 '1a4dO7GjSe89': 'No printed textiles visible. Figures 0.',
 '1uUV4ZaZekbL': 'Figures 0 (OAD-40). Footer FICTIONAL, no cultural claim.',
 '1v_Sls4vJNSV': 'Board: V003 candidate adds a square stone-lined outlet at the foot of the slab. This is a generative candidate not approved; see E4 for register text on the VR-010 outlet ruling.',
 '1DtT7wfMJt63': 'Architecture reads North African/Levantine; redo flagged in batch notes.',
 '1sRagEJxTo': 'Verification artefact, not a candidate.',
 '1NQCWe-zXx7D': 'Verification artefact (diff map), not a candidate image.',
}
# text-note classification for ORIGINAL images that the batch notes flag (from text_findings_ORIGINAL)
FLAG_O = {
 '12v0y9sOdgbn': 'Baked "STATUS: APPROVED 2026-11-15" text on an unapproved candidate. Not an approval.',
 '1IljvE5kdAQK': 'Baked "STATUS: APPROVED / DATE 2026-11-15" text on an unapproved candidate. Not an approval.',
 '1gDpiCSJVuhS': 'Board header UNAPPROVED — PENDING CD; open items shown on board.',
 '1RcEkIjAlMqO': 'Background of British-style terraces: off-brief for Igbo/West African setting (batch flag, SUB-006).',
 '1uHEH6I8SKhw': 'APPROVED stamp is on the reference panel, not the candidate panel.',
 '1Vyt8yjZAcy8': 'THREE_QUARTER hilt visible over shoulder; not in any reference (V001 rejected).',
}
# ---- exceptions catalogue (codes) ----
EXC = {
 'E1': 'ORIGINAL EXP-001 (1SsRkI8j): the Drive file is a 2,537-byte text report, not artwork. It cites artwork MD5 bce36fd7 / 337,726 B, which is absent from the folder. Register text records an overwrite; restore needs Drive version history (owner action). Artwork cannot be researched.',
 'E2': 'RESOLVED, no defect. The B2_SUBMISSION_MANIFEST_v2 MD5 in the pass-10 manifest (5fac8fed2b42a388c09ece13cbcc4d18) matches a fresh Drive get_file and the local copy. An earlier record of a 33-character Drive value was a transcription error and is withdrawn.',
 'E3': 'ORIGINAL ADANNA TURNAROUND PENDING note (1m32I8rI) lists four candidate Drive IDs (1c0mXB…, 1JnnvbtnD…, 1ukZNph…, 18sbSdv…) that are not in the folder. The folder holds four *_REFERENCE_VS_CANDIDATE.jpg files instead. Recorded; not reconciled.',
 'E4': 'WITHDRAWN. An earlier draft said the BATCH7 note listed CH05 EXP-002 as held; the body lists it as produced (1oMCsvO-). No discrepancy.',
 'E5': 'ADANNA baldric route conflict: V002 plates say over RIGHT shoulder to LEFT hip; V003/V004 copy says LEFT shoulder to RIGHT hip with painted strap not repainted. Not reconciled.',
 'E6': 'Register headers cite branch arena/90e15011-chat-gpt, not this session branch. Recorded; not reconciled.',
 'E7': 'CQ-9 blade authority: WEAPON_ADANNA_PRIMARY_BLADE_V001 is REVIEW REQUIRED but cited as approved on master footers; its construction disagrees with VR-006/007 compositions. Blocks VR-006/007.',
 'E8': 'Placement: the author records that PENDING/ASSISTANT_VA_SUBMISSIONS was created rather than found, and that five live candidates were in wrong parents and moved. Its own moves table lists seven rows; the count is inconsistent in the record. Recorded by author; not re-audited.',
 'E9': 'ASSISTANT folder listing: page 2 verified (49 files, next token null); page 1 output truncated and not fully parsed. Visible rows match manifest.',
 'E10': 'ORIGINAL folder listing: output truncated; not fully parsed. Visible rows match manifest; manifest values were hand-typed.',
 'E11': 'Partial text reading: head and tail only for this file (middle sections not read). Findings are limited to what was read.',
 'E12': 'COMP_ADANNA_NNEKAS_YARD_FULL_FIGURE_V001 is BLOCKED (no rejection report) and is not a PENDING listing item. Not researched here.',
 'E13': 'Manifest ID transcription differs from a note-typed ID (1xDJaz1ip / 1xDJazip; 1v_Sls4v / 1v_SIs4v). Manifest value used. Not verified against live listing.',
 'E14': 'Image coverage: the image-notes file records batch F (7 images) that the action log did not record as viewed. All 7 were re-viewed on 2026-11-18 at 1000px and match their notes.',
}
PARTIAL_TXT = ('1U4xF6NU', '1RO7-agpxO', '1uvSrH46', '1WlPZ0g2', '1fEhvp7x', '1mODNxto', '1sRagEJx', '1xPD33CT', '1I9BzFKP', '1RO7-agpxO9')
CAND_EXC = {
 '1SsRkI8jhM': ['E1'], '1m32I8rIhe': ['E3'], '1u_ey_gPxd': ['E2'],
 '1-QexQjgdEF': ['E5'], '1obe3Ry3B8': ['E5'], '1QFJ_9JSjm': ['E7'], '1h_s2Zaw5l': ['E8', 'E6'],
 '1epIa9Tkph': ['E6'], '1LVTcBLlt5': ['E8'], '1lPnwpnYUXtsVd': ['E7'], '1C_jk77ERIws': ['E7'],
 '1oGedLDNFIWE': ['E14'],
}
def cand_exc(cid, folder, mime):
    ex = list(CAND_EXC.get(cid[:10], [])) if cid[:10] in CAND_EXC else []
    for k, v in CAND_EXC.items():
        if cid.startswith(k) and k not in ('',) and v != ex:
            ex = list(dict.fromkeys(ex + v))
    if any(cid.startswith(p) for p in PARTIAL_TXT):
        ex.append('E11')
    if folder == 'ASSISTANT' and mime.startswith('image/'):
        ex.append('E9')
    if folder == 'ORIGINAL' and mime.startswith('image/'):
        ex.append('E10')
    return list(dict.fromkeys(ex))

SUPERSEDED_FIX = {
 '1QtJIm1YcL8o': 'The ASSISTANT folder holds a V002 of this scene (1e98rc…); see its record.',
 '1P-PjtOw4TrI': 'The ASSISTANT folder holds a V002 of this scene (13Dc48…); see its record.',
}
def fix_assess(t, cid):
    for k, v in SUPERSEDED_FIX.items():
        if cid.startswith(k[:10]):
            t = t.replace('Superseded in ASSISTANT folder by V002.', v).replace('Superseded by ASSISTANT V002.', v)
    return t

def note_text(r):
    pool = notes_o if r[0] == 'ORIGINAL' else notes_a
    if r[1].startswith('1v_Sls4v'):
        return [v for k, v in pool.items() if k.startswith('1v_SIs4v')][0]
    if r[1].startswith('1xDJaz1ip'):
        return [v for k, v in pool.items() if k.startswith('1xDJazip')][0]
    n = note_for(r[1], pool)
    if n is None:
        for k, v in pool.items():
            if k.startswith(r[1][:6]) or r[1][:6] in k:
                n = v; break
    return n

def build(r):
    folder, did, name, mime, size, md5 = r
    stem = re.sub(r'[^A-Za-z0-9]+', '_', re.sub(r'\.[A-Za-z0-9]+$', '', name)).strip('_')[:110]
    exc = cand_exc(did, folder, mime)
    if mime.startswith('image/'):
        method = ('Image viewed at 1000px-max JPEG copy (`/tmp/p10view`), 2026-11-18. Observations recorded in '
                  + ('`notes/image_findings_batch1.md`' if folder == 'ORIGINAL' else '`notes/image_findings_assistant.md`') + '.')
        finding = note_text(r) or 'No observation note found for this candidate.'
        assess = FLAG.get(did[:12]) or FLAG_O.get(did[:12]) or 'Unapproved candidate. Observations above are as seen in the reduced view; no approval or rejection implied.'
        if folder == 'ORIGINAL' and look(MD, did) and False:
            base = look(MD, did)[2]
            assess = fix_assess(base, did) + (' ' + FLAG_O[did[:12]] if did[:12] in FLAG_O else '')
        if did.startswith('1SsRk'):
            finding = 'Not an image.'
        cov = 'Image: 1000px JPEG view.'
    else:
        if did.startswith('1SsRkI8j'):
            finding, assess = MD['1SsRkI8jhMeK'][1], 'Cannot be assessed as artwork (E1).'
            method = 'Text read in full, 2026-11-18 (`notes/text_findings_ORIGINAL.md`).'
        elif folder == 'ORIGINAL':
            t = look(MD, did)
            if t is None:
                finding, assess = 'No record found in ORIGINAL text notes.', 'Not assessed.'
            else:
                finding, assess = t[1], t[2]
            method = 'Text read in full, 2026-11-18 (`notes/text_findings_ORIGINAL.md`).'
        else:
            t = look(MD, did)
            if t is None:
                finding, assess, cov = 'No record found.', 'Not assessed.', 'Not read.'
            else:
                cov, finding, assess = t
            cov_txt = {'FULL': 'read in full (whole body)', 'HT': 'head and tail read; middle sections not read (E11)',
                       'EARLIER': 'read in full in an earlier pass-10 window (`notes/text_findings_ASSISTANT_part1.md` or prior record)'}.get(cov, cov)
            method = 'Text: ' + cov_txt + '.'
    lines = [
        f'# Research report — {name}', '',
        '> Pass 10 research assessment. Advisory only; not an approval or rejection. CD decides; Our Eyes disposes.', '',
        '| Field | Value |', '|---|---|',
        f'| Folder | {folder} VA submissions (PENDING `11DxQ0d_noAPbZCPrYQBkUonHFl_cFAWm`) |',
        f'| Drive ID | `{did}` |', f'| Name | `{name}` |', f'| MIME | {mime} |',
        f'| Bytes | {size} |', f'| MD5 (manifest) | `{md5}` |', '',
        '## Inspection', '', method, '',
        '## Observed contents', '', finding, '',
        '## Research assessment', '', assess, '',
        '## Exceptions for this candidate', '',
    ]
    if exc:
        for c in exc:
            lines.append(f'- **{c}** — {EXC[c]}')
    else:
        lines.append('None recorded for this candidate.')
    lines += ['', '---', 'Pass 10 · generated from `pass10_manifest.tsv` and the notes files in `RESEARCH_PROGRAMME/REFRESH_PASS10/notes/`.', '']
    fn = f'RR10_{stem}__{did[:10]}.md'
    return fn, '\n'.join(lines), exc

if __name__ == '__main__':
    os.makedirs(os.path.join(ROOT, 'reports'), exist_ok=True)
    index = []
    for r in rows:
        fn, body, exc = build(r)
        open(os.path.join(ROOT, 'reports', fn), 'w', encoding='utf-8').write(body)
        index.append((r[0], r[1], r[2], fn, exc, len(body)))
    with open(os.path.join(ROOT, 'build', 'report_index.tsv'), 'w', encoding='utf-8') as f:
        f.write('folder\tdrive_id\tname\treport_file\texceptions\tbytes\n')
        for x in index:
            f.write('\t'.join([x[0], x[1], x[2], x[3], ','.join(x[4]) or '-', str(x[5])]) + '\n')
    print('reports written', len(index))
