"""
upnormal_ui.core.aspect_ratio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arsitektur Rasio Visual (Aspect Ratio Standards) & Solusi "Card Fatigue" (Dekartunisasi).
Menghilangkan kebiasaan "box soup" (tumpukan kardus berlebih) dan menegakkan
standar proporsi visual terkalibrasi serta 5 alternatif tata letak borderless.
"""

import re
from typing import Dict, Any, List, Optional

# ==============================================================================
# TAKSONOMI 8 RASIO VISUAL BAKU UI/UX
# ==============================================================================
ASPECT_RATIOS_REGISTRY: Dict[str, Dict[str, Any]] = {
    "1:1": {
        "name": "Square (1:1)",
        "decimal": 1.00,
        "css_value": "1 / 1",
        "tailwind_class": "aspect-square",
        "character": "Fokus Sentral & Simetris",
        "optimal_usage": "Avatar profil, icon grid, thumbnail produk fashion/sepatu, grid galeri. Paling netral dan stabil di mobile.",
        "cls_zero_css": "aspect-ratio: 1 / 1; width: 100%; object-fit: cover;"
    },
    "4:3": {
        "name": "Classic Standard (4:3)",
        "decimal": 1.33,
        "css_value": "4 / 3",
        "tailwind_class": "aspect-[4/3]",
        "character": "Informasi Ringkas & Stabil",
        "optimal_usage": "Kartu artikel berita klasik, modal dialog pop-up, preview dokumen/PDF, compact showcase.",
        "cls_zero_css": "aspect-ratio: 4 / 3; width: 100%; object-fit: cover;"
    },
    "3:2": {
        "name": "Golden Photography (3:2)",
        "decimal": 1.50,
        "css_value": "3 / 2",
        "tailwind_class": "aspect-[3/2]",
        "character": "Fotografi Alami Sensor 35mm",
        "optimal_usage": "Katalog arsitektur, lanskap produk detail, cover portofolio fotografi.",
        "cls_zero_css": "aspect-ratio: 3 / 2; width: 100%; object-fit: cover;"
    },
    "16:9": {
        "name": "Widescreen Media (16:9)",
        "decimal": 1.7778,
        "css_value": "16 / 9",
        "tailwind_class": "aspect-video",
        "character": "Standar Video & Hero Lebar",
        "optimal_usage": "Video player, thumbnail YouTube, banner presentasi, header dashboard analitik utama.",
        "cls_zero_css": "aspect-ratio: 16 / 9; width: 100%; object-fit: cover;"
    },
    "21:9": {
        "name": "Ultrawide Cinematic (21:9)",
        "decimal": 2.3333,
        "css_value": "21 / 9",
        "tailwind_class": "aspect-[21/9]",
        "character": "Panorama & Banner Strip Tipis",
        "optimal_usage": "Hero banner tipis di landing page, strip promosi atas, dashboard multi-monitor agar tidak memakan ruang vertikal.",
        "cls_zero_css": "aspect-ratio: 21 / 9; width: 100%; object-fit: cover;"
    },
    "4:5": {
        "name": "Vertical Portrait (4:5)",
        "decimal": 0.80,
        "css_value": "4 / 5",
        "tailwind_class": "aspect-[4/5]",
        "character": "Raja Feed Mobile (Maximum Screen Coverage)",
        "optimal_usage": "Format terbaik kartu media di ponsel (Instagram/TikTok carousel). Menutup ruang layar secara maksimal tanpa terpotong (no dead space).",
        "cls_zero_css": "aspect-ratio: 4 / 5; width: 100%; object-fit: cover;"
    },
    "9:16": {
        "name": "Full Vertical (9:16)",
        "decimal": 0.5625,
        "css_value": "9 / 16",
        "tailwind_class": "aspect-[9/16]",
        "character": "Imersif Layar Penuh Ponsel",
        "optimal_usage": "Story, Reels, Shorts, onboarding mobile modal layar penuh.",
        "cls_zero_css": "aspect-ratio: 9 / 16; width: 100%; object-fit: cover;"
    },
    "1.618:1": {
        "name": "Golden Ratio Phi (1.618:1)",
        "decimal": 1.618,
        "css_value": "1.618 / 1",
        "tailwind_class": "aspect-[1.618/1]",
        "character": "Harmoni Rasio Emas Asimetris",
        "optimal_usage": "Pembagian tata letak split-pane (Master 61.8% vs Detail 38.2%), sangat elegan untuk majalah digital dan editorial.",
        "cls_zero_css": "aspect-ratio: 1.618 / 1; width: 100%; object-fit: cover;"
    }
}

# ==============================================================================
# DOKTRIN DEKARTUNISASI & ELIMINASI CARD FATIGUE
# ==============================================================================
CARD_FATIGUE_DOCTRINE = {
    "philosophy": (
        "Card Fatigue (Penyakit Kotak Berlebihan) adalah kebiasaan malas membungkus setiap kelompok data "
        "ke dalam border kotak + rounded + background tebal ('box soup'). Ini memicu pemborosan ruang vertikal, "
        "padding berlipat, dan melelahkan mata pengguna. Informasi profesional harus mengalir melalui ritme tipografi "
        "dan garis rambut ultra-tipis, bukan tumpukan kardus."
    ),
    "when_cards_allowed": [
        "Heterogen & Mandiri: Setiap entitas memiliki status, metadata, dan tipe aksi yang berbeda total (misal: pricing tier cards).",
        "Bisa Dimanipulasi Independen: Elemen bisa di-drag-and-drop (Kanban board), di-swipe, atau di-reorder secara fisik.",
        "Katalog Showcase: Kartu etalase produk e-commerce atau portofolio visual mandiri."
    ],
    "when_cards_forbidden": [
        "Data Homogen Berulang: Riwayat transaksi, daftar mutasi, log aktivitas, tabel master data (membungkus 50 transaksi ke dalam 50 kartu adalah bencana UX).",
        "Ringkasan KPI / Metrik Utama: Memecah 4 angka metrik ke dalam 4 kotak tebal memakan 30% tinggi layar secara sia-sia.",
        "Formulir & Dokumen: Isian formulir berurutan tidak boleh dipecah-pecah ke dalam kotak-kotak terisolasi."
    ],
    "borderless_alternatives": [
        {
            "pattern": "1. Rule-Based (Hairline Separator)",
            "technique": "border-b: 1px solid rgba(255,255,255,0.08) atau divider ultra-tipis",
            "advantage": "Informasi mengalir bersih seperti majalah/koran modern tanpa sekat kardus tebal."
        },
        {
            "pattern": "2. Surface Tint Banding (Wash Area)",
            "technique": "Zebra pergeseran warna latar belakang halus (misal #0f172a ke #141f36) tanpa garis border",
            "advantage": "Membedakan grup data secara instan tanpa menambah bobot visual garis pinggir."
        },
        {
            "pattern": "3. Continuous Data Surfaces (Row Density)",
            "technique": "Baris interaktif satu kanvas utuh (ala Linear / Stripe) dengan hover state halus",
            "advantage": "Densitas data tinggi, pemindaian cepat, menghemat 50% ruang layar."
        },
        {
            "pattern": "4. Typographic Anchor & Proximity",
            "technique": "Kontras tipografi H2 display tebal + jeda vertikal 24px-32px (Law of Proximity Gestalt)",
            "advantage": "Mata mengenali babak baru secara alami tanpa butuh kotak pembungkus."
        },
        {
            "pattern": "5. Horizontal Split Strip (In-line Key-Value)",
            "technique": "Susunan angka KPI horizontal 1 baris datar dipisahkan garis vertikal tipis (|)",
            "advantage": "Menghemat hingga 60% ruang vertikal dibanding 4 kartu KPI terpisah."
        }
    ]
}

# Regex deteksi Card Fatigue (tumpukan card repetitif)
EXCESSIVE_CARD_REGEX = re.compile(r"(?:class=[\"'][^\"']*(?:rounded-2xl|rounded-xl|border|card|shadow-sm)[^\"']*[\"']){4,}", re.IGNORECASE)

def get_aspect_ratio_spec(ratio_key: str = "16:9") -> Dict[str, Any]:
    """Ambil spesifikasi teknis dan CSS rumus dari rasio visual yang dipilih."""
    clean_key = ratio_key.strip()
    return ASPECT_RATIOS_REGISTRY.get(clean_key, ASPECT_RATIOS_REGISTRY["16:9"])

def list_all_aspect_ratios() -> Dict[str, Any]:
    """Kembalikan daftar lengkap 8 rasio visual baku UI/UX."""
    return {
        "status": "UPNORMAL_ASPECT_RATIOS_V1",
        "total_ratios": len(ASPECT_RATIOS_REGISTRY),
        "ratios": ASPECT_RATIOS_REGISTRY
    }

def get_card_fatigue_doctrine() -> Dict[str, Any]:
    """Kembalikan doktrin dekartunisasi & 5 alternatif borderless layouts."""
    return {
        "status": "CARD_FATIGUE_DOCTRINE_V1",
        "doctrine": CARD_FATIGUE_DOCTRINE
    }

def generate_aspect_ratio_css(
    ratio_key: str = "16:9",
    object_fit: str = "cover",
    enable_container_query: bool = True
) -> Dict[str, str]:
    """
    Hasilkan blok CSS modern bebas CLS (Cumulative Layout Shift = 0)
    dengan opsi Container Query responsif.
    """
    spec = get_aspect_ratio_spec(ratio_key)
    css_val = spec["css_value"]
    
    css_code = f""".up-media-frame {{
  aspect-ratio: {css_val};
  width: 100%;
  max-width: 100%;
  overflow: hidden;
  position: relative;
  background-color: rgba(15, 23, 42, 0.4);
}}

.up-media-frame > img,
.up-media-frame > video {{
  width: 100%;
  height: 100%;
  object-fit: {object_fit};
  display: block;
}}
"""
    if enable_container_query:
        css_code += """
/* Responsive Container Query: Auto-switch dari Card View ke Row Strip saat ruang menyempit */
@container (max-width: 540px) {
  .up-card-to-row {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
}
"""

    return {
        "ratio": ratio_key,
        "decimal": str(spec["decimal"]),
        "css": css_code
    }

def audit_card_fatigue(html_code: str) -> Dict[str, Any]:
    """
    Pindai kode antarmuka terhadap penyakit 'Card Fatigue' (box soup):
    1. Mendeteksi pengulangan kartu berlebih (> 4 kartu dengan border/rounded/shadow identik).
    2. Memberikan rekomendasi dekartunisasi (Hairline rule, Surface wash, atau Horizontal KPI Strip).
    """
    issues = []
    
    # Hitung jumlah tag kartu atau artikel
    card_divs = len(re.findall(r"\b(?:rounded-2xl|rounded-xl)\b[^>]*\b(?:border|p-6|shadow)\b", html_code))
    
    if card_divs >= 4:
        issues.append({
            "type": "CARD_FATIGUE_OVERLOAD",
            "severity": "HIGH",
            "detected_cards": card_divs,
            "description": f"Ditemukan {card_divs} kontainer kartu ber-border/rounded tebal dalam satu tampilan. Ini memicu 'Card Fatigue' dan pemborosan ruang layar.",
            "solution": "Ganti dengan 5 Alternatif Borderless: (1) Rule-based hairline separator, (2) Surface tint wash area, (3) Continuous data row, atau (4) In-line horizontal KPI strip."
        })
    
    is_clean = len(issues) == 0
    return {
        "status": "BORDERLESS_EXCELLENCE" if is_clean else "CARD_FATIGUE_DETECTED",
        "compliant": is_clean,
        "issues": issues,
        "recommendation": "Desain mengalir bebas tanpa kotak berlebih." if is_clean else "Lakukan dekartunisasi dengan menerapkan pola borderless Upnormal."
    }
