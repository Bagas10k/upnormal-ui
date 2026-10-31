"""
Unit Test Suite Komprehensif v1.0.0 untuk upnormal-ui.
Menguji seluruh invarian matematis, linter DOM struktural, pabrik komponen modular, dan generator playground.
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from upnormal_ui.core.contrast import calculate_contrast_ratio, auto_correct_contrast
from upnormal_ui.core.color_scale import generate_11_step_scale
from upnormal_ui.core.spacing import get_spacing_system, audit_spacing_classes
from upnormal_ui.core.ast_linter import lint_dom_structure
from upnormal_ui.core.palette import generate_upnormal_palette
from upnormal_ui.transmute.ast_transmute import transmute_dom_tree
from upnormal_ui.components.button import render_button
from upnormal_ui.components.card import render_bento_grid, render_metric_card
from upnormal_ui.components.dialog import render_morphing_dialog
from upnormal_ui.components.badge import render_badge
from upnormal_ui.components.dropdown import render_dropdown_menu
from upnormal_ui.components.navbar import render_navbar
from upnormal_ui.components.playground import generate_interactive_playground_html
from upnormal_ui.archetypes.swiss_editorial import render_swiss_hero
from upnormal_ui.archetypes.neo_brutalist import render_neo_card
from upnormal_ui.archetypes.console_hud import render_hud_telemetry_panel
from upnormal_ui.chassis.tables import render_high_density_table

class TestUpnormalUIEnterprise(unittest.TestCase):

    def test_contrast_and_11_step_color_scale(self):
        # 1. Contrast ratio verification
        cr = calculate_contrast_ratio("#000000", "#ffffff")
        self.assertAlmostEqual(cr, 21.0, delta=0.1)

        # 2. 11-Step Perceptual Scale Generator
        scale = generate_11_step_scale("#06b6d4", name="cyan")
        self.assertEqual(len(scale["steps"]), 11)
        self.assertIn("50", scale["steps"])
        self.assertIn("500", scale["steps"])
        self.assertIn("950", scale["steps"])
        
        # Tiap step wajib memiliki foreground teks yang terverifikasi kontras tinggi (>= 4.5:1)
        for step_name, data in scale["steps"].items():
            self.assertTrue(data["contrast_ratio"] >= 4.5, f"Step {step_name} gagal kontras minimum AA!")

    def test_ast_dom_linter(self):
        slop_html = """
        <form action="/submit">
          <div class="hero-pill"><span>INDONESIA // VOL. 02</span></div>
          <button class="bg-gradient-to-r from-purple-500 to-cyan-500 shadow-2xl">
            KLIK DISINI 🚀✨
          </button>
          <select><option>Pilih</option></select>
        </form>
        """
        report = lint_dom_structure(slop_html)
        self.assertTrue(report["score"] < 70)
        self.assertEqual(report["status"], "SLOP_DETECTED")
        
        rule_ids = [v["rule_id"] for v in report["violations"]]
        self.assertIn("DOM_01_FORM_MISSING_NOVALIDATE", rule_ids)
        self.assertIn("DOM_02_UNSTYLED_NATIVE_SELECT", rule_ids)
        self.assertIn("DOM_03_EMOJI_IN_INTERACTIVE_UI", rule_ids)
        self.assertIn("DOM_04_PURPLE_CYAN_SLOP_GRADIENT", rule_ids)
        self.assertIn("DOM_05_MUDDY_DIFFUSE_SHADOW", rule_ids)
        self.assertIn("DOM_06_PERFORMATIVE_BADGE_CLUTTER", rule_ids)

    def test_ast_dom_transmutation(self):
        slop_html = """
        <form action="/login">
          <div class="hero-pill"><span>VOL. 02 // PORTFOLIO</span></div>
          <button class="bg-gradient-to-r from-purple-600 to-cyan-600 shadow-2xl">
            GABUNG SEKARANG 🔥
          </button>
          <select><option>Indonesia</option></select>
        </form>
        """
        res = transmute_dom_tree(slop_html, target_archetype="neo_brutalist")
        self.assertEqual(res["status"], "SUCCESS")
        self.assertTrue(res["transmuted_score"] > res["initial_score"])
        
        transmuted = res["transmuted_code"]
        self.assertIn('novalidate=""', transmuted)
        self.assertNotIn("from-purple-600", transmuted)
        self.assertNotIn("🔥", transmuted)
        self.assertNotIn("hero-pill", transmuted)
        self.assertIn("appearance-none", transmuted)

    def test_modular_button_factory(self):
        # 1. HTML Neo-Brutalist
        btn_html = render_button("SIMPAN DRAF", variant="neo_brutal", size="lg", framework="html")
        self.assertIn("shadow-[4px_4px_0px_#000000]", btn_html)
        self.assertIn("SIMPAN DRAF", btn_html)

        # 2. Blade Component
        btn_blade = render_button("PROSES TRANSAKSI", variant="swiss_editorial", framework="blade")
        self.assertIn("@props", btn_blade)
        self.assertIn("<button", btn_blade)

        # 3. React Component
        btn_react = render_button("SUBMIT", variant="spatial_glass", framework="react")
        self.assertIn("export function UpnormalButton", btn_react)

        # 4. Vue Component
        btn_vue = render_button("SIMPAN VUE", variant="obsidian_sleek", framework="vue")
        self.assertIn("<script setup>", btn_vue)
        self.assertIn("defineProps", btn_vue)
        self.assertIn("<template>", btn_vue)

        # 5. Svelte Component
        btn_svelte = render_button("KIRIM SVELTE", variant="neo_brutal", framework="svelte")
        self.assertIn("$props()", btn_svelte)
        self.assertIn("restProps", btn_svelte)

        # 6. Alpine Component
        btn_alpine = render_button("KLIK ALPINE", variant="pill_soft", framework="alpine")
        self.assertIn("x-data", btn_alpine)
        self.assertIn("$dispatch('upnormal-click'", btn_alpine)

    def test_card_bento_and_dialog_components(self):
        # Asymmetric Bento Grid
        cells = [
            {"title": "Card 1", "desc": "Desc 1", "span": "col-span-2", "tag": "FEATURE"},
            {"title": "Card 2", "desc": "Desc 2", "span": "col-span-1", "tag": "METRIC"}
        ]
        bento_html = render_bento_grid(cells)
        self.assertIn("col-span-2", bento_html)
        self.assertIn("col-span-1", bento_html)

        # In-Place Morphing Dialog
        dialog_html = render_morphing_dialog("BUKA DETAIL", "Konfirmasi Pesanan", "Apakah pesanan sudah benar?")
        self.assertIn("up-morph-trigger", dialog_html)
        self.assertIn("up-morph-surface", dialog_html)
        self.assertIn("backdrop-blur-md", dialog_html)

    def test_badges_dropdown_and_navbar(self):
        # 1. Badge test
        badge = render_badge("live")
        self.assertIn("LIVE", badge)
        self.assertIn("animate-ping", badge)

        # 2. Dropdown test
        dropdown = render_dropdown_menu()
        self.assertIn("data-up-dropdown", dropdown)
        self.assertIn("data-up-dropdown-trigger", dropdown)

        # 3. Navbar test
        navbar = render_navbar(brand_text="cihuy", brand_dot_color="#10b981")
        self.assertIn("cihuy", navbar)
        self.assertIn("animate-pulse", navbar)

    def test_spacing_intelligence(self):
        # 1. Spacing scale tokens
        sys_standard = get_spacing_system("standard")
        self.assertEqual(sys_standard["density_mode"], "standard")
        self.assertIn("--space-4: 1rem", sys_standard["css_variables"])

        # 2. Spacing audit detects oversized mobile padding
        bad_spacing = '<div class="p-8 m-[17px] pt-6 toggle">Konten</div>'
        audit = audit_spacing_classes(bad_spacing)
        self.assertEqual(audit["status"], "SPACING_ISSUES_DETECTED")
        types = [i["type"] for i in audit["issues"]]
        self.assertIn("OVERSIZED_MOBILE_PADDING", types)
        self.assertIn("ARBITRARY_NON_SCALE_SPACING", types)

    def test_interactive_playground_generator(self):
        playground = generate_interactive_playground_html()
        self.assertIn("<!DOCTYPE html>", playground)
        self.assertIn("UPNORMAL UI PLAYGROUND", playground)
        self.assertIn("MODULAR BUTTON SHOWCASE", playground)
        self.assertIn("ASYMMETRIC BENTO GRID", playground)

if __name__ == "__main__":
    unittest.main()
