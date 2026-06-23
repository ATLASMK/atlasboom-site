# -*- coding: utf-8 -*-
import os, re, io
HERE = os.path.dirname(os.path.abspath(__file__))

# old slug -> new slug (first 5 existing models)
slug_map = {"hs-30":"at-10","hs-40":"at-13","hs-50":"at-16","hs-60":"at-20","hs-75-80":"at-25-27"}

# 1) rename image assets models/<old>-<angle>.png -> <new>-<angle>.png
mdir = os.path.join(HERE,"assets","images","models")
for old,new in slug_map.items():
    for a in ("side","hero","front"):
        src=os.path.join(mdir,"%s-%s.png"%(old,a)); dst=os.path.join(mdir,"%s-%s.png"%(new,a))
        if os.path.exists(src): os.rename(src,dst); print("rename img:",os.path.basename(src),"->",os.path.basename(dst))

# 2) rename frames folder frames/<old> -> frames/<new>
fdir = os.path.join(HERE,"assets","images","frames")
for old,new in slug_map.items():
    src=os.path.join(fdir,old); dst=os.path.join(fdir,new)
    if os.path.isdir(src): os.rename(src,dst); print("rename frames:",old,"->",new)

# 3) edit generator _gen_pages.py (slug + sku + frames key)
gp=os.path.join(HERE,"_gen_pages.py"); s=io.open(gp,encoding="utf-8").read()
gen_reps={'slug="hs-30"':'slug="at-10"','slug="hs-40"':'slug="at-13"','slug="hs-50"':'slug="at-16"',
          'slug="hs-60"':'slug="at-20"','slug="hs-75-80"':'slug="at-25-27"',
          'sku="AT10"':'sku="AT-10"','sku="AT13"':'sku="AT-13"','sku="AT16"':'sku="AT-16"',
          'sku="AT20"':'sku="AT-20"','sku="AT25"':'sku="AT-25-27"','"hs-30": 73':'"at-10": 73'}
for a,b in gen_reps.items(): s=s.replace(a,b)
io.open(gp,"w",encoding="utf-8").write(s)
print("generator guncellendi")

# 4) edit index.html
ip=os.path.join(HERE,"index.html"); h=io.open(ip,encoding="utf-8").read()
# 4a card hrefs + img srcs (first 5)
for old,new in slug_map.items():
    h=h.replace("models/%s.html"%old,"models/%s.html"%new)
    h=h.replace("models/%s-hero.png"%old,"models/%s-hero.png"%new)
# 4b display SKUs ATxx -> AT-xx (ranges special), single regex pass
def skuf(m):
    n=m.group(1)
    if n=="25": return "AT-25-27"
    if n=="35": return "AT-35-38"
    return "AT-"+n
h=re.sub(r"\bAT(\d+)\b", skuf, h)
io.open(ip,"w",encoding="utf-8").write(h)
print("index.html guncellendi | kalan duz ATxx:", bool(re.search(r'\bAT\d', h)))
