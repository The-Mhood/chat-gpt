from PIL import Image, ImageDraw, ImageFont
import json

BOX=(60,152,1961,1321)
PW,PH=BOX[2]-BOX[0],BOX[3]-BOX[1]
IW,IH=950,584

def font(sz):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']:
        try: return ImageFont.truetype(p, sz)
        except Exception: pass
    return ImageFont.load_default()
FB=font(20); F=font(15); FS=font(13)

def board(outpath, left_src, right_src, title, sub_l, sub_r, lines):
    W=IW*2+40; H=IH+150
    c=Image.new('RGB',(W,H),(13,17,23)); d=ImageDraw.Draw(c)
    def place(src, x, label):
        im=Image.open(src).convert('RGB')
        if im.size!=(PW,PH): im=im.crop(BOX) if im.size==(2560,1440) else im.resize((PW,PH),Image.LANCZOS)
        im=im.resize((IW,IH), Image.LANCZOS); c.paste(im,(x,60))
        d.rectangle([x-1,59,x+IW,60+IH], outline=(90,100,115))
        d.text((x,32), label, font=FB, fill=(235,238,242))
    place(left_src, 13, sub_l)
    place(right_src, IW+27, sub_r)
    d.text((13,8), title, font=FB, fill=(255,255,255))
    y=60+IH+10
    for ln in lines:
        d.text((14,y), ln, font=FS, fill=(168,178,190)); y+=17
    c.save(outpath, quality=93)
    print(outpath, c.size)

T = {
 'VR-008': dict(
   left='masters/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005.jpg',
   right='final/CAND_VR-008_2560x1440.png',
   title='VR-008  COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL  —  V005 (REVIEW REQUIRED)  ->  V006 CANDIDATE (REVIEW REQUIRED)',
   l='ORIGINAL — V005 master, 2560x1440',
   r='CANDIDATE — V006, 2560x1440',
   lines=[
    'DEFECT ADDRESSED: the crack in the sealed plaster panel is illegible — master board "KNOWN ISSUES: the crack in the seal is hard to see."',
    'METHOD: hand retouch on the staged master panel only. The existing faint fracture was deepened, displaced and branched; a lit lip added. No generative pass.',
    'CHANGE OUTSIDE THE ARTWORK PANEL: none — pixel diff outside the panel box (60,152)-(1961,1321) is exactly 0.',
    'RESIDUAL: the fracture is now more prominent than "subtle legibility"; a retoucher would soften the core if the CD prefers it quieter. Scabbard angle untouched (V005 known issue, not in brief).',
    'STATUS: CANDIDATE READY FOR REVIEW — not approved, not filed. Source V005 preserved unchanged.',
   ]),
 'VR-010': dict(
   left='masters/ENV_HOME_SETTLEMENT_WASHING_PLACE_V002.jpg',
   right='final/CAND_VR-010_2560x1440.png',
   title='VR-010  ENV_HOME_SETTLEMENT_WASHING_PLACE  —  V002 (REVIEW REQUIRED)  ->  V003 CANDIDATE (REVIEW REQUIRED)',
   l='ORIGINAL — V002 master, 2560x1440',
   r='CANDIDATE — V003, 2560x1440',
   lines=[
    'DEFECT ADDRESSED: master board "KNOWN ISSUES: the drain still runs across open ground." The bright wet channel crossed the yard and stopped in the open.',
    'RESOLUTION: the channel now discharges into a stone-lined culvert mouth at the foot of the compound wall; the open yard floor is unbroken damp earth.',
    'SECONDARY DRIFT (reported, not intended): the palm-frond screen weave is more open and more regular; the wall reads slightly redder; the background tree line is more visible;',
    '   jar and cup positions shifted slightly and the chewing sticks moved a little. The standing stone, leaf-and-soap, sponge and screen height are preserved.',
    'CHANGE OUTSIDE THE ARTWORK PANEL: none (diff 0). STATUS: CANDIDATE READY FOR REVIEW — not approved, not filed. V002 preserved unchanged.',
   ]),
 'VR-011': dict(
   left='masters/ENV_GATES_DEAD_LANDING_OF_UNCLAIMED_V001.jpg',
   right='final/CAND_VR-011_2560x1440.png',
   title='VR-011  ENV_GATES_DEAD_LANDING_OF_UNCLAIMED  —  V001 (REVIEW REQUIRED)  ->  V002 CANDIDATE (REVIEW REQUIRED)',
   l='ORIGINAL — V001 master, 2560x1440',
   r='CANDIDATE — V002, 2560x1440',
   lines=[
    'DEFECTS ADDRESSED (three, from the master board "KNOWN ISSUES"): cloth on the rampart poles read as small flags; canoes fewer and scattered than "hundreds"; river very bright against the bank.',
    'RESOLUTION: every strip now hangs straight down from its pole as limp rectangular cloth; the canoe field is far denser in overlapping receding rows; the water is darker and calmer.',
    'RESIDUAL: the strips read as pale uniform cloth and the rhythm along the rampart is more regular than a hand-tied line would be; the poles are barely visible;',
    '   the canoe field is denser but its far edge is still findable; the foreground canoe and its cargo have drifted (bundles, pots, folded cloth re-arranged).',
    'CHAPTER 7 STATUS: still PROPOSED, not canon. No burial-cloth or belief claim is made. CHANGE OUTSIDE PANEL: none (diff 0).',
   ]),
 'EST': dict(
   left='masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING_V005.jpg',
   right='final/CAND_ESTABLISHING_2560x1440.png',
   title='ESTABLISHING VIEW  ENV_LAST_DAUGHTER_ANCESTRAL_REALM_ESTABLISHING  —  V005 (REVIEW REQUIRED)  ->  V006 CANDIDATE (REVIEW REQUIRED)',
   l='ORIGINAL — V005 master, 2560x1440',
   r='CANDIDATE — V006, 2560x1440',
   lines=[
    'NO V006 EXISTS IN DRIVE: the highest Establishing master is V005. V006 was the target version named in the authorisation, so V005 is the source and V006 is the output.',
    'DEFECTS ADDRESSED: master board "the mound is still too regular a cone ... one house in warm daylight (Nneka\'s) is not visible."',
    'RESOLUTION: the mound is rebuilt as an irregular stack of individual houses with stepped shoulders, ladders and stair runs; one low house is lit by warm low sun.',
    'ADDITIONAL CHANGE DECLARED: the generative pass placed a small standing figure in a yard; "figureless by client decision (OAD-40)" — the figure was removed by hand.',
    'RESIDUAL: the overhead reflection of the settlement is more abstract than V005; colours are warmer; foreground compound layout differs. CHANGE OUTSIDE PANEL: none (diff 0).',
   ]),
 'WALL': dict(
   left='masters/ENV_LAST_DAUGHTER_ANCESTRAL_REALM_WALL_OF_HOUSES_V003.jpg',
   right='final/CAND_WALL_OF_HOUSES_2560x1440.png',
   title='WALL OF HOUSES  ENV_LAST_DAUGHTER_ANCESTRAL_REALM_WALL_OF_HOUSES  —  V003 (REVIEW REQUIRED)  ->  V004 CANDIDATE (REVIEW REQUIRED)',
   l='ORIGINAL — V003 master, 2560x1440',
   r='CANDIDATE — V004, 2560x1440',
   lines=[
    'NO V004 EXISTS IN DRIVE: the highest Wall of Houses master is V003. V004 was the target version named in the authorisation, so V003 is the source and V004 is the output.',
    'DEFECTS ADDRESSED: master board "several houses are two-storey blocks. The first settlement at the foot is not distinct. Sealed doorways do not read at this distance."',
    'RESOLUTION: every building is single-storey with one roof and one opening; the foot of the mound carries separate freestanding houses with gaps and paths;',
    '   the sealed doorways are now pale plastered panels with visible cracks, one of them clearly fractured.',
    'RESIDUAL: fog is heavier at the top than V003 and the palette is redder; the mound silhouette is broader. CHANGE OUTSIDE PANEL: none (diff 0).',
   ]),
}
for tag,cfg in T.items():
    board(f'boards/COMPARE_{tag}.jpg', cfg['left'], cfg['right'], cfg['title'], cfg['l'], cfg['r'], cfg['lines'])
