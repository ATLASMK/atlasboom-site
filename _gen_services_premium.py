# -*- coding: utf-8 -*-
"""
Migrate the 18 existing service-area landings to the premium theme.

Strategy: parse each landing's existing HTML (title / meta description / h1 /
main body / JSON-LD), then re-render with the premium shell (Saira+Geist,
shared.css, new Cranes/Parts/Specs/Contact nav, premium footer).

Special handling: Chicago crane rental gets SEO-optimized title + meta +
keyword-tight intro for "crane rental Chicago" intent.
"""
import os, re, html, json

HERE = os.path.dirname(os.path.abspath(__file__))
ORIGIN = "https://atlasboom.com"
EMAIL = "info@atlasboom.com"

# slug -> (service label, service schema type, region label, state, primary keyword for SEO)
SLUGS = {
 "crane-rental-chicago-il":               ("Crane Rental","Crane Rental","Chicago, IL","Illinois","crane rental Chicago"),
 "concrete-pumping-chicago-illinois":     ("Concrete Pumping","Concrete Pumping","Chicago, IL","Illinois","concrete pumping Chicago"),
 "heavy-haul-lowboy-transport-illinois":  ("Heavy Haul & Lowboy","Heavy Haul Transport","Illinois","Illinois","heavy haul Illinois"),
 "crane-rental-indiana":                  ("Crane Rental","Crane Rental","Indiana","Indiana","crane rental Indiana"),
 "concrete-pumping-indiana":              ("Concrete Pumping","Concrete Pumping","Indiana","Indiana","concrete pumping Indiana"),
 "heavy-haul-lowboy-transport-indiana":   ("Heavy Haul & Lowboy","Heavy Haul Transport","Indiana","Indiana","heavy haul Indiana"),
 "crane-rental-michigan":                 ("Crane Rental","Crane Rental","Michigan","Michigan","crane rental Michigan"),
 "concrete-pumping-michigan":             ("Concrete Pumping","Concrete Pumping","Michigan","Michigan","concrete pumping Michigan"),
 "heavy-haul-lowboy-transport-michigan":  ("Heavy Haul & Lowboy","Heavy Haul Transport","Michigan","Michigan","heavy haul Michigan"),
 "crane-rental-milwaukee-wisconsin":      ("Crane Rental","Crane Rental","Milwaukee, WI","Wisconsin","crane rental Milwaukee"),
 "concrete-pumping-milwaukee-wisconsin":  ("Concrete Pumping","Concrete Pumping","Milwaukee, WI","Wisconsin","concrete pumping Milwaukee"),
 "heavy-haul-lowboy-transport-wisconsin": ("Heavy Haul & Lowboy","Heavy Haul Transport","Wisconsin","Wisconsin","heavy haul Wisconsin"),
 "crane-rental-ohio":                     ("Crane Rental","Crane Rental","Ohio","Ohio","crane rental Ohio"),
 "concrete-pumping-ohio":                 ("Concrete Pumping","Concrete Pumping","Ohio","Ohio","concrete pumping Ohio"),
 "heavy-haul-lowboy-transport-ohio":      ("Heavy Haul & Lowboy","Heavy Haul Transport","Ohio","Ohio","heavy haul Ohio"),
 "crane-rental-pennsylvania":             ("Crane Rental","Crane Rental","Pennsylvania","Pennsylvania","crane rental Pennsylvania"),
 "concrete-pumping-pennsylvania":         ("Concrete Pumping","Concrete Pumping","Pennsylvania","Pennsylvania","concrete pumping Pennsylvania"),
 "heavy-haul-lowboy-transport-pennsylvania":("Heavy Haul & Lowboy","Heavy Haul Transport","Pennsylvania","Pennsylvania","heavy haul Pennsylvania"),
}

# SEO overrides — Chicago is the primary commercial target; others use a
# tight "{Service} {Region} | Atlas Boom" format that stays under 60 chars.
SEO_OVERRIDES = {
 "crane-rental-chicago-il": {
   "title": "Crane Rental Chicago, IL | Atlas Boom Knuckle Boom",
   "desc":  "Crane rental in Chicago, IL. Atlas Boom delivers operated knuckle boom cranes downtown and across Cook County within 24-48 hours. Email for fast quotes.",
   "intro": "Crane rental in Chicago, IL from Atlas Boom. Operated hydraulic knuckle boom cranes for downtown skyline lifts, suburban industrial sites and emergency work across Cook County, on site within 24 to 48 hours. Email <a href=\"mailto:info@atlasboom.com\">info@atlasboom.com</a> for same-day quotes.",
   "extra_h2": "Chicago neighborhoods served",
   "extra_para": "Atlas Boom dispatches crews to the Loop, River North, West Loop, Fulton Market, Lincoln Park, North Side, Pilsen, South Side and the suburban Cook County corridor. Lift plans for tight downtown streets, alley access and permitted lane closures are handled in-house.",
 },
 "concrete-pumping-chicago-illinois": {
   "title": "Concrete Pumping Chicago, IL | Atlas Boom",
   "desc":  "Concrete pumping in Chicago, IL. Boom pump and line pump service for slabs, foundations and high-rise pours across Cook County. Fast 24-hour quotes by email.",
 },
 # Crane rental — short titles
 "crane-rental-indiana":             {"title":"Crane Rental Indiana | Atlas Boom"},
 "crane-rental-michigan":            {"title":"Crane Rental Michigan | Atlas Boom"},
 "crane-rental-milwaukee-wisconsin": {"title":"Crane Rental Milwaukee, WI | Atlas Boom"},
 "crane-rental-ohio":                {"title":"Crane Rental Ohio | Atlas Boom"},
 "crane-rental-pennsylvania":        {"title":"Crane Rental Pennsylvania | Atlas Boom"},
 # Concrete pumping — short titles
 "concrete-pumping-indiana":             {"title":"Concrete Pumping Indiana | Atlas Boom"},
 "concrete-pumping-michigan":            {"title":"Concrete Pumping Michigan | Atlas Boom"},
 "concrete-pumping-milwaukee-wisconsin": {"title":"Concrete Pumping Milwaukee, WI | Atlas Boom"},
 "concrete-pumping-ohio":                {"title":"Concrete Pumping Ohio | Atlas Boom"},
 "concrete-pumping-pennsylvania":        {"title":"Concrete Pumping Pennsylvania | Atlas Boom"},
 # Heavy haul — short titles
 "heavy-haul-lowboy-transport-illinois":     {"title":"Heavy Haul & Lowboy Illinois | Atlas Boom"},
 "heavy-haul-lowboy-transport-indiana":      {"title":"Heavy Haul & Lowboy Indiana | Atlas Boom"},
 "heavy-haul-lowboy-transport-michigan":     {"title":"Heavy Haul & Lowboy Michigan | Atlas Boom"},
 "heavy-haul-lowboy-transport-ohio":         {"title":"Heavy Haul & Lowboy Ohio | Atlas Boom"},
 "heavy-haul-lowboy-transport-pennsylvania": {"title":"Heavy Haul & Lowboy Pennsylvania | Atlas Boom"},
 "heavy-haul-lowboy-transport-wisconsin":    {"title":"Heavy Haul & Lowboy Wisconsin | Atlas Boom"},
}

def esc(s): return html.escape(s, quote=True)

def extract(text, start, end):
    """Slice between two regex patterns (inclusive of start match span end)."""
    m = re.search(start, text, re.S)
    if not m: return ""
    rest = text[m.end():]
    m2 = re.search(end, rest, re.S)
    return rest[:m2.start()] if m2 else rest

def parse_page(html_text):
    title = ""
    m = re.search(r"<title>(.*?)</title>", html_text, re.S)
    if m: title = m.group(1).strip()
    desc = ""
    m = re.search(r'<meta name="description" content="(.*?)"', html_text, re.S)
    if m: desc = m.group(1).strip()
    h1 = ""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html_text, re.S)
    if m: h1 = re.sub(r"\s+"," ", m.group(1).strip())
    body = extract(html_text, r'<main class="svc-body">', r'</main>').strip()
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html_text, re.S)
    return dict(title=title, desc=desc, h1=h1, body=body, schemas=schemas)

PAGE_TPL = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{TITLE}</title>
<meta name="description" content="{DESC}" />
<meta name="theme-color" content="#0A0B0D" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="{URL}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{TITLE}" />
<meta property="og:description" content="{DESC}" />
<meta property="og:url" content="{URL}" />
<meta property="og:site_name" content="Atlas Boom" />
<meta property="og:image" content="{ORIGIN}/assets/images/hero-industrial.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{TITLE}" />
<meta name="twitter:description" content="{DESC}" />
<meta name="twitter:image" content="{ORIGIN}/assets/images/hero-industrial.jpg" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%230A0B0D'/%3E%3Cpath d='M9 24 V10 L23 16.5 M9 24 H22 M23 16.5 V20' stroke='%23F5A623' stroke-width='2.6' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@500;600;700;800;900&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/css/shared.css" />
{LD}
<style>
.svc-article{{max-width:780px;margin:0 auto;padding:0 28px}}
.svc-article h2{{font-size:clamp(26px,3.6vw,38px);margin:48px 0 14px;letter-spacing:.4px}}
.svc-article h2:first-child{{margin-top:0}}
.svc-article h3{{font-size:20px;letter-spacing:.3px;margin:30px 0 6px;color:var(--amber-2)}}
.svc-article h3.faq-q{{color:var(--amber-2)}}
.svc-article p{{color:#d4d9e1;font-size:17px;line-height:1.7;margin:0 0 18px}}
.svc-article p:first-of-type{{font-size:19px;color:#eaecf1}}
.svc-article strong{{color:#fff;font-weight:600}}
.svc-article a{{color:var(--amber);border-bottom:1px solid rgba(245,166,35,.34);transition:.2s}}
.svc-article a:hover{{border-bottom-color:var(--amber)}}
.svc-article ul{{list-style:none;margin:0 0 24px;padding:0}}
.svc-article li{{position:relative;padding:10px 0 10px 28px;color:#d4d9e1;font-size:16.5px;border-bottom:1px solid var(--line)}}
.svc-article li::before{{content:"";position:absolute;left:2px;top:18px;width:8px;height:8px;border-radius:2px;background:var(--amber)}}
.svc-article .svc-note{{color:var(--muted)!important;font-size:14px!important;font-style:italic;margin-top:32px;border-top:1px solid var(--line);padding-top:18px}}
.svc-related{{margin:64px 0 0;padding:30px 32px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-card)}}
.svc-related h4{{font-size:15px;letter-spacing:1.4px;color:var(--amber);margin-bottom:14px;font-family:var(--mono);text-transform:uppercase;font-weight:500}}
.svc-related-list{{display:flex;gap:10px;flex-wrap:wrap}}
.svc-related-list a{{font-family:var(--display);font-weight:600;font-size:13.5px;text-transform:uppercase;letter-spacing:.6px;padding:8px 14px;border-radius:var(--r-chip);background:var(--bg-1);border:1px solid var(--line);color:var(--steel);transition:.2s}}
.svc-related-list a:hover{{border-color:var(--amber);color:#fff;background:var(--surface-2)}}
@media(max-width:600px){{.svc-related{{padding:22px 20px}}}}
</style>
</head>
<body>
<div class="wrap">

<nav class="nav" id="nav"><div class="container nav-inner">
  <a href="/" class="logo">
    <svg class="mark" viewBox="0 0 40 40" aria-label="Atlas Boom"><rect x=".75" y=".75" width="38.5" height="38.5" rx="10" fill="#14181f" stroke="rgba(245,166,35,.28)" stroke-width="1.5"/><path d="M11 29.5 V13 L30 20.5" fill="none" stroke="#F5A623" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M10.5 29.5 H28.5" stroke="#F5A623" stroke-width="3.4" stroke-linecap="round"/><path d="M30 20.5 V25.5" stroke="#F5A623" stroke-width="2.6" stroke-linecap="round"/></svg>
    <span class="wm"><span>ATLAS<b>BOOM</b></span><small>Knuckle Boom Cranes</small></span>
  </a>
  <div class="nav-links">
    <a href="/cranes/">Cranes</a>
    <a href="/parts/">Parts</a>
    <a href="/specs/">Specs</a>
    <a href="/contact/" class="active">Contact</a>
  </div>
  <div class="nav-cta">
    <a href="mailto:{EMAIL}" class="btn btn-amber btn-sm">Email us</a>
    <button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</div></nav>

<div class="mobile-menu" id="mobileMenu">
  <a href="/cranes/">Cranes</a>
  <a href="/parts/">Parts</a>
  <a href="/specs/">Specs</a>
  <a href="/contact/">Contact</a>
  <a href="mailto:{EMAIL}" class="btn btn-amber">Email us</a>
</div>

<section class="page-hero">
  <div class="container">
    <div class="page-hero-inner">
      <div>
        <div class="breadcrumb"><a href="/">Atlas Boom</a><span><a href="/contact/service-areas/">Service Areas</a></span><span>{REGION}</span></div>
        <span class="eyebrow">{SERVICE} &middot; {REGION}</span>
        <h1>{H1}</h1>
      </div>
      <p class="lede">{LEDE}</p>
    </div>
  </div>
</section>

<section class="section">
  <article class="svc-article">
{BODY}
    <div class="svc-related">
      <h4>Explore Atlas Boom</h4>
      <div class="svc-related-list">
        <a href="/cranes/">All cranes</a>
        <a href="/specs/">Compare specs</a>
        <a href="/parts/">Replacement parts</a>
        <a href="/contact/service-areas/">All service areas</a>
        <a href="/contact/">Request a quote</a>
      </div>
    </div>
  </article>
</section>

<section class="cta-strip">
  <div class="container cta-strip-inner">
    <div>
      <h2>Get a {SERVICE} quote.</h2>
      <p>Tell us the job site, the lift and the date. We respond by email within one business day.</p>
    </div>
    <a href="mailto:{EMAIL}" class="btn btn-amber">Email {EMAIL}</a>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="/" class="logo">
          <svg class="mark" viewBox="0 0 40 40"><rect x=".75" y=".75" width="38.5" height="38.5" rx="10" fill="#14181f" stroke="rgba(245,166,35,.28)" stroke-width="1.5"/><path d="M11 29.5 V13 L30 20.5" fill="none" stroke="#F5A623" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M10.5 29.5 H28.5" stroke="#F5A623" stroke-width="3.4" stroke-linecap="round"/><path d="M30 20.5 V25.5" stroke="#F5A623" stroke-width="2.6" stroke-linecap="round"/></svg>
          <span class="wm"><span>ATLAS<b>BOOM</b></span><small>Knuckle Boom Cranes</small></span>
        </a>
        <p>Hydraulic knuckle boom cranes built to American load standards. A brand of Atlas Chicago LLC.</p>
      </div>
      <div class="footer-col"><h4>Cranes</h4><a href="/cranes/">All models</a><a href="/specs/">Compare specs</a><a href="/parts/">Parts</a></div>
      <div class="footer-col"><h4>Company</h4><a href="/contact/">Contact</a><a href="/contact/service-areas/">Service areas</a><a href="/contact/">Request a quote</a></div>
      <div class="footer-col"><h4>Reach us</h4><a href="mailto:{EMAIL}">{EMAIL}</a><a href="/contact/">Chicago, IL</a></div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Atlas Chicago LLC. All rights reserved.</span>
      <span>Atlas Boom &middot; Hydraulic knuckle boom cranes</span>
    </div>
  </div>
</footer>

</div>
<script src="/assets/js/shared.js"></script>
</body>
</html>
"""

def lede_for(parsed, service, region):
    body = parsed["body"]
    first_p = re.search(r"<p[^>]*>(.*?)</p>", body, re.S)
    if first_p:
        text = re.sub(r"<[^>]+>", "", first_p.group(1)).strip()
        text = re.sub(r"\s+", " ", text)
        if len(text) > 220: text = text[:217].rsplit(" ", 1)[0] + "..."
        return text
    return "%s by Atlas Boom. Email %s for a same-day quote." % (service, EMAIL)

def build_one(slug):
    fp = os.path.join(HERE, slug, "index.html")
    if not os.path.exists(fp):
        return None
    raw = open(fp, encoding="utf-8").read()
    parsed = parse_page(raw)
    service, stype, region, state, _kw = SLUGS[slug]
    url = "%s/%s/" % (ORIGIN, slug)

    title = parsed["title"]
    desc = parsed["desc"]
    h1 = parsed["h1"]
    body = parsed["body"]
    intro_override = None
    extra_h2 = None
    extra_para = None
    if slug in SEO_OVERRIDES:
        o = SEO_OVERRIDES[slug]
        if o.get("title"): title = o["title"]
        if o.get("desc"):  desc = o["desc"]
        intro_override = o.get("intro")
        extra_h2 = o.get("extra_h2")
        extra_para = o.get("extra_para")

    # If we have an intro override, swap the first <p>
    if intro_override:
        body = re.sub(r"<p[^>]*>.*?</p>", "<p>" + intro_override + "</p>", body, count=1, flags=re.S)
    # If extra section, insert after first <p> (after intro)
    if extra_h2 and extra_para:
        section = "\n<h2>%s</h2>\n<p>%s</p>\n" % (extra_h2, extra_para)
        body = re.sub(r"(</p>)", r"\1" + section, body, count=1, flags=re.S)

    lede = lede_for(parsed, service, region)

    # Rebuild JSON-LD with refreshed LocalBusiness + BreadcrumbList; preserve FAQPage if present
    service_schema = {
        "@context":"https://schema.org","@type":"Service",
        "name": h1, "serviceType": stype, "url": url,
        "areaServed": {"@type":"State","name":state},
        "provider": {
            "@type":"LocalBusiness","name":"Atlas Chicago LLC","alternateName":"Atlas Boom",
            "email":EMAIL,"url":ORIGIN+"/",
            "image": ORIGIN+"/assets/images/hero-industrial.jpg",
            "address":{"@type":"PostalAddress","addressLocality":"Chicago","addressRegion":"IL","addressCountry":"US"},
            "areaServed": state,
        }
    }
    crumb_schema = {
        "@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Atlas Boom","item":ORIGIN+"/"},
            {"@type":"ListItem","position":2,"name":"Service Areas","item":ORIGIN+"/contact/service-areas/"},
            {"@type":"ListItem","position":3,"name":h1,"item":url}]
    }
    schemas_json = [json.dumps(service_schema, ensure_ascii=False),
                    json.dumps(crumb_schema, ensure_ascii=False)]
    for s in parsed["schemas"]:
        if '"FAQPage"' in s:
            schemas_json.append(s.strip())
            break
    ld = "\n".join('<script type="application/ld+json">%s</script>' % s for s in schemas_json)

    page = PAGE_TPL.format(
        TITLE=esc(title), DESC=esc(desc), URL=url, ORIGIN=ORIGIN, EMAIL=EMAIL,
        REGION=esc(region), SERVICE=esc(service), H1=esc(h1), LEDE=esc(lede),
        BODY=body, LD=ld,
    )

    with open(fp, "w", encoding="utf-8") as f:
        f.write(page)
    return (slug, len(title), len(desc), title)

if __name__ == "__main__":
    print("%-44s %-4s %-4s" % ("SLUG","T","M"))
    for slug in sorted(SLUGS):
        r = build_one(slug)
        if r is None:
            print("%-44s MISSING" % slug); continue
        s, tl, ml, t = r
        warn = "  <-- TITLE>60" if tl > 60 else ""
        warn += "  <-- META>160" if ml > 160 else ""
        print("%-44s %-4d %-4d %s%s" % (s, tl, ml, t, warn))
    print("DONE")
