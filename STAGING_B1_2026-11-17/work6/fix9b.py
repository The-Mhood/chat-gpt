from PIL import Image, ImageFilter, ImageDraw
import numpy as np
P=Image.open('_e_v11_panel.png').convert('RGB')
A=np.array(P,np.float32)

def rect_mask(w,h,r=10):
    m=Image.new('L',(w,h),0); d=ImageDraw.Draw(m); d.rectangle([0,0,w-1,h-1],fill=255)
    return np.array(m.filter(ImageFilter.GaussianBlur(r)),np.float32)[...,None]/255.

def ell_mask(w,h,r=12):
    m=Image.new('L',(w,h),0); d=ImageDraw.Draw(m); d.ellipse([2,2,w-3,h-3],fill=255)
    return np.array(m.filter(ImageFilter.GaussianBlur(r)),np.float32)[...,None]/255.

# 1. blue cast, gentler and local to the wall face
x0,y0,x1,y1=1380,1044,1901,1169
ref=A[1044:1169,760:1300].reshape(-1,3).mean(0); tgt=A[y0:y1,x0:x1].reshape(-1,3).mean(0)
scale=np.clip(ref/tgt,0.95,1.05)
A[y0:y1,x0:x1]=A[y0:y1,x0:x1]*scale*rect_mask(x1-x0,y1-y0,12)+A[y0:y1,x0:x1]*(1-rect_mask(x1-x0,y1-y0,12))
print('blue scale',scale.round(3))

# 2. seam
sx0,sx1=1382,1426; sy0,sy1=768,968
band=A[sy0:sy1,sx0:sx1]
blur=np.array(Image.fromarray(band.astype(np.uint8)).filter(ImageFilter.GaussianBlur(5)),np.float32)
A[sy0:sy1,sx0:sx1]=blur*0.7+band*0.3

# 3. halo
hx0,hy0,hx1,hy1=1228,772,1478,940
reg=A[hy0:hy1,hx0:hx1]
med=np.array(Image.fromarray(reg.astype(np.uint8)).filter(ImageFilter.MedianFilter(13)),np.float32)
L=reg.mean(2); Lm=med.mean(2)
ex=np.clip(L-Lm-7,0,None)[...,None]
A[hy0:hy1,hx0:hx1]=reg-np.clip(ex*0.7,0,70)

# 4. remove the whole paling footprint
px0,py0,px1,py1=1422,830,1524,918
src=A[py0-80:py1-80,px0:px1]
m=rect_mask(px1-px0,py1-py0,9)
A[py0:py1,px0:px1]=src*m+A[py0:py1,px0:px1]*(1-m)

# 5. draped striped cloth from untouched V005, soft-edged, on that wall
V5=np.array(Image.open('_e_base_panel.png').convert('RGB'),np.float32)
src=V5[922:1002,1186:1250]
cw,ch=64,96
cloth=np.array(Image.fromarray(src.astype(np.uint8)).resize((cw,ch),Image.LANCZOS),np.float32)
cloth=cloth*np.linspace(1.0,0.88,ch)[:,None,None]      # drape falloff
cx0,cy0=1446,838
dst=A[cy0:cy0+ch,cx0:cx0+cw]
mk=ell_mask(cw,ch,10)*0.95
A[cy0:cy0+ch,cx0:cx0+cw]=cloth*mk+dst*(1-mk)

Image.fromarray(np.clip(A,0,255).astype(np.uint8)).save('work6/est_v12_panel.png')
print('ok')
