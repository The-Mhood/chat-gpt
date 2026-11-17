"""V003 — detail-transfer composite: retouch high-frequency detail onto a host that
keeps its own tone and lighting, so no rectangle or tone step can appear."""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/turnv3/'
JOBS = [('step1_FRONT.png', 'p_pend_front_new.png', (985, 400, 1145, 520), 'step3_FRONT.png'),
        ('step2_LEFT_SIDE.png', 'p_pend_side_new.png', (1010, 400, 1170, 520), 'step3_LEFT_SIDE.png'),
        ('step2_THREE_QUARTER.png', 'p_pend_tq_new.png', (975, 400, 1135, 520), 'step3_THREE_QUARTER.png')]

R_BLUR = 9
LF = 0.50          # how much of the retouch's low frequency is kept
FEATH = 18


def blur(a, r):
    return np.array(Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
                    .filter(ImageFilter.GaussianBlur(r))).astype(np.float64)


for base_name, new_name, rect, out_name in JOBS:
    base = Image.open(S + base_name).convert('RGB')
    w, h = rect[2] - rect[0], rect[3] - rect[1]
    new = np.array(Image.open(S + new_name).convert('RGB').resize((w, h), Image.LANCZOS)).astype(np.float64)
    host_a = np.array(base).astype(np.float64)
    host = host_a[rect[1]:rect[3], rect[0]:rect[2]].copy()

    hb, nb = blur(host, R_BLUR), blur(new, R_BLUR)
    out = hb + (new - nb) + LF * (nb - hb)

    m = Image.new('L', (w, h), 0)
    ImageDraw.Draw(m).rectangle((FEATH, FEATH, w - 1 - FEATH, h - 1 - FEATH), fill=255)
    mm = np.array(m.filter(ImageFilter.GaussianBlur(FEATH))).astype(np.float64)[..., None] / 255.0

    host_a[rect[1]:rect[3], rect[0]:rect[2]] = host * (1 - mm) + out * mm
    Image.fromarray(np.clip(host_a, 0, 255).astype(np.uint8)).save(S + out_name)
    print(out_name, 'ok')
