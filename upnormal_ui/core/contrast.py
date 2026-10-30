"""
upnormal_ui.core.contrast
~~~~~~~~~~~~~~~~~~~~~~~~~
Kalkulator dan engine koreksi matematis rasio kontras warna berbasis WCAG 2.2.
Menegakkan Hard Invariant: Rasio Kontras (CR) >= 7.0:1 (WCAG AAA Strict).
"""

import colorsys
import re
from typing import Dict, Tuple, Any

HEX_REGEX = re.compile(r"^#?([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$")

def parse_hex_to_rgb(hex_str: str) -> Tuple[int, int, int]:
    """Parse hex color string (3 or 6 chars) into (R, G, B) tuple 0-255."""
    clean = hex_str.strip().lstrip("#")
    if len(clean) == 3:
        clean = "".join([c * 2 for c in clean])
    if len(clean) != 6:
        raise ValueError(f"Format hex warna tidak valid: '{hex_str}'")
    return int(clean[0:2], 16), int(clean[2:4], 16), int(clean[4:6], 16)

def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Format RGB (0-255) to 6-char hex string with leading #."""
    r = max(0, min(255, int(round(r))))
    g = max(0, min(255, int(round(g))))
    b = max(0, min(255, int(round(b))))
    return f"#{r:02x}{g:02x}{b:02x}"

def srgb_channel_to_linear(c_srgb: float) -> float:
    """Convert sRGB channel (0.0 - 1.0) to linear light value."""
    if c_srgb <= 0.04045:
        return c_srgb / 12.92
    return ((c_srgb + 0.055) / 1.055) ** 2.4

def linear_to_srgb_channel(c_lin: float) -> float:
    """Convert linear channel to sRGB (0.0 - 1.0)."""
    if c_lin <= 0.0031308:
        return c_lin * 12.92
    return 1.055 * (c_lin ** (1.0 / 2.4)) - 0.055

def calculate_relative_luminance(hex_str: str) -> float:
    """
    Hitung Relative Luminance (L) sesuai standar WCAG 2.2:
    L = 0.2126 * R_lin + 0.7152 * G_lin + 0.0722 * B_lin
    """
    r, g, b = parse_hex_to_rgb(hex_str)
    r_lin = srgb_channel_to_linear(r / 255.0)
    g_lin = srgb_channel_to_linear(g / 255.0)
    b_lin = srgb_channel_to_linear(b / 255.0)
    return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin

def calculate_contrast_ratio(hex_fg: str, hex_bg: str) -> float:
    """
    Hitung rasio kontras antara dua warna hex:
    CR = (L_terang + 0.05) / (L_gelap + 0.05)
    Output rentang 1.0 hingga 21.0.
    """
    l1 = calculate_relative_luminance(hex_fg)
    l2 = calculate_relative_luminance(hex_bg)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return round((lighter + 0.05) / (darker + 0.05), 2)

def auto_correct_contrast(hex_fg: str, hex_bg: str, target_ratio: float = 7.0) -> Dict[str, Any]:
    """
    Koreksi otomatis kanal Lightness pada HSL agar teks mencapai target_ratio (default 7.0 = AAA).
    Menjaga rona warna (Hue) dan saturasi (Saturation) semaksimal mungkin.
    """
    fg_clean = hex_fg if hex_fg.startswith("#") else f"#{hex_fg}"
    bg_clean = hex_bg if hex_bg.startswith("#") else f"#{hex_bg}"
    
    current_ratio = calculate_contrast_ratio(fg_clean, bg_clean)
    if current_ratio >= target_ratio:
        return {
            "status": "PASS",
            "original_ratio": current_ratio,
            "corrected_hex": fg_clean,
            "target_ratio": target_ratio,
            "adjusted": False,
            "grade": "AAA" if current_ratio >= 7.0 else "AA"
        }

    bg_lum = calculate_relative_luminance(bg_clean)
    r, g, b = parse_hex_to_rgb(fg_clean)
    h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)

    # Tentukan arah iterasi: jika background gelap (lum < 0.5), naikkan lightness ke arah terang (1.0).
    # Jika background terang (lum >= 0.5), turunkan lightness ke arah gelap (0.0).
    direction = 1 if bg_lum < 0.5 else -1
    step = 0.01
    best_hex = fg_clean
    achieved_ratio = current_ratio

    curr_l = l
    while 0.0 <= curr_l <= 1.0:
        curr_l += (direction * step)
        curr_l = max(0.0, min(1.0, curr_l))
        
        test_r, test_g, test_b = colorsys.hls_to_rgb(h, curr_l, s)
        test_hex = rgb_to_hex(test_r * 255, test_g * 255, test_b * 255)
        ratio = calculate_contrast_ratio(test_hex, bg_clean)
        
        if ratio > achieved_ratio:
            achieved_ratio = ratio
            best_hex = test_hex
            
        if ratio >= target_ratio:
            best_hex = test_hex
            achieved_ratio = ratio
            break

    return {
        "status": "CORRECTED" if achieved_ratio >= target_ratio else "BEST_EFFORT",
        "original_hex": fg_clean,
        "background_hex": bg_clean,
        "original_ratio": current_ratio,
        "corrected_hex": best_hex,
        "achieved_ratio": achieved_ratio,
        "target_ratio": target_ratio,
        "adjusted": True,
        "grade": "AAA" if achieved_ratio >= 7.0 else ("AA" if achieved_ratio >= 4.5 else "FAIL")
    }
