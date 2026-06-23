# -*- coding: utf-8 -*-
"""Crop the load chart diagrams from HS-300 and HS-360 catalog pages
(only the right column = both K8 and K8+K5 charts, no vehicle photo)."""
import os
from PIL import Image, ImageDraw

SRC = {
 "at-100": r"C:\Users\PC\Desktop\HSA CRANE\MODELLER\HS 300 - 100 TON\HS-300_2-ozellikler.png",
 "at-120": r"C:\Users\PC\Desktop\HSA CRANE\MODELLER\HS 360 - 120 TON\HS-360_2-ozellikler.png",
}

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "images", "charts")
os.makedirs(OUT_DIR, exist_ok=True)

for slug, path in SRC.items():
    img = Image.open(path)
    w, h = img.size
    # Take only the K8+K5 (8 hydraulic + 5 manual, the wider-reach variant)
    # diagram and crop tight enough that the catalog title bar, the HSA
    # brand mark on the page, and the left vehicle photo are all left out.
    L, R = int(w * 0.415), int(w * 0.945)
    T, B = int(h * 0.625), int(h * 0.945)
    crop = img.crop((L, T, R, B)).convert("RGB")
    target_w = 1280
    crop = crop.resize((target_w, int(target_w * crop.size[1] / crop.size[0])), Image.LANCZOS)
    out = os.path.join(OUT_DIR, f"{slug}-loadchart.png")
    crop.save(out, optimize=True)
    print(f"{slug}: -> {crop.size} {os.path.getsize(out)} bytes")
print("DONE")
