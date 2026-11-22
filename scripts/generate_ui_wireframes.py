"""
Generates clean, professional UI Wireframe / Mobile Screen Mockup diagrams for MindEase FYP SRDS:
- WF01_Landing_Onboarding_Screen
- WF02_Sign_Up_Screen
- WF03_Log_In_Screen
- WF04_Student_Dashboard_Screen
- WF05_Multilingual_Questionnaire_Screen
- WF06_Voice_Diary_Screen
- WF07_XAI_Insights_Screen
- WF08_Adaptive_Study_Planner_Screen
- WF09_Counselor_Booking_Screen
- WF10_Peer_Community_Feed_Screen
"""
import os
import pymupdf
from drawio_builder import DrawioBuilder

def write_wireframe(name, svg_content, title):
    svg_dir = os.path.join("Documentation", "Diagrams", "SVG")
    png_dir = os.path.join("Documentation", "Diagrams", "PNG")
    pdf_dir = os.path.join("Documentation", "Diagrams", "PDF")
    editable_dir = os.path.join("Documentation", "Diagrams", "Editable")
    visio_dir = os.path.join("Documentation", "Diagrams", "Visio")
    os.makedirs(svg_dir, exist_ok=True)
    os.makedirs(png_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)
    os.makedirs(editable_dir, exist_ok=True)
    os.makedirs(visio_dir, exist_ok=True)

    svg_path = os.path.join(svg_dir, f"{name}.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    # Draw.io
    b = DrawioBuilder(name, 500, 850)
    b.add_cell(title, "shape=umlFrame;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1e293b;strokeWidth=1.5;", x=20, y=20, w=460, h=810)
    drawio_content = b.to_xml()

    drawio_path = os.path.join(editable_dir, f"{name}.drawio")
    with open(drawio_path, "w", encoding="utf-8") as f:
        f.write(drawio_content)

    visio_path = os.path.join(visio_dir, f"{name}.drawio")
    with open(visio_path, "w", encoding="utf-8") as f:
        f.write(drawio_content)

    # Render PNG & PDF via pymupdf
    doc = pymupdf.open(svg_path)
    pix = doc[0].get_pixmap(dpi=300)
    png_path = os.path.join(png_dir, f"{name}.png")
    pix.save(png_path)

    pdf_bytes = doc.convert_to_pdf()
    pdf_doc = pymupdf.open("pdf", pdf_bytes)
    pdf_path = os.path.join(pdf_dir, f"{name}.pdf")
    pdf_doc.save(pdf_path)
    pdf_doc.close()
    doc.close()

    print(f"Generated Wireframe: {name} (.svg, .drawio, .png, .pdf)")

def mobile_frame(title, inner_svg):
    w, h = 420, 780
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<rect width="{w}" height="{h}" fill="#ffffff"/>
<!-- Mobile Phone Chassis -->
<rect x="25" y="20" width="370" height="710" rx="36" fill="#f8fafc" stroke="#0f172a" stroke-width="3"/>
<rect x="35" y="30" width="350" height="690" rx="28" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>

<!-- Camera Notch / Dynamic Island -->
<rect x="150" y="38" width="120" height="18" rx="9" fill="#0f172a"/>
<circle cx="240" cy="47" r="3.5" fill="#1e293b"/>

<!-- Status Bar -->
<text x="60" y="52" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">9:41</text>
<text x="350" y="52" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="end">5G 100%</text>

<!-- Screen Content -->
{inner_svg}

<!-- Home Navigation Bar Indicator -->
<rect x="150" y="705" width="120" height="4" rx="2" fill="#94a3b8"/>
<!-- Figure Title Below -->
<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">{title}</text>
</svg>'''

def build_all_wireframes():
    # WF01: Landing & Onboarding
    inner_01 = '''
<!-- Header Logo -->
<circle cx="210" cy="140" r="35" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2"/>
<text x="210" y="148" font-family="Arial, sans-serif" font-size="28" fill="#1e3a8a" text-anchor="middle">🧠</text>
<text x="210" y="205" font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">MindEase</text>
<text x="210" y="228" font-family="Arial, sans-serif" font-size="12" fill="#475569" text-anchor="middle">AI Stress Detection &amp; Academic Support</text>

<!-- Language Selection Card -->
<rect x="55" y="270" width="310" height="150" rx="12" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2"/>
<text x="75" y="298" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Choose Language / زبان منتخب کریں</text>

<rect x="75" y="315" width="80" height="35" rx="6" fill="#1e3a8a"/>
<text x="115" y="337" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">English</text>

<rect x="170" y="315" width="80" height="35" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="210" y="337" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">اردو (Urdu)</text>

<rect x="265" y="315" width="85" height="35" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="307" y="337" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Roman Urdu</text>

<text x="75" y="380" font-family="Arial, sans-serif" font-size="10" fill="#64748b">• Standardized Perceived Stress Scale (PSS)</text>
<text x="75" y="400" font-family="Arial, sans-serif" font-size="10" fill="#64748b">• Voice Reflections via Whisper Speech ASR</text>

<!-- Action Buttons -->
<rect x="55" y="480" width="310" height="48" rx="8" fill="#1e3a8a"/>
<text x="210" y="510" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Get Started (Student / Counselor)</text>

<rect x="55" y="545" width="310" height="48" rx="8" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.5"/>
<text x="210" y="575" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Sign In to Existing Account</text>
'''
    write_wireframe("WF01_Landing_Onboarding_Screen", mobile_frame("Figure 3.3.1: Landing & Onboarding Screen", inner_01), "WF01 Landing Page")

    # WF02: Sign Up
    inner_02 = '''
<text x="55" y="100" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="#0f172a">Create Account</text>
<text x="55" y="120" font-family="Arial, sans-serif" font-size="11" fill="#475569">Join MindEase for confidential support</text>

<!-- Role Toggle -->
<rect x="55" y="145" width="310" height="40" rx="8" fill="#f1f5f9"/>
<rect x="60" y="149" width="145" height="32" rx="6" fill="#1e3a8a"/>
<text x="132" y="169" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Student</text>
<text x="282" y="169" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">Counselor</text>

<!-- Form fields -->
<text x="55" y="215" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Full Name</text>
<rect x="55" y="225" width="310" height="42" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="70" y="251" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">Muhammad Rehan Khalid</text>

<text x="55" y="290" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">University Email</text>
<rect x="55" y="300" width="310" height="42" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="70" y="326" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">fa23-bcs-140@cuiwah.edu.pk</text>

<text x="55" y="365" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Registration Number</text>
<rect x="55" y="375" width="310" height="42" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="70" y="401" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">CIIT/FA23-BCS-140/WAH</text>

<text x="55" y="440" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Password</text>
<rect x="55" y="450" width="310" height="42" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="70" y="476" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">••••••••••••</text>

<rect x="55" y="520" width="310" height="46" rx="8" fill="#1e3a8a"/>
<text x="210" y="548" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Register Account</text>
'''
    write_wireframe("WF02_Sign_Up_Screen", mobile_frame("Figure 3.3.2: User Registration Screen (Sign Up)", inner_02), "WF02 Sign Up Screen")

    # WF03: Log In
    inner_03 = '''
<circle cx="210" cy="130" r="30" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2"/>
<text x="210" y="138" font-family="Arial, sans-serif" font-size="24" fill="#1e3a8a" text-anchor="middle">🔐</text>
<text x="210" y="190" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">Welcome Back</text>
<text x="210" y="210" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Log in to track your stress &amp; study plan</text>

<text x="55" y="255" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Email Address</text>
<rect x="55" y="265" width="310" height="42" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="70" y="291" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">student@cuiwah.edu.pk</text>

<text x="55" y="330" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Password</text>
<rect x="55" y="340" width="310" height="42" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="70" y="366" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8">••••••••••••</text>

<text x="365" y="402" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#1e3a8a" text-anchor="end">Forgot Password?</text>

<rect x="55" y="430" width="310" height="46" rx="8" fill="#1e3a8a"/>
<text x="210" y="458" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Sign In</text>

<text x="210" y="520" font-family="Arial, sans-serif" font-size="11" fill="#64748b" text-anchor="middle">Don't have an account? <tspan font-weight="bold" fill="#1e3a8a">Register</tspan></text>
'''
    write_wireframe("WF03_Log_In_Screen", mobile_frame("Figure 3.3.3: User Login Screen (Authentication)", inner_03), "WF03 Log In Screen")

    # WF04: Student Dashboard
    inner_04 = '''
<text x="55" y="90" font-family="Arial, sans-serif" font-size="12" fill="#64748b">Good morning,</text>
<text x="55" y="112" font-family="Arial, sans-serif" font-size="17" font-weight="bold" fill="#0f172a">Muhammad Rehan</text>

<!-- Today's Stress Status Card -->
<rect x="55" y="130" width="310" height="110" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
<text x="75" y="155" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e40af">TODAY'S ESTIMATED STRESS</text>
<rect x="75" y="165" width="90" height="26" rx="13" fill="#1e40af"/>
<text x="120" y="182" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">MODERATE</text>
<text x="180" y="182" font-family="Arial, sans-serif" font-size="11" fill="#1e293b">Confidence: 87%</text>
<text x="75" y="215" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#2563eb">Why do I feel this way? (Explainable AI) →</text>

<!-- Quick Action Grid -->
<text x="55" y="265" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Quick Check-ins</text>

<rect x="55" y="280" width="145" height="75" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="70" y="305" font-family="Arial, sans-serif" font-size="18">📝</text>
<text x="70" y="325" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Questionnaire</text>
<text x="70" y="340" font-family="Arial, sans-serif" font-size="9" fill="#64748b">PSS-10 Localized</text>

<rect x="220" y="280" width="145" height="75" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="235" y="305" font-family="Arial, sans-serif" font-size="18">🎙️</text>
<text x="235" y="325" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Voice Diary</text>
<text x="235" y="340" font-family="Arial, sans-serif" font-size="9" fill="#64748b">Whisper ASR</text>

<!-- Today's Adaptive Study Plan Card -->
<text x="55" y="380" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Adaptive Study Plan</text>
<rect x="55" y="395" width="310" height="95" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="70" y="420" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Pomodoro: 35m Study, 10m Break</text>
<text x="70" y="440" font-family="Arial, sans-serif" font-size="10" fill="#475569">☑ Software Architecture (Complete 10:00 AM)</text>
<text x="70" y="460" font-family="Arial, sans-serif" font-size="10" fill="#475569">☐ Machine Learning Lab (2:00 PM)</text>

<!-- Bottom Navigation Bar -->
<rect x="35" y="650" width="350" height="55" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5"/>
<text x="75" y="682" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Home</text>
<text x="145" y="682" font-family="Arial, sans-serif" font-size="10" fill="#64748b" text-anchor="middle">Check-in</text>
<text x="210" y="682" font-family="Arial, sans-serif" font-size="10" fill="#64748b" text-anchor="middle">Planner</text>
<text x="280" y="682" font-family="Arial, sans-serif" font-size="10" fill="#64748b" text-anchor="middle">Counselor</text>
<text x="345" y="682" font-family="Arial, sans-serif" font-size="10" fill="#64748b" text-anchor="middle">Community</text>
'''
    write_wireframe("WF04_Student_Dashboard_Screen", mobile_frame("Figure 3.3.4: Student Main Wellness Dashboard", inner_04), "WF04 Student Dashboard")

    # WF05: Questionnaire Screen
    inner_05 = '''
<text x="55" y="90" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Stress Questionnaire</text>
<text x="55" y="108" font-family="Arial, sans-serif" font-size="10" fill="#64748b">Question 3 of 10 • PSS Standardized</text>

<!-- Progress Bar -->
<rect x="55" y="120" width="310" height="6" rx="3" fill="#e2e8f0"/>
<rect x="55" y="120" width="93" height="6" rx="3" fill="#1e3a8a"/>

<!-- Question Card -->
<rect x="55" y="145" width="310" height="230" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
<text x="70" y="175" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">In the last month, how often have</text>
<text x="70" y="195" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">you felt nervous and stressed?</text>
<text x="70" y="220" font-family="Arial, sans-serif" font-size="10" fill="#64748b">پچھلے مہینے میں آپ نے کتنی بار بے چینی محسوس کی؟</text>

<rect x="70" y="240" width="280" height="30" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
<text x="85" y="260" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">Never (کبھی نہیں)</text>

<rect x="70" y="280" width="280" height="30" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
<text x="85" y="300" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">Sometimes (کبھی کبھار)</text>

<rect x="70" y="320" width="280" height="30" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
<text x="85" y="340" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#1e40af">✓ Fairly Often (اکثر اوقات)</text>

<!-- AI Text Scoring Hint -->
<text x="55" y="405" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Optional Personal Reflection:</text>
<rect x="55" y="415" width="310" height="60" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
<text x="65" y="435" font-family="Arial, sans-serif" font-size="10" fill="#94a3b8">Exams are next week and I have 3 assignments...</text>

<rect x="55" y="485" width="310" height="30" rx="4" fill="#ecfdf5" stroke="#10b981"/>
<text x="70" y="505" font-family="Arial, sans-serif" font-size="9" fill="#047857">AI suggested text sub-score: 3/4 [Click to adjust]</text>

<rect x="55" y="535" width="310" height="44" rx="8" fill="#1e3a8a"/>
<text x="210" y="562" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Next Question →</text>
'''
    write_wireframe("WF05_Multilingual_Questionnaire_Screen", mobile_frame("Figure 3.3.5: Multilingual Stress Questionnaire Screen", inner_05), "WF05 Questionnaire Screen")

    # WF06: Voice Diary
    inner_06 = '''
<text x="55" y="90" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#0f172a">Daily Voice Diary Check-in</text>
<text x="55" y="108" font-family="Arial, sans-serif" font-size="10" fill="#64748b">Speak freely in English, Urdu, or Roman Urdu</text>

<!-- Audio Waveform Visualizer -->
<rect x="55" y="140" width="310" height="120" rx="12" fill="#0f172a"/>
<text x="210" y="170" font-family="Arial, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Recording... 01:24 / 03:00</text>
<line x1="80" y1="210" x2="80" y2="230" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<line x1="100" y1="200" x2="100" y2="240" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<line x1="120" y1="190" x2="120" y2="250" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<line x1="140" y1="205" x2="140" y2="235" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<line x1="160" y1="185" x2="160" y2="255" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<line x1="180" y1="195" x2="180" y2="245" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<line x1="200" y1="180" x2="200" y2="260" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<line x1="220" y1="195" x2="220" y2="245" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<line x1="240" y1="205" x2="240" y2="235" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<line x1="260" y1="190" x2="260" y2="250" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<line x1="280" y1="200" x2="280" y2="240" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
<line x1="300" y1="210" x2="300" y2="230" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>

<!-- Whisper Live Transcription -->
<text x="55" y="285" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Whisper ASR Live Transcription:</text>
<rect x="55" y="295" width="310" height="90" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
<text x="70" y="320" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">"Aaj subah se assignment ka bohot load tha,</text>
<text x="70" y="340" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">raat ko sirf 4 ghante neend aayi aur sir dard hai."</text>
<text x="70" y="365" font-family="Arial, sans-serif" font-size="9" fill="#10b981">✓ Language detected: Roman Urdu (Confidence 96%)</text>

<!-- Crisis Safety Banner -->
<rect x="55" y="405" width="310" height="60" rx="8" fill="#fef2f2" stroke="#ef4444"/>
<text x="70" y="425" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#b91c1c">🔒 100% AES-256 Private Encryption</text>
<text x="70" y="445" font-family="Arial, sans-serif" font-size="9" fill="#7f1d1d">Your diary is never accessible to university admins.</text>

<rect x="55" y="485" width="310" height="46" rx="8" fill="#1e3a8a"/>
<text x="210" y="513" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Stop &amp; Save Diary Entry</text>
'''
    write_wireframe("WF06_Voice_Diary_Screen", mobile_frame("Figure 3.3.6: Voice Diary & Whisper Transcription Screen", inner_06), "WF06 Voice Diary Screen")

    # WF07: Explainable AI Insights
    inner_07 = '''
<text x="55" y="90" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#0f172a">Explainable AI (XAI) Insights</text>
<text x="55" y="108" font-family="Arial, sans-serif" font-size="10" fill="#64748b">Transparent root cause breakdown via SHAP</text>

<!-- Summary Box -->
<rect x="55" y="130" width="310" height="85" rx="10" fill="#f8fafc" stroke="#cbd5e1"/>
<text x="70" y="152" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Primary Stress Drivers (Today):</text>
<text x="70" y="172" font-family="Arial, sans-serif" font-size="10" fill="#334155">• Sleep Deficit: Only 4.0 hours logged (-45% impact)</text>
<text x="70" y="192" font-family="Arial, sans-serif" font-size="10" fill="#334155">• High Screen Time: 7.2 hours on phone (+32% impact)</text>
<text x="70" y="208" font-family="Arial, sans-serif" font-size="10" fill="#334155">• Exam Proximity: Software Architecture quiz</text>

<!-- SHAP Attribution Horizontal Bar Chart -->
<text x="55" y="240" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Feature Impact Weight (SHAP Values)</text>

<text x="55" y="265" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">Sleep (4 hrs)</text>
<rect x="150" y="255" width="180" height="14" rx="3" fill="#dc2626"/>
<text x="335" y="266" font-family="Arial, sans-serif" font-size="9" fill="#dc2626">+0.42</text>

<text x="55" y="295" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">Screen Time (7h)</text>
<rect x="150" y="285" width="130" height="14" rx="3" fill="#ea580c"/>
<text x="285" y="296" font-family="Arial, sans-serif" font-size="9" fill="#ea580c">+0.28</text>

<text x="55" y="325" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">PSS Score (28)</text>
<rect x="150" y="315" width="100" height="14" rx="3" fill="#f59e0b"/>
<text x="255" y="326" font-family="Arial, sans-serif" font-size="9" fill="#f59e0b">+0.19</text>

<text x="55" y="355" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">Steps (6,500)</text>
<rect x="150" y="345" width="70" height="14" rx="3" fill="#10b981"/>
<text x="225" y="356" font-family="Arial, sans-serif" font-size="9" fill="#10b981">-0.15</text>

<!-- Targeted Action Recommendation -->
<rect x="55" y="390" width="310" height="90" rx="10" fill="#eff6ff" stroke="#3b82f6"/>
<text x="70" y="415" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e40af">Recommended Recovery Action:</text>
<text x="70" y="435" font-family="Arial, sans-serif" font-size="10" fill="#1e293b">Take a 20-minute screen break and listen to</text>
<text x="70" y="452" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#1e3a8a">"Deep Calming Theta Waves" from the library.</text>

<rect x="55" y="500" width="310" height="44" rx="8" fill="#1e3a8a"/>
<text x="210" y="527" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Start Relaxation Activity Now →</text>
'''
    write_wireframe("WF07_XAI_Insights_Screen", mobile_frame("Figure 3.3.7: Explainable AI (XAI) Attribution Screen", inner_07), "WF07 XAI Screen")

    # WF08: Study Planner
    inner_08 = '''
<text x="55" y="90" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#0f172a">Adaptive Study Planner</text>
<text x="55" y="108" font-family="Arial, sans-serif" font-size="10" fill="#64748b">Stress-adapted Pomodoro intervals</text>

<rect x="55" y="125" width="310" height="36" rx="6" fill="#fef3c7" stroke="#f59e0b"/>
<text x="70" y="147" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#92400e">⚡ Stress Mode Active: Lighter 25m Sessions + 15m Breaks</text>

<!-- Timeline Tasks -->
<rect x="55" y="175" width="310" height="65" rx="8" fill="#ffffff" stroke="#cbd5e1"/>
<text x="70" y="198" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">10:00 AM - 10:25 AM (Focus Session)</text>
<text x="70" y="218" font-family="Arial, sans-serif" font-size="10" fill="#475569">Read Chapter 4: UML Sequence Diagrams</text>

<rect x="55" y="250" width="310" height="50" rx="8" fill="#eff6ff" stroke="#3b82f6"/>
<text x="70" y="272" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e40af">10:25 AM - 10:40 AM (Mindfulness Break)</text>
<text x="70" y="290" font-family="Arial, sans-serif" font-size="10" fill="#1e40af">4-7-8 Breathing Exercise &amp; Hydration</text>

<rect x="55" y="310" width="310" height="65" rx="8" fill="#ffffff" stroke="#cbd5e1"/>
<text x="70" y="333" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">10:40 AM - 11:05 AM (Focus Session)</text>
<text x="70" y="353" font-family="Arial, sans-serif" font-size="10" fill="#475569">Implement FastAPI Endpoint for Habit Tracking</text>

<!-- Task Roll-over -->
<rect x="55" y="390" width="310" height="70" rx="8" fill="#f8fafc" stroke="#e2e8f0"/>
<text x="70" y="415" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Uncompleted Tasks (Roll-over):</text>
<text x="70" y="435" font-family="Arial, sans-serif" font-size="10" fill="#64748b">☐ Data Structures Assignment (Due Tomorrow)</text>
<text x="350" y="445" font-family="Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#1e3a8a" text-anchor="end">Move to Tomorrow →</text>

<rect x="55" y="480" width="310" height="44" rx="8" fill="#1e3a8a"/>
<text x="210" y="507" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">+ Add New Academic Task</text>
'''
    write_wireframe("WF08_Adaptive_Study_Planner_Screen", mobile_frame("Figure 3.3.8: Adaptive Study & Recovery Planner Screen", inner_08), "WF08 Study Planner Screen")

    # WF09: Counselor Directory & Booking
    inner_09 = '''
<text x="55" y="90" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#0f172a">Counselor Directory</text>
<text x="55" y="108" font-family="Arial, sans-serif" font-size="10" fill="#64748b">Book confidential sessions with campus professionals</text>

<!-- Free Session Banner -->
<rect x="55" y="125" width="310" height="42" rx="6" fill="#ecfdf5" stroke="#10b981"/>
<text x="70" y="145" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#047857">🎉 Free Triage Eligible! (High Stress Detected)</text>
<text x="70" y="159" font-family="Arial, sans-serif" font-size="9" fill="#065f46">Your first consultation is 100% sponsored by MindEase.</text>

<!-- Counselor Card 1 -->
<rect x="55" y="180" width="310" height="140" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<circle cx="85" cy="215" r="20" fill="#f1f5f9"/>
<text x="85" y="222" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">👩‍⚕️</text>
<text x="115" y="210" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Dr. Ayesha Tariq, Ph.D.</text>
<text x="115" y="226" font-family="Arial, sans-serif" font-size="10" fill="#64748b">Student Cognitive Anxiety &amp; Burnout</text>
<text x="115" y="242" font-family="Arial, sans-serif" font-size="9" fill="#10b981">✓ CUI Verified Counselor • 8 yrs exp.</text>

<text x="70" y="275" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a">Available Slots Today:</text>
<rect x="70" y="285" width="70" height="24" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
<text x="105" y="301" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">2:00 PM</text>

<rect x="150" y="285" width="70" height="24" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
<text x="185" y="301" font-family="Arial, sans-serif" font-size="9" fill="#0f172a" text-anchor="middle">3:30 PM</text>

<rect x="230" y="285" width="70" height="24" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
<text x="265" y="301" font-family="Arial, sans-serif" font-size="9" fill="#0f172a" text-anchor="middle">5:00 PM</text>

<!-- Counselor Card 2 -->
<rect x="55" y="335" width="310" height="120" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<circle cx="85" cy="370" r="20" fill="#f1f5f9"/>
<text x="85" y="377" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">👨‍⚕️</text>
<text x="115" y="365" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Mr. Bilal Ahmed, M.Sc.</text>
<text x="115" y="381" font-family="Arial, sans-serif" font-size="10" fill="#64748b">Academic Performance &amp; Stress</text>
<text x="115" y="397" font-family="Arial, sans-serif" font-size="9" fill="#10b981">✓ CUI Verified Counselor</text>

<rect x="55" y="475" width="310" height="44" rx="8" fill="#1e3a8a"/>
<text x="210" y="502" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Confirm Free Booking (2:00 PM)</text>
'''
    write_wireframe("WF09_Counselor_Booking_Screen", mobile_frame("Figure 3.3.9: Counselor Directory & Booking Screen", inner_09), "WF09 Counselor Booking")

    # WF10: Peer Community Feed
    inner_10 = '''
<text x="55" y="90" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#0f172a">Student Community</text>
<text x="55" y="108" font-family="Arial, sans-serif" font-size="10" fill="#64748b">Peer support, coping strategies, safe space</text>

<!-- Community Post 1 -->
<rect x="55" y="130" width="310" height="160" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<circle cx="80" cy="155" r="14" fill="#e2e8f0"/>
<text x="80" y="160" font-family="Arial, sans-serif" font-size="11" text-anchor="middle">👤</text>
<text x="105" y="155" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Anonymous Student #402</text>
<text x="105" y="169" font-family="Arial, sans-serif" font-size="9" fill="#94a3b8">2 hours ago • Exams &amp; Stress</text>

<text x="70" y="195" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">Anyone else feeling overwhelmed by the 7th semester</text>
<text x="70" y="210" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">FYP deadlines? How are you guys managing sleep?</text>

<!-- Counselor Reply Inside Post -->
<rect x="70" y="225" width="280" height="50" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>
<text x="80" y="243" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#1e40af">Dr. Ayesha Tariq [VERIFIED COUNSELOR]:</text>
<text x="80" y="259" font-family="Arial, sans-serif" font-size="9" fill="#334155">Break tasks into 30m Pomodoro blocks. Prioritize 7h sleep!</text>

<!-- Post Action Bar -->
<text x="70" y="282" font-family="Arial, sans-serif" font-size="9" fill="#64748b">❤️ 24 Likes   💬 8 Replies   🚩 Report</text>

<!-- Community Post 2 -->
<rect x="55" y="305" width="310" height="110" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
<circle cx="80" cy="330" r="14" fill="#e2e8f0"/>
<text x="80" y="335" font-family="Arial, sans-serif" font-size="11" text-anchor="middle">👤</text>
<text x="105" y="330" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">CS Student Wah</text>
<text x="105" y="344" font-family="Arial, sans-serif" font-size="9" fill="#94a3b8">5 hours ago • Recovery Tips</text>
<text x="70" y="370" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">The 10-minute guided breathing audio in the app</text>
<text x="70" y="385" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">really helped lower my anxiety before my viva!</text>

<rect x="55" y="475" width="310" height="44" rx="8" fill="#1e3a8a"/>
<text x="210" y="502" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">+ Share Anonymous Experience</text>
'''
    write_wireframe("WF10_Peer_Community_Feed_Screen", mobile_frame("Figure 3.3.10: Peer Community Support Feed Screen", inner_10), "WF10 Community Feed Screen")

    print("All 10 UI Wireframes successfully generated!")

if __name__ == "__main__":
    build_all_wireframes()
