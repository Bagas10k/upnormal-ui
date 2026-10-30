"""
upnormal_ui.archetypes.neo_brutalist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arketipe Desain: High-Contrast Neo-Brutalism
Ciri Khas: Hard offset shadow (3px-5px hitam pekat), border 2.5px tebal, warna pop tajam, fisika klik taktil.
"""

from typing import Dict, Any

def get_neo_brutalist_spec() -> Dict[str, Any]:
    return {
        "id": "neo_brutalist",
        "name": "High-Contrast Neo-Brutalism",
        "vibe": "Taktil, percaya diri, berenergi tinggi, pop-culture retro-modern anti-halus.",
        "tokens": {
            "bg_base": "#f8fafc",
            "border": "#000000",
            "shadow": "4px 4px 0px #000000",
            "shadow_hover": "6px 6px 0px #000000",
            "shadow_active": "0px 0px 0px #000000",
            "accent_yellow": "#facc15",
            "accent_cyan": "#06b6d4",
            "accent_lime": "#84cc16"
        },
        "rules": [
            "Wajib memiliki garis batas tegas (border: 2px - 3px solid #000000).",
            "Bayangan wajib berupa Hard Offset Shadow (tanpa blur, 100% solid opacity).",
            "Fisika klik taktil: ketika ditekan (:active), elemen bergeser ke arah bayangan (translate-x-1 translate-y-1 shadow-none).",
            "Radius sudut kaku atau sedikit membulat terukur (rounded-lg atau rounded-none)."
        ]
    }

def render_neo_card(title: str, description: str, tag: str = "FEATURE", bg_accent: str = "#facc15") -> str:
    """Hasilkan komponen Kartu Taktil Neo-Brutalist (Tailwind CSS)."""
    return f"""<!-- UPNORMAL CHASSIS: Neo-Brutalist Tactile Card -->
<div class="bg-white border-[2.5px] border-black p-6 rounded-xl shadow-[4px_4px_0px_#000000] hover:shadow-[6px_6px_0px_#000000] hover:-translate-x-0.5 hover:-translate-y-0.5 active:translate-x-1 active:translate-y-1 active:shadow-none transition-all duration-150 font-['Plus_Jakarta_Sans',sans-serif]">
  <div class="flex items-center justify-between mb-4">
    <span class="inline-block px-2.5 py-1 text-xs font-black uppercase font-['JetBrains_Mono',monospace] border-2 border-black rounded shadow-[2px_2px_0px_#000000]" style="background-color: {bg_accent};">
      {tag}
    </span>
    <span class="text-xs font-bold text-slate-500 font-['JetBrains_Mono',monospace]">#001</span>
  </div>
  <h3 class="text-xl font-black text-black tracking-tight mb-2 uppercase">
    {title}
  </h3>
  <p class="text-sm font-semibold text-slate-700 leading-relaxed mb-6">
    {description}
  </p>
  <button class="w-full py-2.5 px-4 bg-black text-white hover:bg-slate-900 active:bg-black font-black text-xs uppercase tracking-wider border-2 border-black rounded transition-colors font-['JetBrains_Mono',monospace]">
    EKSEKUSI TINDAKAN ➔
  </button>
</div>"""
