"""
upnormal_ui.archetypes.liquid_gooey
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arketipe Desain: Liquid Gooey & Jelly Morphing
Ciri Khas: Peleburan cairan fluida organik (SVG feGaussianBlur + feColorMatrix) dengan arsitektur Dua-Lapisan (Two-Layer Silhouette) agar teks di layer atas tetap 100% tajam dan terbaca.
"""

from typing import Dict, Any

def get_liquid_gooey_spec() -> Dict[str, Any]:
    return {
        "id": "liquid_gooey",
        "name": "Liquid Gooey & Jelly Morphing",
        "vibe": "Organik, fluida hidup, elastisitas jelly, interaktif dan memikat mata.",
        "rules": [
            "DILARANG mengaplikasikan filter blur pada container yang memuat teks utama.",
            "Wajib memisahkan panggung menjadi 2 Lapisan (Two-Layer Silhouette Architecture): Lapisan latar belakang menerapkan filter SVG cairan, sedangkan lapisan teks berada di atas (z-index 10) dalam kondisi 100% tajam dan murni.",
            "Gunakan spring transition untuk interaksi hover dan click peleburan tetesan."
        ]
    }

def render_liquid_filter_svg() -> str:
    """Hasilkan SVG filter defs untuk efek fusi cairan fluida."""
    return """<!-- UPNORMAL SVG FLUID FUSION FILTER -->
<svg class="hidden" aria-hidden="true">
  <defs>
    <filter id="upnormal-gooey-filter">
      <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur" />
      <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -9" result="goo" />
      <feComposite in="SourceGraphic" in2="goo" operator="atop" />
    </filter>
  </defs>
</svg>"""

def render_liquid_button(label: str = "PELEBURAN CAIRAN ➔") -> str:
    """Hasilkan tombol cairan fluida dengan Dua Lapisan Siluet."""
    return f"""<!-- UPNORMAL CHASSIS: Two-Layer Silhouette Liquid Button -->
<div class="relative inline-block group">
  <!-- Layer 1: Fluid Fusion Canvas (Belakang) -->
  <div class="absolute inset-0 bg-[#06b6d4] rounded-full blur-md opacity-40 group-hover:opacity-80 group-hover:scale-110 transition-all duration-300 ease-out"></div>
  
  <!-- Layer 2: Pristine Crisp Interactive Layer (Depan - WCAG AAA Compliant) -->
  <button class="relative z-10 inline-flex items-center justify-center px-8 py-3.5 bg-[#090e17] text-[#38bdf8] border-2 border-[#06b6d4] rounded-full font-['Plus_Jakarta_Sans',sans-serif] font-extrabold text-xs uppercase tracking-widest shadow-lg hover:bg-[#06b6d4] hover:text-[#090e17] active:scale-95 transition-all duration-200">
    {label}
  </button>
</div>"""
