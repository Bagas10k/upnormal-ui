"""
upnormal_ui.components.badge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Komponen Badge Status Fungsional Upnormal (Functional Status Badges).
Menegakkan doktrin Upnormal: DILARANG badge pamer teknis (seperti 'Zero AI-Slop', 'WCAG AAA').
HANYA untuk status operasional fungsional: Live, Pending, Sukses, Gangguan, Draft.
"""

from typing import Dict, Any, Optional

STATUS_VARIANTS = {
    "live": {
        "label": "LIVE",
        "dot_color": "#10b981",
        "classes": "bg-[#10b981]/10 text-[#10b981] border border-[#10b981]/30",
        "has_ping": True
    },
    "pending": {
        "label": "PENDING",
        "dot_color": "#f59e0b",
        "classes": "bg-[#f59e0b]/10 text-[#f59e0b] border border-[#f59e0b]/30",
        "has_ping": False
    },
    "closed": {
        "label": "SELESAI",
        "dot_color": "#94a3b8",
        "classes": "bg-white/5 text-[#94a3b8] border border-white/10",
        "has_ping": False
    },
    "alert": {
        "label": "GANGGUAN",
        "dot_color": "#ef4444",
        "classes": "bg-[#ef4444]/10 text-[#ef4444] border border-[#ef4444]/30",
        "has_ping": True
    },
    "info": {
        "label": "INFO",
        "dot_color": "#06b6d4",
        "classes": "bg-[#06b6d4]/10 text-[#06b6d4] border border-[#06b6d4]/30",
        "has_ping": False
    }
}

def render_badge(status: str = "live", custom_label: Optional[str] = None) -> str:
    """Hasilkan badge status operasional fungsional dengan suar titik optik."""
    s = status.lower().strip()
    data = STATUS_VARIANTS.get(s, STATUS_VARIANTS["live"])
    label = custom_label if custom_label else data["label"]

    ping_html = ""
    if data["has_ping"]:
        ping_html = f"""<span class="animate-ping absolute inline-flex h-full w-full rounded-full opacity-75" style="background-color: {data['dot_color']};"></span>"""

    return f"""<!-- UPNORMAL FUNCTIONAL STATUS BADGE -->
<span class="inline-flex items-center gap-2 px-2.5 py-1 rounded-md text-[11px] font-bold font-['JetBrains_Mono',monospace] tracking-wider uppercase {data['classes']}">
  <span class="relative flex h-2 w-2">
    {ping_html}
    <span class="relative inline-flex rounded-full h-2 w-2" style="background-color: {data['dot_color']};"></span>
  </span>
  <span>{label}</span>
</span>"""
