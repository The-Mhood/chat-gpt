from PIL import Image, ImageDraw, ImageFont
import json
F  = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
st = json.load(open('work2/env_diffstats.json'))

def board(base, cand, outpath, title, sub, dets, lines, stats):
    B=Image.open(base).convert('RGB'); C=Image.open(cand).convert('RGB')
    BP=B.crop((60,152,1961,1321)); CP=C.crop((60,152,1961,1321))
    W,H=2200,1400
    c=Image.new('RGB',(W,H),(13,17,23)); d=ImageDraw.Draw(c)
    d.text((22,10), title, font=FB(20), fill=(255,255,255))
    d.text((22,42), sub, font=F(15), fill=(170,180,192))
    tw=1050; th=int(tw*BP.size[1]/BP.size[0]); y0=68
    for i,(im,lab) in enumerate([(BP,'BASE (unchanged source)'),(CP,'CANDIDATE · REVIEW REQUIRED')]):
        x=22+i*(tw+56)
        c.paste(im.resize((tw,th), Image.LANCZOS),(x,y0))
        d.rectangle([x-1,y0-1,x+tw,y0+th], outline=(90,100,115))
        d.text((x,y0+th+7), lab, font=FB(16), fill=(235,238,242))
    y1=y0+th+76
    maxh=0
    x=22
    for name,box in dets:
        cw,ch=box[2]-box[0], box[3]-box[1]
        s=min(430/cw, 330/ch); w2,h2=int(cw*s),int(ch*s)
        d.text((x,y1-20), name, font=FB(14), fill=(200,170,110))
        c.paste(BP.crop(box).resize((w2,h2), Image.LANCZOS),(x,y1))
        c.paste(CP.crop(box).resize((w2,h2), Image.LANCZOS),(x+w2+10,y1))
        d.rectangle([x-1,y1-1,x+w2,y1+h2], outline=(80,90,105))
        d.rectangle([x+w2+9,y1-1,x+w2+10+w2,y1+h2], outline=(80,90,105))
        d.text((x, y1+h2+4), 'base  |  candidate', font=F(11), fill=(150,160,175))
        x += w2*2 + 46
        maxh = max(maxh, h2)
    H = y1 + maxh + 34 + 15*len(lines) + 18
    c = c.crop((0,0,W,H)); d = ImageDraw.Draw(c)
    yy = H - 14 - 15*len(lines)
    for t in lines:
        d.text((22,yy), t, font=F(13), fill=(168,178,190)); yy += 15
    c.save(outpath, quality=93); print(outpath, c.size, stats)

e=st['EST']; w=st['WALL']
board('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg',
      'final/CAND_ESTABLISHING_V007_2560x1440.png',
      'submit/B2_COMPARE_ESTABLISHING_V005_vs_V007.jpg',
      "ESTABLISHING VIEW  ·  ANCESTRAL REALM  ·  V005 base  ->  V007 CANDIDATE",
      "Answers REJECTION_REPORT_ESTABLISHING_V006. Masked architectural repaint of the settlement mound only; everything outside the mask is V005's own pixels.",
      [('SETTLEMENT MOUND — cone replaced by an irregular heap',(1080,120,1900,760)),
       ('MOUND FOOT / FOREGROUND JUNCTION',(1080,540,1700,790))],
      [f"DEFECT A — the regular symmetrical cone is gone. The mound is now an irregular, asymmetrical accumulation of separate single-storey mud-and-thatch houses: uneven shoulders, jutting clusters, staggered ridges, ladders and worn stair runs. No stepped pyramid, no ziggurat, no fortress wall, no symmetry.",
       f"DEFECT B — the 'wall smear' was a V006-only artefact; building from V005 means it never existed here. Zero hand-retouch smears, zero figures anywhere (OAD-40).",
       f"DEFECT C — the V006 board and register claims are not repeated: this board and the register describe only what is in the exported PNG. Verified against the file bytes, not against intent.",
       f"DEFECT E — chrome: header V005 -> V007; CLIENT REVIEW, CHANGED SINCE V005 and KNOWN ISSUES rewritten; STATUS: REVIEW REQUIRED, EXPLORATORY — NOT APPROVED CANON and the consultant-review disclaimer retained.",
       f"PIXEL PROOF — total changed vs V005: {e['total']:,} px; {e['inside_mask']:,} inside the mask; {e['outside']} outside mask+chrome. Hall of Posts, aerial river, inverted overhead settlement, foreground compound: V005 pixels untouched.",
       "OPEN — Nneka's warm-daylight house is NOT yet placed (declared in KNOWN ISSUES). The rebuilt surfaces read slightly flatter than V005's and do not yet match WALL_OF_HOUSES material weight. The mask edge sits in haze: soft, not invisible.",
       "STATUS — CANDIDATE ONLY, REVIEW REQUIRED. Not approved, not canon, not filed, not a master. V005 and the rejected V006 are preserved untouched."],
      e)
board('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_WALL_OF_HOUSES_V003.jpg',
      'final/CAND_WALL_OF_HOUSES_V005_2560x1440.png',
      'submit/B2_COMPARE_WALL_OF_HOUSES_V003_vs_V005.jpg',
      "WALL OF HOUSES  ·  ANCESTRAL REALM  ·  V003 base  ->  V005 CANDIDATE",
      "Answers REJECTION_REPORT_WALL_OF_HOUSES_V004. Masked architectural repaint of the built mound; sky, mist and frame edges are V003's own pixels.",
      [('FIRST SETTLEMENT AT THE FOOT',(560,690,1500,1070)),
       ('DOORWAY STATES — lit / dark / plain-sealed',(980,760,1500,1070))],
      [f"DEFECT A — every dwelling in the exported image is single-storey: one thatch roof and one ground-level doorway each. The two-storey blocks flagged on V003 (right of centre, centre, upper slope) are gone.",
       f"DEFECT C — a distinct older first settlement now stands at the foot: separate, lower-slung, eroded dwellings with worn paths and gaps between them, visibly more decayed than the houses above.",
       f"DEFECT D — the lit / dark / sealed triad reads: warm hearth-lit doorways, several dark openings, and plain-sealed doors in warm-pale mud plaster with natural dry-mud crazing and wedged timber. No red bars, no red glyphs, no painted symbols, no shrine elements: 0 bright-red pixels detected in the panel.",
       f"DEFECT F — chrome: header V003 -> V005; CLIENT REVIEW, CHANGED SINCE V003 and KNOWN ISSUES rewritten; STATUS: REVIEW REQUIRED and EXPLORATORY — NOT APPROVED CANON retained.",
       f"PIXEL PROOF — total changed vs V003: {w['total']:,} px; {w['inside_mask']:,} inside the mask; {w['outside']} outside mask+chrome. The V004-only defects (red bars, glyphs, the obstructing left hut, the inverted chronology) do not exist here because this is built from V003, not from V004.",
       "OPEN — ladder routes are fewer than V003 and read less clearly as one continuous climb; the mound sits slightly lower and broader; the whole mound is a masked repaint so its surfaces differ from V003's photoreal grain.",
       "STATUS — CANDIDATE ONLY, REVIEW REQUIRED. Not approved, not canon, not filed, not a master. V003 and the rejected V004 are preserved untouched."],
      w)
