"""V003 step 1 — remove the mutated bronze medallion hanging off the armlet.

Bounded, deterministic: the medallion is located as the bronze blob below the
coil band, then replaced with arm skin cloned down-shifted from the same limb and
feathered so the coil band itself is untouched.
"""
from PIL import Image, ImageFilter
import numpy as np

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/turnv3/'
# search window per view: (x0, y0, x1, y1) around the medallion
WIN = {'FRONT': (1163, 512, 1216, 572),
       'LEFT_SIDE': (1103, 493, 1162, 548),
       'BACK': (918, 505, 968, 556),
       'THREE_QUARTER': (948, 512, 1000, 572)}
SHIFT = 34          # clone source offset (down the limb)
PAD = 6


def bronze(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (r > 55) & (g > 38) & (b < 120) & (r - b > 18) & (r - g > 6)


def fix(view):
    im = Image.open(S + f'CAND_CHAR_ADANNA_TURNAROUND_{view}_V002_2560x1440.png').convert('RGB')
    a = np.array(im).astype(np.float32)
    x0, y0, x1, y1 = WIN[view]
    win = a[y0:y1, x0:x1]
    m = bronze(win.astype(int))
    ys, xs = np.where(m)
    if len(xs) == 0:
        print(view, 'no medallion found'); return
    bx0, bx1 = xs.min() + x0, xs.max() + x0
    by0, by1 = ys.min() + y0, ys.max() + y0
    print(view, 'medallion bbox', bx0, by0, bx1, by1, 'px', len(xs))

    X0, Y0 = bx0 - PAD, by0 - PAD
    X1, Y1 = bx1 + PAD, by1 + PAD
    w, h = X1 - X0, Y1 - Y0

    mask = Image.new('L', (w, h), 0)
    mask.paste(Image.fromarray((m * 255).astype(np.uint8)).crop(
        (X0 - x0, Y0 - y0, X1 - x0, Y1 - y0)), (0, 0))
    mask = mask.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(3.5))

    src = a[Y0 + SHIFT:Y1 + SHIFT, X0:X1]
    host = a[Y0:Y1, X0:X1]
    alpha = (np.array(mask).astype(np.float32) / 255)[..., None]
    a[Y0:Y1, X0:X1] = host * (1 - alpha) + src * alpha
    Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(S + f'step1_{view}.png')


for v in WIN:
    fix(v)
