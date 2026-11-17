from PIL import Image, ImageDraw, ImageFont
BG=(11,14,23); LINE=(52,62,78); WHITE=(238,238,232); GREY=(150,158,172); TAN=(186,156,110); ALERT=(214,120,96)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
W,H=2560,1440
S=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(S)

def spaced(x,y,t,f,fill,gap=1.1,anchor='ls'):
    cur=x
    for ch in t:
        d.text((cur,y),ch,font=f,fill=fill,anchor=anchor); cur+=d.textlength(ch,font=f)+gap

def panel(img, box, cap=None, capcol=GREY):
    x,y,w,h=box
    c=img.copy(); c.thumbnail((w,h), Image.LANCZOS)
    px,py=(w-c.width)//2,(h-c.height)//2
    S.paste(c,(x+px,y+py))
    d.rectangle([x-1,y-1,x+w,y+h],outline=LINE,width=2)
    if cap: d.text((x,y+h+10),cap,font=FB(16),fill=capcol); return y+h+42
    return y+h

def hatch(box,label,sub=None,col=ALERT):
    x,y,w,h=box
    tile=Image.new('RGB',(w,h),(18,21,31)); td=ImageDraw.Draw(tile)
    for i in range(-h,w+h,26):
        td.line([(i,h),(i+h,0)],fill=(40,46,60),width=1)
    S.paste(tile,(x,y))
    d.rectangle([x,y,x+w,y+h],outline=col,width=2)
    d.text((x+18,y+22),label,font=FB(19),fill=col)
    if sub:
        yy=y+52
        for line in sub:
            d.text((x+18,yy),line,font=FR(15),fill=GREY); yy+=21

def tag(x,y,n):
    r=15
    d.ellipse([x-r,y-r,x+r,y+r],fill=TAN)
    d.text((x,y+1),str(n),font=FB(15),fill=(12,14,20),anchor='mm')

# ---------------- header
d.text((60,32),"THE DISOBEDIENT DAUGHTER  ·  Nwanyi Na-an\u1ee5gh\u1ecb Ihe",font=FB(19),fill=GREY)
d.text((2500,32),"CHAR_ADANNA_COSTUME_BREAKDOWN  ·  V002",font=FB(19),fill=TAN,anchor='rs')
d.text((2500,60),"STATUS: UNAPPROVED — PENDING CD",font=FR(18),fill=WHITE,anchor='rs')

d.text((60,100),"ADANNA — COSTUME BREAKDOWN",font=FB(44),fill=WHITE)
d.line([(60,168),(2500,168)],fill=LINE,width=2)

# ---------------- status banner (hatched)
bx,by,bw,bh=60,184,2440,44
d.rectangle([bx,by,bx+bw,by+bh],fill=(26,20,22),outline=(120,64,56),width=2)
for i in range(-bh,bw,22):
    d.line([(bx+i,by+bh),(bx+i+bh,by)],fill=(52,34,34),width=1)
d.text((bx+18,by+12),"UNAPPROVED — PENDING CD — COSTUME BREAKDOWN  ·  NOT CANON  ·  OAD-02 IDENTITY LOCKS APPLIED",font=FB(20),fill=(238,206,196))

# ---------------- panels
port=Image.open('work5/crop_portrait.png'); face=Image.open('work5/trim_face.png')
temp=Image.open('work5/trim_temple.png'); arm=Image.open('work5/trim_armlet.png')
pend=Image.open('work5/trim_pendant.png'); wrap=Image.open('work5/trim_wrap.png')
strap=Image.open('work5/trim_strap.png')

AX,AY,AW,AH=60,250,500,743
panel(port,(AX,AY,AW,AH),"FRONT / THREE-QUARTER — approved plate, native crop")
sc=AW/port.width
def A(x,y): return (AX+x*sc, AY+y*sc)
anchors=[(1,(434,225)),(2,(380,442)),(3,(289,690)),(4,(377,770)),(5,(244,866)),(6,(625,918))]
for n,(x,y) in anchors:
    px,py=A(x,y); tag(px,py,n)

panel(temp,(600,250,300,330),"LEFT TEMPLE — 3 cuffs + 2 coral")
panel(arm,(920,250,300,330),"COILED ARMLET — ~9 wires")
panel(face,(1240,250,300,330),"FACE — scar, LEFT cheek only")

panel(pend,(600,636,300,268),"SPIRAL PENDANT (fiction)")
panel(wrap,(920,636,300,268),"INDIGO HAND-WOVEN WRAP")
panel(strap,(1240,636,300,268),"LEATHER STRAP · WEAR")

# ---------------- right column
TX=1580
d.text((TX,262),"IDENTITY LOCKS — APPLIED",font=FB(20),fill=TAN)
locks=["Deep brown skin. Thin micro-braids, top half in a high knot.",
       "3 bronze cuffs + 2 coral beads — LEFT temple ONLY (viewer-right).",
       "Diagonal scar — LEFT cheekbone ONLY.",
       "Coiled aged-bronze armlet, ~9 slender wires — LEFT upper arm ONLY.",
       "RIGHT temple, RIGHT cheek, RIGHT arm: plain by design.",
       "Spiral aged-bronze pendant (fictional, not a documented emblem).",
       "Hand-woven indigo cotton strapless bandeau wrap.",
       "Vegetable-tanned leather strap with subtle shoulder stud.",
       "No gold anywhere on the costume.",
       "Blade at LEFT hip for right-hand cross-draw — construction CQ-9 OPEN."]
y=300
for t in locks:
    d.text((TX,y),"·",font=FB(16),fill=TAN)
    d.text((TX+16,y),t,font=FR(16),fill=WHITE); y+=23
y+=14
d.text((TX,y),"TAG KEY",font=FB(20),fill=TAN); y+=30
key=["1  LEFT temple — 3 bronze cuffs + 2 coral beads",
     "2  LEFT cheekbone — diagonal scar",
     "3  Spiral bronze pendant",
     "4  Leather strap (shoulder to hip)",
     "5  Indigo cotton bandeau",
     "6  LEFT upper arm — coiled bronze armlet"]
for t in key:
    d.text((TX,y),t,font=FR(16),fill=WHITE); y+=23
y+=16
d.text((TX,y),"FRAME NOTE",font=FB(20),fill=TAN); y+=30
for t in ["Each panel is a native-resolution crop of the approved",
          "master reference (MD5 901a5009…). Nothing is drawn or",
          "generated here: approved pixels only."]:
    d.text((TX,y),t,font=FR(15),fill=GREY); y+=21

y+=16
d.text((TX,y),"NOT DRAWN — UNRESOLVED (CQ OPEN)",font=FB(20),fill=ALERT); y+=30
for t in ["· Back torso construction — undesigned",
          "· Lower-body garment type and length — undesigned",
          "· Fasteners, closures and pendant cord — undesigned",
          "· Hand-scale weapon sizing — CQ-9 OPEN",
          "· Blade and scabbard construction — CQ-9 OPEN",
          "· Strap-to-scabbard junction — CQ-9 OPEN",
          "· Right-side plate — absent from the approved set"]:
    d.text((TX,y),t,font=FR(15),fill=WHITE); y+=21

# ---------------- row 3
hatch((60,1030,560,240),"RIGHT SIDE — PLAIN BY DESIGN",
      ["No approved right-side plate exists in the",
       "reference set. The V001 sheet's right profile",
       "was an invented plate and carried beads and a",
       "scar. Not reused, not redrawn: a right plate",
       "must be generated by Original VA and approved",
       "before this panel can be filled."])
hatch((640,1030,560,240),"BACK TORSO — UNRESOLVED",
      ["Construction not designed or approved.",
       "Shown as a placeholder only. Nothing here",
       "may be treated as costume canon."])
hatch((1200,1030,560,240),"LOWER BODY + WEAPON — UNRESOLVED",
      ["Garment construction, fasteners and blade/",
       "scabbard build are open (CQ-9). Position only:",
       "LEFT hip, right-hand cross-draw. No hilt, no",
       "pommel and no skirt are drawn on this sheet."])

# palette
px,py=1800,1030
d.text((px,py),"PALETTE — sampled from the approved sheet",font=FB(18),fill=TAN)
pal=[("#06080D","deep shade"),("#121215","blade-black"),("#241916","skin shadow"),
     ("#283338","indigo shade"),("#403D3E","leather shade"),("#44525C","indigo lit"),
     ("#677A85","mist / highlight")]
x0=px; y0=py+34
for i,(hx,note) in enumerate(pal):
    col=hx; rgb=tuple(int(hx[j:j+2],16) for j in (1,3,5))
    d.rectangle([x0+i*98,y0,x0+i*98+84,y0+58],fill=rgb,outline=LINE)
    d.text((x0+i*98,y0+66),col,font=FR(15),fill=WHITE)
    d.text((x0+i*98,y0+86),note,font=FR(12),fill=GREY)
d.text((px,y0+112),"HAND-WOVEN INDIGO COTTON  /  VEGETABLE-TANNED LEATHER",font=FB(14),fill=GREY)
d.text((px,y0+132),"AGED CAST BRONZE  /  CORAL — NO GOLD",font=FB(14),fill=GREY)

# ---------------- footer
fy=1352
d.line([(60,fy-16),(2500,fy-16)],fill=LINE,width=2)
d.text((60,fy),"UNAPPROVED WORKING SHEET — NOT CANON. Identity locks follow OAD-02 and the approved master reference. Braided styling and indigo cloth are",
       font=FR(15),fill=GREY)
d.text((60,fy+22),"broadly West African forms; the spiral pendant, bead count and bead placement are original fiction, not documented Igbo emblems. Hatched panels are unresolved,",
       font=FR(15),fill=GREY)
d.text((60,fy+44),"not design. Nothing on this sheet may be cited as approved costume canon. V001 is rejected and preserved; this sheet supersedes it as a candidate only.",
       font=FR(15),fill=GREY)

S.save('final/CAND_COSTUME_BREAKDOWN_V002_2560x1440.png')
print('saved', S.size)
