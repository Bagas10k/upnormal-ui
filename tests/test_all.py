"""
Unit Test Suite untuk upnormal-ui.
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from upnormal_ui.core.contrast import calculate_contrast_ratio, auto_correct_contrast
from upnormal_ui.core.anti_slop import scan_anti_slop
from upnormal_ui.core.palette import generate_upnormal_palette
from upnormal_ui.core.morph import get_morph_script, get_morph_css
from upnormal_ui.transmute.transmute_engine import transmute_code
from upnormal_ui.archetypes.swiss_editorial import render_swiss_hero
from upnormal_ui.archetypes.neo_brutalist import render_neo_card
from upnormal_ui.archetypes.console_hud import render_hud_telemetry_panel
from upnormal_ui.archetypes.liquid_gooey import render_liquid_button
from upnormal_ui.archetypes.spatial_glass import render_spatial_glass_card
from upnormal_ui.chassis.tables import render_high_density_table

class TestUpnormalUI(unittest.TestCase):

    def test_contrast_calculation(self):
        # Hitam di atas putih = 21.0:1
        cr = calculate_contrast_ratio("#000000", "#ffffff")
        self.assertAlmostEqual(cr, 21.0, delta=0.1)

        # Abu-abu pudar di atas background gelap (gagal AAA)
        cr_fail = calculate_contrast_ratio("#64748b", "#06090e")
        self.assertTrue(cr_fail < 7.0)

        # Auto-correction harus menaikkan rasio ke >= 7.0 (AAA)
        corrected = auto_correct_contrast("#64748b", "#06090e", target_ratio=7.0)
        self.assertTrue(corrected["achieved_ratio"] >= 7.0)
        self.assertEqual(corrected["grade"], "AAA")

    def test_anti_slop_scanner(self):
        slop_code = """
        <div class="bg-gradient-to-r from-purple-500 to-cyan-500 shadow-2xl">
          <button class="bg-gradient-to-r from-purple-600 to-cyan-600">
            KLIK DISINI 🚀✨
          </button>
          <p class="text-gray-400 bg-black">Teks pudar tidak terbaca</p>
        </div>
        """
        report = scan_anti_slop(slop_code)
        self.assertTrue(report["score"] < 70)
        self.assertEqual(report["status"], "SLOP_DETECTED")
        self.assertTrue(report["total_violations"] >= 2)

    def test_palette_generator(self):
        palette = generate_upnormal_palette("obsidian", accent_hex="#06b6d4")
        self.assertIn("contrast_verification", palette)
        self.assertIn("tokens", palette)
        self.assertEqual(palette["tokens"]["accent"], "#06b6d4")

    def test_transmute_engine(self):
        slop_code = """
        <button class="bg-gradient-to-r from-purple-500 to-cyan-500 shadow-2xl">
          DAPATKAN SEKARANG 🚀
        </button>
        """
        res = transmute_code(slop_code, target_archetype="neo_brutalist")
        self.assertEqual(res["status"], "SUCCESS")
        self.assertTrue(res["transmuted_score"] > res["initial_score"])
        self.assertNotIn("from-purple-500", res["transmuted_code"])
        self.assertNotIn("🚀", res["transmuted_code"])

    def test_archetypes_and_chassis_render(self):
        swiss = render_swiss_hero("JUDUL", "SUBTITLE")
        self.assertIn("Swiss Editorial Brutalism", swiss)

        neo = render_neo_card("KARTU", "DESKRIPSI")
        self.assertIn("Neo-Brutalist", neo)

        hud = render_hud_telemetry_panel("NODE-1")
        self.assertIn("Console HUD", hud)

        liquid = render_liquid_button("TOMBOL")
        self.assertIn("Two-Layer Silhouette", liquid)

        glass = render_spatial_glass_card("GLASS", "KONTEN")
        self.assertIn("Tactile Spatial Frosted Glass", glass)

        table = render_high_density_table()
        self.assertIn("High-Density Financial Data Table", table)

if __name__ == "__main__":
    unittest.main()
