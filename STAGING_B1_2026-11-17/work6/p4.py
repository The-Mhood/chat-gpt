from PIL import Image
import numpy as np
BASE=Image.open('work6/est_v9_p2.png').convert('RGB')
G=Image.open('work6/house_gen1.png').convert('RGB').resize((751,500),Image.LANCZOS)
X,Y=1150,640
base=np.array(BASE,np.float32); patch=np.array(G,np.float32)
h,w,_=patch.shape
yy,xx=np.mgrid[0:h,0:w].astype(np.float32)
a=np.ones((h,w),np.float32)
a*=np.clip(yy/45.0,0,1)                     # top: dust band under the mound
a*=np.clip(xx/55.0,0,1)                     # left: central longhouse edge
a*=np.clip((w-1-xx)/14.0,0,1)               # right: frame edge
a*=np.clip((h-1-yy)/40.0,0,1)               # bottom: near wall
A=a[...,None]
# colour check against the shared mound band (same content in both)
sel=patch[0:40,:,:].reshape(-1,3); ref=base[Y:Y+40,X:X+w].reshape(-1,3)
shift=np.median(ref,0)-np.median(sel,0)
patch_c=np.clip(patch+shift,0,255)
reg=base[Y:Y+h,X:X+w]
base[Y:Y+h,X:X+w]=patch_c*A+reg*(1-A)
Image.fromarray(base.astype(np.uint8)).save('work6/est_v9_p4.png')
print('shift',shift.round(1))
