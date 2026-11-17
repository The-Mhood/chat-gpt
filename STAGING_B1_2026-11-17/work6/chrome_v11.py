from PIL import Image, ImageDraw, ImageFont
BG=(9,13,24); TAN=(164,139,93); BODY=(226,225,217); DIM=(150,158,172)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
im=Image.open('final/CAND_ESTABLISHING_V010_2560x1440.png').convert('RGB')
d=ImageDraw.Draw(im)
def spaced(xy,txt,font,fill,gap=1.2):
    x,y=xy
    for ch in txt:
        d.text((x,y),ch,font=font,fill=fill,anchor='ls'); x+=d.textlength(ch,font=font)+gap
# version block: 10 -> 11
d.rectangle([2468,33,2508,66],fill=BG); d.text((2478,58),'11',font=FB(22),fill=TAN,anchor='ls')
d.rectangle([1520,18,2560,140],fill=BG)
name='ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V011'
w=d.textlength(name,font=FB(19)); assert 2497-w>1775
d.text((2497,56),name,font=FB(19),fill=TAN,anchor='rs')
d.text((2497,88),'STATUS: REVIEW REQUIRED',font=FR(18),fill=(238,238,232),anchor='rs')
d.text((2497,116),'EXPLORATORY \u2014 NOT APPROVED CANON \u00b7 CHAPTER 8',font=FR(16),fill=DIM,anchor='rs')
# CLIENT REVIEW block: honest population
rect=(1986,262,2548,360)
d.rectangle(rect,fill=BG)
spaced((1995,286),'CLIENT REVIEW',FB(15),TAN)
lines=["PENDING. No client ruling is recorded on","this version; it is a candidate only."]
y=rect[1]+24+28
for t in lines:
    wd=d.textlength(t,font=FR(16)); assert 1995+wd<2548,(round(1995+wd),t)
    d.text((1995,y),t,font=FR(16),fill=BODY,anchor='ls'); y+=23
# footer version register
foot="VERSIONS KEPT: V005 base, V006\u2013V010 preserved. This sheet is V011, unapproved."
wd=d.textlength(foot,font=FR(15)); assert 940+wd<2540,(round(940+wd),)
d.text((940,1419),foot,font=FR(15),fill=DIM,anchor='ls')
im.save('final/CAND_ESTABLISHING_V011_2560x1440.png')
print('saved',im.size)
