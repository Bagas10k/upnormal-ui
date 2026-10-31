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
from typing import Optional, List, Dict, Any

# Pastikan root package masuk ke sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mcp.server.mcpserver import MCPServer

from upnormal_ui.core.contrast import calculate_contrast_ratio, auto_correct_contrast
from upnormal_ui.core.color_scale import generate_11_step_scale
from upnormal_ui.core.spacing import get_spacing_system, audit_spacing_classes
from upnormal_ui.core.ast_linter import lint_dom_structure
from upnormal_ui.core.anti_slop import scan_anti_slop
from upnormal_ui.core.palette import generate_upnormal_palette
from upnormal_ui.core.morph import get_morph_script, get_morph_css
from upnormal_ui.transmute.ast_transmute import transmute_dom_tree
from upnormal_ui.archetypes.swiss_editorial import get_swiss_editorial_spec, render_swiss_hero
from upnormal_ui.archetypes.neo_brutalist import get_neo_brutalist_spec, render_neo_card
from upnormal_ui.archetypes.console_hud import get_console_hud_spec, render_hud_telemetry_panel
from upnormal_ui.archetypes.liquid_gooey import get_liquid_gooey_spec, render_liquid_filter_svg, render_liquid_button
from upnormal_ui.archetypes.spatial_glass import get_spatial_glass_spec, render_spatial_glass_card
from upnormal_ui.components.button import render_button
from upnormal_ui.components.card import render_bento_grid, render_metric_card
from upnormal_ui.components.dialog import render_morphing_dialog
from upnormal_ui.components.badge import render_badge
from upnormal_ui.components.dropdown import render_dropdown_menu
from upnormal_ui.components.navbar import render_navbar
from upnormal_ui.components.playground import generate_interactive_playground_html
from upnormal_ui.chassis.tables import render_high_density_table
from upnormal_ui.chassis.inputs import render_custom_select, render_tactile_toggle

server = MCPServer("upnormal-ui")

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
        return json.dumps({"status": "ERROR", "message": str(e)})

@server.tool()
def upnormal_audit_spacing(code: str) -> str:
    """
    [SPATIAL RHYTHM AUDIT] Pindai kode terhadap cacat penataan jarak & margin:
    1. Padding kaku besar di mobile (misal p-8 tanpa breakpoint sm:p-8) yang memakan lebar layar.
    2. Jarak arbitrer non-skala (misal p-[17px], m-[23px]).
    3. Magic vertical offset (misal pt-6 artifisial).
    """
    try:
        res = audit_spacing_classes(code)
        return json.dumps(res, indent=2)
    except Exception as e:
        return json.dumps({"status": "ERROR", "message": str(e)})

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
        return json.dumps({"status": "ERROR", "message": str(e)})

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
        return json.dumps({"status": "ERROR", "message": str(e)})

@server.tool()
def upnormal_scan_anti_slop(code: str) -> str:
    """
    [DOM-AWARE LINTER] Pindai kode HTML / Blade / CSS terhadap 9 Dosa AI UI Slop:
    1. Gradien ungu-cyan murahan
    2. Emoji dalam tombol / tautan
    3. Teks abu-abu redup (low contrast)
    4. Bayangan blur tebal kusam
    5. Gradien pelangi multi-warna
    6. Bento grid simetris monoton
    7. Kontrol native select tanpa kustomisasi
    8. Modal pop-up kaku tanpa kontinuitas
    9. Kicker badge clutter & floating tag pamer teknis
    """
    try:
        res = lint_dom_structure(code)
        return json.dumps(res, indent=2)
    except Exception as e:
        return json.dumps({"status": "ERROR", "message": str(e)})

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
        return json.dumps({"status": "ERROR", "message": str(e)})

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
        return json.dumps({"status": "ERROR", "message": str(e)})

@server.tool()
def upnormal_render_button(
    label: str = "TINDAKAN ➔",
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
    Framework: 'html', 'blade', atau 'react'.
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
        return f"Error rendering button: {str(e)}"

@server.tool()
def upnormal_render_bento_grid(cells_json: str, archetype: str = "obsidian") -> str:
    """
    [ASYMMETRIC BENTO FACTORY] Hasilkan komposisi Bento Grid 3-kolom asimetris berbobot 2:1.
    Input cells_json: array objek [{'title': '...', 'desc': '...', 'span': 'col-span-2' atau 'col-span-1', 'tag': '...', 'metric': '...'}]
    """
    try:
        data = json.loads(cells_json) if isinstance(cells_json, str) else cells_json
        return render_bento_grid(data, archetype=archetype)
    except Exception as e:
        return f"Error rendering bento grid: {str(e)}"

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
        return f"Error rendering dialog: {str(e)}"

@server.tool()
def upnormal_get_archetype(archetype_name: str, component_type: str = "hero") -> str:
    """
    Hasilkan sasis komponen siap pakai dari 5 Arketipe Desain Dunia:
    - 'swiss_editorial' (Swiss Editorial Brutalism)
    - 'neo_brutalist' (High-Contrast Neo-Brutalism)
    - 'console_hud' (Console-First Cyber HUD)
    - 'liquid_gooey' (Liquid Gooey & Jelly Morphing)
    - 'spatial_glass' (Tactile Spatial Frosted Glass)
    """
    arch = archetype_name.lower().strip()
    if arch == "swiss_editorial":
        return render_swiss_hero("ARSITEKTUR MANDIRI", "Membangun sistem antarmuka berjiwa seni tanpa belenggu template model.", "JELAJAHI SISTEM ➔")
    elif arch == "neo_brutalist":
        return render_neo_card("ARSITEKTUR TAKTIL", "Kontras tinggi dengan batas garis pekat 2.5px dan bayangan offset solid 4px.", tag="UPNORMAL", bg_accent="#facc15")
    elif arch == "console_hud":
        return render_hud_telemetry_panel("NODE_ALPHA_01", status="OPERATIONAL", latency="11.4ms", uptime="99.99%")
    elif arch == "liquid_gooey":
        return render_liquid_filter_svg() + "\n" + render_liquid_button("PELEBURAN CAIRAN ➔")
    elif arch == "spatial_glass":
        return render_spatial_glass_card("SPATIAL OPTICS 2.5D", "Kedalaman optik nyata dengan progressive blur dan kontras teks murni WCAG AAA.", "TINJAU ARSITEKTUR ➔")
    else:
        return f"Arketipe '{archetype_name}' tidak dikenal. Pilihan: 'swiss_editorial', 'neo_brutalist', 'console_hud', 'liquid_gooey', 'spatial_glass'."

@server.tool()
def upnormal_get_chassis(chassis_type: str) -> str:
    """
    Ambil sasis komponen siap tempel untuk kebutuhan web spesifik:
    - 'financial_table' / 'pos_table': Tabel data padat transaksi kasir/keuangan.
    - 'custom_select': Dropdown custom anti-native peramban.
    - 'tactile_toggle': Switch toggle taktil dengan animasi spring physics.
    """
    c = chassis_type.lower().strip()
    if c in ["financial_table", "pos_table", "table"]:
        return render_high_density_table("JURNAL TRANSAKSI KASIR PBJ")
    elif c in ["custom_select", "select"]:
        return render_custom_select("PILIH KATEGORI BARANG", ["Semen & Mortar", "Besi & Baja Tulangan", "Cat & Pelapis", "Batu & Agregat"])
    elif c in ["tactile_toggle", "toggle", "switch"]:
        return render_tactile_toggle("AKTIFKAN MODE AUTO-POSTING JURNAL", is_active=True)
    else:
        return f"Sasis '{chassis_type}' tidak ditemukan. Pilihan: 'financial_table', 'custom_select', 'tactile_toggle'."

@server.tool()
def upnormal_render_badge(status: str = "live", custom_label: Optional[str] = None) -> str:
    """
    [FUNCTIONAL STATUS BADGE] Hasilkan status badge fungsional dengan suar titik optik.
    Status: 'live' (hijau berdenyut), 'pending' (amber), 'closed' (abu-abu), 'alert' (merah berdenyut), 'info' (cyan).
    """
    try:
        return render_badge(status=status, custom_label=custom_label)
    except Exception as e:
        return f"Error rendering badge: {str(e)}"

@server.tool()
def upnormal_render_dropdown(items_json: Optional[str] = None) -> str:
    """
    [TACTILE ACTION DROPDOWN] Hasilkan popover menu aksi 3-titik dengan transisi spring dan listener penutup luar.
    """
    try:
        items = json.loads(items_json) if items_json else None
        return render_dropdown_menu(items=items)
    except Exception as e:
        return f"Error rendering dropdown: {str(e)}"

@server.tool()
def upnormal_render_navbar(brand_text: str = "bagas", brand_dot_color: str = "#E8590C") -> str:
    """
    [SITE HEADER & NAVIGATION] Hasilkan header navigasi situs berkelas dengan direct text-only typography,
    animasi denyut titik merek, dan backdrop blur sticky (bebas squircle AI logo).
    """
    try:
        return render_navbar(brand_text=brand_text, brand_dot_color=brand_dot_color)
    except Exception as e:
        return f"Error rendering navbar: {str(e)}"

@server.tool()
def upnormal_generate_playground_html() -> str:
    """
    Hasilkan seluruh dokumen HTML Interactive Component Playground mandiri yang dapat langsung
    disimpan dan dibuka di peramban untuk melihat & menguji seluruh komponen Upnormal secara visual.
    """
    try:
        return generate_interactive_playground_html()
    except Exception as e:
        return f"Error generating playground: {str(e)}"

if __name__ == "__main__":
    asyncio.run(server.run_stdio_async())
