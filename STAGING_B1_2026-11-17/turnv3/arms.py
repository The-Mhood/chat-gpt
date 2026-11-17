"""V003 three-quarter arms: bare right arm, plain coils on the left arm."""
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

T = '/home/user/chat-gpt/STAGING_B1_2026-11-17/turnv3/'
b = np.array(Image.open(T + 'step4_THREE_QUARTER.png').convert('RGB')).astype(float)


def paste(gen_path, box, mask_rect, feather, tone_rect):
    """Paste gen into box through a feathered rectangle, LF tone-matched."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    gen = np.array(Image.open(gen_path).convert('RGB').resize((w, h), Image.LANCZOS)).astype(float)
    host = b[y0:y1, x0:x1]
    m = Image.new('L', (w, h), 0)
    ImageDraw.Draw(m).rectangle(mask_rect, fill=255)
    m = np.array(m.filter(ImageFilter.GaussianBlur(feather))).astype(float)[..., None] / 255

    sel = np.zeros((h, w), bool)
    sel[tone_rect[1]:tone_rect[3], tone_rect[0]:tone_rect[2]] = True
    off = np.median((host - gen)[sel], 0)
    gen = np.clip(gen + off, 0, 255)
    b[y0:y1, x0:x1] = host * (1 - m) + gen * m
    print(gen_path.split('/')[-1], 'offset', off.round(1))


# far arm, her LEFT: plain concentric coils replace the hammered cuff + medallion
paste(T + 'p_fararm_new.png', (1155, 480, 1250, 575), (29, 0, 90, 95), 6, (34, 58, 86, 92))
# near arm, her RIGHT: bare skin
paste(T + 'p_neararm_new.png', (905, 455, 1005, 555), (11, 22, 89, 79), 4, (20, 84, 70, 96))

Image.fromarray(np.clip(b, 0, 255).astype(np.uint8)).save(T + 'step5_THREE_QUARTER.png')
print('saved step5')
