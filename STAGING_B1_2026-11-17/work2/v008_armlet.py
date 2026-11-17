from PIL import Image, ImageDraw, ImageFilter
import numpy as np

V5 = Image.open('masters/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005.jpg').convert('RGB').crop((60,152,1961,1321))
V7 = Image.open('work2/V007_panel.png').convert('RGB')
REF = Image.open('refs/CHAR_ADANNA_MASTER_REFERENCE_V001.jpg').convert('RGB')

base = np.asarray(V7).astype(np.float32)
v5   = np.asarray(V5).astype(np.float32)
W,H  = V5.size

# 1. remove the painted V007 armlet: restore the master's own pixels there
OLD = (995,533,1079,632)
out = base.copy()
out[OLD[1]:OLD[3], OLD[0]:OLD[2]] = v5[OLD[1]:OLD[3], OLD[0]:OLD[2]]

# 2. cut the armlet out of the approved character master
c = REF.crop((580,1010,800,1140)).rotate(-7.6, resample=Image.BICUBIC, expand=True)
strip = c.crop((45,46,200,110))                # 155 x 64, coils now level
BW, BH = 74, 29
strip = strip.resize((BW,BH), Image.LANCZOS)

# 3. grade it to the overcast light of this scene: match the arm's local luminance
arm_patch = v5[585:605, 1016:1052]
arm_mean  = float(arm_patch.mean())
s = np.asarray(strip).astype(np.float32)
s_mean = float(s.mean())
target = arm_mean * 0.86                     # dull metal in shade, not a highlight
s = s * (target/max(s_mean,1e-6))
s = np.clip(s,0,255)

# 4. place it on the arm, following the arm's curvature
img = out.copy()
x0, y0 = 999, 551
xx = np.arange(BW, dtype=np.float32)[None,:]
bow = 2.6*((2*xx/(BW-1)-1)**2)               # ring dips at the silhouette edges
alpha = np.ones((BH,BW), np.float32)
edge_x = np.minimum(np.arange(BW), BW-1-np.arange(BW)).astype(np.float32)
alpha *= np.clip(edge_x/6.0, 0, 1)[None,:]**1.3   # fade where the arm turns away
edge_y = np.minimum(np.arange(BH), BH-1-np.arange(BH)).astype(np.float32)
alpha *= np.clip(edge_y/2.5, 0, 1)[:,None]

for j in range(BH):
    dy = int(round(bow[0,j]))
    a = alpha[j][:,None]
    img[y0+j, x0:x0+BW] = img[y0+j, x0:x0+BW]*(1-a) + s[j]*a

# 5. a little occlusion so it sits in the arm instead of on top of it
ao = Image.new('L',(W,H),0); d=ImageDraw.Draw(ao)
d.rectangle([x0-2, y0-3, x0+BW+2, y0-1], fill=150)
d.rectangle([x0-2, y0+BH, x0+BW+2, y0+BH+3], fill=150)
ao = np.asarray(ao.filter(ImageFilter.GaussianBlur(1.6))).astype(np.float32)/255.0
img = img*(1-ao[...,None]*0.45)

Image.fromarray(np.clip(img,0,255).astype(np.uint8)).save('work2/V008_panel.png')
print('saved panel; arm mean %.1f, source mean %.1f -> target %.1f' % (arm_mean, s_mean, target))

# diff v V005 and v V007
a1 = np.asarray(Image.open('work2/V008_panel.png')).astype(int)
d5 = (np.abs(a1-v5.astype(int)).sum(axis=2) > 12)
d7 = (np.abs(a1-np.asarray(V7).astype(int)).sum(axis=2) > 12)
print('vs V005 changed px', int(d5.sum()), ' vs V007 changed px', int(d7.sum()))
ys,xs = np.where(d7); print('V007->V008 bbox', xs.min(), ys.min(), xs.max(), ys.max())
