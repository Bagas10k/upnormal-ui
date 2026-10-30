"""
upnormal_ui.archetypes.spatial_glass
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arketipe Desain: Tactile Spatial & Progressive Frosted Glass
Ciri Khas: Efek kaca es berjenjang (Progressive Frosted Glass), kilau tepian optik (Optical Rim Border), kedalaman ruang taktil, teks kontras tinggi WCAG AAA.
"""

from typing import Dict, Any

def get_spatial_glass_spec() -> Dict[str, Any]:
    return {
        "id": "spatial_glass",
        "name": "Tactile Spatial & Progressive Frosted Glass",
        "vibe": "Kedalaman spasial visionOS, elegan, optik jernih, fisika mikro taktil.",
        "tokens": {
            "bg_backdrop": "rgba(13, 20, 34, 0.75)",
            "border_rim": "rgba(255, 255, 255, 0.12)",
            "border_highlight": "rgba(255, 255, 255, 0.25)",
            "text_primary": "#ffffff",
            "text_secondary": "#cbd5e1"
        },
        "rules": [
            "Gunakan backdrop-filter: blur(16px) hingga blur(24px) dengan latar belakang gelap transparan.",
            "Wajib memiliki garis batas tepian optik (border 1px solid rgba(255, 255, 255, 0.12)) untuk menegaskan tepi kaca.",
            "Teks di atas kaca es WAJIB berwarna putih solid (#ffffff) atau slate terang (#cbd5e1) dengan rasio kontras >= 7:1.",
            "Dilarang meletakkan teks tipis (font-weight 300) di atas kaca transparan."
        ]
    }

def render_spatial_glass_card(title: str, content: str, action_label: str = "TINJAU DETAIL ➔") -> str:
    """Hasilkan kartu Spatial Frosted Glass (Tailwind CSS)."""
    return f"""<!-- UPNORMAL CHASSIS: Tactile Spatial Frosted Glass Card -->
<div class="relative backdrop-blur-xl bg-[#0d1422]/80 border border-white/15 rounded-2xl p-7 shadow-[0_16px_36px_rgba(0,0,0,0.45)] hover:border-white/30 hover:-translate-y-1 transition-all duration-300 font-['Plus_Jakarta_Sans',sans-serif] overflow-hidden group">
  <!-- Subtle Internal Specular Glare -->
  <div class="absolute -top-24 -left-24 w-48 h-48 bg-white/5 rounded-full blur-2xl pointer-events-none group-hover:scale-150 transition-transform duration-500"></div>

  <div class="relative z-10">
    <div class="flex items-center justify-between mb-4">
      <span class="text-[11px] font-extrabold uppercase font-['JetBrains_Mono',monospace] tracking-wider text-[#38bdf8] px-2.5 py-1 rounded-md bg-[#38bdf8]/10 border border-[#38bdf8]/20">
        SPATIAL 2.5D
      </span>
      <span class="w-2 h-2 rounded-full bg-[#10b981] shadow-[0_0_8px_#10b981]"></span>
    </div>

    <h3 class="text-xl font-black text-white tracking-tight mb-2">
      {title}
    </h3>
    <p class="text-sm font-medium text-[#cbd5e1] leading-relaxed mb-6">
      {content}
    </p>

    <button class="inline-flex items-center gap-2 text-xs font-bold font-['JetBrains_Mono',monospace] tracking-wider text-white uppercase group-hover:text-[#38bdf8] transition-colors">
      <span>{action_label}</span>
    </button>
  </div>
</div>"""
