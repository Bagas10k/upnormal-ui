"""
upnormal_ui.components.dropdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Menu Dropdown & Popover Aksi Taktil Upnormal (Tactile Action Dropdown).
Mendukung 3-dots trigger button, transisi opacity/scale 60 FPS, dan listener penutup luar.
"""

from typing import List, Dict, Any, Optional

def render_dropdown_menu(
    trigger_icon: str = "dots",
    items: Optional[List[Dict[str, str]]] = None
) -> str:
    """Hasilkan menu aksi popover taktil dengan transisi spring."""
    if not items:
        items = [
            {"label": "Lihat Detail", "action": "view"},
            {"label": "Cetak Dokumen", "action": "print"},
            {"label": "Salin URL", "action": "copy"},
            {"label": "Hapus Item", "action": "delete", "is_danger": "true"}
        ]

    items_html = []
    for item in items:
        danger_class = "text-[#ef4444] hover:bg-[#ef4444]/10" if item.get("is_danger") == "true" else "text-[#f8fafc] hover:bg-white/5"
        items_html.append(f"""
      <button type="button" class="w-full text-left px-3.5 py-2 text-xs font-semibold rounded-md transition-colors {danger_class} flex items-center justify-between">
        <span>{item['label']}</span>
      </button>""")

    rendered_items = "\n".join(items_html)

    return f"""<!-- UPNORMAL TACTILE ACTION DROPDOWN -->
<div class="relative inline-block text-left font-['Plus_Jakarta_Sans',sans-serif]" data-up-dropdown>
  <button type="button" class="w-8 h-8 rounded-lg bg-[#0d1422] border border-[#1e293b] text-[#94a3b8] hover:text-[#f8fafc] hover:border-[#38bdf8] flex items-center justify-center transition-colors shadow-sm focus:outline-none" data-up-dropdown-trigger aria-haspopup="true">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/></svg>
  </button>

  <div class="hidden absolute right-0 mt-2 w-48 rounded-xl bg-[#0d1422] border border-[#1e293b] p-1.5 shadow-2xl z-30 transition-all duration-200" data-up-dropdown-menu>
    <div class="space-y-0.5">
{rendered_items}
    </div>
  </div>
</div>

<script>
(function() {{
  document.querySelectorAll('[data-up-dropdown]').forEach(container => {{
    const trigger = container.querySelector('[data-up-dropdown-trigger]');
    const menu = container.querySelector('[data-up-dropdown-menu]');
    if (!trigger || !menu) return;

    trigger.addEventListener('click', (e) => {{
      e.stopPropagation();
      const isHidden = menu.classList.contains('hidden');
      document.querySelectorAll('[data-up-dropdown-menu]').forEach(m => m.classList.add('hidden'));
      if (isHidden) menu.classList.remove('hidden');
    }});

    document.addEventListener('click', () => menu.classList.add('hidden'));
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') menu.classList.add('hidden');
    }});
  }});
}})();
</script>"""
