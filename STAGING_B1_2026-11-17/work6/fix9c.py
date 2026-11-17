from PIL import Image, ImageFilter, ImageDraw
import numpy as np
V11=Image.open('_e_v11_panel.png').convert('RGB')
V5=Image.open('_e_base_panel.png').convert('RGB')
A=np.array(V11,np.float32); B=np.array(V5,np.float32)

def rect_mask(w,h,r=10):
    m=Image.new('L',(w,h),0); d=ImageDraw.Draw(m); d.rectangle([0,0,w-1,h-1],fill=255)
    return np.array(m.filter(ImageFilter.GaussianBlur(r)),np.float32)[...,None]/255.

# 1. blue cast on the lower-right wall face
x0,y0,x1,y1=1380,1044,1901,1169
ref=A[1044:1169,760:1300].reshape(-1,3).mean(0); tgt=A[y0:y1,x0:x1].reshape(-1,3).mean(0)
scale=np.clip(ref/tgt,0.95,1.05); m=rect_mask(x1-x0,y1-y0,12)
A[y0:y1,x0:x1]=A[y0:y1,x0:x1]*scale*m+A[y0:y1,x0:x1]*(1-m)

# 2. vertical seam
sx0,sx1=1382,1426; sy0,sy1=768,968
band=A[sy0:sy1,sx0:sx1]
blur=np.array(Image.fromarray(band.astype(np.uint8)).filter(ImageFilter.GaussianBlur(5)),np.float32)
A[sy0:sy1,sx0:sx1]=blur*0.7+band*0.3

# 3. halo
hx0,hy0,hx1,hy1=1228,772,1478,940
reg=A[hy0:hy1,hx0:hx1]
med=np.array(Image.fromarray(reg.astype(np.uint8)).filter(ImageFilter.MedianFilter(13)),np.float32)
ex=np.clip(reg.mean(2)-med.mean(2)-7,0,None)[...,None]
A[hy0:hy1,hx0:hx1]=reg-np.clip(ex*0.7,0,70)

# 4. remove the paling: inpaint its footprint from the wall band above
px0,py0,px1,py1=1420,828,1526,920
src=A[py0-84:py1-84,px0:px1]
mk=rect_mask(px1-px0,py1-py0,8)
A[py0:py1,px0:px1]=src*mk+A[py0:py1,px0:px1]*(1-mk)
Image.fromarray(np.clip(A,0,255).astype(np.uint8)).save('work6/_step_paling.png')

# 5. restore the missing V005 cloth pieces at their own V005 coordinates (same camera, no invented placement)
bx0,by0,bx1,by1=1120,905,1270,1010
v5=B[by0:by1,bx0:bx1]; now=A[by0:by1,bx0:bx1]
L5=v5.mean(2); Ln=now.mean(2)
cloth=(L5<Ln-14).astype(np.float32)
cloth=Image.fromarray((cloth*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(3))
mk=np.array(cloth,np.float32)[...,None]/255.*0.95
A[by0:by1,bx0:bx1]=v5*mk+now*(1-mk)
Image.fromarray(np.clip(A,0,255).astype(np.uint8)).save('work6/est_v12_panel.png')
print('cloth px',int((mk>0.5).sum()))
