# -*- coding: utf-8 -*-
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "models")
os.makedirs(OUT, exist_ok=True)

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
    dict(slug="at-25-27", sku="AT-25-27", badge="28-30 US tons", cap="55,100-59,500 lb", frames=73,
         extra=dict(reach="69.9 ft", outrigger="27.3 ft", boom="5 hydraulic + 2 manual"),
         chart=[("15.9 ft","32,045 lb"),("22.5 ft","20,130 lb"),("29.4 ft","12,930 lb"),
                ("36.6 ft","9,085 lb"),("44.0 ft","6,880 lb"),("52.0 ft","5,510 lb"),
                ("60.7 ft","4,070 lb"),("69.9 ft","3,065 lb")]),
    dict(slug="at-30", sku="AT-30", badge="33 US tons", cap="66,140 lb", frames=73,
         extra=dict(reach="69.2 ft", outrigger="27.5 ft", boom="5 hydraulic + 2 manual"),
         chart=[("16.1 ft","41,790 lb"),("22.1 ft","27,020 lb"),("26.5 ft","18,885 lb"),
                ("35.9 ft","13,910 lb"),("43.5 ft","11,585 lb"),("51.5 ft","9,570 lb"),
                ("60.4 ft","5,985 lb"),("69.2 ft","4,650 lb")]),
    dict(slug="at-35-38", sku="AT-35-38", badge="39-42 US tons", cap="77,160-83,780 lb", frames=73,
         extra=dict(reach="78.2 ft", outrigger="27.5 ft", boom="6 hydraulic + 2 manual"),
         chart=[("15.9 ft","46,970 lb"),("22.6 ft","31,315 lb"),("29.4 ft","22,885 lb"),
                ("36.7 ft","16,720 lb"),("44.1 ft","12,690 lb"),("52.0 ft","10,385 lb"),
                ("60.2 ft","8,675 lb"),("69.1 ft","6,635 lb"),("78.2 ft","5,300 lb")]),
    dict(slug="at-45", sku="AT-45", badge="50 US tons", cap="99,210 lb", frames=73,
         extra=dict(reach="73.2 ft", outrigger="29.7 ft", boom="6 hydraulic + 2 manual"),
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
    dict(slug="at-100", sku="AT-100", badge="110 US tons", cap="220,460 lb", frames=73, extra=None, chart=None, loadchart_img="at-100-loadchart.jpg"),
    dict(slug="at-120", sku="AT-120", badge="132 US tons", cap="264,550 lb", frames=73, extra=None, chart=None, loadchart_img="at-120-loadchart.jpg"),
]

def spec_card(k, v):
    return '<div class="spec"><div class="k">%s</div><div class="v">%s</div></div>' % (k, v)

def build_specs(m):
    if m["extra"]:
        e = m["extra"]
        cards = (spec_card("Rated capacity", m["cap"].replace(" lb"," <b>lb</b>"))
               + spec_card("Max reach", e["reach"].replace(" ft"," <b>ft</b>"))
               + spec_card("Working pressure", "3,626 <b>psi</b>")
               + spec_card("Outrigger spread", e["outrigger"].replace(" ft"," <b>ft</b>")))
        note = ('<p class="note">%s boom sections &middot; 360 degree continuous slewing &middot; '
                'figures for the standard configuration. <a href="../contact/" '
                'style="color:var(--amber)">Request the full spec sheet.</a></p>' % e["boom"])
    else:
        cards = (spec_card("Rated capacity", m["cap"].replace(" lb"," <b>lb</b>"))
               + spec_card("Slewing", "360 <b>deg</b>")
               + spec_card("Working pressure", "3,626 <b>psi</b>")
               + spec_card("Crane type", '<span style="font-size:18px">Hydraulic<br/>knuckle boom</span>'))
        note = ('<p class="note">Detailed load chart, reach diagram and boom configuration available on request. '
                '<a href="../contact/" style="color:var(--amber)">Request the full spec sheet.</a></p>')
    return cards, note

def build_chart(m):
    if m.get("loadchart_img"):
        img = m["loadchart_img"]
        return ('<section class="section bg-soft">\n  <div class="container">\n'
                '    <div class="sec-head" style="margin-bottom:30px"><span class="eyebrow">Load chart</span>\n'
                '      <h2>%s lifting capacity diagram</h2>\n'
                '      <p>Heavy-class lifting curve, 8 hydraulic plus 5 manual sections. Read radius (m) on the horizontal axis against lift height (m) on the vertical. For a US-unit printable chart, <a href="../contact/" style="color:var(--amber)">email info@atlasboom.com</a>.</p>\n'
                '    </div>\n'
                '    <div class="chart-img-wrap"><img src="../assets/images/charts/%s" alt="%s lifting capacity diagram" loading="lazy" /></div>\n'
                '  </div>\n</section>\n' % (m["sku"], img, m["sku"]))
    if not m["chart"]:
        return ""
    rows = "".join('<tr><td>%s</td><td>%s</td></tr>' % (r, c) for r, c in m["chart"])
    boom = m["extra"]["boom"] if m.get("extra") else "standard"
    return ('<section class="section bg-soft">\n  <div class="container">\n'
            '    <div class="sec-head" style="margin-bottom:30px"><span class="eyebrow">Load chart</span>\n'
            '      <h2>%s lifting capacity by reach</h2>\n'
            '      <p>As the boom extends, rated capacity decreases. Figures shown for the %s configuration in US units.</p>\n'
            '    </div>\n'
            '    <div class="chart-wrap"><table class="chart"><thead><tr><th>Working reach</th><th>Max lifting capacity</th></tr></thead>'
            '<tbody>%s</tbody></table></div>\n  </div>\n</section>\n' % (m["sku"], boom, rows))

def build_headseo(m):
    url = "https://atlasboom.com/models/%s.html" % m["slug"]
    img = "https://atlasboom.com/assets/images/models/%s-hero.jpg" % m["slug"]
    title = "%s Hydraulic Knuckle Boom Crane — %s | Atlas Boom" % (m["sku"], m["cap"])
    desc = ("%s hydraulic knuckle boom crane with %s rated lifting capacity. "
            "Full specs, load chart and gallery. Atlas Boom, a brand of Atlas Chicago LLC." % (m["sku"], m["cap"]))
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
<meta name="description" content="{{SKU}} hydraulic knuckle boom crane, {{CAP}} rated lifting capacity. Full specs, load chart and gallery." />
<meta name="theme-color" content="#0A0B0D" />
{{HEADSEO}}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%230A0B0D'/%3E%3Cpath d='M9 24 V10 L23 16.5 M9 24 H22 M23 16.5 V20' stroke='%23F5A623' stroke-width='2.6' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@500;600;700;800;900&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="../assets/css/shared.css" />
<style>
/* === Model page specific (3D viewer, gallery, specs, chart, lightbox) === */
.viewer{position:relative;height:100vh;background:radial-gradient(120% 90% at 50% 0%,#161b26 0%,#0c0f16 70%)}
.viewer-stage{position:sticky;top:0;height:100vh;overflow:hidden}
.viewer-stage::after{content:"";position:absolute;inset:0;background:radial-gradient(80% 70% at 50% 45%,transparent 45%,rgba(10,11,13,.62) 100%);pointer-events:none}
#frameImg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.viewer-cap{position:absolute;left:0;right:0;top:118px;text-align:center;z-index:2;pointer-events:none;text-shadow:0 4px 34px rgba(0,0,0,.78),0 2px 8px rgba(0,0,0,.55)}
.viewer-cap .eyebrow{justify-content:center}
.viewer-cap h1{font-family:var(--display);font-weight:900;font-size:clamp(54px,9vw,128px);margin-top:12px;letter-spacing:-1.6px;line-height:.86;text-transform:uppercase}
.viewer-cap .cls{color:var(--steel);font-family:var(--mono);font-size:13px;letter-spacing:2.2px;text-transform:uppercase;margin-top:14px;display:inline-block}
.scroll-hint{position:absolute;bottom:30px;left:50%;transform:translateX(-50%);z-index:2;display:flex;flex-direction:column;align-items:center;gap:8px;color:var(--muted);font-family:var(--mono);font-size:11px;letter-spacing:2.2px;text-transform:uppercase}
.scroll-hint svg{width:18px;height:18px;animation:bob 1.8s infinite}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(7px)}}

.gallery{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:30px}
@media(min-width:900px){.gallery{grid-template-columns:repeat(5,1fr);gap:16px}}
.gallery figure{border:1px solid var(--line);border-radius:var(--r-card);overflow:hidden;background:var(--surface);cursor:pointer;transition:.35s var(--ease)}
.gallery figure:hover{transform:translateY(-5px);border-color:rgba(245,166,35,.4);background:var(--surface-2)}
.gallery img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block;transition:.5s var(--ease)}
.gallery figure:hover img{transform:scale(1.04)}
.gallery figcaption{font-family:var(--mono);text-transform:uppercase;letter-spacing:1.4px;font-size:11.5px;color:var(--muted);padding:13px 16px}

.spec-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:30px}
.spec{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-card);padding:24px 22px;transition:.25s}
.spec:hover{border-color:rgba(245,166,35,.4);background:var(--surface-2)}
.spec .k{font-family:var(--mono);color:var(--muted-2);font-size:11.5px;letter-spacing:1.5px;text-transform:uppercase}
.spec .v{font-family:var(--display);font-weight:800;font-size:30px;color:#fff;margin-top:8px;line-height:1}
.spec .v b{color:var(--amber);font-weight:500;font-family:var(--mono);font-size:15px;letter-spacing:.3px;margin-left:4px;vertical-align:middle}
.note{color:var(--muted);font-size:15px;margin-top:26px;max-width:62ch}

.chart-wrap{border:1px solid var(--line);border-radius:var(--r-card);overflow:hidden;background:var(--surface)}
.chart-img-wrap{border:1px solid var(--line);border-radius:var(--r-card);overflow:hidden;background:#f5f6f8;padding:24px}
.chart-img-wrap img{width:100%;height:auto;display:block;border-radius:6px}
.chart{width:100%;border-collapse:collapse;font-family:var(--mono);font-variant-numeric:tabular-nums}
.chart thead th{background:rgba(255,255,255,.03);text-align:left;font-family:var(--display);text-transform:uppercase;letter-spacing:1.5px;font-size:12px;color:var(--muted);padding:16px 22px;font-weight:700;border-bottom:1px solid var(--line)}
.chart td{padding:14px 22px;font-size:15.5px;color:var(--text);border-bottom:1px solid rgba(255,255,255,.04)}
.chart tbody tr:last-child td{border-bottom:none}
.chart tbody tr:nth-child(odd){background:rgba(255,255,255,.012)}
.chart td:last-child{color:var(--amber);text-align:right}

.lb{position:fixed;inset:0;background:rgba(5,6,8,.95);display:none;align-items:center;justify-content:center;z-index:200;padding:30px}
.lb.open{display:flex}
.lb img{max-width:88%;max-height:88vh;border-radius:10px}
.lb-close{position:absolute;top:22px;right:26px;color:#fff;font-size:34px;font-family:var(--display);cursor:pointer;line-height:1;z-index:2}
.lb-nav{position:absolute;top:50%;transform:translateY(-50%);width:54px;height:54px;border-radius:50%;background:rgba(255,255,255,.08);border:1px solid var(--line-2);color:#fff;font-size:28px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.2s;user-select:none}
.lb-nav:hover{background:var(--amber);color:#0A0B0D;border-color:var(--amber)}
.lb-prev{left:24px}.lb-next{right:24px}
.lb-cap{position:absolute;bottom:26px;left:0;right:0;text-align:center;color:var(--steel);font-family:var(--mono);text-transform:uppercase;letter-spacing:2px;font-size:12px}

@media(max-width:900px){.spec-grid{grid-template-columns:1fr 1fr}.gallery{grid-template-columns:1fr}.lb-nav{width:44px;height:44px;font-size:24px}.viewer-cap{top:96px}}
</style>
</head>
<body>
<div class="wrap">

<nav class="nav" id="nav"><div class="container nav-inner">
  <a href="../" class="logo">
    <svg class="mark" viewBox="0 0 40 40" aria-label="Atlas Boom"><rect x=".75" y=".75" width="38.5" height="38.5" rx="10" fill="#14181f" stroke="rgba(245,166,35,.28)" stroke-width="1.5"/><path d="M11 29.5 V13 L30 20.5" fill="none" stroke="#F5A623" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M10.5 29.5 H28.5" stroke="#F5A623" stroke-width="3.4" stroke-linecap="round"/><path d="M30 20.5 V25.5" stroke="#F5A623" stroke-width="2.6" stroke-linecap="round"/></svg>
    <span class="wm"><span>ATLAS<b>BOOM</b></span><small>Knuckle Boom Cranes</small></span>
  </a>
  <div class="nav-links">
    <a href="../cranes/" class="active">Cranes</a>
    <a href="../parts/">Parts</a>
    <a href="../specs/">Specs</a>
    <a href="../contact/">Contact</a>
  </div>
  <div class="nav-cta">
    <a href="../contact/" class="btn btn-amber btn-sm">Request a quote</a>
    <button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</div></nav>

<div class="mobile-menu" id="mobileMenu">
  <a href="../cranes/">Cranes</a>
  <a href="../parts/">Parts</a>
  <a href="../specs/">Specs</a>
  <a href="../contact/">Contact</a>
  <a href="../contact/" class="btn btn-amber">Request a quote</a>
</div>

<section class="viewer" id="viewer">
  <div class="viewer-cap">
    <span class="eyebrow">Atlas Boom lineup</span>
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
    <div class="sec-head" style="margin-bottom:24px">
      <span class="eyebrow">Studio gallery</span>
      <h2>Every angle</h2>
    </div>
    <div class="gallery">
      <figure data-full="../assets/images/models/{{SLUG}}-side.jpg" data-cap="Side profile"><img src="../assets/images/models/{{SLUG}}-side.jpg" alt="{{SKU}} side view" loading="lazy" /><figcaption>Side profile</figcaption></figure>
      <figure data-full="../assets/images/models/{{SLUG}}-hero.jpg" data-cap="3/4 hero"><img src="../assets/images/models/{{SLUG}}-hero.jpg" alt="{{SKU}} hero view" loading="lazy" /><figcaption>3/4 hero</figcaption></figure>
      <figure data-full="../assets/images/models/{{SLUG}}-front.jpg" data-cap="Front"><img src="../assets/images/models/{{SLUG}}-front.jpg" alt="{{SKU}} front view" loading="lazy" /><figcaption>Front</figcaption></figure>
      <figure data-full="../assets/images/models/{{SLUG}}-rear.jpg" data-cap="Rear 3/4"><img src="../assets/images/models/{{SLUG}}-rear.jpg" alt="{{SKU}} rear view" loading="lazy" /><figcaption>Rear 3/4</figcaption></figure>
      <figure data-full="../assets/images/models/{{SLUG}}-lowangle.jpg" data-cap="Low angle"><img src="../assets/images/models/{{SLUG}}-lowangle.jpg" alt="{{SKU}} low-angle dramatic view" loading="lazy" /><figcaption>Low angle</figcaption></figure>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="sec-head" style="margin-bottom:24px">
      <span class="eyebrow">Specifications</span>
      <h2>{{SKU}} at a glance</h2>
    </div>
    <div class="spec-grid">{{SPECCARDS}}</div>
    {{SPECNOTE}}
  </div>
</section>
{{CHART}}
<section class="cta-strip">
  <div class="container cta-strip-inner">
    <div>
      <h2>Need the {{SKU}}?</h2>
      <p>Send us your lift, reach and truck class. We respond with a quote and lead time within one business day.</p>
    </div>
    <div style="display:flex;gap:12px;flex-wrap:wrap">
      <a href="../contact/" class="btn btn-amber">Request a quote</a>
      <a href="../cranes/" class="btn btn-ghost">Back to lineup</a>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="../" class="logo">
          <svg class="mark" viewBox="0 0 40 40"><rect x=".75" y=".75" width="38.5" height="38.5" rx="10" fill="#14181f" stroke="rgba(245,166,35,.28)" stroke-width="1.5"/><path d="M11 29.5 V13 L30 20.5" fill="none" stroke="#F5A623" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M10.5 29.5 H28.5" stroke="#F5A623" stroke-width="3.4" stroke-linecap="round"/><path d="M30 20.5 V25.5" stroke="#F5A623" stroke-width="2.6" stroke-linecap="round"/></svg>
          <span class="wm"><span>ATLAS<b>BOOM</b></span><small>Knuckle Boom Cranes</small></span>
        </a>
        <p>Hydraulic knuckle boom cranes built to American load standards. A brand of Atlas Chicago LLC.</p>
      </div>
      <div class="footer-col"><h4>Cranes</h4><a href="../cranes/">All models</a><a href="../specs/">Compare specs</a><a href="../parts/">Parts</a></div>
      <div class="footer-col"><h4>Company</h4><a href="../contact/">Contact</a><a href="../contact/service-areas/">Service areas</a><a href="../contact/">Request a quote</a></div>
      <div class="footer-col"><h4>Reach us</h4><a href="mailto:info@atlasboom.com">info@atlasboom.com</a><a href="../contact/">Chicago, IL</a></div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Atlas Chicago LLC. All rights reserved.</span>
      <span>Atlas Boom &middot; Hydraulic knuckle boom cranes</span>
    </div>
  </div>
</footer>

</div>

<div class="lb" id="lb">
  <span class="lb-close" id="lbClose">&times;</span>
  <button class="lb-nav lb-prev" id="lbPrev" aria-label="Previous">&#8249;</button>
  <img id="lbImg" src="" alt="" />
  <button class="lb-nav lb-next" id="lbNext" aria-label="Next">&#8250;</button>
  <div class="lb-cap" id="lbCap"></div>
</div>

<script src="../assets/js/shared.js"></script>
<script>
(function(){
  var FRAME_COUNT = {{FRAMES}};
  var slug = "{{SLUG}}";
  var viewer = document.getElementById('viewer');
  var frame = document.getElementById('frameImg');
  var hint = document.getElementById('scrollHint');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(FRAME_COUNT > 0 && !reduce){
    var imgs = [];
    for(var i = 1; i <= FRAME_COUNT; i++){
      var im = new Image();
      im.src = "../assets/images/frames/" + slug + "/f-" + String(i).padStart(4, '0') + ".jpg";
      imgs.push(im);
    }
    viewer.style.height = "320vh";
    var lastIdx = -1;
    function onScroll(){
      var rect = viewer.getBoundingClientRect();
      var total = viewer.offsetHeight - window.innerHeight;
      var prog = Math.min(1, Math.max(0, -rect.top / total));
      var idx = Math.min(FRAME_COUNT - 1, Math.floor(prog * (FRAME_COUNT - 1)));
      if(idx !== lastIdx && imgs[idx]){ frame.src = imgs[idx].src; lastIdx = idx; }
    }
    window.addEventListener('scroll', onScroll, {passive:true});
    onScroll();
  } else {
    if(hint) hint.style.display = 'none';
  }

  var figs = [].slice.call(document.querySelectorAll('.gallery figure'));
  var shots = figs.map(function(f){ return {src: f.getAttribute('data-full'), cap: f.getAttribute('data-cap')}; });
  var lb = document.getElementById('lb'), lbImg = document.getElementById('lbImg'), lbCap = document.getElementById('lbCap');
  var idx = 0;
  function show(i){ idx = (i + shots.length) % shots.length; lbImg.src = shots[idx].src; lbCap.textContent = shots[idx].cap; }
  function open(i){ show(i); lb.classList.add('open'); }
  function close(){ lb.classList.remove('open'); }
  figs.forEach(function(f, i){ f.addEventListener('click', function(){ open(i); }); });
  document.getElementById('lbPrev').addEventListener('click', function(e){ e.stopPropagation(); show(idx - 1); });
  document.getElementById('lbNext').addEventListener('click', function(e){ e.stopPropagation(); show(idx + 1); });
  document.getElementById('lbClose').addEventListener('click', close);
  lb.addEventListener('click', function(e){ if(e.target === lb) close(); });
  document.addEventListener('keydown', function(e){
    if(!lb.classList.contains('open')) return;
    if(e.key === 'ArrowLeft') show(idx - 1);
    else if(e.key === 'ArrowRight') show(idx + 1);
    else if(e.key === 'Escape') close();
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
    print("wrote:", m["slug"], "->", m["sku"], ("(+load chart)" if m["chart"] else ""))
print("DONE")
