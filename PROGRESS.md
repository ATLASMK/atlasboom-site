# AtlasBoom.com — PROGRESS (resume notu)

**Proje:** `C:\Users\PC\CLAUDE\ATLASBOOM.COM and ATLASWAY.NET PREMİUM DESİGN\atlasboom\`
**Önizleme:** `.claude/launch.json` config **"atlasboom"** → http://localhost:4322 (python http.server). Atlasway ayrı (port 4323), o henüz V1.
**Tema (CURRENT):** koyu #0A0B0D + amber #F5A623, **Saira Condensed + Geist + Geist Mono** (Barlow+Inter eski).

## 🚀 2026-06-23 TURNKEY OTURUM 2 — PREMIUM YAYIN (5 sayfa + 18 SEO landing)

Kullanıcı 1 saatlik turnkey yetki verdi. Tüm site premium temaya geçirildi.

**Yapı (yeni):**
- `index.html` — Hero scroll-scrub (73 frame `frames/header/`) + Fleet (13 model grid) + Capacity slider + Service teaser + CTA. Marka sahibi tonu; "HSA" / "Engineered in Turkey" YOK.
- **Yeni nav:** Cranes / Parts / Specs / Contact (yarı saydam, scroll'da koyulaşan).
- `cranes/index.html` — 13 model showcase + boom config filtresi (5+2/6+2/7+2/heavy) + capacity matcher.
- `parts/index.html` — 8 kategori chip (boom/cylinder/slewing/valve/winch/electrical/hose/structural) + email-only istek formu.
- `specs/index.html` — 13 modelin karşılaştırma tablosu (sort: model/cap/reach).
- `contact/index.html` — email-only form (mailto: fallback) + 3 info kart.
- `contact/service-areas/index.html` — 18 SEO landing'in gruplu indeksi (3 svc block × 6 eyalet).

**Paylaşılan asset:** `assets/css/shared.css` + `assets/js/shared.js` (nav/footer/btn/page-hero tokens). Index inline tutuldu (hero scroll-scrub'a özel). Model sayfaları + 18 service sayfası shared.css link veriyor.

**13 model sayfası (yeniden üretildi):** `_gen_pages.py` premium TPL'ye çevrildi. Scroll-3D viewer + 3-açılı galeri lightbox + spec grid + load chart KORUNDU. CTA artık `../contact/`.

**18 SEO landing (yeniden üretildi):** `_gen_services_premium.py` mevcut HTML'leri parse ediyor → premium shell ile sarmalıyor. Mevcut body içerik + FAQPage schema korunur, yeni Service + BreadcrumbList JSON-LD eklenir.

**SEO optimizasyonu (SEO_OVERRIDES + skill kullanıldı):**
- Chicago crane-rental + concrete-pumping: özel title/desc/intro + "Chicago neighborhoods served" extra H2 (Loop, River North, West Loop vb).
- Kalan 16 landing: kısa title `{Service} {Region} | Atlas Boom` (hepsi <60 char).
- LocalBusiness schema her sayfada Atlas Chicago LLC ile.
- BreadcrumbList: Home → Service Areas → Page.

**sitemap.xml:** 37 URL (core + 13 model + 18 service). Chicago landings priority 0.8-0.9, diğerleri 0.7.
**robots.txt:** generator script'leri ve `.claude/` Disallow'da.

**Skill kullanıldı:** `npx claude-code-templates@latest --skill business-marketing/seo-optimizer` → `.claude/skills/seo-optimizer/SKILL.md`.

**Push:** ATLASMK/atlasboom-site main, Pages rebuild tetiklendi.

## 🚀 2026-06-23 TURNKEY OTURUM 3 — DNS rehber + Form backend + 4. açı galeri

Kullanıcı tekrar 1 saat turnkey yetki verdi (1-3-4 numaralı işler için).

**Faz 9 — CNAME + DNS_SETUP.md:** Repo köküne `CNAME` (= `atlasboom.com`) eklendi. **DNS_SETUP.md** Shopify Admin'den GitHub Pages IP'lerine (185.199.108-111.153) geçiş için step-by-step kılavuz. ⚠️ "atlasboom.com'u Shopify'da PRIMARY YAPMA — SkinAge bozulur" uyarısı korunur. MX/SPF/DKIM/DMARC dokunulmaz. Bu external Shopify hesap erişimi gerektiriyor — kullanıcı 5 dakikada bitirebilir.

**Faz 10 — Form backend (Web3Forms + mailto fallback):** Yeni `assets/js/forms.js` (config: WEB3FORMS_ACCESS_KEY constant). Form'lar `data-atlas-form data-subject` ile opt-in. Key boş → mailto: fallback (mevcut davranış). Key set edilince fetch POST Web3Forms. Parts + Contact form'ları upgrade edildi; inline JS kaldırıldı. Kullanıcı web3forms.com'a info@atlasboom.com ile kayıt → access key → forms.js'e yapıştır → 1 dakika setup.

**Faz 11 — 4. açı galeri (rear) — Higgsfield SİZ DEDİĞİNİZ MALİYET/ZAMAN İLE YAPILMADI, ZERO-COST ÇÖZÜMLE ÇÖZÜLDÜ:** Higgsfield 26 görseli (rear+lowangle) yerine, her modelin mevcut `frames/<slug>/f-0073.jpg` (Seedance orbit son frame'i) rear 3/4 açıdan iyi görüntü veriyor. 13 model × frame73 → `models/<slug>-rear.jpg` kopyalandı. `_gen_pages.py` galerisi 4-açıya genişledi (Side / 3/4 hero / Front / Rear 3/4), CSS grid 2-col mobile + 4-col desktop. **Lowangle hâlâ yapılmadı** — orbit videolar sabit elevation, frame'lerden çıkmaz; gerçek lowangle için Higgsfield Nano Banana gerekli (sonraki oturum).

## 🚀 2026-06-23 TURNKEY OTURUM 4 — 5. açı + AT-100/120 yük grafiği

**Faz 12 — Lowangle (5. açı):** Higgsfield Nano Banana Pro ile 13 model × 1 lowangle = 13 görsel üretildi (~26 kredi). Pipeline: `media_upload` batch (13 hero JPG) → `urllib` PUT 13 paralel (`_lowangle_upload.py`) → `media_confirm` batch → `generate_image` 13 paralel dramatic-low-angle prompt + reference image → `show_generations` ile job ID/URL eşleştir → `_lowangle_download.py` paralel download + ffmpeg scale=1600 q4 jpg (~100-200 KB her biri). Galeri 5-açıya genişledi (Side / 3/4 hero / Front / Rear 3/4 / Low angle), CSS 2-col mobile / 5-col desktop.

**Faz 13 — AT-100/120 yük grafiği:** Katalogtaki K8+K5 lifting capacity diagramları `_loadchart_crop.py` (PIL) ile crop edildi (sadece sağ-alt chart, sol vinç fotoğrafı + HSA logo + Türkçe başlık çubuğu kesildi) → JPG 1280px ~110 KB. `_gen_pages.py` build_chart()'a `loadchart_img` desteği eklendi: MODELS dict'inde `loadchart_img="<slug>-loadchart.jpg"` varsa diagram göster + "For US-unit printable chart email info@atlasboom.com" notu. AT-100/AT-120 sayfalarında artık katalog diagram'ı gömülü.

### ⚠️ HÂLÂ EKSİK (sadece external)
1. **Domain yayını** — CNAME eklendi, DNS değişimi external (kullanıcı Shopify Admin'de yapacak, DNS_SETUP.md var).

---

## ÖNCEKİ DURUM (resume için tutuluyor)

## DURUM: ÇOĞU BİTTİ ✅ (2026-06-22 turnkey oturum)

### Tamamlanan
- **İsimlendirme:** AT-10, AT-13, AT-16, AT-20, **AT-25-27**, AT-30, **AT-35-38**, AT-45, AT-55, AT-65, AT-75, AT-100, AT-120 (SKU = AT-(metrik ton), tireli). Dosya slug'ları da at-* (URL'de görünür).
- **ABD birimleri/jargon:** kapasite **lb** (badge US tons), uzanma **ft**, basınç **3,626 psi**. "HSA" sitede yok.
- **Fotoğraflar:** 13 model × **3 açı** (side/hero/front) → `assets/images/models/<slug>-<angle>.jpg` (ffmpeg scale=1600 q3 optimize, ~176KB).
- **Kartlar:** 13'ü de `<a class=model-card href=models/<slug>.html>` + `<img class=model-photo>`. Slider US tons.
- **13 model sayfası:** scroll-3D viewer (full-bleed) + 3-açılı galeri (lightbox **ok butonları + ←→ klavye + Esc**) + specs + CTA. AT-13'te **yük tablosu** (page-13'ten, ft/lb).
- **Scroll-3D (her model):** Seedance 2.0 orbit video (1080p) → `ffmpeg fps=12 scale=1600 q3` → `assets/images/frames/<slug>/f-%04d.jpg` (73 frame) → generator'da `frames=73` → sayfada scroll scrubber. **13/13 çalışıyor.**
- **ANA HERO (index.html):** sinematik sanayi gün batımı görseli (Higgsfield, hero-B=aa302a64) → dolly-in video → 73 frame `assets/images/frames/hero/` → `HERO_FRAMES=73` → scroll'da video ilerler + hero metni soluar. Poster: `assets/images/hero-industrial.jpg`.

### 🎨 PREMIUM TEMA REDESIGN — PİLOT BİTTİ (2026-06-23)
Kullanıcı `Leonxlnx/taste-skill` GitHub repo'sunu attı ([taste-skill](https://github.com/Leonxlnx/taste-skill) — anti-slop frontend design skill kütüphanesi: brutalist/minimalist/soft/redesign/taste vb.). Mod = **redesign-overhaul** (yeni görsel dil, içerik/IA/SEO korunur). Yön = **koyu sinematik endüstriyel premium** (kullanıcı kararı, en düşük risk, mevcut koyu görsellerle uyumlu).

**Pilot dosya:** `_preview-theme.html` (izole, izle/test et — onaylanınca index.html + iki generator'a yayılacak). Önizleme: port 4322 / `_preview-theme.html`.

**Sistem:**
- Fontlar: **Saira Condensed 500-900** (display) + **Geist 400-600** (body) + **Geist Mono 400-500** (specs, load chart, sayılar). Eski Barlow+Inter atıldı.
- Renkler: `--bg #0A0B0D` / `--surface #13161c` / **`--amber #F5A623` (TEK aksan)** / `--steel #aeb7c4`. Sinematik ambient + ince grain (SVG noise overlay).
- Radius: kart **12px** / buton **8px** / chip **6px** (tek scale).
- Em-dash=0, eyebrow seyrek, dynamic boom config notu (`build_chart` artık `extra["boom"]`'dan alıyor).

**Yeni hero (scroll-scrub video + iki bölgeli wow):**
- Kaynak: `C:\Users\PC\CLAUDE\header.mp4` (1928x1076, 6sn, 24fps) → ffmpeg `fps=12,scale=1600,q4` ile **73 jpg kare** → `assets/images/frames/header/`.
- Scroll yapısı: `.hero-scroll{height:300vh}` + sticky `.hero-sticky` + tam-ekran canvas. ⚠️ **`video.currentTime` KULLANMA** (takılır) — mevcut scroll-3D pipeline'ı ile aynı: canvas drawImage + rAF kapısı YOK (eval ortamında kilitleniyordu, direkt update fonksiyonu).
- Akış (üzerinde 4 dial ayarı yapıldı): SCRUB_END=0.72 (video burada biter) → REVEAL=0.16 (sıralı reveal) → sonra %12 sabit kalış.
- **Kompozisyon (kullanıcı çizim onaylı):** "LIFT HEAVIER." sol-üst Bölge1 (Y'den yükselir, gecikme 0), "REACH <span class=am>FARTHER.</span>" sağ-orta Bölge2 (X'den sağdan kayar, gecikme 0.22, mesafe 90px — boom yönünü pekiştirir), alt blok (lead+CTA+stats) sol-orta ok bölgesi (gecikme 0.5).
- **Alt blok saydam** (vinç son karesini kapatmasın): koyu cam panel KALDIRILDI. Açık zeminde okunması için metin **koyu** (`#14171d`) + hafif beyaz halo (`text-shadow:0 1px 18px rgba(250,250,252,.85)`); mobil (zemin koyu) beyaza döner. Ghost button rengi `.hero-foot{--gc,--gb}` CSS değişkenleriyle çözüldü (`.btn-ghost{color:#fff}` base cascade tuhaflığı yüzünden).
- Logo yeniden: 40px boom-mark SVG (mast + diagonal kol + kanca, amber, koyu tile) + 800 ağırlık ATLAS**BOOM** + altında mono `Knuckle Boom Cranes`.
- Hero h1: clamp(46,7.2vw,116) **ağırlık 900**, line-height .82, letter-spacing -1.7, gölgeli. (Önceki 700/98px güçsüzdü.)

**⚠️ ekran görüntüsü aracı bu ortamda timeout veriyor** — programatik doğrulama yaptım (canvas pixel sampling + getBoundingClientRect %'leri + opacity check). Tüm 3 reveal noktasında doğrulandı.

### 🌐 GITHUB + PAGES + CLAUDE CHAT BRIEFING (2026-06-23)
- **Repo:** https://github.com/ATLASMK/atlasboom-site (PUBLIC, hesap ATLASMK, gh CLI device-flow keyring'de).
- **Pages canlı:** https://atlasmk.github.io/atlasboom-site/ (legacy index), https://atlasmk.github.io/atlasboom-site/_preview-theme.html (yeni hero), https://atlasmk.github.io/atlasboom-site/CLAUDE_BRIEF.md (Claude chat-design-code için brief).
- **⚠️ `.nojekyll` ZORUNLU** — underscore'lu dosyalar (`_preview-theme.html`, `_gen_*.py`) yoksa 404. Eklendiğinde Pages otomatik re-deploy ETMEZ → `gh api -X POST repos/ATLASMK/atlasboom-site/pages/builds` ile manuel tetiklendi.
- **CLAUDE_BRIEF.md:** repo kökünde, Claude chat session'larının saniyelerde projeyi kavraması için yazıldı (stack, layout, current status, yeni hero, em-dash yasağı/conventions, açık kararlar).
- **/design-sync skill'i UYUMSUZ** — package.json/dist/React yok, bizim proje pure static. /design-sync component kütüphaneleri için. Bunun yerine: Claude chat'e Pages URL'i + brief verildi.
- **İş akışı kuralı:** kullanıcı Claude chat'te `_preview-theme.html`'i düzenleyince → bana yapıştırır veya pushlar → ben dokunmadan önce dosyayı yeniden okurum (üzerine yazma riski). Local'de pushlanmamış commit varsa da sor.

### ✅ YÜK TABLOLARI BİTTİ (2026-06-23)
**11/13 modelde** yük tablosu var: AT-13, AT-16 (önceki) + bu oturumda **AT-10, AT-20, AT-25-27, AT-30, AT-35-38, AT-45, AT-55, AT-65, AT-75**. Yöntem: yük tablosu sayfaları PDF'ten (`hsa baskı son (1).pdf`) **300 DPI** render (`_loadcharts_300dpi/`) → PIL ile band kırpıp oku → her sayfanın **en üst (standart) konfigi** → m×3.28084=ft, kg×2.20462=lb, lb nearest-5 → `_gen_pages.py` MODELS'e `extra=`+`chart=`. Konfigler değişken: AT-10..AT-45 çoğu **5+2**, AT-35-38=**6+2**, AT-55/65=**6+2** (HS165 ve HS195 katalogta AYNI L6+4 tabloyu paylaşıyor — gerçek üretici verisi), AT-75=**7+2**. `build_chart` notu artık `extra["boom"]`'dan dinamik. ⚠️ **AT-100 (HS300) ve AT-120 (HS360) katalogta sadece GRAFİK eğrisi** — tablo yok; uydurma rakam yazılmadı, `extra=None` (yük tablosu "request" notu kalıyor). İstenirse grafikten yaklaşık nokta okunabilir.

### ✅ ARŞİV TAŞIMA (2026-06-23)
- 13 modelin **3 studio fotosu** (proje `assets/images/models/`) → KOPYA → `Desktop\HSA CRANE\TONS\<ton>TON\STUDIO\` (orijinaller projede, site bozulmadı). hs-30 orbit mp4'leri → `10TON\STUDIO\`. (Çoğu modelin orbit videosu ayrı dosya değil, projede frame jpg.)
- Cowork SEO klasörü **taşındı** (kesme): `cowork iletisim\atlasboom-seo` → `Desktop\HSA CRANE\SEO\` (18 makale + xlsx + kılavuz). `cowork iletisim` artık boş.

### ⚠️ KALAN İŞ
1. **4. ve 5. açı (rear + lowangle)** — şu an 3 açı var, kullanıcı 5 istedi. Her model için 2 açı daha (26 görsel) + galeriyi 5'liye çıkar. (Tema değişimi netleşince yapılır.)
2. **AT-100 / AT-120 yük tablosu** — katalogda sadece GRAFİK (çok-eğrili diyagram, tablo yok). Grafik okuma denendi ama tutarsız çıktı (120t grafiği <100t okunuyor → eksen/eğri yorumu güvenilmez). **Kullanıcı kararı (2026-06-23): ŞİMDİLİK BOŞ** — `extra=None`, "detaylı yük tablosu talep üzerine" notu kalıyor. İleri seçenek: HSA'dan tablo spec sheet alıp diğerleri gibi gir, veya gerçek diyagram görselini sayfaya resim olarak göm.

## ✅ SEO — COWORK SERVİS SAYFALARI (2026-06-23 BİTTİ)
Cowork paketi: `C:\Users\PC\CLAUDE\cowork iletisim\atlasboom-seo\` (18 makale + keyword xlsx + CLAUDE.md). Şirket adı kararı = **Atlas Chicago LLC**, iletişim **email-only** (info@atlasboom.com, telefon yok).
- **Faz 1 — generator `_gen_services.py`:** 18 markdown → 18 stillenmiş HTML servis sayfası. Temiz URL `/<slug>/index.html`. 3 hizmet (crane-rental / concrete-pumping / heavy-haul-lowboy-transport) × 6 eyalet (chicago-il, indiana, michigan, milwaukee-wisconsin, ohio, pennsylvania). Her sayfa: title≤60 + desc≤155 + canonical + og + twitter; **Service + BreadcrumbList + FAQPage** JSON-LD; iç linkler (kardeş hizmetler); email CTA.
- **Faz 2 + 3 — script `_seo_finish.py`:** index.html'e `#services` bölümü (3 sütun × 6 link = 18) + nav/mobil-menü linki. sitemap.xml (32 URL: 1 ana + 13 model + 18 servis), robots.txt, anasayfa **LocalBusiness** JSON-LD. Düzeltmeler: og "50+" kaldırıldı, stat "50+ Models"→"13 Crane Models", hero eyebrow + footer + quote = "Atlas Trade Solutions LLC"→**"Atlas Chicago LLC"**, sahte telefon kaldırıldı (footer + quote li). Form'daki "Phone" alanı korundu (müşteri alanı).
- Model sayfaları (`_gen_pages.py`) da güncellendi: canonical + og + twitter + **Product** JSON-LD + footer firma adı.
- **DOĞRULANDI:** 18 servis + sitemap + robots HTTP 200, konsol temiz, JSON-LD geçerli (DOM/snapshot ile — ⚠️ screenshot aracı bu oturumda bozuktu).
- **KULLANICIYA KALAN (Cowork kılavuzundan):** domain'i siteye bağla, Google Business Profile aç + yorum topla, heavy-haul DOT izin rakamlarını eyalet DOT'undan teyit et.

## ÜRETİM PİPELINE (tekrar lazım olur)
- **Higgsfield hesabı:** user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP. ⚠️ **MAX 8 EŞZAMANLI İŞ** — batch'leri 8'erli yap.
- **CLI bozuk** → MCP kullan: `media_upload`(filename)→curl PUT bytes→`media_confirm`(type image)→`generate_image`(model **nano_banana_pro**, 3:2, 2k, medias[{value:media_id, role:image}]).
- **Orbit video:** `generate_video`(model **seedance_2_0**, 1080p, 6s, 16:9, bitrate high, audio false, medias[{value:**hero görselin job_id'si**, role:start_image}]).
- **Toplama:** `show_generations`(type image/video) → rawUrl. **ffmpeg URL'den direkt** indirip optimize/frame'le.
- **Temiz referanslar:** `C:\Users\PC\Desktop\HSA CRANE\REFERANSLAR\<slug>-ref.png` (kırpılmış). Model→media_id eşleşmesi (yeni açı üretmek için):
  at-10=c9b0f6e9 · at-13=f37e3535 · at-16=53a93b3d · at-20=0161f706 · at-25-27=b809929f · at-30=3abcaecb · at-35-38=fa0c563f · at-45=249cdb7f · at-55=2a224620 · at-65=77bf8a4e · at-75=4c8e804c · at-100=f7562891 · at-120=3ee7c61c (media_id'ler süreyle dolabilir → REFERANSLAR'dan yeniden yükle).
- **Generator:** `_gen_pages.py` (MODELS listesi: slug/sku/badge/cap/frames/extra/chart). Değiştir → çalıştır → 13 sayfa yenilenir.
- **Kaynak katalog:** `C:\Users\PC\Desktop\HSA CRANE\hsa baskı son (1).pdf` (PyMuPDF/fitz ile okunur).

## NOT
- Atlasway.net (diğer site) V1 bitti ama bu oturumda dokunulmadı. atlasway.net domaini şu an boş Horizon Shopify (SkinAge rafa kaldırıldı).
