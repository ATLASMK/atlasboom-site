# -*- coding: utf-8 -*-
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "models")
os.makedirs(OUT, exist_ok=True)

# Each model: slug(file), sku(display), badge(US tons), cap(rated lb), frames, extra(reach/outrigger/boom), chart
MODELS = [
    dict(slug="at-10", sku="AT-10", badge="11 US tons", cap="22,050 lb", frames=73,
         extra=dict(reach="53.3 ft", outrigger="16.9 ft", boom="5 hydraulic + 2 manual"),
         chart=[("13.0 ft","15,290 lb"),("17.6 ft","8,775 lb"),("22.5 ft","5,635 lb"),
                ("27.7 ft","3,900 lb"),("33.5 ft","2,945 lb"),("39.5 ft","2,350 lb"),
                ("46.1 ft","1,700 lb"),("53.3 ft","1,170 lb")]),
    dict(slug="at-13", sku="AT-13", badge="14 US tons", cap="28,660 lb", frames=73,
         extra=dict(reach="69.5 ft", outrigger="18.6 ft", boom="5 hydraulic + 2 manual"),
         chart=[("15.6 ft","16,130 lb"),("22.1 ft","10,440 lb"),("29.0 ft","6,480 lb"),
                ("36.3 ft","4,300 lb"),("43.8 ft","3,120 lb"),("51.8 ft","2,460 lb"),
                ("60.5 ft","1,665 lb"),("69.6 ft","1,058 lb")]),
    dict(slug="at-16", sku="AT-16", badge="18 US tons", cap="35,270 lb", frames=73,
         extra=dict(reach="69.5 ft", outrigger="20.9 ft", boom="5 hydraulic + 2 manual"),
         chart=[("16.1 ft","22,600 lb"),("22.6 ft","13,430 lb"),("29.4 ft","9,570 lb"),
                ("36.6 ft","7,100 lb"),("44.3 ft","5,340 lb"),("52.3 ft","4,150 lb"),
                ("61.0 ft","3,150 lb"),("69.6 ft","2,270 lb")]),
    dict(slug="at-20", sku="AT-20", badge="22 US tons", cap="44,090 lb", frames=73,
         extra=dict(reach="69.9 ft", outrigger="25.0 ft", boom="5 hydraulic + 2 manual"),
         chart=[("15.9 ft","25,860 lb"),("22.5 ft","16,655 lb"),("29.4 ft","11,080 lb"),
                ("36.6 ft","7,650 lb"),("44.1 ft","5,720 lb"),("52.2 ft","3,870 lb"),
                ("60.9 ft","3,405 lb"),("69.9 ft","2,580 lb")]),
    dict(slug="at-25-27", sku="AT-25-27", badge="28–30 US tons", cap="55,100–59,500 lb", frames=73,
         extra=dict(reach="69.9 ft", outrigger="27.3 ft", boom="5 hydraulic + 2 manual"),
         chart=[("15.9 ft","32,045 lb"),("22.5 ft","20,130 lb"),("29.4 ft","12,930 lb"),
                ("36.6 ft","9,085 lb"),("44.0 ft","6,880 lb"),("52.0 ft","5,510 lb"),
                ("60.7 ft","4,070 lb"),("69.9 ft","3,065 lb")]),
    dict(slug="at-30", sku="AT-30", badge="33 US tons", cap="66,140 lb", frames=73,
         extra=dict(reach="69.2 ft", outrigger="27.5 ft", boom="5 hydraulic + 2 manual"),
         chart=[("16.1 ft","41,790 lb"),("22.1 ft","27,020 lb"),("26.5 ft","18,885 lb"),
                ("35.9 ft","13,910 lb"),("43.5 ft","11,585 lb"),("51.5 ft","9,570 lb"),
                ("60.4 ft","5,985 lb"),("69.2 ft","4,650 lb")]),
    dict(slug="at-35-38", sku="AT-35-38", badge="39–42 US tons", cap="77,160–83,780 lb", frames=73,
         extra=dict(reach="78.2 ft", outrigger="27.5 ft", boom="6 hydraulic + 2 manual"),
         chart=[("15.9 ft","46,970 lb"),("22.6 ft","31,315 lb"),("29.4 ft","22,885 lb"),
                ("36.7 ft","16,720 lb"),("44.1 ft","12,690 lb"),("52.0 ft","10,385 lb"),
                ("60.2 ft","8,675 lb"),("69.1 ft","6,635 lb"),("78.2 ft","5,300 lb")]),
    dict(slug="at-45", sku="AT-45", badge="50 US tons", cap="99,210 lb", frames=73,
         extra=dict(reach="73.2 ft", outrigger="29.7 ft", boom="5 hydraulic + 2 manual"),
         chart=[("18.0 ft","52,920 lb"),("24.6 ft","38,075 lb"),("31.3 ft","28,935 lb"),
                ("38.7 ft","21,375 lb"),("46.1 ft","16,655 lb"),("54.6 ft","13,505 lb"),
                ("63.8 ft","10,550 lb"),("73.2 ft","8,335 lb")]),
    dict(slug="at-55", sku="AT-55", badge="61 US tons", cap="121,250 lb", frames=73,
         extra=dict(reach="81.4 ft", outrigger="29.7 ft", boom="6 hydraulic + 2 manual"),
         chart=[("18.5 ft","61,520 lb"),("25.1 ft","42,650 lb"),("31.8 ft","32,165 lb"),
                ("39.0 ft","24,715 lb"),("46.9 ft","19,300 lb"),("54.8 ft","15,665 lb"),
                ("62.8 ft","13,130 lb"),("71.9 ft","11,300 lb"),("81.4 ft","8,950 lb")]),
    dict(slug="at-65", sku="AT-65", badge="72 US tons", cap="143,300 lb", frames=73,
         extra=dict(reach="81.4 ft", outrigger="29.7 ft", boom="6 hydraulic + 2 manual"),
         chart=[("18.5 ft","61,520 lb"),("25.1 ft","42,650 lb"),("31.8 ft","32,165 lb"),
                ("39.0 ft","24,715 lb"),("46.9 ft","19,300 lb"),("54.8 ft","15,665 lb"),
                ("62.8 ft","13,130 lb"),("71.9 ft","11,300 lb"),("81.4 ft","8,950 lb")]),
    dict(slug="at-75", sku="AT-75", badge="83 US tons", cap="165,350 lb", frames=73,
         extra=dict(reach="61.7 ft", outrigger="36.3 ft", boom="7 hydraulic + 2 manual"),
         chart=[("17.7 ft","87,965 lb"),("22.9 ft","66,580 lb"),("28.5 ft","54,785 lb"),
                ("34.4 ft","42,660 lb"),("40.6 ft","35,605 lb"),("47.2 ft","30,095 lb"),
                ("53.7 ft","25,840 lb"),("61.7 ft","20,170 lb")]),
    dict(slug="at-100", sku="AT-100", badge="110 US tons", cap="220,460 lb", frames=73, extra=None, chart=None),
    dict(slug="at-120", sku="AT-120", badge="132 US tons", cap="264,550 lb", frames=73, extra=None, chart=None),
]

def spec_card(k, v):
    return '<div class="spec"><div class="k">%s</div><div class="v">%s</div></div>' % (k, v)

def build_specs(m):
    if m["extra"]:
        e = m["extra"]
        cards = (spec_card("Rated Capacity", m["cap"].replace(" lb"," <b>lb</b>"))
               + spec_card("Max Reach", e["reach"].replace(" ft"," <b>ft</b>"))
               + spec_card("Working Pressure", "3,626 <b>psi</b>")
               + spec_card("Outrigger Spread", e["outrigger"].replace(" ft"," <b>ft</b>")))
        note = ('<p class="note">%s boom sections &middot; 360&deg; continuous slewing &middot; '
                'figures for the standard configuration. <a href="../index.html#quote" '
                'style="color:var(--amber)">Request the full spec sheet.</a></p>' % e["boom"])
    else:
        cards = (spec_card("Rated Capacity", m["cap"].replace(" lb"," <b>lb</b>").replace(" US tons"," <b>US tons</b>"))
               + spec_card("Slewing Angle", "360<b>&deg;</b>")
               + spec_card("Working Pressure", "3,626 <b>psi</b>")
               + spec_card("Crane Type", '<span style="font-size:20px">Hydraulic<br/>Knuckle Boom</span>'))
        note = ('<p class="note">Detailed load chart, reach diagram and boom configuration available on request '
                '&mdash; <a href="../index.html#quote" style="color:var(--amber)">request the full spec sheet.</a></p>')
    return cards, note

def build_chart(m):
    if not m["chart"]:
        return ""
    rows = "".join('<tr><td>%s</td><td>%s</td></tr>' % (r, c) for r, c in m["chart"])
    boom = m["extra"]["boom"] if m.get("extra") else "standard"
    return ('<section class="section">\n  <div class="container">\n'
            '    <span class="eyebrow-line">Load Chart</span>\n'
            '    <h2>%s Lifting Capacity by Reach</h2>\n'
            '    <p class="note" style="margin-top:0;margin-bottom:24px">As the boom extends, rated capacity decreases. '
            'Figures shown for the %s configuration (US units).</p>\n'
            '    <table class="chart"><thead><tr><th>Working Reach</th><th>Max Lifting Capacity</th></tr></thead>'
            '<tbody>%s</tbody></table>\n  </div>\n</section>\n' % (m["sku"], boom, rows))

def build_headseo(m):
    url = "https://atlasboom.com/models/%s.html" % m["slug"]
    img = "https://atlasboom.com/assets/images/models/%s-hero.jpg" % m["slug"]
    title = "%s Hydraulic Knuckle Boom Crane — %s | Atlas Boom" % (m["sku"], m["cap"])
    desc = ("%s truck-mounted hydraulic knuckle boom crane — %s rated lifting capacity. "
            "Specs, load chart and gallery. Distributed by Atlas Chicago LLC across the USA." % (m["sku"], m["cap"]))
    product = {
        "@context": "https://schema.org", "@type": "Product",
        "name": "Atlas Boom %s Hydraulic Knuckle Boom Crane" % m["sku"],
        "image": img, "description": desc, "sku": m["sku"],
        "brand": {"@type": "Brand", "name": "Atlas Boom"},
        "category": "Hydraulic Knuckle Boom Crane",
        "offers": {"@type": "Offer", "url": url, "availability": "https://schema.org/InStock",
                   "priceCurrency": "USD", "seller": {"@type": "Organization", "name": "Atlas Chicago LLC"}},
    }
    tags = [
        '<link rel="canonical" href="%s" />' % url,
        '<meta name="robots" content="index, follow" />',
        '<meta property="og:type" content="product" />',
        '<meta property="og:title" content="%s" />' % title,
        '<meta property="og:description" content="%s" />' % desc,
        '<meta property="og:url" content="%s" />' % url,
        '<meta property="og:image" content="%s" />' % img,
        '<meta property="og:site_name" content="Atlas Boom" />',
        '<meta name="twitter:card" content="summary_large_image" />',
        '<meta name="twitter:title" content="%s" />' % title,
        '<meta name="twitter:image" content="%s" />' % img,
        '<script type="application/ld+json">%s</script>' % json.dumps(product, ensure_ascii=False),
    ]
    return "\n".join(tags)

TPL = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{{SKU}} Hydraulic Knuckle Boom Crane — {{CAP}} | Atlas Boom</title>
<meta name="description" content="{{SKU}} truck-mounted hydraulic knuckle boom crane — {{CAP}} rated lifting capacity. Specs, load chart and gallery. Distributed by Atlas Boom across the USA." />
<meta name="theme-color" content="#0A0B0D" />
{{HEADSEO}}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%230A0B0D'/%3E%3Cpath d='M6 22h20M9 22V9l14 4' stroke='%23F5A623' stroke-width='2.4' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
<style>
:root{--bg:#0A0B0D;--panel:#111318;--card:#141820;--amber:#F5A623;--amber-bright:#ffba48;--steel:#C0C8D4;--text:#fff;--muted:#8b93a1;--line:rgba(255,255,255,.08);--line-strong:rgba(255,255,255,.14);--ease:cubic-bezier(.16,1,.3,1);--maxw:1180px}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Inter',system-ui,sans-serif;line-height:1.65;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
h1,h2,h3{font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:.5px;line-height:1.02}
.container{width:100%;max-width:var(--maxw);margin:0 auto;padding:0 24px}
.btn{display:inline-flex;align-items:center;gap:9px;font-family:'Barlow Condensed',sans-serif;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;font-size:16px;padding:14px 28px;border-radius:10px;transition:.35s var(--ease)}
.btn-amber{background:var(--amber);color:#0A0B0D;box-shadow:0 10px 30px -10px rgba(245,166,35,.35)}
.btn-amber:hover{background:var(--amber-bright);transform:translateY(-2px)}
.btn-ghost{border:1.5px solid var(--line-strong);color:#fff}
.btn-ghost:hover{border-color:var(--amber);color:var(--amber)}
.btn svg{width:16px;height:16px}
.nav{position:fixed;top:0;left:0;right:0;z-index:100;transition:.4s var(--ease)}
.nav.scrolled{background:rgba(10,11,13,.72);backdrop-filter:blur(18px);border-bottom:1px solid var(--line)}
.nav-inner{display:flex;align-items:center;justify-content:space-between;height:74px}
.logo{display:flex;align-items:center;gap:10px;font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:23px;text-transform:uppercase}
.logo b{color:var(--amber)}
.logo svg{width:32px;height:32px}
.nav-back{font-family:'Barlow Condensed',sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:1px;font-size:15px;color:var(--steel);display:flex;align-items:center;gap:7px;transition:.2s}
.nav-back:hover{color:var(--amber)}
.nav-back svg{width:16px;height:16px}
@media(max-width:680px){.nav-back span{display:none}}
.viewer{position:relative;height:100vh;background:radial-gradient(120% 90% at 50% 0%,#161b26 0%,#0c0f16 70%)}
.viewer-stage{position:sticky;top:0;height:100vh;overflow:hidden}
.viewer-stage::after{content:"";position:absolute;inset:0;background:radial-gradient(80% 70% at 50% 45%,transparent 45%,rgba(10,11,13,.55) 100%);pointer-events:none}
#frameImg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.viewer-cap{position:absolute;left:0;right:0;top:104px;text-align:center;z-index:2;pointer-events:none;text-shadow:0 4px 34px rgba(0,0,0,.78),0 2px 8px rgba(0,0,0,.55)}
.viewer-cap .eyebrow{display:inline-block;font-family:'Barlow Condensed',sans-serif;letter-spacing:3px;text-transform:uppercase;color:var(--amber);font-size:13px;font-weight:600}
.viewer-cap h1{font-size:clamp(44px,8vw,96px);margin-top:6px}
.viewer-cap .cls{color:var(--steel);font-family:'Barlow Condensed';font-size:20px;letter-spacing:2px;text-transform:uppercase}
.scroll-hint{position:absolute;bottom:26px;left:50%;transform:translateX(-50%);z-index:2;display:flex;flex-direction:column;align-items:center;gap:6px;color:var(--muted);font-size:11px;letter-spacing:2px;text-transform:uppercase}
.scroll-hint svg{width:18px;height:18px;animation:bob 1.8s infinite}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(7px)}}
.section{padding:96px 0;position:relative}
.eyebrow-line{font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:3px;font-weight:600;color:var(--amber);font-size:14px;display:inline-flex;align-items:center;gap:10px;margin-bottom:14px}
.eyebrow-line::before{content:"";width:28px;height:2px;background:var(--amber)}
.section h2{font-size:clamp(30px,4.5vw,48px);margin-bottom:14px}
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:30px}
.gallery figure{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--card);cursor:pointer;transition:.35s var(--ease)}
.gallery figure:hover{transform:translateY(-5px);border-color:var(--amber)}
.gallery img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block}
.gallery figcaption{font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:1px;font-size:14px;color:var(--steel);padding:11px 14px}
.specs{background:var(--panel);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.spec-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:30px}
.spec{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:26px 22px}
.spec .k{color:var(--muted);font-size:13px;letter-spacing:1px;text-transform:uppercase}
.spec .v{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:30px;color:#fff;margin-top:6px}
.spec .v b{color:var(--amber)}
.note{color:var(--muted);font-size:15px;margin-top:26px}
.chart{width:100%;border-collapse:collapse;border:1px solid var(--line);border-radius:12px;overflow:hidden}
.chart th{background:var(--amber);color:#0A0B0D;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:1px;font-size:15px;text-align:left;padding:14px 22px}
.chart td{padding:14px 22px;border-top:1px solid var(--line);font-family:'Barlow Condensed',sans-serif;font-size:20px;color:#fff}
.chart tbody tr:nth-child(even){background:var(--card)}
.chart td:last-child{color:var(--amber)}
.cta{text-align:center}
.cta h2{font-size:clamp(30px,4.5vw,52px);margin-bottom:14px}
.cta p{color:var(--muted);max-width:520px;margin:0 auto 28px}
.cta-actions{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.lb{position:fixed;inset:0;background:rgba(5,6,8,.95);display:none;align-items:center;justify-content:center;z-index:200;padding:30px}
.lb.open{display:flex}
.lb img{max-width:88%;max-height:88vh;border-radius:10px}
.lb-close{position:absolute;top:22px;right:26px;color:#fff;font-size:34px;font-family:'Barlow Condensed';cursor:pointer;line-height:1;z-index:2}
.lb-nav{position:absolute;top:50%;transform:translateY(-50%);width:56px;height:56px;border-radius:50%;background:rgba(255,255,255,.08);border:1px solid var(--line-strong);color:#fff;font-size:30px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.2s;user-select:none}
.lb-nav:hover{background:var(--amber);color:#0A0B0D;border-color:var(--amber)}
.lb-prev{left:24px}.lb-next{right:24px}
.lb-cap{position:absolute;bottom:26px;left:0;right:0;text-align:center;color:var(--steel);font-family:'Barlow Condensed';text-transform:uppercase;letter-spacing:2px;font-size:15px}
footer{border-top:1px solid var(--line);padding:34px 0;text-align:center;color:var(--muted);font-size:14px}
@media(max-width:880px){.spec-grid{grid-template-columns:1fr 1fr}.gallery{grid-template-columns:1fr}.lb-nav{width:46px;height:46px;font-size:26px}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;scroll-behavior:auto!important}}
</style>
</head>
<body>
<nav class="nav" id="nav">
  <div class="container nav-inner">
    <a href="../index.html" class="logo"><svg viewBox="0 0 34 34" fill="none"><rect width="34" height="34" rx="8" fill="#141820" stroke="#F5A623" stroke-opacity=".4"/><path d="M7 24h20M10 24V10l14 4M10 14l5-4" stroke="#F5A623" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg> ATLAS <b>BOOM</b></a>
    <a href="../index.html#models" class="nav-back"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M19 12H5M11 18l-6-6 6-6" stroke-linecap="round" stroke-linejoin="round"/></svg> <span>All Models</span></a>
    <a href="../index.html#quote" class="btn btn-amber">Request a Quote</a>
  </div>
</nav>

<section class="viewer" id="viewer">
  <div class="viewer-cap">
    <span class="eyebrow">Atlas Boom Lineup</span>
    <h1>{{SKU}}</h1>
    <div class="cls">{{BADGE}} &middot; Hydraulic Knuckle Boom Crane</div>
  </div>
  <div class="viewer-stage">
    <img id="frameImg" src="../assets/images/models/{{SLUG}}-hero.jpg" alt="{{SKU}} hydraulic knuckle boom crane" />
  </div>
  <div class="scroll-hint" id="scrollHint">Scroll to rotate
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M6 13l6 6 6-6" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow-line">Studio Gallery</span>
    <h2>Every Angle</h2>
    <div class="gallery">
      <figure data-full="../assets/images/models/{{SLUG}}-side.jpg" data-cap="Side Profile"><img src="../assets/images/models/{{SLUG}}-side.jpg" alt="{{SKU}} side view" loading="lazy" /><figcaption>Side Profile</figcaption></figure>
      <figure data-full="../assets/images/models/{{SLUG}}-hero.jpg" data-cap="3/4 Hero"><img src="../assets/images/models/{{SLUG}}-hero.jpg" alt="{{SKU}} hero view" loading="lazy" /><figcaption>3/4 Hero</figcaption></figure>
      <figure data-full="../assets/images/models/{{SLUG}}-front.jpg" data-cap="Front"><img src="../assets/images/models/{{SLUG}}-front.jpg" alt="{{SKU}} front view" loading="lazy" /><figcaption>Front</figcaption></figure>
    </div>
  </div>
</section>

<section class="section specs">
  <div class="container">
    <span class="eyebrow-line">Specifications</span>
    <h2>{{SKU}} at a Glance</h2>
    <div class="spec-grid">{{SPECCARDS}}</div>
    {{SPECNOTE}}
  </div>
</section>
{{CHART}}
<section class="section cta">
  <div class="container">
    <span class="eyebrow-line" style="justify-content:center">Get Started</span>
    <h2>Need the {{SKU}}?</h2>
    <p>Get pricing, lead time and spec recommendations from our team within one business day.</p>
    <div class="cta-actions">
      <a href="../index.html#quote" class="btn btn-amber">Request a Quote</a>
      <a href="../index.html#models" class="btn btn-ghost">Back to Lineup</a>
    </div>
  </div>
</section>

<footer>&copy; 2026 Atlas Boom &middot; Atlas Chicago LLC &middot; Chicago, IL</footer>

<div class="lb" id="lb">
  <span class="lb-close" id="lbClose">&times;</span>
  <button class="lb-nav lb-prev" id="lbPrev" aria-label="Previous">&#8249;</button>
  <img id="lbImg" src="" alt="" />
  <button class="lb-nav lb-next" id="lbNext" aria-label="Next">&#8250;</button>
  <div class="lb-cap" id="lbCap"></div>
</div>

<script>
(function(){
  var nav=document.getElementById('nav');
  function s(){nav.classList.toggle('scrolled',window.scrollY>20);} s();
  window.addEventListener('scroll',s,{passive:true});

  var FRAME_COUNT = {{FRAMES}};
  var slug = "{{SLUG}}";
  var viewer=document.getElementById('viewer');
  var frame=document.getElementById('frameImg');
  var hint=document.getElementById('scrollHint');
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(FRAME_COUNT>0 && !reduce){
    var imgs=[];
    for(var i=1;i<=FRAME_COUNT;i++){var im=new Image();im.src="../assets/images/frames/"+slug+"/f-"+String(i).padStart(4,'0')+".jpg";imgs.push(im);}
    viewer.style.height="320vh";
    var lastIdx=-1;
    function onScroll(){
      var rect=viewer.getBoundingClientRect();
      var total=viewer.offsetHeight-window.innerHeight;
      var prog=Math.min(1,Math.max(0,-rect.top/total));
      var idx=Math.min(FRAME_COUNT-1,Math.floor(prog*(FRAME_COUNT-1)));
      if(idx!==lastIdx && imgs[idx]){frame.src=imgs[idx].src;lastIdx=idx;}
    }
    window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  } else { if(hint) hint.style.display='none'; }

  /* ---- Lightbox with prev/next + keyboard ---- */
  var figs=[].slice.call(document.querySelectorAll('.gallery figure'));
  var shots=figs.map(function(f){return {src:f.getAttribute('data-full'),cap:f.getAttribute('data-cap')};});
  var lb=document.getElementById('lb'),lbImg=document.getElementById('lbImg'),lbCap=document.getElementById('lbCap');
  var idx=0;
  function show(i){idx=(i+shots.length)%shots.length;lbImg.src=shots[idx].src;lbCap.textContent=shots[idx].cap;}
  function open(i){show(i);lb.classList.add('open');}
  function close(){lb.classList.remove('open');}
  figs.forEach(function(f,i){f.addEventListener('click',function(){open(i);});});
  document.getElementById('lbPrev').addEventListener('click',function(e){e.stopPropagation();show(idx-1);});
  document.getElementById('lbNext').addEventListener('click',function(e){e.stopPropagation();show(idx+1);});
  document.getElementById('lbClose').addEventListener('click',close);
  lb.addEventListener('click',function(e){if(e.target===lb)close();});
  document.addEventListener('keydown',function(e){
    if(!lb.classList.contains('open'))return;
    if(e.key==='ArrowLeft')show(idx-1);
    else if(e.key==='ArrowRight')show(idx+1);
    else if(e.key==='Escape')close();
  });
})();
</script>
</body>
</html>
"""

for m in MODELS:
    cards, note = build_specs(m)
    chart = build_chart(m)
    headseo = build_headseo(m)
    html = (TPL.replace("{{HEADSEO}}", headseo)
               .replace("{{SLUG}}", m["slug"]).replace("{{SKU}}", m["sku"])
               .replace("{{BADGE}}", m["badge"]).replace("{{CAP}}", m["cap"])
               .replace("{{FRAMES}}", str(m["frames"]))
               .replace("{{SPECCARDS}}", cards).replace("{{SPECNOTE}}", note)
               .replace("{{CHART}}", chart))
    with open(os.path.join(OUT, m["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("yazildi:", m["slug"], "->", m["sku"], ("(+load chart)" if m["chart"] else ""))
print("DONE")
