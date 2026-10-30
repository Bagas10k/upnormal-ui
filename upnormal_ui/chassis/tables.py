"""
upnormal_ui.chassis.tables
~~~~~~~~~~~~~~~~~~~~~~~~~~
Sasis Tabel Kasir & Finansial Berkepadatan Tinggi (High-Density Data Surface).
Angka tabular murni (tabular-nums), sticky header, zebra striping halus, dan kontras tinggi.
"""

def render_high_density_table(title: str = "JURNAL TRANSAKSI KASIR") -> str:
    """Hasilkan tabel data padat siap pakai untuk transaksi kasir/akuntansi (Tailwind CSS)."""
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
        <tr class="hover:bg-[#162032] transition-colors">
          <td class="py-2.5 px-4 tabular-nums text-[#94a3b8]">01:45:12</td>
          <td class="py-2.5 px-4 font-bold text-[#38bdf8]">INV-2026-0891</td>
          <td class="py-2.5 px-4 font-semibold text-[#f8fafc]">Semen Portland Composite 50kg</td>
          <td class="py-2.5 px-4 tabular-nums text-center font-bold">120</td>
          <td class="py-2.5 px-4 tabular-nums text-right font-bold text-[#10b981]">7.800.000</td>
          <td class="py-2.5 px-4 text-center">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#10b981]/10 text-[#10b981] border border-[#10b981]/30">LUNAS</span>
          </td>
        </tr>
        <tr class="hover:bg-[#162032] transition-colors bg-[#090e17]/40">
          <td class="py-2.5 px-4 tabular-nums text-[#94a3b8]">01:42:04</td>
          <td class="py-2.5 px-4 font-bold text-[#38bdf8]">INV-2026-0890</td>
          <td class="py-2.5 px-4 font-semibold text-[#f8fafc]">Besi Beton Ulir 12mm x 12m</td>
          <td class="py-2.5 px-4 tabular-nums text-center font-bold">45</td>
          <td class="py-2.5 px-4 tabular-nums text-right font-bold text-[#10b981]">5.175.000</td>
          <td class="py-2.5 px-4 text-center">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#10b981]/10 text-[#10b981] border border-[#10b981]/30">LUNAS</span>
          </td>
        </tr>
        <tr class="hover:bg-[#162032] transition-colors">
          <td class="py-2.5 px-4 tabular-nums text-[#94a3b8]">01:38:50</td>
          <td class="py-2.5 px-4 font-bold text-[#38bdf8]">INV-2026-0889</td>
          <td class="py-2.5 px-4 font-semibold text-[#f8fafc]">Cat Tembok Eksterior 20L</td>
          <td class="py-2.5 px-4 tabular-nums text-center font-bold">4</td>
          <td class="py-2.5 px-4 tabular-nums text-right font-bold text-[#f59e0b]">3.200.000</td>
          <td class="py-2.5 px-4 text-center">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#f59e0b]/10 text-[#f59e0b] border border-[#f59e0b]/30">PENDING</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>"""
