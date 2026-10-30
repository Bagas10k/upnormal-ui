"""
upnormal_ui.cli
~~~~~~~~~~~~~~~
CLI interface mandiri untuk upnormal-ui.
Bisa dijalankan langsung via terminal: `python -m upnormal_ui [command]`.
"""

import sys
import argparse
import json
import asyncio
from upnormal_ui.core.anti_slop import scan_anti_slop
from upnormal_ui.transmute.transmute_engine import transmute_code
from upnormal_ui.core.palette import generate_upnormal_palette
from upnormal_ui.server import server

def main():
    parser = argparse.ArgumentParser(
        prog="upnormal-ui",
        description="The Anti-AI-Slop UI/UX Engine & Design System"
    )
    subparsers = parser.add_subparsers(dest="command", help="Perintah yang tersedia")

    # Command: serve (Jalankan MCP server)
    subparsers.add_parser("serve", help="Jalankan MCP server (stdio transport)")

    # Command: audit
    audit_parser = subparsers.add_parser("audit", help="Pindai file HTML/Blade terhadap dosa AI Slop")
    audit_parser.add_argument("file", help="Path ke berkas yang ingin diaudit")

    # Command: transmute
    transmute_parser = subparsers.add_parser("transmute", help="Rombak file UI slop menjadi kode Upnormal")
    transmute_parser.add_argument("file", help="Path ke berkas target")
    transmute_parser.add_argument("--archetype", default="neo_brutalist", choices=["neo_brutalist", "swiss_editorial", "console_hud", "spatial_glass"], help="Arketipe target")
    transmute_parser.add_argument("--accent", default="#06b6d4", help="Hex warna aksen 5%")
    transmute_parser.add_argument("-o", "--output", help="Simpan hasil ke file baru")

    # Command: palette
    palette_parser = subparsers.add_parser("palette", help="Hasilkan palet warna rasio emas 95:5")
    palette_parser.add_argument("--stage", default="obsidian", choices=["obsidian", "warm_paper", "terminal_carbon", "liquid_void"])
    palette_parser.add_argument("--accent", default="#06b6d4")

    args = parser.parse_args()

    if args.command == "serve" or args.command is None:
        asyncio.run(server.run_stdio_async())
    elif args.command == "audit":
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
        res = scan_anti_slop(content)
        print(json.dumps(res, indent=2))
    elif args.command == "transmute":
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
        res = transmute_code(content, target_archetype=args.archetype, accent_color=args.accent)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(res["transmuted_code"])
            print(f"Hasil transmutasi berhasil disimpan ke: {args.output}")
        else:
            print(res["transmuted_code"])
    elif args.command == "palette":
        res = generate_upnormal_palette(stage_name=args.stage, accent_hex=args.accent)
        print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
