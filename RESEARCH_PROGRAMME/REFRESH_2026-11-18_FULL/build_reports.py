import csv, hashlib, os, re
ROOT = "/home/user/chat-gpt/RESEARCH_PROGRAMME/REFRESH_2026-11-18_FULL"
SRC = "/tmp/refresh_pass9/src"
OUT = os.path.join(ROOT, "reports")
RESEARCH_ID = "1qEEDsGMhCy6JBd0hrrMPuZdFBfC8Zll2"
FOLDER_IDS = {"ORIGINAL": "1YUCfczTDGsdcMGz3favvphMabMR9q9PJ", "ASSISTANT": "16p2TYXn16u9UNdMlJzjTK873YK_Fk7Ab"}
NOTES = open("/tmp/refresh_pass9/notes/image_notes.md").read() + "\n" + open("/tmp/refresh_pass9/notes/text_notes_A.md").read()

bullets = []
for line in NOTES.splitlines():
    if not line.startswith("- "):
        continue
    m = re.search(r"\(([A-Za-z0-9_\-]{4,})[,)]", line)
    if m:
        bullets.append((m.group(1), line[2:]))

STATUS_RE = re.compile(r"(\*\*Status|Status:|STATUS|Verdict|VERDICT|Supersedes|Answers |APPROVED|REJECTED|HOLD|NOT RECOMMENDED|REVISE|UNRESOLVED|BLOCKED|PWQ|CANDIDATE)")

def note_for(fid):
    hits = [t for tok, t in bullets if fid.startswith(tok)]
    return hits

def md_extract(path):
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    title = next((l for l in lines if l.startswith("# ")), "(no H1 heading)")
    hits = [l.strip() for l in lines if STATUS_RE.search(l)]
    return title[:160], [h[:220] for h in hits[:4]]

rows = [r for r in csv.reader(open(os.path.join(ROOT, "pending_manifest.tsv")), delimiter="\t")]
made = []
for folder, fid, name, mime, size, md5 in rows:
    path = os.path.join(SRC, folder, f"{fid}__{name}")
    data = open(path, "rb").read()
    assert len(data) == int(size) and hashlib.md5(data).hexdigest() == md5, (fid, name)
    stem = name.rsplit(".", 1)[0]
    is_image = mime.startswith("image/")
    notes = note_for(fid)
    lines = []
    lines.append(f"# RR_{folder}_{stem}")
    lines.append("")
    lines.append("**Publication run:** REFRESH 2026-11-18 (pass 9). **Type:** research observation report. **Not a verdict.** Reviewer decision required.")
    lines.append("")
    lines.append("## Identity (verified)")
    lines.append(f"- Folder of origin: {folder} (`{FOLDER_IDS[folder]}`)")
    lines.append(f"- Source file ID: `{fid}`")
    lines.append(f"- Source name: `{name}`")
    lines.append(f"- MIME: {mime}; size: {size} bytes; MD5: `{md5}`")
    lines.append("- Local staged copy re-verified against the manifest (size and MD5) before this report was written.")
    lines.append("")
    lines.append("## Findings")
    gaps = []
    if notes:
        for n in notes:
            lines.append(f"- {n}")
        depth = "Pass-9 observation recorded in notes" + (" (image viewed at 1000 px)." if is_image else " (text read in pass 9).")
    elif is_image:
        depth = "Viewed at 1000 px in pass 9; no per-file observation line was written to the notes, so none is reported here."
        lines.append("- Visual check only. No per-file observation was recorded in the pass-9 notes.")
        gaps.append("No per-file observation line recorded for this image.")
    else:
        title, hits = md_extract(path)
        depth = "Automated extraction only (title, status and verdict lines). Full body not read in pass 9."
        lines.append(f"- Title: {title}")
        for h in hits:
            lines.append(f"- Line: {h}")
        if not hits:
            lines.append("- No status or verdict line matched the extraction pattern.")
        gaps.append("Full body text not read; findings limited to title and status lines.")
    lines.append("")
    lines.append("## Read depth")
    lines.append(depth)
    lines.append("")
    lines.append("## Evidence gaps")
    if is_image:
        gaps.append("Checked on a 1000 px viewing copy only; not checked against the full-resolution original at pixel level.")
    if fid.startswith("1SsRkI8j"):
        gaps.append("This ID holds a 2,537-byte text research report, not the JPEG. The artwork (MD5 bce36fd7..., 337,726 bytes) is not present under this ID.")
    if "VR-011" in name or fid.startswith("1_vJFw"):
        gaps.append("The on-image header reads ENV_GATES_DEAD_LANDING_OF_UNCLAIMED_V001, which does not match this V002 file. Administrative only; flagged, not reconciled.")
    if "ADANNA" in name:
        gaps.append("Adanna baldric route is recorded as LEFT-shoulder-to-RIGHT-hip in V003 copy and RIGHT-shoulder-to-LEFT-hip in the V002 alignment sheet. Not reconciled.")
    if not gaps:
        gaps.append("None recorded beyond the read depth stated above.")
    for g in gaps:
        lines.append(f"- {g}")
    lines.append("")
    lines.append("## Status")
    lines.append("Not approved. Not canon. No filing decision is made by this report. Open items above remain open.")
    lines.append("")
    rname = f"RR_{folder}_{stem}_{fid[:8]}.md"
    open(os.path.join(OUT, rname), "w", encoding="utf-8").write("\n".join(lines))
    made.append((folder, fid, name, rname, len(data), md5, depth.split(" (")[0]))

with open(os.path.join(ROOT, "report_map.tsv"), "w") as f:
    for m in made:
        f.write("\t".join(map(str, m)) + "\n")
print("reports:", len(made))
from collections import Counter
print(Counter(m[6] for m in made))
print("names unique:", len(set(m[3] for m in made)))
