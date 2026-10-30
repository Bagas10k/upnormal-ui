"""
upnormal_ui.core.morph
~~~~~~~~~~~~~~~~~~~~~~
Engine Fisika Motion & Morphing 60 FPS In-Place (GSAP FLIP + Pure CSS Spring).
Menjamin kontinuitas fisik objek tanpa kedip (CLS = 0, No-Blink SPA).
"""

from typing import Dict, Any

SPRING_EASING = "cubic-bezier(0.16, 1, 0.3, 1)"

def get_morph_script(technique: str = "gsap_flip") -> str:
    """
    Hasilkan skrip boilerplate JavaScript untuk morphing in-place 60 FPS.
    Pilihan: 'gsap_flip' (GSAP FLIP Plugin) atau 'waapi_spring' (Web Animations API murni).
    """
    if technique == "gsap_flip":
        return """// UPNORMAL 60 FPS IN-PLACE MORPHING (GSAP FLIP)
// Memastikan elemen mengembang dari titik asalnya tanpa kedip atau popup kaku
import { gsap } from 'gsap';
import { Flip } from 'gsap/Flip';

gsap.registerPlugin(Flip);

export function morphElement(triggerEl, targetContainer, expandedContentHtml, onComplete) {
  // 1. Rekam state awal (koordinat fisik & ukuran trigger)
  const state = Flip.getState(triggerEl, { props: "borderRadius,backgroundColor,boxShadow" });

  // 2. Mutasi DOM secara aman
  triggerEl.classList.add('is-expanded');
  if (expandedContentNode && expandedContentNode.nodeType) {
    triggerEl.replaceChildren(expandedContentNode);
  }

  // 3. Mainkan morphing fisik dari state awal ke posisi akhir
  Flip.from(state, {
    duration: 0.45,
    ease: "power4.out", // Setara cubic-bezier(0.16, 1, 0.3, 1)
    absolute: true,
    scale: true,
    onComplete: () => {
      if (typeof onComplete === 'function') onComplete();
    }
  });
}
"""
    else:
        return """// UPNORMAL ZERO-DEPENDENCY IN-PLACE MORPHING (WAAPI)
// Menggunakan Web Animations API murni tanpa library eksternal
export function morphInPlaceWAAPI(element, targetRect, durationMs = 380) {
  const first = element.getBoundingClientRect();
  
  // Terapkan state akhir
  element.style.position = 'fixed';
  element.style.top = `${targetRect.top}px`;
  element.style.left = `${targetRect.left}px`;
  element.style.width = `${targetRect.width}px`;
  element.style.height = `${targetRect.height}px`;
  
  const last = element.getBoundingClientRect();
  
  // Hitung selisih transformasi (Invert)
  const deltaX = first.left - last.left;
  const deltaY = first.top - last.top;
  const deltaW = first.width / last.width;
  const deltaH = first.height / last.height;
  
  // Mainkan animasi Play
  return element.animate([
    {
      transformOrigin: 'top left',
      transform: `translate(${deltaX}px, ${deltaY}px) scale(${deltaW}, ${deltaH})`
    },
    {
      transformOrigin: 'top left',
      transform: 'none'
    }
  ], {
    duration: durationMs,
    easing: 'cubic-bezier(0.16, 1, 0.3, 1)',
    fill: 'both'
  });
}
"""

def get_morph_css() -> str:
    """CSS utility classes untuk animasi spring dan morphing."""
    return f"""/* UPNORMAL IN-PLACE MORPHING & SPRING STYLES */
.up-morph-target {{
  will-change: transform, opacity;
  transform-origin: center center;
  transition: transform 380ms {SPRING_EASING}, 
              opacity 300ms {SPRING_EASING}, 
              box-shadow 300ms {SPRING_EASING};
}}

.up-spring-hover:hover {{
  transform: translateY(-2px) scale(1.01);
}}

.up-spring-active:active {{
  transform: translateY(1px) scale(0.98);
}}

@media (prefers-reduced-motion: reduce) {{
  .up-morph-target, .up-spring-hover, .up-spring-active {{
    transition: none !important;
    transform: none !important;
  }}
}}
"""
