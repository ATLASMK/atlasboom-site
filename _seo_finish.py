# -*- coding: utf-8 -*-
"""Faz 2 + Faz 3 — integrate services into index.html + technical SEO.
Safe: every index.html edit asserts exactly ONE match before replacing.
Outputs: edits index.html, writes sitemap.xml + robots.txt.
"""
import os, glob, json, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ORIGIN = "https://atlasboom.com"
EMAIL = "info@atlasboom.com"
COMPANY = "Atlas Chicago LLC"
TODAY = "2026-06-23"

CRANE = [("Chicago & Illinois","crane-rental-chicago-il"),("Indiana","crane-rental-indiana"),
         ("Michigan","crane-rental-michigan"),("Milwaukee & Wisconsin","crane-rental-milwaukee-wisconsin"),
         ("Ohio","crane-rental-ohio"),("Pennsylvania","crane-rental-pennsylvania")]
PUMP = [("Chicago & Illinois","concrete-pumping-chicago-illinois"),("Indiana","concrete-pumping-indiana"),
        ("Michigan","concrete-pumping-michigan"),("Milwaukee & Wisconsin","concrete-pumping-milwaukee-wisconsin"),
        ("Ohio","concrete-pumping-ohio"),("Pennsylvania","concrete-pumping-pennsylvania")]
HAUL = [("Illinois","heavy-haul-lowboy-transport-illinois"),("Indiana","heavy-haul-lowboy-transport-indiana"),
        ("Michigan","heavy-haul-lowboy-transport-michigan"),("Wisconsin","heavy-haul-lowboy-transport-wisconsin"),
        ("Ohio","heavy-haul-lowboy-transport-ohio"),("Pennsylvania","heavy-haul-lowboy-transport-pennsylvania")]

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
IC_CRANE = '<svg class="svc-col-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M5 21V8l14 3M5 11l9-5M14 6l5 5M16 11v4a2 2 0 0 1-2 2"/></svg>'
IC_PUMP = '<svg class="svc-col-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 16h11V9H2zM13 11h4l5 3v2h-9M5 19a2 2 0 1 0 0-.01M17 19a2 2 0 1 0 0-.01M9 9V5h3"/></svg>'
IC_HAUL = '<svg class="svc-col-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M1 17h15V7H1zM16 11h4l3 3v3h-7M5 20a2 2 0 1 0 0-.01M18 20a2 2 0 1 0 0-.01"/></svg>'

def col(icon, title, blurb, items):
    links = "".join(
        '<a href="/%s/">%s %s</a>' % (slug, html_label(lbl), ARROW) for lbl, slug in items)
    return ('<article class="svc-col">%s<h3>%s</h3><p>%s</p>'
            '<div class="svc-col-links">%s</div></article>' % (icon, title, blurb, links))

def html_label(s): return s.replace("&", "&amp;")

# assert each slug folder exists
for _, slug in CRANE + PUMP + HAUL:
    assert os.path.isdir(os.path.join(HERE, slug)), "MISSING service folder: " + slug

SERVICES_SECTION = '''
<!-- ============================ SERVICES (regional) ============================ -->
<style>
.svcs{background:linear-gradient(180deg,#0c0e12,#0a0b0d)}
.svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:36px}
.svc-col{background:var(--card,#141820);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:30px 26px;transition:.35s cubic-bezier(.16,1,.3,1)}
.svc-col:hover{border-color:rgba(245,166,35,.5);transform:translateY(-4px)}
.svc-col-ic{width:46px;height:46px;color:#F5A623;margin-bottom:16px}
.svc-col h3{font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;font-size:26px;letter-spacing:.5px;margin-bottom:6px;color:#fff}
.svc-col>p{color:#8b93a1;font-size:14.5px;line-height:1.55;margin-bottom:16px}
.svc-col-links{display:flex;flex-direction:column}
.svc-col-links a{display:flex;align-items:center;justify-content:space-between;gap:10px;color:#C0C8D4;font-size:15px;font-weight:500;padding:11px 0;border-top:1px solid rgba(255,255,255,.07);transition:.2s}
.svc-col-links a:hover{color:#F5A623;padding-left:5px}
.svc-col-links a svg{width:15px;height:15px;opacity:.45;flex:none}
.svc-areas-note{text-align:center;color:#8b93a1;font-size:14.5px;margin-top:34px}
.svc-areas-note b{color:#C0C8D4;font-weight:600}
@media(max-width:860px){.svc-grid{grid-template-columns:1fr}}
</style>
<section class="section svcs" id="services">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Regional Services</span>
      <h2>Crane Rental, Concrete Pumping &amp; Heavy Haul</h2>
      <p>Beyond crane sales, %(company)s provides operated crane rental, concrete pumping, and heavy haul &amp; lowboy transport across six states &mdash; pick your region.</p>
    </div>
    <div class="svc-grid">
      %(crane)s
      %(pump)s
      %(haul)s
    </div>
    <p class="svc-areas-note">Serving <b>Illinois, Indiana, Michigan, Wisconsin, Ohio &amp; Pennsylvania</b> &mdash; and shipping cranes to all 48 states.</p>
  </div>
</section>
''' % {
    "company": COMPANY,
    "crane": col(IC_CRANE, "Crane Rental", "Operated mobile, rough-terrain and boom truck cranes with certified operators.", CRANE),
    "pump":  col(IC_PUMP, "Concrete Pumping", "Boom and line pumps with operators for slabs, foundations and high-rise pours.", PUMP),
    "haul":  col(IC_HAUL, "Heavy Haul &amp; Lowboy", "Permitted oversize / overweight transport on lowboy and RGN trailers.", HAUL),
}

# ---------- LocalBusiness schema for home ----------
HOME_LD = {
    "@context": "https://schema.org", "@type": "LocalBusiness",
    "name": COMPANY, "alternateName": "Atlas Boom", "url": ORIGIN + "/",
    "email": EMAIL, "image": ORIGIN + "/assets/images/hero-industrial.jpg",
    "description": "Hydraulic knuckle boom crane distributor and regional service provider — crane rental, concrete pumping and heavy haul / lowboy transport across the US Midwest and Northeast.",
    "address": {"@type": "PostalAddress", "addressLocality": "Chicago", "addressRegion": "IL", "addressCountry": "US"},
    "areaServed": [{"@type": "State", "name": s} for s in ["Illinois","Indiana","Michigan","Wisconsin","Ohio","Pennsylvania"]],
    "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}}
                   for n in ["Crane Rental","Concrete Pumping","Heavy Haul Transport","Knuckle Boom Crane Sales"]],
}
HOME_SCHEMA = '<script type="application/ld+json">%s</script>' % json.dumps(HOME_LD, ensure_ascii=False)

NEW_HEAD = '''<meta property="og:title" content="Atlas Boom — Knuckle Boom Crane Distributor & Regional Services" />
<meta property="og:description" content="Crane distributor plus crane rental, concrete pumping & heavy haul across IL, IN, MI, WI, OH & PA." />
<meta property="og:site_name" content="Atlas Boom" />
<meta property="og:url" content="%(o)s/" />
<meta property="og:image" content="%(o)s/assets/images/hero-industrial.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Atlas Boom — Knuckle Boom Crane Distributor & Regional Services" />
<meta name="twitter:description" content="Crane sales, rental, concrete pumping & heavy haul across the Midwest & Northeast." />
<meta name="twitter:image" content="%(o)s/assets/images/hero-industrial.jpg" />
<link rel="canonical" href="%(o)s/" />
<meta name="robots" content="index, follow" />
%(schema)s''' % {"o": ORIGIN, "schema": HOME_SCHEMA}

def sub1(s, old, new, tag):
    n = s.count(old)
    assert n == 1, "ANCHOR '%s' found %d times (need 1)" % (tag, n)
    return s.replace(old, new)

idx_path = os.path.join(HERE, "index.html")
h = open(idx_path, encoding="utf-8").read()

# 1) nav: add Services link after Models (6-space indent block)
h = sub1(h,
    '      <a href="#models">Models</a>\n      <a href="#industries">Industries</a>',
    '      <a href="#models">Models</a>\n      <a href="#services">Services</a>\n      <a href="#industries">Industries</a>',
    "nav-links")

# 2) mobile menu: add Services (2-space indent block)
h = sub1(h,
    '<div class="mobile-menu" id="mobileMenu">\n  <a href="#models">Models</a>\n  <a href="#industries">Industries</a>',
    '<div class="mobile-menu" id="mobileMenu">\n  <a href="#models">Models</a>\n  <a href="#services">Services</a>\n  <a href="#industries">Industries</a>',
    "mobile-menu")

# 3) hero eyebrow company name
h = sub1(h, '<span class="eyebrow" data-anim>Atlas Trade Solutions LLC</span>',
            '<span class="eyebrow" data-anim>Atlas Chicago LLC</span>', "hero-eyebrow")

# 4) stat 50+ Models -> 13 Models (factual consistency)
h = sub1(h,
    '<div class="stat"><div class="num"><span data-count="50">50</span><span>+</span></div><div class="lbl">Models</div></div>',
    '<div class="stat"><div class="num"><span data-count="13">13</span></div><div class="lbl">Crane Models</div></div>',
    "stat-models")

# 5) insert SERVICES section before INDUSTRIES comment
h = sub1(h, '<!-- ============================ INDUSTRIES ============================ -->',
            SERVICES_SECTION.strip() + '\n\n<!-- ============================ INDUSTRIES ============================ -->',
            "industries-anchor")

# 6) footer: remove fake phone (email-only)
h = sub1(h,
    '<a href="#quote">Chicago, IL</a><a href="mailto:info@atlasboom.com">info@atlasboom.com</a><a href="tel:+13120000000">+1 (312) 000-0000</a>',
    '<a href="#quote">Chicago, IL</a><a href="mailto:info@atlasboom.com">info@atlasboom.com</a>',
    "footer-phone")

# 7) footer bottom company name
h = sub1(h, '© 2026 Atlas Boom · Atlas Trade Solutions LLC. All rights reserved.',
            '© 2026 Atlas Boom · Atlas Chicago LLC. All rights reserved.', "footer-company")

# 8) head: replace OG block tail with expanded SEO + schema
h = sub1(h,
    '<meta property="og:title" content="Atlas Boom — Hydraulic Knuckle Boom Crane Distributor" />\n<meta property="og:description" content="Engineered in Turkey. Delivered across the USA. 50+ crane models, full warranty, certified technicians." />\n<meta property="og:site_name" content="Atlas Boom" />',
    NEW_HEAD, "og-block")

open(idx_path, "w", encoding="utf-8").write(h)
print("index.html updated OK")

# ---------- sitemap.xml ----------
urls = [(ORIGIN + "/", "1.0")]
for m in sorted(glob.glob(os.path.join(HERE, "models", "*.html"))):
    urls.append((ORIGIN + "/models/" + os.path.basename(m), "0.8"))
for _, slug in CRANE + PUMP + HAUL:
    urls.append((ORIGIN + "/" + slug + "/", "0.7"))
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u, pr in urls:
    sm.append("  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>%s</priority></url>" % (u, TODAY, pr))
sm.append("</urlset>")
open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm))
print("sitemap.xml written:", len(urls), "urls")

# ---------- robots.txt ----------
robots = "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % ORIGIN
open(os.path.join(HERE, "robots.txt"), "w", encoding="utf-8").write(robots)
print("robots.txt written")
print("DONE")
