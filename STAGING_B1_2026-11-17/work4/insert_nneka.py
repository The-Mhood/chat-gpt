from PIL import Image, ImageDraw, ImageFilter
import numpy as np
B=Image.open('work4/EST_V008_moundcomp.png').convert('RGB')
G=Image.open('work4/EST_nneka_yard2.png').convert('RGB')
# crop the house + its own yard from the render
c=G.crop((255,55,905,600))          # 650x545
TW,TH=300,252
c=c.resize((TW,TH), Image.LANCZOS)
# tone match to the base courtyard floor
b=np.asarray(B).astype(np.float32); g=np.asarray(c).astype(np.float32)
bp=b[1040:1130,600:760]             # base courtyard floor patch
gp=g[190:250,20:140]                # render's own floor patch
for ch in range(3):
    g[:,:,ch]*= (bp[:,:,ch].mean()/gp[:,:,ch].mean())
g=np.clip(g,0,255)
c=Image.fromarray(g.astype(np.uint8))
X,Y=608,872
# feathered rectangular mask, softer at bottom (ground merge)
m=Image.new('L',(TW,TH),0); d=ImageDraw.Draw(m)
d.rectangle([10,6,TW-10,TH-4],fill=255)
m=m.filter(ImageFilter.GaussianBlur(26))
out=B.copy()
layer=Image.new('RGB',(TW,TH),(0,0,0))
out.paste(Image.composite(c,B.crop((X,Y,X+TW,Y+TH)),m),(X,Y))
out.save('work4/EST_V008_house.png')
out.crop((470,820,1000,1169)).save('_e_house_test.jpg',quality=92)
print('ok')
