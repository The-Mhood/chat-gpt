from PIL import Image, ImageDraw, ImageFont
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
V1=Image.open('work5/COSTUME_BREAKDOWN_SHEET_V001.jpg').convert('RGB')
V2=Image.open('final/CAND_COSTUME_BREAKDOWN_V002_2560x1440.png').convert('RGB')
W=2200; tw=1060; th=int(tw*768/1376); y0=86
c=Image.new('RGB',(W,1500),(13,17,23)); d=ImageDraw.Draw(c)
d.text((22,14),'ADANNA — COSTUME BREAKDOWN  ·  V001 rejected  ->  V002 CANDIDATE',font=FB(21),fill=(255,255,255))
d.text((22,48),'Answers REJECTION_REPORT_COSTUME_BREAKDOWN_SHEET_V001. Rebuilt at 2560x1440 from approved master pixels only; no figure, face or costume element is drawn or generated.',font=F(15),fill=(176,184,196))
for i,(im,lab) in enumerate([(V1,'V001 — REJECTED (1376x768, preserved untouched)'),(V2,'V002 CANDIDATE — UNAPPROVED, PENDING CD')]):
    x=22+i*(tw+38); c.paste(im.resize((tw,th),Image.LANCZOS),(x,y0))
    d.rectangle([x-1,y0-1,x+tw,y0+th],outline=(92,100,116)); d.text((x,y0+th+8),lab,font=FB(15),fill=(236,238,242))
y1=y0+th+44; x=22; maxh=0
for name,(bx,by,bw,bh),src in [('V001 palette — garbled hex',(30,600,330,700),V1),
                               ('V002 palette — verbatim hex',(1790,1060,2520,1200),V2)]:
    sc=min(470/bw,210/bh); w2,h2=int(bw*sc),int(bh*sc)
    d.text((x,y1-20),name,font=FB(14),fill=(200,170,110))
    c.paste(src.crop((bx,by,bx+bw,by+bh)).resize((w2,h2),Image.LANCZOS),(x,y1))
    d.rectangle([x-1,y1-1,x+w2,y1+h2],outline=(80,90,105)); x+=w2+46; maxh=max(maxh,h2)
lines=[
 "CRITICAL 1 & 2 (beads/scar on the right side and on both temples) — there is no right-side panel in V002 at all: it is a hatched placeholder stating that no approved right-side plate exists. Nothing drawn there can carry a bead or a scar. In the front plate every bead, cuff and the scar sit on her LEFT side only, tagged 1 and 2 with a keyed legend at right.",
 "CRITICAL 3 (misdirected scabbard pointer) — the wrong pointer is gone. V002 carries no leader lines at all; six numbered tags sit on the feature they name, keyed in text, so a pointer cannot land on the wrong hip. The blade is described in words only: LEFT hip, right-hand cross-draw, construction CQ-9 OPEN.",
 "MAJOR 4 (invented skirt, detailed unapproved weapon) — neither is drawn. The lower body and weapon zone is a hatched UNRESOLVED panel with the line 'position only ... no hilt, no pommel and no skirt are drawn on this sheet'. Back torso is hatched UNRESOLVED as before.",
 "MODERATE 5 (corrupted hex, armlet drift, below-spec resolution) — all seven codes are typeset programmatically from source strings and read verbatim: #06080D #121215 #241916 #283338 #403D3E #44525C #677A85. The armlet plate is a native crop of the approved master showing its ~9 slender coils, not 5-6 thick bands. Sheet is 2560x1440.",
 "METHOD — every image on V002 is a native-resolution crop of CHAR_ADANNA_MASTER_REFERENCE_V001.jpg (MD5 901a5009...). Type is DejaVu Sans set in code. No generative pass, no hand paint, no new figure: this is the one asset in the batch where 'correction' could be done without inventing anything, because the defects were layout and labelling, not artwork.",
 "OPEN DEPENDENCY — V001's full front figure and right profile were themselves drawn plates that do not exist in the approved reference set. V002 therefore cannot reproduce them without generating new artwork, which is outside Assistant VA's authority. They are hatched and labelled, not faked.",
 "STATUS — CANDIDATE ONLY, UNAPPROVED, PENDING CD. Not canon, not filed. V001 preserved byte-identical in 16_REJECTED_DESIGNS."]
H=y1+maxh+34+15*len(lines)+18
c=c.crop((0,0,W,H)); d=ImageDraw.Draw(c); yy=H-14-15*len(lines)
for t in lines: d.text((22,yy),t,font=F(13),fill=(170,180,192)); yy+=15
c.save('submit/B2_COMPARE_COSTUME_BREAKDOWN_V001_vs_V002.jpg',quality=93); print(c.size)
