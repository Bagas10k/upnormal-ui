# upnormal-ui ⚡

> **The Anti-AI-Slop UI/UX Engine & Design System for Autonomous Agents & Developers**  
> *Bebas dari belenggu template model yang kaku. Menghidupkan seni antarmuka radikal, berjiwa seni, kontras tinggi (WCAG AAA ≥ 7:1), dan fisika morphing 60 FPS in-place.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)
[![MCP Protocol](https://img.shields.io/badge/MCP-Standard%20v1.0-orange.svg)](https://modelcontextprotocol.io)
[![WCAG Strict](https://img.shields.io/badge/Accessibility-WCAG%202.2%20AAA-success.svg)](https://www.w3.org/WAI/standards-guidelines/wcag/)
[![FPS Motion](https://img.shields.io/badge/Motion-60%20FPS%20In--Place-purple.svg)](#)

---

## 🏛️ Manifesto: Mengapa `upnormal-ui` Lahir?

Sebagian besar antarmuka yang dihasilkan oleh model kecerdasan buatan (LLM) modern terjebak dalam **AI Slop**:
- Tombol gradien ungu-ke-cyan murahan yang klise.
- Bento grid simetris 3 kolom yang kaku tanpa hierarki.
- Bayangan kabur tebal (*muddy diffuse shadow*) yang mengotori panggung.
- Teks abu-abu redup (*low contrast*) yang melanggar aksesibilitas.
- Modal pop-up kaku tanpa kontinuitas fisik objek.

**`upnormal-ui` didirikan atas Hakikat Desain Upnormal Mas Bagas:**
> *"Sebenarnya tidak ada patokan tunggal yang kaku! Desain upnormal adalah kebebasan eksplorasi tanpa batas yang berjiwa seni tinggi."*

Paket ini mengubah 20 doktrin desain pasif menjadi **Mesin Komputasi Aktif (Model Context Protocol)** yang bisa dipanggil oleh agen AI (Hermes, Claude, Cursor) maupun pengembang melalui CLI mandiri.

---

## ⚙️ Fitur Utama (Dual Engine)

### 1. Engine Transmutasi Otomatis (The Healer)
Menerima potongan kode HTML/Tailwind biasa yang terinfeksi template AI, mendeteksi 8 dosanya, dan **otomatis me-refactor kode tersebut** menjadi salah satu arketipe upnormal pilihan (menaikkan kontras ke AAA, membuang emoji tombol, dan menyematkan spring physics).

### 2. Generator Sasis Arketipe Dunia (The Creator)
Menghasilkan komponen antarmuka siap pakai (Tailwind CSS + HTML/Blade + GSAP) dari 5 gaya visual dunia:
- 🗞️ **Swiss Editorial Brutalism:** Kanvas *Warm Paper*, display font raksasa kondensasi tinggi, aksen crimson berani, batas garis 1px tegas.
- 🧱 **High-Contrast Neo-Brutalism:** Hard offset shadow (3px-4px hitam pekat), border 2.5px tebal, warna pop tajam, fisika klik taktil.
- 🎛️ **Console-First Cyber HUD:** Monospace tabular murni (*JetBrains Mono*), densitas instrumen tinggi, status beacon aktif.
- 💧 **Liquid Gooey & Jelly Morphing:** *Two-Layer Silhouette Architecture* (peleburan cairan fluida di latar belakang, teks 100% tajam di lapisan atas).
- 🪟 **Tactile Spatial Frosted Glass:** Kedalaman optik berjenjang, *optical border rim*, dan WCAG AAA compliant.

### 3. Mesin Matematis Keterbacaan & Warna
- **Strict WCAG 2.2 AAA Linter:** Menghitung luminansi relatif. Jika rasio $< 7.0:1$, engine mengoreksi *Lightness* HSL secara otomatis.
- **Rasio Panggung Emas 95 : 5:** 95% kanvas akromatik berkelas (*Obsidian, Warm Paper, Terminal Carbon*) + 5% aksen berenergi tinggi.
- **In-Place 60 FPS Morphing:** Boilerplate GSAP FLIP dan Web Animations API (WAAPI) dengan kurva spring `cubic-bezier(0.16, 1, 0.3, 1)`.

---

## 🚀 Instalasi & Penggunaan

### 1. Menjalankan sebagai MCP Server (Hermes / Claude / AI Agent)
Tambahkan ke konfigurasi MCP agen Anda:

```bash
# Integrasi instan ke Hermes Agent
hermes mcp add upnormal-ui --command python3 --args -m upnormal_ui.server
```

Atau daftarkan secara manual ke `claude_desktop_config.json` / `~/.hermes/config.yaml`:
```json
{
  "mcpServers": {
    "upnormal-ui": {
      "command": "python3",
      "args": ["-m", "upnormal_ui.server"]
    }
  }
}
```

### 2. Menjalankan via CLI Mandiri
Paket ini memiliki antarmuka baris perintah (*CLI*) profesional bawaan:

```bash
# 1. Audit DOM struktur terhadap 9 Dosa AI Slop
python3 -m upnormal_ui.cli audit ./resources/views/dashboard.blade.php

# 2. Transmutasi DOM otomatis ke Neo-Brutalist / Swiss Noir
python3 -m upnormal_ui.cli transmute ./components/card.html --archetype neo_brutalist -o ./components/upnormal_card.html

# 3. Generate skala warna perseptual 11-langkah (50-950)
python3 -m upnormal_ui.cli scale "#06b6d4" --name cyan

# 4. Generate komponen tombol modular (HTML / Blade / React)
python3 -m upnormal_ui.cli button "SIMPAN TRANSAKSI" --variant neo_brutal --size lg --framework blade

# 5. Generate seluruh Interactive Component Playground ke HTML
python3 -m upnormal_ui.cli playground -o playground.html
```

---

## 🛠️ Daftar 11 Perkakas MCP (Tool Catalog)

| Nama Tool | Parameter | Deskripsi & Luaran |
|:---|:---|:---|
| **`upnormal_audit_contrast`** | `hex_fg`, `hex_bg`, `target_ratio` | Menghitung rasio kontras. Jika gagal (< 7:1), otomatis melakukan perbaikan warna (*auto-correction*) pada kanal Lightness HSL. |
| **`upnormal_generate_color_scale`** | `accent_hex`, `name` | Menghasilkan skala warna perseptual 11-langkah (50–950) lengkap dengan warna teks kontras WCAG AAA. |
| **`upnormal_scan_anti_slop`** | `code` | [DOM-AWARE LINTER] Memindai kode terhadap 9 Dosa AI Slop (BeautifulSoup4 AST linter). |
| **`upnormal_transmute_ui`** | `code`, `target_archetype`, `accent_color` | [DOM TRANSMUTATION] Merombak struktur DOM template generik menjadi karya seni Upnormal berkelas. |
| **`upnormal_palette_generator`**| `stage`, `accent` | Hasilkan palet panggung 95% akromatik + 5% aksen tunggal (CSS variables & Tailwind). |
| **`upnormal_render_button`** | `label`, `variant`, `size`, `framework` | [BUTTON FACTORY] Hasilkan komponen tombol modular untuk HTML, Blade, atau React. |
| **`upnormal_render_bento_grid`**| `cells_json`, `archetype` | [BENTO FACTORY] Hasilkan komposisi bento grid asimetris berbobot 2:1. |
| **`upnormal_get_morph_dialog`** | `trigger_label`, `dialog_title`, `dialog_content` | [60 FPS MODAL] Sasis dialog modal in-place morphing tanpa jeda kedip (*CLS = 0*). |
| **`upnormal_get_archetype`** | `archetype_name`, `component_type` | Hasilkan sasis komponen siap pakai dari 5 arketipe dunia (*swiss_editorial*, *neo_brutalist*, dll). |
| **`upnormal_get_chassis`** | `chassis_type` | Ambil sasis spesifik: tabel kasir padat (*financial_table*), custom select, atau toggle switch. |
| **`upnormal_generate_playground_html`** | *none* | Hasilkan dokumen HTML Interactive Playground lengkap untuk pengujian visual di browser. |

---

## 🧪 Pengujian Unit (Test Suite)

Seluruh komponen diuji dengan unit test komprehensif:

```bash
python3 tests/test_all.py
```

Output:
```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.014s

OK
```

---

## 📄 Hak Cipta & Lisensi

Diciptakan dan dirancang oleh **Bagas Saputra (Bagas Cihuy)** bersama **Hermes Architecture**.  
Dilisensikan di bawah [MIT License](LICENSE). 100% Open Source, bebas royalti, bebas API key luar, dan bebas registrasi login.
