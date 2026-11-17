from PIL import Image, ImageDraw, ImageFilter
import numpy as np, random

random.seed(20261117)
src = Image.open('panels/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005_PANEL.png').convert('RGB')
W,H = src.size

def jitter_path(pts, step=6, amp=1.6, seed=1):
    rnd = random.Random(seed)
    out=[]
    for i in range(len(pts)-1):
        x0,y0=pts[i]; x1,y1=pts[i+1]
        d=((x1-x0)**2+(y1-y0)**2)**0.5
        n=max(2,int(d/step))
        for k in range(n):
            t=k/n
            x=x0+(x1-x0)*t; y=y0+(y1-y0)*t
            out.append((x+rnd.uniform(-amp,amp), y+rnd.uniform(-amp,amp)))
    out.append(pts[-1])
    return out

main = jitter_path([(383,303),(392,378),(377,452),(398,520),(429,584),(447,640),(431,700),(454,760),(471,822)], seed=7)
branch = jitter_path([(398,520),(437,556),(462,592)], seed=11)
branch2 = jitter_path([(447,640),(414,676),(404,712)], seed=13)

# width profile: taper at both ends
def build_mask(path, wmax=3.4, seedsplit=None):
    m = Image.new('L', (W,H), 0)
    d = ImageDraw.Draw(m)
    n=len(path)
    for i in range(n-1):
        t=i/max(1,n-1)
        w = wmax*(0.35+0.65*(1-abs(2*t-1)**1.6))
        w *= 1.0 + 0.25*random.uniform(-1,1)
        d.line([path[i],path[i+1]], fill=255, width=max(1,int(round(w))))
        d.ellipse([path[i][0]-w/2,path[i][1]-w/2,path[i][0]+w/2,path[i][1]+w/2], fill=255)
    return m

mask = build_mask(main, 3.6)
for p in (branch, branch2):
    mask = Image.fromarray(np.maximum(np.asarray(mask), np.asarray(build_mask(p, 2.2))))

# soften
soft = mask.filter(ImageFilter.GaussianBlur(1.1))
M = np.asarray(soft).astype(np.float32)/255.0
Mb = np.asarray(mask.filter(ImageFilter.GaussianBlur(2.6))).astype(np.float32)/255.0

# rim: shifted mask on the light side (upper-right of the crack)
rim = Image.fromarray(np.asarray(mask))
rim_shift = Image.new('L',(W,H),0); rim_shift.paste(rim, (2,-2))
R = np.asarray(rim_shift.filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)/255.0
R = np.clip(R - Mb*0.85, 0, 1)

img = np.asarray(src).astype(np.float32)

# occlude: darken interior of the crack, strongest at its core
dark = 1.0 - 0.80*M
img = img*dark[...,None]

# the crack should also carry a bit of its own colour (cool shadow), not pure black
shadow_tint = np.array([26,24,26], dtype=np.float32)
img = img*(1-M[...,None]*0.35) + shadow_tint*(M[...,None]*0.35)

# lit lip along one side
img = img + (R[...,None] * np.array([58,52,42], dtype=np.float32))

# faint secondary micro-fissures (low contrast) to break the line up
rnd = random.Random(99)
for k in range(9):
    y0 = 330 + k*55 + rnd.uniform(-10,10)
    x0 = 372 + rnd.uniform(-6,10)
    p = jitter_path([(x0,y0),(x0+rnd.uniform(18,40), y0+rnd.uniform(10,26))], step=5, amp=1.2, seed=100+k)
    m2 = np.asarray(build_mask(p, 1.2).filter(ImageFilter.GaussianBlur(0.9))).astype(np.float32)/255.0
    img = img*(1-m2[...,None]*0.35)

out = Image.fromarray(np.clip(img,0,255).astype(np.uint8))
out.save('work/VR-008_crack_panel.png')
print('saved', out.size)
