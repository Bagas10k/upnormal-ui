"""
upnormal_ui.transmute.transmute_engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Engine Transmutasi Otomatis (Dual Engine: Refactoring Slop ➔ Upnormal).
Mentransformasikan template generik menjadi karya seni antarmuka berkelas sesuai arketipe pilihan.
"""

import re
from typing import Dict, List, Any
from upnormal_ui.core.anti_slop import scan_anti_slop

def transmute_code(code: str, target_archetype: str = "neo_brutalist", accent_color: str = "#06b6d4") -> Dict[str, Any]:
    """
    Rombak kode UI generik/slop secara otomatis menjadi kode Upnormal berstandar tinggi.
    """
    initial_audit = scan_anti_slop(code)
    transmuted = code
    changes = []

    # 1. Musnahkan tombol gradien ungu-cyan murahan
    if "from-purple-" in transmuted and "to-cyan-" in transmuted:
        if target_archetype == "neo_brutalist":
            transmuted = re.sub(
                r'class=["\'][^"\']*bg-gradient-to-r\s+from-purple-\d+00\s+to-cyan-\d+00[^"\']*["\']',
                'class="px-5 py-2.5 bg-black text-white font-black text-xs uppercase tracking-wider border-2 border-black rounded shadow-[3px_3px_0px_#000000] hover:-translate-x-0.5 hover:-translate-y-0.5 active:translate-x-0.5 active:translate-y-0.5 active:shadow-none transition-all font-[\'JetBrains_Mono\',monospace]"',
                transmuted
            )
            changes.append("Mengganti tombol gradien ungu-cyan generik dengan tombol taktil Neo-Brutalist Hard Offset.")
        elif target_archetype == "swiss_editorial":
            transmuted = re.sub(
                r'class=["\'][^"\']*bg-gradient-to-r\s+from-purple-\d+00\s+to-cyan-\d+00[^"\']*["\']',
                'class="px-6 py-3 bg-[#0c0a09] text-[#fafaf9] hover:bg-[#ef4444] font-bold text-xs uppercase tracking-widest transition-colors font-[\'JetBrains_Mono\',monospace]"',
                transmuted
            )
            changes.append("Mengganti tombol gradien ungu-cyan dengan tombol Swiss Editorial Noir & Aksen Crimson.")
        else:
            transmuted = re.sub(
                r'class=["\'][^"\']*bg-gradient-to-r\s+from-purple-\d+00\s+to-cyan-\d+00[^"\']*["\']',
                f'class="px-6 py-2.5 bg-[#0d1422] text-[#f8fafc] border border-[#1e293b] hover:border-[{accent_color}] hover:text-[{accent_color}] active:scale-95 transition-all font-bold text-xs uppercase tracking-wider rounded-lg"',
                transmuted
            )
            changes.append(f"Mengganti tombol gradien ungu-cyan dengan tombol presisi border aksen {accent_color}.")

    # 2. Hapus emoji dalam tombol/badge dan ubah ke label teks bersih
    emoji_matches = re.findall(r'([🚀✨🔥💡🤖🎉⚡👍🏆📦🛒])', transmuted)
    if emoji_matches:
        transmuted = re.sub(r'[🚀✨🔥💡🤖🎉⚡👍🏆📦🛒]\s*', '', transmuted)
        changes.append(f"Menghapus {len(emoji_matches)} emoji dari UI dan menggantinya dengan tipografi bersih (gunakan Iconify SVG untuk ikon).")

    # 3. Koreksi teks abu-abu pudar melanggar WCAG AAA
    if re.search(r'text-(?:gray|slate|zinc|neutral)-(?:400|500)', transmuted):
        transmuted = re.sub(r'text-(?:gray|slate|zinc|neutral)-(?:400|500)', 'text-slate-200', transmuted)
        changes.append("Menaikkan kontras teks abu-abu pudar ke 'text-slate-200' untuk memenuhi standar WCAG AAA (≥ 7:1).")

    # 4. Ganti bayangan difus kusam (muddy blur)
    if "shadow-2xl" in transmuted or "shadow-xl" in transmuted:
        if target_archetype == "neo_brutalist":
            transmuted = re.sub(r'shadow-(?:2xl|xl)', 'shadow-[4px_4px_0px_#000000]', transmuted)
            changes.append("Mengganti shadow blur kusam menjadi Neo-Brutalist Hard Offset Shadow (4px 4px 0px).")
        else:
            transmuted = re.sub(r'shadow-(?:2xl|xl)', 'border border-white/10 shadow-lg', transmuted)
            changes.append("Mengganti shadow blur kusam menjadi garis tepian optik ramping (border-white/10).")

    # 5. Kustomisasi elemen <select> native tanpa gaya
    if re.search(r'<select(?![^>]*class=)', transmuted):
        transmuted = re.sub(
            r'<select',
            '<select class="appearance-none bg-[#0d1422] border border-[#1e293b] text-[#f8fafc] px-4 py-2.5 rounded-lg text-xs font-semibold focus:outline-none focus:border-[#06b6d4] transition-colors"',
            transmuted
        )
        changes.append("Membungkus elemen <select> native menjadi kontrol kustom anti-native berkelas.")

    # 6. Injeksi kurva motion spring in-place jika belum ada
    if "up-morph-target" not in transmuted and ("hover:" in transmuted or "transition" in transmuted):
        transmuted = transmuted.replace('class="', 'class="up-morph-target ', 1)
        changes.append("Menyematkan utility class 'up-morph-target' untuk memastikan transisi mengikuti kurva spring 60 FPS.")

    # 7. Musnahkan kicker badge clutter & floating bragging pills
    if re.search(r'<div[^>]*class=["\'][^"\']*(?:hero-pill|hero-badges-strip)[^"\']*[\s\S]*?<\/div>', transmuted, re.IGNORECASE):
        transmuted = re.sub(r'<div[^>]*class=["\'][^"\']*(?:hero-pill|hero-badges-strip)[^"\']*[\s\S]*?<\/div>\s*', '', transmuted, flags=re.IGNORECASE)
        changes.append("Memusnahkan kicker badge clutter dan floating tech-bragging pills yang mengotori panggung.")

    final_audit = scan_anti_slop(transmuted)

    return {
        "status": "SUCCESS",
        "archetype_applied": target_archetype,
        "initial_score": initial_audit["score"],
        "transmuted_score": final_audit["score"],
        "total_changes": len(changes),
        "changes_applied": changes,
        "transmuted_code": transmuted
    }
