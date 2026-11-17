from PIL import Image, ImageFilter
import numpy as np
base=Image.open('work6/est_v9_p5.png').convert('RGB')
g=Image.open('work6/mound_scale1.png').convert('RGB').resize((961,760),Image.LANCZOS)
X,Y=940,40
A=np.array(base,np.float32); B=np.array(g,np.float32)
M=np.array(Image.open('work4/EST_V008_mask.png').convert('L'),np.float32)/255.
# erode the mask so the silhouette edge stays with V009 (outline preserved by construction)
Mi=Image.fromarray((M*255).astype(np.uint8)).filter(ImageFilter.MinFilter(41)).filter(ImageFilter.GaussianBlur(22))
Mi=np.array(Mi,np.float32)/255.
# colour match generated to base inside the replaced region
sub=M[Y:Y+760,X:X+961]
reg=B[sub>0.5]; ref=A[Y:Y+760,X:X+961][sub>0.5]
shift=np.median(ref,0)-np.median(reg,0)
B=np.clip(B+shift,0,255)
a=np.zeros_like(A)
win=Mi[Y:Y+760,X:X+961][...,None]
A[Y:Y+760,X:X+961]=B*win+A[Y:Y+760,X:X+961]*(1-win)
out=Image.fromarray(np.clip(A,0,255).astype(np.uint8))
out.save('work6/est_v10_p1.png')
print('shift',shift.round(1),'mask area',int((Mi>0.5).sum()))
