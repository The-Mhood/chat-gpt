from PIL import Image, ImageDraw, ImageFilter
import numpy as np
B=Image.open('panels/BASE_EST.png').convert('RGB')
b=np.asarray(B).astype(np.float32)
# --- river protection from the base itself
r,g,bl=b[:,:,0],b[:,:,1],b[:,:,2]
lum=(r+g+bl)/3; sat=b.max(axis=2)-b.min(axis=2)
river=(lum>150)&(sat<55)
ys,xs=np.where(river)
sel=(ys>190)&(ys<470)&(xs>0)
rm=np.zeros(lum.shape,bool); rm[ys[sel],xs[sel]]=True
R=Image.fromarray((rm*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.GaussianBlur(6))
rm=np.asarray(R)>40
print('river px', int(rm.sum()), 'rows', np.where(rm.any(axis=1))[0][[0,-1]] if rm.any() else None)

# --- generous mask over old cone + new mound, bottom edge at the village band
poly=[(990,700),(1000,640),(1005,570),(1015,505),(1035,455),(1080,405),(1120,355),(1180,325),
      (1260,300),(1350,288),(1440,282),(1530,288),(1620,300),(1700,318),(1770,338),(1830,356),
      (1875,370),(1885,430),(1880,500),(1865,560),(1830,600),(1760,625),(1660,642),(1540,655),
      (1420,662),(1300,668),(1180,672),(1090,682),(1010,700)]
M=Image.new('L',B.size,0); ImageDraw.Draw(M).polygon(poly,fill=255)
# also cover the tall base apex above the new silhouette (x 1300-1700, y 130-290)
ImageDraw.Draw(M).polygon([(1290,300),(1330,180),(1400,140),(1500,132),(1600,150),(1660,210),(1690,300)],fill=255)
M=M.filter(ImageFilter.GaussianBlur(14))
mm=np.asarray(M).astype(np.float32)>128
final=mm
out=(final*255).astype(np.uint8)
Image.fromarray(out).save('work4/EST_V008_mask.png')
print('mask px', int(final.sum()))
# visualisation
vis=np.asarray(B).copy(); vis[final]= (vis[final]*0.35+np.array([0,180,255])*0.65).astype(np.uint8)
Image.fromarray(vis).resize((950,584)).save('_e_maskvis.jpg',quality=90)
