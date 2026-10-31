"""
upnormal_ui.core.color_scale
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generator Skala Warna Persepsi 11-Langkah (50 - 950) Berbasis Ruang Warna HSL/RGB.
Menghitung luminansi relatif untuk setiap anak tangga dan menentukan warna teks (kontras)
secara deterministik agar selalu memenuhi standar aksesibilitas WCAG 2.2 AAA (>= 7:1) atau AA (>= 4.5:1).
"""

import colorsys
from typing import Dict, Any, List
from decimal import Decimal
from upnormal_ui.core.contrast import (
    parse_hex_to_rgb,
    rgb_to_hex,
    calculate_relative_luminance,
    calculate_contrast_ratio
)

# Tangga tingkat kecerahan (Lightness Target) untuk 11 langkah standar
STEP_LIGHTNESS = [
    ("50", 0.96),
    ("100", 0.92),
    ("200", 0.84),
    ("300", 0.74),
    ("400", 0.62),
    ("500", 0.50),  # Midpoint / Brand base
    ("600", 0.40),
    ("700", 0.30),
    ("800", 0.20),
    ("900", 0.12),
    ("950", 0.06),
]

def generate_11_step_scale(hex_color: str, name: str = "brand") -> Dict[str, Any]:
    """
    Hasilkan skala 11-langkah (50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950)
    lengkap dengan warna teks pendamping (foreground) yang terverifikasi kontras tinggi.
    """
    r, g, b = parse_hex_to_rgb(hex_color)
    h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)

    steps = {}
    css_vars = []
    tailwind_colors = {}

    for step_name, target_l in STEP_LIGHTNESS:
        # Sedikit modulasi saturasi: step sangat terang (50-100) dan sangat gelap (900-950)
        # saturasi diturunkan sedikit agar tidak memekakkan mata
        adj_s = s
        if target_l > 0.85:
            adj_s = min(s, 0.75)
        elif target_l < 0.15:
            adj_s = min(s, 0.85)

        step_r, step_g, step_b = colorsys.hls_to_rgb(h, target_l, adj_s)
        step_hex = rgb_to_hex(step_r * 255, step_g * 255, step_b * 255)

        # Hitung kontras teks pendamping (hitam vs putih)
        cr_dark = calculate_contrast_ratio("#000000", step_hex)
        cr_light = calculate_contrast_ratio("#ffffff", step_hex)

        fg_hex = "#000000" if cr_dark >= cr_light else "#ffffff"
        best_cr = max(cr_dark, cr_light)
        grade = "AAA" if best_cr >= 7.0 else ("AA" if best_cr >= 4.5 else "FAIL")

        steps[step_name] = {
            "hex": step_hex,
            "fg_hex": fg_hex,
            "contrast_ratio": best_cr,
            "grade": grade,
            "luminance": round(calculate_relative_luminance(step_hex), 4)
        }

        css_vars.append(f"  --color-{name}-{step_name}: {step_hex};")
        css_vars.append(f"  --color-{name}-{step_name}-fg: {fg_hex};")
        tailwind_colors[step_name] = step_hex

    css_block = f":root {{\n" + "\n".join(css_vars) + "\n}"

    return {
        "name": name,
        "base_hex": hex_color if hex_color.startswith("#") else f"#{hex_color}",
        "steps": steps,
        "css_variables": css_block,
        "tailwind_config": {name: tailwind_colors}
    }
