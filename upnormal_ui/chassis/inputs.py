"""
upnormal_ui.chassis.inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~
Sasis Kontrol Kustom Anti-Native (Custom Inputs, Selects, & Toggles).
Melenyapkan elemen bawaan peramban yang kaku dan menggantinya dengan kontrol taktil presisi.
"""

def render_custom_select(label: str, options: list) -> str:
    """Hasilkan custom select dropdown anti-native (Tailwind CSS)."""
    options_html = "\n".join([f'      <option value="{opt.lower()}" class="bg-[#0d1422] text-[#f8fafc]">{opt}</option>' for opt in options])
    return f"""<!-- UPNORMAL CHASSIS: Anti-Native Custom Select -->
<div class="relative font-['Plus_Jakarta_Sans',sans-serif]">
  <label class="block text-xs font-bold uppercase tracking-wider text-[#94a3b8] mb-1.5 font-['JetBrains_Mono',monospace]">
    {label}
  </label>
  <div class="relative">
    <select class="w-full appearance-none bg-[#0d1422] border border-[#1e293b] text-[#f8fafc] py-2.5 px-4 pr-10 rounded-lg text-xs font-semibold focus:outline-none focus:border-[#06b6d4] focus:ring-1 focus:ring-[#06b6d4] transition-all cursor-pointer">
{options_html}
    </select>
    <!-- Custom SVG Chevron Indicator -->
    <div class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none text-[#94a3b8]">
      <svg width="16" height="16" style="width:16px;height:16px;" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </div>
  </div>
</div>"""

def render_tactile_toggle(label: str, is_active: bool = True) -> str:
    """Hasilkan switch toggle taktil dengan kurva spring."""
    active_bg = "bg-[#10b981]" if is_active else "bg-[#1e293b]"
    translate_knob = "translate-x-5" if is_active else "translate-x-0"
    return f"""<!-- UPNORMAL CHASSIS: Tactile Spring Toggle Switch -->
<label class="inline-flex items-center gap-3 cursor-pointer select-none font-['Plus_Jakarta_Sans',sans-serif]">
  <span class="text-xs font-bold text-[#f8fafc] tracking-wide">{label}</span>
  <div class="relative">
    <input type="checkbox" class="sr-only peer" {"checked" if is_active else ""}>
    <div class="w-11 h-6 {active_bg} rounded-full transition-colors duration-200 peer-focus:outline-none border border-white/10 peer-checked:bg-[#10b981]"></div>
    <div class="absolute left-1 top-1 bg-white w-4 h-4 rounded-full transition-transform duration-200 ease-out {translate_knob} peer-checked:translate-x-5 shadow-sm"></div>
  </div>
</label>"""
