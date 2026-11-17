from PIL import Image, ImageDraw, ImageFont
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
BASE=(13,17,23); WH=(240,242,246); TAN=(200,170,110); GR=(172,182,194)
V9=Image.open('final/CAND_ESTABLISHING_V009_2560x1440.png').convert('RGB')
V0=Image.open('final/CAND_ESTABLISHING_V010_2560x1440.png').convert('RGB')
W=2300
c=Image.new('RGB',(W,3200),BASE); d=ImageDraw.Draw(c)
def wrap(t,f,width):
    out=[];cur=""
    for w in t.split():
        s=(cur+" "+w).strip()
        if d.textlength(s,font=f)<=width: cur=s
        else: out.append(cur); cur=w
    out.append(cur); return out
d.text((22,14),"ESTABLISHING  \u00b7  V009  \u2192  V010 CANDIDATE",font=FB(22),fill=WH)
d.text((22,48),"Single authorised correction this round: the mound dwellings are re-scaled to the plain. The foreground compound, Hall of Posts, left compound and frame are untouched \u2014 0 px changed.",font=F(15),fill=GR)
tw=1090; th=int(tw*1440/2560); y0=86
for i,(im,lab) in enumerate([(V9,"V009 (superseded, preserved)"),(V0,"V010 CANDIDATE \u2014 REVIEW REQUIRED")]):
    x=22+i*(tw+46); c.paste(im.resize((tw,th),Image.LANCZOS),(x,y0))
    d.rectangle([x-1,y0-1,x+tw,y0+th],outline=(92,100,116)); d.text((x,y0+th+8),lab,font=FB(15),fill=WH)

def pair(y,label,box,size):
    x=22
    d.text((22,y),label,font=FB(15),fill=TAN)
    for im,tag in ((V9,"V009"),(V0,"V010")):
        s=im.crop(box); s=s.resize(size,Image.LANCZOS)
        c.paste(s,(x,y+24)); d.rectangle([x-1,y+23,x+size[0],y+24+size[1]],outline=(80,90,105))
        d.text((x,y+24+size[1]+6),tag,font=FB(13),fill=GR); x+=size[0]+26
    return y+24+size[1]+34

y=y0+th+44
y=pair(y,"A  HILL \u2014 dwellings ~30% smaller, ~2\u00d7 as many, same outline",(1020,250,1720,760),(1090,520))
y=pair(y,"B  HILL FOOT \u2014 scale reads against the plain village",(1060,700,1760,930),(1090,360))
y=pair(y,"C  RIGHT COMPOUND \u2014 unchanged this round (0 px)",(1150,840,1901,1180),(1090,494))
d.text((22,y),"D  HILL AT 1:1 \u2014 V010, 2\u00d7 (thatch grain and terrace wear carried across)",font=FB(15),fill=TAN)
hh=V0.crop((1250,430,1620,660)).resize((1480,920),Image.LANCZOS)
c.paste(hh,(22,y+26)); d.rectangle([21,y+25,22+1480,y+26+920],outline=(80,90,105))
y=y+26+920+30

note=[
 "WHAT CHANGED THIS ROUND \u2014 one thing. Every dwelling on the hill is rebuilt about 30 per cent smaller and roughly twice as numerous, so the hill reads at the scale of the plain village below it instead of 1.4\u20131.7\u00d7 above it. This is the item left open in V009 and named in \u00a76.2 of REJECTION_REPORT_ESTABLISHING_V008.",
 "HOW, STATED PLAINLY \u2014 the hill interior was re-rendered from the V009 hill as reference, registered back into the same crop, and composited inside a mask eroded 20 px and feathered 22 px from the V008 hill mask. The outline against the sky is therefore V009 pixels by construction, not by hopeful generation: the new houses sit inside the old silhouette.",
 "TEXTURE CARRIED ACROSS \u2014 the re-render was flatter than the V008 hill. The original\u2019s high-frequency detail (thatch straw, mud grain, terrace wear) was extracted and re-applied at 0.38 weight inside the replaced area, so the smaller dwellings keep the granular quality Our Eyes asked to preserve.",
 "INTEGRITY (panel, pre-grain, vs V009) \u2014 Hall of Posts 0 px; left compound 0; right compound 0; frame bottom 0. All structural change is inside the hill bbox: 101,913 px >12, 49,526 px >20, max delta 195. Nothing outside the hill was touched.",
 "WHAT DID NOT CHANGE \u2014 Requirement D stands as delivered in V009: the right compound re-staged, Nneka\u2019s House and her staked unbuilt plot in warm daylight. Chrome, palette, READ and the no-count wording carry forward; the V010 header and CLIENT REVIEW block are updated.",
 "RESEARCH GAP \u2014 restated on the sheet itself, not buried here: no exact-version Research Agent report exists for this file. The V008 report flags that gap and asks for an exact-version report on each new candidate; V009 and V010 both remain without one.",
 "STATUS \u2014 CANDIDATE ONLY, UNAPPROVED, for fresh Our Eyes inspection. V008 and V009 preserved untouched."]
yy=y+8
for t in note:
    for s in wrap(t,F(14),W-44):
        d.text((22,yy),s,font=F(14),fill=GR); yy+=19
    yy+=5
c=c.crop((0,0,W,yy+12)); c.save('submit/B2_COMPARE_ESTABLISHING_V009_vs_V010.jpg',quality=93); print(c.size)
