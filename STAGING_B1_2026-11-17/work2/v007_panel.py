from PIL import Image, ImageDraw, ImageFilter
import numpy as np, random, math

random.seed(7); np.random.seed(7)
V5 = Image.open('masters/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005.jpg').convert('RGB').crop((60,152,1961,1321))
V4 = Image.open('panels/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V004_PANEL.jpg').convert('RGB')
W,H = V5.size
S, DX, DY = 1.01, 6, 6     # measured: V5(x,y) ~= V4((x+DX)/S, (y+DY)/S)

base = np.asarray(V5).astype(np.float32)
img  = base.copy()

# ---------------------------------------------------------------- 1. MIDRIFF
# paste the approved bare-midriff construction from V004, aligned
src = V4.transform((W,H), Image.AFFINE, (1/S, 0, DX/S, 0, 1/S, DY/S), resample=Image.BICUBIC)
src = np.asarray(src).astype(np.float32)

poly = [(874,652),(896,642),(924,636),(952,632),(972,630),(980,668),(978,706),(972,740),(944,744),(912,744),(884,738),(872,716),(870,682)]
m = Image.new('L',(W,H),0); ImageDraw.Draw(m).polygon(poly, fill=255)
m = m.filter(ImageFilter.GaussianBlur(7))
Mm = np.asarray(m).astype(np.float32)/255.0

img = img*(1-Mm[...,None]) + src*Mm[...,None]

# ---------------------------------------------------------------- 2. ARMLET
def arm_span(y):
    t = (y-552.0)/(610.0-552.0)
    l = 1004 + (1013-1004)*t
    r = 1059 + (1068-1059)*t
    return l, r

Y0, Y1 = 552, 610
NC = 5

ring = Image.new('L',(W,H),0); rd=ImageDraw.Draw(ring)
for yy in range(Y0-3, Y1+4):
    l,r = arm_span(yy)
    rd.line([(int(l),yy),(int(r),yy)], fill=255)
R = np.asarray(ring.filter(ImageFilter.GaussianBlur(0.5))).astype(np.float32)/255.0

yy = np.arange(H, dtype=np.float32)[:,None]
xx = np.arange(W, dtype=np.float32)[None,:]
l0, r0 = arm_span((Y0+Y1)/2.0)
uu = np.clip((xx - l0)/(r0-l0), 0, 1)
bow = 9.0*((2*uu-1)**2)
yv = yy + bow

span = float(Y1-Y0)
coil = ((yv - Y0)/span)*NC
frac = coil - np.floor(coil)

# each coil is a wire: circular cross-section -> bright crest, tight dark groove between wires
bead = np.sin(np.pi*np.clip(frac,0,1))**0.55
groove = np.minimum(np.clip(frac/0.16,0,1), np.clip((1-frac)/0.16,0,1))
groove = 0.06 + 0.94*groove**0.7

# the arm's own luminance supplies the cylindrical form AND the overcast light
lum = base.mean(axis=2)/255.0
sel = R>0.5
lo, hi = np.percentile(lum[sel], 6), np.percentile(lum[sel], 94)
ln = np.clip((lum-lo)/(hi-lo+1e-6), 0, 1)

# aged cast bronze, low chroma, no gold
tint = np.array([118,95,64], np.float32)
bronze = tint*(0.10 + 0.78*(ln**1.38))[...,None]*((0.34 + 0.70*bead)*groove)[...,None]
bronze = np.clip(bronze, 0, 255)

# dull specular: only where the arm is already lit, only on the crest of each wire, biased left
spec = np.clip((0.55-uu*1.00),0,1)*np.clip(bead-0.80,0,1)*np.clip(ln-0.62,0,1)*0.45
bronze = np.clip(bronze + np.array([52,46,34],np.float32)*spec[...,None], 0, 255)
ls = bronze.mean(axis=2, keepdims=True)
bronze = np.clip(bronze*0.82 + ls*0.18, 0, 255)

# patina / hammer grain
bronze = np.clip(bronze + np.random.normal(0,3.0,(H,W,1)), 0, 255)

# alpha: solid on the arm, faded where the arm turns away at the silhouette
alpha = R*((yv>=Y0)&(yv<=Y1))*np.clip(ln*2.6,0,1)
alpha = np.asarray(Image.fromarray((alpha*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))).astype(np.float32)/255.0

img = img*(1-alpha[...,None]) + bronze*alpha[...,None]

def aoshadow(y0,y1,strength):
    mm = Image.new('L',(W,H),0); d=ImageDraw.Draw(mm)
    for yy2 in range(int(y0),int(y1)):
        l,r = arm_span(yy2); d.line([(int(l),yy2),(int(r),yy2)], fill=255)
    arr = np.asarray(mm.filter(ImageFilter.GaussianBlur(2.4))).astype(np.float32)/255.0
    return arr*strength
img = img*(1-aoshadow(Y0-6,Y0+1,0.55)[...,None])
img = img*(1-aoshadow(Y1-1,Y1+8,0.55)[...,None])

# ---------------------------------------------------------------- 3. FRACTURE
def jitter(pts, step=5, amp=1.3, sd=1):
    r=random.Random(sd); out=[]
    for i in range(len(pts)-1):
        x0,y0=pts[i]; x1,y1=pts[i+1]
        d=math.hypot(x1-x0,y1-y0); n=max(2,int(d/step))
        for k in range(n):
            t=k/n
            out.append((x0+(x1-x0)*t+r.uniform(-amp,amp), y0+(y1-y0)*t+r.uniform(-amp,amp)))
    out.append(pts[-1]); return out

trunk = jitter([(472,838),(479,792),(466,742),(481,691),(470,640),(486,592),(476,553),(489,527)], step=5, amp=1.1, sd=3)
br = [jitter([(481,691),(508,672),(516,650)], step=5, amp=1.0, sd=11),
      jitter([(470,640),(447,624),(438,606)], step=5, amp=1.0, sd=13),
      jitter([(476,553),(455,540)], step=4, amp=0.8, sd=17),
      jitter([(472,838),(452,850)], step=4, amp=0.8, sd=19)]

def stroke(paths_widths):
    mm=Image.new('L',(W,H),0); d=ImageDraw.Draw(mm)
    for path,wmax,sd in paths_widths:
        r=random.Random(sd); n=len(path)
        for i in range(n-1):
            t=i/max(1,n-1)
            w = wmax*(0.28+0.72*(1-abs(2*t-1)**1.4))*(1+0.30*r.uniform(-1,1))
            w = max(0.9,w)
            d.line([path[i],path[i+1]], fill=255, width=int(round(w)))
            d.ellipse([path[i][0]-w/2,path[i][1]-w/2,path[i][0]+w/2,path[i][1]+w/2], fill=255)
    return mm

core = stroke([(trunk,2.6,31)]+[(p,1.5,41+i) for i,p in enumerate(br)])
core = core.filter(ImageFilter.GaussianBlur(0.4))
C = np.asarray(core).astype(np.float32)/255.0

# granular edge: break the mask with plaster-grain noise so it is not a clean stroke
noise = np.random.normal(0,1,(H,W))
noise = np.asarray(Image.fromarray(((noise-noise.min())/((noise.max()-noise.min())+1e-9)*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.0))).astype(np.float32)/255.0
edge = np.clip(C*(0.84+0.34*noise), 0, 1)
coreC = np.clip(edge - 0.15, 0, 1)

# displacement of the plaster on the far side of the fracture (small, local)
sh = Image.new('L',(W,H),0); sh.paste(core, (3,0))
D = np.asarray(sh.filter(ImageFilter.GaussianBlur(1.6))).astype(np.float32)/255.0
D = np.clip(D,0,1)
shifted = np.asarray(V5.transform((W,H), Image.AFFINE, (1,0,-1.3,0,1,-0.35), resample=Image.BICUBIC)).astype(np.float32)
mixed = img*(1-D[...,None]*0.85) + shifted*(D[...,None]*0.85)

# warm dark-umber crevice, modulated along its length; no wide blur halo
mod = np.asarray(core.filter(ImageFilter.GaussianBlur(6.0))).astype(np.float32)/255.0
mod = 0.55 + 0.85*mod
umber = np.array([30,22,17], np.float32)
mixed = mixed*(1-(0.62*coreC*mod)[...,None]) * (1-(0.10*C)[...,None])
mixed = mixed*(1-coreC[...,None]*0.28) + umber*(coreC[...,None]*0.28)

# micro-crumbled clay lips: small chips with a lit top edge and a tiny shadow
rnd=random.Random(77)
for i in range(46):
    t = rnd.random()
    idx = int(t*(len(trunk)-1))
    px,py = trunk[idx]
    off = rnd.choice([-1,1])*(2.0+rnd.random()*3.0)
    w = rnd.uniform(1.6,4.2); h = rnd.uniform(1.2,2.6)
    chip = Image.new('L',(W,H),0)
    ImageDraw.Draw(chip).ellipse([px+off-w/2, py-h/2, px+off+w/2, py+h/2], fill=255)
    chipb = np.asarray(chip.filter(ImageFilter.GaussianBlur(0.5))).astype(np.float32)/255.0
    lit = 0.16 if rnd.random()<0.6 else 0.09
    mixed = mixed + chipb[...,None]*np.array([lit*255, lit*236, lit*205], np.float32)
    # the chip casts a hairline shadow on its lower side
    sh2 = Image.new('L',(W,H),0)
    ImageDraw.Draw(sh2).ellipse([px+off-w/2, py+h/2-0.6, px+off+w/2, py+h/2+1.4], fill=255)
    sb = np.asarray(sh2.filter(ImageFilter.GaussianBlur(0.7))).astype(np.float32)/255.0
    mixed = mixed*(1-sb[...,None]*0.30)

img = mixed
out = Image.fromarray(np.clip(img,0,255).astype(np.uint8))
out.save('work2/V007_panel.png')
print('saved', out.size)
