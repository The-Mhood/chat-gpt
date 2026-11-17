from PIL import Image, ImageDraw, ImageFilter
import numpy as np

V8=Image.open('submit/B2_CAND_ESTABLISHING_V008_2560x1440.png').convert('RGB').crop((60,152,1961,1321))
G=Image.open('work6/yard_gen1.png').convert('RGB').resize((681,610),Image.LANCZOS)
X,Y=1280,520

def feather_mask(w,h,f=35):
    m=Image.new('L',(w,h),0); d=ImageDraw.Draw(m)
    d.rectangle([0,0,w-1,h-1],fill=255)
    m=m.filter(ImageFilter.GaussianBlur(0))
    # ramp: build alpha via distance from edge
    a=np.zeros((h,w),np.float32)
    yy,xx=np.mgrid[0:h,0:w]
    dist=np.minimum(np.minimum(xx,w-1-xx),np.minimum(yy,h-1-yy)).astype(np.float32)
    a=np.clip(dist/f,0,1)
    return Image.fromarray((a*255).astype(np.uint8))

base=np.array(V8,np.float32)
patch=np.array(G,np.float32)
# colour match: shift patch means to base means in a ring around the paste area
h,w,_=patch.shape
ring=base[Y-60:Y+h+60, X-60:X+w+60].reshape(-1,3)
pm=patch.reshape(-1,3)
shift=ring.mean(0)-pm.mean(0)
patch_c=np.clip(patch+shift,0,255)
alpha=np.array(feather_mask(w,h,35),np.float32)[...,None]/255.0
region=base[Y:Y+h,X:X+w]
base[Y:Y+h,X:X+w]=patch_c*alpha+region*(1-alpha)
out=Image.fromarray(base.astype(np.uint8))
out.save('work6/est_v9_p1.png')
print('shift',shift.round(1))
