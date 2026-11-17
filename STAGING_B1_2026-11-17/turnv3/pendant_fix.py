"""V003 — paste the retouched pendant through a tone-matched, diff-limited mask."""
from PIL import Image, ImageFilter
import numpy as np

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/turnv3/'
JOBS = [('step1_FRONT.png', 'p_pend_front_src.png', 'p_pend_front_new.png',
         (985, 400, 1145, 520), 'step3_FRONT.png'),
        ('step2_LEFT_SIDE.png', 'p_pend_side_src.png', 'p_pend_side_new.png',
         (1010, 400, 1170, 520), 'step3_LEFT_SIDE.png'),
        ('step2_THREE_QUARTER.png', 'p_pend_tq_src.png', 'p_pend_tq_new.png',
         (975, 400, 1135, 520), 'step3_THREE_QUARTER.png')]


def match(p, host, ring):
    out = p.copy()
    for c in range(3):
        h = host[..., c][ring]
        q = p[..., c][ring]
        A = np.vstack([q, np.ones_like(q)]).T
        gain, off = np.linalg.lstsq(A, h, rcond=None)[0]
        out[..., c] = np.clip(p[..., c] * gain + off, 0, 255)
    return out


for base_name, src_name, new_name, rect, out_name in JOBS:
    base = Image.open(S + base_name).convert('RGB')
    w, h = rect[2] - rect[0], rect[3] - rect[1]
    src = np.array(Image.open(S + src_name).convert('RGB').resize((w, h), Image.LANCZOS)).astype(np.float64)
    new = np.array(Image.open(S + new_name).convert('RGB').resize((w, h), Image.LANCZOS)).astype(np.float64)
    host_a = np.array(base).astype(np.float64)
    host = host_a[rect[1]:rect[3], rect[0]:rect[2]].copy()

    ring = np.zeros((h, w), bool)
    ring[:10] = ring[-10:] = True
    ring[:, :10] = ring[:, -10:] = True
    new_m = match(new, host, ring)

    diff = np.abs(new_m - src).max(2)
    m = (diff > 38).astype(np.uint8) * 255
    m = Image.fromarray(m).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(4))
    mm = np.array(m).astype(np.float32)[None, :, :, None] / 255.0
    mm = mm[0]
    host = host * (1 - mm) + new_m * mm
    host_a[rect[1]:rect[3], rect[0]:rect[2]] = host
    Image.fromarray(np.clip(host_a, 0, 255).astype(np.uint8)).save(S + out_name)
    print(out_name, 'mask px', int((mm[..., 0] > 0.4).sum()))
