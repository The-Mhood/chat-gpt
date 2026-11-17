from PIL import Image, ImageDraw, ImageFilter, ImageChops
import numpy as np, random
random.seed(7)

src = Image.open('panels/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005_PANEL.png').convert('RGB')
W,H = src.size

def jitter_path(pts, step=6, amp=1.7, seed=1):
    rnd = random.Random(seed); out=[]
    for i in range(len(pts)-1):
        x0,y0=pts[i]; x1,y1=pts[i+1]
        d=((x1-x0)**2+(y1-y0)**2)**0.5; n=max(2,int(d/step))
        for k in range(n):
            t=k/n
            out.append((x0+(x1-x0)*t+rnd.uniform(-amp,amp), y0+(y1-y0)*t+rnd.uniform(-amp,amp)))
    out.append(pts[-1]); return out

main = jitter_path([(381,303),(390,376),(376,450),(397,519),(428,583),(446,639),(430,699),(453,759),(470,821)], seed=7)
branches = [jitter_path([(397,519),(436,555),(461,591)], seed=11),
            jitter_path([(446,639),(413,675),(403,711)], seed=13),
            jitter_path([(428,583),(465,606)], seed=17),
            jitter_path([(376,450),(352,470)], seed=19),
            jitter_path([(470,821),(492,842)], seed=23)]

def build(paths_widths):
    m = Image.new('L',(W,H),0); d=ImageDraw.Draw(m)
    for path,wmax,seedbase in paths_widths:
        rnd=random.Random(seedbase)
        n=len(path)
        for i in range(n-1):
            t=i/max(1,n-1)
            w = wmax*(0.30+0.70*(1-abs(2*t-1)**1.5))*(1+0.35*rnd.uniform(-1,1))
            w=max(1.0,w)
            d.line([path[i],path[i+1]], fill=255, width=int(round(w)))
            d.ellipse([path[i][0]-w/2,path[i][1]-w/2,path[i][0]+w/2,path[i][1]+w/2], fill=255)
    return m

core_mask = build([(main,3.0,3)] + [(p,1.9,31+i) for i,p in enumerate(branches)])
core_mask = core_mask.filter(ImageFilter.GaussianBlur(0.55))
M = np.asarray(core_mask).astype(np.float32)/255.0

wide = core_mask.filter(ImageFilter.GaussianBlur(7.0))
Mw = np.asarray(wide).astype(np.float32)/255.0

# --- slight lateral displacement of the plaster on the right of the fracture
side_src = core_mask.filter(ImageFilter.GaussianBlur(1.0))
side = Image.new('L',(W,H),0); side.paste(side_src,(4,0))
S = np.asarray(side.filter(ImageFilter.GaussianBlur(2.0))).astype(np.float32)/255.0
S = np.clip(S,(0),1)

arr = np.asarray(src).astype(np.float32)
shifted = np.asarray(src.transform((W,H), Image.AFFINE, (1,0,-1.7,0,1,-0.5), resample=Image.BICUBIC)).astype(np.float32)
img = arr*(1-S[...,None]*0.9) + shifted*(S[...,None]*0.9)

# occlusion band + core darkening (modulated along length so it is not a uniform line)
mod = np.asarray(core_mask.filter(ImageFilter.GaussianBlur(9.0))).astype(np.float32)/255.0
mod = 0.65 + 0.7*mod
img = img*(1 - (0.16*Mw*mod)[...,None])
img = img*(1 - (0.72*M*mod)[...,None])
img = img*(1-M[...,None]*0.30) + np.array([28,26,28],np.float32)*(M[...,None]*0.30)

# lit lip on the far side of the fracture
lip = Image.new('L',(W,H),0); lip.paste(core_mask,(-3,-1))
L = np.asarray(lip.filter(ImageFilter.GaussianBlur(1.4))).astype(np.float32)/255.0
L = np.clip(L - M*1.1, 0, 1)
img = img + L[...,None]*np.array([46,42,34],np.float32)

# micro fissures
rnd=random.Random(99)
for k in range(10):
    y0=330+k*52+rnd.uniform(-8,8); x0=372+rnd.uniform(-8,8)
    p=jitter_path([(x0,y0),(x0+rnd.uniform(16,38), y0+rnd.uniform(8,24))], step=5, amp=1.1, seed=100+k)
    m2=np.asarray(build([(p,1.0,0)]).filter(ImageFilter.GaussianBlur(0.8))).astype(np.float32)/255.0
    img = img*(1-m2[...,None]*0.30)

out=Image.fromarray(np.clip(img,0,255).astype(np.uint8))
out.save('work/VR-008_crack_panel_v2.png')
print('ok', out.size)
