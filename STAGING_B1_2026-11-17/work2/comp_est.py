from PIL import Image, ImageDraw, ImageFilter
import numpy as np

BASE = Image.open('panels/BASE_EST.png').convert('RGB')
GEN  = Image.open('work2/gen_EST_raw.png').convert('RGB')
W,H = BASE.size
G = GEN.resize((W,H), Image.LANCZOS)

# align the generation to the base using the areas it was told to leave alone
b = np.asarray(BASE.convert('L')).astype(np.float32)
g = np.asarray(G.convert('L')).astype(np.float32)
best=(1e18,0,0)
for dy in range(-18,19,2):
    for dx in range(-18,19,2):
        gg = np.roll(np.roll(g, dy, axis=0), dx, axis=1)
        reg = (slice(200,480), slice(150,900))          # hall of posts + distant plain
        d = np.abs(b[reg]-gg[reg]).mean()
        if d < best[0]: best=(d,dx,dy)
_,dx,dy = best
print('align', dx, dy, 'mean abs diff', round(best[0],2))
G = np.asarray(Image.fromarray(np.asarray(G)).transform((W,H), Image.AFFINE, (1,0,-dx,0,1,-dy), resample=Image.BICUBIC)).astype(np.float32)

# mask: the settlement mound only
poly = [(1140,700),(1128,600),(1150,520),(1120,450),(1150,370),(1150,300),(1200,215),(1290,165),
        (1400,140),(1540,132),(1660,150),(1760,190),(1820,255),(1845,330),(1835,420),(1860,500),
        (1845,580),(1855,660),(1810,715),(1700,735),(1560,715),(1420,720),(1290,715),(1180,712)]
m = Image.new('L',(W,H),0); ImageDraw.Draw(m).polygon(poly, fill=255)
m = m.filter(ImageFilter.GaussianBlur(26))
M = (np.asarray(m).astype(np.float32)/255.0)[...,None]
out = np.asarray(BASE).astype(np.float32)*(1-M) + G*M

# protect the base's own river: the generation shifted it slightly, which shows as a
# step where the mask crosses the water. Water is bright, low-saturation, blue-leaning.
bA = np.asarray(BASE).astype(np.float32)
mx = bA.max(axis=2); mn = bA.min(axis=2)
sat = (mx-mn)/np.maximum(mx,1)
water = (mx>150)&(sat<0.22)&(bA[:,:,2]>=bA[:,:,0]-6)
band = np.zeros(water.shape,bool); band[150:520, 950:1901] = True
water = water&band
wm = Image.fromarray((water*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(10))
WM = (np.asarray(wm).astype(np.float32)/255.0)[...,None]
out = out*(1-WM) + bA*WM
print('protected river px', int(water.sum()))
Image.fromarray(np.clip(out,0,255).astype(np.uint8)).save('work2/EST_V007_panel.png')
print('saved')
