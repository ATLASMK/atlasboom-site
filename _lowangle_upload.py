# -*- coding: utf-8 -*-
"""One-shot uploader: PUT 13 hero JPGs to presigned Higgsfield URLs."""
import os, sys, urllib.request, concurrent.futures

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "images", "models")

UPLOADS = [
 ("at-10",     "c5b4d822-e38e-470c-b23e-1f57376066ac", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/c5b4d822-e38e-470c-b23e-1f57376066ac.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=cbcc9daf7302173c551ca30eb6a0dc69bfb81eccdcf63a2a5c1994ade165474f"),
 ("at-13",     "1bdcee23-3929-4f00-bc55-8ba4dc9e5a56", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/1bdcee23-3929-4f00-bc55-8ba4dc9e5a56.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=278bdab5e0972f749ac8ed5f1a3a428b2a8c677f7d2f009ee4a9530ddc434598"),
 ("at-16",     "e630e55c-e71b-4929-a7c1-90b431bac9dc", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/e630e55c-e71b-4929-a7c1-90b431bac9dc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=a157fb86b745dae59fa6cdffe744a6902dcbf909aef213efaac1541dcd373927"),
 ("at-20",     "9b501c8e-130b-49dd-98f0-fba17e25b170", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/9b501c8e-130b-49dd-98f0-fba17e25b170.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=e4eaf12e3fe1263bb4cb855b9f9310a282a43871407a0a35d2fbf5400a0aac3b"),
 ("at-25-27",  "681338eb-d73f-4e94-b7b7-bf87913c8b59", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/681338eb-d73f-4e94-b7b7-bf87913c8b59.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=b2fa1f2a319523043657c141a696d39a1bb19347fa4d1caf17a1b8a902422da2"),
 ("at-30",     "7d6b4ba8-b9cf-4be4-9679-db5cbe3a4852", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/7d6b4ba8-b9cf-4be4-9679-db5cbe3a4852.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121843Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=6d911c6a56875f84c810128f7c780ea3a2af8225740849e36e1326aff48abe98"),
 ("at-35-38",  "c796c767-47d1-474b-b494-1fbca70ac67a", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/c796c767-47d1-474b-b494-1fbca70ac67a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=660173c0becfb0a83c504eafe7df726790f9425faa4269dbdb86ad4b4ca3ff44"),
 ("at-45",     "1f6d5abb-afbb-414f-b81e-a591ad4a838b", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/1f6d5abb-afbb-414f-b81e-a591ad4a838b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=fc04c580e9be9166bc70288b552f99a43f185f6a71d3037022a5991d715f032f"),
 ("at-55",     "36be9c84-5f23-4be8-b89a-81e0ba71f187", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/36be9c84-5f23-4be8-b89a-81e0ba71f187.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=4d0fd19f9b6c2594ebfe0af5e10b1c8d5e5cf696da2579d8277ca0844ed7f7f7"),
 ("at-65",     "eaf3f78a-1dfb-4eba-b41f-4bdeee88d802", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/eaf3f78a-1dfb-4eba-b41f-4bdeee88d802.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=87d8d5ad52528df39c4e5c83c0891b2cfa227fba23f788aad8575506543d5d95"),
 ("at-75",     "20add336-4ade-40e2-a8da-c717d9dd5149", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/20add336-4ade-40e2-a8da-c717d9dd5149.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=0ec83ca002f867ed2356a34f2c66e0495aeea2039654430b637c2cd76e4446b3"),
 ("at-100",    "45ad7687-3337-4e73-b734-77549b693ce5", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/45ad7687-3337-4e73-b734-77549b693ce5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=5d0afd713d7ea528ce0174579a84c342e9f977a087f5ba5152570701a3bf5e5d"),
 ("at-120",    "ce1b3f7f-3038-4329-b602-7ed74bde36cc", "https://upload.higgsfield.ai/user_3Eq3lkNUD37wbMOn7ZOCWiNVmQP/ce1b3f7f-3038-4329-b602-7ed74bde36cc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYPNTVMCGYPZMTKFK%2F20260623%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Date=20260623T121842Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=fa285bc1a3db6eba41cc9fa4d084309e75f81e1e95de7ea85036a7f169b1e710"),
]

def put_one(slug, media_id, url):
    path = os.path.join(ROOT, slug + "-hero.jpg")
    with open(path, "rb") as f:
        body = f.read()
    req = urllib.request.Request(url, data=body, method="PUT",
                                 headers={"Content-Type": "image/jpeg"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return (slug, r.status, len(body), media_id)
    except Exception as e:
        return (slug, "ERR", str(e), media_id)

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(lambda t: put_one(*t), UPLOADS))

for slug, status, size, mid in results:
    print(f"{slug:10s} {status} {size}  media={mid}")
print("DONE")
