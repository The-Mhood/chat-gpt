from PIL import Image, ImageFilter, ImageDraw
import numpy as np
P=Image.open('_e_v11_panel.png').convert('RGB')
A=np.array(P,np.float32)
H,W=A.shape[:2]

def feather(w,h,r=8):
    m=Image.new('L',(w,h),0); d=ImageDraw.Draw(m); d.rectangle([r,r,w-r,h-r],fill=255)
    return np.array(m.filter(ImageFilter.GaussianBlur(r)),np.float32)/255.

# --- 1. lower-right blue cast on the foreground wall face
box=(1360,1030,1901,1169)
x0,y0,x1,y1=box
ref=A[1030:1169,760:1300]
tgt=A[y0:y1,x0:x1]
rm=ref.reshape(-1,3).mean(0); tm=tgt.reshape(-1,3).mean(0)
scale=np.clip(rm/tm,0.85,1.15)
corr=tgt*scale
m=feather(x1-x0,y1-y0,10)[...,None]
A[y0:y1,x0:x1]=corr*m+tgt*(1-m)
print('blue cast scale (target/src):',scale.round(3))

# --- 2. vertical blend seam near panel x=1400 (yard boundary)
sx0,sx1=1382,1424; sy0,sy1=770,965
band=A[sy0:sy1,sx0:sx1]
blur=np.array(Image.fromarray(band.astype(np.uint8)).filter(ImageFilter.GaussianBlur(4)),np.float32)
# keep a little of the original structure so the band does not read as a smear
mix=0.62
A[sy0:sy1,sx0:sx1]=blur*mix+band*(1-mix)

# --- 3. halo around the hut: pull over-bright pixels toward the local median
hx0,hy0,hx1,hy1=1230,775,1475,935
reg=A[hy0:hy1,hx0:hx1]
med=np.array(Image.fromarray(reg.astype(np.uint8)).filter(ImageFilter.MedianFilter(11)),np.float32)
L=reg.mean(2); Lm=med.mean(2)
excess=np.clip(L-Lm-9,0,None)[...,None]
reg=reg-np.clip(excess*0.55,0,60)
A[hy0:hy1,hx0:hx1]=reg
print('halo pull applied, mean excess',float(np.clip(L-Lm-9,0,None).mean()).__round__(2))

# --- 4. remove the wooden paling, restore V005 content behind it
px0,py0,px1,py1=1428,838,1516,910
src=A[py0-72:py1-72,px0:px1]           # the same wall, one band higher
m=feather(px1-px0,py1-py0,7)[...,None]
A[py0:py1,px0:px1]=src*m+A[py0:py1,px0:px1]*(1-m)

# --- 5. restore the V005 draped striped cloth on that wall
V5=np.array(Image.open('_e_base_panel.png').convert('RGB'),np.float32)
cloth=V5[924:1000,1188:1248]           # plain + striped cloths from the untouched V005 line
cloth=Image.fromarray(cloth.astype(np.uint8)).resize((62,92),Image.LANCZOS)
cm=np.array(cloth,np.float32)
# light drape shading: slightly darker at the bottom edge
sh=np.linspace(1.0,0.86,92)[:,None,None]; cm=cm*sh
dst=A[846:938,1452:1514]
mask=np.array(Image.new('L',(62,92),0).point(lambda v:255).filter(ImageFilter.GaussianBlur(6)),np.float32)[...,None]/255.
mask*=np.linspace(1,1,92)[:,None,None]
A[846:938,1452:1514]=cm*mask+dst*(1-mask)

out=Image.fromarray(np.clip(A,0,255).astype(np.uint8))
out.save('work6/est_v12_panel.png')
print('saved',out.size)
