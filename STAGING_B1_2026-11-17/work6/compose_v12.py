from PIL import Image, ImageDraw, ImageFont
import numpy as np
BG=(9,13,24); TAN=(164,139,93); BODY=(226,225,217); DIM=(150,158,172)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)

a=np.array(Image.open('work6/est_v12_panel.png').convert('RGB'),np.float32)
rng=np.random.default_rng(31); g=rng.normal(0,1.0,(a.shape[0],a.shape[1],1)).astype(np.float32)
a=np.clip(a+g,0,255)
P=Image.fromarray(a.astype(np.uint8)); P.save('work6/EST_V012_panel.png')

M=Image.open('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg').convert('RGB')
out=M.copy(); out.paste(P,(60,152)); d=ImageDraw.Draw(out)

def spaced(xy,txt,font,fill,gap=1.2):
    x,y=xy
    for ch in txt:
        d.text((x,y),ch,font=font,fill=fill,anchor='ls'); x+=d.textlength(ch,font=font)+gap

d.rectangle([2468,33,2508,66],fill=BG); d.text((2478,58),'12',font=FB(22),fill=TAN,anchor='ls')
d.rectangle([1520,18,2560,140],fill=BG)
name='ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V012'
w=d.textlength(name,font=FB(19)); assert 2497-w>1775
d.text((2497,56),name,font=FB(19),fill=TAN,anchor='rs')
d.text((2497,88),'STATUS: REVIEW REQUIRED',font=FR(18),fill=(238,238,232),anchor='rs')
d.text((2497,116),'EXPLORATORY \u2014 NOT APPROVED CANON \u00b7 CHAPTER 8',font=FR(16),fill=DIM,anchor='rs')

def block(rect,items,paint=True):
    if paint: d.rectangle(rect,fill=BG)
    y=rect[1]+24; first=True
    for kind,txt in items:
        if kind=='L':
            if not first: y+=8
            spaced((1995,y),txt,FB(15),TAN); y+=28; first=False
        else:
            wd=d.textlength(txt,font=FR(16)); assert 1995+wd<2548,(round(1995+wd),txt)
            d.text((1995,y),txt,font=FR(16),fill=BODY,anchor='ls'); y+=23; first=False
    assert y<rect[3]+6,(y,rect)

block((1986,262,2548,360),[('L','CLIENT REVIEW'),
    ('B','PENDING. No client ruling is recorded on'),
    ('B','this version; it is a candidate only.')])

d.rectangle((1986,560,2548,1170),fill=BG)
block((1986,364,2548,556),[('L','READ'),
    ('B','Walled compounds of rectangular gabled houses;'),
    ('B','the long roof of the Hall of Posts; a stack of'),
    ('B','small houses on a hill; a river running through'),
    ('B','the air; the same settlement hanging overhead.'),
    ('B','Foreground right: one house in its own swept'),
    ('B','yard, with a staked plot marked out and empty.')])

block((1986,590,2548,790),[('L','CHANGED SINCE V009'),
    ('B','The hill\u2019s dwellings are ~30 per cent smaller'),
    ('B','and ~2\u00d7 as numerous; the wooden paling behind'),
    ('B','the yard house is gone and the V005 cloth line'),
    ('B','is whole again; the halo round the house and'),
    ('B','the vertical seam are blended out; the pale'),
    ('B','blue cast on the lower-right wall is corrected.')],paint=False)

block((1986,802,2548,1016),[('L','KNOWN ISSUES'),
    ('B','Nneka\u2019s House still reads large for the yard;'),
    ('B','reducing it needs the house re-rendered in'),
    ('B','place, which is not attempted here. The hill'),
    ('B','interior is a masked repaint inside a preserved'),
    ('B','silhouette. The compound and house remain a'),
    ('B','generative re-stage from the approved plate.'),
    ('B','No exact-version Research report on this file.')],paint=False)

block((1986,1030,2548,1160),[('L','FICTIONAL ELEMENTS'),
    ('B','The aerial river and the stacked mound of'),
    ('B','houses are fictional game-world conceits.'),
    ('B','They are not documented Igbo settlement forms.')],paint=False)

foot="VERSIONS KEPT: V005 base, V006\u2013V011 preserved. This sheet is V012, unapproved."
wd=d.textlength(foot,font=FR(15)); assert 940+wd<2540
d.text((940,1419),foot,font=FR(15),fill=DIM,anchor='ls')

out.save('final/CAND_ESTABLISHING_V012_2560x1440.png')
print('saved',out.size)
