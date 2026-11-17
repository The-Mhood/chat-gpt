from PIL import Image, ImageFilter
import numpy as np, json
B=Image.open('panels/BASE_EST.png').convert('RGB')
G=Image.open('work4/EST_V008_mound_up.png').convert('RGB')
dx,dy=[int(v) for v in open('work4/align.txt').read().split()[:2]]
G=np.roll(np.roll(np.asarray(G),dy,axis=0),dx,axis=1)
G=Image.fromarray(G)
# tone: match render to base on plain sky+mist patches outside the mound
b=np.asarray(B).astype(np.float32); g=np.asarray(G).astype(np.float32)
px=(slice(430,560),slice(300,900))   # distant misty village band, left of mound
for c in range(3):
    gm=g[px][:,:,c].mean(); bm=b[px][:,:,c].mean(); g[:,:,c]*= (bm/gm)
g=np.clip(g,0,255); G=Image.fromarray(g.astype(np.uint8))
M=Image.open('work4/EST_V008_mask.png').convert('L').filter(ImageFilter.GaussianBlur(24))
out=Image.composite(G,B,M)
# photographic-grain transfer: add V005's own high-frequency detail inside the mask
import numpy as _np
from PIL import ImageFilter as _IF
base=_np.asarray(G).astype(_np.float32)
soft=_np.asarray(G.filter(_IF.GaussianBlur(1.6))).astype(_np.float32)
detail=base-soft
comp=_np.asarray(out).astype(_np.float32)
mw=(_np.asarray(M).astype(_np.float32)/255.0)[:,:,None]
comp=_np.clip(comp+0.85*detail*mw,0,255)
out=Image.fromarray(comp.astype(_np.uint8))
print('grain transfer applied')
out.save('work4/EST_V008_moundcomp.png')
print('done', json.dumps({'dx':dx,'dy':dy}))
