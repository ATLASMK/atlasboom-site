# AtlasBoom.com — PROGRESS (resume notu)

**Proje:** `C:\Users\PC\CLAUDE\ATLASBOOM.COM and ATLASWAY.NET PREMİUM DESİGN\atlasboom\`
**Önizleme:** `.claude/launch.json` config **"atlasboom"** → http://localhost:4322 (python http.server). Atlasway ayrı (port 4323), o henüz V1.
**Tek dosya site:** `index.html` (pure HTML/CSS/JS, GSAP+CountUp CDN) + `models/at-*.html` (13 model sayfası, generator'dan).
**Tema:** koyu #0A0B0D + amber #F5A623, Barlow Condensed + Inter.

## DURUM: ÇOĞU BİTTİ ✅ (2026-06-22 turnkey oturum)

### Tamamlanan
- **İsimlendirme:** AT-10, AT-13, AT-16, AT-20, **AT-25-27**, AT-30, **AT-35-38**, AT-45, AT-55, AT-65, AT-75, AT-100, AT-120 (SKU = AT-(metrik ton), tireli). Dosya slug'ları da at-* (URL'de görünür).
- **ABD birimleri/jargon:** kapasite **lb** (badge US tons), uzanma **ft**, basınç **3,626 psi**. "HSA" sitede yok.
- **Fotoğraflar:** 13 model × **3 açı** (side/hero/front) → `assets/images/models/<slug>-<angle>.jpg` (ffmpeg scale=1600 q3 optimize, ~176KB).
- **Kartlar:** 13'ü de `<a class=model-card href=models/<slug>.html>` + `<img class=model-photo>`. Slider US tons.
- **13 model sayfası:** scroll-3D viewer (full-bleed) + 3-açılı galeri (lightbox **ok butonları + ←→ klavye + Esc**) + specs + CTA. AT-13'te **yük tablosu** (page-13'ten, ft/lb).
- **Scroll-3D (her model):** Seedance 2.0 orbit video (1080p) → `ffmpeg fps=12 scale=1600 q3` → `assets/images/frames/<slug>/f-%04d.jpg` (73 frame) → generator'da `frames=73` → sayfada scroll scrubber. **13/13 çalışıyor.**
- **ANA HERO (index.html):** sinematik sanayi gün batımı görseli (Higgsfield, hero-B=aa302a64) → dolly-in video → 73 frame `assets/images/frames/hero/` → `HERO_FRAMES=73` → scroll'da video ilerler + hero metni soluar. Poster: `assets/images/hero-industrial.jpg`.

### 🔜 SIRADAKİ BÜYÜK İŞ: TEMA DEĞİŞİMİ (2026-06-23 kullanıcı kararı)
Kullanıcı **temayı komple baştan değiştirmek** istiyor — ya sıfırdan "cool & premium" yeni tema, ya da kullanıcı bir hazır tema seçip gönderecek. Mevcut amber/endüstriyel (#0A0B0D + #F5A623) tema KORUNMAYABİLİR. **İçerik/veri hazır** (13 model, fotolar, scroll-3D, yük tabloları, SEO sayfaları) → tema değişince bunlar yeni kabuğa taşınacak. Yeni tema gelene kadar bekle, sonra plan yaz.

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
