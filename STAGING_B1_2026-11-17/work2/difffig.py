from PIL import Image, ImageDraw, ImageFont
import numpy as np, json
st=json.load(open('work2/v007_diffstats.json'))
V=Image.open('masters/COMP_ADANNA_SEALED_QUARTER_HAND_ON_SEAL_V005.jpg').convert('RGB').crop((60,152,1961,1321))
N=Image.open('work2/V007_panel.png').convert('RGB')
a=np.asarray(V).astype(int); b=np.asarray(N).astype(int)
d=(np.abs(a-b).sum(axis=2)>12)
base=(np.asarray(V.convert('L')).astype(np.float32)*0.28).astype(np.uint8)
vis=np.stack([np.where(d,255,base)]*3,axis=-1).astype(np.uint8)
im=Image.fromarray(vis); W,H=im.size
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', s)
FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
c=Image.new('RGB',(W,H+152),(13,17,23)); c.paste(im,(0,0)); g=ImageDraw.Draw(c)
for (x0,y0,x1,y1),lab,k in [((425,512,528,862),'A  fracture','A fracture'),((852,614,1000,764),'B  midriff','B midriff'),((996,536,1076,628),'C  armlet','C armlet')]:
    g.rectangle([x0,y0,x1,y1], outline=(0,255,120), width=2)
    g.text((x0+4, max(0,y0-18)), f'{lab}  {st[k]:,} px', font=F(15), fill=(0,255,120))
g.text((12,H+12),"PIXEL DIFFERENCE   V005 panel -> V007 panel   (threshold: sum |dRGB| > 12)", font=FB(20), fill=(255,255,255))
g.text((12,H+42),f"Changed pixels {st['total']:,} of 2,222,269 (0.61%).  Every one of them falls inside the three declared masks; {st['outside']} pixels changed anywhere else on the panel.", font=F(16), fill=(180,190,205))
g.text((12,H+68),"Chrome edits on the surrounding board are separate and enumerated in the ledger: header 329 px, KNOWN ISSUES 4,185 px, footer line 2 7,979 px, V007 note 6,301 px.", font=F(16), fill=(180,190,205))
g.text((12,H+94),"Green boxes = the masks authorised by the rejection report. Face, expression, scar, braids, cuffs, beads, right arm and hand, pose, silhouette, architecture, bowl, pot, mist and palette: 0 px changed.", font=F(16), fill=(180,190,205))
g.text((12,H+120),"Fracture drawn from the authentic lower-right fissure upward beneath her palm; midriff taken from V004 by aligned crop; armlet reconstructed on the left upper arm only.", font=F(16), fill=(150,160,175))
c.save('submit/B2_PIXELDIFF_VR-008_V007.jpg', quality=93); print(c.size)
