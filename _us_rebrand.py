# -*- coding: utf-8 -*-
import io, sys
P = r"C:\Users\PC\CLAUDE\ATLASBOOM.COM and ATLASWAY.NET PREMİUM DESİGN\atlasboom\index.html"
with io.open(P, encoding="utf-8") as f:
    s = f.read()
orig = s
n = 0
def rep(a, b, required=True):
    global s, n
    c = s.count(a)
    if c == 0 and required:
        print("!! BULUNAMADI:", repr(a[:50]))
    s = s.replace(a, b); n += c
    return c

master = [
 ("HS 30","AT10","10 Ton","11 US tons","10,000 kg","22,050 lb"),
 ("HS 40","AT13","13 Ton","14 US tons","13,000 kg","28,660 lb"),
 ("HS 50","AT16","16 Ton","18 US tons","16,000 kg","35,270 lb"),
 ("HS 60","AT20","20 Ton","22 US tons","20,000 kg","44,090 lb"),
 ("HS 75-80","AT25","25-27 Ton","28-30 US tons","25,000–27,000 kg","55,100–59,500 lb"),
 ("HS 90","AT30","30 Ton","33 US tons","30,000 kg","66,140 lb"),
 ("HS 105-114","AT35","35-38 Ton","39-42 US tons","35,000–38,000 kg","77,160–83,780 lb"),
 ("HS 135","AT45","45 Ton","50 US tons","45,000 kg","99,210 lb"),
 ("HS 165","AT55","55 Ton","61 US tons","55,000 kg","121,250 lb"),
 ("HS 195","AT65","65 Ton","72 US tons","65,000 kg","143,300 lb"),
 ("HS 225","AT75","75 Ton","83 US tons","75,000 kg","165,350 lb"),
 ("HS 300","AT100","100 Ton","110 US tons","100,000 kg","220,460 lb"),
 ("HS 360","AT120","120 Ton","132 US tons","120,000 kg","264,550 lb"),
]
for hs, at, bo, bn, kg, lb in master:
    rep("<h3>%s</h3>" % hs, "<h3>%s</h3>" % at)
    rep('class="model-badge">%s</span>' % bo, 'class="model-badge">%s</span>' % bn)
    rep("<b>%s</b>" % kg, "<b>%s</b>" % lb)
    rep('alt="%s hydraulic' % hs, 'alt="%s hydraulic' % at, required=False)

rep("Lifting capacity <b>", "Rated capacity <b>")

rep("From compact 10-ton units to 120-ton heavy lifters — the full HSA-engineered knuckle boom crane lineup, 13 models for every load class.",
    "From compact 11-US-ton units to 132-US-ton heavy lifters — the full Atlas Boom knuckle boom crane lineup, 13 models for every load class.")

rep('<div class="ct-value"><span id="ctVal">10</span><small> Ton</small></div>',
    '<div class="ct-value"><span id="ctVal">11</span><small> US tons</small></div>')

rep('<span data-i="0" class="on">10T</span><span data-i="3">20T</span><span data-i="5">30T</span><span data-i="7">45T</span><span data-i="10">75T</span><span data-i="12">120T</span>',
    '<span data-i="0" class="on">11</span><span data-i="3">22</span><span data-i="5">33</span><span data-i="7">50</span><span data-i="10">83</span><span data-i="12">132</span>')

rep("var labels = ['10','13','16','20','25-27','30','35-38','45','55','65','75','100','120'];",
    "var labels = ['11','14','18','22','28-30','33','39-42','50','61','72','83','110','132'];")

rep('aria-label="Crane capacity in tons"', 'aria-label="Crane capacity in US tons"')

# Quote dropdown
old_sel = ('<option value="5T">5 Ton</option><option value="10T">10 Ton</option><option value="15T">15 Ton</option>\n'
           '              <option value="20T">20 Ton</option><option value="30T">30 Ton</option><option value="50T">50 Ton</option><option value="Custom">Custom / Not sure</option>')
new_sel = ('<option value="AT10">AT10 — 11 US tons</option><option value="AT13">AT13 — 14 US tons</option>'
           '<option value="AT16">AT16 — 18 US tons</option><option value="AT20">AT20 — 22 US tons</option>'
           '<option value="AT25">AT25 — 28-30 US tons</option><option value="AT30">AT30 — 33 US tons</option>'
           '<option value="AT35">AT35 — 39-42 US tons</option><option value="AT45">AT45 — 50 US tons</option>'
           '<option value="AT55">AT55 — 61 US tons</option><option value="AT65">AT65 — 72 US tons</option>'
           '<option value="AT75">AT75 — 83 US tons</option><option value="AT100">AT100 — 110 US tons</option>'
           '<option value="AT120">AT120 — 132 US tons</option><option value="Custom">Custom / Not sure</option>')
rep(old_sel, new_sel)

with io.open(P, "w", encoding="utf-8") as f:
    f.write(s)
print("Toplam degisiklik:", n, "| HSA kaldi mi:", "HSA" in s, "| 'kg' kaldi mi:", " kg<" in s)
