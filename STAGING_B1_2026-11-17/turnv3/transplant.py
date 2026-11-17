"""V003 — transplant only the changed pixels (pendant + cord) back into the plate.

Tone drift in the retouched crop is avoided by pasting through a diff mask: only
where the retouch differs from its own input, feathered, lands on the plate.
"""
from PIL import Image, ImageFilter
import numpy as np

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/turnv3/'
JOBS = [
    ('step1_FRONT.png', 'p_pend_front_src.png', 'p_pend_front_new.png',
     (985, 400, 1145, 520), 'step3_FRONT.png'),
    ('step2_LEFT_SIDE.png', 'p_pend_side_src.png', 'p_pend_side_new.png',
     (1010, 400, 1170, 520), 'step3_LEFT_SIDE.png'),
    ('step2_THREE_QUARTER.png', 'p_pend_tq_src.png', 'p_pend_tq_new.png',
     (975, 400, 1135, 520), 'step3_THREE_QUARTER.png'),
]

for base_name, src_name, new_name, rect, out_name in JOBS:
    base = Image.open(S + base_name).convert('RGB')
    w, h = rect[2] - rect[0], rect[3] - rect[1]
    src = Image.open(S + src_name).convert('RGB').resize((w, h), Image.LANCZOS)
    new = Image.open(S + new_name).convert('RGB').resize((w, h), Image.LANCZOS)
    a_s, a_n = np.array(src).astype(int), np.array(new).astype(int)
    diff = np.abs(a_n - a_s).max(2)
    m = (diff > 22).astype(np.uint8) * 255
    m = Image.fromarray(m).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(2))
    mm = np.array(m).astype(np.float32)[..., None] / 255.0
    host = np.array(base).astype(np.float32)
    reg = host[rect[1]:rect[3], rect[0]:rect[2]]
    reg = reg * (1 - mm) + np.array(new).astype(np.float32) * mm
    host[rect[1]:rect[3], rect[0]:rect[2]] = reg
    Image.fromarray(np.clip(host, 0, 255).astype(np.uint8)).save(S + out_name)
    print(out_name, 'mask px', int((np.array(m) > 60).sum()))
