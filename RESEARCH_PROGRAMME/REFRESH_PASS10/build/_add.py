import ast
P='build/md_findings_pass10.py'
HDR=["# Pass-10 text findings, rebuilt 2026-11-18 from re-read bodies (not from earlier notes).",
"# Key: first 12 chars of the Drive ID. Value: (coverage, finding, assessment).",
"# coverage: FULL = whole body read this pass; HT = head and tail only (see E11)."]
def load():
    ns={}; exec(open(P).read(), ns); return dict(ns['M'])
def save(new):
    M=load()
    for k,v in new.items():
        assert len(k)==12, k
        M[k]=v
    open(P,'w').write("\n".join(HDR+["M = {"]+[f"{k!r}: {M[k]!r}," for k in sorted(M)]+["}"])+"\n")
    print('entries', len(load()))
