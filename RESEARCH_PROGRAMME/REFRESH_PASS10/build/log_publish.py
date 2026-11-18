import sys,os
# usage: log_publish.py seq drive_id drive_bytes drive_md5 [drive_id drive_bytes drive_md5 ...]
# appends rows to build/publish_log.tsv and ../publish_log.tsv after checking against report_md5.tsv
tbl={l.split('\t')[0]:l.rstrip('\n').split('\t') for l in open('build/report_md5.tsv')}
args=sys.argv[1:]
rows=[]
for i in range(0,len(args),4):
    seq,did,dbytes,dmd5=args[i:i+4]
    f,lb,lm=tbl[seq][1],tbl[seq][2],tbl[seq][3]
    ok = (dbytes==lb and dmd5==lm)
    rows.append(f"{seq}\t{f}\t{did}\t{lb}\t{lm}\t{dbytes}\t{dmd5}\t{'yes' if ok else 'NO'}\t1qEEDsGMhCy6JBd0hrrMPuZdFBfC8Zll2")
    print(seq, 'OK' if ok else 'MISMATCH')
for p in ['build/publish_log.tsv','publish_log.tsv']:
    with open(p,'a') as h: h.write('\n'.join(rows)+'\n')
