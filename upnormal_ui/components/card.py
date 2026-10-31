"""
upnormal_ui.components.card
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pabrik Kartu & Sel Bento Asimetris Upnormal (Bento & Metric Cards).
Menghilangkan bento grid simetris kaku dan menggantinya dengan komposisi ruang
berbobot asimetris, garis batas hairline, dan indikator status aktif.
"""

from typing import Dict, Any, List, Optional

def render_bento_grid(cells_data: List[Dict[str, Any]], archetype: str = "obsidian") -> str:
    """
    Hasilkan komposisi Bento Grid Asimetris 60 FPS Upnormal.
    Setiap cell dapat memiliki rentang asimetris ('span': 'col-span-2' atau 'col-span-1').
    """
    cells_html = []
    for idx, c in enumerate(cells_data, 1):
        span = c.get("span", "col-span-1")
        title = c.get("title", f"Fitur {idx}")
        desc = c.get("desc", "Deskripsi komponen interaktif.")
        tag = c.get("tag", "AKTIF")
        metric = c.get("metric", None)

        metric_html = ""
        if metric:
            metric_html = f"""
            <div class="mt-4 pt-4 border-t border-white/10 flex items-baseline justify-between">
              <span class="text-xs text-[#94a3b8] font-['JetBrains_Mono',monospace]">NILAI AKHIR:</span>
              <span class="text-2xl font-black text-[#38bdf8] font-['JetBrains_Mono',monospace] tabular-nums">{metric}</span>
            </div>
            """

        cells_html.append(f"""
    <!-- Bento Cell {idx} ({span}) -->
    <article class="{span} bg-[#0d1422] border border-[#1e293b] rounded-2xl p-6 flex flex-col justify-between hover:border-[#38bdf8] hover:-translate-y-1 transition-all duration-300 shadow-sm relative overflow-hidden group">
      <div>
        <div class="flex items-center justify-between mb-3">
          <span class="text-[11px] font-bold font-['JetBrains_Mono',monospace] text-[#38bdf8] uppercase tracking-wider">
            {tag}
          </span>
          <span class="w-2 h-2 rounded-full bg-[#10b981] shadow-[0_0_8px_#10b981]"></span>
        </div>
        <h4 class="text-lg font-black text-[#f8fafc] tracking-tight mb-2">
          {title}
        </h4>
        <p class="text-sm font-medium text-[#94a3b8] leading-relaxed">
          {desc}
        </p>
      </div>
      {metric_html}
    </article>
        """)

    rendered_cells = "\n".join(cells_html)

    return f"""<!-- UPNORMAL ASYMMETRIC BENTO GRID (3-COL BALANCED HIERARCHY) -->
<section class="grid grid-cols-1 md:grid-cols-3 gap-5 font-['Plus_Jakarta_Sans',sans-serif]">
{rendered_cells}
</section>"""

def render_metric_card(title: str, value: str, trend: str = "+12.4%", is_positive: bool = True) -> str:
    """Hasilkan kartu metrik finansial/telemetri dengan angka tabular tajam."""
    trend_color = "text-[#10b981]" if is_positive else "text-[#ef4444]"
    trend_icon = "↑" if is_positive else "↓"

    return f"""<!-- UPNORMAL METRIC CARD -->
<div class="bg-[#0d1422] border border-[#1e293b] rounded-2xl p-6 font-['Plus_Jakarta_Sans',sans-serif] shadow-sm hover:border-[#38bdf8] transition-colors">
  <div class="flex items-center justify-between text-xs font-semibold text-[#94a3b8] mb-2 font-['JetBrains_Mono',monospace]">
    <span>{title}</span>
    <span class="px-2 py-0.5 rounded bg-white/5 border border-white/10 text-[10px]">LIVE</span>
  </div>
  <div class="text-3xl font-black text-[#f8fafc] font-['JetBrains_Mono',monospace] tabular-nums tracking-tight mb-2">
    {value}
  </div>
  <div class="flex items-center gap-1.5 text-xs font-bold font-['JetBrains_Mono',monospace] {trend_color}">
    <span>{trend_icon} {trend}</span>
    <span class="text-[#64748b] font-normal">vs bulan lalu</span>
  </div>
</div>"""
