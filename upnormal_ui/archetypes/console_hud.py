"""
upnormal_ui.archetypes.console_hud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arketipe Desain: Console-First Cyber HUD
Ciri Khas: Monospace tabular murni (JetBrains Mono), densitas data tinggi, status beacon berkedip, dashboard telemetri instrumen.
"""

from typing import Dict, Any

def get_console_hud_spec() -> Dict[str, Any]:
    return {
        "id": "console_hud",
        "name": "Console-First Cyber HUD",
        "vibe": "Instrumen telemetri, pusat kendali pesawat/server, glitch-free, fungsionalitas murni.",
        "tokens": {
            "bg_base": "#06090e",
            "bg_surface": "#0d1422",
            "border": "#1e293b",
            "text_primary": "#f8fafc",
            "text_muted": "#64748b",
            "beacon_online": "#10b981",
            "beacon_alert": "#ef4444",
            "accent_cyan": "#06b6d4"
        },
        "rules": [
            "Seluruh data angka dan tabel WAJIB menggunakan font monospace dengan angka tabular (tabular-nums).",
            "Indikator status menggunakan titik suar aktif (Status Beacon dengan efek glowing CSS ring).",
            "Garis batas panel ramping dan bersih (1px solid #1e293b).",
            "Densitas informasi tinggi: manfaatkan ruang secara efisien untuk kasir dan dashboard finansial."
        ]
    }

def render_hud_telemetry_panel(node_name: str, status: str = "ONLINE", latency: str = "12ms", uptime: str = "99.98%") -> str:
    """Hasilkan panel telemetri HUD Console (Tailwind CSS)."""
    return f"""<!-- UPNORMAL CHASSIS: Console HUD Instrument Panel -->
<div class="bg-[#0d1422] border border-[#1e293b] rounded-lg p-5 font-['JetBrains_Mono',monospace] text-xs text-[#94a3b8] shadow-2xl relative overflow-hidden">
  <!-- Top Instrument Bar -->
  <div class="flex items-center justify-between border-b border-[#1e293b] pb-3 mb-4">
    <div class="flex items-center gap-2.5">
      <span class="relative flex h-2.5 w-2.5">
        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#10b981] opacity-75"></span>
        <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-[#10b981]"></span>
      </span>
      <span class="font-bold text-[#f8fafc] tracking-wider uppercase">{node_name}</span>
    </div>
    <span class="px-2 py-0.5 rounded bg-[#10b981]/10 text-[#10b981] border border-[#10b981]/30 font-bold uppercase tracking-widest text-[10px]">
      {status}
    </span>
  </div>

  <!-- Telemetry Metrics Grid -->
  <div class="grid grid-cols-2 gap-4 mb-4">
    <div class="bg-[#06090e] p-3 rounded border border-[#1e293b]/60">
      <span class="block text-[10px] text-[#64748b] uppercase tracking-wider mb-1">LATENCY (P99)</span>
      <span class="text-base font-bold text-[#38bdf8] tabular-nums">{latency}</span>
    </div>
    <div class="bg-[#06090e] p-3 rounded border border-[#1e293b]/60">
      <span class="block text-[10px] text-[#64748b] uppercase tracking-wider mb-1">SERVICE UPTIME</span>
      <span class="text-base font-bold text-[#f8fafc] tabular-nums">{uptime}</span>
    </div>
  </div>

  <!-- Terminal Trace Line -->
  <div class="flex items-center justify-between text-[11px] text-[#64748b] pt-2 border-t border-[#1e293b]/60">
    <span>AUTH_MODE: STRICT_LOCAL</span>
    <span class="text-[#38bdf8] font-bold">READY</span>
  </div>
</div>"""
