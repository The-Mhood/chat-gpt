from PIL import Image
import numpy as np
B=Image.open('panels/BASE_EST.png').convert('RGB')
G=Image.open('work4/EST_V008_mound.png').convert('RGB').resize((1901,1169), Image.LANCZOS)
G.save('work4/EST_V008_mound_up.png')
b=np.asarray(B).astype(np.float32); g=np.asarray(G).astype(np.float32)
g0=g.copy()
best=None
for dy in range(-24,25,3):
    for dx in range(-24,25,3):
        sh=np.roll(np.roll(g0,dy,axis=0),dx,axis=1)
        m=np.abs(sh[150:900,200:1100]-b[150:900,200:1100]).mean()
        if best is None or m<best[0]: best=(m,dx,dy)
m0,dx0,dy0=best
for dy in range(dy0-3,dy0+4):
    for dx in range(dx0-3,dx0+4):
        sh=np.roll(np.roll(g0,dy,axis=0),dx,axis=1)
        mm=np.abs(sh[150:900,200:1100]-b[150:900,200:1100]).mean()
        if mm<best[0]: best=(mm,dx,dy)
print('best',best)
open('work4/align.txt','w').write(f'{best[1]} {best[2]} {best[0]:.3f}')
