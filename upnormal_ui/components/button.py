"""
upnormal_ui.components.button
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pabrik Komponen Tombol Modular Upnormal (Button Component Factory).
Mendukung 5 Varian Arketipe, 3 Skala Ukuran, Status Taktil Spring,
dan Export Multi-Framework (HTML/Tailwind, Laravel Blade, React JSX).
"""

from typing import Dict, Any, Optional

VARIANTS = {
    "neo_brutal": {
        "name": "Neo-Brutalist Hard Offset",
        "classes": (
            "bg-black text-white font-black uppercase tracking-wider border-2 border-black rounded-lg "
            "shadow-[4px_4px_0px_#000000] hover:-translate-x-0.5 hover:-translate-y-0.5 "
            "active:translate-x-1 active:translate-y-1 active:shadow-none transition-all duration-150 "
            "font-['JetBrains_Mono',monospace]"
        ),
        "accent_bg": "bg-[#facc15] text-black border-2 border-black"
    },
    "swiss_editorial": {
        "name": "Swiss Editorial Noir",
        "classes": (
            "bg-[#0c0a09] text-[#fafaf9] hover:bg-[#ef4444] font-bold uppercase tracking-widest "
            "border border-[#0c0a09] rounded-none transition-colors duration-200 "
            "font-['JetBrains_Mono',monospace]"
        ),
        "accent_bg": "bg-[#ef4444] text-[#fafaf9] hover:bg-[#0c0a09]"
    },
    "obsidian_sleek": {
        "name": "Obsidian Sleek Hairline",
        "classes": (
            "bg-[#0d1422] text-[#f8fafc] border border-[#1e293b] hover:border-[#38bdf8] "
            "hover:text-[#38bdf8] rounded-xl font-bold tracking-wide active:scale-95 "
            "transition-all duration-200 shadow-sm"
        ),
        "accent_bg": "bg-[#06b6d4] text-[#06090e] border border-[#06b6d4] hover:bg-[#38bdf8]"
    },
    "spatial_glass": {
        "name": "Spatial Frosted Glass",
        "classes": (
            "backdrop-blur-xl bg-white/10 text-white border border-white/20 hover:border-white/40 "
            "hover:bg-white/15 rounded-2xl font-bold tracking-wide active:scale-95 "
            "transition-all duration-300 shadow-[0_8px_20px_rgba(0,0,0,0.3)]"
        ),
        "accent_bg": "bg-[#38bdf8]/20 text-[#38bdf8] border border-[#38bdf8]/40 hover:bg-[#38bdf8]/30"
    },
    "pill_soft": {
        "name": "Playful Soft Pill",
        "classes": (
            "bg-[#181715] text-white hover:bg-[#E8590C] rounded-full font-extrabold tracking-tight "
            "transition-transform duration-200 hover:-translate-y-0.5 active:translate-y-0.5 "
            "shadow-md hover:shadow-lg"
        ),
        "accent_bg": "bg-[#E8590C] text-white hover:bg-[#D9480F]"
    }
}

SIZES = {
    "sm": "py-2 px-3.5 text-xs",
    "md": "py-2.5 px-5 text-sm",
    "lg": "py-3.5 px-7 text-base"
}

def render_button(
    label: str = "TINDAKAN ➔",
    variant: str = "neo_brutal",
    size: str = "md",
    is_accent: bool = False,
    is_full_width: bool = False,
    framework: str = "html",
    icon_svg: Optional[str] = None
) -> str:
    """
    Hasilkan kode komponen tombol Upnormal siap pakai.
    framework: 'html' (Tailwind CSS), 'blade' (Laravel component), atau 'react' (JSX).
    """
    v_data = VARIANTS.get(variant, VARIANTS["neo_brutal"])
    base_class = v_data["accent_bg"] if is_accent else v_data["classes"]
    size_class = SIZES.get(size, SIZES["md"])
    width_class = "w-full justify-center" if is_full_width else "inline-flex"
    combined_class = f"{width_class} items-center gap-2.5 {size_class} {base_class}".strip()

    icon_markup = icon_svg if icon_svg else ""

    if framework == "blade":
        return f"""{{-- Blade Component: resources/views/components/upnormal-button.blade.php --}}
@props([
    'variant' => '{variant}',
    'size' => '{size}',
    'href' => null
])

@php
    $classes = '{combined_class}';
@endphp

@if($href)
    <a href="{{{{ $href }}}}" {{{{ $attributes->merge(['class' => $classes]) }}}}>
        {icon_markup}
        <span>{{{{ $slot->isEmpty() ? '{label}' : $slot }}}}</span>
    </a>
@else
    <button type="button" {{{{ $attributes->merge(['class' => $classes]) }}}}>
        {icon_markup}
        <span>{{{{ $slot->isEmpty() ? '{label}' : $slot }}}}</span>
    </button>
@endif"""

    elif framework == "react":
        react_snippet = (
            "// React Component: UpnormalButton.jsx\n"
            "import React from 'react';\n\n"
            f"export function UpnormalButton({{ children = '{label}', onClick, className = '', ...props }}) {{\n"
            "  return (\n"
            "    <button\n"
            "      onClick={onClick}\n"
            f"      className=\"{combined_class} \" + className\n"
            "      {...props}\n"
            "    >\n"
            f"      {icon_markup}\n"
            "      <span>{children}</span>\n"
            "    </button>\n"
            "  );\n"
            "}"
        )
        return react_snippet

    else: # HTML / Tailwind
        return f"""<!-- UPNORMAL BUTTON: {v_data['name']} ({size.upper()}) -->
<button type="button" class="{combined_class}">
  {icon_markup}
  <span>{label}</span>
</button>"""
