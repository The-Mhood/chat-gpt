from PIL import Image, ImageDraw, ImageFilter
import numpy as np
B=Image.open('masters/ENV_HOME_SETTLEMENT_WASHING_PLACE_V002.jpg').convert('RGB')
C=Image.open('final/CAND_VR-010_WASHING_PLACE_V004_2560x1440.png').convert('RGB')
b=np.asarray(B).astype(int); c=np.asarray(C).astype(int)
d=(np.abs(b-c).sum(axis=2)>12)
# corridor mask in panel coords -> frame coords
centre=[(425,132),(455,180),(490,206),(522,230),(548,254),(573,278),(597,302),(613,328),(630,352),(653,374),
        (650,398),(650,422),(655,446),(650,470),(626,494),(626,518),(610,542),(606,572)]
def band(pts,half):
    L=[];R=[]
    for i,(x,y) in enumerate(pts):
        x0,y0=pts[max(0,i-1)]; x1,y1=pts[min(len(pts)-1,i+1)]
        dx,dy=x1-x0,y1-y0; n=max((dx*dx+dy*dy)**.5,1e-6)
        nx,ny=-dy/n,dx/n
        L.append((x-nx*half+760+60,y-ny*half+520+152)); R.append((x+nx*half+760+60,y+ny*half+520+152))
    return L+R[::-1]
m=Image.new('L',B.size,0)
ImageDraw.Draw(m).polygon([(int(a),int(bb)) for a,bb in band(centre,60)], fill=255)
m=m.filter(ImageFilter.GaussianBlur(45)); mm=np.asarray(m).astype(np.float32)>0.5
outside=d&~mm
for (x0,y0,x1,y1) in [(1884,30,2514,64),(1992,424,2548,540),(1992,564,2548,684),(976,1330,1980,1440)]:
    outside[y0:y1,x0:x1]=False
print('total changed', int(d.sum()), '| in corridor mask', int((d&mm).sum()), '| outside mask+chrome', int(outside.sum()))
if outside.sum():
    ys,xs=np.where(outside); print(' stray bbox', xs.min(),ys.min(),xs.max(),ys.max())
# prove the protected V002 elements are untouched
for name,(x0,y0,x1,y1) in [('stone slab',(140,600,1240,1000)),('pots+ladle',(60,560,560,860)),
                           ('leaf+sticks+straw',(200,860,760,1244)),('screens above',(200,152,1940,560)),
                           ('left mud wall',(60,152,140,1244))]:
    dd=(np.abs(b[y0:y1,x0:x1]-c[y0:y1,x0:x1]).sum(axis=2)>0).sum()
    print(f'  {name:20s} changed px = {dd}')
