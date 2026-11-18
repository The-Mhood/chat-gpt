import sys, hashlib, os
# usage: verify_log.py "name|fileid|drive_md5|drive_size|parent" ...
LOG = 'REFRESH_PASS11/work/upload_log.tsv'
PARENT = '1qEEDsGMhCy6JBd0hrrMPuZdFBfC8Zll2'
done = {l.split('\t')[0] for l in open(LOG) if l.strip()} if os.path.exists(LOG) else set()
out = []
for arg in sys.argv[1:]:
    name, fid, dmd5, dsize, parent = arg.split('|')
    p = os.path.join('REFRESH_PASS11/reports', name)
    data = open(p, 'rb').read()
    lmd5 = hashlib.md5(data).hexdigest(); lsz = len(data)
    ok = (lmd5 == dmd5) and (str(lsz) == dsize) and (parent == PARENT)
    status = 'OK' if ok else 'MISMATCH'
    print(f"{status} {name} local={lsz}/{lmd5} drive={dsize}/{dmd5} parent_ok={parent==PARENT}")
    if name in done:
        print('  (already logged, not duplicated)')
        continue
    out.append('\t'.join([name, fid, parent, str(lsz), lmd5, dsize, dmd5, status]))
with open(LOG, 'a') as f:
    for line in out: f.write(line + '\n')
