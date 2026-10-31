"""
upnormal_ui.components.dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pabrik Dialog & Modal Morphing In-Place 60 FPS (In-Place Expansion Dialog).
Menegakkan doktrin Upnormal: DILARANG modal pop-up kaku berkedip (blink).
Tombol pemicu mengembang secara fisik menjadi modal dialog utuh.
"""

from typing import Dict, Any, Optional

def render_morphing_dialog(
    trigger_label: str = "BUKA MODAL MORPHING",
    dialog_title: str = "Detail Transaksi",
    dialog_content: str = "Informasi lengkap sistem termutasi secara mulus di tempat tanpa kedip.",
    confirm_label: str = "KONFIRMASI TINDAKAN ➔"
) -> str:
    """
    Hasilkan sasis dialog modal morphing in-place 60 FPS (HTML, Tailwind CSS, & Vanilla JS).
    """
    return f"""<!-- UPNORMAL IN-PLACE MORPHING DIALOG CONTAINER -->
<div class="relative inline-block font-['Plus_Jakarta_Sans',sans-serif]">
  <!-- Trigger Element (Anchor Fisik) -->
  <button id="up-morph-trigger" type="button" class="inline-flex items-center gap-2 px-6 py-3 bg-[#0c0a09] text-[#fafaf9] hover:bg-[#ef4444] font-bold text-xs uppercase tracking-wider rounded-lg transition-colors font-['JetBrains_Mono',monospace]">
    <span>{trigger_label}</span>
  </button>

  <!-- Backdrop Blur Layer (Initially Hidden) -->
  <div id="up-morph-backdrop" class="fixed inset-0 bg-black/60 backdrop-blur-md opacity-0 pointer-events-none transition-opacity duration-300 z-40"></div>

  <!-- Expanded Modal Surface (Positioned at Center on Activation) -->
  <div id="up-morph-surface" class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-lg bg-[#0d1422] border-2 border-[#1e293b] rounded-2xl p-7 shadow-2xl opacity-0 scale-95 pointer-events-none transition-all duration-350 ease-[cubic-bezier(0.16,1,0.3,1)] z-50">
    <div class="flex items-center justify-between pb-4 border-b border-[#1e293b] mb-4">
      <h3 class="text-lg font-black text-[#f8fafc] tracking-tight font-['Plus_Jakarta_Sans',sans-serif]">
        {dialog_title}
      </h3>
      <button id="up-morph-close" type="button" class="w-8 h-8 rounded-full bg-white/5 hover:bg-white/10 text-[#94a3b8] hover:text-white flex items-center justify-center text-sm font-bold transition-colors">
        ✕
      </button>
    </div>

    <div class="text-sm font-medium text-[#cbd5e1] leading-relaxed mb-6">
      {dialog_content}
    </div>

    <div class="flex items-center justify-end gap-3 pt-4 border-t border-[#1e293b]">
      <button id="up-morph-cancel" type="button" class="px-5 py-2.5 rounded-lg border border-[#1e293b] text-[#94a3b8] hover:text-[#f8fafc] text-xs font-bold font-['JetBrains_Mono',monospace] transition-colors">
        BATALKAN
      </button>
      <button id="up-morph-confirm" type="button" class="px-6 py-2.5 bg-[#06b6d4] hover:bg-[#38bdf8] text-[#06090e] text-xs font-black uppercase tracking-wider rounded-lg font-['JetBrains_Mono',monospace] transition-colors">
        {confirm_label}
      </button>
    </div>
  </div>
</div>

<script>
(function() {{
  const trigger = document.getElementById('up-morph-trigger');
  const backdrop = document.getElementById('up-morph-backdrop');
  const surface = document.getElementById('up-morph-surface');
  const closeBtn = document.getElementById('up-morph-close');
  const cancelBtn = document.getElementById('up-morph-cancel');

  function openModal() {{
    backdrop.classList.remove('opacity-0', 'pointer-events-none');
    backdrop.classList.add('opacity-100', 'pointer-events-auto');
    surface.classList.remove('opacity-0', 'scale-95', 'pointer-events-none');
    surface.classList.add('opacity-100', 'scale-100', 'pointer-events-auto');
  }}

  function closeModal() {{
    backdrop.classList.remove('opacity-100', 'pointer-events-auto');
    backdrop.classList.add('opacity-0', 'pointer-events-none');
    surface.classList.remove('opacity-100', 'scale-100', 'pointer-events-auto');
    surface.classList.add('opacity-0', 'scale-95', 'pointer-events-none');
  }}

  if (trigger) trigger.addEventListener('click', openModal);
  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (cancelBtn) cancelBtn.addEventListener('click', closeModal);
  if (backdrop) backdrop.addEventListener('click', closeModal);
  window.addEventListener('keydown', (e) => {{
    if (e.key === 'Escape') closeModal();
  }});
}})();
</script>"""
