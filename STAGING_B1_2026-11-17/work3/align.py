from PIL import Image
import numpy as np
ref=np.asarray(Image.open('work3/WASH_REF_ground.png').convert('RGB').resize((860,572), Image.LANCZOS)).astype(np.float32)
g=Image.open('work3/WASH_gen_ground.png').convert('RGB').resize((860,572), Image.LANCZOS)
gd=np.asarray(g).astype(np.float32)
best=None
for dy in range(-14,15,2):
    for dx in range(-14,15,2):
        sh=np.roll(np.roll(gd,dy,axis=0),dx,axis=1)
        m=np.abs(sh[80:540,80:800]-ref[80:540,80:800]).mean()
        if best is None or m<best[0]: best=(m,dx,dy)
print('coarse',best)
m0,dx0,dy0=best
for dy in range(dy0-3,dy0+4):
    for dx in range(dx0-3,dx0+4):
        sh=np.roll(np.roll(gd,dy,axis=0),dx,axis=1)
        m=np.abs(sh[80:540,80:800]-ref[80:540,80:800]).mean()
        if m<best[0]: best=(m,dx,dy)
print('fine',best)
# tone check on ground patches away from channel
dx,dy=best[1],best[2]
sh=np.roll(np.roll(gd,dy,axis=0),dx,axis=1)
for (y0,y1,x0,x1) in [(400,500,150,350),(300,400,600,780),(500,560,200,500)]:
    print('patch',(y0,x0),'ref mean',ref[y0:y1,x0:x1].mean(axis=(0,1)).round(1),'gen mean',sh[y0:y1,x0:x1].mean(axis=(0,1)).round(1))
