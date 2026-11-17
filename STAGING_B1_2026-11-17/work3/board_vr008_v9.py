from PIL import Image, ImageDraw, ImageFont
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
BASE=(13,17,23); WH=(240,242,246); TAN=(200,170,110); GR=(172,182,194)
V8=Image.open('submit/B2_CAND_VR-008_SEALED_QUARTER_V008_2560x1440.png').convert('RGB')
V9=Image.open('final/CAND_VR-008_SEALED_QUARTER_V009_2560x1440.png').convert('RGB')
W=2100
c=Image.new("RGB",(W,3600),BASE); d=ImageDraw.Draw(c)
def wrap(t,f,width):
    out=[];cur=""
    for w in t.split():
        s=(cur+" "+w).strip()
        if d.textlength(s,font=f)<=width: cur=s
        else: out.append(cur); cur=w
    out.append(cur); return out
d.text((22,14),"VR-008 SEALED QUARTER  \u00b7  V008 \u2192 V009 CANDIDATE",font=FB(22),fill=WH)
d.text((22,48),"Answers REJECTION_REPORT_VR-008_SEALED_QUARTER_V008: the unapproved metal pauldron is removed and the bare shoulder with the plain leather strap restored per OAD-02; stale V004 chrome replaced. Environment untouched.",font=F(15),fill=GR)
tw=1010; th=int(tw*1440/2560); y0=86
for i,(im,lab) in enumerate([(V8,"V008 (rejected, preserved)"),(V9,"V009 CANDIDATE \u2014 REVIEW REQUIRED")]):
    x=22+i*(tw+30); c.paste(im.resize((tw,th),Image.LANCZOS),(x,y0))
    d.rectangle([x-1,y0-1,x+tw,y0+th],outline=(92,100,116)); d.text((x,y0+th+8),lab,font=FB(15),fill=WH)
def pair(y,label,box,size):
    x=22; d.text((22,y),label,font=FB(15),fill=TAN)
    for im,tag in ((V8,"V008"),(V9,"V009")):
        s=im.crop(box).resize(size,Image.LANCZOS); c.paste(s,(x,y+24))
        d.rectangle([x-1,y+23,x+size[0],y+24+size[1]],outline=(80,90,105))
        d.text((x,y+24+size[1]+6),tag,font=FB(13),fill=GR); x+=size[0]+26
    return y+24+size[1]+34
y=y0+th+44
y=pair(y,"A  LEFT SHOULDER \u2014 bronze pauldron \u2192 bare shoulder, plain leather strap",(980,540,1200,760),(1000,1000))
y=pair(y,"B  COILED BRONZE ARMLET \u2014 preserved in place (2\u00d7)",(1010,690,1150,775),(1000,630))
d.text((22,y),"C  SHEET CHROME \u2014 stale V004 comparison language replaced",font=FB(15),fill=TAN)
a=V8.crop((1932,180,2100,560)); b=V9.crop((1932,180,2100,560))
c.paste(a,(22,y+24)); c.paste(b,(22+168+20,y+24))
d.rectangle([21,y+23,22+168,y+24+380],outline=(80,90,105)); d.rectangle([22+168+19,y+23,22+168+20+168,y+24+380],outline=(80,90,105))
d.text((22,y+24+386),"V008",font=FB(13),fill=GR); d.text((22+188,y+24+386),"V009",font=FB(13),fill=GR)
y=y+24+380+34
note=[
 "ITEM 1 \u2014 pauldron removed. The metal shoulder cap occupied (1012,562)\u2013(1152,698). It was removed with a generative retouch of that shoulder region, composited back through a rounded-feather footprint mask, colour-matched to the surrounding skin (median shift \u22127,\u221210,\u22124). The shoulder is now bare brown skin and the thin dark-brown leather strap crosses it, exactly as CHAR_ADANNA_MASTER_REFERENCE_V001 (OAD-02) specifies: bare shoulders, plain leather strap, no metal.",
 "ITEM 3 \u2014 gains preserved. Warm skin tone, braided silhouette with its brass rings, bare right shoulder, and the coiled bronze armlet all survive. The armlet sits inside the blend feather and 191 px of its top edge move by up to 28 levels; that is the mask edge, not a rebuild. Everything else in the figure is untouched.",
 "ITEM 2 \u2014 chrome. Header \u2192 COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V009. ASSESSMENT no longer claims a V004 comparison. KNOWN ISSUES drops \u2018tighter than V004\u2019 and states what is true: framing carried from V008, RQ-10-1 open, U-11 open, the hand-on-seal gesture FICTIONAL. SOURCES now names CHAR_ADANNA_MASTER_REFERENCE_V001 (OAD-02) and WEAPON_ADANNA_PRIMARY_BLADE_V001. A PROVENANCE block records the lineage and that V006\u2013V008 are preserved in 16_REJECTED_DESIGNS.",
 "AUDIT \u2014 art environment left: 0 px changed. Art environment right: 0 px changed. Footer band: 0 px changed. Figure: 12,834 px >12, all inside the pauldron footprint. Chrome column: text replaced. Sheet total 148,467 px >12.",
 "STATUS \u2014 CANDIDATE ONLY, UNAPPROVED. V006, V007 and V008 preserved untouched in 16_REJECTED_DESIGNS. Nothing promoted."]
yy=y+8
for t in note:
    for s in wrap(t,F(14),W-44):
        d.text((22,yy),s,font=F(14),fill=GR); yy+=19
    yy+=5
c=c.crop((0,0,W,yy+12)); c.save('submit/B2_COMPARE_VR-008_V008_vs_V009.jpg',quality=93); print(c.size)
