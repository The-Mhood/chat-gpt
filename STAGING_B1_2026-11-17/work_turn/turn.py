"""Adanna turnaround V002 — panel build.

Every view is scaled so the measured figure height is identical (1103 px on the
1180 px panel) and the floor sits on the same row; crown, shoulder line, waist,
hem and feet therefore land on the same pixels in all four plates (rejection
item #4). Backdrop is colour-matched per view and the paste edge is feathered
into a flat fill of the same neutral grey.
"""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/'
VIEWS = [('FRONT', 'work_turn_front_v5.png'),
         ('LEFT_SIDE', 'work_turn_left.png'),
         ('BACK', 'work_turn_back3.png'),
         ('THREE_QUARTER', 'work_turn_34.png')]

PANEL = (1870, 1180)
FIG_H = 1103           # shared body height on the panel
FLOOR = 1158           # shared floor row
CROPS = 768            # source crop height (all renders are 1365x768)
TARGET = np.array([209.0, 209.0, 207.0])


def bbox(im):
    a = np.array(im).astype(np.int16)
    bg = np.median(np.concatenate([a[:20].reshape(-1, 3),
                                   a[-20:].reshape(-1, 3)]), 0)
    m = np.abs(a - bg).max(2) > 16
    rows, cols = m.sum(1), m.sum(0)
    ys = np.where(rows > 8)[0]
    xs = np.where(cols > 8)[0]
    xs = xs[xs < 1200]
    return xs.min(), xs.max(), ys.min(), ys.max()


def load(f):
    im = Image.open(S + f).convert('RGB')
    x0, x1, y0, y1 = bbox(im)
    bh = y1 - y0 + 1
    cw = 1217
    ch = CROPS
    cx = int(round((x0 + x1) / 2))
    left = max(0, min(cx - cw // 2, im.width - cw))
    top = max(0, min(im.height - ch, int(round((y0 + y1) / 2 - ch / 2))))
    crop = np.array(im.crop((left, top, left + cw, top + ch))).astype(np.float32)
    band = np.concatenate([crop[:40].reshape(-1, 3), crop[-40:].reshape(-1, 3)], 0)
    med = np.median(band, 0)
    crop = np.clip(crop * (TARGET / np.maximum(med, 1)), 0, 255)
    base = Image.fromarray(crop.astype(np.uint8)).resize(PANEL, Image.LANCZOS)

    k = FIG_H / (bh / ch * PANEL[1])          # uniform rescale, no distortion
    w, h = int(round(PANEL[0] * k)), int(round(PANEL[1] * k))
    scl = base.resize((w, h), Image.LANCZOS)

    canvas = Image.new('RGB', PANEL, tuple(int(v) for v in TARGET))
    px = (PANEL[0] - w) // 2
    py = int(round(FLOOR - (y1 - top) / ch * h))
    mask = Image.new('L', (w, h), 0)
    ImageDraw.Draw(mask).rectangle((18, 18, w - 18, h - 18), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(16))
    canvas.paste(scl, (px, py), mask)
    crown = py + (y0 - top) / ch * h
    return canvas, dict(bh=bh, scale=round(k, 4), crown=round(crown, 1),
                        floor=round(FLOOR, 1), paste=(px, py, w, h))


if __name__ == '__main__':
    for name, f in VIEWS:
        img, meta = load(f)
        img.save(f'{S}work_turn/panel_{name}.png')
        print(name, meta)
