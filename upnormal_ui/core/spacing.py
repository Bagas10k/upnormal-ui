"""
upnormal_ui.core.spacing
~~~~~~~~~~~~~~~~~~~~~~~~
Engine Kecerdasan Spasial & Ritme Penataan Tata Letak (UI Spacing Intelligence).
Menegakkan doktrin penataan ruang 4-tingkat:
1. Tingkat Halaman (Page level): max-width, safe area, inline padding adaptif.
2. Tingkat Seksi (Section level): pemisah antar-kelompok konten makro (64px - 96px).
3. Tingkat Komponen (Component level): padding kontainer (16px - 24px) & card gap.
4. Tingkat Mikro (Micro level): icon-label gap (8px), badge padding, kontrol inline (12px).
"""

import re
from typing import Dict, Any, List, Optional

# Skala ritme modular berbasis 4px (micro) dan 8px (komponen & layout)
SPACING_SCALE = {
    "1": {"px": 4, "rem": "0.25rem", "role": "Micro gap / Hairline offset"},
    "2": {"px": 8, "rem": "0.5rem", "role": "Icon-to-label gap / Badge padding-y"},
    "3": {"px": 12, "rem": "0.75rem", "role": "Inline controls gap / Badge padding-x"},
    "4": {"px": 16, "rem": "1rem", "role": "Base input padding / Dense card padding"},
    "5": {"px": 20, "rem": "1.25rem", "role": "Standard card padding (Mobile)"},
    "6": {"px": 24, "rem": "1.5rem", "role": "Standard card padding (Desktop) / Grid gap"},
    "8": {"px": 32, "rem": "2rem", "role": "Comfortable container padding / Section header gap"},
    "10": {"px": 40, "rem": "2.5rem", "role": "Card-to-section boundary"},
    "12": {"px": 48, "rem": "3rem", "role": "Sub-section vertical rhythm"},
    "16": {"px": 64, "rem": "4rem", "role": "Major section vertical separation (Mobile)"},
    "20": {"px": 80, "rem": "5rem", "role": "Major section vertical separation (Desktop)"},
    "24": {"px": 96, "rem": "6rem", "role": "Hero & landing page breathing room"}
}

DENSITY_PRESETS = {
    "compact": {
        "name": "Compact (Data-Heavy & Finansial Kasir)",
        "page_inline": "px-4 sm:px-6",
        "section_gap": "space-y-10 lg:space-y-12",
        "card_padding": "p-4 sm:p-5",
        "grid_gap": "gap-3 sm:gap-4",
        "table_cell": "py-2 px-3 text-xs",
        "control_gap": "gap-2"
    },
    "standard": {
        "name": "Standard (Produktivitas & Dashboard Modern)",
        "page_inline": "px-4 sm:px-6 lg:px-8",
        "section_gap": "space-y-14 lg:space-y-16",
        "card_padding": "p-5 sm:p-6 lg:p-7",
        "grid_gap": "gap-4 sm:gap-6",
        "table_cell": "py-2.5 px-4 text-xs sm:text-sm",
        "control_gap": "gap-3"
    },
    "comfortable": {
        "name": "Comfortable (Situs Portofolio & Showroom)",
        "page_inline": "px-6 sm:px-8 lg:px-12",
        "section_gap": "space-y-16 lg:space-y-24",
        "card_padding": "p-6 sm:p-8 lg:p-10",
        "grid_gap": "gap-6 sm:gap-8",
        "table_cell": "py-3.5 px-5 text-sm",
        "control_gap": "gap-4"
    }
}

# Regex deteksi anti-pattern penataan ruang
ARBITRARY_SPACING_REGEX = re.compile(r"\b(?:p|m|gap|top|bottom|left|right)-\[(\d+)px\]")
OVERSIZED_MOBILE_PADDING = re.compile(r"\bp-(?:8|10|12|16)\b(?!\s+(?:sm|md|lg):)")
MAGIC_ALIGNMENT_OFFSET = re.compile(r"\bpt-(?:5|6|7|8)\b(?=.*(?:toggle|switch|checkbox))", re.IGNORECASE)
UNDERSIZED_BUTTON_TARGET = re.compile(r"<button\b[^>]*\bclass=[\"'][^\"']*\b(?:p-1|py-0\.5|px-1|p-0\.5)\b", re.IGNORECASE)

# ==============================================================================
# DOKTRIN SPASIAL UPNORMAL KREATIF (CREATIVE EDITORIAL RHYTHM & FLUID CLAMP)
# ==============================================================================
CREATIVE_SPACING_RATIOS = {
    "golden_editorial": {"ratio": 1.618, "description": "Pemisahan asimetris berkelas Awwwards/Godly (konten vs whitespace)"},
    "hierarchical_dominance": {"ratio": 2.0, "description": "Bobot ganda 2:1 untuk Bento Grid asimetris (hero cell vs support cell)"},
    "dramatic_contrast": {"ratio": 3.0, "description": "Panggung akromatik megah (hero padding 96px vs card internal 32px)"}
}

def generate_fluid_clamp(min_px: int, max_px: int, min_vw: int = 390, max_vw: int = 1280) -> str:
    """
    Hitung nilai CSS clamp() matematis linier antara min_px (pada min_vw) dan max_px (pada max_vw).
    Formula: clamp(MIN, SLOPE * 100vw + INTERCEPT, MAX)
    Menghasilkan responsivitas fluida murni tanpa jeda breakpoint yang kaku.
    """
    slope = (max_px - min_px) / (max_vw - min_vw)
    intercept = min_px - slope * min_vw

    min_rem = round(min_px / 16.0, 4)
    max_rem = round(max_px / 16.0, 4)
    slope_vw = round(slope * 100.0, 4)
    intercept_rem = round(intercept / 16.0, 4)

    sign = "+" if intercept_rem >= 0 else "-"
    abs_intercept = abs(intercept_rem)

    return f"clamp({min_rem}rem, {slope_vw}vw {sign} {abs_intercept}rem, {max_rem}rem)"

def get_upnormal_creative_spacing_preset() -> Dict[str, Any]:
    """
    Hasilkan token penataan ruang kreatif Upnormal berjiwa seni (fluid clamp & asymmetric balance).
    """
    return {
        "status": "UPNORMAL_CREATIVE_SPACING_V2",
        "ratios": CREATIVE_SPACING_RATIOS,
        "fluid_tokens": {
            "section_padding_y": generate_fluid_clamp(48, 112),  # 48px di mobile -> 112px di desktop
            "page_padding_x": generate_fluid_clamp(16, 48),       # 16px di mobile -> 48px di desktop
            "card_padding": generate_fluid_clamp(20, 36),         # 20px di mobile -> 36px di desktop
            "hero_headline_gap": generate_fluid_clamp(24, 48),    # 24px di mobile -> 48px di desktop
        },
        "invariants": [
            "Touch target minimum 44px x 44px (W3C AAA) untuk tombol dan elemen interaktif.",
            "Bottom clearance: padding-bottom wajib menyisakan ruang untuk floating dock + env(safe-area-inset-bottom).",
            "Optical hanging punctuation & display offset: gunakan negative margin halus (misal -ml-1) pada huruf besar display awal.",
            "Asymmetric editorial rhythm: jangan buat padding sekeliling simetris membosankan (gunakan rasio Golden 1:1.618)."
        ]
    }

def get_spacing_system(density: str = "standard") -> Dict[str, Any]:
    """Hasilkan konfigurasi sistem penataan ruang (spacing tokens) siap pakai."""
    d = density.lower().strip()
    preset = DENSITY_PRESETS.get(d, DENSITY_PRESETS["standard"])

    css_vars = []
    for k, v in SPACING_SCALE.items():
        css_vars.append(f"  --space-{k}: {v['rem']}; /* {v['px']}px - {v['role']} */")

    css_block = ":root {\n" + "\n".join(css_vars) + "\n}"

    return {
        "density_mode": d,
        "preset": preset,
        "scale": SPACING_SCALE,
        "css_variables": css_block,
        "rules": [
            "Terapkan 4 tingkat penataan: Page > Section > Component > Micro.",
            "Gunakan parent-controlled 'gap' untuk elemen bersaudara (sibling), bukan margin liar.",
            "Padding kontainer di mobile wajib adaptif: p-5 sm:p-6 lg:p-8 (hindari p-8 kaku di layar sempit).",
            "Jarak antar-seksi makro (64px - 96px) wajib lebih besar dari jarak internal komponen (16px - 24px)."
        ]
    }

def audit_spacing_classes(html_or_classes: str) -> Dict[str, Any]:
    """
    Pindai kode terhadap cacat penataan jarak:
    1. Padding besar di mobile tanpa breakpoint (misal: p-8 tanpa sm:p-8) yang memakan lebar layar ponsel.
    2. Jarak acak arbitrer non-skala (misal: p-[17px], m-[23px]).
    3. Magic vertical offset (misal: pt-6 palsu untuk meluruskan elemen form).
    """
    issues = []

    # 1. Cek oversized padding on mobile
    oversized = OVERSIZED_MOBILE_PADDING.findall(html_or_classes)
    if oversized:
        issues.append({
            "type": "OVERSIZED_MOBILE_PADDING",
            "severity": "HIGH",
            "matches": oversized[:5],
            "description": "Ditemukan padding besar statis (p-8/p-10/p-12) tanpa breakpoint adaptif. Di layar ponsel (390px), padding ini memakan ruang horizontal secara berlebihan.",
            "solution": "Ganti dengan skala responsif: 'p-5 sm:p-6 lg:p-8'."
        })

    # 2. Cek arbitrary non-scale spacing
    arbitrary = ARBITRARY_SPACING_REGEX.findall(html_or_classes)
    if arbitrary:
        non_standard = [px for px in arbitrary if int(px) % 4 != 0]
        if non_standard:
            issues.append({
                "type": "ARBITRARY_NON_SCALE_SPACING",
                "severity": "MEDIUM",
                "matches": non_standard[:5],
                "description": f"Ditemukan jarak piksel arbitrer yang tidak mematuhi kelipatan 4px/8px: {non_standard[:5]}.",
                "solution": "Gunakan token standar terdekat (misal: 12px -> p-3, 16px -> p-4, 24px -> p-6)."
            })

    # 3. Cek magic alignment offset
    magic = MAGIC_ALIGNMENT_OFFSET.findall(html_or_classes)
    if magic:
        issues.append({
            "type": "MAGIC_ALIGNMENT_OFFSET",
            "severity": "LOW",
            "matches": magic[:3],
            "description": "Ditemukan pt-6 atau offset vertikal artifisial untuk menyamakan tinggi kontrol form.",
            "solution": "Gunakan flexbox container dengan 'items-center' atau grid alignment yang seimbang secara struktural."
        })

    # 4. Cek undersized click targets on buttons (< 44px)
    undersized_btns = UNDERSIZED_BUTTON_TARGET.findall(html_or_classes)
    if undersized_btns:
        issues.append({
            "type": "UNDERSIZED_INTERACTIVE_TARGET",
            "severity": "MEDIUM",
            "matches": undersized_btns[:3],
            "description": "Ditemukan tombol interaktif dengan padding terlalu kecil (p-1/py-0.5) tanpa batas min-w/min-h, melanggar standar touch target WCAG AAA 44x44px.",
            "solution": "Terapkan padding minimum 'py-2.5 px-5' atau pastikan elemen memiliki tinggi/lebar minimal 44px ('min-h-[44px] min-w-[44px]')."
        })

    is_clean = len(issues) == 0
    return {
        "status": "CLEAN" if is_clean else "SPACING_ISSUES_DETECTED",
        "total_issues": len(issues),
        "issues": issues,
        "verdict": "Penataan ruang mematuhi ritme modular 4px/8px dan responsif adaptif." if is_clean else "Terdeteksi ketidakseimbangan spasial. Terapkan rekomendasi ritme Upnormal."
    }
