from PIL import Image, ImageDraw, ImageFilter
import numpy as np
B=Image.open('work4/EST_V008_moundcomp.png').convert('RGB')
G=Image.open('work4/EST_nneka_yard2.png').convert('RGB')   # 1304x800
# house + shallow ground shadow only
c=G.crop((300,80,860,560))            # 560x480
TW,TH=170,146
c=c.resize((TW,TH), Image.LANCZOS)
b=np.asarray(B).astype(np.float32); g=np.asarray(c).astype(np.float32)
bp=b[1000:1060,570:700]; gp=g[120:150,10:90]
for ch in range(3): g[:,:,ch]*= (bp[:,:,ch].mean()/gp[:,:,ch].mean())
c=Image.fromarray(np.clip(g,0,255).astype(np.uint8))
X,Y=600,905
m=Image.new('L',(TW,TH),0); d=ImageDraw.Draw(m)
d.polygon([(14,60),(40,30),(78,14),(112,12),(150,34),(166,62),(166,140),(150,144),(20,144),(12,120)],fill=255)
m=m.filter(ImageFilter.GaussianBlur(9))
out=B.copy()
out.paste(Image.composite(c,B.crop((X,Y,X+TW,Y+TH)),m),(X,Y))
out.save('work4/EST_V008_house2.png')
out.crop((470,820,1000,1169)).save('_e_house_test2.jpg',quality=92); print('ok')
