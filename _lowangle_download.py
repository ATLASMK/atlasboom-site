# -*- coding: utf-8 -*-
"""Download 13 Higgsfield lowangle results in parallel + optimize to JPG."""
import os, urllib.request, subprocess, concurrent.futures

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_lowangle_raw")
os.makedirs(ROOT, exist_ok=True)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "images", "models")

# slug -> raw image URL from Higgsfield
URLS = {
 "at-10":     "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122205_4a5980b3-0d1a-43ab-997e-c3aef277afed.jpeg",
 "at-13":     "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122210_f810c08c-cb9e-458f-8cab-93224d48e21e.jpeg",
 "at-16":     "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122214_5e731fb7-7e33-4d83-b22d-67f4cafbf896.png",
 "at-20":     "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122216_bf2544b5-d803-4ef9-841c-8cfb70d9279b.jpeg",
 "at-25-27":  "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122237_dde03c25-c23a-4754-a130-555c07589bdf.jpeg",
 "at-30":     "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122106_fbbcad5c-683a-41d0-a393-aca0043b036c.png",
 "at-35-38":  "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122241_42e06f73-1064-4b4c-ae54-9ae2a576fdc0.jpeg",
 "at-45":     "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122243_4b939880-aca4-464b-a7fd-97a6da1f4c55.jpeg",
 "at-55":     "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122327_0d3649c7-28cd-48fb-8bed-758c9dd841af.jpeg",
 "at-65":     "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122330_3cdd2462-ef99-4774-880b-21d6536c0048.jpeg",
 "at-75":     "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122334_027d6583-a79c-4caa-a621-246294b31271.jpeg",
 "at-100":    "https://d8j0ntlcm91z4.cloudfront.net/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/hf_20260623_122338_b93351ea-0f83-4135-9062-ac4e4882c83d.jpeg",
}

def download_one(slug, url):
    ext = ".png" if url.endswith(".png") else ".jpg"
    raw = os.path.join(ROOT, slug + ext)
    try:
        urllib.request.urlretrieve(url, raw)
    except Exception as e:
        return (slug, "DL_ERR", str(e))
    out = os.path.join(OUT, slug + "-lowangle.jpg")
    # ffmpeg scale=1600 q3 jpg (same recipe as other angles)
    cmd = ["ffmpeg", "-y", "-i", raw, "-vf", "scale=1600:-2", "-q:v", "3", out]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            return (slug, "FFMPEG_ERR", r.stderr[-200:])
        size = os.path.getsize(out)
        return (slug, "OK", size)
    except Exception as e:
        return (slug, "FFMPEG_EXC", str(e))

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(lambda t: download_one(*t), URLS.items()))

for slug, status, info in results:
    print(f"{slug:10s} {status} {info}")
print("DONE")
