from PIL import Image, ImageDraw, ImageFont
import json
F  = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
st = json.load(open('work2/v008_diffstats.json'))

W,H = 2400, 1370
c = Image.new('RGB',(W,H),(13,17,23)); d = ImageDraw.Draw(c)
d.text((24,12), "VR-008  COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL   V005 base  ->  V008 CANDIDATE", font=FB(25), fill=(255,255,255))
d.text((24,46), "Answer to REJECTION_REPORT_VR-008_SEALED_QUARTER_V006 (updated 18,150 B version incl. the §8 provenance addendum). Hand retouch only, no generative pass.", font=F(16), fill=(170,180,192))

M  = Image.open('masters/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005.jpg').convert('RGB')
N8 = Image.open('final/CAND_VR-008_V008_2560x1440.png').convert('RGB')
N7 = Image.open('final/CAND_VR-008_V007_2560x1440.png').convert('RGB')
V4 = Image.open('panels/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V004_PANEL.jpg').convert('RGB')
CH = Image.open('refs/CHAR_ADANNA_MASTER_REFERENCE_V001.jpg').convert('RGB')
BOX=(60,152,1961,1321)
mp=M.crop(BOX); p8=N8.crop(BOX); p7=N7.crop(BOX)

tw=1100; th=int(tw*mp.size[1]/mp.size[0]); y0=64
for i,(im,lab) in enumerate([(mp,'BASE — V005 master (handover branch, unchanged)'),(p8,'CANDIDATE — V008 · REVIEW REQUIRED')]):
    x=24+i*(tw+52)
    c.paste(im.resize((tw,th), Image.LANCZOS),(x,y0))
    d.rectangle([x-1,y0-1,x+tw,y0+th], outline=(90,100,115))
    d.text((x,y0+th+8), lab, font=FB(17), fill=(235,238,242))

def panel(im, box, x, y, maxw, maxh, label, col=(200,170,110)):
    cw,ch=box[2]-box[0], box[3]-box[1]
    s=min(maxw/cw, maxh/ch); w2,h2=int(cw*s),int(ch*s)
    c.paste(im.crop(box).resize((w2,h2), Image.LANCZOS),(x,y))
    d.rectangle([x-1,y-1,x+w2,y+h2], outline=(80,90,105))
    d.text((x,y-20), label, font=FB(15), fill=col)
    return w2,h2

y1 = 856
def head(x,y,t): d.text((x,y), t, font=FB(16), fill=(200,170,110))

head(24, 800, "DEFECT B \u2014 bare midriff: V004 reference  |  V008 candidate")
panel(V4,(852,614,1000,764), 24, y1, 300, 300, 'V004 reference (canonical copy)')
panel(p8,(852,614,1000,764), 340, y1, 300, 300, 'V008 \u2014 restored')

head(700, 800, "DEFECT C \u2014 armlet: approved master  |  V007 painted  |  V008 transferred")
panel(CH,(580,1010,800,1140), 700, y1+70, 300, 210, 'CHAR master portrait')
panel(p7,(985,520,1090,640), 1010, y1, 250, 300, 'V007 \u2014 painted')
panel(p8,(985,520,1090,640), 1272, y1, 250, 300, 'V008 \u2014 transferred')

head(1560, 800, "DEFECT A \u2014 fracture: V005  |  V008")
panel(mp,(405,495,575,890), 1560, y1, 190, 340, 'V005')
panel(p8,(405,495,575,890), 1760, y1, 190, 340, 'V008')

lines = [
 f"DEFECT A — the V006 crack was discarded and redrawn as a plaster fracture rising from the authentic lower-right fissure beneath her palm: warm umber crevice, granular crumbled lips, displaced edge, no vector stroke, bevel, blurred halo, glow or doorway collapse.",
 f"DEFECT B — bare midriff restored by ALIGNED CROP from V004, not painted. V004 and V005 are the same frame (landmark correlation 0.805 at scale 1.01, offset +6,+6); the 1 % resample is the only source of softness in the patch.",
 f"DEFECT C — the armlet is now a TRANSFER, not a painting: the band is cut from CHAR_ADANNA_MASTER_REFERENCE_V001's own portrait (x 580–800, y 1010–1140), levelled 7.6°, graded to this scene's overcast light and scaled to this arm's width. V007's painted five-coil band is superseded.",
 f"DEFECT D — chrome: header V005 -> V008; obsolete 'crack hard to see' removed; READ left as-is because it is now true; footer no longer claims an approved blade board (WEAPON_ADANNA_PRIMARY_BLADE_V001 is REVIEW REQUIRED, CQ-9 open).",
 f"PIXEL PROOF — V008 vs V005: {st['V008']['total']:,} changed px, all inside the three masks (fracture {st['V008']['A fracture']:,} · midriff {st['V008']['B midriff']:,} · armlet {st['V008']['C armlet']:,}); 0 outside. V007 -> V008: {st['v7_to_v8']['total']:,} px, all inside the armlet mask.",
 "UNTOUCHED — face, expression, scar, braids with 3 bronze cuffs and 2 coral beads, right hand flat on the seal, pose, silhouette, framing, SEALED_QUARTER_V003 architecture, bowl and pot, mist and palette, left-hip sheathed weapon, belt, skirt: 0 px changed in every one of those regions.",
 "STATUS — CANDIDATE ONLY, REVIEW REQUIRED. Not approved, not canon, not filed, not a master. V005, V006 and V007 are all preserved; V006 remains in 16_REJECTED_DESIGNS as evidence.",
]
yy = H-8-16*len(lines)
for t in lines:
    d.text((24,yy), t, font=F(13), fill=(168,178,190)); yy += 16
c.save('submit/B2_COMPARE_VR-008_V005_to_V008_with_references.jpg', quality=93)
print('board', c.size)
