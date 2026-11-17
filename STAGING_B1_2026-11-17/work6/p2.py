from PIL import Image
import numpy as np
V8=Image.open('submit/B2_CAND_ESTABLISHING_V008_2560x1440.png').convert('RGB').crop((60,152,1961,1321))
G=Image.open('work6/yard_gen2.png').convert('RGB').resize((721,630),Image.LANCZOS)
X,Y=1180,500
base=np.array(V8,np.float32); patch=np.array(G,np.float32)
h,w,_=patch.shape
yy,xx=np.mgrid[0:h,0:w].astype(np.float32)
a=np.ones((h,w),np.float32)
a*=np.clip((yy-150)/50.0,0,1)      # top feather lands in the dust band at the mound foot
a*=np.clip(xx/60.0,0,1)            # left feather lands on the central longhouse edge
A=a[...,None]
# colour: match the model's own re-render of the shared mound band (same content, no spatial shift)
sel=patch[0:140,:,:].reshape(-1,3); ref=base[Y:Y+140,X:X+w].reshape(-1,3)
shift=np.median(ref,0)-np.median(sel,0)
patch_c=np.clip(patch+shift,0,255)
reg=base[Y:Y+h,X:X+w]
base[Y:Y+h,X:X+w]=patch_c*A+reg*(1-A)
out=Image.fromarray(base.astype(np.uint8)); out.save('work6/est_v9_p2.png')
print('shift',shift.round(1))
