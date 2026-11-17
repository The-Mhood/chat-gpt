from PIL import Image, ImageDraw, ImageFont

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/work13/'
BG = (9, 13, 24); TAN = (170, 146, 102); BODY = (222, 219, 210)
DIM = (140, 146, 158); WH = (236, 234, 226)
FB = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)

im = Image.open(S + 'step3.png').convert('RGB')
d = ImageDraw.Draw(im)

# wipe the old right column and the right-hand header block
d.rectangle((1958, 148, 2560, 1252), fill=BG)
d.rectangle((1180, 16, 2560, 66), fill=BG)
d.rectangle((1560, 66, 2560, 128), fill=BG)
d.rectangle((928, 1403, 1770, 1425), fill=BG)

d.text((2552, 54), 'ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V013', font=FR(19), fill=BODY, anchor='rs')
d.text((2552, 87), 'STATUS: REVIEW REQUIRED', font=FR(16), fill=BODY, anchor='rs')
d.text((2552, 115), 'EXPLORATORY \u2014 NOT APPROVED CANON  \u00b7  CHAPTER 8', font=FR(14), fill=DIM, anchor='rs')
d.text((940, 1419), 'VERSIONS KEPT: V005 base, V006 \u2013 V012 preserved.  This sheet is V013, unapproved.', font=FR(14), fill=DIM, anchor='ls')

X0, X1 = 1966, 2552
y = 178


def head(t):
    global y
    d.text((X0, y), t, font=FB(14), fill=TAN, anchor='ls'); y += 24


def body(t, indent=0):
    global y
    f = FR(15)
    w = d.textlength(t, font=f)
    assert X0 + indent + w < X1, (round(X0 + indent + w), t)
    d.text((X0 + indent, y), t, font=f, fill=BODY, anchor='ls'); y += 21


def gap(n=13):
    global y
    y += n


head('LABEL')
body('EXPLORATORY \u2014 NOT APPROVED CANON \u00b7')
body('CH08-SUB-001')
body('Version V013. Client review pending.')
body('No client ruling is recorded on this')
body('version; it is a candidate only.')
gap()
head('CHANGED SINCE V012')
body('1  Lower-right mud wall re-warmed to the')
body('   V005 daylight value. Measured on the')
body('   V013 file: RGB(38-56, 8-17, 3-7) on the')
body('   wall band, against RGB(44, 23, 23) and')
body('   cooler on V012.')
body('2  Frame margin bleed removed. The')
body('   RGB(0, 17, 36) cyan band below the art')
body('   is gone: left and right margins now')
body('   read RGB(8, 12, 23) at y1250 and y1270.')
body('3  Cloth-line right end repaired. The cut')
body('   seam and the pale wedge are gone; the')
body('   cloth falls as fabric into yard shadow.')
body('4  Nneka\u2019s House re-rendered about 15%')
body('   smaller in its compound, with the')
body('   approved striped side cloth restored on')
body('   its right wall. Thatch gable and the')
body('   back plot stakes read sharp again.')
gap()
head('NOT FIXED \u2014 STATED PLAINLY')
body('5  Basal hill huts are not re-proportioned')
body('   and the left flank is unchanged. No')
body('   measurable target was given for hut')
body('   size, and horizontal profiles across')
body('   the flank (y 580-760) show roof detail,')
body('   not a uniform alpha feather, so the')
body('   softness is the approved V005 haze and')
body('   is preserved rather than sharpened.')
gap()
head('FICTIONAL ELEMENTS')
body('The aerial river and the stacked mound')
body('of houses are fictional game-world')
body('conceits. They are not documented Igbo')
body('settlement forms.')
gap()
head('RESEARCH')
body('Exact-version report RR_ESTABLISHING_')
body('V013 is outstanding. Labels above are')
body('carried forward unchanged.')
assert y < 1244, y
im.save(S + 'CAND_ESTABLISHING_V013_2560x1440.png')
print('column bottom', y)
