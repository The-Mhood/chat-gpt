from PIL import Image, ImageDraw, ImageFont
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
BASE=(13,17,23); WH=(240,242,246); TAN=(200,170,110); GR=(170,180,192)
V2=Image.open('masters/ENV_HOME_SETTLEMENT_WASHING_PLACE_V002.jpg').convert('RGB')
V5=Image.open('final/CAND_VR-010_WASHING_PLACE_V005_2560x1440.png').convert('RGB')
W=2200
c=Image.new('RGB',(W,1700),BASE); d=ImageDraw.Draw(c)
def wrap(txt,f,width):
    lines=[];cur=""
    for wd in txt.split():
        t=(cur+" "+wd).strip()
        if d.textlength(t,font=f)<=width: cur=t
        else: lines.append(cur); cur=wd
    lines.append(cur); return lines

d.text((22,14),"WASHING PLACE  \u00b7  HOME SETTLEMENT  \u00b7  V002 base  \u2192  V005 CANDIDATE",font=FB(21),fill=WH)
d.text((22,46),"Answers CD ruling on V004: chrome only. Artwork is V004 pixels, unchanged \u2014 no drain, no wall opening, no recess, no new architecture, camera unmoved.",font=F(15),fill=GR)

tw=1060; th=int(tw*1440/2560); y0=84
for i,(im,lab) in enumerate([(V2,"BASE V002 (source, untouched) \u2014 runoff channel present"),
                             (V5,"CANDIDATE V005 \u2014 flush grade, off-frame outlet")]):
    x=22+i*(tw+38); c.paste(im.resize((tw,th),Image.LANCZOS),(x,y0))
    d.rectangle([x-1,y0-1,x+tw,y0+th],outline=(92,100,116))
    d.text((x,y0+th+9),lab,font=FB(15),fill=WH)

P2=(60,152); y1=y0+th+44
crops=[(V2,"BASE V002 \u2014 runoff channel",(1150,560,1560,1030)),
       (V5,"V005 \u2014 same ground, flush",(1150,560,1560,1030)),
       (V5,"V005 \u2014 slab, pots, dipper, soap",(240,560,760,1030)),
       (V5,"V005 \u2014 woven screen, no wall opening",(1180,150,1720,560))]
x=22; hmax=0
for im,lab,(cx0,cy0,cx1,cy1) in crops:
    sub=im.crop((P2[0]+cx0,P2[1]+cy0,P2[0]+cx1,P2[1]+cy1))
    w2,h2=500,int(500*sub.size[1]/sub.size[0]); h2=min(h2,330)
    w2=int(h2*sub.size[0]/sub.size[1])
    c.paste(sub.resize((w2,h2),Image.LANCZOS),(x,y1+22))
    d.rectangle([x-1,y1+21,x+w2,y1+22+h2],outline=(80,90,105))
    d.text((x,y1+8),lab,font=FB(14),fill=TAN)
    x+=w2+22; hmax=max(hmax,h2)

lines=[
 "DEFECT 1 \u2014 orphaned V002 footer fragment. Removed. The footer band is repainted edge to edge (x 940\u20132556) before the new text is set, so no V002 tail survives at the right margin.",
 "DEFECT 2 \u2014 unsupported citation. Removed. The footer no longer invokes Basden or any external source; it states only that the settlement forms follow documented types and that every specific design here is invented.",
 "DEFECT 3 \u2014 READ and footer descriptions. Corrected to the image: a woven-screen corner (not frond), the wet standing stone on flush earth, the four props actually in shot, and no 'drain' \u2014 because no drain is visible.",
 "DEFECT 4 \u2014 board banner. 'ANCESTRAL REALM' \u2192 'HOME SETTLEMENT', matching ENV_HOME_SETTLEMENT_WASHING_PLACE_V005.",
 "DEFECT 5 \u2014 clipped captions. Every caption is measured and drawn inside the canvas: panel captions sit in their own band, crop captions above their frames, and the defect list wraps to the canvas width.",
 "UNCHANGED \u2014 the artwork is V004 pixels, byte for byte. No runoff, no ditch, no wall-base opening, no recess, no new architecture, no camera move. V002, the rejected V003 and V004 are all preserved.",
 "STATUS \u2014 CANDIDATE ONLY. Not approved, not canon. Returned for fresh Our Eyes inspection."]
yy=y1+22+hmax+34
for t in lines:
    for sub in wrap(t,F(13.5 if False else 14),W-44):
        d.text((22,yy),sub,font=F(14),fill=GR); yy+=20
    yy+=6
c=c.crop((0,0,W,yy+10))
c.save('submit/B2_COMPARE_VR-010_WASHING_PLACE_V002_vs_V005.jpg',quality=93)
print(c.size)
