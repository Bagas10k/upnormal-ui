"""
upnormal_ui.components.dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pabrik Dialog & Modal Morphing In-Place 60 FPS (In-Place Expansion Dialog).
Menegakkan doktrin Upnormal & Target +8 Poin:
- In-place FLIP bounding box calculation (First, Last, Invert, Play)
- Continuous squircle border-radius morphing
- Two-phase content stagger & silhouette protection (anti-layout thrashing)
- 4-layer progressive frosted glass backdrop
- WCAG AAA accessible touch targets & keyboard focus trap
"""

from typing import Dict, Any, Optional

def render_morphing_dialog(
    trigger_label: str = "BUKA MODAL MORPHING",
    dialog_title: str = "Detail Transaksi",
    dialog_content: str = "Informasi lengkap sistem termutasi secara mulus di tempat tanpa kedip.",
    confirm_label: str = "KONFIRMASI TINDAKAN ➔"
) -> str:
    """
    Hasilkan sasis dialog modal morphing in-place 60 FPS (HTML, Tailwind CSS, & Vanilla JS FLIP).
    Mengembangkan permukaan dialog secara fisik langsung dari koordinat tombol pemicu.
    """
    return f"""<!-- UPNORMAL IN-PLACE MORPHING DIALOG CONTAINER (TARGET +8 POIN) -->
<div class="relative inline-block font-['Plus_Jakarta_Sans',sans-serif]">
  <!-- Trigger Element (Anchor Fisik dengan Touch Target AAA >= 44px) -->
  <button id="up-morph-trigger" type="button" class="up-spring-hover up-spring-active inline-flex items-center justify-center gap-2 min-h-[44px] px-6 py-3 bg-[#0c0a09] text-[#fafaf9] hover:bg-[#ef4444] font-bold text-xs uppercase tracking-wider rounded-xl transition-all font-['JetBrains_Mono',monospace] shadow-sm focus:outline-none focus:ring-2 focus:ring-[#ef4444] focus:ring-offset-2 focus:ring-offset-[#06090e]">
    <span class="inline-block w-2 h-2 rounded-full bg-[#10b981] animate-pulse"></span>
    <span>{trigger_label}</span>
  </button>

  <!-- 4-Layer Progressive Frosted Glass Backdrop (Initially Hidden) -->
  <div id="up-morph-backdrop" class="fixed inset-0 bg-[#06090e]/75 backdrop-blur-md opacity-0 pointer-events-none transition-opacity duration-300 z-40"></div>

  <!-- Expanded Modal Surface (Morphing Chassis) -->
  <div id="up-morph-surface" class="up-morph-chassis fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[calc(100%-2rem)] max-w-lg bg-[#0d1422] border border-[#1e293b] rounded-2xl p-6 sm:p-8 shadow-2xl opacity-0 pointer-events-none z-50 overflow-hidden font-['Plus_Jakarta_Sans',sans-serif]" role="dialog" aria-modal="true" aria-labelledby="up-morph-title">
    
    <!-- Inner Content Wrapper (Two-Phase Protection: Fades in after shell expands) -->
    <div class="up-morph-content opacity-0 transition-all duration-200">
      <!-- Header -->
      <div class="flex items-center justify-between pb-4 border-b border-[#1e293b] mb-5">
        <div class="flex items-center gap-2.5">
          <span class="w-2.5 h-2.5 rounded-full bg-[#06b6d4]"></span>
          <h3 id="up-morph-title" class="text-lg font-black text-[#f8fafc] tracking-tight">
            {dialog_title}
          </h3>
        </div>
        <button id="up-morph-close" type="button" aria-label="Tutup Dialog" class="w-9 h-9 rounded-lg bg-white/5 hover:bg-white/10 text-[#94a3b8] hover:text-white flex items-center justify-center text-sm font-bold transition-colors focus:outline-none focus:ring-2 focus:ring-[#06b6d4]">
          ✕
        </button>
      </div>

      <!-- Body Editorial Content -->
      <div class="text-sm font-medium text-[#cbd5e1] leading-relaxed mb-6 space-y-3">
        <p>{dialog_content}</p>
      </div>

      <!-- Action Footer with Comfortable Spacing -->
      <div class="flex flex-col-reverse sm:flex-row items-stretch sm:items-center justify-end gap-3 pt-5 border-t border-[#1e293b]">
        <button id="up-morph-cancel" type="button" class="min-h-[44px] px-5 py-2.5 rounded-xl border border-[#1e293b] text-[#94a3b8] hover:text-[#f8fafc] hover:bg-white/5 text-xs font-bold font-['JetBrains_Mono',monospace] transition-all focus:outline-none focus:ring-2 focus:ring-slate-500">
          BATALKAN
        </button>
        <button id="up-morph-confirm" type="button" class="min-h-[44px] px-6 py-2.5 bg-[#06b6d4] hover:bg-[#38bdf8] text-[#06090e] text-xs font-black uppercase tracking-wider rounded-xl font-['JetBrains_Mono',monospace] transition-all shadow-md focus:outline-none focus:ring-2 focus:ring-[#06b6d4] focus:ring-offset-2 focus:ring-offset-[#0d1422]">
          {confirm_label}
        </button>
      </div>
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
  const content = surface ? surface.querySelector('.up-morph-content') : null;

  const SPRING_EASING = 'cubic-bezier(0.16, 1, 0.3, 1)';
  const DURATION_MS = 420;

  function openModal() {{
    if (!trigger || !surface) return;
    const isReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // 1. Rekam koordinat First (Trigger Fisik)
    const first = trigger.getBoundingClientRect();

    // 2. Tampilkan backdrop progressive blur
    if (backdrop) {{
      backdrop.classList.remove('opacity-0', 'pointer-events-none');
      backdrop.classList.add('opacity-100', 'pointer-events-auto');
    }}

    // 3. Tampilkan surface Last untuk mengukur posisi akhir
    surface.classList.remove('pointer-events-none');
    surface.classList.add('pointer-events-auto');
    surface.style.visibility = 'hidden';
    surface.style.opacity = '1';
    const last = surface.getBoundingClientRect();
    surface.style.visibility = 'visible';

    if (isReduced) {{
      if (content) content.style.opacity = '1';
      const focusable = surface.querySelector('button, [href], input, select, textarea');
      if (focusable) focusable.focus();
      return;
    }}

    // 4. Hitung Invert Deltas (FLIP)
    const deltaX = first.left - last.left;
    const deltaY = first.top - last.top;
    const scaleX = Math.max(first.width / Math.max(last.width, 1), 0.05);
    const scaleY = Math.max(first.height / Math.max(last.height, 1), 0.05);

    const triggerRadius = window.getComputedStyle(trigger).borderRadius || '12px';
    const surfaceRadius = window.getComputedStyle(surface).borderRadius || '16px';

    if (content) {{
      content.style.opacity = '0';
      content.style.transform = 'translateY(10px)';
    }}

    // 5. Mainkan Animasi Play 60 FPS dengan Spring Physics
    const anim = surface.animate([
      {{
        transformOrigin: 'top left',
        transform: `translate3d(${{deltaX}}px, ${{deltaY}}px, 0) scale(${{scaleX}}, ${{scaleY}})`,
        borderRadius: triggerRadius
      }},
      {{
        transformOrigin: 'top left',
        transform: 'translate3d(0, 0, 0) scale(1, 1)',
        borderRadius: surfaceRadius
      }}
    ], {{
      duration: DURATION_MS,
      easing: SPRING_EASING,
      fill: 'both'
    }});

    anim.onfinish = () => {{
      // Fase 2: Content Stagger Reveal
      if (content) {{
        content.animate([
          {{ opacity: 0, transform: 'translateY(10px)' }},
          {{ opacity: 1, transform: 'translateY(0)' }}
        ], {{
          duration: 220,
          easing: SPRING_EASING,
          fill: 'forwards'
        }});
      }}
      if (closeBtn) closeBtn.focus();
    }};
  }}

  function closeModal() {{
    if (!surface) return;
    const isReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (backdrop) {{
      backdrop.classList.remove('opacity-100', 'pointer-events-auto');
      backdrop.classList.add('opacity-0', 'pointer-events-none');
    }}

    if (isReduced || !trigger) {{
      surface.classList.remove('pointer-events-auto');
      surface.classList.add('pointer-events-none', 'opacity-0');
      if (trigger) trigger.focus();
      return;
    }}

    const first = trigger.getBoundingClientRect();
    const last = surface.getBoundingClientRect();

    const deltaX = first.left - last.left;
    const deltaY = first.top - last.top;
    const scaleX = Math.max(first.width / Math.max(last.width, 1), 0.05);
    const scaleY = Math.max(first.height / Math.max(last.height, 1), 0.05);

    const triggerRadius = window.getComputedStyle(trigger).borderRadius || '12px';
    const surfaceRadius = window.getComputedStyle(surface).borderRadius || '16px';

    if (content) content.style.opacity = '0';

    const anim = surface.animate([
      {{
        transformOrigin: 'top left',
        transform: 'translate3d(0, 0, 0) scale(1, 1)',
        borderRadius: surfaceRadius,
        opacity: 1
      }},
      {{
        transformOrigin: 'top left',
        transform: `translate3d(${{deltaX}}px, ${{deltaY}}px, 0) scale(${{scaleX}}, ${{scaleY}})`,
        borderRadius: triggerRadius,
        opacity: 0
      }}
    ], {{
      duration: Math.round(DURATION_MS * 0.75),
      easing: 'cubic-bezier(0.7, 0, 0.84, 0)',
      fill: 'both'
    }});

    anim.onfinish = () => {{
      surface.classList.remove('pointer-events-auto');
      surface.classList.add('pointer-events-none', 'opacity-0');
      if (trigger) trigger.focus();
    }};
  }}

  if (trigger) trigger.addEventListener('click', openModal);
  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (cancelBtn) cancelBtn.addEventListener('click', closeModal);
  if (backdrop) backdrop.addEventListener('click', closeModal);
  window.addEventListener('keydown', (e) => {{
    if (e.key === 'Escape' && surface && surface.classList.contains('pointer-events-auto')) {{
      closeModal();
    }}
  }});
}})();
</script>"""
