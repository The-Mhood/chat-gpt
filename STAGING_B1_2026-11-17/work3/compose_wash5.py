from PIL import Image, ImageDraw, ImageFont
BG=(9,13,24); TAN=(164,139,93); BODY=(204,202,195); GREY=(153,157,169)
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)

M=Image.open('masters/ENV_HOME_SETTLEMENT_WASHING_PLACE_V002.jpg').convert('RGB')
P=Image.open('work3/WASH_V004_panel.png').convert('RGB')   # V004 artwork, unchanged
out=M.copy(); out.paste(P,(60,152)); d=ImageDraw.Draw(out)

def raw(x,y,t,f,fill):
    d.text((x,y),t,font=f,fill=fill)
def right(xr,y,t,f,fill):
    w=d.textlength(t,font=f); assert xr-w>1880,(t,round(xr-w)); d.text((xr,y),t,font=f,fill=fill,anchor='rs')
def check(t,f,x=2001,lim=2545):
    w=d.textlength(t,font=f); assert x+w<lim,(round(x+w),t)

# header asset name -> V005
d.rectangle([1830,32,2546,62], fill=BG)
right(2497,55,'ENV_HOME_SETTLEMENT_WASHING_PLACE_V005',FB(19),TAN)

# --- patches first, then all text (no overlap by draw order)
for rect in [(1986,286,2560,446),(1986,446,2560,556),(1986,556,2560,700)]:
    d.rectangle(rect, fill=BG)

check('READ',FB(19)); raw(2001,312,'READ',FB(19),TAN)
read=["A woven-screen corner against the compound","wall: wet standing stone on flush earth, water","pot and dipper, soap on a leaf, chewing sticks,","sponge."]
y=348
for t in read:
    check(t,F(19)); raw(2001,y,t,F(19),BODY); y+=24

check('CORRECTED SINCE V002',FB(19)); raw(2001,462,'CORRECTED SINCE V002',FB(19),TAN)
corr=["The bright open-ground runoff channel that crossed","the yard is gone. The earth now grades gently, flush","and unbroken: no ditch, no trench, no rut, no water."]
y=494
for t in corr:
    check(t,F(19)); raw(2001,y,t,F(19),BODY); y+=25

check('KNOWN ISSUES',FB(19)); raw(2001,586,'KNOWN ISSUES',FB(19),TAN)
ks=["Outlet off-frame: the only boundary in shot is the","woven screen, so no wall-base pass-through is drawn","and no recess invented. V005 is chrome only \u2014 the","panel is V004 pixels, unchanged."]
y=616
for t in ks:
    check(t,F(19)); raw(2001,y,t,F(19),BODY); y+=25

# footer: whole band repainted (no orphaned V002 tail), no external citation
d.rectangle([940,1326,2556,1440], fill=BG)
ftxt=("Igbo-inspired fictional settlement. Compound layout, mud walls, woven cane screens, steep thatch and carved doors follow documented forms; "
      "every specific design here is invented. The runoff outlet sits off-frame by design and nothing is added to show it. Not approved. "
      "Supersedes V004; V002 and V004 are kept.")
fF=F(13); lines=[]; cur=""
for word in ftxt.split(" "):
    t=(cur+" "+word).strip()
    if d.textlength(t,font=fF) <= 945: cur=t
    else: lines.append(cur); cur=word
lines.append(cur)
assert len(lines)<=4, len(lines)
y=1358
for t in lines:
    assert 984+d.textlength(t,font=fF) < 1945, (round(984+d.textlength(t,font=fF)), t)
    raw(984,y,t,fF,GREY); y+=24
print('footer lines', len(lines))
out.save('final/CAND_VR-010_WASHING_PLACE_V005_2560x1440.png')
print('saved', out.size)
