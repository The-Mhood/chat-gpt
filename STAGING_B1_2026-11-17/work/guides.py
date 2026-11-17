from PIL import Image, ImageDraw, ImageFont
FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def fb(s): return ImageFont.truetype(FB,s)
def f(s): return ImageFont.truetype(F,s)
OX,OY=60,152

def guide(master, out, ann):
    base=Image.open(master).convert('RGB')
    ov=Image.new('RGBA', base.size, (0,0,0,0))
    d=ImageDraw.Draw(ov)
    for a in ann: a(d)
    img=Image.alpha_composite(base.convert('RGBA'), ov).convert('RGB')
    img.save(out, quality=94)
    print(out, img.size)

def P(x,y): return (x+OX, y+OY)

def dashed_line(d, p0, p1, fill, width=3, dash=14, gap=10):
    import math
    x0,y0=p0; x1,y1=p1
    L=math.hypot(x1-x0,y1-y0); n=int(L//(dash+gap))+1
    for i in range(n):
        t0=(i*(dash+gap))/L; t1=min(1.0,(i*(dash+gap)+dash)/L)
        d.line([(x0+(x1-x0)*t0, y0+(y1-y0)*t0),(x0+(x1-x0)*t1, y0+(y1-y0)*t1)], fill=fill, width=width)

def cross(d, p, r=22, fill=(255,60,60,255), w=3):
    d.line([(p[0]-r,p[1]),(p[0]+r,p[1])], fill=fill, width=w)
    d.line([(p[0],p[1]-r),(p[0],p[1]+r)], fill=fill, width=w)

def label(d, p, text, fnt=None, fill=(255,255,255,255), bg=(10,12,16,215), pad=8):
    fnt=fnt or f(24)
    bb=d.textbbox((0,0),text,font=fnt)
    w,h=bb[2]-bb[0], bb[3]-bb[1]
    x,y=p
    d.rectangle([x-pad,y-pad,x+w+pad,y+h+pad+6], fill=bg)
    d.text((x,y), text, font=fnt, fill=fill)

# ---------------- VR-007 ----------------
pommel=P(1545,690); chape=P(1357,940); tipY=P(1357,865)[1]
def a1(d):
    d.line([pommel,chape], fill=(255,80,80,235), width=4)
    cross(d,pommel,26,(255,80,80,255))
    cross(d,chape,30,(255,80,80,255))
    dashed_line(d,(P(1250,865)[0], tipY),(P(1700,865)[0], tipY),(80,255,120,235),4,16,10)
    dashed_line(d,(P(1250,940)[0], P(1250,940)[1]),(P(1700,940)[0], P(1700,940)[1]),(255,80,80,180),2,10,10)
    label(d,(P(1180,600)), 'VR-007  RETOUCH GUIDE  -  one object only', fb(30))
    label(d,(P(1180,640)), 'ORIGINAL V002  (CD-mandated base)  panel coords 1901x1169', f(22),(200,210,220,255))
    label(d,(P(1230,690)), 'A  spiral pommel  (1545,690)  KEEP', f(22),(255,150,150,255))
    label(d,(P(1150,960)), 'B  chape disc  (1357,940)  MOVE UP', f(22),(255,150,150,255))
    label(d,(P(1180,1005)), 'sheath currently 383 px long = ~90-100 cm blade', f(22),(255,190,190,255))
    label(d,(P(1690,858)), 'TARGET: tip no lower than here  (y 865)', f(22),(150,255,170,255))
    label(d,(P(1690,930)), 'current lowest point  (y 940)', f(22),(255,150,150,255))
    label(d,(P(1180,1060)), 'ACTION  shorten along the axis about A to ~70% so the tip lands on the green line;', f(22),(235,240,247,255))
    label(d,(P(1180,1092)), 're-seat the chape disc at the new tip; rebuild skirt + platform shadow behind the removed section.', f(22),(235,240,247,255))
    label(d,(P(1180,1124)), 'MUST NOT CHANGE  face, hair, costume, hands, cloth, hearth, doorway view, mat, jars, basket, light.', f(22),(235,240,247,255))
    label(d,(P(1180,1156)), 'NO bare blade. No second weapon. Nothing on the sleeping platform.', f(22),(150,255,170,255))
guide('masters/COMP_ADANNA_NNEKAS_HOUSE_INTERIOR_V002.jpg','guides/RETOUCH_GUIDE_VR-007.jpg',[a1])

# ---------------- VR-006 ----------------
hilt=P(1560,622); tip=P(1760,782)
def a2(d):
    d.line([hilt,tip], fill=(255,80,80,235), width=4)
    cross(d,hilt,24,(255,80,80,255))
    cross(d,tip,26,(255,80,80,255))
    dashed_line(d,P(1600,660),P(1600,890),(80,255,120,235),4,16,10)
    cross(d,(P(1600,880)),24,(80,255,120,255))
    label(d,(P(1200,600)), 'VR-006  RETOUCH GUIDE  -  one object only', fb(30))
    label(d,(P(1200,640)), 'ORIGINAL V003  panel coords 1901x1169  -  doorway view MUST be held', f(22),(200,210,220,255))
    label(d,(P(1250,690)), 'A  hilt at her left hip  (1560,622)  KEEP', f(22),(255,150,150,255))
    label(d,(P(1790,770)), 'B  current tip (1760,782)', f(22),(255,150,150,255))
    label(d,(P(1170,830)), 'FAULT  angled back and reaching below mid-thigh;', f(22),(255,190,190,255))
    label(d,(P(1170,862)), 'it passes behind the mortar instead of hanging at her side.', f(22),(255,190,190,255))
    label(d,(P(1230,860)), 'TARGET  hang VERTICALLY from A; tip at or above (1600,880)', f(22),(150,255,170,255))
    label(d,(P(1170,930)), 'ACTION  rotate the sheath upright about the hilt and shorten to ~65% of B;', f(22),(235,240,247,255))
    label(d,(P(1170,962)), 'rebuild the skirt behind the old diagonal; keep the mortar and pestle untouched and in front.', f(22),(235,240,247,255))
    label(d,(P(1170,994)), 'MUST NOT CHANGE  face, hair, costume, ornaments, sandals, stance, hand on pestle, loom cloth, jars, tree, broom, light.', f(22),(235,240,247,255))
guide('masters/COMP_ADANNA_MOTHERS_COURTYARD_V003.jpg','guides/RETOUCH_GUIDE_VR-006.jpg',[a2])
