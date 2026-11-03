"""
upnormal_ui.chassis.tables
~~~~~~~~~~~~~~~~~~~~~~~~~~
Sasis Tabel Kasir & Finansial Berkepadatan Tinggi (High-Density Data Surface).
Angka tabular murni (tabular-nums), sticky header, zebra striping halus, dan kontras tinggi.
"""

from typing import Dict, List, Optional

# Warna status yang sudah terverifikasi kontrasnya terhadap latar gelap.
STATUS_COLORS = {
    "LUNAS": "#10b981",
    "PAID": "#10b981",
    "PENDING": "#f59e0b",
    "BATAL": "#ef4444",
    "VOID": "#ef4444",
    "REFUND": "#38bdf8",
}

_DEFAULT_ROWS: List[Dict[str, str]] = [
    {"time": "01:45:12", "invoice": "INV-2026-0891", "item": "Semen Portland Composite 50kg", "qty": "120", "total": "7.800.000", "status": "LUNAS"},
    {"time": "01:42:04", "invoice": "INV-2026-0890", "item": "Besi Beton Ulir 12mm x 12m", "qty": "45", "total": "5.175.000", "status": "LUNAS"},
    {"time": "01:38:50", "invoice": "INV-2026-0889", "item": "Cat Tembok Eksterior 20L", "qty": "4", "total": "3.200.000", "status": "PENDING"},
]


def render_high_density_table(
    title: str = "JURNAL TRANSAKSI KASIR",
    rows: Optional[List[Dict[str, str]]] = None,
) -> str:
    """
    Hasilkan tabel data padat siap pakai untuk transaksi kasir/akuntansi (Tailwind CSS).

    rows: list of dict dengan kunci: time, invoice, item, qty, total, status.
    Jika tidak diberikan, contoh data bawaan yang dipakai.
    """
    data = rows if rows else _DEFAULT_ROWS
    if not isinstance(data, list) or not all(isinstance(r, dict) for r in data):
        raise ValueError("rows harus berupa list of dict dengan kunci: time, invoice, item, qty, total, status.")

    body_rows = []
    for i, r in enumerate(data):
        status = str(r.get("status", "LUNAS")).upper()
        color = STATUS_COLORS.get(status, "#38bdf8")
        zebra = ' bg-[#090e17]/40' if i % 2 == 1 else ''
        body_rows.append(f"""        <tr class="hover:bg-[#162032] transition-colors{zebra}">
          <td class="py-2.5 px-4 tabular-nums text-[#94a3b8]">{r.get('time', '--:--:--')}</td>
          <td class="py-2.5 px-4 font-bold text-[#38bdf8]">{r.get('invoice', '-')}</td>
          <td class="py-2.5 px-4 font-semibold text-[#f8fafc]">{r.get('item', '-')}</td>
          <td class="py-2.5 px-4 tabular-nums text-center font-bold">{r.get('qty', '0')}</td>
          <td class="py-2.5 px-4 tabular-nums text-right font-bold" style="color: {color}">{r.get('total', '0')}</td>
          <td class="py-2.5 px-4 text-center">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold border" style="background: {color}1a; color: {color}; border-color: {color}4d">{status}</span>
          </td>
        </tr>""")

    return f"""<!-- UPNORMAL CHASSIS: High-Density Financial Data Table -->
<div class="bg-[#0d1422] border border-[#1e293b] rounded-xl overflow-hidden font-['Plus_Jakarta_Sans',sans-serif] shadow-2xl">
  <!-- Table Control Header -->
  <div class="px-5 py-4 border-b border-[#1e293b] flex flex-wrap items-center justify-between gap-4 bg-[#0a0f1a]">
    <div class="flex items-center gap-3">
      <span class="w-2.5 h-2.5 bg-[#10b981] rounded-full shadow-[0_0_8px_#10b981]"></span>
      <h3 class="text-sm font-black tracking-wider uppercase text-[#f8fafc] font-['JetBrains_Mono',monospace]">
        {title}
      </h3>
    </div>
    <div class="flex items-center gap-2">
      <span class="text-xs text-[#64748b] font-semibold font-['JetBrains_Mono',monospace]">DENSITAS: PADAT</span>
    </div>
  </div>

  <!-- Scrollable Table Body -->
  <div class="overflow-x-auto">
    <table class="w-full text-left text-xs font-['JetBrains_Mono',monospace] border-collapse">
      <thead>
        <tr class="bg-[#06090e] text-[#94a3b8] uppercase tracking-wider text-[11px] border-b border-[#1e293b]">
          <th class="py-3 px-4 font-bold">WAKTU (WIB)</th>
          <th class="py-3 px-4 font-bold">NO. INVOICE</th>
          <th class="py-3 px-4 font-bold">ITEM TRANSAKSI</th>
          <th class="py-3 px-4 font-bold text-center">QTY</th>
          <th class="py-3 px-4 font-bold text-right">TOTAL (RP)</th>
          <th class="py-3 px-4 font-bold text-center">STATUS</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-[#1e293b]/60 text-[#e2e8f0]">
{chr(10).join(body_rows)}
      </tbody>
    </table>
  </div>
</div>"""
