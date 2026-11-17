from PIL import Image, ImageDraw, ImageFont
BG=(9,13,24); TAN=(164,139,93); BODY=(226,225,217); DIM=(150,158,172); WH=(238,238,232)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
FR=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
im=Image.open('work3/vr008_v9_panel_full.png').convert('RGB')
d=ImageDraw.Draw(im)

def spaced(xy,txt,font,fill,gap=1.2):
    x,y=xy
    for ch in txt:
        d.text((x,y),ch,font=font,fill=fill,anchor='ls'); x+=d.textlength(ch,font=font)+gap

# header
for r in [(1786,26,2556,57),(2085,70,2556,96),(1945,100,2556,128)]:
    d.rectangle(r,fill=BG)
title='COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V009'
tw=d.textlength(title,font=FB(19)); assert 2545-tw>1500,(tw,)
d.text((2545,56),title,font=FB(19),fill=TAN,anchor='rs')
d.text((2545,86),'STATUS: REVIEW REQUIRED',font=FR(18),fill=WH,anchor='rs')
d.text((2545,116),'CHARACTER COMPOSITION \u00b7 CHAPTER 8 \u00b7 EXPLORATORY',font=FR(16),fill=DIM,anchor='rs')

# right column
X0,X1=1956,2545
d.rectangle((1946,168,2556,1190),fill=BG)
y=200
def head(t):
    global y
    spaced((X0,y),t,FB(15),TAN); y+=30
def body(t, indent=0):
    global y
    f=FR(16); w=d.textlength(t,font=f); assert X0+indent+w<X1+2,(round(X0+indent+w),t)
    d.text((X0+indent,y),t,font=f,fill=BODY,anchor='ls'); y+=23
def gap(n=12):
    global y; y+=n

head('LOCATION')
for line in ['CH08-SUB-007 \u00b7 approved environment','SEALED_QUARTER_V003']: body(line)
gap()
head('SOURCES')
for line in ['Environment: approved issue named above.','Character:','CHAR_ADANNA_MASTER_REFERENCE_V001 (OAD-02).','Blade:','WEAPON_ADANNA_PRIMARY_BLADE_V001.']: body(line)
gap()
head('ASSESSMENT')
for line in ['SUBMITTED FOR REVIEW. Version 9. Bare','shoulder and plain leather strap restored','per OAD-02. V006\u2013V008 are preserved, not','deleted; this sheet supersedes V008 only.']: body(line)
gap()
head('SCABBARD CHECK')
for line in ['Length: short, ends at mid-thigh. Placement:','at her left hip, hanging from the belt on the','side nearest the camera. It no longer crosses','the front of her body.']: body(line)
gap()
head('READ')
for line in ['Right hand on the plaster; guard, armlet,','braid cuffs and blade all on her left. Bare','shoulders, no armour.']: body(line)
gap()
head('KNOWN ISSUES')
for line in ['The scabbard hangs at a slight forward angle','and not straight down the thigh. Framing is','carried from V008. Coiled armlet on an','untitled young woman stays open (RQ-10-1);','the hand-on-seal gesture is FICTIONAL and','is not a documented Igbo ritual (U-11).']: body(line)
assert y<1014,(y,)

# provenance block at the foot of the column
gap()
head('PROVENANCE')
for line in ['V009 version. V008\u2019s metal shoulder','pauldron removed; bare shoulder and plain','leather strap per OAD-02. Environment','untouched from approved SEALED_QUARTER_V003.','V006\u2013V008 preserved in 16_REJECTED_DESIGNS.','Establishes no story event or canon.']: body(line)
im.save('final/CAND_VR-008_SEALED_QUARTER_V009_2560x1440.png')
print('saved',im.size)
