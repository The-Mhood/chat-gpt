from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np
BG=(9,13,24); TAN=(164,139,93); BODY=(226,225,217)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)

# ---- final grain unification
a=np.array(Image.open('work6/est_v9_p5.png').convert('RGB'),np.float32)
rng=np.random.default_rng(11)
g=rng.normal(0,1.15,(a.shape[0],a.shape[1],1)).astype(np.float32)
a=np.clip(a+g,0,255)
P=Image.fromarray(a.astype(np.uint8)); P.save('work6/EST_V009_panel.png')

M=Image.open('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg').convert('RGB')
out=M.copy(); out.paste(P,(60,152)); d=ImageDraw.Draw(out)

def spaced(xy,txt,font,fill,gap=1.2):
    x,y=xy
    for ch in txt:
        d.text((x,y),ch,font=font,fill=fill,anchor='ls'); x+=d.textlength(ch,font=font)+gap

d.rectangle([2478,33,2508,66],fill=BG); d.text((2485,58),'9',font=FB(22),fill=TAN,anchor='ls')
d.rectangle([1520,18,2560,140],fill=BG)
name='ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V009'
w=d.textlength(name,font=FB(19)); assert 2497-w>1775; d.text((2497,56),name,font=FB(19),fill=TAN,anchor='rs')
d.text((2497,88),'STATUS: REVIEW REQUIRED',font=FR(18),fill=(238,238,232),anchor='rs')
d.text((2497,116),'EXPLORATORY \u2014 NOT APPROVED CANON \u00b7 CHAPTER 8',font=FR(16),fill=(150,158,172),anchor='rs')

def block(rect,items):
    d.rectangle(rect,fill=BG); y=rect[1]+24; first=True
    for kind,txt in items:
        if kind=='L':
            if not first: y+=8
            spaced((1995,y),txt,FB(15),TAN); y+=28; first=False
        else:
            wd=d.textlength(txt,font=FR(16)); assert 1995+wd<2548,(round(1995+wd),txt)
            d.text((1995,y),txt,font=FR(16),fill=BODY,anchor='ls'); y+=23; first=False
    assert y<rect[3]+6,(y,rect)

block((1986,262,2548,360),[('L','CLIENT REVIEW'),
    ('B','REVISE. Ninth. Compound re-staged; house and'),
    ('B','staked plot placed in the right-hand yard.')])

block((1986,364,2548,556),[('L','READ'),
    ('B','Walled compounds of rectangular gabled houses;'),
    ('B','the long roof of the Hall of Posts; a stack of'),
    ('B','houses on a hill; a river running through the'),
    ('B','air; the same settlement hanging overhead.'),
    ('B','Foreground right: one house in its own swept'),
    ('B','yard, with a staked plot marked out and empty.')])

block((1986,656,2548,852),[('L','CHANGED SINCE V008'),
    ('B','The mound\u2019s shadows and haze now sit in the same'),
    ('B','dusty aerial perspective as the plain, and its'),
    ('B','foot dissolves into drifting dust instead of a'),
    ('B','hard seam. The pale grey mist over the lower-right'),
    ('B','houses is warmed out. The right compound is'),
    ('B','re-staged: the cramped longhouse set back.')])

block((1986,826,2548,1052),[('L','KNOWN ISSUES'),
    ('B','Dwellings on the summit still read large for the'),
    ('B','distance; shrinking them means re-rendering the'),
    ('B','heap, which is not attempted here. The right'),
    ('B','compound and its house are a generative re-stage'),
    ('B','built from the approved Nneka\u2019s House plate,'),
    ('B','not V008 pixels. The mound stays a masked repaint.')])

out.save('final/CAND_ESTABLISHING_V009_2560x1440.png')
print('saved',out.size)
