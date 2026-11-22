"""
MindEase FYP - Official World-Class Brand Identity & Vector Logo Generator
Final Year Project: MindEase - AI-Driven Stress Detection, Recovery & Support for Students
COMSATS University Islamabad, Wah Campus

Generates high-precision, aesthetic vector brand assets:
1. MindEase App Icon (Squircle Badge 1024x1024 with Neural Lotus & Pulse)
2. MindEase Full Horizontal Brand Identity Logo (Emblem + Precision Typography)
3. MindEase Circular Emblem (Ideal for UI headers, avatars, and mobile top bars)
4. MindEase Wireframe Vector Component (Optimized inline SVG for mobile screens)
"""
import os
import pymupdf

def generate_all_brand_assets():
    brand_dir = os.path.join("Documentation", "Brand")
    os.makedirs(brand_dir, exist_ok=True)

    # =========================================================================
    # 1. Flagship App Icon (1024x1024 Master Vector)
    # =========================================================================
    app_icon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
  <defs>
    <!-- Background Canvas Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e1a"/>
      <stop offset="35%" stop-color="#0f172a"/>
      <stop offset="70%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>

    <!-- Calming Oceanic Sky Gradient -->
    <linearGradient id="cyanGlow" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="45%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#bae6fd"/>
    </linearGradient>

    <!-- Healing Emerald Mint Gradient -->
    <linearGradient id="mintGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="60%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>

    <!-- Warm Serenity Lavender Gradient -->
    <linearGradient id="violetGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>

    <!-- Gold Accent Gradient -->
    <linearGradient id="goldGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </linearGradient>

    <!-- Soft Drop Shadow Filter -->
    <filter id="badgeShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="24" stdDeviation="32" flood-color="#000000" flood-opacity="0.45"/>
    </filter>

    <filter id="glowFilter" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Pure White Canvas Background -->
  <rect width="1024" height="1024" fill="#ffffff"/>

  <!-- Master Squircle Container with Premium Shadow -->
  <rect x="92" y="92" width="840" height="840" rx="196" fill="url(#bgGrad)" filter="url(#badgeShadow)"/>
  
  <!-- Subtle Chamfer Rim Light -->
  <rect x="96" y="96" width="832" height="832" rx="192" fill="none" stroke="#38bdf8" stroke-width="4" opacity="0.4"/>
  <rect x="100" y="100" width="824" height="824" rx="188" fill="none" stroke="#ffffff" stroke-width="1.5" opacity="0.2"/>

  <!-- Ambient Radial Guidance Rings & Dial Ticks -->
  <circle cx="512" cy="512" r="330" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8,12" opacity="0.25"/>
  <circle cx="512" cy="512" r="270" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="4,8" opacity="0.15"/>

  <!-- ================= THE EMBLEM: NEURAL BRAIN + ZEN LOTUS + BIO-PULSE ================= -->
  <!-- Ambient Center Aura -->
  <circle cx="512" cy="512" r="180" fill="#0284c7" opacity="0.15" filter="url(#glowFilter)"/>

  <!-- Brain Hemisphere Lobes (Dual Symmetry Harmonized with Lotus Petal Contours) -->
  <!-- Left Brain Hemisphere -->
  <path d="M 512 256 C 410 256 320 324 320 430 C 320 476 344 516 372 544 C 336 572 312 616 312 668 C 312 752 380 816 464 816 C 490 816 504 804 512 792" 
        fill="none" stroke="#ffffff" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" opacity="0.95"/>
  
  <!-- Right Brain Hemisphere -->
  <path d="M 512 256 C 614 256 704 324 704 430 C 704 476 680 516 652 544 C 688 572 712 616 712 668 C 712 752 644 816 560 816 C 534 816 520 804 512 792" 
        fill="none" stroke="#ffffff" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" opacity="0.95"/>

  <!-- Inner Blooming Lotus Petals (Cyan Gradient Flow) -->
  <!-- Outer Left Lotus Petal -->
  <path d="M 512 740 C 470 690 410 610 410 510 C 410 410 470 330 512 290" 
        fill="none" stroke="url(#cyanGlow)" stroke-width="20" stroke-linecap="round"/>
  
  <!-- Outer Right Lotus Petal -->
  <path d="M 512 740 C 554 690 614 610 614 510 C 614 410 554 330 512 290" 
        fill="none" stroke="url(#cyanGlow)" stroke-width="20" stroke-linecap="round"/>

  <!-- Central Serenity Heart-Leaf (Healing Translucent Gradient) -->
  <path d="M 512 320 C 480 420 456 510 456 590 C 456 670 480 730 512 750 C 544 730 568 670 568 590 C 568 510 544 420 512 320 Z" 
        fill="url(#cyanGlow)" opacity="0.32"/>

  <!-- Inner Soft Violet Energy Ray -->
  <path d="M 512 360 C 496 440 484 510 484 580 C 484 640 496 690 512 710 C 528 690 540 640 540 580 C 540 510 528 440 512 360 Z" 
        fill="url(#violetGlow)" opacity="0.45"/>

  <!-- ================= VITAL BIO-SIGNAL ECG PULSE ================= -->
  <!-- The Real-Time Stress Tracking Pulse that flows through the heart of the mind -->
  <path d="M 410 570 L 470 570 L 488 520 L 512 630 L 536 540 L 552 570 L 614 570" 
        fill="none" stroke="#ffffff" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" filter="url(#glowFilter)"/>

  <!-- ================= NEURAL AI SYNAPSE NODES ================= -->
  <!-- Top Temporal Synapses -->
  <circle cx="410" cy="390" r="18" fill="#38bdf8" filter="url(#glowFilter)"/>
  <circle cx="410" cy="390" r="9" fill="#ffffff"/>

  <circle cx="614" cy="390" r="18" fill="#38bdf8" filter="url(#glowFilter)"/>
  <circle cx="614" cy="390" r="9" fill="#ffffff"/>

  <!-- Lateral Parietal Synapses -->
  <circle cx="370" cy="550" r="16" fill="#38bdf8"/>
  <circle cx="370" cy="550" r="8" fill="#ffffff"/>

  <circle cx="654" cy="550" r="16" fill="#38bdf8"/>
  <circle cx="654" cy="550" r="8" fill="#ffffff"/>

  <!-- Lower Healing Synapses (Emerald Green for Recovery & Equilibrium) -->
  <circle cx="420" cy="710" r="18" fill="url(#mintGlow)" filter="url(#glowFilter)"/>
  <circle cx="420" cy="710" r="9" fill="#ffffff"/>

  <circle cx="604" cy="710" r="18" fill="url(#mintGlow)" filter="url(#glowFilter)"/>
  <circle cx="604" cy="710" r="9" fill="#ffffff"/>

  <!-- Crown Apex Clarity Node (Clarity & Mindfulness) -->
  <circle cx="512" cy="256" r="22" fill="#ffffff" filter="url(#glowFilter)"/>
  <circle cx="512" cy="256" r="11" fill="#0284c7"/>
</svg>'''

    # =========================================================================
    # 2. Horizontal Master Brand Identity (1200x340)
    # =========================================================================
    horizontal_logo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="340" viewBox="0 0 1200 340">
  <defs>
    <linearGradient id="hbgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e1a"/>
      <stop offset="40%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e3a8a"/>
    </linearGradient>

    <linearGradient id="hcyanGlow" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#7dd3fc"/>
    </linearGradient>

    <linearGradient id="hmintGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>

    <filter id="hShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000000" flood-opacity="0.22"/>
    </filter>
  </defs>

  <rect width="1200" height="340" fill="#ffffff"/>

  <!-- Left Icon Emblem (240x240, Center at 160, 170) -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="240" height="240" rx="56" fill="url(#hbgGrad)" filter="url(#hShadow)"/>
    <rect x="2" y="2" width="236" height="236" rx="54" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.45"/>
    <circle cx="120" cy="120" r="95" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4,6" opacity="0.25"/>

    <!-- Scaled Vector Symbol (Centered inside Emblem) -->
    <g transform="translate(120, 120) scale(0.24) translate(-512, -512)">
      <!-- Left Brain Lobe -->
      <path d="M 512 256 C 410 256 320 324 320 430 C 320 476 344 516 372 544 C 336 572 312 616 312 668 C 312 752 380 816 464 816 C 490 816 504 804 512 792" 
            fill="none" stroke="#ffffff" stroke-width="28" stroke-linecap="round"/>
      <!-- Right Brain Lobe -->
      <path d="M 512 256 C 614 256 704 324 704 430 C 704 476 680 516 652 544 C 688 572 712 616 712 668 C 712 752 644 816 560 816 C 534 816 520 804 512 792" 
            fill="none" stroke="#ffffff" stroke-width="28" stroke-linecap="round"/>
      <!-- Lotus Petals -->
      <path d="M 512 740 C 470 690 410 610 410 510 C 410 410 470 330 512 290" 
            fill="none" stroke="url(#hcyanGlow)" stroke-width="22" stroke-linecap="round"/>
      <path d="M 512 740 C 554 690 614 610 614 510 C 614 410 554 330 512 290" 
            fill="none" stroke="url(#hcyanGlow)" stroke-width="22" stroke-linecap="round"/>
      <!-- Pulse line -->
      <path d="M 410 570 L 470 570 L 488 520 L 512 630 L 536 540 L 552 570 L 614 570" 
            fill="none" stroke="#ffffff" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Synapses -->
      <circle cx="410" cy="390" r="18" fill="#38bdf8"/>
      <circle cx="614" cy="390" r="18" fill="#38bdf8"/>
      <circle cx="420" cy="710" r="18" fill="url(#hmintGlow)"/>
      <circle cx="604" cy="710" r="18" fill="url(#hmintGlow)"/>
      <circle cx="512" cy="256" r="22" fill="#ffffff"/>
    </g>
  </g>

  <!-- Typography Suite -->
  <!-- Wordmark -->
  <text x="320" y="152" font-family="'Segoe UI', -apple-system, 'Helvetica Neue', Arial, sans-serif" font-size="82" font-weight="900" fill="#0f172a" letter-spacing="-2">Mind<tspan fill="#0284c7">Ease</tspan></text>
  
  <!-- Category Badge -->
  <rect x="690" y="96" width="145" height="34" rx="17" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
  <text x="762" y="118" font-family="'Segoe UI', Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e40af" text-anchor="middle" letter-spacing="0.5">AI PLATFORM</text>

  <!-- Primary Subtitle / Tagline -->
  <text x="324" y="202" font-family="'Segoe UI', Arial, sans-serif" font-size="22" font-weight="700" fill="#334155" letter-spacing="0.5">AI-Driven Stress Detection, Recovery &amp; Academic Support</text>
  
  <!-- Secondary Institutional Line -->
  <text x="324" y="238" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="500" fill="#64748b">Final Year Project (FYP) • COMSATS University Islamabad, Wah Campus</text>

  <!-- Decorative Accent Bar -->
  <rect x="324" y="260" width="380" height="4" rx="2" fill="url(#hcyanGlow)"/>
</svg>'''

    # =========================================================================
    # 3. Circular Emblem (For Profile Avatars, App Headers, 512x512)
    # =========================================================================
    circular_badge_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="cbg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e1a"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="ccyan" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#7dd3fc"/>
    </linearGradient>
    <linearGradient id="cmint" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <filter id="cShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
  </defs>

  <rect width="512" height="512" fill="#ffffff"/>
  <circle cx="256" cy="256" r="220" fill="url(#cbg)" filter="url(#cShadow)"/>
  <circle cx="256" cy="256" r="216" fill="none" stroke="#38bdf8" stroke-width="3" opacity="0.5"/>
  <circle cx="256" cy="256" r="185" fill="none" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="6,8" opacity="0.2"/>

  <!-- Centered Symbol -->
  <g transform="translate(256, 256) scale(0.25) translate(-512, -512)">
    <path d="M 512 256 C 410 256 320 324 320 430 C 320 476 344 516 372 544 C 336 572 312 616 312 668 C 312 752 380 816 464 816 C 490 816 504 804 512 792" 
          fill="none" stroke="#ffffff" stroke-width="28" stroke-linecap="round"/>
    <path d="M 512 256 C 614 256 704 324 704 430 C 704 476 680 516 652 544 C 688 572 712 616 712 668 C 712 752 644 816 560 816 C 534 816 520 804 512 792" 
          fill="none" stroke="#ffffff" stroke-width="28" stroke-linecap="round"/>
    <path d="M 512 740 C 470 690 410 610 410 510 C 410 410 470 330 512 290" 
          fill="none" stroke="url(#ccyan)" stroke-width="22" stroke-linecap="round"/>
    <path d="M 512 740 C 554 690 614 610 614 510 C 614 410 554 330 512 290" 
          fill="none" stroke="url(#ccyan)" stroke-width="22" stroke-linecap="round"/>
    <path d="M 410 570 L 470 570 L 488 520 L 512 630 L 536 540 L 552 570 L 614 570" 
          fill="none" stroke="#ffffff" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="410" cy="390" r="18" fill="#38bdf8"/>
    <circle cx="614" cy="390" r="18" fill="#38bdf8"/>
    <circle cx="420" cy="710" r="18" fill="url(#cmint)"/>
    <circle cx="604" cy="710" r="18" fill="url(#cmint)"/>
    <circle cx="512" cy="256" r="22" fill="#ffffff"/>
  </g>
</svg>'''

    # Save SVG files
    svg_app = os.path.join(brand_dir, "MindEase_App_Icon.svg")
    png_app = os.path.join(brand_dir, "MindEase_App_Icon.png")
    pdf_app = os.path.join(brand_dir, "MindEase_App_Icon.pdf")

    svg_h = os.path.join(brand_dir, "MindEase_Logo_Horizontal.svg")
    png_h = os.path.join(brand_dir, "MindEase_Logo_Horizontal.png")
    pdf_h = os.path.join(brand_dir, "MindEase_Logo_Horizontal.pdf")

    svg_c = os.path.join(brand_dir, "MindEase_Circular_Badge.svg")
    png_c = os.path.join(brand_dir, "MindEase_Circular_Badge.png")
    pdf_c = os.path.join(brand_dir, "MindEase_Circular_Badge.pdf")

    with open(svg_app, "w", encoding="utf-8") as f:
        f.write(app_icon_svg)
    with open(svg_h, "w", encoding="utf-8") as f:
        f.write(horizontal_logo_svg)
    with open(svg_c, "w", encoding="utf-8") as f:
        f.write(circular_badge_svg)

    # Render PNGs at 300 DPI
    for s_path, p_path, pdf_p in [
        (svg_app, png_app, pdf_app),
        (svg_h, png_h, pdf_h),
        (svg_c, png_c, pdf_c)
    ]:
        doc = pymupdf.open(s_path)
        pix = doc[0].get_pixmap(dpi=300)
        pix.save(p_path)
        pdf_bytes = doc.convert_to_pdf()
        pdf_doc = pymupdf.open("pdf", pdf_bytes)
        pdf_doc.save(pdf_p)
        pdf_doc.close()
        doc.close()
        print(f"Generated Brand Asset: {p_path} ({pix.width}x{pix.height} px, 300 DPI)")

if __name__ == "__main__":
    generate_all_brand_assets()
