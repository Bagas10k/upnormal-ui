"""
upnormal-ui: The Professional Anti-AI-Slop UI/UX Engine & Design System.
Hak Cipta: Bagas Cihuy (Bagas Saputra) & Hermes Architecture.
"""

__version__ = "1.0.0"
__author__ = "Bagas Cihuy & Hermes Agent"

from upnormal_ui.core.contrast import calculate_contrast_ratio, auto_correct_contrast
from upnormal_ui.core.color_scale import generate_11_step_scale
from upnormal_ui.core.spacing import get_spacing_system, audit_spacing_classes
from upnormal_ui.core.ast_linter import lint_dom_structure
from upnormal_ui.core.palette import generate_upnormal_palette
from upnormal_ui.core.morph import get_morph_script, get_morph_css
from upnormal_ui.transmute.ast_transmute import transmute_dom_tree
from upnormal_ui.components.button import render_button
from upnormal_ui.components.card import (
    render_bento_grid,
    render_metric_card,
    render_horizontal_metric_strip,
    render_continuous_data_rows
)
from upnormal_ui.core.aspect_ratio import (
    get_aspect_ratio_spec,
    list_all_aspect_ratios,
    get_card_fatigue_doctrine,
    audit_card_fatigue
)
from upnormal_ui.components.dialog import render_morphing_dialog
from upnormal_ui.components.badge import render_badge
from upnormal_ui.components.dropdown import render_dropdown_menu
from upnormal_ui.components.navbar import render_navbar
