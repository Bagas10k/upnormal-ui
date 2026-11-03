"""
upnormal_ui.archetypes.registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dispatch layer yang memetakan (arketipe, tipe komponen) ke renderer yang tepat.
Memisahkan logika pemilihan komponen dari server MCP agar dapat diuji
dan digunakan ulang tanpa dependensi protokol MCP.
"""

import json
from typing import Callable, Dict, Any

from upnormal_ui.archetypes.swiss_editorial import (
    get_swiss_editorial_spec,
    render_swiss_hero,
)
from upnormal_ui.archetypes.neo_brutalist import (
    get_neo_brutalist_spec,
    render_neo_card,
)
from upnormal_ui.archetypes.console_hud import (
    get_console_hud_spec,
    render_hud_telemetry_panel,
)
from upnormal_ui.archetypes.liquid_gooey import (
    get_liquid_gooey_spec,
    render_liquid_filter_svg,
    render_liquid_button,
)
from upnormal_ui.archetypes.spatial_glass import (
    get_spatial_glass_spec,
    render_spatial_glass_card,
)

# Setiap arketipe: satu spesifikasi token + komponen-komponen khasnya.
_ARCHETYPES: Dict[str, Dict[str, Any]] = {
    "swiss_editorial": {
        "label": "Swiss Editorial Brutalism",
        "spec": get_swiss_editorial_spec,
        "components": {
            "hero": lambda: render_swiss_hero(
                "ARSITEKTUR MANDIRI",
                "Membangun sistem antarmuka berjiwa seni tanpa belenggu template model.",
                "JELAJAHI SISTEM \u2794",
            ),
        },
    },
    "neo_brutalist": {
        "label": "High-Contrast Neo-Brutalism",
        "spec": get_neo_brutalist_spec,
        "components": {
            "card": lambda: render_neo_card(
                "ARSITEKTUR TAKTIL",
                "Kontras tinggi dengan batas garis pekat 2.5px dan bayangan offset solid 4px.",
                tag="UPNORMAL",
                bg_accent="#facc15",
            ),
        },
    },
    "console_hud": {
        "label": "Console-First Cyber HUD",
        "spec": get_console_hud_spec,
        "components": {
            "panel": lambda: render_hud_telemetry_panel(
                "NODE_ALPHA_01", status="OPERATIONAL", latency="11.4ms", uptime="99.99%"
            ),
            "telemetry": lambda: render_hud_telemetry_panel(
                "NODE_ALPHA_01", status="OPERATIONAL", latency="11.4ms", uptime="99.99%"
            ),
        },
    },
    "liquid_gooey": {
        "label": "Liquid Gooey & Jelly Morphing",
        "spec": get_liquid_gooey_spec,
        "components": {
            "filter": lambda: render_liquid_filter_svg(),
            "button": lambda: render_liquid_button("PELEBURAN CAIRAN \u2794"),
        },
    },
    "spatial_glass": {
        "label": "Tactile Spatial Frosted Glass",
        "spec": get_spatial_glass_spec,
        "components": {
            "card": lambda: render_spatial_glass_card(
                "SPATIAL OPTICS 2.5D",
                "Kedalaman optik nyata dengan progressive blur dan kontras teks murni WCAG AAA.",
                "TINJAU ARSITEKTUR \u2794",
            ),
        },
    },
}


def list_archetypes() -> Dict[str, Dict[str, Any]]:
    """Kembalikan metadata seluruh arketipe (label, tipe komponen yang tersedia)."""
    return {
        key: {
            "label": meta["label"],
            "component_types": sorted(["spec", *meta["components"].keys()]),
        }
        for key, meta in _ARCHETYPES.items()
    }


def render_archetype_component(archetype_name: str, component_type: str = "hero") -> str:
    """
    Render satu komponen dari arketipe tertentu.

    component_type:
    - 'spec'  : spesifikasi desain (token, tipografi, aturan) dalam JSON.
    - selain  : nama komponen khas arketipe (mis. 'hero', 'card', 'panel', 'button', 'filter').
    """
    key = archetype_name.lower().strip()
    meta = _ARCHETYPES.get(key)
    if meta is None:
        valid = ", ".join(sorted(_ARCHETYPES))
        raise ValueError(f"Arketipe '{archetype_name}' tidak dikenal. Pilihan: {valid}.")

    ctype = component_type.lower().strip() or "hero"

    if ctype == "spec":
        return json.dumps(meta["spec"](), indent=2)

    renderer: Dict[str, Callable[[], str]] = meta["components"]
    if ctype not in renderer:
        if len(renderer) == 1:
            # Aliasing ringan: 'hero' selalu diterima untuk komponen tunggal.
            only = next(iter(renderer))
            if ctype in ("hero", "component", "default"):
                return renderer[only]()
        valid = ", ".join(sorted(["spec", *renderer.keys()]))
        raise ValueError(
            f"Tipe komponen '{component_type}' tidak tersedia untuk arketipe '{key}'. "
            f"Pilihan: {valid}."
        )
    return renderer[ctype]()
