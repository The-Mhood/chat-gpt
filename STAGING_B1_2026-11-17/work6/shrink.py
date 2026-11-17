from PIL import Image, ImageFilter
import numpy as np
im=Image.open('work6/est_v9_p5.png').convert('RGB')
a=np.array(im,np.float32); H,W,_=a.shape
M=np.array(Image.open('work4/EST_V008_mask.png').convert('L'),np.float32)/255.
M=Image.fromarray((M*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(12))
M=np.array(M,np.float32)/255.
ys,xs=np.where(M>0.2)
cx=(xs.min()+xs.max())/2.0; cy=705.0        # base centre of the mound
R=520.0; s=0.90
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
r=np.sqrt((xx-cx)**2+((yy-cy)*1.15)**2)
k=np.clip(1.0-(r/R),0,1)                     # influence: 1 at centre, 0 at R
k=0.5-0.5*np.cos(np.pi*k)                    # smoothstep
mag=(1.0-s)*k
sx=cx+(xx-cx)*(1.0-mag); sy=cy+(yy-cy)*(1.0-mag)
x0=np.clip(sx,0,W-1); y0=np.clip(sy,0,H-1)
xi=x0.astype(np.int32); yi=y0.astype(np.int32)
fx=(x0-xi)[...,None]; fy=(y0-yi)[...,None]
a00=a[yi,xi]; a10=a[yi,np.clip(xi+1,0,W-1)]; a01=a[np.clip(yi+1,0,H-1),xi]; a11=a[np.clip(yi+1,0,H-1),np.clip(xi+1,0,W-1)]
out=a00*(1-fx)*(1-fy)+a10*fx*(1-fy)+a01*(1-fx)*fy+a11*fx*fy
Image.fromarray(np.clip(out,0,255).astype(np.uint8)).save('work6/est_v9_p6.png')
print('centre',cx,cy)
