from PIL import Image
import numpy as np, hashlib, json

M = 'masters/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005.jpg'
print('V005 master md5', hashlib.md5(open(M,'rb').read()).hexdigest(), '(expect a94a084af0f7fb6d8016a6e33d44dc62)')
V5 = np.asarray(Image.open(M).convert('RGB').crop((60,152,1961,1321))).astype(int)

MASKS = {                      # panel coords, the only regions authorised to change
 'A fracture': (425,512,528,862),
 'B midriff' : (852,614,1000,764),
 'C armlet'  : (996,533,1080,632),
}
INVARIANTS = {                 # must be untouched
 'face + head'      : (650,330,830,570),
 'braids + cuffs'   : (620,290,840,430),
 'right arm + hand' : (410,370,640,580),
 'seal panel'       : (250,300,560,900),
 'bowl + pot'       : (280,860,580,1100),
 'skirt + belt'     : (800,740,1010,1160),
 'right-side huts'  : (1200,180,1900,1120),
}

def audit(path, label):
    A = np.asarray(Image.open(path).convert('RGB')).astype(int)
    P = A[152:1321, 60:1961]
    d = (np.abs(P-V5).sum(axis=2) > 12)
    cov = np.zeros(d.shape, bool); out={}
    for k,(x0,y0,x1,y1) in MASKS.items():
        cov[y0:y1,x0:x1]=True; out[k]=int(d[y0:y1,x0:x1].sum())
    out['outside masks']=int((d&~cov).sum()); out['total']=int(d.sum())
    print(f'\n[{label}] size={A.shape[1]}x{A.shape[0]}  changed={out["total"]}  '
          f'fracture={out["A fracture"]} midriff={out["B midriff"]} armlet={out["C armlet"]}  '
          f'OUTSIDE={out["outside masks"]}')
    for k,(x0,y0,x1,y1) in INVARIANTS.items():
        n=int(d[y0:y1,x0:x1].sum())
        print(f'   invariant {k:18s} {n} px  {"OK" if n==0 else "<-- CHANGED"}')
    return out, P

o7,_ = audit('final/CAND_VR-008_V007_2560x1440.png','V007')
o8,P8 = audit('final/CAND_VR-008_V008_2560x1440.png','V008')

A7 = np.asarray(Image.open('final/CAND_VR-008_V007_2560x1440.png').convert('RGB')).astype(int)[152:1321,60:1961]
d = (np.abs(P8-A7).sum(axis=2) > 12)
ys,xs = np.where(d)
x0,y0,x1,y1 = MASKS['C armlet']
inside = int(d[y0:y1,x0:x1].sum())
print(f'\n[V007 -> V008] changed={int(d.sum())}  inside armlet mask={inside}  outside={int(d.sum())-inside}  bbox=({xs.min()},{ys.min()})-({xs.max()},{ys.max()})')
json.dump({'V007':o7,'V008':o8,'v7_to_v8':{'total':int(d.sum()),'inside':inside}}, open('work2/v008_diffstats.json','w'), indent=1)
