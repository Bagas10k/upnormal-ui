"""
upnormal_ui.components.playground
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Generator Halaman Visual Showcase & Interactive Playground Upnormal.
Menghasilkan dokumen HTML lengkap mandiri yang dapat dibuka langsung di peramban
untuk menguji rasa sentuh (*feel*), animasi morphing, dan kontras optik komponen secara nyata.
"""

from upnormal_ui.components.button import render_button
from upnormal_ui.components.card import render_bento_grid, render_metric_card
from upnormal_ui.components.dialog import render_morphing_dialog
from upnormal_ui.components.badge import render_badge
from upnormal_ui.components.dropdown import render_dropdown_menu
from upnormal_ui.components.navbar import render_navbar
from upnormal_ui.chassis.tables import render_high_density_table
from upnormal_ui.chassis.inputs import render_custom_select, render_tactile_toggle
from upnormal_ui.archetypes.swiss_editorial import render_swiss_hero
from upnormal_ui.archetypes.neo_brutalist import render_neo_card
from upnormal_ui.archetypes.console_hud import render_hud_telemetry_panel

def generate_interactive_playground_html() -> str:
    """Hasilkan halaman HTML interaktif mandiri untuk menguji seluruh komponen Upnormal."""
    
    # 1. Render buttons
    btn_neo = render_button("TOMBOL NEO-BRUTAL", variant="neo_brutal", size="md")
    btn_swiss = render_button("TOMBOL SWISS NOIR", variant="swiss_editorial", size="md")
    btn_obsidian = render_button("TOMBOL OBSIDIAN", variant="obsidian_sleek", size="md", is_accent=True)
    btn_glass = render_button("TOMBOL SPATIAL GLASS", variant="spatial_glass", size="md")
    btn_pill = render_button("TOMBOL SOFT PILL", variant="pill_soft", size="md", is_accent=True)

    # 2. Render cards & bento
    bento_sample = render_bento_grid([
        {"title": "Arsitektur Otonom", "desc": "Pemisahan sistematis dengan isolasi git worktree dan memori persisten.", "span": "col-span-2", "tag": "CORE ENGINE", "metric": "99.98%"},
        {"title": "Kontras AAA", "desc": "Rasio kontras luminansi relatif >= 7:1 diuji matematis.", "span": "col-span-1", "tag": "AKSESIBILITAS", "metric": "15.3:1"},
        {"title": "Two-Layer Silhouette", "desc": "Filter cairan di latar belakang, tipografi 100% tajam di lapisan atas.", "span": "col-span-1", "tag": "OPTICS"},
        {"title": "High-Density Table", "desc": "Format tabel finansial dan kasir dengan angka tabular monospace.", "span": "col-span-2", "tag": "DATA SURFACES"}
    ])

    # 3. Render dialog
    dialog_sample = render_morphing_dialog("UJI MODAL IN-PLACE MORPHING ➔", "Modal Transmutasi Fisik", "Modal ini mengembang secara fisik dari titik trigger tanpa jeda kedip atau layout shift mendadak.")

    # 4. Render Table
    table_sample = render_high_density_table("JURNAL TRANSAKSI KASIR BAHAN BANGUNAN")

    # 5. Render Inputs
    select_sample = render_custom_select("PILIH KATEGORI PRODUK", ["Semen & Mortar", "Besi Beton & Wiremesh", "Cat & Pelapis Tembok", "Pipa & Sanitari"])
    toggle_sample = render_tactile_toggle("AKTIFKAN VERIFIKASI DUAL-ENTRY AUTO-LOCK", is_active=True)

    # 6. Render Badges, Dropdown & Navbar
    badges_sample = f"""
    <div class="flex flex-wrap gap-3 items-center">
      {render_badge('live')}
      {render_badge('pending')}
      {render_badge('closed')}
      {render_badge('alert')}
      {render_badge('info')}
    </div>
    """
    dropdown_sample = render_dropdown_menu()
    navbar_sample = render_navbar(brand_text="upnormal", brand_dot_color="#38bdf8")

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Upnormal UI — Interactive Component Playground</title>
<!-- Tailwind Play CDN for Playground Demonstration Only -->
<script src="https://cdn.tailwindcss.com" crossorigin="anonymous"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
<style>
  body {{
    background-color: #06090e;
    color: #f8fafc;
    font-family: 'Plus Jakarta Sans', sans-serif;
  }}
  .glass-panel {{
    background: rgba(13, 20, 34, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.1);
  }}
</style>
</head>
<body class="bg-[#06090e] text-[#f8fafc]">

  <!-- Top Sticky Navbar Component -->
  {navbar_sample}

  <div class="px-4 sm:px-6 lg:px-8 py-8 sm:py-12 max-w-7xl mx-auto space-y-12 sm:space-y-16 lg:space-y-20">

  <!-- Header -->
  <header class="border-b border-[#1e293b] pb-8 flex flex-wrap items-center justify-between gap-4">
    <div>
      <h1 class="text-3xl font-black tracking-tight text-white flex items-center gap-3">
        <span>UPNORMAL UI PLAYGROUND</span>
        <span class="text-xs px-2.5 py-1 rounded bg-[#06b6d4]/10 text-[#06b6d4] border border-[#06b6d4]/30 font-['JetBrains_Mono',monospace]">v1.0.0</span>
      </h1>
      <p class="text-sm text-[#94a3b8] mt-1 font-medium">
        Katalog interaktif komponen antarmuka berjiwa seni, bebas AI slop, dan terverifikasi di runtime.
      </p>
    </div>
    <div class="flex items-center gap-3 font-['JetBrains_Mono',monospace] text-xs">
      <span class="w-2.5 h-2.5 rounded-full bg-[#10b981] shadow-[0_0_8px_#10b981]"></span>
      <span class="text-[#f8fafc] font-bold">ALL SYSTEMS LIVE</span>
    </div>
  </header>

  <!-- 1. Varian Tombol Modular -->
  <section class="space-y-4">
    <div class="border-b border-[#1e293b] pb-3 flex items-center justify-between">
      <h2 class="text-sm font-bold uppercase tracking-wider text-[#38bdf8] font-['JetBrains_Mono',monospace]">01 // MODULAR BUTTON SHOWCASE</h2>
      <span class="text-xs text-[#64748b]">5 Arketipe Visual</span>
    </div>
    <div class="p-5 sm:p-6 lg:p-8 rounded-2xl bg-[#090e17] border border-[#1e293b] flex flex-wrap gap-4 items-center">
      {btn_neo}
      {btn_swiss}
      {btn_obsidian}
      {btn_glass}
      {btn_pill}
    </div>
  </section>

  <!-- 2. Asymmetric Bento Grid -->
  <section class="space-y-4">
    <div class="border-b border-[#1e293b] pb-3 flex items-center justify-between">
      <h2 class="text-sm font-bold uppercase tracking-wider text-[#38bdf8] font-['JetBrains_Mono',monospace]">02 // ASYMMETRIC BENTO GRID</h2>
      <span class="text-xs text-[#64748b]">Hierarki 3-Kolom Berbobot 2:1</span>
    </div>
    {bento_sample}
  </section>

  <!-- 3. In-Place Morphing Dialog -->
  <section class="space-y-4">
    <div class="border-b border-[#1e293b] pb-3 flex items-center justify-between">
      <h2 class="text-sm font-bold uppercase tracking-wider text-[#38bdf8] font-['JetBrains_Mono',monospace]">03 // IN-PLACE MORPHING DIALOG</h2>
      <span class="text-xs text-[#64748b]">Fisika Spring 60 FPS (No-Blink SPA)</span>
    </div>
    <div class="p-5 sm:p-6 lg:p-8 rounded-2xl bg-[#090e17] border border-[#1e293b]">
      {dialog_sample}
    </div>
  </section>

  <!-- 4. High-Density Financial Data Table -->
  <section class="space-y-4">
    <div class="border-b border-[#1e293b] pb-3 flex items-center justify-between">
      <h2 class="text-sm font-bold uppercase tracking-wider text-[#38bdf8] font-['JetBrains_Mono',monospace]">04 // HIGH-DENSITY FINANCIAL DATA TABLE</h2>
      <span class="text-xs text-[#64748b]">Angka Tabular Monospace & Sticky Header</span>
    </div>
    {table_sample}
  </section>

  <!-- 5. Anti-Native Custom Controls -->
  <section class="space-y-4">
    <div class="border-b border-[#1e293b] pb-3 flex items-center justify-between">
      <h2 class="text-sm font-bold uppercase tracking-wider text-[#38bdf8] font-['JetBrains_Mono',monospace]">05 // ANTI-NATIVE CUSTOM CONTROLS</h2>
      <span class="text-xs text-[#64748b]">Custom Select & Spring Switch</span>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 p-5 sm:p-6 lg:p-8 rounded-2xl bg-[#090e17] border border-[#1e293b]">
      <div>
        {select_sample}
      </div>
      <div class="flex flex-col justify-end">
        <label class="block text-xs font-bold uppercase tracking-wider text-[#94a3b8] mb-2 font-['JetBrains_Mono',monospace]">
          STATUS VERIFIKASI
        </label>
        <div class="py-2">
          {toggle_sample}
        </div>
      </div>
    </div>
  </section>

  <!-- 6. Functional Status Badges & Action Dropdowns -->
  <section class="space-y-4">
    <div class="border-b border-[#1e293b] pb-3 flex items-center justify-between">
      <h2 class="text-sm font-bold uppercase tracking-wider text-[#38bdf8] font-['JetBrains_Mono',monospace]">06 // FUNCTIONAL STATUS BADGES & ACTION MENUS</h2>
      <span class="text-xs text-[#64748b]">Operational Beacons & Spring Dropdowns</span>
    </div>
    <div class="p-5 sm:p-6 lg:p-8 rounded-2xl bg-[#090e17] border border-[#1e293b] flex flex-wrap items-center justify-between gap-6">
      {badges_sample}
      <div class="flex items-center gap-3">
        <span class="text-xs text-[#94a3b8] font-semibold">Tindakan Cepat:</span>
        {dropdown_sample}
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="pt-8 border-t border-[#1e293b] text-center text-xs text-[#64748b] font-['JetBrains_Mono',monospace]">
    © 2026 BAGAS SAPUTRA (BAGAS CIHUY) • UPNORMAL UI ENGINE • BEBAS AI SLOP
  </footer>

  </div>
</body>
</html>
"""
