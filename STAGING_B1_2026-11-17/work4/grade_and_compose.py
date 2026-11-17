from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np
BG=(9,13,24); TAN=(164,139,93); BODY=(226,225,217)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)

def spaced(d,xy,txt,font,fill,gap=1.2):
    x,y=xy
    for ch in txt:
        d.text((x,y),ch,font=font,fill=fill,anchor='ls'); x+=d.textlength(ch,font=font)+gap

# ---------- 1. local atmospheric grade around Nneka's House
im=Image.open('work4/EST_V008_moundcomp.png').convert('RGB')
a=np.asarray(im).astype(np.float32)
H,W=a.shape[:2]
cx,cy,r0,r1=685,975,120,300
yy,xx=np.mgrid[0:H,0:W]
dist=np.sqrt((xx-cx)**2+(yy-cy)**2)
w=np.zeros((H,W,1),dtype=np.float32)      # 1 inside r0, 0 beyond r1
# desaturate + warm haze
lum=a.mean(axis=2,keepdims=True)
desat=a*(1-0.16*w)+lum*(0.16*w)
haze=np.array([212,178,148],dtype=np.float32)
graded=desat*(1-0.07*w)+haze*(0.07*w)
Image.fromarray(np.clip(graded,0,255).astype(np.uint8)).save('work4/EST_V008_graded.png')
print('grade px', int((w[:,:,0]>0.01).sum()))

# ---------- 2. chrome
M=Image.open('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg').convert('RGB')
P=Image.open('work4/EST_V008_graded.png').convert('RGB')
out=M.copy(); out.paste(P,(60,152)); d=ImageDraw.Draw(out)
d.rectangle([2481,33,2504,63],fill=BG)
d.text((2485,57),'8',font=FB(22),fill=TAN,anchor='ls')
def block(rect, items):
    d.rectangle(rect,fill=BG); y=rect[1]+22; first=True
    for kind,txt in items:
        if kind=='L':
            if not first: y+=6
            spaced(d,(1995,y),txt,FB(15),TAN); y+=27; first=False
        else:
            wd=d.textlength(txt,font=FR(16)); assert 1995+wd<2548,(round(1995+wd),txt)
            d.text((1995,y),txt,font=FR(16),fill=BODY,anchor='ls'); y+=23; first=False
block((1986,268,2548,356),[('L','CLIENT REVIEW'),
    ('B','REVISE. Eighth. Heap rescaled to village scale.')])
block((1986,676,2548,1058),[('L','CHANGED SINCE V005'),
    ('B','The mound is rebuilt as a dense heap of hundreds of'),
    ('B','small single-storey homes at the same scale as the'),
    ('B','village below it, with granular mud and ragged'),
    ('B','thatch instead of the old oversized huts.'),
    ('B','No pole crosses the aerial river. Chrome now V008,'),
    ('B','CLIENT REVIEW populated (it was blank in V007).'),
    ('L','KNOWN ISSUES'),
    ('B','Nneka\u2019s House is NOT placed: three integration'),
    ('B','attempts read pasted or CGI. Needs CD direction.'),
    ('B','Mound surfaces still read smoother than V005\u2019s.'),
    ('B','The whole mound is a masked repaint, not V005.')])
out.save('final/CAND_ESTABLISHING_V008_2560x1440.png')
print('saved', out.size)
