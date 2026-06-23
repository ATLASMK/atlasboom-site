# atlasboom.com — DNS Setup

Goal: point **atlasboom.com** from the current Netlify "for sale" landing to this GitHub Pages site.

Domain is registered through **Shopify** ("My Store 5" / 13dh1r-8v.myshopify.com, account atlaschicagollc@gmail.com). DNS records are managed there.

---

## ⚠️ Before you start — DO NOT TOUCH THESE

1. **Do NOT mark `atlasboom.com` as the "Primary domain" in Shopify.**
   Shopify will then redirect your other live site (atlasway.net → SkinAge app)
   through atlasboom.com and break it. Leave atlasway.net as primary.
2. **Do NOT delete the existing MX / SPF / DKIM / DMARC records.**
   Those keep `info@atlasboom.com` working (mailbox is on hostedemail.com).

---

## Step-by-step (Shopify Admin)

1. Sign in: https://admin.shopify.com → store **"My Store 5"**.
2. **Settings → Domains**.
3. Click **atlasboom.com** in the domain list.
4. Click **DNS settings** (or "Manage DNS").

### Replace the A records

Delete the current root A record:
```
A   @   75.2.60.5     ← Netlify, DELETE
```

Add four GitHub Pages A records (you can paste them one at a time):
```
A   @   185.199.108.153
A   @   185.199.109.153
A   @   185.199.110.153
A   @   185.199.111.153
```

### Replace the CNAME for www

Delete the current www CNAME:
```
CNAME   www   darling-pithivier-d94ab3.netlify.app     ← Netlify, DELETE
```

Add the GitHub Pages CNAME:
```
CNAME   www   atlasmk.github.io
```

### Keep these records (DO NOT TOUCH)

```
MX     @     <hostedemail.com mail servers>
TXT    @     v=spf1 ...
TXT    default._domainkey ... (DKIM)
TXT    _dmarc ...
```

Save and exit DNS settings.

---

## After the DNS change

DNS propagation takes 15 minutes to 2 hours. Verify with:

- macOS / Linux: `dig atlasboom.com +short`
- Windows PowerShell: `Resolve-DnsName atlasboom.com -Type A`

You should see the four 185.199.x.x addresses.

### Tell GitHub Pages about the custom domain

The `CNAME` file in this repo (root) already contains `atlasboom.com`, so GitHub
will pick it up automatically. To confirm and turn on HTTPS:

1. Open https://github.com/ATLASMK/atlasboom-site/settings/pages
2. **Custom domain:** should already show `atlasboom.com` (sourced from the `CNAME` file).
3. Wait for **"DNS check successful"** (the green check, takes a few minutes after DNS propagates).
4. Tick **"Enforce HTTPS"** once the certificate is provisioned (Let's Encrypt, automatic, may take up to 24 hours).

---

## Sanity checks

- https://atlasboom.com/ → should serve the premium site (not the Netlify "for sale" landing).
- https://www.atlasboom.com/ → should redirect to the apex.
- https://atlasboom.com/sitemap.xml → 37 URL sitemap.
- `info@atlasboom.com` → still receives email (MX records untouched).

If anything looks wrong, the previous Netlify landing is still hosted at
darling-pithivier-d94ab3.netlify.app and can be reattached by reverting the
A and CNAME records above. Nothing destructive is performed by this DNS change.
