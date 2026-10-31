"""
upnormal_ui.core.anti_slop
~~~~~~~~~~~~~~~~~~~~~~~~~~
Linter heuristik dan detektor otomatis 8 Dosa AI UI Slop.
Menegakkan doktrin Tabula Rasa Mas Bagas: membasmi bias template model generik.
"""

import re
from typing import Dict, List, Any

# Heuristik Pola Dosa AI Slop
PATTERNS = [
    {
        "id": "SLOP_01_PURPLE_CYAN_GRADIENT",
        "name": "Tombol/Elemen Gradien Ungu-Cyan Murahan",
        "regex": re.compile(r"(from-purple-[4-6]00\s+to-cyan-[4-6]00|linear-gradient\([^)]*purple[^)]*cyan[^)]*\))", re.IGNORECASE),
        "severity": "CRITICAL",
        "description": "Gradien ungu ke cyan adalah ciri khas utama template AI generik 2023-2024 yang tidak memiliki rasa seni.",
        "solution": "Gunakan warna akromatik dengan aksen tunggal berani (misal: Solid Obsidian + Aksen Cyan 5%, atau Hard Offset Shadow 4px)."
    },
    {
        "id": "SLOP_02_EMOJI_AS_UI_ICON",
        "name": "Penggunaan Emoji sebagai Ikon Antarmuka",
        "regex": re.compile(r"([🚀✨🔥💡🤖🎉⚡👍🏆📦🛒])(?=\s*<\/button>|\s*<\/a>|\s*<\/span>|\s*class=)", re.UNICODE),
        "severity": "CRITICAL",
        "description": "Emoji di dalam tombol, badge, atau navigasi menghasilkan kesan amatir dan inkonsisten antar peramban/OS.",
        "solution": "Ganti dengan vektor SVG presisi dari Iconify MCP (misal: Lucide, Tabler, atau Heroicons) dengan ukuran standar 20-24px."
    },
    {
        "id": "SLOP_03_LOW_CONTRAST_GRAY",
        "name": "Teks Abu-Abu Pudar di Panggung Gelap",
        "regex": re.compile(r"class=[\"'][^\"']*(?:bg-(?:slate|zinc|gray|neutral)-(?:900|950)|bg-black)[^\"']*(?:text-(?:gray|slate|zinc|neutral)-(?:400|500))[^\"']*[\"']", re.IGNORECASE),
        "severity": "HIGH",
        "description": "Teks abu-abu redup di atas latar belakang gelap melanggar WCAG AAA dan membuat informasi sulit dibaca.",
        "solution": "Naikkan kontras ke minimum 7:1 (Gunakan text-slate-200 atau text-white dengan Two-Layer Silhouette)."
    },
    {
        "id": "SLOP_04_MUDDY_DIFFUSE_SHADOW",
        "name": "Bayangan Difus Tebal Kusam (Muddy Blur)",
        "regex": re.compile(r"(shadow-(?:2xl|xl)\s+shadow-(?:indigo|purple|cyan|blue)-\d+00|box-shadow:[^;]*0\s+25px\s+50px)", re.IGNORECASE),
        "severity": "MEDIUM",
        "description": "Bayangan berwarna dengan blur besar (diffuse glow) menciptakan polusi visual dan menutupi hierarki kartu.",
        "solution": "Gunakan Hard Offset Shadow (misal: box-shadow: 4px 4px 0px #000000) atau batas garis pekat (border: 1.5px solid #1e293b)."
    },
    {
        "id": "SLOP_05_RAINBOW_TEXT_GRADIENT",
        "name": "Teks Gradien Pelangi Multi-Warna",
        "regex": re.compile(r"bg-clip-text\s+text-transparent\s+bg-gradient-to-r\s+from-\w+-\d+00\s+via-\w+-\d+00\s+to-\w+-\d+00", re.IGNORECASE),
        "severity": "CRITICAL",
        "description": "Gradien teks dengan lebih dari 2 spektrum warna mengorbankan keterbacaan (*legibility*) demi kesan futuristik palsu.",
        "solution": "Kembalikan teks ke warna solid berbobot tegas (font-weight 800/900) dengan kontras optik bersih."
    },
    {
        "id": "SLOP_06_RIGID_BENTO_GRID",
        "name": "Bento Grid Simetris Monoton",
        "regex": re.compile(r"grid-cols-1\s+md:grid-cols-3\s+gap-4(?=[\s\S]*?<div[\s\S]*?<div[\s\S]*?<div)", re.IGNORECASE),
        "severity": "LOW",
        "description": "3 kartu bento berukuran persis sama tanpa hierarki asimetris adalah pola malas bawaan model AI.",
        "solution": "Gunakan grid asimetris (misal: col-span-2 untuk hero cell, sel sekunder bertumpuk dengan rasio matematis 2:1)."
    },
    {
        "id": "SLOP_07_UNSTYLED_NATIVE_SELECT",
        "name": "Kontrol Bawaan Peramban Tanpa Kustomisasi",
        "regex": re.compile(r"<select(?![^>]*class=[\"'][^\"']*(?:appearance-none|border-|rounded-))[^>]*>", re.IGNORECASE),
        "severity": "HIGH",
        "description": "Elemen native select/input tanpa penyesuaian merusak kesatuan desain dan terasa tidak selesai.",
        "solution": "Gunakan custom control wrapper (appearance-none dengan panah SVG kustom) atau komponen taktil kustom."
    },
    {
        "id": "SLOP_08_STIFF_POPUP_DIALOG",
        "name": "Modal Pop-up Kaku Tanpa Kontinuitas Objek",
        "regex": re.compile(r"<dialog(?![^>]*data-morph)[^>]*>|<div[^>]*role=[\"']dialog[\"'](?![^>]*transition)[^>]*>", re.IGNORECASE),
        "severity": "MEDIUM",
        "description": "Dialog yang muncul tiba-tiba tanpa transisi morphing memutus alur pandang pengguna (*visual cognitive jump*).",
        "solution": "Terapkan In-Place Morphing (GSAP FLIP atau spring cubic-bezier) di mana tombol pemanggil mengembang menjadi dialog."
    },
    {
        "id": "SLOP_09_ORNAMENTAL_KICKER_BADGE_CLUTTER",
        "name": "Badge Clutter & Kicker Pill Pamer Teknis",
        "regex": re.compile(r"(?:class=[\"'][^\"']*(?:hero-pill|badge-tag|hero-badges-strip)[^\"']*|(?:\b(?:Zero\s*AI-Slop|WCAG\s*AAA\s*\(?≥?\s*7:1\)?|60\s*FPS\s*In-Place|PORTOFOLIO\s*RESMI\s*VOL)[^<]*<\/span>))", re.IGNORECASE),
        "severity": "CRITICAL",
        "description": "Kicker badge mengambang dan deretan tag pamer teknis (seperti 'Zero AI-Slop', 'WCAG AAA', '60 FPS') adalah polusi visual AI yang murahan dan menjijikkan.",
        "solution": "Hapus total badge clutter ornamental. Biarkan tipografi bersih, ruang lega, dan kualitas layout yang berbicara."
    }
]

def scan_anti_slop(code: str) -> Dict[str, Any]:
    """
    Pindai kode HTML / Blade / JSX / CSS terhadap 8 Dosa AI UI Slop.
    Mengembalikan skor kualitas (0-100), daftar pelanggaran, dan resep solusi Upnormal.
    """
    violations = []
    total_penalty = 0

    for p in PATTERNS:
        matches = list(p["regex"].finditer(code))
        if matches:
            count = len(matches)
            weight = {"CRITICAL": 25, "HIGH": 15, "MEDIUM": 10, "LOW": 5}[p["severity"]]
            penalty = weight * min(count, 3)
            total_penalty += penalty
            
            snippets = [m.group(0)[:80] for m in matches[:3]]
            violations.append({
                "rule_id": p["id"],
                "rule_name": p["name"],
                "severity": p["severity"],
                "occurrences": count,
                "snippets": snippets,
                "description": p["description"],
                "upnormal_solution": p["solution"]
            })

    score = max(0, 100 - total_penalty)
    status = "UPNORMAL_EXCELLENCE" if score >= 90 else ("SLOP_DETECTED" if score < 70 else "NEEDS_POLISH")

    return {
        "score": score,
        "status": status,
        "total_violations": len(violations),
        "violations": violations,
        "verdict": "Kode bebas dari pola AI Slop generik. Siap rilis!" if score >= 90 else "Terdeteksi pola template generik AI. Terapkan rekomendasi Upnormal untuk mengubahnya menjadi karya seni berkelas."
    }
