from PIL import Image, ImageDraw, ImageFont
import numpy as np
BG=(9,13,24); TAN=(164,139,93); BODY=(226,225,217)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)

a=np.array(Image.open('work6/est_v10_p2.png').convert('RGB'),np.float32)
rng=np.random.default_rng(23)
g=rng.normal(0,1.15,(a.shape[0],a.shape[1],1)).astype(np.float32)
a=np.clip(a+g,0,255)
P=Image.fromarray(a.astype(np.uint8)); P.save('work6/EST_V010_panel.png')

M=Image.open('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg').convert('RGB')
out=M.copy(); out.paste(P,(60,152)); d=ImageDraw.Draw(out)

def spaced(xy,txt,font,fill,gap=1.2):
    x,y=xy
    for ch in txt:
        d.text((x,y),ch,font=font,fill=fill,anchor='ls'); x+=d.textlength(ch,font=font)+gap

d.rectangle([2468,33,2508,66],fill=BG); d.text((2478,58),'10',font=FB(22),fill=TAN,anchor='ls')
d.rectangle([1520,18,2560,140],fill=BG)
name='ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V010'
w=d.textlength(name,font=FB(19)); assert 2497-w>1775,(w,); d.text((2497,56),name,font=FB(19),fill=TAN,anchor='rs')
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
    ('B','REVISE. Tenth. Hill dwellings re-scaled to the'),
    ('B','plain; the right-hand compound is unchanged')])

block((1986,364,2548,556),[('L','READ'),
    ('B','Walled compounds of rectangular gabled houses;'),
    ('B','the long roof of the Hall of Posts; a stack of'),
    ('B','small houses on a hill; a river running through'),
    ('B','the air; the same settlement hanging overhead.'),
    ('B','Foreground right: one house in its own swept'),
    ('B','yard, with a staked plot marked out and empty.')])

block((1986,656,2548,852),[('L','CHANGED SINCE V009'),
    ('B','Every dwelling on the hill is rebuilt roughly 30'),
    ('B','per cent smaller and about twice as numerous,'),
    ('B','inside the same outline against the sky, so the'),
    ('B','hill now reads at the scale of the village below'),
    ('B','it. Thatch grain and terrace wear were carried'),
    ('B','back over the rebuilt surface.')])

block((1986,826,2548,1052),[('L','KNOWN ISSUES'),
    ('B','The hill interior is a generative re-render'),
    ('B','composited inside a preserved silhouette mask,'),
    ('B','not V008 pixels; its outline is unchanged by'),
    ('B','construction. The right compound and its house'),
    ('B','remain a generative re-stage built from the'),
    ('B','approved Nneka\u2019s House plate. No exact-version'),
    ('B','Research Agent report exists yet for this file.')])

out.save('final/CAND_ESTABLISHING_V010_2560x1440.png')
print('saved',out.size)
