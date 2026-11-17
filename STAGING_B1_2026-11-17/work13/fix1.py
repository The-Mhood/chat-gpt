"""EST V013 step 1 — measurable fixes (V013 brief item 1).

(a) kill the cyan/blue margin bleed below the frame (y 1246-1290)
(b) re-warm the lower-right foreground mud wall to the approved V005 daylight
"""
from PIL import Image, ImageFilter
import numpy as np

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/'
im = Image.open(S + 'work13/B2_CAND_ESTABLISHING_V012_2560x1440.png').convert('RGB')
a = np.array(im).astype(np.float32)
W = a.shape[1]

ART_TOP, ART_BOT = 176, 1245          # measured: bright rule at 152, art 176-1245
rowmean = a[:, 100:1900].mean(axis=(1, 2))
assert rowmean[ART_BOT] > 40 and rowmean[ART_BOT + 5] < 20, (rowmean[ART_BOT], rowmean[ART_BOT + 5])
print('art rows', ART_TOP, ART_BOT)

# ---- 1a. wall warmth -------------------------------------------------------
x0, x1 = 1400, 1958
y0, y1 = 1140, ART_BOT + 1
reg = a[y0:y1, x0:x1].copy()
L = reg @ np.array([0.299, 0.587, 0.114], np.float32)
blur = np.array(Image.fromarray(reg.astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))).astype(np.float32)
detail = reg - blur
ramp = np.stack([46 + 0.42 * L, 15 + 0.13 * L, 6 + 0.07 * L], -1)
new = ramp + detail * 0.55
new = np.maximum(new, np.array([26, 8, 3], np.float32))
h, w = L.shape
mx = np.clip(np.arange(w) / 70.0, 0, 1)
my = np.clip(np.arange(h) / 55.0, 0, 1)
m = ((my[:, None] * mx[None, :]) ** 0.9)[..., None] * 0.92
a[y0:y1, x0:x1] = reg * (1 - m) + new * m

# ---- 1b. margin bleed ------------------------------------------------------
m0, m1 = ART_BOT + 2, 1315
clean = a[m0:m1, 60:520]
row_med = np.median(clean, axis=1)
row_med = np.array(Image.fromarray(row_med[:, None, :].astype(np.uint8).repeat(4, 1))
                   .filter(ImageFilter.GaussianBlur(3)))[:, 0, :].astype(np.float32)
a[m0:m1, :] = row_med[:, None, :]

out = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
out.save(S + 'work13/step1.png')

b = np.array(out).astype(int)
def px(x, y): return tuple(int(v) for v in b[y, x])
print('bleed gone?  y1250 R', px(1900, 1250), 'L', px(300, 1250),
      '| y1270 R', px(1900, 1270), 'L', px(300, 1270))
for y in (1210, 1225, 1240):
    print('wall y', y, px(1700, y), px(1800, y), px(1900, y))
