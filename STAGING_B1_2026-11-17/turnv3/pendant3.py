"""V003 — pendant built from approved master pixels, masked to its own footprint.

No rectangular paste and no tone pass: only the disc ellipse and a thin cord strip
are replaced, so the surrounding skin is untouched and no seam can form.
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/'
M = Image.open(S + 'refs/CHAR_ADANNA_MASTER_REFERENCE_V001.jpg').convert('RGB')
DISC_SRC = M.crop((940, 702, 1016, 780))
CORD_SRC = M.crop((1000, 652, 1042, 700))

# plate, disc centre, disc w, disc h, cord length, cord tilt (x drift)
JOBS = [('turnv3/step1_FRONT.png', (1060, 470), 19, 19, 20, -3, 'turnv3/step3_FRONT.png'),
        ('turnv3/step2_LEFT_SIDE.png', (1082, 445), 12, 17, 16, 2, 'turnv3/step3_LEFT_SIDE.png'),
        ('turnv3/step2_THREE_QUARTER.png', (1074, 447), 17, 17, 16, 2, 'turnv3/step3_THREE_QUARTER.png')]


def tint(img, f):
    a = np.array(img).astype(float) * f
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


for path, (cx, cy), dw, dh, clen, drift, out in JOBS:
    base = Image.open(S + path).convert('RGB')
    img = base.copy()

    # soft contact shadow first
    sh = Image.new('RGBA', (dw + 8, dh + 8), (0, 0, 0, 0))
    d = ImageDraw.Draw(sh)
    d.ellipse((4, 5, dw + 3, dh + 4), fill=(30, 12, 4, 90))
    sh = sh.filter(ImageFilter.GaussianBlur(2.2))
    img.paste(sh, (cx - dw // 2 - 3, cy - dh // 2 - 1), sh)

    # cord: thin braided strip, fading at the top
    cord = CORD_SRC.resize((3, clen), Image.LANCZOS)
    ca = np.array(cord)
    mask = Image.new('L', (3, clen), 0)
    for i in range(clen):
        v = int(255 * (0.35 + 0.65 * (i / max(clen - 1, 1))))
        ImageDraw.Draw(mask).line([(0, i), (2, i)], fill=v)
    mask = mask.filter(ImageFilter.GaussianBlur(0.8))
    img.paste(cord, (cx + int(drift * -1), cy - dh // 2 - clen + 2), mask)

    # disc
    disc = DISC_SRC.resize((dw, dh), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.4))
    dm = Image.new('L', (dw, dh), 0)
    ImageDraw.Draw(dm).ellipse((1, 1, dw - 2, dh - 2), fill=255)
    dm = dm.filter(ImageFilter.GaussianBlur(1.1))
    img.paste(disc, (cx - dw // 2, cy - dh // 2), dm)

    img.save(S + out)
    print(out, 'placed', (cx, cy), dw, dh)
