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

def render_horizontal_metric_strip(metrics: Optional[List[Dict[str, Any]]] = None) -> str:
    """
    [DEKARTUNISASI: HORIZONTAL SPLIT STRIP]
    Pola borderless pengganti 4 kartu KPI terpisah.
    Menyusun metrik angka dalam satu baris datar dengan pembatas vertikal hairline (|).
    Menghemat hingga 60% ruang vertikal layar dibanding card konvensional.
    """
    default_metrics = [
        {"label": "TOTAL OMZET", "value": "Rp 148.500.000", "trend": "+18.2%", "positive": True},
        {"label": "TRANSAKSI AKTIF", "value": "1.248", "trend": "+6.4%", "positive": True},
        {"label": "MARGIN BERSIH", "value": "24.6%", "trend": "+1.8%", "positive": True},
        {"label": "PENDING INVOICE", "value": "12", "trend": "-3.1%", "positive": False}
    ]
    items = metrics if metrics is not None else default_metrics
    
    parts = []
    for idx, m in enumerate(items):
        t_color = "text-[#10b981]" if m.get("positive", True) else "text-[#ef4444]"
        t_icon = "↑" if m.get("positive", True) else "↓"
        border_right = "border-r border-white/10" if idx < len(items) - 1 else ""
        
        parts.append(f"""    <div class="flex-1 px-5 py-4 {border_right}">
      <div class="text-[11px] font-bold tracking-wider text-[#94a3b8] font-['JetBrains_Mono',monospace] mb-1">
        {m['label']}
      </div>
      <div class="text-2xl font-black text-[#f8fafc] font-['JetBrains_Mono',monospace] tabular-nums tracking-tight mb-1">
        {m['value']}
      </div>
      <div class="text-xs font-semibold {t_color} font-['JetBrains_Mono',monospace]">
        <span>{t_icon} {m['trend']}</span>
      </div>
    </div>""")

    body = "\n".join(parts)
    return f"""<!-- UPNORMAL BORDERLESS HORIZONTAL METRIC STRIP (ANTI-CARD FATIGUE) -->
<div class="w-full bg-[#0d1422] border-y border-[#1e293b] flex flex-col md:flex-row items-stretch justify-between font-['Plus_Jakarta_Sans',sans-serif]">
{body}
</div>"""

def render_continuous_data_rows(rows: Optional[List[Dict[str, Any]]] = None) -> str:
    """
    [DEKARTUNISASI: CONTINUOUS DATA SURFACE]
    Baris interaktif satu kanvas utuh (ala Linear / Stripe Dashboard).
    Menggantikan tumpukan kartu transaksi menjadi baris ber-hover halus tanpa border kotak tebal.
    """
    default_rows = [
        {"id": "TRX-8801", "name": "Distribusi Semen Curah 40T", "party": "PT Mandiri Beton", "amount": "Rp 42.000.000", "status": "SELESAI"},
        {"id": "TRX-8802", "name": "Baja Tulangan Ulir D16", "party": "CV Sumber Logam", "amount": "Rp 28.500.000", "status": "DIPROSES"},
        {"id": "TRX-8803", "name": "Bata Ringan AAC 12 Pallet", "party": "PT Graha Surya", "amount": "Rp 14.200.000", "status": "SELESAI"}
    ]
    items = rows if rows is not None else default_rows
    
    row_html = []
    for r in items:
        status_bg = "bg-[#10b981]/10 text-[#10b981] border-[#10b981]/30" if r["status"] == "SELESAI" else "bg-[#f59e0b]/10 text-[#f59e0b] border-[#f59e0b]/30"
        row_html.append(f"""  <!-- Row {r['id']} -->
  <div class="flex items-center justify-between py-3.5 px-4 hover:bg-white/[0.03] transition-colors border-b border-white/[0.06] cursor-pointer group">
    <div class="flex items-center gap-4">
      <span class="text-xs font-bold text-[#38bdf8] font-['JetBrains_Mono',monospace]">{r['id']}</span>
      <div>
        <div class="text-sm font-bold text-[#f8fafc] group-hover:text-[#38bdf8] transition-colors">{r['name']}</div>
        <div class="text-xs text-[#64748b]">{r['party']}</div>
      </div>
    </div>
    <div class="flex items-center gap-5">
      <span class="text-sm font-black text-[#f8fafc] font-['JetBrains_Mono',monospace] tabular-nums">{r['amount']}</span>
      <span class="text-[10px] font-bold font-['JetBrains_Mono',monospace] px-2.5 py-0.5 rounded border {status_bg}">{r['status']}</span>
    </div>
  </div>""")

    body = "\n".join(row_html)
    return f"""<!-- UPNORMAL CONTINUOUS DATA ROWS (ZERO-CARD SOUP) -->
<div class="w-full font-['Plus_Jakarta_Sans',sans-serif]">
{body}
</div>"""

