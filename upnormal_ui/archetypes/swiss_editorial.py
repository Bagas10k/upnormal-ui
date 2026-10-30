"""
upnormal_ui.archetypes.swiss_editorial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arketipe Desain: Swiss Editorial Brutalism
Ciri Khas: Kanvas Warm Paper/Noir, tipografi raksasa terkondensasi, aksen kromatik tunggal, garis batas 1px tegas, zero-blur.
"""

from typing import Dict, Any

def get_swiss_editorial_spec() -> Dict[str, Any]:
    return {
        "id": "swiss_editorial",
        "name": "Swiss Editorial Brutalism",
        "vibe": "Intelektual, berani, editorial majalah avant-garde Eropa, tipografi ekstrem.",
        "tokens": {
            "bg_base": "#fafaf9",       # Warm Paper
            "bg_surface": "#ffffff",
            "border": "#0c0a09",        # Jet Black
            "text_primary": "#0c0a09",
            "text_muted": "#57534e",
            "accent": "#ef4444",        # Crimson Focal Accent
            "accent_contrast": "#ffffff"
        },
        "typography": {
            "font_display": "'Plus Jakarta Sans', sans-serif",
            "font_mono": "'JetBrains Mono', monospace",
            "headline_tracking": "-0.04em",
            "headline_weight": "900"
        },
        "rules": [
            "Panggung 95% monokromatik (Kertas Putih/Hitam) dengan 5% sentuhan merah/crimson.",
            "Hirarki tipografi masif: rasio ukuran judul terhadap teks body minimal 4:1.",
            "Garis pemisah struktural tegas (border 1px - 2px hitam pekat).",
            "Dilarang bayangan kabur (box-shadow blur = 0). Hard offset only jika dibutuhkan."
        ]
    }

def render_swiss_hero(title: str, subtitle: str, cta_text: str = "JELAJAHI SISTEM ➔") -> str:
    """Hasilkan komponen Hero Section bergaya Swiss Editorial Brutalism (Tailwind CSS)."""
    return f"""<!-- UPNORMAL CHASSIS: Swiss Editorial Brutalism Hero -->
<section class="relative bg-[#fafaf9] text-[#0c0a09] border-b-2 border-[#0c0a09] px-6 py-20 lg:py-28 font-['Plus_Jakarta_Sans',sans-serif] overflow-hidden">
  <div class="max-w-7xl mx-auto">
    <!-- Top Meta Strip -->
    <div class="flex flex-wrap items-center justify-between border-b border-[#0c0a09] pb-4 mb-12 text-xs font-['JetBrains_Mono',monospace] font-bold tracking-wider uppercase text-[#57534e]">
      <span class="flex items-center gap-2">
        <span class="w-2 h-2 bg-[#ef4444]"></span>
        EDISI DOKTRIN 2026 // KONTRAK VISUAL RESMI
      </span>
      <span>01 / 05 — MANIFESTO ARSITEKTUR</span>
    </div>

    <!-- Massive Asymmetrical Headline -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-end mb-16">
      <div class="lg:col-span-8">
        <h1 class="text-5xl sm:text-7xl lg:text-8xl font-black tracking-[-0.04em] leading-[0.92] text-[#0c0a09] uppercase">
          {title}
        </h1>
      </div>
      <div class="lg:col-span-4 border-l-2 border-[#0c0a09] pl-6 lg:pl-8">
        <p class="text-base sm:text-lg font-medium text-[#292524] leading-relaxed mb-6">
          {subtitle}
        </p>
        <a href="#action" class="inline-flex items-center justify-center px-6 py-3.5 bg-[#0c0a09] text-[#fafaf9] hover:bg-[#ef4444] transition-colors duration-200 text-xs font-bold font-['JetBrains_Mono',monospace] tracking-widest uppercase">
          {cta_text}
        </a>
      </div>
    </div>

    <!-- Numbered Metric Ticker -->
    <div class="grid grid-cols-1 sm:grid-cols-3 border-t-2 border-[#0c0a09] pt-6 gap-6 font-['JetBrains_Mono',monospace]">
      <div class="border-r border-[#0c0a09]/20 pr-4">
        <span class="text-xs text-[#57534e] block mb-1">01. RATIO</span>
        <span class="text-2xl font-black text-[#0c0a09]">95% : 5%</span>
      </div>
      <div class="border-r border-[#0c0a09]/20 pr-4">
        <span class="text-xs text-[#57534e] block mb-1">02. CONTRAST</span>
        <span class="text-2xl font-black text-[#ef4444]">WCAG AAA (≥7:1)</span>
      </div>
      <div>
        <span class="text-xs text-[#57534e] block mb-1">03. REFRESH RATE</span>
        <span class="text-2xl font-black text-[#0c0a09]">60 FPS CONTINUOUS</span>
      </div>
    </div>
  </div>
</section>"""
