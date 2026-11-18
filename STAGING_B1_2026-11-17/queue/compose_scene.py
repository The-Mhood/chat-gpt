"""Chapter 1 scene plates: crop the art to plate ratio and lay the standing chrome band."""
from PIL import Image, ImageDraw, ImageFont
import sys

W, H = 1672, 941
BAND = 54
FB = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR = lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
TAN = (170, 146, 102); BODY = (222, 219, 210); DIM = (140, 146, 158)


def compose(art_path, out_path, code, title, version, prev='V001 (rejected)'):
    art = Image.open(art_path).convert('RGB')
    aw, ah = art.size
    target = W / (H - BAND)
    if aw / ah > target:                       # too wide -> trim sides
        nw = round(ah * target); x0 = (aw - nw) // 2
        art = art.crop((x0, 0, x0 + nw, ah))
    else:                                      # too tall -> trim top/bottom
        nh = round(aw / target); y0 = (ah - nh) // 2
        art = art.crop((0, y0, aw, y0 + nh))
    art = art.resize((W, H - BAND), Image.LANCZOS)

    plate = Image.new('RGB', (W, H), (9, 13, 24))
    plate.paste(art, (0, 0))
    d = ImageDraw.Draw(plate)

    y1, y2 = H - BAND + 20, H - BAND + 41
    left = f'{code}  \u00b7  {title}  \u00b7  {version}' if title else f'{code}  \u00b7  {version}'
    d.text((18, y1), left, font=FB(15), fill=BODY, anchor='ls')
    x = 18 + d.textlength(left, font=FB(15)) + 16
    tag = 'EXPLORATORY \u2014 NOT APPROVED CANON  \u00b7  STATUS: REVIEW REQUIRED'
    d.text((x, y1), tag, font=FB(15), fill=TAN, anchor='ls')
    assert x + d.textlength(tag, font=FB(15)) < W - 18, 'band overruns'

    foot = ('CH01  \u00b7  figures 0 (OAD-40)  \u00b7  FICTIONAL design, no cultural claim  \u00b7  '
            f'VERSIONS KEPT: {prev}, {version} this plate  \u00b7  not to scale')
    d.text((18, y2), foot, font=FR(12), fill=DIM, anchor='ls')
    assert 18 + d.textlength(foot, font=FR(12)) < W - 18, 'footer overruns'

    plate.save(out_path, quality=92, subsampling=0)
    return plate.size


if __name__ == '__main__':
    art, out, code, title, ver = sys.argv[1:6]
    print(compose(art, out, code, title, ver))
