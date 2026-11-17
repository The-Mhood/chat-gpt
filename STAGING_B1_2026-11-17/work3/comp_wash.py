from PIL import Image, ImageFilter, ImageDraw
import numpy as np

REF='work3/WASH_REF_ground.png'; GEN='work3/WASH_gen_ground.png'
MASTER='masters/ENV_HOME_SETTLEMENT_WASHING_PLACE_V002.jpg'
BOX=(760,520,1620,1092)           # crop origin in panel coords
CW,CH=860,572

panel=Image.open(MASTER).convert('RGB').crop((60,152,1960,1244))
ref=Image.open(REF).convert('RGB')
gen=Image.open(GEN).convert('RGB').resize((CW,CH), Image.LANCZOS)

# --- tone match on ground patches away from the drain corridor
g=np.asarray(gen).astype(np.float32); r=np.asarray(ref).astype(np.float32)
px=(slice(380,560),slice(60,340))          # plain earth, left-bottom of crop
for c in range(3):
    gm=g[px][:,:,c].mean(); rm=r[px][:,:,c].mean()
    g[:,:,c]*= (rm/gm)
g=np.clip(g,0,255)
gen=Image.fromarray(g.astype(np.uint8))

# --- corridor mask (feathered)
# centreline measured on the V002 master (panel coords minus crop origin)
centre=[(425,132),(455,180),(490,206),(522,230),(548,254),(573,278),(597,302),(613,328),
        (630,352),(653,374),(650,398),(650,422),(655,446),(650,470),(626,494),(626,518),
        (610,542),(606,572)]
def band(pts, half):
    left=[];right=[]
    for i,(x,y) in enumerate(pts):
        x0,y0=pts[max(0,i-1)]; x1,y1=pts[min(len(pts)-1,i+1)]
        dx,dy=x1-x0,y1-y0; L=max((dx*dx+dy*dy)**0.5,1e-6)
        nx,ny=-dy/L,dx/L
        left.append((x-nx*half, y-ny*half)); right.append((x+nx*half, y+ny*half))
    return left+right[::-1]
poly=band(centre,46)
m=Image.new('L',(CW,CH),0); ImageDraw.Draw(m).polygon([(max(0,min(CW-1,int(a))),max(0,min(CH-1,int(b)))) for a,b in poly], fill=255)
m=m.filter(ImageFilter.GaussianBlur(22))
mp=np.asarray(m).astype(np.float32)[:,:,None]/255.0

comp=Image.composite(gen, ref, Image.fromarray((mp[:,:,0]*255).astype(np.uint8)))
panel.paste(comp, (BOX[0],BOX[1]))
panel.save('work3/WASH_V004_panel.png')
stats={'mask_px':int((mp[:,:,0]>0.02).sum()),'hard_px':int((mp[:,:,0]>0.5).sum()),
       'tone_patch_ref':r[px].mean(axis=(0,1)).round(1).tolist(),
       'tone_patch_gen_after':g[px].mean(axis=(0,1)).round(1).tolist()}
print(stats)
import json; json.dump(stats, open('work3/wash_stats.json','w'), indent=1)
