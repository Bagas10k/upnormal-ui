"""
upnormal-ui: The Anti-AI-Slop UI/UX Engine & Design System.
Hak Cipta: Bagas Cihuy (Bagas Saputra) & Hermes Architecture.
"""

__version__ = "1.0.0"
__author__ = "Bagas Cihuy & Hermes Agent"

from upnormal_ui.core.contrast import calculate_contrast_ratio, auto_correct_contrast
from upnormal_ui.core.anti_slop import scan_anti_slop
from upnormal_ui.core.palette import generate_upnormal_palette
from upnormal_ui.core.morph import get_morph_script, get_morph_css
from upnormal_ui.transmute.transmute_engine import transmute_code
