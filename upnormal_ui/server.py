#!/usr/bin/env python3
"""
upnormal_ui.server
~~~~~~~~~~~~~~~~~~
MCP Server: upnormal-ui (The Professional Anti-AI-Slop UI/UX Engine)
Author: Bagas Cihuy (Bagas Saputra) & Hermes Architecture
100% Bebas API Key & Tanpa Login. Mesin rekayasa antarmuka berjiwa seni, bebas template kaku.
"""

import os
import sys
import json
import asyncio
from typing import Optional

# Pastikan root package masuk ke sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mcp.server.mcpserver import MCPServer

from upnormal_ui.core.contrast import auto_correct_contrast
from upnormal_ui.core.color_scale import generate_11_step_scale
from upnormal_ui.core.spacing import (
    get_spacing_system,
    audit_spacing_classes,
    get_upnormal_creative_spacing_preset,
    generate_fluid_clamp,
    audit_negative_space_architecture,
    get_negative_space_doctrine
)
from upnormal_ui.core.ast_linter import lint_dom_structure
from upnormal_ui.core.anti_slop import scan_anti_slop
from upnormal_ui.core.palette import generate_upnormal_palette
from upnormal_ui.core.morph import (
    get_morph_script,
    get_morph_css,
    get_morph_engine_spec,
    get_spring_trajectory,
    SPRING_PHYSICS_PROFILES
)
from upnormal_ui.transmute.ast_transmute import transmute_dom_tree
from upnormal_ui.archetypes.registry import render_archetype_component, list_archetypes
from upnormal_ui.core.aspect_ratio import (
    get_aspect_ratio_spec,
    list_all_aspect_ratios,
    get_card_fatigue_doctrine,
    generate_aspect_ratio_css,
    audit_card_fatigue
)
from upnormal_ui.components.button import render_button
from upnormal_ui.components.card import (
    render_bento_grid,
    render_metric_card,
    render_horizontal_metric_strip,
    render_continuous_data_rows
)
from upnormal_ui.components.dialog import render_morphing_dialog
from upnormal_ui.components.badge import render_badge
from upnormal_ui.components.dropdown import render_dropdown_menu
from upnormal_ui.components.navbar import render_navbar
from upnormal_ui.components.playground import generate_interactive_playground_html
from upnormal_ui.chassis.tables import render_high_density_table
from upnormal_ui.chassis.inputs import render_custom_select, render_tactile_toggle

server = MCPServer("upnormal-ui")

_DEFAULT_SELECT_OPTIONS = ["Semen & Mortar", "Besi & Baja Tulangan", "Cat & Pelapis", "Batu & Agregat"]


def _error(message: str) -> str:
    """Format error seragam (JSON) untuk seluruh tool."""
    return json.dumps({"status": "ERROR", "message": message})


@server.tool()
def upnormal_audit_contrast(hex_fg: str, hex_bg: str, target_ratio: float = 7.0) -> str:
    """
    Hitung rasio kontras warna secara matematis (WCAG 2.2 AAA Strict).
    Jika gagal (< 7:1), otomatis melakukan perbaikan warna (auto-correction) pada Lightness HSL.
    """
    try:
        res = auto_correct_contrast(hex_fg, hex_bg, target_ratio=target_ratio)
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_audit_spacing(code: str) -> str:
    """
    [SPATIAL RHYTHM AUDIT] Pindai kode terhadap cacat penataan jarak & margin:
    1. Padding kaku besar di mobile (misal p-8 tanpa breakpoint sm:p-8) yang memakan lebar layar.
    2. Jarak arbitrer non-skala (misal p-[17px], m-[23px]).
    3. Magic vertical offset (misal pt-6 artifisial).
    4. Undersized button target (< 44px).
    """
    try:
        res = audit_spacing_classes(code)
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_audit_negative_space(code: str) -> str:
    """
    [ACTIVE NEGATIVE SPACE AUDIT & 'MA' INTERACTION]
    Pindai kode antarmuka terhadap kegunaan fungsional area kosong (Active Negative Space Architecture):
    1. CRAMPED_MACRO_SECTION: Seksi utama tercekik (py-2 s/d py-6) tanpa breathing room (minimal py-12 s/d py-24).
    2. ZERO_LATERAL_BREATHING: Hilangnya padding samping layar ponsel (px-0/px-1), konten menempel bezel.
    3. Memeriksa kepatuhan terhadap 7 Pilar Kegunaan Aktif Area Kosong Upnormal.
    """
    try:
        audit = audit_negative_space_architecture(code)
        doctrine = get_negative_space_doctrine()
        res = {
            "audit_result": audit,
            "doctrine_guide": doctrine
        }
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_get_spacing_system(density: str = "standard") -> str:
    """
    [SPATIAL SCALE SYSTEM] Ambil konfigurasi sistem penataan ruang 4-tingkat (Page, Section, Component, Micro)
    berbasis skala ritme 4px/8px modular. Pilihan density: 'compact', 'standard', 'comfortable'.
    """
    try:
        res = get_spacing_system(density=density)
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_generate_color_scale(accent_hex: str, name: str = "brand") -> str:
    """
    Hasilkan skala warna persepsi 11-langkah (50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950)
    lengkap dengan warna teks pendamping (hitam/putih) yang terverifikasi kontras WCAG AAA.
    Menghasilkan CSS variables dan konfigurasi Tailwind CSS.
    """
    try:
        res = generate_11_step_scale(accent_hex, name=name)
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_scan_anti_slop(code: str, mode: str = "dom") -> str:
    """
    [ANTI-SLOP LINTER] Pindai kode HTML / Blade / CSS terhadap 9 Dosa AI UI Slop:
    1. Gradien ungu-cyan murahan
    2. Emoji dalam tombol / tautan (panah CTA tipografis '\u2794' dikecualikan)
    3. Teks abu-abu redup (low contrast)
    4. Bayangan blur tebal kusam
    5. Gradien pelangi multi-warna
    6. Bento grid simetris monoton
    7. Kontrol native select tanpa kustomisasi
    8. Modal pop-up kaku tanpa kontinuitas
    9. Kicker badge clutter & floating tag pamer teknis

    mode:
    - 'dom'   : linter struktural berbasis BeautifulSoup (default; paling akurat).
    - 'regex' : pemindaian pola cepat berbasis regex (juga menangkap gradien teks
                pelangi & modal kaku yang lolos dari parse DOM).
    - 'all'   : gabungan keduanya, skor diambil dari yang terburuk (paling konservatif).
    """
    try:
        m = mode.lower().strip()
        if m == "dom":
            res = lint_dom_structure(code)
        elif m == "regex":
            res = scan_anti_slop(code)
        elif m == "all":
            dom_res = lint_dom_structure(code)
            rx_res = scan_anti_slop(code)
            seen = set()
            merged = []
            for v in dom_res["violations"] + rx_res["violations"]:
                if v["rule_id"] not in seen:
                    seen.add(v["rule_id"])
                    merged.append(v)
            score = min(dom_res["score"], rx_res["score"])
            res = {
                "status": "UPNORMAL_EXCELLENCE" if score >= 90 else ("SLOP_DETECTED" if score < 70 else "NEEDS_POLISH"),
                "score": score,
                "total_violations": len(merged),
                "violations": merged,
                "verdict": "Kode bersih dari AI slop." if score >= 90
                    else f"Terdeteksi {len(merged)} pelanggaran arsitektur antarmuka. Terapkan rekomendasi Upnormal.",
            }
        else:
            return _error(f"Mode '{mode}' tidak dikenal. Pilihan: 'dom', 'regex', 'all'.")
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_transmute_ui(code: str, target_archetype: str = "neo_brutalist", accent_color: str = "#06b6d4") -> str:
    """
    [DOM STRUCTURAL TRANSMUTATION] Otomatis merombak struktur DOM HTML/Blade yang terinfeksi template AI
    menjadi kode antarmuka Upnormal berstandar tinggi secara aman dan terstruktur (BeautifulSoup4).
    Target: 'neo_brutalist', 'swiss_editorial', 'console_hud', 'spatial_glass'.
    """
    try:
        res = transmute_dom_tree(code, target_archetype=target_archetype, accent_color=accent_color)
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_palette_generator(stage: str = "obsidian", accent: str = "#06b6d4") -> str:
    """
    Hasilkan palet warna rasio emas (95% Panggung Akromatik + 5% Aksen Berani).
    Pilihan panggung: 'obsidian', 'warm_paper', 'terminal_carbon', 'liquid_void'.
    """
    try:
        res = generate_upnormal_palette(stage_name=stage, accent_hex=accent)
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_render_button(
    label: str = "TINDAKAN \u2794",
    variant: str = "neo_brutal",
    size: str = "md",
    is_accent: bool = False,
    is_full_width: bool = False,
    framework: str = "html"
) -> str:
    """
    [MODULAR BUTTON FACTORY] Hasilkan komponen tombol Upnormal siap pakai.
    Varian:
    - 'neo_brutal': Hard offset shadow 4px, border 2.5px pekat, click translate taktil.
    - 'swiss_editorial': Warm paper/noir, border 1px tajam, uppercase tracking.
    - 'obsidian_sleek': Dark obsidian, hairline border, accent hover glow.
    - 'spatial_glass': Frosted glass, white/15 rim, progressive hover.
    - 'pill_soft': Rounded-full, playful soft spring.
    Framework: 'html', 'blade', 'react', 'vue', 'svelte', atau 'alpine'.
    """
    try:
        return render_button(
            label=label,
            variant=variant,
            size=size,
            is_accent=is_accent,
            is_full_width=is_full_width,
            framework=framework
        )
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_render_bento_grid(cells_json: str, archetype: str = "obsidian") -> str:
    """
    [ASYMMETRIC BENTO FACTORY] Hasilkan komposisi Bento Grid 3-kolom asimetris berbobot 2:1.
    Input cells_json: array objek [{'title': '...', 'desc': '...', 'span': 'col-span-2' atau 'col-span-1', 'tag': '...', 'metric': '...'}]
    Kunci 'title' wajib; 'desc', 'span', 'tag', 'metric' opsional.
    """
    try:
        data = json.loads(cells_json) if isinstance(cells_json, str) else cells_json
        if not isinstance(data, list) or not data:
            raise ValueError(
                'cells_json harus berupa array objek tidak kosong, contoh: '
                '[{"title": "Judul", "desc": "Deskripsi", "span": "col-span-2"}]'
            )
        if not all(isinstance(c, dict) for c in data):
            raise ValueError("Setiap elemen cells_json harus berupa objek dengan kunci 'title' (wajib).")
        missing = [i for i, c in enumerate(data) if not c.get("title")]
        if missing:
            raise ValueError(f"Elemen cells_json pada indeks {missing} tidak memiliki kunci 'title'.")
        return render_bento_grid(data, archetype=archetype)
    except json.JSONDecodeError as e:
        return _error(f"cells_json bukan JSON valid: {e}")
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_get_borderless_chassis(pattern: str = "metric_strip", items_json: Optional[str] = None) -> str:
    """
    [DEKARTUNISASI: BORDERLESS SURFACES]
    Hasilkan komponen antarmuka borderless elegan pengganti 'Card Fatigue' (box soup):
    - 'metric_strip': Horizontal split strip in-line KPI dengan pembatas hairline (|), hemat 60% vertikal.
    - 'continuous_rows': Baris interaktif satu kanvas utuh dengan hover state halus ala Linear/Stripe.
    """
    try:
        items = json.loads(items_json) if items_json else None
        p = pattern.lower().strip()
        if p in ["metric_strip", "kpi_strip", "strip"]:
            return render_horizontal_metric_strip(metrics=items)
        elif p in ["continuous_rows", "rows", "data_surface"]:
            return render_continuous_data_rows(rows=items)
        else:
            return _error(f"Pola borderless '{pattern}' tidak dikenal. Pilihan: 'metric_strip', 'continuous_rows'.")
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_get_aspect_ratio(ratio_key: str = "16:9", object_fit: str = "cover", enable_container_query: bool = True) -> str:
    """
    [ASPECT RATIO ARCHITECTURE & ZERO-CLS]
    Hasilkan aturan CSS dan spesifikasi dari 8 Rasio Visual Baku UI/UX:
    '1:1', '4:3', '3:2', '16:9', '21:9', '4:5', '9:16', '1.618:1'.
    Mencegah pergeseran tata letak (Cumulative Layout Shift = 0) saat aset gambar/video dimuat.
    """
    try:
        spec = get_aspect_ratio_spec(ratio_key)
        css_data = generate_aspect_ratio_css(
            ratio_key=ratio_key,
            object_fit=object_fit,
            enable_container_query=enable_container_query
        )
        res = {
            "specification": spec,
            "generated_css": css_data
        }
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_list_aspect_ratios() -> str:
    """
    Kembalikan daftar lengkap 8 rasio visual baku UI/UX beserta karakter dan penggunaan optimalnya.
    """
    try:
        return json.dumps(list_all_aspect_ratios(), indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_audit_card_fatigue(code: str) -> str:
    """
    [CARD FATIGUE LINTER & DEKARTUNISASI]
    Pindai kode terhadap penyakit 'Card Fatigue' (tumpukan kotak/kardus berlebihan):
    - Mendeteksi pengulangan kartu berlebih (> 4 kartu dengan border/rounded tebal).
    - Menghubungkan ke doktrin 5 Alternatif Borderless Layouts.
    """
    try:
        audit = audit_card_fatigue(code)
        doctrine = get_card_fatigue_doctrine()
        res = {
            "audit_result": audit,
            "doctrine": doctrine
        }
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_get_morph_dialog(
    trigger_label: str = "BUKA MODAL MORPHING",
    dialog_title: str = "Detail Transaksi",
    dialog_content: str = "Konten modal yang mengembang secara fisik tanpa jeda kedip."
) -> str:
    """
    [60 FPS MORPHING MODAL] Hasilkan komponen dialog modal yang mengembang dari titik tombol pemicu
    secara fisik dengan kurva spring (No-Blink SPA & CLS = 0).
    """
    try:
        return render_morphing_dialog(trigger_label=trigger_label, dialog_title=dialog_title, dialog_content=dialog_content)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_get_archetype(archetype_name: str, component_type: str = "hero") -> str:
    """
    Hasilkan komponen atau spesifikasi dari 5 Arketipe Desain Dunia:
    - 'swiss_editorial' (Swiss Editorial Brutalism)      -> component_type: 'spec' | 'hero'
    - 'neo_brutalist' (High-Contrast Neo-Brutalism)      -> component_type: 'spec' | 'card'
    - 'console_hud' (Console-First Cyber HUD)            -> component_type: 'spec' | 'panel'
    - 'liquid_gooey' (Liquid Gooey & Jelly Morphing)     -> component_type: 'spec' | 'filter' | 'button'
    - 'spatial_glass' (Tactile Spatial Frosted Glass)    -> component_type: 'spec' | 'card'

    component_type 'spec' mengembalikan token desain (JSON): warna, tipografi, dan aturan arketipe.
    Nilai 'hero' selalu diterima sebagai alias komponen khas arketipe mana pun.
    """
    try:
        return render_archetype_component(archetype_name, component_type)
    except ValueError as e:
        return _error(str(e))
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_get_chassis(
    chassis_type: str,
    title: str = "",
    items_json: Optional[str] = None,
    label: str = "",
    is_active: bool = True
) -> str:
    """
    Ambil sasis komponen siap tempel untuk kebutuhan web spesifik:
    - 'financial_table' / 'pos_table': Tabel data padat transaksi kasir/keuangan.
      Kustomisasi: 'title' (judul tabel) dan 'items_json' (array baris:
      [{"time": "...", "invoice": "...", "item": "...", "qty": "...", "total": "...", "status": "LUNAS|PENDING|BATAL|REFUND"}]).
    - 'custom_select': Dropdown custom anti-native peramban.
      Kustomisasi: 'label' dan 'items_json' (array string opsi).
    - 'tactile_toggle': Switch toggle taktil dengan animasi spring physics.
      Kustomisasi: 'label' dan 'is_active'.

    Semua parameter kustomisasi opsional; jika kosong, contoh data bawaan yang dipakai.
    """
    try:
        c = chassis_type.lower().strip()
        items = None
        if items_json:
            items = json.loads(items_json)
            if not isinstance(items, list) or not items:
                return _error("items_json harus berupa array tidak kosong.")

        if c in ["financial_table", "pos_table", "table"]:
            if items is not None and not all(isinstance(r, dict) for r in items):
                return _error("items_json untuk tabel harus berupa array of objects.")
            return render_high_density_table(title=title or "JURNAL TRANSAKSI KASIR", rows=items)
        elif c in ["custom_select", "select"]:
            return render_custom_select(label or "PILIH KATEGORI BARANG", items if items is not None else _DEFAULT_SELECT_OPTIONS)
        elif c in ["tactile_toggle", "toggle", "switch"]:
            return render_tactile_toggle(label or "AKTIFKAN MODE AUTO-POSTING JURNAL", is_active=is_active)
        else:
            return _error(
                f"Sasis '{chassis_type}' tidak ditemukan. "
                "Pilihan: 'financial_table', 'custom_select', 'tactile_toggle'."
            )
    except json.JSONDecodeError as e:
        return _error(f"items_json bukan JSON valid: {e}")
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_render_badge(status: str = "live", custom_label: Optional[str] = None) -> str:
    """
    [FUNCTIONAL STATUS BADGE] Hasilkan status badge fungsional dengan suar titik optik.
    Status: 'live' (hijau berdenyut), 'pending' (amber), 'closed' (abu-abu), 'alert' (merah berdenyut), 'info' (cyan).
    """
    try:
        return render_badge(status=status, custom_label=custom_label)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_render_dropdown(items_json: Optional[str] = None) -> str:
    """
    [TACTILE ACTION DROPDOWN] Hasilkan popover menu aksi 3-titik dengan transisi spring dan listener penutup luar.
    items_json opsional: array string label, misal ["Edit", "Duplikat", "Hapus"].
    """
    try:
        items = json.loads(items_json) if items_json else None
        return render_dropdown_menu(items=items)
    except json.JSONDecodeError as e:
        return _error(f"items_json bukan JSON valid: {e}")
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_render_navbar(brand_text: str = "bagas", brand_dot_color: str = "#E8590C") -> str:
    """
    [SITE HEADER & NAVIGATION] Hasilkan header navigasi situs berkelas dengan direct text-only typography,
    animasi denyut titik merek, dan backdrop blur sticky (bebas squircle AI logo).
    """
    try:
        return render_navbar(brand_text=brand_text, brand_dot_color=brand_dot_color)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_get_morph_assets() -> str:
    """
    [MORPHING ASSETS] Ambil potongan CSS dan JavaScript boilerplate In-Place Morphing
    (GSAP FLIP + Web Animations API, kurva spring cubic-bezier(0.16, 1, 0.3, 1))
    untuk dipakai ulang di proyek apa pun.
    """
    try:
        res = {
            "css": get_morph_css(),
            "javascript": get_morph_script(),
        }
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_get_morph_engine(technique: str = "all", profile: str = "tactile_smooth") -> str:
    """
    [UPNORMAL 60 FPS MORPH ENGINE (TARGET +8 POIN)]
    Hasilkan mesin animasi morphing in-place 60 FPS lengkap dengan solver fisika pegas teredam (Damped Harmonic Oscillator):
    - 8 Poin Peningkatan Arsitektur Animasi Upnormal
    - Profil fisika pegas: 'tactile_smooth' (Linear/Apple), 'playful_bounce' (Neo-Brutalist), 'viscous_liquid' (Liquid Gooey), 'critically_damped' (Console HUD).
    - Kode JavaScript (FLIP + squircle morph + two-phase reveal + reduced motion) siap pakai.
    - Kode CSS (progressive frosted glass + GPU layer promotion).
    """
    try:
        spec = get_morph_engine_spec()
        trajectory = get_spring_trajectory(profile_name=profile, samples=20)
        res = {
            "engine_spec": spec,
            "selected_profile": SPRING_PHYSICS_PROFILES.get(profile, SPRING_PHYSICS_PROFILES["tactile_smooth"]),
            "trajectory_preview": trajectory,
            "css": get_morph_css(),
            "javascript": get_morph_script(technique=technique),
        }
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_get_creative_spacing(min_px: int = 16, max_px: int = 48) -> str:
    """
    [UPNORMAL CREATIVE SPACING & FLUID CLAMP]
    Hasilkan token tata letak spasial kreatif berbasis rasio emas (Fibonacci/Golden), ritme asimetris editorial,
    serta formula CSS fluid clamp linier responsif tanpa jeda breakpoint yang kaku.
    """
    try:
        preset = get_upnormal_creative_spacing_preset()
        fluid_clamp = generate_fluid_clamp(min_px, max_px)
        res = {
            "preset": preset,
            "custom_fluid_clamp": {
                "input_min_px": min_px,
                "input_max_px": max_px,
                "css_clamp": fluid_clamp
            }
        }
        return json.dumps(res, indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_list_archetypes() -> str:
    """
    Daftar seluruh arketipe desain yang tersedia beserta tipe komponen yang valid
    untuk masing-masing (guna mengisi parameter 'archetype_name' dan 'component_type'
    pada tool upnormal_get_archetype).
    """
    try:
        return json.dumps(list_archetypes(), indent=2)
    except Exception as e:
        return _error(str(e))

@server.tool()
def upnormal_generate_playground_html() -> str:
    """
    Hasilkan seluruh dokumen HTML Interactive Component Playground mandiri yang dapat langsung
    disimpan dan dibuka di peramban untuk melihat & menguji seluruh komponen Upnormal secara visual.
    """
    try:
        return generate_interactive_playground_html()
    except Exception as e:
        return _error(str(e))

if __name__ == "__main__":
    asyncio.run(server.run_stdio_async())
