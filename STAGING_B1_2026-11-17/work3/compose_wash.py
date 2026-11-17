from PIL import Image, ImageDraw, ImageFont
BG=(9,13,24); TAN=(164,139,93); BODY=(204,202,195); GREY=(153,157,169)
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)

M=Image.open('masters/ENV_HOME_SETTLEMENT_WASHING_PLACE_V002.jpg').convert('RGB')
P=Image.open('work3/WASH_V004_panel.png').convert('RGB')
out=M.copy(); out.paste(P,(60,152)); d=ImageDraw.Draw(out)

def raw(x,y,t,f,fill,anchor='ls'):
    d.text((x,y),t,font=f,fill=fill,anchor=anchor)
def right(xr,y,t,f,fill):
    w=d.textlength(t,font=f); assert xr-w>1880,(t,round(xr-w)); d.text((xr,y),t,font=f,fill=fill,anchor='rs')

# header asset name
d.rectangle([1884,32,2512,62], fill=BG)
right(2497,55,'ENV_HOME_SETTLEMENT_WASHING_PLACE_V004',FB(19),TAN)

# CORRECTED SINCE V002 label + body
d.rectangle([1994,426,2546,455], fill=BG)
raw(2001,447,'CORRECTED SINCE V002',FB(19),TAN)
d.rectangle([1994,456,2546,538], fill=BG)
corr=["The bright open-ground runoff channel that crossed",
      "the yard is gone. The earth now grades gently, flush",
      "and unbroken: no ditch, no trench, no rut, no water."]
y=477
for t in corr:
    w=d.textlength(t,font=F(19)); assert 2001+w<2545,(round(2001+w),t); raw(2001,y,t,F(19),BODY); y+=26

# KNOWN ISSUES body (label kept)
d.rectangle([1994,566,2546,650], fill=BG)
ks=["Outlet off-frame: the only boundary in shot is the",
    "woven screen, so no wall-base pass-through is drawn",
    "and no recess invented. Screen, slab, pots and",
    "utensils are V002 pixels; the wet ground is repainted."]
y=590
for t in ks:
    w=d.textlength(t,font=F(19)); assert 2001+w<2545,(round(2001+w),t); raw(2001,y,t,F(19),BODY); y+=26

# footer paragraph (auto-wrapped to the measured column width)
d.rectangle([978,1334,1976,1436], fill=BG)
ftxt=("Igbo-inspired fictional settlement. Compound layout, mud walls, steep thatch and carved doors follow documented forms; "
      "every specific design here is invented. A plain open wall-base drain outlet is a fictional design choice, not documented "
      "Igbo precedent \u2014 Basden records distant water sources and surface catch-pits, not wall outlets. Not approved. "
      "Supersedes V002, which is kept.")
fF=F(13); lines=[]; cur=""
for word in ftxt.split(" "):
    t=(cur+" "+word).strip()
    if d.textlength(t,font=fF) <= 945: cur=t
    else: lines.append(cur); cur=word
lines.append(cur)
assert len(lines)<=4, len(lines)
y=1356
for t in lines:
    assert 984+d.textlength(t,font=fF) < 1945, (round(984+d.textlength(t,font=fF)), t)
    raw(984,y,t,fF,GREY); y+=24
print('footer lines', len(lines))

out.save('final/CAND_VR-010_WASHING_PLACE_V004_2560x1440.png')
print('saved', out.size)
