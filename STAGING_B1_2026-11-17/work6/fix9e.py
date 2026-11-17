from PIL import Image, ImageFilter, ImageDraw
import numpy as np
V11=Image.open('_e_v11_panel.png').convert('RGB'); V5=Image.open('_e_base_panel.png').convert('RGB')
A=np.array(V11,np.float32); B=np.array(V5,np.float32)
def rect_mask(w,h,r=10):
    m=Image.new('L',(w,h),0); d=ImageDraw.Draw(m); d.rectangle([0,0,w-1,h-1],fill=255)
    return np.array(m.filter(ImageFilter.GaussianBlur(r)),np.float32)[...,None]/255.

# 1 lower-right blue cast
x0,y0,x1,y1=1380,1044,1901,1169
ref=A[1044:1169,760:1300].reshape(-1,3).mean(0); tgt=A[y0:y1,x0:x1].reshape(-1,3).mean(0)
scale=np.clip(ref/tgt,0.95,1.05); m=rect_mask(x1-x0,y1-y0,12)
A[y0:y1,x0:x1]=A[y0:y1,x0:x1]*scale*m+A[y0:y1,x0:x1]*(1-m)
print('blue scale',scale.round(3))

# 2 vertical blend seam x~1400
sx0,sx1=1382,1426; sy0,sy1=768,968
band=A[sy0:sy1,sx0:sx1]
blur=np.array(Image.fromarray(band.astype(np.uint8)).filter(ImageFilter.GaussianBlur(5)),np.float32)
A[sy0:sy1,sx0:sx1]=blur*0.7+band*0.3

# 3 hull halo
hx0,hy0,hx1,hy1=1228,772,1478,940
reg=A[hy0:hy1,hx0:hx1]
med=np.array(Image.fromarray(reg.astype(np.uint8)).filter(ImageFilter.MedianFilter(13)),np.float32)
ex=np.clip(reg.mean(2)-med.mean(2)-7,0,None)[...,None]
A[hy0:hy1,hx0:hx1]=reg-np.clip(ex*0.7,0,70)

# 4 remove the paling using the generative in-context patch, footprint only
CX0,CY0,CX1,CY1=1340,770,1620,960
gen=Image.open('work6/paling_fix.png').convert('RGB').resize((CX1-CX0,CY1-CY0),Image.LANCZOS)
G=np.array(gen,np.float32)
gref=np.median(G[40:150,60:120].reshape(-1,3),0); dref=np.median(A[CY0+40:CY0+150,CX0+60:CX0+120].reshape(-1,3),0)
G=np.clip(G+(dref-gref),0,255)
fp=np.zeros((CY1-CY0,CX1-CX0),np.float32)
fx0,fy0,fx1,fy1=1420-CX0,826-CY0,1526-CX0,922-CY0
mm=Image.new('L',(CX1-CX0,CY1-CY0),0); ImageDraw.Draw(mm).rectangle([fx0,fy0,fx1,fy1],fill=255)
mk=np.array(mm.filter(ImageFilter.GaussianBlur(12)),np.float32)[...,None]/255.
A[CY0:CY1,CX0:CX1]=G*mk+A[CY0:CY1,CX0:CX1]*(1-mk)

# 5 restore the missing V005 cloth pieces at their own coordinates
bx0,by0,bx1,by1=1120,905,1270,1010
v5=B[by0:by1,bx0:bx1]; now=A[by0:by1,bx0:bx1]
cloth=(v5.mean(2)<now.mean(2)-14).astype(np.float32)
cloth=Image.fromarray((cloth*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(3))
mk2=np.array(cloth,np.float32)[...,None]/255.*0.95
A[by0:by1,bx0:bx1]=v5*mk2+now*(1-mk2)
Image.fromarray(np.clip(A,0,255).astype(np.uint8)).save('work6/est_v12_panel.png')
print('ok')
