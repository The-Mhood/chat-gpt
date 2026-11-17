from PIL import Image, ImageDraw, ImageFont

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/'
BG = (9, 13, 24); TAN = (164, 139, 93); BODY = (226, 225, 217)
DIM = (150, 158, 172); WH = (238, 238, 232)
FB = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)

VIEWS = ['FRONT', 'LEFT_SIDE', 'BACK', 'THREE_QUARTER']
LOCKS = {
 'FRONT': ['high braided knot, braids to shoulder', 'brass cuffs + coral beads at LEFT temple',
           '(viewer-right in this view)', 'thin scar, LEFT cheekbone (viewer-right)',
           'RIGHT temple and cheek plain', 'coiled bronze armlet, LEFT upper arm',
           'bare shoulders, no armour', 'plain dark-brown diagonal leather baldric',
           'indigo bandeau and wrap, leather sandals'],
 'LEFT_SIDE': ['high braided knot, braids to shoulder', 'beaded braid tips at LEFT temple',
               'shoulder line relaxed, arm at side', 'bare shoulders, no armour',
               'coiled bronze armlet, LEFT upper arm', 'plain leather baldric over shoulder',
               'indigo bandeau and wrap, leather sandals'],
 'BACK': ['high braided knot at crown', 'braids fall to the shoulder blades',
          'coral beads read at the nape, LEFT side', 'bare shoulders and back, no armour',
          'baldric crosses the back shoulder to hip', 'coiled bronze armlet, LEFT arm (viewer-left)',
          'indigo wrap tie at the back, leather sandals'],
 'THREE_QUARTER': ['high braided knot, braids to shoulder', 'brass cuffs + coral beads, LEFT temple',
                   'thin scar, LEFT cheekbone', 'RIGHT temple and cheek plain',
                   'coiled bronze armlet, LEFT upper arm', 'bare shoulders, no armour',
                   'plain leather baldric, indigo bandeau and wrap'],
}
NOTES = {
 'FRONT': 'label now reads viewer-right = anatomical left',
 'LEFT_SIDE': 'profile confirms the bead side reads left',
 'BACK': 'bead cluster sits left of the nape midline',
 'THREE_QUARTER': 'near side carries the beaded braids',
}


def plate(view):
    im = Image.new('RGB', (2560, 1440), BG)
    im.paste(Image.open(f'{S}work_turn/panel_{view}.png'), (60, 130))
    d = ImageDraw.Draw(im)

    def spaced(xy, txt, font, fill, gap=1.2):
        x, y = xy
        for ch in txt:
            d.text((x, y), ch, font=font, fill=fill, anchor='ls')
            x += d.textlength(ch, font=font) + gap

    # header
    spaced((60, 52), 'THE DISOBEDIENT DAUGHTER  \u00b7  ADANNA  \u00b7  4-VIEW TURNAROUND',
           FB(15), TAN, 2.0)
    d.text((58, 104), f'ADANNA \u2014 TURNAROUND: {view.replace("_", " ")}',
           font=FB(38), fill=WH, anchor='ls')
    d.text((2556, 104), '2560\u00d71440  \u00b7  CHARACTER ART  \u00b7  BATCH 1',
           font=FR(17), fill=DIM, anchor='rs')

    # footer caption
    d.text((60, 1362), 'UNAPPROVED \u2014 PENDING REVIEW.  Candidate V002, not an approved asset.',
           font=FB(18), fill=TAN, anchor='ls')
    d.text((60, 1396),
           'All four plates built to one orthographic scale: crown row 57, floor row 1158. '
           'No blade depicted in this set (CQ-9).',
           font=FR(17), fill=DIM, anchor='ls')

    # right column
    X0, X1 = 1956, 2545
    d.rectangle((1946, 130, 2556, 1310), fill=BG)
    y = 168

    def head(t):
        nonlocal y
        spaced((X0, y), t, FB(14), TAN); y += 28

    def body(t, indent=0):
        nonlocal y
        f = FR(16)
        assert X0 + indent + d.textlength(t, font=f) < X1 + 2, (round(X0 + indent + d.textlength(t, font=f)), t)
        d.text((X0 + indent, y), t, font=f, fill=BODY, anchor='ls'); y += 22

    def gap(n=14):
        nonlocal y
        y += n

    head('ASSET')
    body('CHAR_ADANNA_TURNAROUND_' + view)
    body('_V002  \u00b7  plate 1 of 4-view set')
    gap()
    head('STATUS')
    body('UNAPPROVED \u2014 PENDING REVIEW.')
    body('Supersedes V001 (rejected). V001 kept')
    body('in 16_REJECTED_DESIGNS.')
    gap()
    head('SOURCE')
    body('CHAR_ADANNA_MASTER_REFERENCE_V001')
    body('(OAD-02 lock). V001 read for defects')
    body('only; not regenerated from it.')
    gap()
    head('CORRECTIONS IN V002')
    body('1  Baked "APPROVED" header removed;')
    body('   neutral review header on all four.')
    body('2  Temple callout now anatomical LEFT')
    body('   = viewer-right in front view.')
    body('3  Baldric reconciled: over her right')
    body('   shoulder to her left hip, identical')
    body('   route in all four plates.')
    body('4  Four views on one scale and floor.')
    gap()
    head('OAD-02 LOCKS CHECKED')
    for l in LOCKS[view]:
        body(l)
    gap()
    head('VIEW NOTE')
    body(NOTES[view] + '.')
    gap()
    head('OPEN')
    body('CQ-9 blade / scabbard mechanics OPEN.')
    body('No blade is depicted here: the master')
    body('and three generation passes disagree')
    body('on the worn side, and a wrong-side')
    body('blade is the V001 defect. Baldric')
    body('only until Our Eyes sets the side.')
    body('RQ-10-1 coiled armlet stays open.')
    body('Spiral pendant is FICTIONAL; not')
    body('visible in these views, lock intact.')
    assert y < 1300, y
    body = None
    im.save(f'{S}final/CAND_CHAR_ADANNA_TURNAROUND_{view}_V002_2560x1440.png')
    return y


if __name__ == '__main__':
    for v in VIEWS:
        print(v, 'column bottom', plate(v))
