"""
upnormal_ui.transmute.ast_transmute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Engine Transmutasi DOM Struktural (BeautifulSoup4).
Mentransformasikan pohon HTML/Blade yang terinfeksi template AI slop
secara atomik dan aman tanpa merusak struktur markup.
"""

import re
from typing import Dict, Any, List
from bs4 import BeautifulSoup, Tag, NavigableString
from upnormal_ui.core.ast_linter import lint_dom_structure, EMOJI_REGEX, GRADIENT_SLOP_REGEX, SHADOW_SLOP_REGEX

def transmute_dom_tree(html_content: str, target_archetype: str = "neo_brutalist", accent_color: str = "#06b6d4") -> Dict[str, Any]:
    """
    Rombak struktur DOM HTML/Blade secara menyeluruh menjadi kode antarmuka Upnormal berstandar tinggi.
    """
    initial_lint = lint_dom_structure(html_content)
    soup = BeautifulSoup(html_content, "html.parser")
    changes_applied: List[str] = []

    # 1. Hapus total performative kicker badge clutter (.hero-pill, .hero-badges-strip, dsb)
    for elem in list(soup.find_all(True)):
        if getattr(elem, "attrs", None) is None:
            continue
        classes = elem.get("class", [])
        class_str = " ".join(classes) if isinstance(classes, list) else str(classes)
        text = elem.get_text()

        is_pill_class = any(p in class_str for p in ["hero-pill", "hero-badges-strip", "badge-tag"])
        has_bragging_text = any(w in text.lower() for w in ["zero ai-slop", "wcag aaa", "60 fps in-place", "portofolio resmi vol"])

        if is_pill_class or has_bragging_text:
            elem.decompose()
            changes_applied.append("Menghapus elemen kicker badge clutter & tag pamer teknis dari DOM.")

    # 2. Tambahkan 'novalidate' ke seluruh tag <form>
    for form in list(soup.find_all("form")):
        if getattr(form, "attrs", None) is not None and not form.has_attr("novalidate"):
            form["novalidate"] = ""
            changes_applied.append("Menambahkan atribut 'novalidate' ke tag <form> untuk mencegah tooltip error bawaan peramban.")

    # 3. Bersihkan emoji dari tombol, tautan, dan badge
    for elem in list(soup.find_all(["button", "a", "span"])):
        if getattr(elem, "contents", None) is None:
            continue
        for child in list(elem.children):
            if isinstance(child, NavigableString):
                cleaned_text = EMOJI_REGEX.sub("", str(child)).strip()
                if cleaned_text != str(child).strip():
                    child.replace_with(cleaned_text)
                    changes_applied.append("Membersihkan emoji dari elemen teks tombol/tautan.")

    # 4. Transmutasikan tombol gradien ungu-cyan murahan
    for elem in list(soup.find_all(True)):
        if getattr(elem, "attrs", None) is None:
            continue
        classes = elem.get("class", [])
        if not classes:
            continue
        class_str = " ".join(classes) if isinstance(classes, list) else str(classes)

        if GRADIENT_SLOP_REGEX.search(class_str):
            # Bersihkan kelas gradien
            new_classes = [c for c in classes if not any(g in c for g in ["from-purple-", "to-cyan-", "bg-gradient-to-r", "bg-gradient-to-l"])]

            if target_archetype == "neo_brutalist":
                new_classes.extend([
                    "px-6", "py-3", "bg-black", "text-white", "font-black", "text-xs",
                    "uppercase", "tracking-wider", "border-2", "border-black", "rounded-lg",
                    "shadow-[4px_4px_0px_#000000]", "hover:-translate-x-0.5", "hover:-translate-y-0.5",
                    "active:translate-x-1", "active:translate-y-1", "active:shadow-none",
                    "transition-all", "font-['JetBrains_Mono',monospace]"
                ])
                changes_applied.append("Mengubah tombol gradien ungu-cyan menjadi tombol taktil Neo-Brutalist Hard Offset.")
            elif target_archetype == "swiss_editorial":
                new_classes.extend([
                    "px-6", "py-3.5", "bg-[#0c0a09]", "text-[#fafaf9]", "hover:bg-[#ef4444]",
                    "font-bold", "text-xs", "uppercase", "tracking-widest", "transition-colors",
                    "font-['JetBrains_Mono',monospace]"
                ])
                changes_applied.append("Mengubah tombol gradien ungu-cyan menjadi tombol Swiss Noir & Aksen Crimson.")
            else:
                new_classes.extend([
                    "px-6", "py-3", "bg-[#0d1422]", "text-[#f8fafc]", "border", "border-[#1e293b]",
                    f"hover:border-[{accent_color}]", f"hover:text-[{accent_color}]", "rounded-xl",
                    "font-bold", "text-xs", "uppercase", "tracking-wider", "transition-all"
                ])
                changes_applied.append(f"Mengubah tombol gradien menjadi tombol presisi beraksen {accent_color}.")

            elem["class"] = list(set(new_classes))

        # 5. Ganti bayangan blur kusam (muddy diffuse shadow)
        if SHADOW_SLOP_REGEX.search(class_str):
            new_classes = [c for c in elem.get("class", []) if not c.startswith("shadow-2xl") and not c.startswith("shadow-xl")]
            if target_archetype == "neo_brutalist":
                new_classes.append("shadow-[4px_4px_0px_#000000]")
            else:
                new_classes.append("border")
                new_classes.append("border-white/10")
            elem["class"] = new_classes
            changes_applied.append("Mengganti bayangan blur tebal dengan garis batas tajam / hard offset.")

    # 6. Sempurnakan elemen <select> native
    for sel in list(soup.find_all("select")):
        if getattr(sel, "attrs", None) is None:
            continue
        classes = sel.get("class", [])
        if "appearance-none" not in classes:
            classes.extend([
                "appearance-none", "bg-[#0d1422]", "border", "border-[#1e293b]",
                "text-[#f8fafc]", "py-2.5", "px-4", "pr-10", "rounded-lg",
                "text-xs", "font-semibold", "focus:outline-none", "transition-colors", "cursor-pointer"
            ])
            sel["class"] = classes
            changes_applied.append("Mengonversi elemen <select> native menjadi kontrol kustom anti-native.")

    transmuted_html = str(soup)
    final_lint = lint_dom_structure(transmuted_html)

    return {
        "status": "SUCCESS",
        "archetype_applied": target_archetype,
        "initial_score": initial_lint["score"],
        "transmuted_score": final_lint["score"],
        "initial_violations_count": initial_lint["total_violations"],
        "final_violations_count": final_lint["total_violations"],
        "total_changes_applied": len(changes_applied),
        "changes_applied": changes_applied,
        "transmuted_code": transmuted_html
    }
