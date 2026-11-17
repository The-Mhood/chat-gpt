from PIL import Image, ImageFilter
import numpy as np

im=Image.open('work6/est_v9_p4.png').convert('RGB')
a=np.array(im,np.float32)
H,W,_=a.shape

# ---------- 1. stray roof-post stubs: thin vertical structures poking above the local roof envelope
L=a.mean(2)
struct=(L<168)
region_y=(slice(140,760), slice(880,1901))
top=np.full(W,10**6,dtype=int)
for x in range(880,1901):
    col=np.where(struct[140:760,x])[0]
    if len(col): top[x]=col[0]+140
env=top.copy()
for x in range(880,1901):
    lo=max(880,x-14); hi=min(1900,x+14)
    vals=top[lo:hi+1]; vals=vals[vals<10**6]
    env[x]=int(np.median(vals)) if len(vals) else top[x]
removed=0
for x in range(900,1900):
    if top[x]<env[x]-10:
        y0,y1=top[x],env[x]
        # copy a clean neighbouring column
        for off in (12,-12,20,-20,28,-28):
            xs=x+off
            if 900<=xs<1900 and top[xs]>=env[xs]-3:
                patch=a[y0:y1+2, xs:xs+1, :]
                patch=np.repeat(patch,y1+2-y0,axis=1)
                a[y0:y1+2, max(0,x-1):x+2, :]=patch
                removed+=1; break
print('stub columns cleaned',removed)

# ---------- 2. atmospheric perspective + shadow lift inside the mound mask
M=np.array(Image.open('work4/EST_V008_mask.png').convert('L'),np.float32)/255.0
M=Image.fromarray((M*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(26))
M=np.array(M,np.float32)/255.0
base_y, top_y = 705.0, 185.0
yy=np.arange(H)[:,None].astype(np.float32)
w=np.clip((base_y-yy)/(base_y-top_y),0,1)          # 1 = far (summit), 0 = base
haze=np.array([223,201,172],np.float32)            # dusty daylight haze sampled from the plain
alpha=(0.03+0.185*np.clip(w,0,1)**1.4)*M
a=a*(1-alpha[...,None])+haze*alpha[...,None]
# shadow lift where the haze is strongest
lev=(0.06+0.13*np.clip(w,0,1)**1.2)*M
lum=a.mean(2,keepdims=True)/255.0
lift=(lum**0.78)*255.0
a=a*(1-lev[...,None])+ (a*0.55+lift*0.45)*lev[...,None]

# ---------- 3. dust drift along the mound foot (softens the base seam)
band=np.zeros((H,W),np.float32)
masks=np.array(Image.open('work4/EST_V008_mask.png').convert('L'),np.float32)/255.0
# bottom edge of mask per column
bot=np.zeros(W,dtype=np.int32)
for x in range(880,1901):
    col=np.where(masks[:,x]>0.5)[0]
    if len(col): bot[x]=col[-1]
drift=np.zeros((H,W),np.float32)
rng=np.random.default_rng(7)
for x in range(860,1901):
    b=bot[x]
    if b==0: continue
    for dy in range(0,64):
        y=b+dy-32
        if 0<=y<H:
            v=np.exp(-((dy-32)**2)/(2*17.0**2))
            drift[y,x]=max(drift[y,x],v*0.26)
drift=Image.fromarray((np.clip(drift,0,1)*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(9))
drift=np.array(drift,np.float32)/255.0
# dust noise so it does not read as a clean gradient
noise=rng.normal(0,1,(H//8+1,W//8+1)).astype(np.float32)
noise=Image.fromarray(((noise-noise.min())/(noise.max()-noise.min())*255).astype(np.uint8)).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(6))
noise=np.array(noise,np.float32)/255.0
d_alpha=drift*(0.30+0.70*noise)
a=a*(1-d_alpha[...,None])+np.array([226,203,174],np.float32)*d_alpha[...,None]

# ---------- 4. grey mist veil on the lower-right mound: warm it and restore contrast
gy,gx=np.mgrid[0:H,0:W]
R=((gx>1480)&(gx<1901)&(gy>380)&(gy<720)).astype(np.float32)
R=Image.fromarray((R*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(30))
R=np.array(R,np.float32)/255.0*masks
grey=(a.max(2)-a.min(2))<48
veil=R*grey.astype(np.float32)
g=np.array([1.10,1.01,0.84],np.float32)
a=a*(1-0.85*veil[...,None])+np.clip(a*g,0,255)*(0.85*veil[...,None])
# local contrast back
blur=np.array(Image.fromarray(a.astype(np.uint8)).filter(ImageFilter.GaussianBlur(9)),np.float32)
a=a+ (a-blur)*0.45*veil[...,None]

Image.fromarray(np.clip(a,0,255).astype(np.uint8)).save('work6/est_v9_p5.png')
print('saved')
