"""V004 targeted fixes: connected pendant cord (FRONT + THREE_QUARTER) and the
three-quarter near-arm patch blend. Bounded pixel edits on the filed V003 plates."""
from PIL import Image, ImageFilter
import numpy as np, math

S = '/home/user/chat-gpt/STAGING_B1_2026-11-17/'
F = S + 'submit/B2_CAND_CHAR_ADANNA_TURNAROUND_%s_V003_2560x1440.png'


def load(v):
    return np.array(Image.open(F % v).convert('RGB')).astype(float)


def save(a, path):
    Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(path)


def seg_dist(xx, yy, p0, p1):
    ax, ay = p0; bx, by = p1
    vx, vy = bx - ax, by - ay
    t = np.clip(((xx - ax) * vx + (yy - ay) * vy) / (vx * vx + vy * vy), 0, 1)
    dx, dy = xx - (ax + t * vx), yy - (ay + t * vy)
    return np.hypot(dx, dy), t


def cord_strand(a, pts, colour, w0, w1, fade_start, fade_end, shadow=True):
    """Draw one strand of cord along a polyline, tapering, fading out at the top."""
    h, w = a.shape[:2]
    x0 = int(min(p[0] for p in pts)) - 6; x1 = int(max(p[0] for p in pts)) + 7
    y0 = int(min(p[1] for p in pts)) - 5; y1 = int(max(p[1] for p in pts)) + 6
    yy, xx = np.mgrid[y0:y1, x0:x1]
    d = np.full(xx.shape, 1e6); tt = np.zeros(xx.shape)
    for i in range(len(pts) - 1):
        di, ti = seg_dist(xx, yy, pts[i], pts[i + 1])
        m = di < d
        d[m] = di[m]
        tt[m] = (i + ti[m]) / (len(pts) - 1)
    yabs = yy + 0.0
    wid = w0 + (w1 - w0) * tt                        # taper along the strand
    alpha = np.clip(1.0 - (d - wid) / 0.9, 0, 1)      # soft edge
    f = np.clip((fade_end - yabs) / max(1.0, (fade_end - fade_start)), 0, 1)
    alpha = alpha * np.clip(1 - f, 0, 1) ** 0.9
    braid = 0.86 + 0.14 * np.cos(tt * 26.0)
    alpha *= 0.88 * braid
    sub = a[y0:y1, x0:x1]
    if shadow:
        ds = np.clip(1.0 - (d - wid - 1.3) / 1.2, 0, 1) * np.clip(1 - f, 0, 1) * 0.28
        sub = sub * (1 - ds[..., None] * 0.55)
    sub = sub * (1 - alpha[..., None]) + np.array(colour) * alpha[..., None] * 0.9 \
        + sub * alpha[..., None] * 0.1
    a[y0:y1, x0:x1] = sub


def arm_patch(a, gen_path, box=(890, 435, 1050, 575), rect=(898, 447, 1043, 563),
              erode=7, feather=16):
    """Re-lay the near-arm skin: generated interior only, host silhouette and cloth kept."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    H = a[y0:y1, x0:x1]
    G = np.array(Image.open(gen_path).convert('RGB').resize((w, h), Image.LANCZOS)).astype(float)

    R, Gd, B = H[..., 0], H[..., 1], H[..., 2]
    lum = H.mean(2)
    skin = ((R > Gd) & (Gd > B) & (R - B > 15) & (lum > 25) & (lum < 175) & (B < 150))
    m = Image.fromarray((skin * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(2 * erode + 1))
    keep = Image.new('L', (w, h), 0)
    keep.paste(m, (0, 0))
    box_mask = np.array(keep).astype(float) / 255.0
    lim = np.zeros((h, w), bool)
    lim[rect[1] - y0:rect[3] - y0, rect[0] - x0:rect[2] - x0] = True
    box_mask *= lim
    soft = np.array(Image.fromarray((box_mask * 255).astype(np.uint8))
                    .filter(ImageFilter.GaussianBlur(feather))).astype(float)[..., None] / 255.0

    wgt = soft[..., 0] > 0.5
    mH, mG = np.median(H[wgt], 0), np.median(G[wgt], 0)
    sH, sG = H[wgt].std(0), G[wgt].std(0)
    G = np.clip(mH + (G - mG) * np.clip(sH / np.maximum(sG, 1e-3), 0.85, 1.2), 0, 255)
    print('arm patch gain', (sH / np.maximum(sG, 1e-3)).round(2),
          'offset', (mH - mG).round(1), 'mask px', int(wgt.sum()))
    combined = H * (1 - soft) + G * soft
    # matched grain: the generated skin upsampled from a big render is smoother than the host,
    # which is what reads as a flat patch. Re-seed high-frequency grain with host statistics.
    ref = a[575:655, 930:1030].astype(float)
    def hp(x):
        b = np.array(Image.fromarray(np.clip(x, 0, 255).astype(np.uint8))
                     .filter(ImageFilter.GaussianBlur(2.0))).astype(float)
        return x - b
    sigma = float(min(np.median(hp(ref).mean(2).std()), 7.0))
    rng = np.random.default_rng(11)
    noise = rng.normal(0, 1, combined.shape[:2])[..., None].repeat(3, 2)
    noise = np.clip(noise * 30 + 128, 0, 255)
    nhp = hp(noise)
    nhp *= sigma / max(float(nhp.std()), 1e-6)
    combined = np.clip(combined + nhp * soft * 0.22, 0, 255)
    print('grain sigma', round(sigma, 1))
    a[y0:y1, x0:x1] = combined
    return a


# ---------------- FRONT: cord to the neck ----------------
a = load('FRONT')
cord_col = (104, 74, 52)
cord_strand(a, [(1064, 452), (1062, 437), (1057, 422), (1054, 410), (1052, 402)],
            cord_col, 1.60, 1.15, fade_start=400, fade_end=414)
cord_strand(a, [(1067, 450), (1068, 437), (1070, 423), (1071, 412), (1071, 403)],
            cord_col, 1.60, 1.15, fade_start=402, fade_end=416)
save(a, S + 'turnv3/step6_FRONT.png')

# ---------------- THREE QUARTER: cord + arm patch ----------------
b = load('THREE_QUARTER')
# arm patch tonal/texture blend first
b = arm_patch(b, S + 'turnv3/p_armtq_v4_new.png')

cord_col_t = (96, 70, 50)
cord_strand(b, [(1073, 432), (1072, 424), (1070, 414), (1068, 406), (1066, 400)],
            cord_col_t, 1.5, 1.0, fade_start=400, fade_end=412)
cord_strand(b, [(1076, 430), (1077, 424), (1078, 415), (1080, 407), (1081, 401)],
            cord_col_t, 1.5, 1.0, fade_start=401, fade_end=413)
save(b, S + 'turnv3/step6_THREE_QUARTER.png')
print('done')
