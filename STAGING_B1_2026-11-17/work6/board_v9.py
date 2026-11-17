from PIL import Image, ImageDraw, ImageFont
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
BASE=(13,17,23); WH=(240,242,246); TAN=(200,170,110); GR=(172,182,194)
V8=Image.open('submit/B2_CAND_ESTABLISHING_V008_2560x1440.png').convert('RGB')
V9=Image.open('final/CAND_ESTABLISHING_V009_2560x1440.png').convert('RGB')
W=2300
c=Image.new('RGB',(W,3200),BASE); d=ImageDraw.Draw(c)
def wrap(t,f,width):
    out=[];cur=""
    for w in t.split():
        s=(cur+" "+w).strip()
        if d.textlength(s,font=f)<=width: cur=s
        else: out.append(cur); cur=w
    out.append(cur); return out
d.text((22,14),"ESTABLISHING  \u00b7  V008  \u2192  V009 CANDIDATE",font=FB(22),fill=WH)
d.text((22,48),"Answers the CD ruling: Option A for Requirement D (foreground compound re-staged, Nneka\u2019s House and staked plot placed in warm daylight) plus the five Our Eyes defects. Everything outside the two named zones is untouched.",font=F(15),fill=GR)
tw=1090; th=int(tw*1440/2560); y0=86
for i,(im,lab) in enumerate([(V8,"V008 (superseded, preserved)"),(V9,"V009 CANDIDATE \u2014 REVIEW REQUIRED")]):
    x=22+i*(tw+46); c.paste(im.resize((tw,th),Image.LANCZOS),(x,y0))
    d.rectangle([x-1,y0-1,x+tw,y0+th],outline=(92,100,116)); d.text((x,y0+th+8),lab,font=FB(15),fill=WH)

# detail rows: projections in sheet coords
def pair(y,label,box,size):
    x=22
    d.text((22,y),label,font=FB(15),fill=TAN)
    for im,tag in ((V8,"V008"),(V9,"V009")):
        s=im.crop(box); s=s.resize(size,Image.LANCZOS)
        c.paste(s,(x,y+24)); d.rectangle([x-1,y+23,x+size[0],y+24+size[1]],outline=(80,90,105))
        d.text((x,y+24+size[1]+6),tag,font=FB(13),fill=GR); x+=size[0]+26
    return y+24+size[1]+34

y=y0+th+44
y=pair(y,"A  MOUND FOOT \u2014 hard seam \u2192 drifting dust",(620,500,1420,860),(1090,490))
y=pair(y,"B  LOWER-RIGHT MIST VEIL \u2014 warm-corrected",(1400,380,1901,606),(1090,490))
y=pair(y,"C  RIGHT COMPOUND \u2014 cramped longhouse \u2192 open yard with Nneka\u2019s House and staked plot",(1150,820,1901,1158),(1090,490))
# row D: 1:1 detail of the placed house
d.text((22,y),"D  NNEKA HOUSE + STAKED PLOT AT 1:1 (V009, 2x)",font=FB(15),fill=TAN)
hh=V9.crop((1290,920,1700,1165)).resize((1476,882),Image.LANCZOS)
c.paste(hh,(22,y+26)); d.rectangle([21,y+25,22+1476,y+26+882],outline=(80,90,105))
y=y+26+882+30

note=[
 "REQUIREMENT D \u2014 DELIVERED THIS ROUND. The right foreground longhouse is set back into a longer, lower range, opening a swept yard; Nneka\u2019s House stands in it in warm daylight with her staked, unbuilt plot laid out in front, marked by short timber stakes and string. Built with the approved NNEKAS_HOUSE_V004 plate supplied as the design reference, so roof pitch, veranda, door, window and props follow the approved design rather than being invented.",
 "DEFECT 1 \u2014 mound shadows and atmospheric perspective. A distance-graded warm haze (alpha 0.03 at the foot rising to 0.22 at the summit) plus a shadow lift now sits the mound in the same dusty aerial perspective as the plain, instead of the darker, contrastier mass V008 carried.",
 "DEFECT 2 \u2014 base seam. The mound foot no longer ends on a hard edge: a dust drift band, modulated by noise so it is not a clean gradient, carries the base into the plain.",
 "DEFECT 3 \u2014 lower-right mist artefact. The pale grey veil in front of the lower-right houses is colour-corrected to warm dust and its local contrast restored, so it reads as haze behind the roofs rather than a smudge in front of them.",
 "DEFECT 4 \u2014 stray roof-post stubs. Two independent scans (narrow skyline peaks; thin vertical columns rising above the local roof envelope) were run across the full width and returned no protruding stub in V008. The thin items on the roofs are ladder rails and batten ends \u2014 correct detail, kept. Nothing was invented to satisfy the note; if Our Eyes can point to the stub, it can be removed precisely.",
 "DEFECT 5 \u2014 the inaccurate \u2018hundreds\u2019 description is gone. No count is asserted anywhere on the sheet; the READ describes what is in frame.",
 "NOT DONE, STATED PLAINLY \u2014 the summit dwellings still read large for the distance. Genuinely reducing them means re-rendering the heap; two attempts this round (a full re-render and a crest-only edit) both altered the silhouette and were discarded rather than shipped. This is the one CD item not delivered.",
 "INTEGRITY \u2014 Hall of Posts 0 px changed; left compound 0; frame bottom 0. Mound 283,557 px (haze + drift), right compound 467,451 px (the ordered re-stage). Both zones are the ones the ruling names.",
 "STATUS \u2014 CANDIDATE ONLY, UNAPPROVED, for fresh Our Eyes inspection. V008 preserved untouched."]
yy=y+8
for t in note:
    for s in wrap(t,F(14),W-44):
        d.text((22,yy),s,font=F(14),fill=GR); yy+=19
    yy+=5
c=c.crop((0,0,W,yy+12)); c.save('submit/B2_COMPARE_ESTABLISHING_V008_vs_V009.jpg',quality=93); print(c.size)
