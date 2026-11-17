from PIL import Image
import numpy as np, json
V8=np.array(Image.open('submit/B2_CAND_ESTABLISHING_V008_2560x1440.png').convert('RGB'),np.int16)
V9=np.array(Image.open('final/CAND_ESTABLISHING_V009_2560x1440.png').convert('RGB'),np.int16)
d=np.abs(V8[:V9.shape[0],:V9.shape[1]]-V9).max(2)
ch=d>2
def region(x0,y0,x1,y1): return int(ch[y0:y1,x0:x1].sum())
res={
 'total_changed':int(ch.sum()),
 'panel_changed':region(60,152,1961,1321),
 'hall_of_posts_(60,300,470,570)':region(60,300,470,570),
 'left_compound_(60,700,1000,1321)':region(60,700,1000,1321),
 'mound_(1000,152,1901,760)':region(1000,152,1901,760),
 'new_compound_(1180,650,1961,1321)':region(1180,650,1961,1321),
 'sky_top_band_(60,152,1961,320)':region(60,152,1961,320),
 'frame_bottom_(60,1300,1961,1321)':region(60,1300,1961,1321),
 'chrome_column_(1986,0,2560,1440)':region(1986,0,2560,1440),
 'header_(0,0,2560,150)':region(0,0,2560,150),
}
res['pct_of_frame']=round(100*ch[152:1321,60:1961].sum()/(1901*1169),2)
print(json.dumps(res,indent=1))
json.dump(res,open('work6/v9_stats.json','w'),indent=1)
