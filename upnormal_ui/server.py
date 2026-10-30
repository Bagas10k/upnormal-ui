#!/usr/bin/env python3
"""
upnormal_ui.server
~~~~~~~~~~~~~~~~~~
MCP Server: upnormal-ui (The Anti-AI-Slop UI/UX Engine)
Author: Bagas Cihuy (Bagas Saputra) & Hermes Agent
100% Bebas API Key & Tanpa Login. Solusi antarmuka upnormal berjiwa seni, bebas template generik.
"""

import os
import json
import asyncio
from typing import Optional
from mcp.server.mcpserver import MCPServer

from upnormal_ui.core.contrast import calculate_contrast_ratio, auto_correct_contrast
from upnormal_ui.core.anti_slop import scan_anti_slop
from upnormal_ui.core.palette import generate_upnormal_palette, STAGE_PALETTES, ACCENT_PRESETS
from upnormal_ui.core.morph import get_morph_script, get_morph_css
from upnormal_ui.transmute.transmute_engine import transmute_code
from upnormal_ui.archetypes.swiss_editorial import get_swiss_editorial_spec, render_swiss_hero
from upnormal_ui.archetypes.neo_brutalist import get_neo_brutalist_spec, render_neo_card
from upnormal_ui.archetypes.console_hud import get_console_hud_spec, render_hud_telemetry_panel
from upnormal_ui.archetypes.liquid_gooey import get_liquid_gooey_spec, render_liquid_filter_svg, render_liquid_button
from upnormal_ui.archetypes.spatial_glass import get_spatial_glass_spec, render_spatial_glass_card
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
def upnormal_scan_anti_slop(code: str) -> str:
    """
    Pindai kode HTML / Blade / CSS terhadap 8 Dosa AI UI Slop (gradien ungu-cyan murahan, tombol ber-emoji, bayangan difus kusam, teks abu-abu pudar, bento kaku, dsb).
    Mengembalikan skor kualitas (0-100) dan rekomendasi perbaikan Upnormal.
    """
    try:
        res = scan_anti_slop(code)
        return json.dumps(res, indent=2)
    except Exception as e:
        return json.dumps({"status": "ERROR", "message": str(e)})

@server.tool()
def upnormal_palette_generator(stage: str = "obsidian", accent: str = "#06b6d4") -> str:
    """
    Hasilkan palet warna rasio emas (95% Panggung Akromatik + 5% Aksen Berani).
    Pilihan panggung: 'obsidian', 'warm_paper', 'terminal_carbon', 'liquid_void'.
    Mengembalikan CSS Variables, konfigurasi Tailwind, dan verifikasi kontras WCAG AAA.
    """
    try:
        res = generate_upnormal_palette(stage_name=stage, accent_hex=accent)
        return json.dumps(res, indent=2)
    except Exception as e:
        return json.dumps({"status": "ERROR", "message": str(e)})

@server.tool()
def upnormal_transmute_ui(code: str, target_archetype: str = "neo_brutalist", accent_color: str = "#06b6d4") -> str:
    """
    [DUAL ENGINE - TRANSMUTE] Otomatis merombak kode UI template generik/slop menjadi karya seni Upnormal berkelas.
    Arketipe target: 'neo_brutalist', 'swiss_editorial', 'console_hud', 'spatial_glass'.
    """
    try:
        res = transmute_code(code, target_archetype=target_archetype, accent_color=accent_color)
        return json.dumps(res, indent=2)
    except Exception as e:
        return json.dumps({"status": "ERROR", "message": str(e)})

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
def upnormal_get_morph_engine(technique: str = "gsap_flip") -> str:
    """
    Ambil boilerplate kode JavaScript dan CSS untuk implementasi Motion Morphing 60 FPS In-Place (GSAP FLIP atau WAAPI).
    technique: 'gsap_flip' atau 'waapi_spring'.
    """
    js_code = get_morph_script(technique=technique)
    css_code = get_morph_css()
    return f"/* === JAVASCRIPT ENGINE ({technique.upper()}) === */\n{js_code}\n\n/* === CSS SPRING UTILITIES === */\n{css_code}"

if __name__ == "__main__":
    asyncio.run(server.run_stdio_async())
