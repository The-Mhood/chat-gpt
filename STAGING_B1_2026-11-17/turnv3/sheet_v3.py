"""Measure the four V003 plates and build the 4-up alignment sheet."""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, json

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/'
T = S + 'turnv3/'
VIEWS = ['FRONT', 'LEFT_SIDE', 'BACK', 'THREE_QUARTER']
PANEL = (60, 130, 1930, 1310)
FB = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)

out = {}
for v in VIEWS:
    im = Image.open(T + f'FINAL_CHAR_ADANNA_TURNAROUND_{v}_V003_2560x1440.png').convert('RGB')
    a = np.array(im.crop(PANEL)).astype(np.int16)
    bg = np.array([209, 209, 207])
    m = np.abs(a - bg).max(2) > 34
    ys = np.where(m.sum(1) > 10)[0]
    xs = np.where(m.sum(0) > 10)[0]
    out[v] = dict(crown_row=int(ys[0]), floor_row=int(ys[-1]),
                  fig_height=int(ys[-1] - ys[0] + 1),
                  fig_centre=int((xs[0] + xs[-1]) // 2))
h = [d['fig_height'] for d in out.values()]
c = [d['crown_row'] for d in out.values()]
f = [d['floor_row'] for d in out.values()]
out['_spread'] = dict(height=max(h) - min(h), crown=max(c) - min(c), floor=max(f) - min(f))

PW, PH = 620, 391
SC = PW / 1870
BW = 20 + 4 * (PW + 20)
TOP = 150
board = Image.new('RGB', (BW, TOP + PH + 320), (9, 13, 24))
d = ImageDraw.Draw(board)
BG, TAN, WH, DIM, BODY = (9, 13, 24), (170, 146, 102), (236, 234, 226), (140, 146, 158), (222, 219, 210)
d.text((20, 40), 'ADANNA \u2014 TURNAROUND V003', font=FB(30), fill=WH, anchor='ls')
d.text((20, 74), 'EXPLORATORY \u2014 NOT APPROVED CANON   \u00b7   STATUS: REVIEW REQUIRED   \u00b7   '
                 'UNAPPROVED \u2014 PENDING REVIEW', font=FB(15), fill=TAN, anchor='ls')
d.text((20, 100), 'Four views on one orthographic scale, built from the V002 plates with seven bounded corrections. '
                  'Plates 1\u20134 of a 4-view set.', font=FR(16), fill=DIM, anchor='ls')
d.text((20, 124), 'No blade or scabbard depicted \u2014 CQ-9 OPEN.  Spiral pendant is FICTIONAL.',
       font=FR(15), fill=DIM, anchor='ls')

for i, v in enumerate(VIEWS):
    p = Image.open(T + f'FINAL_CHAR_ADANNA_TURNAROUND_{v}_V003_2560x1440.png').crop(PANEL).resize((PW, PH), Image.LANCZOS)
    x = 20 + i * (PW + 20)
    board.paste(p, (x, TOP))
    d.text((x + 6, TOP + PH + 32), f'{i+1}. {v.replace("_", " ")}', font=FB(17), fill=WH, anchor='ls')
    dd = out[v]
    d.text((x + 6, TOP + PH + 56),
           f"crown {dd['crown_row']}  floor {dd['floor_row']}  h {dd['fig_height']}",
           font=FR(14), fill=DIM, anchor='ls')
    for row in (dd['crown_row'], dd['floor_row']):
        yy = TOP + row * SC
        for xx in range(x, x + PW, 14):
            d.line([(xx, yy), (xx + 7, yy)], fill=TAN, width=1)

y0 = TOP + PH + 118
lines = [
    (f"height spread {out['_spread']['height']} px  \u00b7  crown spread {out['_spread']['crown']} px  "
     f"\u00b7  floor spread {out['_spread']['floor']} px   (panel 1870\u00d71180, body target 1103 px)", BODY),
    ('Baldric: over her anatomical LEFT shoulder to her anatomical RIGHT hip, identical in all four plates.', TAN),
    ('Armlet and temple beads stay on her anatomical LEFT. In the three-quarter view her RIGHT side is the near', BODY),
    ('side and that arm is bare; the coiled armlet reads on the far arm at frame right.', BODY),
    ('V002 was rejected on seven points; each is answered above. V001 and V002 are preserved in 16_REJECTED_DESIGNS.', BODY),
]
for i, (t, col) in enumerate(lines):
    d.text((20, y0 + i * 26), t, font=FR(15), fill=col, anchor='ls')

board.save(S + 'submit/B2_COMPARE_ADANNA_TURNAROUND_V003_alignment.jpg', quality=94)
json.dump(out, open(T + 'turn_audit_v3.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
