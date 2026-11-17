from PIL import Image, ImageDraw, ImageFont
F =lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
B=Image.open('masters/ENV_HOME_SETTLEMENT_WASHING_PLACE_V002.jpg').convert('RGB').crop((60,152,1960,1244))
C=Image.open('final/CAND_VR-010_WASHING_PLACE_V004_2560x1440.png').convert('RGB').crop((60,152,1960,1244))
W=2200; tw=1050; th=int(tw*B.size[1]/B.size[0]); y0=78
c=Image.new('RGB',(W,1500),(13,17,23)); d=ImageDraw.Draw(c)
d.text((22,12),'WASHING PLACE  ·  ANCESTRAL REALM  ·  V002 base  ->  V004 CANDIDATE',font=FB(20),fill=(255,255,255))
d.text((22,44),'Answers REJECTION_REPORT_VR-010_WASHING_PLACE_V003. Masked removal of the exposed runoff channel only; every named V002 element is its own pixels.',font=F(15),fill=(170,180,192))
for i,(im,lab) in enumerate([(B,'BASE V002 (unchanged source)'),(C,'CANDIDATE V004 · REVIEW REQUIRED')]):
    x=22+i*(tw+56); c.paste(im.resize((tw,th),Image.LANCZOS),(x,y0))
    d.rectangle([x-1,y0-1,x+tw,y0+th],outline=(90,100,115)); d.text((x,y0+th+7),lab,font=FB(16),fill=(235,238,242))
y1=y0+th+84; x=22; maxh=0
for name,box in [('RUNOFF CHANNEL — before / after',(1080,560,1560,1092)),('SLAB, POTS, DIPPER, SPLASH EARTH',(60,560,760,1092))]:
    cw,ch=box[2]-box[0],box[3]-box[1]; s=min(430/cw,300/ch); w2,h2=int(cw*s),int(ch*s)
    d.text((x,y1-20),name,font=FB(14),fill=(200,170,110))
    c.paste(B.crop(box).resize((w2,h2),Image.LANCZOS),(x,y1))
    c.paste(C.crop(box).resize((w2,h2),Image.LANCZOS),(x+w2+10,y1))
    d.rectangle([x-1,y1-1,x+w2,y1+h2],outline=(80,90,105)); d.rectangle([x+w2+9,y1-1,x+w2+10+w2,y1+h2],outline=(80,90,105))
    d.text((x,y1+h2+4),'base  |  candidate',font=F(11),fill=(150,160,175))
    x+=w2*2+46; maxh=max(maxh,h2)
lines=[
 "DEFECT 1 — the stone washing slab is V002's own pixels in full scale: 0 changed pixels across the slab; it is neither shrunk, recessed nor darkened.",
 "DEFECTS 2 & 3 — there is no recess, niche, cavity or arched alcove anywhere at a wall base, and no object, vessel or stone sits inside or beside a drainage opening. Nothing was added: 0 changed pixels in the pots, dipper, leaf, chewing sticks and straw.",
 "DEFECT 4 — the water trough, the pot and dipper and the damp splash-earth immediately around the slab are untouched V002 pixels.",
 "DEFECT 5 — the palm-mat screens and their posts are unaltered: 0 changed pixels across every screen face; the only change at the right screen is the earth where the channel used to run.",
 "DEFECT 6 — the bright exposed runoff line is gone. The ground now reads as plain damp earth with no ditch, trench, groove or rut, and no water channel drawn anywhere.",
 "DEFECT 7 — chrome corrected: header now reads ENV_HOME_SETTLEMENT_WASHING_PLACE_V004, STATUS: REVIEW REQUIRED; the CORRECTED SINCE V002 and KNOWN ISSUES blocks are rewritten; the footer states plainly that any open wall-base outlet is a fictional design choice, not documented Igbo precedent (Basden records distant sources and catch-pits, not wall outlets).",
 "PIXEL PROOF vs V002: 113,314 px changed in total; 46,197 inside the repaint corridor; 0 outside corridor + metadata column. Every other pixel of the frame is V002's own.",
 "DECLARED DEVIATION — no wall-base pass-through is drawn. The only boundary in this camera is the woven screen, and the report forbids recesses, cavities and placed objects; the drain therefore reads as a flush damp grade that seeps under the screen's shadow, and the outlet itself is off-frame. If the CD wants a visible low gap at the screen base, that is a further authorised change.",
 "STATUS — CANDIDATE ONLY, REVIEW REQUIRED. Not approved, not canon, not filed. V002 and V001 are preserved untouched; the rejected V003 is left exactly as rejected."]
H=y1+maxh+34+15*len(lines)+18
c=c.crop((0,0,W,H)); d=ImageDraw.Draw(c); yy=H-14-15*len(lines)
for t in lines: d.text((22,yy),t,font=F(13),fill=(168,178,190)); yy+=15
c.save('submit/B2_COMPARE_VR-010_WASHING_PLACE_V002_vs_V004.jpg',quality=93); print(c.size)
