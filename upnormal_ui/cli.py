"""
upnormal_ui.cli
~~~~~~~~~~~~~~~
CLI mandiri profesional untuk upnormal-ui.
Bisa dijalankan langsung via terminal: `python -m upnormal_ui.cli [command]`.
"""

import sys
import argparse
import json
import asyncio
from upnormal_ui.core.ast_linter import lint_dom_structure
from upnormal_ui.transmute.ast_transmute import transmute_dom_tree
from upnormal_ui.core.color_scale import generate_11_step_scale
from upnormal_ui.core.palette import generate_upnormal_palette
from upnormal_ui.components.button import render_button
from upnormal_ui.components.playground import generate_interactive_playground_html
from upnormal_ui.server import server

def main():
    parser = argparse.ArgumentParser(
        prog="upnormal-ui",
        description="The Professional Anti-AI-Slop UI/UX Engine & Design System"
    )
    subparsers = parser.add_subparsers(dest="command", help="Perintah yang tersedia")

    # Command: serve (Jalankan MCP server)
    subparsers.add_parser("serve", help="Jalankan MCP server (stdio transport)")

    # Command: audit (DOM-aware linter)
    audit_parser = subparsers.add_parser("audit", help="Pindai file HTML/Blade terhadap 9 Dosa AI Slop (DOM AST)")
    audit_parser.add_argument("file", help="Path ke berkas yang ingin diaudit")

    # Command: transmute (DOM-aware refactoring)
    transmute_parser = subparsers.add_parser("transmute", help="Rombak file UI slop menjadi kode Upnormal berkelas")
    transmute_parser.add_argument("file", help="Path ke berkas target")
    transmute_parser.add_argument("--archetype", default="neo_brutalist", choices=["neo_brutalist", "swiss_editorial", "console_hud", "spatial_glass"], help="Arketipe target")
    transmute_parser.add_argument("--accent", default="#06b6d4", help="Hex warna aksen 5%")
    transmute_parser.add_argument("-o", "--output", help="Simpan hasil ke file baru")

    # Command: scale (11-step color scale)
    scale_parser = subparsers.add_parser("scale", help="Hasilkan skala warna perseptual 11-langkah (50-950) WCAG AAA")
    scale_parser.add_argument("hex", help="Kode hex warna dasar (misal: #06b6d4)")
    scale_parser.add_argument("--name", default="brand", help="Nama prefix token")

    # Command: palette (95:5 stage)
    palette_parser = subparsers.add_parser("palette", help="Hasilkan palet warna rasio emas 95:5")
    palette_parser.add_argument("--stage", default="obsidian", choices=["obsidian", "warm_paper", "terminal_carbon", "liquid_void"])
    palette_parser.add_argument("--accent", default="#06b6d4")

    # Command: button
    btn_parser = subparsers.add_parser("button", help="Hasilkan kode tombol Upnormal modular")
    btn_parser.add_argument("label", nargs="?", default="TINDAKAN ➔")
    btn_parser.add_argument("--variant", default="neo_brutal", choices=["neo_brutal", "swiss_editorial", "obsidian_sleek", "spatial_glass", "pill_soft"])
    btn_parser.add_argument("--size", default="md", choices=["sm", "md", "lg"])
    btn_parser.add_argument("--framework", default="html", choices=["html", "blade", "react", "vue", "svelte", "alpine"])
    btn_parser.add_argument("--accent", action="store_true", help="Gunakan warna aksen")

    # Command: playground
    play_parser = subparsers.add_parser("playground", help="Hasilkan file HTML Interactive Playground lengkap")
    play_parser.add_argument("-o", "--output", default="playground.html", help="Path file output HTML")

    args = parser.parse_args()

    if args.command == "serve" or args.command is None:
        asyncio.run(server.run_stdio_async())
    elif args.command == "audit":
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
        res = lint_dom_structure(content)
        print(json.dumps(res, indent=2))
    elif args.command == "transmute":
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
        res = transmute_dom_tree(content, target_archetype=args.archetype, accent_color=args.accent)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(res["transmuted_code"])
            print(f"Hasil transmutasi berhasil disimpan ke: {args.output} (Skor: {res['initial_score']} ➔ {res['transmuted_score']})")
        else:
            print(res["transmuted_code"])
    elif args.command == "scale":
        res = generate_11_step_scale(args.hex, name=args.name)
        print(json.dumps(res, indent=2))
    elif args.command == "palette":
        res = generate_upnormal_palette(stage_name=args.stage, accent_hex=args.accent)
        print(json.dumps(res, indent=2))
    elif args.command == "button":
        btn = render_button(label=args.label, variant=args.variant, size=args.size, is_accent=args.accent, framework=args.framework)
        print(btn)
    elif args.command == "playground":
        html = generate_interactive_playground_html()
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Interactive Component Playground berhasil dibuat: {args.output}")

if __name__ == "__main__":
    main()
