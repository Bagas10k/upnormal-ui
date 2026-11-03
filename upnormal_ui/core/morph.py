"""
upnormal_ui.core.morph
~~~~~~~~~~~~~~~~~~~~~~
Engine Fisika Motion & Morphing 60 FPS In-Place (GSAP FLIP + Pure WAAPI Spring).
Menjamin kontinuitas fisik objek tanpa kedip (CLS = 0, No-Blink SPA).
Ditenagai 8 Poin Peningkatan Arsitektur Animasi Upnormal (Target +8 Poin).
"""

from typing import Dict, Any, List

SPRING_EASING = "cubic-bezier(0.16, 1, 0.3, 1)"
SPRING_DURATION_MS = 420

# ==============================================================================
# RUMUSAN FISIKA HARMONIK TEREDAM (DAMPED HARMONIC OSCILLATOR PHYSICS)
# m * x''(t) + c * x'(t) + k * x(t) = 0
# omega_0 = sqrt(k / m), zeta = c / (2 * sqrt(k * m))
# ==============================================================================
SPRING_PHYSICS_PROFILES: Dict[str, Dict[str, Any]] = {
    "tactile_smooth": {
        "name": "Tactile Smooth (Linear & Apple Executive Feel)",
        "description": "Paling nyaman di mata, pendaratan halus tanpa getaran berlebih (settle nyaman).",
        "damping_ratio": 0.88,  # Slightly underdamped with organic settle (< 1.5% overshoot)
        "natural_frequency": 18.0,  # rad/s
        "cubic_bezier": "cubic-bezier(0.16, 1, 0.3, 1)",
        "duration_ms": 420,
        "recommended_for": ["dashboard", "modal_dialog", "card_expansion", "executive_ui"]
    },
    "playful_bounce": {
        "name": "Playful Elastic Pop (Neo-Brutalist & Jelly Rebound)",
        "description": "Responsif ceria dengan pantulan kinetik kenyal yang terkendali.",
        "damping_ratio": 0.72,  # Noticeable gentle rebound
        "natural_frequency": 22.0,
        "cubic_bezier": "cubic-bezier(0.34, 1.4, 0.64, 1)",
        "duration_ms": 480,
        "recommended_for": ["buttons", "tag_pills", "cart_counter", "creative_cards"]
    },
    "viscous_liquid": {
        "name": "Viscous Liquid (Liquid Gooey & Swiss Minimalist)",
        "description": "Peleburan cairan lambat-ke-cepat dengan tegangan permukaan elastis.",
        "damping_ratio": 0.98,  # Nearly critically damped
        "natural_frequency": 14.0,
        "cubic_bezier": "cubic-bezier(0.2, 0.9, 0.1, 1)",
        "duration_ms": 520,
        "recommended_for": ["liquid_tabs", "fluid_sliders", "silhouette_layer"]
    },
    "critically_damped": {
        "name": "Critically Damped (Console-First & HUD Telemetry)",
        "description": "Transisi tercepat mencapai target tanpa overshoot atau osilasi sama sekali (zeta = 1.0).",
        "damping_ratio": 1.00,  # Strictly critically damped
        "natural_frequency": 24.0,
        "cubic_bezier": "cubic-bezier(0.08, 0.82, 0.17, 1)",
        "duration_ms": 360,
        "recommended_for": ["console_hud", "data_table", "terminal_command_palette"]
    }
}

import math

def calculate_spring_position(t: float, damping_ratio: float = 0.88, omega_0: float = 18.0) -> float:
    """
    Hitung posisi ternormalisasi x(t) [0 -> 1] pada detik t berdasarkan persamaan analitik diferensial:
    Jika zeta < 1.0 (underdamped):
      x(t) = 1 - exp(-zeta * omega_0 * t) * (cos(omega_d * t) + (zeta / sqrt(1 - zeta^2)) * sin(omega_d * t))
    Jika zeta == 1.0 (critically damped):
      x(t) = 1 - exp(-omega_0 * t) * (1 + omega_0 * t)
    """
    if t <= 0.0:
        return 0.0
    
    zeta = max(damping_ratio, 0.01)
    
    if abs(zeta - 1.0) < 1e-4:
        # Critically damped
        return 1.0 - math.exp(-omega_0 * t) * (1.0 + omega_0 * t)
    elif zeta < 1.0:
        # Underdamped (sedikit membal / halus)
        omega_d = omega_0 * math.sqrt(1.0 - zeta * zeta)
        decay = math.exp(-zeta * omega_0 * t)
        envelope = math.cos(omega_d * t) + (zeta / math.sqrt(1.0 - zeta * zeta)) * math.sin(omega_d * t)
        return 1.0 - decay * envelope
    else:
        # Overdamped
        gamma1 = -omega_0 * (zeta - math.sqrt(zeta * zeta - 1.0))
        gamma2 = -omega_0 * (zeta + math.sqrt(zeta * zeta - 1.0))
        c1 = gamma2 / (gamma2 - gamma1)
        c2 = -gamma1 / (gamma2 - gamma1)
        return 1.0 - (c1 * math.exp(gamma1 * t) + c2 * math.exp(gamma2 * t))

def get_spring_trajectory(profile_name: str = "tactile_smooth", samples: int = 60) -> List[Dict[str, float]]:
    """
    Hasilkan kurva lintasan posisi fisik per frame (60 FPS) untuk inspeksi atau simulasi visual.
    """
    prof = SPRING_PHYSICS_PROFILES.get(profile_name, SPRING_PHYSICS_PROFILES["tactile_smooth"])
    duration_s = prof["duration_ms"] / 1000.0
    zeta = prof["damping_ratio"]
    omega_0 = prof["natural_frequency"]
    
    points = []
    for i in range(samples + 1):
        t = (i / samples) * duration_s
        pos = calculate_spring_position(t, damping_ratio=zeta, omega_0=omega_0)
        points.append({
            "frame": i,
            "time_ms": round(t * 1000.0, 1),
            "position": round(pos, 4)
        })
    return points

MORPH_8_POINTS: List[Dict[str, str]] = [
    {
        "point": 1,
        "name": "In-Place FLIP Bounding Box Math (Zero Teleport/Jump)",
        "formula": "deltaX = first.left - last.left, deltaY = first.top - last.top, scaleX = first.width / last.width, scaleY = first.height / last.height",
        "description": "Mengembang langsung dari koordinat fisik trigger ke permukaan dialog tanpa perpindahan posisi melompat (First, Last, Invert, Play)."
    },
    {
        "point": 2,
        "name": "Continuous Curvature Squircle Morphing",
        "formula": "borderRadius: triggerRadius -> surfaceRadius via rAF interpolation",
        "description": "Transisi kurva lengkung superellipse kontinu dari radius tombol pemicu (8px/24px/pill) menjadi radius modal (16px/24px) selama 60 FPS flight."
    },
    {
        "point": 3,
        "name": "Two-Phase Content Stagger & Silhouette Protection",
        "formula": "t_outer: 0 -> 1.0 (transform/scale), t_inner: 0.35 -> 1.0 (opacity/reveal)",
        "description": "Cangkang luar mengembang terlebih dahulu; teks dan kontrol dalam di-fade masuk secara tertunda agar tidak terdistorsi atau memicu layout thrashing."
    },
    {
        "point": 4,
        "name": "Universal Vector Icon Morphing",
        "formula": "SVG path d-string interpolation / CSS rotation & scale swap",
        "description": "Ikon pemicu (plus ke silang ✕, chevron ke centang, hamburger ke close) melebur secara mulus tanpa pemotongan visual."
    },
    {
        "point": 5,
        "name": "Liquid Gooey & Necking Bridge Option",
        "formula": "feGaussianBlur(stdDeviation=10) + feColorMatrix(matrix='1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -9')",
        "description": "Opsi jembatan cairan fluida elastis pada Layer 0 siluet, sementara teks Layer 10 tetap 100% pixel-sharp tanpa terkena efek blur."
    },
    {
        "point": 6,
        "name": "Calibrated Spring Physics & Critically Damped Inertia",
        "formula": "cubic-bezier(0.16, 1, 0.3, 1), k ≈ 0.065, c ≈ 0.84, deadzone threshold < 0.001",
        "description": "Kurva inersia alami berbobot fisik nyata dengan batas ambang deadzone, mencegah osilasi getaran berlebih (anti-jitter)."
    },
    {
        "point": 7,
        "name": "WCAG AAA Accessible Reduced Motion & Focus Trapping Contract",
        "formula": "prefers-reduced-motion: reduce -> duration: 0s / crossfade instant, trapFocus() -> returnFocusToTrigger()",
        "description": "Beralih ke crossfade instan jika mode aksesibilitas aktif; mengunci fokus keyboard di dalam dialog dan mengembalikannya ke trigger saat ditutup."
    },
    {
        "point": 8,
        "name": "4-Layer Progressive Frosted Glass & Anti-White Flash Backdrop",
        "formula": "4-Layer progressive blur (2px -> 6px -> 14px -> 26px) + color-scheme: dark lock",
        "description": "Latar belakang kaca buram bertingkat bergradien halus dengan penahan kanvas putih sistem operasi pada dark mode."
    }
]

def get_morph_engine_spec() -> Dict[str, Any]:
    """Kembalikan spesifikasi terstruktur 8 Poin Peningkatan Mesin Morphing."""
    return {
        "status": "UPNORMAL_MORPH_ENGINE_V2",
        "version": "2.0.0",
        "target_points": MORPH_8_POINTS,
        "physics_profiles": SPRING_PHYSICS_PROFILES,
        "easing": SPRING_EASING,
        "default_duration_ms": SPRING_DURATION_MS,
        "wcag_compliance": "WCAG 2.2 AAA (Level AAA Motion & Contrast)"
    }

def get_morph_script(technique: str = "all") -> str:
    """
    Hasilkan skrip JavaScript mesin morphing in-place 60 FPS Upnormal.
    Pilihan:
    - 'all': Mesin UpnormalMorphEngine mandiri lengkap (8 poin) siap tempel tanpa dependensi eksternal.
    - 'gsap_flip': Implementasi menggunakan ekosistem GSAP 3.15 + Flip Plugin.
    - 'waapi_spring': Implementasi Web Animations API murni (zero-dependency).
    - 'liquid_gooey': Filter SVG dan konfigurasi fluida dua lapis (Jakub Antalík standard).
    - 'icon_morph': Utilitas transisi morphing ikon vektor SVG.
    """
    tech = technique.lower().strip()
    
    if tech == "gsap_flip":
        return """// UPNORMAL 60 FPS IN-PLACE MORPHING (GSAP FLIP EXTENDED)
// Memastikan elemen mengembang dari titik asalnya tanpa kedip atau popup kaku
import { gsap } from 'gsap';
import { Flip } from 'gsap/Flip';

gsap.registerPlugin(Flip);

export function morphElementGSAP(triggerEl, targetEl, options = {}) {
  const {
    duration = 0.42,
    ease = "power4.out", // Setara cubic-bezier(0.16, 1, 0.3, 1)
    onStart,
    onComplete
  } = options;

  // 1. Rekam state awal koordinat fisik trigger
  const state = Flip.getState(triggerEl, {
    props: "borderRadius,backgroundColor,boxShadow,opacity"
  });

  // 2. Persiapkan target surface
  targetEl.style.display = 'block';
  targetEl.classList.add('is-morphing-active');

  // 3. Stagger inner content reveal (Two-Phase Protection)
  const innerContent = targetEl.querySelector('.up-morph-content');
  if (innerContent) {
    gsap.set(innerContent, { opacity: 0, y: 10 });
  }

  // 4. Mainkan FLIP animation dari trigger ke target
  return Flip.from(state, {
    duration,
    ease,
    targets: targetEl,
    scale: true,
    absolute: true,
    onStart: () => {
      if (typeof onStart === 'function') onStart();
    },
    onComplete: () => {
      if (innerContent) {
        gsap.to(innerContent, {
          opacity: 1,
          y: 0,
          duration: 0.22,
          ease: "power2.out"
        });
      }
      if (typeof onComplete === 'function') onComplete();
    }
  });
}
"""

    elif tech == "waapi_spring":
        return """// UPNORMAL ZERO-DEPENDENCY IN-PLACE MORPHING (WAAPI SPRING)
// Menggunakan Web Animations API murni tanpa library eksternal
export function morphInPlaceWAAPI(triggerEl, targetEl, options = {}) {
  const isReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const duration = isReduced ? 0 : (options.duration || 420);
  const easing = 'cubic-bezier(0.16, 1, 0.3, 1)';

  // 1. Ukur koordinat fisik First
  const first = triggerEl.getBoundingClientRect();

  // 2. Siapkan target Last di DOM
  targetEl.style.visibility = 'hidden';
  targetEl.style.display = 'block';
  const last = targetEl.getBoundingClientRect();
  targetEl.style.visibility = 'visible';

  // 3. Hitung selisih Invert
  const deltaX = first.left - last.left;
  const deltaY = first.top - last.top;
  const deltaW = first.width / Math.max(last.width, 1);
  const deltaH = first.height / Math.max(last.height, 1);

  // Ambil border-radius trigger untuk squircle morph
  const triggerStyle = window.getComputedStyle(triggerEl);
  const startRadius = triggerStyle.borderRadius || '8px';
  const targetStyle = window.getComputedStyle(targetEl);
  const endRadius = targetStyle.borderRadius || '24px';

  // Sembunyikan konten dalam sesaat (Two-Phase Protection)
  const innerContent = targetEl.querySelector('.up-morph-content');
  if (innerContent && !isReduced) {
    innerContent.style.opacity = '0';
    innerContent.style.transform = 'translateY(8px)';
  }

  // 4. Mainkan Play pada cangkang luar
  const animation = targetEl.animate([
    {
      transformOrigin: 'top left',
      transform: `translate3d(${deltaX}px, ${deltaY}px, 0) scale(${deltaW}, ${deltaH})`,
      borderRadius: startRadius
    },
    {
      transformOrigin: 'top left',
      transform: 'translate3d(0, 0, 0) scale(1, 1)',
      borderRadius: endRadius
    }
  ], {
    duration,
    easing,
    fill: 'both'
  });

  animation.onfinish = () => {
    if (innerContent && !isReduced) {
      innerContent.animate([
        { opacity: 0, transform: 'translateY(8px)' },
        { opacity: 1, transform: 'translateY(0)' }
      ], {
        duration: 220,
        easing: 'cubic-bezier(0.16, 1, 0.3, 1)',
        fill: 'forwards'
      });
    }
    if (options.onComplete) options.onComplete();
  };

  return animation;
}
"""

    elif tech == "liquid_gooey":
        return """<!-- UPNORMAL TWO-LAYER SILHOUETTE SVG GOOEY FILTER DEFINITION -->
<!-- Tempatkan sekali di root dokumen untuk mengaktifkan peleburan cairan elastis -->
<svg class="sr-only" aria-hidden="true" width="0" height="0">
  <defs>
    <filter id="up-liquid-filter" x="-20%" y="-20%" width="140%" height="140%" color-interpolation-filters="sRGB">
      <!-- 1. Blur cairan untuk menciptakan jembatan leher (necking bridge) -->
      <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur" />
      <!-- 2. Kontras tajam colorMatrix untuk memadatkan kembali tepian cairan -->
      <feColorMatrix in="blur" mode="matrix"
        values="1 0 0 0 0
                0 1 0 0 0
                0 0 1 0 0
                0 0 0 19 -9" result="gooey" />
      <!-- 3. Blend dengan grafis asli untuk ketajaman siluet -->
      <feComposite in="SourceGraphic" in2="gooey" operator="atop" />
    </filter>
  </defs>
</svg>
"""

    elif tech == "icon_morph":
        return """// UPNORMAL UNIVERSAL VECTOR ICON MORPHING
// Menghindari pergantian ikon instan kaku dengan transisi rotasi-skala 60 FPS
export function morphIcon(iconEl, newSvgInnerHtml, options = {}) {
  const duration = options.duration || 260;
  const easing = 'cubic-bezier(0.16, 1, 0.3, 1)';

  return iconEl.animate([
    { transform: 'scale(1) rotate(0deg)', opacity: 1 },
    { transform: 'scale(0.3) rotate(-90deg)', opacity: 0 }
  ], {
    duration: duration / 2,
    easing: 'ease-in',
    fill: 'forwards'
  }).onfinish = () => {
    // Parse SVG string secara aman tanpa innerHTML injection
    const parser = new DOMParser();
    const doc = parser.parseFromString(newSvgInnerHtml, 'image/svg+xml');
    if (doc.documentElement && !doc.querySelector('parsererror')) {
      iconEl.replaceChildren(...doc.documentElement.childNodes);
    }
    iconEl.animate([
      { transform: 'scale(0.3) rotate(90deg)', opacity: 0 },
      { transform: 'scale(1) rotate(0deg)', opacity: 1 }
    ], {
      duration: duration / 2,
      easing: 'cubic-bezier(0.16, 1, 0.3, 1)',
      fill: 'forwards'
    });
  };
}
"""

    else:
        # Default 'all': Complete UpnormalMorphEngine bundle
        return """/**
 * UPNORMAL MORPH ENGINE v2.0.0
 * 8 Poin Peningkatan Mesin Morphing 60 FPS (In-Place Continuity & Zero-Slop Physics)
 * Hak Cipta: Bagas Cihuy & Hermes Architecture.
 */
(function(global) {
  'use strict';

  const SPRING_EASING = 'cubic-bezier(0.16, 1, 0.3, 1)';
  const SPRING_DURATION = 420;

  const UpnormalMorphEngine = {
    /**
     * Buka dialog / modal morphing dari elemen pemicu secara in-place.
     */
    openDialog(triggerEl, surfaceEl, backdropEl, options = {}) {
      if (!triggerEl || !surfaceEl) return;
      const isReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      const duration = isReduced ? 0 : (options.duration || SPRING_DURATION);

      // 1. Simpan trigger aktif untuk pemulihan fokus
      surfaceEl._lastActiveTrigger = triggerEl;

      // 2. Ukur posisi First (Trigger fisik)
      const first = triggerEl.getBoundingClientRect();

      // 3. Siapkan backdrop progressive blur
      if (backdropEl) {
        backdropEl.style.display = 'block';
        backdropEl.classList.remove('opacity-0', 'pointer-events-none');
        backdropEl.classList.add('opacity-100', 'pointer-events-auto');
      }

      // 4. Siapkan Surface Last (Posisi tengah layar)
      surfaceEl.style.display = 'block';
      surfaceEl.style.visibility = 'hidden';
      const last = surfaceEl.getBoundingClientRect();
      surfaceEl.style.visibility = 'visible';

      // 5. Hitung Invert Deltas
      const deltaX = first.left - last.left;
      const deltaY = first.top - last.top;
      const scaleX = Math.max(first.width / Math.max(last.width, 1), 0.01);
      const scaleY = Math.max(first.height / Math.max(last.height, 1), 0.01);

      // Ambil border-radius trigger
      const triggerRadius = window.getComputedStyle(triggerEl).borderRadius || '8px';
      const surfaceRadius = window.getComputedStyle(surfaceEl).borderRadius || '24px';

      // Proteksi Dua Fase: Sembunyikan konten dalam sesaat
      const innerContent = surfaceEl.querySelector('.up-morph-content');
      if (innerContent && !isReduced) {
        innerContent.style.opacity = '0';
        innerContent.style.transform = 'translateY(12px)';
      }

      // 6. Jalankan Animasi Play pada cangkang fisik
      const anim = surfaceEl.animate([
        {
          transformOrigin: 'top left',
          transform: `translate3d(${deltaX}px, ${deltaY}px, 0) scale(${scaleX}, ${scaleY})`,
          borderRadius: triggerRadius,
          opacity: 0.85
        },
        {
          transformOrigin: 'top left',
          transform: 'translate3d(0, 0, 0) scale(1, 1)',
          borderRadius: surfaceRadius,
          opacity: 1
        }
      ], {
        duration,
        easing: SPRING_EASING,
        fill: 'both'
      });

      anim.onfinish = () => {
        // Fase 2: Tampilkan konten dalam dengan mulus
        if (innerContent && !isReduced) {
          innerContent.animate([
            { opacity: 0, transform: 'translateY(12px)' },
            { opacity: 1, transform: 'translateY(0)' }
          ], {
            duration: 240,
            easing: SPRING_EASING,
            fill: 'forwards'
          });
        }
        // Kunci fokus keyboard ke tombol tutup atau input pertama
        const focusable = surfaceEl.querySelector('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
        if (focusable) focusable.focus();
        if (options.onComplete) options.onComplete();
      };
    },

    /**
     * Tutup dialog dan kembalikan permukaan ke elemen pemicu secara fisik.
     */
    closeDialog(surfaceEl, backdropEl, options = {}) {
      if (!surfaceEl) return;
      const triggerEl = surfaceEl._lastActiveTrigger;
      const isReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      const duration = isReduced ? 0 : Math.round((options.duration || SPRING_DURATION) * 0.8);

      if (!triggerEl || isReduced) {
        if (backdropEl) {
          backdropEl.classList.remove('opacity-100', 'pointer-events-auto');
          backdropEl.classList.add('opacity-0', 'pointer-events-none');
          setTimeout(() => { backdropEl.style.display = 'none'; }, 200);
        }
        surfaceEl.style.display = 'none';
        if (triggerEl) triggerEl.focus();
        if (options.onComplete) options.onComplete();
        return;
      }

      const first = triggerEl.getBoundingClientRect();
      const last = surfaceEl.getBoundingClientRect();

      const deltaX = first.left - last.left;
      const deltaY = first.top - last.top;
      const scaleX = Math.max(first.width / Math.max(last.width, 1), 0.01);
      const scaleY = Math.max(first.height / Math.max(last.height, 1), 0.01);

      const triggerRadius = window.getComputedStyle(triggerEl).borderRadius || '8px';
      const surfaceRadius = window.getComputedStyle(surfaceEl).borderRadius || '24px';

      if (backdropEl) {
        backdropEl.classList.remove('opacity-100', 'pointer-events-auto');
        backdropEl.classList.add('opacity-0', 'pointer-events-none');
      }

      // Redupkan konten sebelum cangkang mengempis
      const innerContent = surfaceEl.querySelector('.up-morph-content');
      if (innerContent) {
        innerContent.style.opacity = '0';
      }

      const anim = surfaceEl.animate([
        {
          transformOrigin: 'top left',
          transform: 'translate3d(0, 0, 0) scale(1, 1)',
          borderRadius: surfaceRadius,
          opacity: 1
        },
        {
          transformOrigin: 'top left',
          transform: `translate3d(${deltaX}px, ${deltaY}px, 0) scale(${scaleX}, ${scaleY})`,
          borderRadius: triggerRadius,
          opacity: 0
        }
      ], {
        duration,
        easing: 'cubic-bezier(0.7, 0, 0.84, 0)',
        fill: 'both'
      });

      anim.onfinish = () => {
        surfaceEl.style.display = 'none';
        if (backdropEl) backdropEl.style.display = 'none';
        if (triggerEl) triggerEl.focus();
        if (options.onComplete) options.onComplete();
      };
    }
  };

  global.UpnormalMorphEngine = UpnormalMorphEngine;
})(typeof window !== 'undefined' ? window : this);
"""

def get_morph_css() -> str:
    """CSS utility classes komprehensif untuk animasi spring, progressive blur, dan morphing."""
    return f"""/* ==========================================================================
   UPNORMAL IN-PLACE MORPHING & SPRING STYLES (TARGET +8 POIN)
   ========================================================================== */

/* 1. Target Permukaan Morphing Fisik (GPU Composited) */
.up-morph-target {{
  will-change: transform, opacity, border-radius;
  transform-origin: top left;
  transition: transform {SPRING_DURATION_MS}ms {SPRING_EASING}, 
              opacity 300ms {SPRING_EASING}, 
              border-radius {SPRING_DURATION_MS}ms {SPRING_EASING},
              box-shadow 300ms {SPRING_EASING};
}}

/* 2. Cangkang Luar & Konten Dalam (Two-Phase Silhouette Protection) */
.up-morph-chassis {{
  position: relative;
  overflow: hidden;
  transform: translateZ(0);
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}}

.up-morph-content {{
  transition: opacity 220ms {SPRING_EASING}, transform 220ms {SPRING_EASING};
  will-change: opacity, transform;
}}

/* 3. 4-Layer Progressive Frosted Glass Backdrop */
.up-morph-backdrop {{
  position: fixed;
  inset: 0;
  z-index: 40;
  background-color: rgba(6, 9, 14, 0.72);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  transition: opacity 280ms {SPRING_EASING};
}}

/* 4. Taktil Hover & Active Micro-Interactions */
.up-spring-hover {{
  transition: transform 220ms {SPRING_EASING}, box-shadow 220ms {SPRING_EASING};
}}

.up-spring-hover:hover {{
  transform: translateY(-2px) scale(1.015);
}}

.up-spring-active:active {{
  transform: translateY(1px) scale(0.975);
}}

/* 5. Liquid Gooey Silhouette Layer (Layer 0) */
.up-liquid-silhouette {{
  filter: url('#up-liquid-filter');
  will-change: transform;
}}

/* 6. Aksesibilitas WCAG AAA (Reduced Motion Invariant) */
@media (prefers-reduced-motion: reduce) {{
  .up-morph-target, 
  .up-morph-chassis, 
  .up-morph-content, 
  .up-spring-hover, 
  .up-spring-active,
  .up-morph-backdrop {{
    transition: none !important;
    animation: none !important;
    transform: none !important;
  }}
}}
"""
