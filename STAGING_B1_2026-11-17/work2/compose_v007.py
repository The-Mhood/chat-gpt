from PIL import Image, ImageDraw, ImageFont
import numpy as np

M = Image.open('masters/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005.jpg').convert('RGB')
P = Image.open('work2/V007_panel.png').convert('RGB')
BOX = (60,152,1961,1321)
assert P.size == (BOX[2]-BOX[0], BOX[3]-BOX[1]), P.size
out = M.copy(); out.paste(P, (BOX[0],BOX[1]))
d = ImageDraw.Draw(out)
BG = (9,13,24)

# --- header: V005 -> V007 -------------------------------------------------
hdr_bg = tuple(np.median(np.asarray(M.crop((2504,34,2540,62))).reshape(-1,3),axis=0).astype(int))
d.rectangle([2481,33,2504,63], fill=hdr_bg)
tancol = tuple(np.percentile(np.asarray(M.crop((2427,36,2478,60))).reshape(-1,3),92,axis=0).astype(int))
f7 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
d.text((2485,57), '7', font=f7, fill=tancol, anchor='ls')

# --- known issues: drop the obsolete crack sentence -----------------------
d.rectangle([2266,963,2552,993], fill=BG)     # "The crack in the seal"
d.rectangle([1996,992,2552,1024], fill=BG)    # "is hard to see."

# --- footer: remove the false "approved blade board" claim ----------------
d.rectangle([962,1358,2560,1390], fill=BG)    # footer line 2 (false blade-source claim)

# --- footer line 2, re-set with the true weapon status --------------------
f14 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
d.text((968,1378), "reference; blade from the blade board \u2014 REVIEW REQUIRED, CQ-9 open: not an approved source. Not approved.",
       font=f14, fill=(175,179,191), anchor='ls')

# --- annotation: what V007 changed (in previously empty chrome) -----------
ann = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
d.text((968,1400), "V007 \u2014 bare midriff restored from V004 (aligned crop); left-arm multi-coil bronze armlet repainted, no reference transfer existed;",
       font=ann, fill=(152,160,174), anchor='ls')
d.text((968,1418), "synthetic crack replaced with a plaster fracture. Candidate only; not approved.",
       font=ann, fill=(152,160,174), anchor='ls')

out.save('final/CAND_VR-008_V007_2560x1440.png')
print('saved', out.size)

# ---- verification: where did pixels change? -----------------------------
a0 = np.asarray(M).astype(int); a1 = np.asarray(out).astype(int)
diff = (np.abs(a0-a1).sum(axis=2) > 12)
ys,xs = np.where(diff)
print('changed px total:', len(xs))
regions = {
 'panel': (60,152,1961,1321),
 'header': (2480,32,2505,64),
 'known_issues': (1994,962,2554,1025),
 'footer_line2': (961,1357,2560,1391),
 'footer_note': (960,1391,2560,1425),
}
for k,(x0,y0,x1,y1) in regions.items():
    m = diff[y0:y1, x0:x1].sum()
    print(f'  {k:16s} {m:7d}')
cov=np.zeros(diff.shape,bool)
for (x0,y0,x1,y1) in regions.values(): cov[y0:y1,x0:x1]=True
print('changed px outside listed regions:', int((diff&~cov).sum()))
shell = diff.copy()
