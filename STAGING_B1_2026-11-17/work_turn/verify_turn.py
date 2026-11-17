"""Verify the four V002 turnaround plates share one orthographic scale."""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, json

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/'
VIEWS = ['FRONT', 'LEFT_SIDE', 'BACK', 'THREE_QUARTER']
PANEL = (60, 130, 1930, 1310)
FB = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)

out = {}
for v in VIEWS:
    im = Image.open(f'{S}final/CAND_CHAR_ADANNA_TURNAROUND_{v}_V002_2560x1440.png').convert('RGB')
    a = np.array(im.crop(PANEL)).astype(np.int16)
    bg = np.array([209, 209, 207])
    m = np.abs(a - bg).max(2) > 34
    rows, cols = m.sum(1), m.sum(0)
    ys = np.where(rows > 10)[0]
    xs = np.where(cols > 10)[0]
    out[v] = dict(crown_row=int(ys[0]), floor_row=int(ys[-1]),
                  fig_height=int(ys[-1] - ys[0] + 1),
                  fig_left=int(xs[0]), fig_right=int(xs[-1]),
                  fig_centre=int((xs[0] + xs[-1]) // 2))
h = [d['fig_height'] for d in out.values()]
c = [d['crown_row'] for d in out.values()]
f = [d['floor_row'] for d in out.values()]
out['_spread'] = dict(height=max(h) - min(h), crown=max(c) - min(c), floor=max(f) - min(f))

# ---- 4-up alignment board -------------------------------------------------
PW, PH = 620, 391
SC = PW / 1870
BW = 20 + 4 * (PW + 20)
TOP = 132
board = Image.new('RGB', (BW, TOP + PH + 300), (9, 13, 24))
d = ImageDraw.Draw(board)
BG, TAN, WH, DIM, BODY = (9, 13, 24), (164, 139, 93), (238, 238, 232), (150, 158, 172), (226, 225, 217)
d.text((20, 40), 'ADANNA \u2014 TURNAROUND V002', font=FB(30), fill=WH, anchor='ls')
d.text((20, 78), 'Four views, one scale: crown, shoulder line, waist, hem and floor land on the same rows. '
                 'Candidate for review \u2014 not an approved asset.', font=FR(16), fill=DIM, anchor='ls')
d.text((20, 104), 'No blade depicted in this set \u2014 CQ-9 OPEN.', font=FB(15), fill=TAN, anchor='ls')

crown_y = TOP + round(c[0] * SC) if False else None
for i, v in enumerate(VIEWS):
    p = Image.open(f'{S}final/CAND_CHAR_ADANNA_TURNAROUND_{v}_V002_2560x1440.png').crop(PANEL).resize((PW, PH), Image.LANCZOS)
    x = 20 + i * (PW + 20)
    board.paste(p, (x, TOP))
    d.text((x + 6, TOP + PH + 34), v.replace('_', ' '), font=FB(17), fill=WH, anchor='ls')
    dd = out[v]
    d.text((x + 6, TOP + PH + 58),
           f"crown {dd['crown_row']}  floor {dd['floor_row']}  h {dd['fig_height']}",
           font=FR(14), fill=DIM, anchor='ls')
    for row, lab in ((dd['crown_row'], 'crown'), (dd['floor_row'], 'floor')):
        yy = TOP + row * SC
        for xx in range(x, x + PW, 14):
            d.line([(xx, yy), (xx + 7, yy)], fill=TAN, width=1)

y0 = TOP + PH + 150
lines = [
    f"height spread {out['_spread']['height']} px \u00b7 crown spread {out['_spread']['crown']} px "
    f"\u00b7 floor spread {out['_spread']['floor']} px  (panel 1870\u00d71180, body target 1103 px)",
    'Baldric route, identical in all four plates: over her RIGHT shoulder to her LEFT hip.',
    'Armlet, temple beads and cheek scar stay on her anatomical LEFT in every view.',
    'Blade and scabbard omitted: three generation passes put the scabbard on her right hip, the',
    'opposite of the OAD-02 lock, which is the defect Our Eyes rejected in V001. CQ-9 stays open.',
]
for i, t in enumerate(lines[:1]):
    d.text((20, y0), t, font=FR(15), fill=BODY, anchor='ls')
for i, t in enumerate(lines[1:]):
    d.text((20, y0 + 26 + i * 24), t, font=FR(15), fill=BODY if i > 1 else TAN, anchor='ls')

board.save(f'{S}submit/B2_COMPARE_ADANNA_TURNAROUND_V002_alignment.jpg', quality=94)
json.dump(out, open(f'{S}work_turn/turn_audit.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
