from PIL import Image, ImageDraw, ImageFont
import json
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
st=json.load(open('work4/est8_stats.json'))
B=Image.open('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg').convert('RGB').crop((60,152,1961,1321))
C=Image.open('final/CAND_ESTABLISHING_V008_2560x1440.png').convert('RGB').crop((60,152,1961,1321))
W=2200; tw=1050; th=int(tw*B.size[1]/B.size[0]); y0=78
c=Image.new('RGB',(W,1500),(13,17,23)); d=ImageDraw.Draw(c)
d.text((22,12),'ESTABLISHING VIEW  ·  ANCESTRAL REALM  ·  V005 base  ->  V008 CANDIDATE',font=FB(20),fill=(255,255,255))
d.text((22,44),'Answers REJECTION_REPORT_ESTABLISHING_V007. Masked mound rebuild at village scale; chrome repaired. Everything outside the mask is V005.',font=F(15),fill=(170,180,192))
for i,(im,lab) in enumerate([(B,'BASE V005 (unchanged source)'),(C,'CANDIDATE V008 · REVIEW REQUIRED')]):
    x=22+i*(tw+56); c.paste(im.resize((tw,th),Image.LANCZOS),(x,y0))
    d.rectangle([x-1,y0-1,x+tw,y0+th],outline=(90,100,115)); d.text((x,y0+th+7),lab,font=FB(16),fill=(235,238,242))
y1=y0+th+84; x=22; maxh=0
for name,box in [('MOUND — oversized huts replaced by village-scale homes',(1080,230,1700,700)),('AERIAL RIVER AT THE MOUND FLANK',(880,240,1300,520))]:
    cw,ch=box[2]-box[0],box[3]-box[1]; s=min(430/cw,300/ch); w2,h2=int(cw*s),int(ch*s)
    d.text((x,y1-20),name,font=FB(14),fill=(200,170,110))
    c.paste(B.crop(box).resize((w2,h2),Image.LANCZOS),(x,y1))
    c.paste(C.crop(box).resize((w2,h2),Image.LANCZOS),(x+w2+10,y1))
    d.rectangle([x-1,y1-1,x+w2,y1+h2],outline=(80,90,105)); d.rectangle([x+w2+9,y1-1,x+w2+10+w2,y1+h2],outline=(80,90,105))
    d.text((x,y1+h2+4),'base  |  candidate',font=F(11),fill=(150,160,175)); x+=w2*2+46; maxh=max(maxh,h2)
lines=[
 "DEFECT 2a (scale) — the mound is rebuilt as a dense accumulation of many hundreds of small single-storey homes matching the scale of the village directly below its foot; the 2.5x-3x oversized diorama huts of V007 are gone.",
 "DEFECT 2b (surface) — granular mud grain is restored by a detail pass taken from the render itself; walls and thatch now carry texture rather than the flat painterly drop V007 showed. It is closer to V005's material weight, not identical to it.",
 "DEFECT 2c (artifacts) — no pole, strut or mast crosses the aerial river; the river thins into mist at the mound's left flank with a crisp edge. No stacked two-tier porch block.",
 "DEFECT 3 (chrome) — CLIENT REVIEW is populated (it was blank on V007 because my re-set drew an unhandled block type and wrote nothing). Header reads V008; CHANGED SINCE V005 and KNOWN ISSUES rewritten; REVIEW REQUIRED and EXPLORATORY - NOT APPROVED CANON retained.",
 f"PIXEL PROOF vs V005 — total changed {st['total']:,} px; {st['in_mask']:,} inside the mask; {st['outside']} outside mask + metadata column. Hall of Posts: 0 changed. Foreground compound: 0 changed. Frame edges: 0 changed.",
 "REQUIREMENT D (Nneka's House) — NOT DELIVERED, and I am not claiming it. Three integration attempts are recorded and all fail visibly: a generative pass with the approved house as design reference returned clean CGI that clashes with the scene; a second pass with only the scene as reference returned a better-styled but still CGI courtyard; and a pixel-composited insert of the approved house reads as a flat pasted patch whose ground plane fights the courtyard's viewing angle.",
 "SPECIFICATION REQUIRED — D needs a decision I must not invent: either an approved integration method (perspective-matched plate or a re-staged compound), or authorisation to place Nneka's House in a dedicated mid-ground plate instead of this dense yard. The approved reference itself (1JIoAiQ20goibDA-ujYr95iyihBTLKZWj) is intact and unused; nothing about it was altered.",
 "STATUS — CANDIDATE ONLY, REVIEW REQUIRED. Not approved, not canon, not filed. V005-V007 all preserved untouched; the rejected V007 stays exactly as rejected."]
H=y1+maxh+34+15*len(lines)+18
c=c.crop((0,0,W,H)); d=ImageDraw.Draw(c); yy=H-14-15*len(lines)
for t in lines: d.text((22,yy),t,font=F(13),fill=(168,178,190)); yy+=15
c.save('submit/B2_COMPARE_ESTABLISHING_V005_vs_V008.jpg',quality=93); print(c.size)
