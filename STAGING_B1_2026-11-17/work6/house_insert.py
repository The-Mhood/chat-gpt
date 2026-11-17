from PIL import Image, ImageDraw, ImageFilter
import numpy as np

BASE=Image.open('work6/est_v9_p2.png').convert('RGB')
PL=Image.open('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_NNEKAS_HOUSE_V004.jpg').convert('RGB')

# ---- house source (plate coords)
hx0,hy0,hx1,hy1=560,520,1340,1010
hs=PL.crop((hx0,hy0,hx1,hy1))
poly_plate=[(615,800),(706,626),(1080,556),(1185,572),(1302,782),(1312,996),(612,996)]
poly=[(x-hx0,y-hy0) for x,y in poly_plate]

matte=Image.new('L',hs.size,0); ImageDraw.Draw(matte).polygon(poly,fill=255)
matte=matte.filter(ImageFilter.GaussianBlur(2.0))

# warm grade (plate is cold mist; scene is warm dust)
a=np.array(hs,np.float32)
a[...,0]*=1.16; a[...,1]*=1.03; a[...,2]*=0.76
m=a.mean(2,keepdims=True); a=np.clip((a-m)*1.06+m,0,255)
hs_w=Image.fromarray(a.astype(np.uint8))

TW,TH=220,110
hs_w=hs_w.resize((TW,int(hs_w.size[1]*TW/hs_w.size[0])),Image.LANCZOS)
matte=matte.resize(hs_w.size,Image.LANCZOS)
hs_w=hs_w.resize((TW,TH),Image.LANCZOS)
matte=matte.resize((TW,TH),Image.LANCZOS)
HX,HY=1300,742

# ---- plot ground + stakes
px0,py0,px1,py1=500,1005,1600,1180
ps=PL.crop((px0,py0,px1,py1))
b=np.array(ps,np.float32)
b[...,0]*=1.16; b[...,1]*=1.03; b[...,2]*=0.76
ps_w=Image.fromarray(np.clip(b,0,255).astype(np.uint8))
PW=352; PH=56
ps_w=ps_w.resize((PW,PH),Image.LANCZOS)
QX,QY=1245,878
pmask=Image.new('L',(PW,PH),0)
pm=ImageDraw.Draw(pmask); pm.rectangle([0,0,PW,PH],fill=255)
pmask=pmask.filter(ImageFilter.GaussianBlur(6))

out=BASE.copy()
# contact shadow under house
sh=Image.new('L',BASE.size,0); ds=ImageDraw.Draw(sh)
ds.ellipse([HX-14,HY+TH-26,HX+TW+16,HY+TH+16],fill=110)
sh=sh.filter(ImageFilter.GaussianBlur(16))
out=Image.composite(Image.new('RGB',BASE.size,(28,16,10)),out,sh)
out.paste(ps_w,(QX,QY),pmask)
out.paste(hs_w,(HX,HY),matte)
out.save('work6/est_v9_p3.png')
print('house at',HX,HY,'plot at',QX,QY)
