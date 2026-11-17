from PIL import Image, ImageFilter
import numpy as np
new=Image.open('work6/est_v10_p1.png').convert('RGB')
orig=Image.open('work6/est_v9_p5.png').convert('RGB')
X,Y=940,40
N=np.array(new,np.float32); O=np.array(orig,np.float32)
# high-frequency detail from the original mound, transferred onto the new geometry
box=(X,Y,X+961,Y+760)
ob=orig.crop(box); ob=ob.filter(ImageFilter.GaussianBlur(2.2))
hi=O[Y:Y+760,X:X+961]-np.array(ob,np.float32)
M=np.array(Image.open('work4/EST_V008_mask.png').convert('L'),np.float32)/255.
Mi=np.array(Image.fromarray((M*255).astype(np.uint8)).filter(ImageFilter.MinFilter(41)).filter(ImageFilter.GaussianBlur(22)),np.float32)/255.
w=(Mi[...,None]*0.38)[Y:Y+760,X:X+961]
N[Y:Y+760,X:X+961]+=hi*w
# gentle local contrast restore on the replaced area
print('detail applied, mean|hi|',float(np.abs(hi).mean()).__round__(2))
Image.fromarray(np.clip(N,0,255).astype(np.uint8)).save('work6/est_v10_p2.png')
