"""EST V013 step 2 — composite the bounded house re-render back into the plate.

The patch region is pasted through a feathered mask and matched to the host
colour on a border ring that excludes the changed content.
"""
from PIL import Image, ImageFilter, ImageDraw
import numpy as np

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/work13/'
base = Image.open(S + 'step1.png').convert('RGB')
patch = Image.open(S + 'patch_house_new.png').convert('RGB').resize((440, 300), Image.LANCZOS)
X0, Y0 = 1240, 850

b = np.array(base).astype(np.float32)
p = np.array(patch).astype(np.float32)

# colour match on a 14 px border ring (unchanged content on both sides)
ring = np.zeros(p.shape[:2], bool)
ring[:14] = ring[-14:] = True
ring[:, :14] = ring[:, -14:] = True
host = b[Y0:Y0 + 300, X0:X0 + 440][ring]
delta = np.median(host - p[ring], 0)
p = np.clip(p + delta, 0, 255)
print('colour delta', delta.round(1))

mask = Image.new('L', (440, 300), 0)
ImageDraw.Draw(mask).rectangle((16, 16, 440 - 16, 300 - 16), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(14))

base.paste(Image.fromarray(p.astype(np.uint8)), (X0, Y0), mask)
base.save(S + 'step2.png')

# seam check: max absolute step across the patch border
c = np.array(base).astype(int)
for x in (X0, X0 + 439):
    d = np.abs(c[Y0:Y0 + 300, x + 1] - c[Y0:Y0 + 300, x]).max()
    print('vertical seam at x', x, d)
for y in (Y0, Y0 + 299):
    d = np.abs(c[y + 1, X0:X0 + 440] - c[y, X0:X0 + 440]).max()
    print('horizontal seam at y', y, d)
