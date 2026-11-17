from PIL import Image, ImageFilter, ImageDraw
import numpy as np, json

def audit(base_path, cand_path, poly, chrome_rects, label):
    B = Image.open(base_path).convert('RGB'); C = Image.open(cand_path).convert('RGB')
    b = np.asarray(B).astype(int); c = np.asarray(C).astype(int)
    d = (np.abs(b-c).sum(axis=2) > 12)
    # mask = polygon + feather 32 to give the soft seam its allowance
    W,H = B.size
    m = Image.new('L',(W,H),0); ImageDraw.Draw(m).polygon(poly, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(60))
    mm = (np.asarray(m).astype(np.float32) > 0.5)
    art = np.zeros(d.shape, bool); art[152:1321, 60:1961] = True
    inside = d & art & mm
    outside = d & ~(art & mm)
    for (x0,y0,x1,y1) in chrome_rects:
        outside[y0:y1, x0:x1] = False
    print(f'[{label}] total changed {int(d.sum()):,} | artwork inside mask {int(inside.sum()):,} | outside mask+chrome {int(outside.sum())}')
    if outside.sum():
        ys,xs=np.where(outside); print('   stray bbox', xs.min(),ys.min(),xs.max(),ys.max())
    # red-mark check on the finished frame
    r,g,bl = c[:,:,0],c[:,:,1],c[:,:,2]
    red = (r>150)&(r-g>90)&(r-bl>90)&(g<80)
    print(f'   saturated red pixels in artwork panel: {int(red[152:1321,60:1961].sum())}')
    return {'total':int(d.sum()),'inside_mask':int(inside.sum()),'outside':int(outside.sum()),'red':int(red[152:1321,60:1961].sum())}

EST_POLY = [(1140,700),(1128,600),(1150,520),(1120,450),(1150,370),(1150,300),(1200,215),(1290,165),
        (1400,140),(1540,132),(1660,150),(1760,190),(1820,255),(1845,330),(1835,420),(1860,500),
        (1845,580),(1855,660),(1810,715),(1700,735),(1560,715),(1420,720),(1290,715),(1180,712)]
WALL_POLY = [(60,900),(48,780),(70,660),(60,540),(85,430),(80,330),(120,245),(220,190),
        (380,160),(560,140),(760,132),(980,138),(1180,150),(1360,170),(1520,200),
        (1660,250),(1760,320),(1815,410),(1840,520),(1830,640),(1845,760),(1820,880),
        (1770,975),(1660,1035),(1500,1060),(1300,1058),(1080,1062),(880,1058),(700,1050),
        (520,1040),(330,1020),(180,975),(90,950)]
# polygons are in panel coords; shift to frame coords
def sh(p): return [(x+60,y+152) for x,y in p]

CHROME = [(2476,28,2512,70),(1980,664,2560,1104),(1990,306,2560,358)]
r1 = audit('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg','final/CAND_ESTABLISHING_V007_2560x1440.png', sh(EST_POLY), CHROME, 'EST V007')
r2 = audit('masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_WALL_OF_HOUSES_V003.jpg','final/CAND_WALL_OF_HOUSES_V005_2560x1440.png', sh(WALL_POLY), CHROME, 'WALL V005')
json.dump({'EST':r1,'WALL':r2}, open('work2/env_diffstats.json','w'), indent=1)
