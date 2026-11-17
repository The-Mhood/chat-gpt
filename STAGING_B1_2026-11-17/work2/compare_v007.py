from PIL import Image, ImageDraw, ImageFont
F = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
W,H = 2400, 1345
c = Image.new('RGB',(W,H),(13,17,23)); d=ImageDraw.Draw(c)
d.text((24,14), "VR-008  COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL   V005 (REVIEW REQUIRED)  ->  V007 CANDIDATE (REVIEW REQUIRED)", font=FB(24), fill=(255,255,255))
d.text((24,46), "Rejection of V006 answered by targeted retouch on the V005 master panel. No generative pass. 0 changed pixels outside the three edit masks.", font=F(17), fill=(170,180,192))

M = Image.open('masters/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005.jpg').convert('RGB')
N = Image.open('final/CAND_VR-008_V007_2560x1440.png').convert('RGB')
BOX=(60,152,1961,1321)
mp = M.crop(BOX); np_ = N.crop(BOX)
tw = 1150; th = int(tw*mp.size[1]/mp.size[0])
y0 = 78
for i,(im,lab) in enumerate([(mp,'BEFORE — V005 panel (unchanged)'),(np_,'AFTER — V007 panel')]):
    x = 24 + i*(tw+52)
    c.paste(im.resize((tw,th), Image.LANCZOS),(x,y0))
    d.rectangle([x-1,y0-1,x+tw,y0+th], outline=(90,100,115))
    d.text((x, y0+th+8), lab, font=FB(18), fill=(235,238,242))

import json
st=json.load(open('work2/v007_diffstats.json'))
dets = [('MIDRIFF  (bare midriff restored)',(858,612,1002,762)),('LEFT UPPER ARM  (armlet)',(972,516,1094,644)),('FRACTURE  (crack replaced)',(402,500,576,892))]
y1 = y0 + th + 40
x = 24
for name,(a,b,cc_,dd) in dets:
    cw,ch = cc_-a, dd-b
    scale = min(330/cw, 330/ch)
    w2,h2 = int(cw*scale), int(ch*scale)
    d.text((x, y1), name, font=FB(17), fill=(200,170,110))
    c.paste(mp.crop((a,b,cc_,dd)).resize((w2,h2), Image.LANCZOS),(x, y1+22))
    c.paste(np_.crop((a,b,cc_,dd)).resize((w2,h2), Image.LANCZOS),(x+w2+10, y1+22))
    d.rectangle([x-1,y1+21,x+w2,y1+22+h2], outline=(80,90,105))
    d.rectangle([x+w2+9,y1+21,x+w2+10+w2,y1+22+h2], outline=(80,90,105))
    d.text((x, y1+28+h2), f'V005   |   V007', font=F(13), fill=(150,160,175))
    x += w2*2 + 60

lines = [
 "DEFECT A — synthetic crack. Now a warm dark-umber plaster fracture rising from the existing lower-right fissure into the panel beneath her palm: displaced edges, granular crumbled lips, no vector stroke, bevel, halo or glow, no doorway collapse.",
 "DEFECT B — bare midriff. Restored by aligned crop from V004 (V004 and V005 are the same frame: best landmark correlation 0.805 at scale 1.01, offset +6,+6), leaving the approved short indigo wrap hem and the belt line.",
 "DEFECT C — armlet. Multi-coil dull aged-bronze armlet restored on the LEFT upper arm only; rings follow the arm's cylinder and fade at the silhouette. LIMITATION: painted reconstruction — no approved armlet reference patch exists to transfer.",
 "DEFECT D — board chrome. Header V005 -> V007; obsolete 'crack hard to see' removed; READ is now true; footer no longer claims an approved blade board (WEAPON_ADANNA_PRIMARY_BLADE_V001 is REVIEW REQUIRED, CQ-9 open).",
 f"PIXEL PROOF: {st['total']:,} changed pixels, all inside the three masks \u2014 fracture {st['A fracture']:,} | midriff {st['B midriff']:,} | armlet {st['C armlet']:,} | outside masks {st['outside']}. Chrome changes are listed separately in the ledger.",
 "UNTOUCHED: face, expression, scar, braids with 3 bronze cuffs and 2 coral beads, right arm and hand on the seal, pose, silhouette, framing, SEALED_QUARTER_V003 architecture, bowl and pot, mist, palette, left-hip sheathed weapon, belt, skirt.",
 "STATUS: CANDIDATE ONLY — REVIEW REQUIRED. Not approved, not canon, not filed. V005 and V006 are preserved unchanged; V006 remains in REJECTED as evidence.",
]
yy = H - 22 - 17*len(lines)
for t in lines:
    d.text((24,yy), t, font=F(14), fill=(168,178,190)); yy += 17
c.save('submit/B2_COMPARE_VR-008_V005_vs_V007.jpg', quality=93)
print('board', c.size)
