# -*- coding: utf-8 -*-
"""Generate 18 styled local-SEO service pages from Cowork markdown articles.
Source: C:\\Users\\PC\\CLAUDE\\cowork iletisim\\atlasboom-seo\\articles\\NN-*.md
Output: atlasboom/<slug>/index.html  (clean folder URLs)
Theme: dark + amber, matches index.html / model pages.
Contact: email-only (info@atlasboom.com), company = Atlas Chicago LLC.
"""
import os, re, html, json

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\Users\PC\CLAUDE\cowork iletisim\atlasboom-seo\articles"
EMAIL = "info@atlasboom.com"
COMPANY = "Atlas Chicago LLC"
ORIGIN = "https://atlasboom.com"

# file -> (service label, service schema type, region label, state)
META = {
 "01-chicago-il-crane-rental.md":      ("Crane Rental","Crane Rental","Chicago & Illinois","Illinois"),
 "02-chicago-il-concrete-pumping.md":  ("Concrete Pumping","Concrete Pumping","Chicago & Illinois","Illinois"),
 "03-illinois-heavy-haul-lowboy.md":   ("Heavy Haul & Lowboy","Heavy Haul Transport","Illinois","Illinois"),
 "04-indiana-crane-rental.md":         ("Crane Rental","Crane Rental","Indiana","Indiana"),
 "05-indiana-concrete-pumping.md":     ("Concrete Pumping","Concrete Pumping","Indiana","Indiana"),
 "06-indiana-heavy-haul-lowboy.md":    ("Heavy Haul & Lowboy","Heavy Haul Transport","Indiana","Indiana"),
 "07-michigan-crane-rental.md":        ("Crane Rental","Crane Rental","Michigan","Michigan"),
 "08-michigan-concrete-pumping.md":    ("Concrete Pumping","Concrete Pumping","Michigan","Michigan"),
 "09-michigan-heavy-haul-lowboy.md":   ("Heavy Haul & Lowboy","Heavy Haul Transport","Michigan","Michigan"),
 "10-milwaukee-wi-crane-rental.md":    ("Crane Rental","Crane Rental","Milwaukee & Wisconsin","Wisconsin"),
 "11-milwaukee-wi-concrete-pumping.md":("Concrete Pumping","Concrete Pumping","Milwaukee & Wisconsin","Wisconsin"),
 "12-wisconsin-heavy-haul-lowboy.md":  ("Heavy Haul & Lowboy","Heavy Haul Transport","Wisconsin","Wisconsin"),
 "13-ohio-crane-rental.md":            ("Crane Rental","Crane Rental","Ohio","Ohio"),
 "14-ohio-concrete-pumping.md":        ("Concrete Pumping","Concrete Pumping","Ohio","Ohio"),
 "15-ohio-heavy-haul-lowboy.md":       ("Heavy Haul & Lowboy","Heavy Haul Transport","Ohio","Ohio"),
 "16-pennsylvania-crane-rental.md":    ("Crane Rental","Crane Rental","Pennsylvania","Pennsylvania"),
 "17-pennsylvania-concrete-pumping.md":("Concrete Pumping","Concrete Pumping","Pennsylvania","Pennsylvania"),
 "18-pennsylvania-heavy-haul-lowboy.md":("Heavy Haul & Lowboy","Heavy Haul Transport","Pennsylvania","Pennsylvania"),
}

def esc(s): return html.escape(s, quote=True)

def inline(text):
    """Inline markdown -> HTML. Order: escape, links, bold."""
    text = html.escape(text, quote=False)
    def link(m):
        label, href = m.group(1), m.group(2)
        if href.startswith("/"):
            if not href.endswith("/"): href += "/"
            return '<a href="%s">%s</a>' % (href, label)
        return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (href, label)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text

def parse_meta_block(raw):
    m = re.search(r"<!--(.*?)-->", raw, re.S)
    block = m.group(1) if m else ""
    def grab(key):
        mm = re.search(r"%s:\s*(.+)" % re.escape(key), block)
        return mm.group(1).strip() if mm else ""
    return {
        "title": grab("Title Tag"),
        "desc": grab("Meta Description"),
        "slug": grab("URL Slug").strip("/"),
        "primary": grab("Primary Keyword"),
    }

def body_to_html(raw):
    """Return (h1, body_html, faqs[list of (q,a)])."""
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S).strip()
    # contact: phone hidden -> email only
    raw = raw.replace("Call **{{PHONE}}** or email **{{EMAIL}}**", "Email **%s**" % EMAIL)
    raw = raw.replace("{{EMAIL}}", EMAIL).replace("{{PHONE}}", "")
    lines = raw.split("\n")
    h1 = ""
    out, faqs = [], []
    i, n = 0, len(lines)
    ul, in_faq = [], False
    def flush_ul():
        if ul:
            out.append("<ul>" + "".join("<li>%s</li>" % inline(x) for x in ul) + "</ul>")
            ul.clear()
    while i < n:
        ln = lines[i].rstrip()
        s = ln.strip()
        if not s:
            flush_ul(); i += 1; continue
        if s.startswith("# "):
            h1 = s[2:].strip(); i += 1; continue
        if s.startswith("## "):
            flush_ul()
            title = s[3:].strip()
            in_faq = title.lower().startswith("frequently asked")
            out.append('<h2>%s</h2>' % esc(title)); i += 1; continue
        if s.startswith("- "):
            ul.append(s[2:].strip()); i += 1; continue
        # FAQ question: a line that is wholly **...**
        mq = re.match(r"^\*\*(.+?)\*\*$", s)
        if in_faq and mq:
            flush_ul()
            q = mq.group(1).strip()
            ans = ""
            if i + 1 < n and lines[i+1].strip():
                ans = lines[i+1].strip(); i += 1
            faqs.append((q, ans))
            out.append('<h3 class="faq-q">%s</h3>' % esc(q))
            out.append('<p>%s</p>' % inline(ans))
            i += 1; continue
        # italic-only note line  *...*
        if s.startswith("*") and s.endswith("*") and not s.startswith("**"):
            flush_ul()
            out.append('<p class="svc-note">%s</p>' % inline(s.strip("*").strip()))
            i += 1; continue
        flush_ul()
        out.append("<p>%s</p>" % inline(s))
        i += 1
    flush_ul()
    return h1, "\n".join(out), faqs

NAV = '''<nav class="nav" id="nav">
  <div class="container nav-inner">
    <a href="/" class="logo"><svg viewBox="0 0 34 34" fill="none"><rect width="34" height="34" rx="8" fill="#141820" stroke="#F5A623" stroke-opacity=".4"/><path d="M7 24h20M10 24V10l14 4M10 14l5-4" stroke="#F5A623" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg> ATLAS <b>BOOM</b></a>
    <a href="/#services" class="nav-back"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M19 12H5M11 18l-6-6 6-6" stroke-linecap="round" stroke-linejoin="round"/></svg> <span>Service Areas</span></a>
    <a href="/#quote" class="btn btn-amber">Request a Quote</a>
  </div>
</nav>'''

FOOTER = '''<footer class="svc-footer">
  <div class="container">
    <div class="svc-footer-grid">
      <div>
        <a href="/" class="logo" style="margin-bottom:14px"><svg viewBox="0 0 34 34" fill="none"><rect width="34" height="34" rx="8" fill="#141820" stroke="#F5A623" stroke-opacity=".4"/><path d="M7 24h20M10 24V10l14 4M10 14l5-4" stroke="#F5A623" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg> ATLAS <b>BOOM</b></a>
        <p>Crane rental, concrete pumping and heavy haul transport across the Midwest &amp; Northeast. Hydraulic knuckle boom crane distribution nationwide.</p>
      </div>
      <div class="svc-footer-col">
        <h4>Services</h4>
        <a href="/crane-rental-chicago-il/">Crane Rental</a>
        <a href="/concrete-pumping-chicago-illinois/">Concrete Pumping</a>
        <a href="/heavy-haul-lowboy-transport-illinois/">Heavy Haul &amp; Lowboy</a>
        <a href="/#models">Cranes for Sale</a>
      </div>
      <div class="svc-footer-col">
        <h4>Contact</h4>
        <a href="mailto:%(email)s">%(email)s</a>
        <a href="/#quote">Request a Quote</a>
        <span>Chicago, IL &middot; USA</span>
      </div>
    </div>
    <div class="svc-footer-bottom">&copy; 2026 %(company)s &middot; All rights reserved.</div>
  </div>
</footer>''' % {"email": EMAIL, "company": COMPANY}

STYLE = '''<style>
:root{--bg:#0A0B0D;--panel:#111318;--card:#141820;--amber:#F5A623;--amber-bright:#ffba48;--steel:#C0C8D4;--text:#fff;--muted:#8b93a1;--line:rgba(255,255,255,.08);--line-strong:rgba(255,255,255,.14);--ease:cubic-bezier(.16,1,.3,1);--maxw:1180px}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Inter',system-ui,sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
h1,h2,h3,h4{font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:.5px;line-height:1.04}
.container{width:100%;max-width:var(--maxw);margin:0 auto;padding:0 24px}
.btn{display:inline-flex;align-items:center;gap:9px;font-family:'Barlow Condensed',sans-serif;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;font-size:16px;padding:14px 28px;border-radius:10px;transition:.35s var(--ease);cursor:pointer}
.btn-amber{background:var(--amber);color:#0A0B0D;box-shadow:0 10px 30px -10px rgba(245,166,35,.35)}
.btn-amber:hover{background:var(--amber-bright);transform:translateY(-2px)}
.btn-ghost{border:1.5px solid var(--line-strong);color:#fff}
.btn-ghost:hover{border-color:var(--amber);color:var(--amber)}
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
.svc-hero{position:relative;padding:150px 0 60px;background:radial-gradient(120% 90% at 50% 0%,#161b26 0%,#0c0f16 70%);border-bottom:1px solid var(--line)}
.crumb{font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:1.5px;font-size:13px;color:var(--muted);margin-bottom:18px}
.crumb a{color:var(--steel)}.crumb a:hover{color:var(--amber)}
.svc-eyebrow{font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:3px;font-weight:600;color:var(--amber);font-size:14px;display:inline-flex;align-items:center;gap:10px;margin-bottom:14px}
.svc-eyebrow::before{content:"";width:28px;height:2px;background:var(--amber)}
.svc-hero h1{font-size:clamp(34px,6vw,64px);max-width:16ch}
.svc-body{max-width:780px;margin:0 auto;padding:56px 24px 20px}
.svc-body h2{font-size:clamp(24px,3.6vw,34px);color:#fff;margin:42px 0 14px;padding-top:6px}
.svc-body h2:first-child{margin-top:0}
.svc-body h3.faq-q{font-size:21px;color:var(--amber-bright);margin:26px 0 4px;letter-spacing:.4px}
.svc-body p{color:#cfd4dd;font-size:17px;margin:0 0 18px}
.svc-body p:first-of-type{font-size:19px;color:#e7eaef}
.svc-body strong{color:#fff;font-weight:600}
.svc-body a{color:var(--amber);border-bottom:1px solid rgba(245,166,35,.32)}
.svc-body a:hover{border-bottom-color:var(--amber)}
.svc-body ul{list-style:none;margin:0 0 22px;padding:0}
.svc-body li{position:relative;padding:7px 0 7px 26px;color:#cfd4dd;font-size:17px;border-bottom:1px solid var(--line)}
.svc-body li::before{content:"";position:absolute;left:2px;top:16px;width:8px;height:8px;border-radius:2px;background:var(--amber)}
.svc-note{color:var(--muted)!important;font-size:14px!important;font-style:italic;margin-top:26px;border-top:1px solid var(--line);padding-top:18px}
.svc-cta{margin:30px 0 0;background:linear-gradient(180deg,#12161e,#0c0f15);border-top:1px solid var(--line)}
.svc-cta .container{max-width:780px;text-align:center;padding-top:64px;padding-bottom:64px}
.svc-cta h2{font-family:'Barlow Condensed';text-transform:uppercase;font-size:clamp(28px,4vw,42px);margin-bottom:12px}
.svc-cta p{color:var(--muted);margin-bottom:26px}
.svc-cta-actions{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.svc-footer{border-top:1px solid var(--line);background:#0c0e12;padding:54px 0 30px;margin-top:0}
.svc-footer-grid{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:30px}
.svc-footer p{color:var(--muted);font-size:14px;margin-top:6px;max-width:36ch}
.svc-footer-col h4{font-family:'Barlow Condensed';text-transform:uppercase;letter-spacing:1px;color:#fff;font-size:16px;margin-bottom:12px}
.svc-footer-col a,.svc-footer-col span{display:block;color:var(--muted);font-size:14px;padding:4px 0}
.svc-footer-col a:hover{color:var(--amber)}
.svc-footer-bottom{border-top:1px solid var(--line);margin-top:30px;padding-top:22px;color:var(--muted);font-size:13px;text-align:center}
@media(max-width:760px){.svc-footer-grid{grid-template-columns:1fr 1fr}.svc-footer-grid>div:first-child{grid-column:1/-1}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;scroll-behavior:auto!important}}
</style>'''

FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%230A0B0D'/%3E%3Cpath d='M6 22h20M9 22V9l14 4' stroke='%23F5A623' stroke-width='2.4' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E"

def build(fname):
    raw = open(os.path.join(SRC, fname), encoding="utf-8").read()
    meta = parse_meta_block(raw)
    service, stype, region, state = META[fname]
    h1, body, faqs = body_to_html(raw)
    slug = meta["slug"]
    url = "%s/%s/" % (ORIGIN, slug)

    service_schema = {
        "@context":"https://schema.org","@type":"Service",
        "name": h1, "serviceType": stype, "url": url,
        "areaServed": {"@type":"State","name":state},
        "provider": {"@type":"LocalBusiness","name":COMPANY,"email":EMAIL,"url":ORIGIN+"/",
                     "address":{"@type":"PostalAddress","addressLocality":"Chicago","addressRegion":"IL","addressCountry":"US"}}
    }
    crumb_schema = {
        "@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Home","item":ORIGIN+"/"},
            {"@type":"ListItem","position":2,"name":"Service Areas","item":ORIGIN+"/#services"},
            {"@type":"ListItem","position":3,"name":h1,"item":url}]
    }
    schemas = [service_schema, crumb_schema]
    if faqs:
        schemas.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]})
    ld = "\n".join('<script type="application/ld+json">%s</script>' %
                   json.dumps(s, ensure_ascii=False) for s in schemas)

    page = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>%(title)s</title>
<meta name="description" content="%(desc)s" />
<link rel="canonical" href="%(url)s" />
<meta name="theme-color" content="#0A0B0D" />
<meta name="robots" content="index, follow" />
<meta property="og:type" content="website" />
<meta property="og:title" content="%(title)s" />
<meta property="og:description" content="%(desc)s" />
<meta property="og:url" content="%(url)s" />
<meta property="og:site_name" content="Atlas Boom" />
<meta property="og:image" content="%(origin)s/assets/images/hero-industrial.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="%(title)s" />
<meta name="twitter:description" content="%(desc)s" />
<meta name="twitter:image" content="%(origin)s/assets/images/hero-industrial.jpg" />
<link rel="icon" href="%(favicon)s" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
%(ld)s
%(style)s
</head>
<body>
%(nav)s
<header class="svc-hero">
  <div class="container">
    <div class="crumb"><a href="/">Home</a> &rsaquo; <a href="/#services">Service Areas</a> &rsaquo; %(region)s</div>
    <span class="svc-eyebrow">%(service)s &middot; %(region)s</span>
    <h1>%(h1)s</h1>
  </div>
</header>
<main class="svc-body">
%(body)s
</main>
<section class="svc-cta">
  <div class="container">
    <h2>Get a %(service)s Quote</h2>
    <p>Tell us about your job &mdash; we&rsquo;ll send a fast, no-obligation quote.</p>
    <div class="svc-cta-actions">
      <a href="mailto:%(email)s" class="btn btn-amber">Email %(email)s</a>
      <a href="/#quote" class="btn btn-ghost">Request a Quote</a>
    </div>
  </div>
</section>
%(footer)s
<script>
(function(){var nav=document.getElementById('nav');function s(){nav.classList.toggle('scrolled',window.scrollY>20);}s();window.addEventListener('scroll',s,{passive:true});})();
</script>
</body>
</html>''' % {
        "title": esc(meta["title"]), "desc": esc(meta["desc"]), "url": url, "origin": ORIGIN,
        "favicon": FAVICON, "ld": ld, "style": STYLE, "nav": NAV, "footer": FOOTER,
        "region": esc(region), "service": esc(service), "h1": esc(h1),
        "body": body, "email": EMAIL,
    }
    outdir = os.path.join(HERE, slug)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    return slug, meta["title"], len(meta["title"]), len(meta["desc"]), len(faqs)

if __name__ == "__main__":
    print("%-44s %-3s %-4s %s" % ("SLUG","T","M","FAQ"))
    for fn in sorted(META):
        slug, title, tl, ml, nf = build(fn)
        warn = " <-- TITLE>60" if tl > 60 else ""
        warn += " <-- META>155" if ml > 155 else ""
        print("%-44s %-3d %-4d %d%s" % (slug, tl, ml, nf, warn))
    print("DONE -> 18 service pages")
