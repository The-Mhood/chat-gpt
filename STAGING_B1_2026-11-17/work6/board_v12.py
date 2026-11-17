from PIL import Image, ImageDraw, ImageFont
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
BASE=(13,17,23); WH=(240,242,246); TAN=(200,170,110); GR=(172,182,194)
W=2300
S0=Image.open('final/CAND_ESTABLISHING_V011_2560x1440.png').convert('RGB')
S1=Image.open('final/CAND_ESTABLISHING_V012_2560x1440.png').convert('RGB')
O=(60,152)  # panel origin in sheet coords
def pc(im,box):  # panel coords -> crop
    x0,y0,x1,y1=box; return im.crop((x0+O[0],y0+O[1],x1+O[0],y1+O[1]))
c=Image.new('RGB',(W,3400),BASE); d=ImageDraw.Draw(c)
def wrap(t,f,width):
    out=[];cur=""
    for w in t.split():
        s=(cur+" "+w).strip()
        if d.textlength(s,font=f)<=width: cur=s
        else: out.append(cur); cur=w
    out.append(cur); return out
d.text((22,14),"ESTABLISHING  \u00b7  V011  \u2192  V012 CANDIDATE",font=FB(22),fill=WH)
d.text((22,48),"Executing the eight-point brief in REJECTION_REPORT_ESTABLISHING_V009. Four zones corrected, summit scale carried, chrome rebuilt. Item 1 (house scale) not attempted \u2014 stated, not hidden.",font=F(15),fill=GR)
tw=1090; th=int(tw*1440/2560); y0=86
for i,(im,lab) in enumerate([(S0,"V011 (superseded, preserved)"),(S1,"V012 CANDIDATE \u2014 REVIEW REQUIRED")]):
    x=22+i*(tw+46); c.paste(im.resize((tw,th),Image.LANCZOS),(x,y0))
    d.rectangle([x-1,y0-1,x+tw,y0+th],outline=(92,100,116)); d.text((x,y0+th+8),lab,font=FB(15),fill=WH)
def pair(y,label,box,size):
    x=22; d.text((22,y),label,font=FB(15),fill=TAN)
    for im,tag in ((S0,"V011"),(S1,"V012")):
        s=pc(im,box).resize(size,Image.LANCZOS); c.paste(s,(x,y+24))
        d.rectangle([x-1,y+23,x+size[0],y+24+size[1]],outline=(80,90,105))
        d.text((x,y+24+size[1]+6),tag,font=FB(13),fill=GR); x+=size[0]+26
    return y+24+size[1]+34
y=y0+th+44
y=pair(y,"A  THE YARD \u2014 paling gone, V005 cloth line whole, halo and seam blended",(1080,780,1560,1010),(1090,460))
y=pair(y,"B  WALL BEHIND THE PALING \u2014 generative in-context patch, footprint only",(1390,795,1560,935),(1090,460))
y=pair(y,"C  LOWER-RIGHT WALL \u2014 pale blue cast corrected to warm earth",(1750,1000,1901,1169),(1090,460))
d.text((22,y),"D  CLOTH LINE AT 1:1 \u2014 V012, 2\u00d7 (V005 striped cloths restored at their own coordinates)",font=FB(15),fill=TAN)
hh=pc(S1,(1100,890,1290,1015)).resize((1520,1000),Image.LANCZOS)
c.paste(hh,(22,y+26)); d.rectangle([21,y+25,22+1520,y+26+1000],outline=(80,90,105))
y=y+26+1000+30
note=[
 "ITEM 2 \u2014 halo and seam. The pale rim around the house was pulled toward its local 13-px median only where it exceeded that median by more than 7 levels; the band where the re-staged yard met the base (x 1382\u20131426) is cross-blended so ground, shadow and grain run through it.",
 "ITEM 3 \u2014 paling out, cloth back. Three deterministic inpaints were tried and discarded (band-shift clone, two-band clone, horizontal mirror \u2014 the mirror produced a symmetrical twin of the pots and shelf). A generative patch on that region alone, composited through a feathered footprint mask, was the only method that left no rectangle. The cloth pieces come from untouched V005, placed at their own V005 coordinates on a mask derived from the cloth\u2019s own silhouette.",
 "ITEM 4 \u2014 blue bleed. The cast sat on the foreground wall face below the yard. Channel ratios matched to the same wall\u2019s warm left run (R \u00d71.05, G \u00d70.95, B \u00d70.95). Zero pixels change by more than 12 levels: a cast removal, not a repaint.",
 "ITEM 5 \u2014 summit. Carried from V010: dwellings ~30% smaller and ~2\u00d7 as numerous inside the preserved silhouette mask, original detail carried back at 0.38, V009 haze and lifted shadows untouched.",
 "ITEM 1 \u2014 NOT DELIVERED. Nneka\u2019s House still reads large. Shrinking a house already composited into a photographed yard leaves the vacated footprint and its cast shadow behind; it needs a re-render in context. Recorded on the sheet\u2019s KNOWN ISSUES in the same words rather than papered over.",
 "INTEGRITY \u2014 panel totals: 19,602 px >12, max 178. Outside the four corrected zones every region is grain-only: Hall of Posts max 6, left compound max 5, frame bottom max 8, hill max 5. Whole panel re-grained at N(0,1.0) so no zone sits in a cleaner noise regime than its neighbours.",
 "STATUS \u2014 CANDIDATE ONLY, UNAPPROVED. V009, V010 and V011 preserved untouched."]
yy=y+8
for t in note:
    for s in wrap(t,F(14),W-44):
        d.text((22,yy),s,font=F(14),fill=GR); yy+=19
    yy+=5
c=c.crop((0,0,W,yy+12)); c.save('submit/B2_COMPARE_ESTABLISHING_V011_vs_V012.jpg',quality=93); print(c.size)
