from PIL import Image, ImageDraw, ImageFilter
import numpy as np

BASE = Image.open('panels/BASE_WALL.png').convert('RGB')
GEN  = Image.open('work2/gen_WALL_raw.png').convert('RGB')
W,H = BASE.size
G = GEN.resize((W,H), Image.LANCZOS)

b = np.asarray(BASE.convert('L')).astype(np.float32)
g = np.asarray(G.convert('L')).astype(np.float32)
best=(1e18,0,0)
for dy in range(-16,17,2):
    for dx in range(-16,17,2):
        gg = np.roll(np.roll(g, dy, axis=0), dx, axis=1)
        reg = (slice(0,150), slice(0,W))        # sky / mist band, untouched by both
        d = np.abs(b[reg]-gg[reg]).mean()
        if d < best[0]: best=(d,dx,dy)
_,dx,dy = best
print('align', dx, dy, round(best[0],2))
G = np.asarray(Image.fromarray(np.asarray(G)).transform((W,H), Image.AFFINE, (1,0,-dx,0,1,-dy), resample=Image.BICUBIC)).astype(np.float32)

# mask: the built mound, keeping the misty sky and the frame edges
poly = [(60,900),(48,780),(70,660),(60,540),(85,430),(80,330),(120,245),(220,190),
        (380,160),(560,140),(760,132),(980,138),(1180,150),(1360,170),(1520,200),
        (1660,250),(1760,320),(1815,410),(1840,520),(1830,640),(1845,760),(1820,880),
        (1770,975),(1660,1035),(1500,1060),(1300,1058),(1080,1062),(880,1058),(700,1050),
        (520,1040),(330,1020),(180,975),(90,950)]
m = Image.new('L',(W,H),0); ImageDraw.Draw(m).polygon(poly, fill=255)
m = m.filter(ImageFilter.GaussianBlur(30))
M = (np.asarray(m).astype(np.float32)/255.0)[...,None]
out = np.asarray(BASE).astype(np.float32)*(1-M) + G*M
Image.fromarray(np.clip(out,0,255).astype(np.uint8)).save('work2/WALL_V005_panel.png')
print('saved; masked px', int((np.asarray(m)>127).sum()))
