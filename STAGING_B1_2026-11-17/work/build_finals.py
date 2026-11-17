from PIL import Image, ImageDraw, ImageFilter
import numpy as np, json, random, hashlib, os

BOX = (60,152,1961,1321)          # verified identical on all eight masters
PW, PH = BOX[2]-BOX[0], BOX[3]-BOX[1]   # 1901 x 1169
random.seed(4242)

def upscale(p):
    im = Image.open(p).convert('RGB')
    return im.resize((PW,PH), Image.LANCZOS)

def remove_figure(panel):
    """Patch out the stray standing figure in the Establishing candidate.
    Region is smooth mud wall + yard floor, so a row-wise horizontal
    interpolation across the gap plus grain re-injection is sufficient."""
    a = np.asarray(panel).astype(np.float32)
    x0,x1,y0,y1 = 596,646,848,928
    out = a.copy()
    rnd = random.Random(5)
    for y in range(y0,y1):
        left = a[y, x0-6:x0].mean(axis=0)
        right= a[y, x1:x1+6].mean(axis=0)
        n = x1-x0
        for i in range(n):
            t=i/(n-1)
            base = left*(1-t)+right*t
            jitter = np.array([rnd.gauss(0,2.2) for _ in range(3)])
            out[y, x0+i] = base + jitter
    # feather the patch edges
    m = np.zeros((PH,PW), np.float32)
    m[y0:y1, x0:x1] = 1.0
    m = np.asarray(Image.fromarray((m*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(5))).astype(np.float32)/255.0
    res = a*(1-m[...,None]) + out*m[...,None]
    return Image.fromarray(np.clip(res,0,255).astype(np.uint8))

JOBS = [
 ('VR-008','COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005', 'work/VR-008_crack_panel_v2.png', None),
 ('VR-010','ENV_HOME_SETTLEMENT_WASHING_PLACE_V002', 'cand_panels/CAND_VR-010_WASHING_PLACE_V003_PANEL.jpg', None),
 ('VR-011','ENV_GATES_DEAD_LANDING_OF_UNCLAIMED_V001', 'cand_panels/CAND_VR-011_LANDING_V002_PANEL.jpg', None),
 ('ESTABLISHING','ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005', 'cand_panels/CAND_ESTABLISHING_V006_PANEL.jpg', 'figure'),
 ('WALL_OF_HOUSES','ENV_LAST_DAUGHTER_ANCESTRAL_REALM_WALL_OF_HOUSES_V003', 'cand_panels/CAND_WALL_OF_HOUSES_V004_PANEL.jpg', None),
]

rep=[]
for tag, master, candpath, extra in JOBS:
    base = Image.open(f'masters/{master}.jpg').convert('RGB')
    panel = upscale(candpath)
    if extra=='figure':
        panel = remove_figure(panel)
    panel.save(f'final/PANEL_{tag}_CAND.png')
    out = base.copy()
    out.paste(panel, (BOX[0],BOX[1]))
    outname = f'final/CAND_{tag}_2560x1440.png'
    out.save(outname)
    # prove nothing outside the box changed
    a=np.asarray(base).astype(np.int16); b=np.asarray(out).astype(np.int16)
    d=np.abs(a-b).sum(axis=2)
    mask=np.ones_like(d,dtype=bool); mask[BOX[1]:BOX[3], BOX[0]:BOX[2]]=False
    rep.append((tag, outname, out.size, int(d.max()), int(d[mask].max()), int((d[mask]>0).sum())))
    print(f'{tag:14s} {outname} {out.size} maxdiff_in={d.max()} maxdiff_outside={d[mask].max()} px_changed_outside={(d[mask]>0).sum()}')
json.dump(rep, open('final/_diffreport.json','w'), indent=1)
