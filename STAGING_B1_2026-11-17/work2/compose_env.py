from PIL import Image, ImageDraw, ImageFont
import numpy as np

FB = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
BG = (9,13,24); TAN=(164,139,93); BODY=(226,225,217)

def spaced(d, xy, txt, font, fill, gap=1.2):
    x,y = xy
    for ch in txt:
        d.text((x,y), ch, font=font, fill=fill, anchor='ls')
        x += d.textlength(ch, font=font) + gap

def chrome(img, digit, hdr_old_last, newlines):
    WIDTH_LIMIT = 2545
    d = ImageDraw.Draw(img)
    d.rectangle([2481,33,2504,63], fill=BG)
    d.text((2485,57), digit, font=FB(22), fill=TAN, anchor='ls')
    for rect, blocks in newlines:
        d.rectangle(rect, fill=BG)
        y = rect[1] + 22
        first = True
        for kind, txt in blocks:
            if kind == 'L':
                if not first: y += 6
                spaced(d, (1995, y), txt, FB(15), TAN); y += 27
            if kind == 'L': first = False
            elif kind == 'B':
                w = d.textlength(txt, font=FR(16))
                assert 1995+w < 2548, (round(1995+w), txt)
                d.text((1995, y), txt, font=FR(16), fill=BODY, anchor='ls'); y += 23
                first = False
    return img

# ------------------------------------------------------------------ ESTABLISHING
M = Image.open('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg').convert('RGB')
P = Image.open('work2/EST_V007_panel.png').convert('RGB')
out = M.copy(); out.paste(P, (60,152))
chrome(out, '7', '5', [
 ((1990,312,2545,352), [('L2','REVISE. Seventh version. Mound rebuilt as an irregular heap.')]),
 ((1986,676,2545,1058), [
   ('L','CHANGED SINCE V005'),
   ('B','The cone is gone: the mound is now an irregular,'),
   ('B','asymmetrical heap of separate single-storey houses'),
   ('B','with uneven shoulders, jutting clusters, staggered'),
   ('B','roof ridges, ladders and worn stair runs.'),
   ('B','Hall of Posts, aerial river, overhead settlement and'),
   ('B','the foreground compound are V005 pixels, unchanged.'),
   ('L','KNOWN ISSUES'),
   ('B','Nneka\u2019s House: the foreground compound is'),
   ('B','V005\u2019s own untouched pixels (0 changed px there),'),
   ('B','so the house is unaltered. A separate warm-daylight'),
   ('B','pass was made and NOT used: it would have lit the'),
   ('B','distance wrongly. Rebuilt houses read flatter than'),
   ('B','V005\u2019s own surfaces and do not yet match'),
   ('B','WALL_OF_HOUSES material weight. The mask edge on'),
   ('B','both flanks sits in haze: soft, not invisible.'),
   ('B','The whole mound is a masked repaint, not V005.'),
 ]),
])
out.save('final/CAND_ESTABLISHING_V007_2560x1440.png'); print('EST saved')

# ------------------------------------------------------------------ WALL OF HOUSES
M2 = Image.open('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_WALL_OF_HOUSES_V003.jpg').convert('RGB')
P2 = Image.open('work2/WALL_V005_panel.png').convert('RGB')
out2 = M2.copy(); out2.paste(P2, (60,152))
chrome(out2, '5', '3', [
 ((1995,312,2545,352), [('L2','REVISE. Fifth version. Single-storey throughout.')]),
 ((1986,778,2545,1090), [
   ('L','CHANGED SINCE V003'),
   ('B','Every dwelling is now single-storey: one roof and'),
   ('B','one ground-level door each. A distinct older, more'),
   ('B','eroded first settlement stands at the foot.'),
   ('B','Doorways read as lit, dark and plain-sealed; no red'),
   ('B','bars, no painted glyphs or symbols anywhere.'),
   ('L','KNOWN ISSUES'),
   ('B','Ladder routes are fewer than V003 and read less'),
   ('B','clearly as one continuous climb. The mound sits'),
   ('B','slightly lower and broader, and the upper right'),
   ('B','slope is hazier and emptier than V003\u2019s. The'),
   ('B','built mound is a masked architectural repaint, so'),
   ('B','its surfaces differ from V003\u2019s grain outside.'),
 ]),
])
out2.save('final/CAND_WALL_OF_HOUSES_V005_2560x1440.png'); print('WALL saved')
