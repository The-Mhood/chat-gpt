import csv, hashlib, os, shutil, sys
ROOT = "/home/user/chat-gpt"
DEST = "/tmp/refresh_pass9/src"
man = os.path.join(ROOT, "RESEARCH_PROGRAMME/REFRESH_2026-11-18_FULL/pending_manifest.tsv")
folder_filter = sys.argv[1] if len(sys.argv) > 1 else None
ok, bad, missing = [], [], []
with open(man) as f:
    for row in csv.reader(f, delimiter="\t"):
        folder, fid, name, mime, size, md5 = row
        if folder_filter and folder != folder_filter:
            continue
        src = os.path.join(ROOT, "google_drive", name)
        if not os.path.exists(src):
            missing.append((fid, name)); continue
        data = open(src, "rb").read()
        h = hashlib.md5(data).hexdigest()
        if h != md5 or len(data) != int(size):
            bad.append((fid, name, len(data), size, h, md5)); continue
        dst_dir = os.path.join(DEST, folder)
        os.makedirs(dst_dir, exist_ok=True)
        shutil.move(src, os.path.join(dst_dir, fid + "__" + name))
        ok.append(fid)
print("verified+moved:", len(ok))
print("missing:", missing)
print("mismatch:", bad)
