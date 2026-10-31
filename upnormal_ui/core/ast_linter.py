"""
upnormal_ui.core.ast_linter
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Linter Struktural Tingkat Tinggi Berbasis DOM Parser (BeautifulSoup4).
Memeriksa kepatuhan antarmuka terhadap arsitektur Upnormal & anti-AI-slop
secara hierarkis dan semantik, bukan sekadar regex string mentah.
"""

import re
from typing import Dict, List, Any
from bs4 import BeautifulSoup, Tag

EMOJI_REGEX = re.compile(r"[\U00010000-\U0010ffff]|[\u2600-\u27ff]|[\u2300-\u23ff]", re.UNICODE)
GRADIENT_SLOP_REGEX = re.compile(r"from-purple-\d+00.*to-cyan-\d+00|linear-gradient\([^)]*purple[^)]*cyan[^)]*\)", re.IGNORECASE)
SHADOW_SLOP_REGEX = re.compile(r"\bshadow-(?:2xl|xl)\b|box-shadow:[^;]*0\s+25px\s+50px", re.IGNORECASE)

def lint_dom_structure(html_content: str) -> Dict[str, Any]:
    """
    Bedah struktur DOM HTML/Blade secara menyeluruh dan temukan cacat desain semantik & estetika.
    Mengembalikan skor kualitas (0-100), daftar pelanggaran terinci (tag, baris, saran perbaikan).
    """
    soup = BeautifulSoup(html_content, "html.parser")
    violations: List[Dict[str, Any]] = []

    # 1. Periksa seluruh tag <form> untuk atribut 'novalidate'
    for form in soup.find_all("form"):
        if not form.has_attr("novalidate"):
            violations.append({
                "rule_id": "DOM_01_FORM_MISSING_NOVALIDATE",
                "severity": "HIGH",
                "element": str(form)[:60] + "...",
                "description": "Formulir tidak memiliki atribut 'novalidate'. Browser akan menampilkan balon validasi native ('Harap isi bidang ini') yang merusak tema antarmuka.",
                "fix_suggestion": "Tambahkan atribut 'novalidate' pada tag <form> dan gunakan validasi visual kustom inline."
            })

    # 2. Periksa kontrol <select> native tanpa penyesuaian kustom
    for sel in soup.find_all("select"):
        classes = sel.get("class", [])
        class_str = " ".join(classes) if isinstance(classes, list) else str(classes)
        if "appearance-none" not in class_str:
            violations.append({
                "rule_id": "DOM_02_UNSTYLED_NATIVE_SELECT",
                "severity": "HIGH",
                "element": str(sel)[:60] + "...",
                "description": "Ditemukan elemen <select> native tanpa class 'appearance-none'. Panah bawaan OS akan merusak estetika antarmuka.",
                "fix_suggestion": "Tambahkan 'appearance-none' dan bungkus dengan div berpanah SVG kustom (atau gunakan komponen custom select Upnormal)."
            })

    # 3. Periksa elemen interaktif (<button>, <a>, badge) yang memuat emoji
    for elem in soup.find_all(["button", "a", "span", "div"]):
        classes = elem.get("class", [])
        class_str = " ".join(classes) if isinstance(classes, list) else str(classes)
        text = elem.get_text()

        if EMOJI_REGEX.search(text) and (elem.name in ["button", "a"] or "badge" in class_str or "btn" in class_str):
            violations.append({
                "rule_id": "DOM_03_EMOJI_IN_INTERACTIVE_UI",
                "severity": "CRITICAL",
                "element": f"<{elem.name} class='{class_str[:30]}'>{text[:40]}</{elem.name}>",
                "description": "Ditemukan emoji di dalam elemen interaktif atau badge. Emoji menciptakan tampilan inkonsisten dan berkesan amatir/template AI.",
                "fix_suggestion": "Hapus emoji dan gantikan dengan vektor SVG presisi dari Iconify (Lucide/Tabler) dengan atribut currentColor."
            })

    # 4. Periksa tombol gradien ungu-cyan murahan
    for elem in soup.find_all(True):
        classes = elem.get("class", [])
        class_str = " ".join(classes) if isinstance(classes, list) else str(classes)
        style = elem.get("style", "")

        if GRADIENT_SLOP_REGEX.search(class_str) or GRADIENT_SLOP_REGEX.search(style):
            violations.append({
                "rule_id": "DOM_04_PURPLE_CYAN_SLOP_GRADIENT",
                "severity": "CRITICAL",
                "element": f"<{elem.name} class='{class_str[:50]}'>",
                "description": "Gradien ungu ke cyan terdeteksi. Ini adalah ciri khas template model AI murahan 2023-2024.",
                "fix_suggestion": "Ganti dengan palet panggung 95% akromatik (Obsidian atau Warm Paper) dan aksen tunggal 5% terukur."
            })

        # 5. Periksa bayangan blur kusam (muddy diffuse shadow)
        if SHADOW_SLOP_REGEX.search(class_str) or SHADOW_SLOP_REGEX.search(style):
            violations.append({
                "rule_id": "DOM_05_MUDDY_DIFFUSE_SHADOW",
                "severity": "MEDIUM",
                "element": f"<{elem.name} class='{class_str[:50]}'>",
                "description": "Bayangan blur tebal (shadow-2xl/xl) menciptakan polusi visual dan mengaburkan batas kartu.",
                "fix_suggestion": "Ganti dengan Hard Offset Shadow pekat (4px 4px 0px #000) atau garis tepian hairline (border: 1px solid #1e293b)."
            })

    # 6. Periksa performative kicker badge clutter (seperti 'Zero AI-Slop', 'WCAG AAA', 'VOL. 02')
    for elem in soup.find_all(["div", "span", "p"]):
        classes = elem.get("class", [])
        class_str = " ".join(classes) if isinstance(classes, list) else str(classes)
        text = elem.get_text()

        is_pill_class = any(p in class_str for p in ["hero-pill", "hero-badges-strip", "badge-tag", "status-strip"])
        has_bragging_text = any(w in text.lower() for w in ["zero ai-slop", "wcag aaa", "60 fps in-place", "portofolio resmi vol"])

        if is_pill_class or has_bragging_text:
            violations.append({
                "rule_id": "DOM_06_PERFORMATIVE_BADGE_CLUTTER",
                "severity": "CRITICAL",
                "element": f"<{elem.name} class='{class_str[:30]}'>{text[:40]}</{elem.name}>",
                "description": "Kicker badge mengambang atau deretan pill pamer teknis terdeteksi. Merupakan polusi visual AI yang murahan.",
                "fix_suggestion": "Hapus total badge clutter ornamental. Biarkan ruang lega, tata letak, dan tipografi yang berbicara sendiri."
            })

    # 7. Periksa grid bento simetris kaku
    for grid in soup.find_all(lambda tag: tag.has_attr("class") and any("grid-cols-3" in c for c in tag["class"])):
        children = [c for c in grid.children if isinstance(c, Tag)]
        if len(children) >= 3 and not any(any("col-span-2" in c for c in child.get("class", [])) for child in children):
            violations.append({
                "rule_id": "DOM_07_RIGID_SYMMETRICAL_GRID",
                "severity": "LOW",
                "element": str(grid)[:60] + "...",
                "description": "Bento grid simetris 3 kolom seragam tanpa hierarki visual asimetris.",
                "fix_suggestion": "Berikan bobot asimetris pada salah satu kartu utama (misal: col-span-2 untuk hero cell, sel sekunder bertumpuk 2:1)."
            })

    # Hitung skor mutu
    weights = {"CRITICAL": 25, "HIGH": 15, "MEDIUM": 10, "LOW": 5}
    penalty = sum(weights.get(v["severity"], 10) for v in violations)
    score = max(0, 100 - penalty)
    status = "UPNORMAL_EXCELLENCE" if score >= 90 else ("SLOP_DETECTED" if score < 70 else "NEEDS_POLISH")

    return {
        "status": status,
        "score": score,
        "total_violations": len(violations),
        "violations": violations,
        "verdict": "Markup bersih, berkelas, dan bebas dari cacat AI slop." if score >= 90 else f"Terdeteksi {len(violations)} pelanggaran arsitektur antarmuka. Terapkan rekomendasi untuk memulihkan standar Upnormal."
    }
