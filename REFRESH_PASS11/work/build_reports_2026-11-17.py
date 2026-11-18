import csv, os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from desc_a import D as DA
from desc_b import D as DB
from desc_c import D as DC
import importlib.util
_spec = importlib.util.spec_from_file_location('corr', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'corrections_2026-11-17.py'))
_corr = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_corr)
DCORR = _corr.C
D = {**DA, **DB, **DC}
D.update(DCORR)
for k in list(D):
    if k.startswith('CH05-') or k.startswith('CH06-') or k.startswith('CH04-') or k.startswith('CH03-'):
        D.setdefault('ENV_' + k, D[k])
ROOT = '/home/user/chat-gpt'
TSV = os.path.join(ROOT, 'REFRESH_PASS11/work/live_listing_2026-11-17.tsv')
REP = os.path.join(ROOT, 'REFRESH_PASS11/reports')
rows = list(csv.DictReader(open(TSV), delimiter='\t'))
assert len(rows) == 78, len(rows)
# replace prior-refresh reports
for f in glob.glob(os.path.join(REP, '*.md')):
    os.remove(f)
manifest = []
missing = []
for i, r in enumerate(rows, 1):
    name = r['name']
    if name not in D:
        missing.append(name); continue
    stem = os.path.splitext(name)[0]
    rep = f"RR11_{name}".rsplit('.', 1)[0] + '.md'
    local = os.path.join(ROOT, 'google_drive', name)
    data = open(local, 'rb').read()
    import hashlib
    md5 = hashlib.md5(data).hexdigest()
    size = len(data)
    assert md5 == r['md5'] and str(size) == r['bytes'], name
    body = f"""# Picture review: {stem}

- Seq: {i} of 78
- Source folder: {r['folder']}
- Picture file: {name}
- Drive file ID: {r['drive_id']}
- Local path: google_drive/{name}
- Local bytes: {size}
- Local MD5: {md5}
- Live Drive bytes and MD5 (listing 2026-11-17): {r['bytes']} / {r['md5']} (match)

## Visible content

{D[name]}

## Scope

Written from this picture only. The picture was viewed and the description was checked against it in this pass. The picture was not modified. Prior-refresh reports and earlier notes were not used.
"""
    open(os.path.join(REP, rep), 'w').write(body)
    manifest.append(f"{rep}\t{r['drive_id']}\t{name}\t{size}\t{md5}\t{r['bytes']}\t{r['md5']}\t{r['folder']}\t{i}")
open(os.path.join(ROOT, 'REFRESH_PASS11/work/report_manifest_2026-11-17.tsv'), 'w').write('\n'.join(manifest) + '\n')
print('written', len(manifest), 'missing_desc', missing)
