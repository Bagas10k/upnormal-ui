"""
upnormal_ui.components.navbar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pabrik Navigasi Situs & Header Merek Upnormal (Site Header & Navigation).
Menegakkan doktrin Upnormal: Direct text-only typography by default.
DILARANG logo kotak rounded bersiluet PC/gedung AI slop.
"""

from typing import List, Dict, Any, Optional

def render_navbar(
    brand_text: str = "bagas",
    brand_dot_color: str = "#E8590C",
    nav_links: Optional[List[Dict[str, str]]] = None,
    cta_label: str = "Hubungi Saya",
    cta_href: str = "#contact"
) -> str:
    """Hasilkan header navigasi situs berkelas dengan direct text typography dan sticky blur."""
    if not nav_links:
        nav_links = [
            {"label": "Karya Pilihan", "href": "#projects"},
            {"label": "Keahlian", "href": "#pillars"},
            {"label": "Cara Kerja", "href": "#process"},
        ]

    links_html = "\n".join([f'      <a href="{l["href"]}" class="text-sm font-bold text-[#94a3b8] hover:text-[#f8fafc] transition-colors">{l["label"]}</a>' for l in nav_links])

    return f"""<!-- UPNORMAL SITE HEADER & NAVIGATION -->
<header class="sticky top-0 z-50 backdrop-blur-xl bg-[#06090e]/85 border-b border-[#1e293b] font-['Plus_Jakarta_Sans',sans-serif]">
  <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
    <!-- Direct Text-Only Branding -->
    <a href="#home" class="flex items-center gap-2 text-xl font-black tracking-tight text-[#f8fafc] no-underline">
      <span>{brand_text}</span>
      <span class="w-2.5 h-2.5 rounded-full inline-block animate-pulse" style="background-color: {brand_dot_color};"></span>
    </a>

    <!-- Desktop Navigation Links -->
    <nav class="hidden md:flex items-center gap-8" aria-label="Navigasi Utama">
{links_html}
    </nav>

    <!-- Header Action Button -->
    <div class="flex items-center gap-4">
      <a href="{cta_href}" class="inline-flex items-center gap-2 px-5 py-2.5 bg-[#f8fafc] text-[#06090e] hover:bg-[#38bdf8] font-black text-xs uppercase tracking-wider rounded-full transition-all shadow-sm">
        <span>{cta_label}</span>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
    </div>
  </div>
</header>"""
