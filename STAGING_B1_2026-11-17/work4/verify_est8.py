from PIL import Image, ImageFilter
import numpy as np, json
B=Image.open('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg').convert('RGB')
C=Image.open('final/CAND_ESTABLISHING_V008_2560x1440.png').convert('RGB')
b=np.asarray(B).astype(int); c=np.asarray(C).astype(int)
d=(np.abs(b-c).sum(axis=2)>12)
M=Image.open('work4/EST_V008_mask.png').convert('L').filter(ImageFilter.GaussianBlur(30))
mm=np.zeros(d.shape,bool); mm[152:1321,60:1961]=np.asarray(M).astype(np.float32)>0.5
outside=d&~mm
for (x0,y0,x1,y1) in [(2476,28,2512,70),(1980,262,2560,362),(1980,670,2560,1064)]:
    outside[y0:y1,x0:x1]=False
res={'total':int(d.sum()),'in_mask':int((d&mm).sum()),'outside':int(outside.sum())}
if outside.sum():
    ys,xs=np.where(outside); res['stray_bbox']=[int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())]
# anchors
for name,(x0,y0,x1,y1) in [('Hall of Posts',(210,402,820,672)),('foreground compound',(440,912,880,1232)),
                           ('sky/inverted settlement',(60,152,1961,282)),('frame bottom',(60,1252,1961,1321))]:
    res[name]=int((np.abs(b[y0:y1,x0:x1]-c[y0:y1,x0:x1]).sum(axis=2)>0).sum())
print(json.dumps(res,indent=1)); json.dump(res,open('work4/est8_stats.json','w'),indent=1)
