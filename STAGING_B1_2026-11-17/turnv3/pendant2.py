"""V003 step 3 — restore the OAD-02 spiral bronze pendant (native master pixels).

Disc is cut from CHAR_ADANNA_MASTER_REFERENCE_V001 with a soft elliptical mask;
the braided cord is a short strip taken from the same master crop, laid up toward
the throat and faded out at the top so no cut edge shows.
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/'
M = Image.open(S + 'refs/CHAR_ADANNA_MASTER_REFERENCE_V001.jpg').convert('RGB')
DISC = (924, 686, 1032, 792)          # master pixels, disc only
CORD = (1000, 652, 1042, 700)         # master pixels, braided cord above the disc

PLATES = [                            # (file, disc centre x, y, disc width, cord length)
    ('turnv3/step1_FRONT.png', 1052, 452, 30, 26),
    ('turnv3/step2_LEFT_SIDE.png', 1084, 452, 26, 24),
    ('turnv3/step2_THREE_QUARTER.png', 1046, 452, 28, 24),
]

disc_src = M.crop(DISC)
cord_src = M.crop(CORD)
cord_col = tuple(int(v) for v in np.median(np.array(cord_src).reshape(-1, 3), 0))

for path, cx, cy, w, clen in PLATES:
    h = int(disc_src.height * w / disc_src.width)
    disc = disc_src.resize((w, h), Image.LANCZOS)
    base = Image.open(S + path).convert('RGB')
    a = np.array(base).astype(np.float32)

    # cord first: thin tapering line from the throat down to the disc
    d = ImageDraw.Draw(base)
    x0, y0 = cx, cy - clen
    for i in range(clen):
        t = i / max(clen - 1, 1)
        d.line([(x0 - 2 * (1 - t), y0 + i), (x0 + 1, y0 + i + 1)], fill=cord_col, width=2)
    a = np.array(base.filter(ImageFilter.GaussianBlur(0.6))).astype(np.float32) * 0.0 + np.array(base).astype(np.float32)
    a = np.array(base).astype(np.float32)

    # disc
    p = np.array(disc).astype(np.float32)
    px, py = cx - w // 2, cy - h // 2
    host = a[py:py + h, px:px + w]
    delta = np.median(host[:4].reshape(-1, 3) - p[:4].reshape(-1, 3), 0) * 0.3
    p = np.clip(p + delta, 0, 255)
    m = Image.new('L', (w, h), 0)
    ImageDraw.Draw(m).ellipse((1, 1, w - 2, h - 2), fill=255)
    m = np.array(m.filter(ImageFilter.GaussianBlur(2))).astype(np.float32)[..., None] / 255.0
    a[py:py + h, px:px + w] = host * (1 - m) + p * m

    out = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    out.save(S + path.replace('step1_', 'step3_').replace('step2_', 'step3_'))
    print(path, 'disc', w, h, 'at', px, py)
