from PIL import Image, ImageFilter, ImageDraw
import numpy as np
SRC='submit/B2_CAND_VR-008_SEALED_QUARTER_V008_2560x1440.png'
full=Image.open(SRC).convert('RGB')
A=np.array(full,np.float32)
CX0,CY0,CX1,CY1=960,520,1200,780
gen=Image.open('work_pauldron_fix.png').convert('RGB').resize((CX1-CX0,CY1-CY0),Image.LANCZOS)
G=np.array(gen,np.float32)
base=A[CY0:CY1,CX0:CX1]
# colour match on the surrounding skin/hair band (exclude the footprint itself)
band=np.zeros(base.shape[:2],bool); band[0:40,:]=True; band[200:260,:]=True; band[:,0:30]=True; band[:,210:240]=True
sh=np.median(base[band],0)-np.median(G[band],0)
G=np.clip(G+sh,0,255)
print('shift',sh.round(1))
# footprint: the metal cap only
m=Image.new('L',(CX1-CX0,CY1-CY0),0)
fx0,fy0,fx1,fy1=1012-CX0,562-CY0,1152-CX0,698-CY0
ImageDraw.Draw(m).rounded_rectangle([fx0,fy0,fx1,fy1],radius=26,fill=255)
mk=np.array(m.filter(ImageFilter.GaussianBlur(10)),np.float32)[...,None]/255.
out=base*mk+G*(1-mk)   # careful: mk=1 keeps ORIGINAL only where feather=1 -> we want replace, so invert below
out=G*mk+base*(1-mk)
A[CY0:CY1,CX0:CX1]=out
Image.fromarray(np.clip(A,0,255).astype(np.uint8)).save('work3/vr008_v9_panel_full.png')
print('ok')
