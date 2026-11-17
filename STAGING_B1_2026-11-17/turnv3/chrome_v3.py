"""Build the four Adanna turnaround V003 plates from the corrected panels."""
from PIL import Image, ImageDraw, ImageFont

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/'
T = S + 'turnv3/'
BG = (9, 13, 24); TAN = (170, 146, 102); BODY = (222, 219, 210)
DIM = (140, 146, 158); WH = (236, 234, 226)
FB = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)

SRC = {
    'FRONT': 'step3_FRONT.png',
    'LEFT_SIDE': 'step3_LEFT_SIDE.png',
    'BACK': 'step2_BACK.png',
    'THREE_QUARTER': 'step5_THREE_QUARTER.png',
}
IDX = {'FRONT': 1, 'LEFT_SIDE': 2, 'BACK': 3, 'THREE_QUARTER': 4}

LOCKS = {
    'FRONT': ['high braided knot, braids to shoulder',
              'baldric over anatomical LEFT shoulder',
              'crossing to anatomical RIGHT hip',
              'brass cuffs + coral beads, LEFT temple',
              '(viewer-right in this view)',
              'thin scar, LEFT cheekbone',
              'coiled bronze armlet, LEFT upper arm',
              'indigo bandeau and wrap, leather sandals'],
    'LEFT_SIDE': ['high braided knot, braids to shoulder',
                  'beaded braid tips read at the LEFT temple',
                  'baldric over the LEFT shoulder, front to',
                  'the RIGHT hip; plain leather',
                  'coiled bronze armlet, LEFT upper arm',
                  'indigo bandeau and wrap, leather sandals'],
    'BACK': ['high braided knot at crown',
             'braids fall plain to the shoulder blades',
             'no beads at the braid tips (removed V003)',
             'bead cluster stays at the LEFT temple only',
             'baldric crosses LEFT shoulder to RIGHT hip',
             'coiled bronze armlet, LEFT arm (viewer-left)',
             'wrap tie at the anatomical LEFT hip, front'],
    'THREE_QUARTER': ['high braided knot, braids to shoulder',
                      'brass cuffs + coral beads, LEFT temple',
                      'thin scar, LEFT cheekbone',
                      'spiral bronze pendant, braided cord',
                      'coiled bronze armlet, LEFT upper arm',
                      'baldric LEFT shoulder to RIGHT hip'],
}
NOTES = {
    'FRONT': ('Front view. Viewer-right is her anatomical\nLEFT: temple beads and scar read\nviewer-right, and the baldric leaves\nthe viewer-right shoulder.'),
    'LEFT_SIDE': ('Left profile: the beaded temple side\nfaces the camera, so the bead cluster\nis on this near side and the baldric\nstrap crosses the near shoulder.'),
    'BACK': ('Back view. Viewer-left is her\nautomical LEFT: the armlet reads\nviewer-left, and the wrap tie sits at\nthe LEFT hip, front, not centre back.'),
    'THREE_QUARTER': ('Three-quarter, turned to her RIGHT.\nHer RIGHT side is the near side; the\nbeaded LEFT temple and the scar are\non the far side, partly foreshortened.'),
}


def build(view):
    im = Image.new('RGB', (2560, 1440), BG)
    im.paste(Image.open(T + SRC[view]).convert('RGB').crop((60, 130, 1930, 1310)), (60, 130))
    d = ImageDraw.Draw(im)

    def spaced(xy, txt, font, fill, gap=1.2):
        x, y = xy
        for ch in txt:
            d.text((x, y), ch, font=font, fill=fill, anchor='ls')
            x += d.textlength(ch, font=font) + gap

    spaced((60, 52), 'THE DISOBEDIENT DAUGHTER  \u00b7  ADANNA  \u00b7  4-VIEW TURNAROUND',
           FB(15), TAN, 2.0)
    d.text((58, 104), f'ADANNA \u2014 TURNAROUND: {view.replace("_", " ")}',
           font=FB(38), fill=WH, anchor='ls')
    d.text((2556, 104), '2560\u00d71440  \u00b7  CHARACTER ART  \u00b7  CHAPTER UNASSIGNED',
           font=FR(17), fill=DIM, anchor='rs')

    d.text((60, 1352), 'V003',
           font=FB(22), fill=TAN, anchor='ls')
    d.text((124, 1352),
           'EXPLORATORY \u2014 NOT APPROVED CANON.  STATUS: REVIEW REQUIRED.  '
           'UNAPPROVED \u2014 PENDING REVIEW.',
           font=FB(15), fill=TAN, anchor='ls')
    d.text((60, 1384),
           'Supersedes V002 (rejected 17 Nov 2026). Locks preserved from '
           'CHAR_ADANNA_MASTER_REFERENCE_V001. No blade depicted (CQ-9).',
           font=FR(16), fill=BODY, anchor='ls')
    d.text((60, 1412),
           'VERSIONS KEPT: V001 rejected, V002 rejected, V003 this sheet. '
           'Nothing has been moved to 14_APPROVED_DESIGNS.',
           font=FR(14), fill=DIM, anchor='ls')

    X0, X1 = 1966, 2552
    d.rectangle((1946, 130, 2560, 1310), fill=BG)
    y = 172

    def head(t):
        nonlocal y
        d.text((X0, y), t, font=FB(14), fill=TAN, anchor='ls'); y += 26

    def body(t, indent=0, font=None, fill=BODY):
        nonlocal y
        f = font or FR(15)
        w = d.textlength(t, font=f)
        assert X0 + indent + w < X1, (round(X0 + indent + w), t)
        d.text((X0 + indent, y), t, font=f, fill=fill, anchor='ls'); y += 21

    def gap(n=12):
        nonlocal y
        y += n

    head('ASSET')
    body('CHAR_ADANNA_TURNAROUND_' + view)
    body(f'_V003  \u00b7  plate {IDX[view]} of 4-view set')
    gap()
    head('LABEL')
    body('EXPLORATORY \u2014 NOT APPROVED CANON.')
    body('STATUS: REVIEW REQUIRED.')
    body('Client ruling on V003 not yet recorded.')
    gap()
    head('SOURCE')
    body('Corrected panels of the V002 plates.')
    body('Geometry, pose, scale untouched: crown')
    body('row 57, floor 1155\u20131159, 1099\u20131103 px.')
    gap()
    head('SEVEN CORRECTIONS (V003)')
    body('1  Armlet: medallion ornament removed,')
    body('   plain concentric bronze coils left.')
    body('2  Spiral bronze pendant restored on a')
    body('   braided cord (FICTIONAL ornament).')
    body('3  Scar moved to the LEFT cheekbone in')
    body('   the three-quarter plate.')
    body('4  BACK: braid-tip coral beads and rings')
    body('   removed; beads at the LEFT temple.')
    body('5  Baldric copy corrected: anatomical')
    body('   LEFT shoulder to RIGHT hip, all')
    body('   plates and the alignment sheet.')
    body('6  Plate index 1\u20134 of 4-view set.')
    body('7  Near-side and wrap-tie notes, below.')
    gap()
    head('OAD-02 LOCKS CHECKED')
    for l in LOCKS[view]:
        body(l)
    gap()
    head('VIEW NOTE')
    for line in NOTES[view].split('\n'):
        body(line)
    gap()
    head('OPEN / QUALIFICATIONS')
    body('CQ-9 blade and scabbard OPEN: no blade')
    body('or scabbard is depicted here.')
    body('RQ-10-1 coiled armlet stays OPEN.')
    body('Pendant FICTIONAL; no Igbo provenance.')
    body('OAD-40: one figure per plate by design.')
    body('Baldric route is copy-corrected only; the')
    body('painted strap is the V002 raster.')
    assert y < 1295, (view, y)
    out = f'{T}FINAL_CHAR_ADANNA_TURNAROUND_{view}_V003_2560x1440.png'
    im.save(out)
    return out, y


if __name__ == '__main__':
    for v in IDX:
        print(*(build(v)))
