"""V003 step 3 — restore the OAD-02 spiral bronze pendant from the approved master.

The pendant is taken at native resolution from CHAR_ADANNA_MASTER_REFERENCE_V001
(the approved source), scaled to plate proportion, and composited with a feathered
oval so the braided cord and disc sit on the chest without a cut edge.
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/'
MASTER = S + 'refs/CHAR_ADANNA_MASTER_REFERENCE_V001.jpg'

# pendant + cord upper stub, native master pixels (detail panel)
SRC_BOX = (905, 655, 1060, 800)

# per-plate destination: (plate_path, centre_x, centre_y, target_width)
PLATES = [
    ('turnv3/step1_FRONT.png', 1052, 604, 60),
    ('turnv3/step2_LEFT_SIDE.png', 1078, 596, 52),
    ('turnv3/step2_THREE_QUARTER.png', 1042, 604, 54),
]


def build(w):
    src = Image.open(MASTER).convert('RGB').crop(SRC_BOX)
    h = int(src.height * w / src.width)
    return src.resize((w, h), Image.LANCZOS)


for path, cx, cy, w in PLATES:
    pend = build(w)
    pw, ph = pend.size
    base = Image.open(S + path).convert('RGB')
    a = np.array(base).astype(np.float32)
    p = np.array(pend).astype(np.float32)

    x0, y0 = cx - pw // 2, cy - ph // 2
    host = a[y0:y0 + ph, x0:x0 + pw]
    delta = np.median(host[:8].reshape(-1, 3) - p[:8].reshape(-1, 3), 0) * 0.35
    p = np.clip(p + delta, 0, 255)

    mask = Image.new('L', (pw, ph), 0)
    ImageDraw.Draw(mask).ellipse((2, 2, pw - 3, ph - 3), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(4))
    m = np.array(mask).astype(np.float32)[..., None] / 255.0 * 0.92

    a[y0:y0 + ph, x0:x0 + pw] = host * (1 - m) + p * m
    out = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    out.save(S + path.replace('step1_', 'step3_').replace('step2_', 'step3_'))
    print(path, 'pendant', pw, 'x', ph, 'at', x0, y0)
