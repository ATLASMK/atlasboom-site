# -*- coding: utf-8 -*-
import io, re
P = r"C:\Users\PC\CLAUDE\ATLASBOOM.COM and ATLASWAY.NET PREMİUM DESİGN\atlasboom\index.html"
s = io.open(P, encoding="utf-8").read()
NEW8 = [
 ("30","at-30","AT-30","33 US tons","66,140 lb"),
 ("36","at-35-38","AT-35-38","39–42 US tons","77,160–83,780 lb"),
 ("45","at-45","AT-45","50 US tons","99,210 lb"),
 ("55","at-55","AT-55","61 US tons","121,250 lb"),
 ("65","at-65","AT-65","72 US tons","143,300 lb"),
 ("75","at-75","AT-75","83 US tons","165,350 lb"),
 ("100","at-100","AT-100","110 US tons","220,460 lb"),
 ("120","at-120","AT-120","132 US tons","264,550 lb"),
]
for dt, slug, sku, badge, cap in NEW8:
    card = ('<a class="model-card" data-ton="%s" href="models/%s.html">\n'
            '        <div class="model-thumb"><span class="model-badge">%s</span>\n'
            '          <img class="model-photo" src="assets/images/models/%s-hero.jpg" alt="%s hydraulic knuckle boom crane" loading="lazy" />\n'
            '        </div>\n'
            '        <div class="model-body"><h3>%s</h3><p class="cap">Rated capacity <b>%s</b></p>\n'
            '          <span class="model-specs-btn">View Specs <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span></div>\n'
            '      </a>') % (dt, slug, badge, slug, sku, sku, cap)
    pat = re.compile(r'<article class="model-card" data-ton="%s">.*?</article>' % dt, re.DOTALL)
    s, n = pat.subn(card, s, count=1)
    print(slug, "card replaced:", n)
io.open(P,"w",encoding="utf-8").write(s)
print("kalan <article model-card:", s.count('<article class="model-card"'))
