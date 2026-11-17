from PIL import Image, ImageDraw, ImageFont

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/'
BG = (9, 13, 24); TAN = (170, 146, 102); BODY = (222, 219, 210)
DIM = (140, 146, 158); WH = (236, 234, 226)
FB = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)

v12 = Image.open(S + 'work13/B2_CAND_ESTABLISHING_V012_2560x1440.png').convert('RGB')
v13 = Image.open(S + 'work13/CAND_ESTABLISHING_V013_2560x1440.png').convert('RGB')

ROWS = [
    ('A   FRAME MARGIN AND LOWER-RIGHT WALL', (1400, 1130, 1960, 1300),
     'V012: margin RGB(0,17,36); wall reads RGB(44,23,23)',
     'V013: margin RGB(8,12,23); wall warm, RGB(38-56,8-17,3-7)'),
    ('B   CLOTH LINE, RIGHT END', (1180, 1030, 1340, 1140),
     'V012: hard cut seam plus a pale wedge under the cloth',
     'V013: edge re-rendered as fabric; wedge gone'),
    ('C   NNEKA\u2019S HOUSE IN THE COMPOUND', (1240, 850, 1680, 1150),
     'V012: house reads large; no striped side cloth',
     'V013: about 15% smaller; approved side cloth restored'),
]

PW = 1000
GAP = 30
PAD = 44
TOP = 250

heights = [PW * (b[3] - b[1]) / (b[2] - b[0]) for _, b, _, _ in ROWS]
total = TOP + sum(h + 78 for h in heights) + 300

board = Image.new('RGB', (PAD * 2 + PW * 2 + GAP, int(total)), BG)
d = ImageDraw.Draw(board)
d.text((PAD, 52), 'ESTABLISHING VIEW \u2014 V012 vs V013', font=FB(32), fill=WH, anchor='ls')
d.text((PAD, 92), 'Diagnostic comparison. Candidate V013, unapproved; nothing here implies approval.',
       font=FR(18), fill=DIM, anchor='ls')
d.text((PAD, 120), 'Approved V005 base preserved untouched. V006 \u2013 V012 preserved in 16_REJECTED_DESIGNS.',
       font=FR(16), fill=DIM, anchor='ls')

y = TOP
for (label, box, c12, c13), bh in zip(ROWS, heights):
    d.text((PAD, y), label, font=FB(17), fill=TAN, anchor='ls')
    d.text((PAD, y + 24), 'V012', font=FB(13), fill=DIM, anchor='ls')
    d.text((PAD + PW + GAP, y + 24), 'V013', font=FB(13), fill=TAN, anchor='ls')
    a = v12.crop(box).resize((PW, int(bh)), Image.LANCZOS)
    b = v13.crop(box).resize((PW, int(bh)), Image.LANCZOS)
    board.paste(a, (PAD, y + 34))
    board.paste(b, (PAD + PW + GAP, y + 34))
    d.text((PAD, y + 34 + int(bh) + 24), c12, font=FR(15), fill=DIM, anchor='ls')
    d.text((PAD + PW + GAP, y + 34 + int(bh) + 24), c13, font=FR(15), fill=BODY, anchor='ls')
    y += int(bh) + 34 + 24 + 44

ny = y + 6
d.line([(PAD, ny), (board.width - PAD, ny)], fill=(42, 48, 60), width=1)
lines = [
    ('Measured on the filed files, not asserted:', BODY, FB(16)),
    ('frame margin  y1250 / y1270 at x=1900        V012 RGB(0,20,38) / RGB(0,14,28)  \u2192  V013 RGB(8,12,23) / RGB(8,12,23)', DIM, FR(15)),
    ('clean left margin, same rows                 RGB(7,11,22) / RGB(6,10,21)        V013 now matches it within 1-2 channels', DIM, FR(15)),
    ('lower-right wall, y1210-1240, x1700-1900     V012 RGB(24-44,1-23,0-23)            \u2192  V013 RGB(27-87,0-32,0-19), warm ramp', DIM, FR(15)),
    ('house height in frame, x1240-1680            V012 227 px                          \u2192  V013 193 px  (-15%)', DIM, FR(15)),
]
for i, (t, c, f) in enumerate(lines):
    d.text((PAD, ny + 36 + i * 27), t, font=f, fill=c, anchor='ls')

fy = ny + 36 + len(lines) * 27 + 30
d.text((PAD, fy), 'Not fixed, stated plainly: the basal hill huts are not re-proportioned (no measurable target was given for hut size), and the ',
       font=FR(15), fill=BODY, anchor='ls')
d.text((PAD, fy + 24), 'left-flank softness measured as atmospheric haze in the approved V005 base rather than a mask feather, so the approved ',
       font=FR(15), fill=BODY, anchor='ls')
d.text((PAD, fy + 48), 'silhouette is preserved rather than sharpened.', font=FR(15), fill=BODY, anchor='ls')

board.save(S + 'submit/B2_COMPARE_ESTABLISHING_V012_vs_V013.jpg', quality=94)
print(board.size, y)
