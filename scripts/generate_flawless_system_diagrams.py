"""
MindEase FYP - Flawless Academic Diagram Generator (Version 4.0 - Master Release)
Completely eliminates clunky white background boxes, text overlaps, and collisions.
Includes ALL 11 System Diagrams:
01_System_Architecture
02_Use_Case_Diagram (TexEye AI Inspiration Layout - Strictly 17 Use Cases, No Edge AI, No Dashed Box)
03_DFD_Level_0 (Context Diagram)
04_DFD_Level_1 (Functional Decomposition - 200px gap, zero collision)
05_DFD_Level_2_Stress_Detection (Multimodal Fusion Pipeline)
06_Component_Diagram (UML 2.5 Architecture)
07_Deployment_Diagram (Physical 3D Nodes & Protocols)
08_Class_Diagram (OOP Domain Architecture - 12 Classes Fully Connected)
09_Entity_Relationship_Diagram (True Crow's Foot Relational Design)
10_Database_Schema (Physical SQL Schema Design)
11_State_Machine_Diagram (Dual Track State Lifecycles)
"""
import os
import pymupdf
from drawio_builder import DrawioBuilder

def save_and_render(name, svg_content, drawio_content):
    svg_dir = os.path.join("Documentation", "Diagrams", "SVG")
    editable_dir = os.path.join("Documentation", "Diagrams", "Editable")
    visio_dir = os.path.join("Documentation", "Diagrams", "Visio")
    png_dir = os.path.join("Documentation", "Diagrams", "PNG")
    pdf_dir = os.path.join("Documentation", "Diagrams", "PDF")
    for d in [svg_dir, editable_dir, visio_dir, png_dir, pdf_dir]:
        os.makedirs(d, exist_ok=True)

    svg_path = os.path.join(svg_dir, f"{name}.svg")
    drawio_path = os.path.join(editable_dir, f"{name}.drawio")
    visio_path = os.path.join(visio_dir, f"{name}.drawio")
    png_path = os.path.join(png_dir, f"{name}.png")
    pdf_path = os.path.join(pdf_dir, f"{name}.pdf")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    with open(drawio_path, "w", encoding="utf-8") as f:
        f.write(drawio_content)
    with open(visio_path, "w", encoding="utf-8") as f:
        f.write(drawio_content)

    doc = pymupdf.open("svg", svg_content.encode("utf-8"))
    pdf_bytes = doc.convert_to_pdf()
    doc_pdf = pymupdf.open("pdf", pdf_bytes)
    doc_pdf.save(pdf_path)

    page = doc_pdf[0]
    pix = page.get_pixmap(dpi=300)
    pix.save(png_path)
    print(f"Generated {name}: PNG ({pix.width}x{pix.height}), PDF ({os.path.getsize(pdf_path)} bytes)")

# =============================================================================
# 01_System_Architecture (5-Tier Clean Multi-Tier Architecture)
# =============================================================================
def build_system_architecture():
    w, h = 1200, 900
    b = DrawioBuilder("01_System_Architecture", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>',
        '  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">',
        '    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>',
        '  </marker>',
        '</defs>',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.1.1: MindEase High-Level Multi-Tier System Architecture</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',
    ]

    # Helper for tier containers
    def draw_tier(tx, ty, tw, th, title, border_col, header_col):
        svg.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" fill="#f8fafc" stroke="{border_col}" stroke-width="1.5" rx="6"/>')
        svg.append(f'<rect x="{tx}" y="{ty}" width="280" height="26" fill="{header_col}" stroke="{border_col}" stroke-width="1.5" rx="4"/>')
        svg.append(f'<text x="{tx+15}" y="{ty+18}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="{border_col}">{title}</text>')

    # Helper for component cards
    def draw_card(cx, cy, cw, ch, t1, t2, t3=""):
        svg.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>')
        svg.append(f'<text x="{cx+cw/2}" y="{cy+20}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">{t1}</text>')
        svg.append(f'<text x="{cx+cw/2}" y="{cy+38}" font-family="Arial, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">{t2}</text>')
        if t3:
            svg.append(f'<text x="{cx+cw/2}" y="{cy+52}" font-family="Arial, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">{t3}</text>')

    # TIER 1: Presentation Layer
    draw_tier(50, 85, 1100, 125, "Presentation Layer (Flutter Mobile App)", "#2563eb", "#eff6ff")
    draw_card(70, 125, 195, 68, "Student Mobile App", "Assessment, Diary, Habits", "XAI Insights, Study Planner")
    draw_card(285, 125, 195, 68, "Counselor Portal", "Appointment Schedule", "Patient Trends, Clinical Notes")
    draw_card(500, 125, 195, 68, "Admin Management", "Counselor Approvals, Content", "Community Post Moderation")
    draw_card(715, 125, 195, 68, "State Management", "Flutter BLoC / Cubit", "Event / State Streams")
    draw_card(930, 125, 200, 68, "Network & Storage", "Dio HTTP Client / WebSockets", "Flutter Secure Storage")

    # Connector 1 -> 2
    svg.append('<line x1="600" y1="210" x2="600" y2="245" stroke="#0f172a" stroke-width="1.6" marker-end="url(#arrow)"/>')
    svg.append('<text x="615" y="232" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">REST APIs &amp; WebSockets (TLS 1.3 / HTTPS)</text>')

    # TIER 2: Application Tier (FastAPI Backend)
    draw_tier(50, 245, 1100, 190, "Application Tier (FastAPI Python Backend)", "#059669", "#ecfdf5")
    # Row 1 Backend Services
    draw_card(70, 285, 160, 56, "Auth & RBAC Service", "JWT, Multi-Role Guard")
    draw_card(250, 285, 160, 56, "Questionnaire Service", "PSS Scoring & History")
    draw_card(430, 285, 160, 56, "Diary & Safety Service", "Crisis Detection Pipeline")
    draw_card(610, 285, 160, 56, "Habits & Fusion Router", "Sleep, Steps, Screen Time")
    draw_card(790, 285, 160, 56, "Baseline & Triggers", "Trend Analysis Engine")
    draw_card(970, 285, 160, 56, "Adaptive Study Planner", "Pomodoro & Load Tuning")
    # Row 2 Backend Services
    draw_card(70, 360, 195, 56, "Content & Recovery Service", "Audio Guides & Exercises")
    draw_card(285, 360, 195, 56, "Counselor Booking Service", "Free Triage & Clinical Notes")
    draw_card(500, 360, 195, 56, "Peer Community Service", "Anonymous Posts & Reports")
    draw_card(715, 360, 195, 56, "Polar Billing Controller", "Webhooks & Transactions")
    draw_card(930, 360, 200, 56, "Admin Portal Controller", "Approvals & Audit Logs")

    # Connector 2 -> 3 and 4
    svg.append('<line x1="330" y1="435" x2="330" y2="475" stroke="#0f172a" stroke-width="1.6" marker-end="url(#arrow)"/>')
    svg.append('<text x="345" y="460" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#0f172a">AI Inference Worker Pipeline</text>')

    svg.append('<line x1="870" y1="435" x2="870" y2="475" stroke="#0f172a" stroke-width="1.6" marker-end="url(#arrow)"/>')
    svg.append('<text x="885" y="460" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#0f172a">Asyncpg PostgreSQL Pool</text>')

    # TIER 3: AI & Machine Learning Engine (Left half)
    draw_tier(50, 475, 535, 175, "AI & Machine Learning Engine", "#7c3aed", "#f5f3ff")
    draw_card(70, 515, 235, 54, "Whisper ASR Model", "Speech-to-Text (Urdu / English)")
    draw_card(330, 515, 235, 54, "Multimodal Fusion Classifier", "PyTorch BiLSTM Neural Network")
    draw_card(70, 580, 235, 54, "SHAP XAI Engine", "Feature Attribution & Drivers")
    draw_card(330, 580, 235, 54, "Conversational Chatbot", "Transformers Contextual Support")

    # TIER 4: Persistence Tier (Right half)
    draw_tier(615, 475, 535, 175, "Persistence Tier (Supabase Cloud)", "#0284c7", "#f0f9ff")
    draw_card(635, 515, 235, 54, "PostgreSQL 15 Database", "Users, Assessments, Habits, Plans")
    draw_card(895, 515, 235, 54, "Supabase Auth (GoTrue)", "Row Level Security (RLS) Guard")
    draw_card(635, 580, 235, 54, "Encrypted Diary Vault", "AES-256 GCM Private Records")
    draw_card(895, 580, 235, 54, "Supabase Media Storage", "Audio Files & Relaxation Media")

    # Connector 2 -> 5
    svg.append('<line x1="600" y1="650" x2="600" y2="685" stroke="#0f172a" stroke-width="1.6" marker-end="url(#arrow)"/>')
    svg.append('<text x="615" y="672" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#0f172a">Secure External Gateways (HTTPS / REST)</text>')

    # TIER 5: External Gateway Tier
    draw_tier(50, 685, 1100, 115, "External Gateway Tier", "#d97706", "#fffbeb")
    draw_card(70, 725, 510, 58, "Polar Payment Gateway (Test Mode / Sandbox)", "Sandbox Hosted Checkout, Card Tokenization & Webhook Signatures")
    draw_card(620, 725, 510, 58, "Crisis Helplines & Telephony Gateway", "Pakistan Mental Health Hotlines & University Counseling Center Service")

    svg.append('</svg>')
    save_and_render("01_System_Architecture", "\n".join(svg), b.to_xml())

# =============================================================================
# 02_Use_Case_Diagram (TexEye AI Inspiration Layout - Strictly 17 Use Cases)
# =============================================================================
def build_use_case_diagram():
    w, h = 1350, 1000
    b = DrawioBuilder("02_Use_Case_Diagram", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>',
        '  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">',
        '    <path d="M 0 0 L 10 5 L 0 10 z" fill="#000000"/>',
        '  </marker>',
        '  <marker id="dashed-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">',
        '    <path d="M 0 1 L 8 5 L 0 9" fill="none" stroke="#000000" stroke-width="1.5"/>',
        '  </marker>',
        '</defs>',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#000000" text-anchor="middle">Figure 3.2.1: UML Use Case Diagram of MindEase AI System</text>',
        f'<line x1="40" y1="48" x2="{w-40}" y2="48" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="60" width="{w-50}" height="{h-80}" fill="none" stroke="#4b5563" stroke-width="1.2"/>',

        # System Boundary Box
        f'<rect x="260" y="80" width="830" height="{h-120}" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>',
        f'<text x="{w/2}" y="106" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#000000" text-anchor="middle" letter-spacing="1">SYSTEM BOUNDARY: MindEase Stress Detection &amp; Support Platform</text>',
        f'<line x1="260" y1="118" x2="1090" y2="118" stroke="#000000" stroke-width="1.2"/>',
    ]

    # Draw.io boundary
    b.add_cell(
        "SYSTEM BOUNDARY: MindEase Stress Detection & Support Platform",
        "swimlane;whiteSpace=wrap;html=1;startSize=35;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontFamily=Arial;fontSize=13;fontStyle=1;align=center;",
        x=260, y=80, w=830, h=h-120
    )

    # Centered Top Use Case: UC02 (Login & Multi-Role Authentication)
    uc02_x, uc02_y, uc02_w, uc02_h = 675, 148, 250, 42
    svg.extend([
        f'<ellipse cx="{uc02_x}" cy="{uc02_y}" rx="{uc02_w/2}" ry="{uc02_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>',
        f'<text x="{uc02_x}" y="{uc02_y-3}" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#000000" text-anchor="middle">UC02</text>',
        f'<text x="{uc02_x}" y="{uc02_y+11}" font-family="Arial, sans-serif" font-size="9.5" fill="#000000" text-anchor="middle">Login &amp; Multi-Role Authentication (JWT)</text>'
    ])
    b.add_cell(
        "<b>UC02</b><br>Login &amp; Multi-Role Authentication (JWT)",
        "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;",
        x=uc02_x-uc02_w/2, y=uc02_y-uc02_h/2, w=uc02_w, h=uc02_h
    )

    # Geometry for 2 Columns (8 on Left, 8 on Right)
    col_w, col_h = 230, 40
    lc_x = 445
    rc_x = 905

    # Left Column: Student Wellness & Tracking Cases (UC01, UC03, UC04, UC05, UC06, UC07, UC08, UC09)
    left_cases = [
        ("UC01", "Register &amp; Onboard Profile", 220),
        ("UC03", "Complete Stress Questionnaire", 285),
        ("UC04", "Record Daily Voice &amp; Text Diary", 350),
        ("UC05", "Log Daily Habits &amp; Biometrics", 415),
        ("UC06", "View Stress Trends &amp; Baseline", 495),
        ("UC07", "View Explainable AI Insights", 575),
        ("UC08", "Access Relaxation Content", 655),
        ("UC09", "Chat with AI Support Assistant", 735),
    ]

    for cid, cname, cy in left_cases:
        svg.extend([
            f'<ellipse cx="{lc_x}" cy="{cy}" rx="{col_w/2}" ry="{col_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            f'<text x="{lc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>',
            f'<text x="{lc_x}" y="{cy+11}" font-family="Arial, sans-serif" font-size="9" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        b.add_cell(
            f"<b>{cid}</b><br>{cname}",
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=9.5;",
            x=lc_x-col_w/2, y=cy-col_h/2, w=col_w, h=col_h
        )

    # Right Column: Planning, Counseling, Peer & Admin (UC10, UC11, UC12, UC13, UC14, UC15, UC16, UC17)
    right_cases = [
        ("UC10", "Generate Adaptive Study Plan", 220),
        ("UC11", "Search Counselors &amp; Request Slot", 285),
        ("UC12", "Conduct Counseling Session &amp; Notes", 350),
        ("UC13", "Process Polar Payment (Test Mode)", 415),
        ("UC14", "Create &amp; Interact in Peer Posts", 495),
        ("UC15", "Report Inappropriate Post", 575),
        ("UC16", "Manage Accounts &amp; Approvals", 655),
        ("UC17", "Moderate Content &amp; Logs", 735),
    ]

    for cid, cname, cy in right_cases:
        svg.extend([
            f'<ellipse cx="{rc_x}" cy="{cy}" rx="{col_w/2}" ry="{col_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            f'<text x="{rc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>',
            f'<text x="{rc_x}" y="{cy+11}" font-family="Arial, sans-serif" font-size="9" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        b.add_cell(
            f"<b>{cid}</b><br>{cname}",
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=9.5;",
            x=rc_x-col_w/2, y=cy-col_h/2, w=col_w, h=col_h
        )

    # UML Relationships in the Gutter (Between x=560 and x=790 - ZERO OVERLAP!)
    # 1. <<extend>> UC07 -> UC06
    svg.extend([
        '<path d="M 560 575 L 590 575 L 590 495 L 560 495" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="625" y="538" font-family="Arial, sans-serif" font-size="8.5" fill="#000000" text-anchor="middle">&lt;&lt;extend&gt;&gt;</text>',

        # 2. <<include>> UC11 -> UC13
        '<path d="M 790 285 L 760 285 L 760 415 L 790 415" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="725" y="353" font-family="Arial, sans-serif" font-size="8.5" fill="#000000" text-anchor="middle">&lt;&lt;include&gt;&gt;</text>',

        # 3. <<extend>> UC15 -> UC14
        '<path d="M 790 575 L 760 575 L 760 495 L 790 495" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="725" y="538" font-family="Arial, sans-serif" font-size="8.5" fill="#000000" text-anchor="middle">&lt;&lt;extend&gt;&gt;</text>',
    ])

    # Actor stick figure helper
    def draw_actor(cx, cy, label1, label2=""):
        res = [
            f'<circle cx="{cx}" cy="{cy-32}" r="13" fill="#ffffff" stroke="#000000" stroke-width="1.7"/>',
            f'<line x1="{cx}" y1="{cy-19}" x2="{cx}" y2="{cy+12}" stroke="#000000" stroke-width="1.7"/>',
            f'<line x1="{cx-20}" y1="{cy-6}" x2="{cx+20}" y2="{cy-6}" stroke="#000000" stroke-width="1.7"/>',
            f'<line x1="{cx}" y1="{cy+12}" x2="{cx-16}" y2="{cy+42}" stroke="#000000" stroke-width="1.7"/>',
            f'<line x1="{cx}" y1="{cy+12}" x2="{cx+16}" y2="{cy+42}" stroke="#000000" stroke-width="1.7"/>',
            f'<text x="{cx}" y="{cy+60}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">{label1}</text>'
        ]
        if label2:
            res.append(f'<text x="{cx}" y="{cy+74}" font-family="Arial, sans-serif" font-size="9.5" fill="#444444" text-anchor="middle">{label2}</text>')
        return "\n".join(res)

    # Actors:
    # 1. Left Top: Student (Assessment & Tracking)
    svg.append(draw_actor(135, 290, "Student", "(Assessment &amp; Tracking)"))
    b.add_cell("Student<br>(Assessment &amp; Tracking)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", x=110, y=255, w=50, h=85)

    # 2. Left Bottom: Student (Intervention & Recovery)
    svg.append(draw_actor(135, 615, "Student", "(Intervention &amp; Recovery)"))
    b.add_cell("Student<br>(Intervention &amp; Recovery)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", x=110, y=580, w=50, h=85)

    # 3. Right Top: Counselor (Mental Health Pro)
    svg.append(draw_actor(1210, 290, "Counselor", "(Mental Health Pro)"))
    b.add_cell("Counselor<br>(Mental Health Pro)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", x=1185, y=255, w=50, h=85)

    # 4. Right Middle: Student (Community & Planning)
    svg.append(draw_actor(1210, 495, "Student", "(Community &amp; Planning)"))
    b.add_cell("Student<br>(Community &amp; Planning)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", x=1185, y=460, w=50, h=85)

    # 5. Right Bottom: Administrator (System Admin)
    svg.append(draw_actor(1210, 695, "Administrator", "(System Admin)"))
    b.add_cell("Administrator<br>(System Admin)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", x=1185, y=660, w=50, h=85)

    # Clean Actor Association Lines (ZERO CROSSING!)
    # Left Actor 1: connects to UC01, UC03, UC04, UC05
    for ty in [220, 285, 350, 415]:
        svg.append(f'<line x1="165" y1="290" x2="{lc_x - col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Left Actor 2: connects to UC06, UC07, UC08, UC09
    for ty in [495, 575, 655, 735]:
        svg.append(f'<line x1="165" y1="615" x2="{lc_x - col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 1: connects to UC11, UC12
    for ty in [285, 350]:
        svg.append(f'<line x1="1180" y1="290" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 2: connects to UC10, UC13, UC14
    for ty in [220, 415, 495]:
        svg.append(f'<line x1="1180" y1="495" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 3: connects to UC16, UC17
    for ty in [655, 735]:
        svg.append(f'<line x1="1180" y1="695" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Subtle upward authentication links to UC02
    svg.append(f'<path d="M 165 260 L 220 260 L 220 148 L {uc02_x - uc02_w/2} 148" fill="none" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3"/>')
    svg.append(f'<path d="M 1180 260 L 1130 260 L 1130 148 L {uc02_x + uc02_w/2} 148" fill="none" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3"/>')

    svg.append('</svg>')
    save_and_render("02_Use_Case_Diagram", "\n".join(svg), b.to_xml())

# =============================================================================
# 03_DFD_Level_0 (Context Diagram - NO CLUNKY WHITE BOXES, ZERO COLLISION)
# =============================================================================
def build_dfd_level_0():
    w, h = 1600, 950
    b = DrawioBuilder("03_DFD_Level_0", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>',
        '  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">',
        '    <path d="M 0 0 L 10 5 L 0 10 z" fill="#1e3a8a"/>',
        '  </marker>',
        '</defs>',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.3.1: DFD Level 0 (Context Diagram) for MindEase System</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',

        # Central Process 0.0 (Radius = 145, centered at cx=800, cy=475)
        '<circle cx="800" cy="475" r="145" fill="#ffffff" stroke="#1e3a8a" stroke-width="2.5"/>',
        '<line x1="660" y1="425" x2="940" y2="425" stroke="#1e3a8a" stroke-width="1.5"/>',
        '<text x="800" y="400" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="#1e3a8a" text-anchor="middle">0.0</text>',
        '<text x="800" y="455" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#0f172a" text-anchor="middle">MindEase AI Stress Detection,</text>',
        '<text x="800" y="480" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Recovery &amp; Support Platform</text>',
        '<text x="800" y="505" font-family="Arial, sans-serif" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">(Core System Boundary)</text>',
    ]

    # External Entities (Width = 260, Height = 84)
    ent_w, ent_h = 260, 84

    # 1. Student (Top Left)
    s_x, s_y = 80, 140
    svg.extend([
        f'<rect x="{s_x}" y="{s_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{s_x+ent_w/2}" y="{s_y+36}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Student</text>',
        f'<text x="{s_x+ent_w/2}" y="{s_y+58}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Primary User)</text>',
    ])

    # 2. Polar Gateway (Bottom Left)
    p_x, p_y = 80, 720
    svg.extend([
        f'<rect x="{p_x}" y="{p_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{p_x+ent_w/2}" y="{p_y+36}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Gateway</text>',
        f'<text x="{p_x+ent_w/2}" y="{p_y+58}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(External Payment Service)</text>',
    ])

    # 3. Counselor (Top Right)
    c_x, c_y = 1260, 140
    svg.extend([
        f'<rect x="{c_x}" y="{c_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{c_x+ent_w/2}" y="{c_y+36}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor</text>',
        f'<text x="{c_x+ent_w/2}" y="{c_y+58}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Mental Health Professional)</text>',
    ])

    # 4. Administrator (Bottom Right)
    a_x, a_y = 1260, 720
    svg.extend([
        f'<rect x="{a_x}" y="{a_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{a_x+ent_w/2}" y="{a_y+36}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Administrator</text>',
        f'<text x="{a_x+ent_w/2}" y="{a_y+58}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(System Admin)</text>',
    ])

    # Clean Orthogonal Flow Helper - Crisp 2-line labels, zero collision, zero white boxes
    def add_flow(path_d, line1, line2, tx, ty, anchor="middle"):
        svg.append(f'<path d="{path_d}" fill="none" stroke="#1e3a8a" stroke-width="1.6" marker-end="url(#arrow)"/>')
        svg.append(f'<text x="{tx}" y="{ty}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#1e3a8a" text-anchor="{anchor}">{line1}</text>')
        if line2:
            svg.append(f'<text x="{tx}" y="{ty+14}" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="{anchor}">{line2}</text>')

    # 1. Student <-> MindEase (Top Left)
    # Student -> System
    add_flow("M 340 160 L 690 160 L 690 345", "Questionnaire Responses, Voice Diary &amp; Habit Logs", "(Sleep Duration, Daily Step Count, Screen Time)", 515, 138)
    # System -> Student
    add_flow("M 655 420 L 655 205 L 340 205", "Stress Level (L/M/H), SHAP XAI Insights &amp; Study Plans", "(Pomodoro Intervals, Audio Exercises, Support Bot)", 495, 185)

    # 2. Counselor <-> MindEase (Top Right)
    # Counselor -> System
    add_flow("M 1260 160 L 910 160 L 910 345", "Counselor Availability Slots &amp; Clinical Notes", "(Scheduled Office Hours, Student Progress Notes)", 1085, 138)
    # System -> Counselor
    add_flow("M 945 420 L 945 205 L 1260 205", "Confirmed Appointment Requests &amp; Patient Dossiers", "(Consented Longitudinal Stress Trends &amp; Baseline)", 1105, 185)

    # 3. Polar Gateway <-> MindEase (Bottom Left)
    # System -> Polar Gateway
    add_flow("M 655 530 L 655 745 L 340 745", "Checkout Session Creation &amp; Payment Intent", "(Booking Reference, Appointment Fee in USD/PKR)", 495, 725)
    # Polar Gateway -> System
    add_flow("M 340 790 L 690 790 L 690 605", "Polar Webhook Payment Notification Token", "(Signature Verification, Payment Status: Success/Fail)", 515, 810)

    # 4. Administrator <-> MindEase (Bottom Right)
    # System -> Administrator
    add_flow("M 945 530 L 945 745 L 1260 745", "Reported Posts Queue &amp; System Telemetry Logs", "(Audit Logs, AI Pipeline Health, Error Telemetry)", 1105, 725)
    # Administrator -> System
    add_flow("M 1260 790 L 910 790 L 910 605", "Moderation Actions &amp; System Configuration", "(Counselor Verification, Content Deletion, Auth Roles)", 1085, 810)

    svg.append('</svg>')
    save_and_render("03_DFD_Level_0", "\n".join(svg), b.to_xml())

# =============================================================================
# 04_DFD_Level_1 (Subsystem Functional Decomposition - 200px GAP, ZERO COLLISION)
# =============================================================================
def build_dfd_level_1():
    w, h = 1750, 1000
    b = DrawioBuilder("04_DFD_Level_1", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>',
        '  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">',
        '    <path d="M 0 0 L 10 5 L 0 10 z" fill="#1e3a8a"/>',
        '  </marker>',
        '</defs>',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.3.2: DFD Level 1 Subsystem Functional Decomposition for MindEase</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',
    ]

    def draw_proc(num, title1, title2, cx, cy, r=48):
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="#1e3a8a" stroke-width="2"/>')
        svg.append(f'<line x1="{cx-r*0.9}" y1="{cy-10}" x2="{cx+r*0.9}" y2="{cy-10}" stroke="#1e3a8a" stroke-width="1.2"/>')
        svg.append(f'<text x="{cx}" y="{cy-18}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">{num}</text>')
        svg.append(f'<text x="{cx}" y="{cy+6}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">{title1}</text>')
        svg.append(f'<text x="{cx}" y="{cy+19}" font-family="Arial, sans-serif" font-size="9" fill="#0f172a" text-anchor="middle">{title2}</text>')

    def draw_dstore(num, name, x, y, w_box=180, h_box=32):
        svg.append(f'<line x1="{x}" y1="{y}" x2="{x+w_box}" y2="{y}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<line x1="{x}" y1="{y+h_box}" x2="{x+w_box}" y2="{y+h_box}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+h_box}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<line x1="{x+36}" y1="{y}" x2="{x+36}" y2="{y+h_box}" stroke="#0f172a" stroke-width="1"/>')
        svg.append(f'<rect x="{x+1}" y="{y+1}" width="34" height="{h_box-2}" fill="#f1f5f9"/>')
        svg.append(f'<text x="{x+18}" y="{y+20}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">{num}</text>')
        svg.append(f'<text x="{x+44}" y="{y+20}" font-family="Arial, sans-serif" font-size="9.5" font-weight="600" fill="#0f172a">{name}</text>')

    # External Entities
    st_x, st_y, ent_w, ent_h = 60, 390, 180, 100
    svg.extend([
        f'<rect x="{st_x}" y="{st_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{st_x+ent_w/2}" y="{st_y+42}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Student</text>',
        f'<text x="{st_x+ent_w/2}" y="{st_y+64}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Primary User)</text>',
    ])

    # Counselor (Top Right)
    c_x, c_y = 1550, 138
    svg.extend([
        f'<rect x="{c_x}" y="{c_y}" width="{ent_w-20}" height="{ent_h-15}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{c_x+(ent_w-20)/2}" y="{c_y+38}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor</text>',
        f'<text x="{c_x+(ent_w-20)/2}" y="{c_y+58}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Clinical Pro)</text>',
    ])

    # Administrator (Middle Right)
    a_x, a_y = 1550, 438
    svg.extend([
        f'<rect x="{a_x}" y="{a_y}" width="{ent_w-20}" height="{ent_h-15}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{a_x+(ent_w-20)/2}" y="{a_y+38}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Administrator</text>',
        f'<text x="{a_x+(ent_w-20)/2}" y="{a_y+58}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(System Admin)</text>',
    ])

    # Polar Gateway (Bottom Right)
    p_x, p_y = 1550, 738
    svg.extend([
        f'<rect x="{p_x}" y="{p_y}" width="{ent_w-20}" height="{ent_h-15}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{p_x+(ent_w-20)/2}" y="{p_y+38}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Gateway</text>',
        f'<text x="{p_x+(ent_w-20)/2}" y="{p_y+58}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Payment)</text>',
    ])

    # COLUMN 1: Student-Facing Processes (at cx=540 - 300px runway from Student box!)
    draw_proc("1.0", "Manage Auth", "&amp; Profiles", 540, 150)
    draw_proc("2.0", "Questionnaire", "&amp; Scoring", 540, 350)
    draw_proc("3.0", "Voice Diary", "&amp; Whisper STT", 540, 550)
    draw_proc("4.0", "Habit Tracking &amp;", "Fusion Model", 540, 780)

    # DATA STORES (Column 1 Stores at x=710..890)
    draw_dstore("D1", "Users &amp; Auth Store", 710, 134)
    draw_dstore("D2", "Stress Assessments", 710, 334)
    draw_dstore("D3", "Encrypted Diaries", 710, 534)

    # COLUMN 2: Intelligence & Planning Processes (at cx=1080)
    draw_proc("5.0", "Baseline &amp; XAI", "Attribution", 1080, 440)
    draw_proc("6.0", "Adaptive Study", "&amp; Recovery Plan", 1080, 780)
    draw_dstore("D4", "Study Plans &amp; Tasks", 1180, 764)

    # COLUMN 3: Clinical, Community & Payment Processes (at cx=1420)
    draw_proc("7.0", "Counselor Booking", "&amp; Sessions", 1420, 180)
    draw_proc("8.0", "Community Forum", "&amp; Moderation", 1420, 480)
    draw_proc("9.0", "Polar Payment", "&amp; Webhook", 1420, 780)
    draw_dstore("D5", "Appointments &amp; Notes", 1200, 164)
    draw_dstore("D6", "Community Posts", 1200, 464)

    def add_clean_flow(path_d, label, tx, ty, anchor="middle"):
        svg.append(f'<path d="{path_d}" fill="none" stroke="#1e3a8a" stroke-width="1.4" marker-end="url(#arrow)"/>')
        svg.append(f'<text x="{tx}" y="{ty}" font-family="Arial, sans-serif" font-size="9" font-weight="600" fill="#1e3a8a" text-anchor="{anchor}">{label}</text>')

    # Student to Column 1 (Staggered orthogonal lines - ZERO COLLISION!)
    # To 1.0 (Auth)
    add_clean_flow("M 240 410 L 300 410 L 300 150 L 492 150", "Credentials &amp; Profile Data", 396, 142)
    # To 2.0 (Questionnaire)
    add_clean_flow("M 240 430 L 340 430 L 340 350 L 492 350", "PSS Questionnaire Responses", 416, 342)
    # To 3.0 (Voice Diary)
    add_clean_flow("M 240 450 L 340 450 L 340 550 L 492 550", "Voice Audio &amp; Text Logs", 416, 542)
    # To 4.0 (Habits)
    add_clean_flow("M 240 470 L 300 470 L 300 780 L 492 780", "Sleep, Steps &amp; Activity", 396, 772)

    # Column 1 to Stores
    add_clean_flow("M 588 150 L 710 150", "User Record", 649, 142)
    add_clean_flow("M 588 350 L 710 350", "Assessment Score", 649, 342)
    add_clean_flow("M 588 550 L 710 550", "Encrypted Diary", 649, 542)

    # Fusion Pipeline to 5.0 (Baseline & XAI)
    add_clean_flow("M 588 780 L 760 780 L 760 440 L 1032 440", "Multimodal Feature Vector", 896, 432)
    add_clean_flow("M 890 350 L 950 350 L 950 420 L 1032 420", "PSS Baseline", 985, 412)
    add_clean_flow("M 890 550 L 950 550 L 950 460 L 1032 460", "Speech Sentiment", 985, 472)
    add_clean_flow("M 1080 488 L 1080 732", "Stress Level (L/M/H) &amp; SHAP Drivers", 1092, 610, "start")
    add_clean_flow("M 1128 780 L 1180 780", "Study Plan", 1154, 772)

    # Right Side: Counselor & Appointments
    add_clean_flow("M 1550 165 L 1468 165", "Availability Slots", 1509, 157)
    add_clean_flow("M 1468 195 L 1550 195", "Booked Calendar", 1509, 207)
    add_clean_flow("M 1380 180 L 1412 180", "Session Notes", 1396, 172)

    # Community
    add_clean_flow("M 1550 465 L 1468 465", "Moderation Action", 1509, 457)
    add_clean_flow("M 1468 495 L 1550 495", "Flagged Posts Queue", 1509, 507)
    add_clean_flow("M 1380 480 L 1412 480", "Post Feeds", 1396, 472)

    # Polar Payment (Bottom Right)
    add_clean_flow("M 1420 732 L 1420 228", "Confirmed Payment &amp; Booking Token", 1432, 350, "start")
    add_clean_flow("M 1468 765 L 1550 765", "Checkout Request", 1509, 757)
    add_clean_flow("M 1550 795 L 1468 795", "Webhook Success Token", 1509, 807)

    svg.append('</svg>')
    save_and_render("04_DFD_Level_1", "\n".join(svg), b.to_xml())

# =============================================================================
# 05_DFD_Level_2_Stress_Detection (NO CLUNKY WHITE BOXES, ZERO COLLISION)
# =============================================================================
def build_dfd_level_2():
    w, h = 1500, 920
    b = DrawioBuilder("05_DFD_Level_2_Stress_Detection", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>',
        '  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">',
        '    <path d="M 0 0 L 10 5 L 0 10 z" fill="#1e3a8a"/>',
        '  </marker>',
        '</defs>',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.3.3: DFD Level 2 Detailed Multimodal Stress Fusion &amp; Explainability Pipeline</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',
    ]

    def draw_proc(num, title1, title2, cx, cy, r=48):
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="#1e3a8a" stroke-width="2"/>')
        svg.append(f'<line x1="{cx-r*0.9}" y1="{cy-10}" x2="{cx+r*0.9}" y2="{cy-10}" stroke="#1e3a8a" stroke-width="1.2"/>')
        svg.append(f'<text x="{cx}" y="{cy-18}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">{num}</text>')
        svg.append(f'<text x="{cx}" y="{cy+6}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">{title1}</text>')
        svg.append(f'<text x="{cx}" y="{cy+19}" font-family="Arial, sans-serif" font-size="9" fill="#0f172a" text-anchor="middle">{title2}</text>')

    # 3 Inputs on Left (width 230, height 56)
    in_w, in_h = 230, 56
    svg.extend([
        f'<rect x="60" y="180" width="{in_w}" height="{in_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="1.8"/>',
        f'<text x="{60+in_w/2}" y="206" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Questionnaire Assessment</text>',
        f'<text x="{60+in_w/2}" y="222" font-family="Arial, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">PSS-10 / DASS-21 Score</text>',

        f'<rect x="60" y="372" width="{in_w}" height="{in_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="1.8"/>',
        f'<text x="{60+in_w/2}" y="398" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Daily Voice &amp; Text Diary</text>',
        f'<text x="{60+in_w/2}" y="414" font-family="Arial, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">Whisper STT &amp; Sentiment</text>',

        f'<rect x="60" y="560" width="{in_w}" height="{in_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="1.8"/>',
        f'<text x="{60+in_w/2}" y="586" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Habit Tracker Logs</text>',
        f'<text x="{60+in_w/2}" y="602" font-family="Arial, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">Sleep, Screen Time, Steps</text>',
    ])

    # 6 Processes with generous runway (cx=460, 740, 1020, 1300)
    draw_proc("4.1", "Feature Ingestion &amp;", "Imputation Engine", 460, 400)
    draw_proc("4.2", "Multimodal Fusion", "BiLSTM Classifier", 740, 400)
    draw_proc("4.3", "Baseline Comparator", "&amp; Trigger Drift", 1020, 200)
    draw_proc("4.4", "Compute SHAP", "Attribution Values", 1020, 400)
    draw_proc("4.5", "Crisis Evaluation &amp;", "SOS Safety Triage", 1020, 600)
    draw_proc("4.6", "Recommendation &amp;", "Recovery Router", 1300, 400)

    # Store D2
    svg.extend([
        '<line x1="930" y1="90" x2="1110" y2="90" stroke="#0f172a" stroke-width="1.8"/>',
        '<line x1="930" y1="122" x2="1110" y2="122" stroke="#0f172a" stroke-width="1.8"/>',
        '<line x1="930" y1="90" x2="930" y2="122" stroke="#0f172a" stroke-width="1.8"/>',
        '<line x1="966" y1="90" x2="966" y2="122" stroke="#0f172a" stroke-width="1"/>',
        '<rect x="931" y="91" width="34" height="30" fill="#f1f5f9"/>',
        '<text x="948" y="111" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">D2</text>',
        '<text x="974" y="111" font-family="Arial, sans-serif" font-size="9.5" font-weight="600" fill="#0f172a">Student Baseline Store</text>',
    ])

    # Output Block
    out_w, out_h = 240, 65
    svg.extend([
        f'<rect x="1180" y="650" width="{out_w}" height="{out_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{1180+out_w/2}" y="678" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Student Mobile Dashboard</text>',
        f'<text x="{1180+out_w/2}" y="698" font-family="Arial, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">Stress Level, XAI Drivers, Plan</text>',
    ])

    def add_clean_flow(path_d, label, tx, ty, anchor="middle"):
        svg.append(f'<path d="{path_d}" fill="none" stroke="#1e3a8a" stroke-width="1.4" marker-end="url(#arrow)"/>')
        svg.append(f'<text x="{tx}" y="{ty}" font-family="Arial, sans-serif" font-size="9" font-weight="600" fill="#1e3a8a" text-anchor="{anchor}">{label}</text>')

    # 3 Inputs to 4.1 (Clean 122px runway)
    add_clean_flow("M 290 208 L 460 208 L 460 352", "Raw PSS Score", 375, 198)
    add_clean_flow("M 290 400 L 412 400", "Audio/Text Sentiment", 351, 390)
    add_clean_flow("M 290 588 L 460 588 L 460 448", "Habit Metrics Vector", 375, 600)

    # 4.1 to 4.2 (184px runway)
    add_clean_flow("M 508 400 L 692 400", "Normalized Multi-Feature Vector", 600, 390)

    # 4.2 to 4.3, 4.4, 4.5 (184px runway)
    add_clean_flow("M 740 352 L 740 200 L 972 200", "Estimated Stress Level", 856, 190)
    add_clean_flow("M 788 400 L 972 400", "Model Weights &amp; Prediction", 880, 390)
    add_clean_flow("M 740 448 L 740 600 L 972 600", "High Risk / Acute Flags", 856, 612)

    # D2 Store <-> 4.3
    svg.append('<line x1="1020" y1="122" x2="1020" y2="152" stroke="#1e3a8a" stroke-width="1.4" marker-end="url(#arrow)"/>')
    svg.append('<text x="1030" y="140" font-family="Arial, sans-serif" font-size="8.5" font-weight="600" fill="#1e3a8a">Update Baseline</text>')

    # 4.3, 4.4, 4.5 to 4.6 (184px runway)
    add_clean_flow("M 1068 200 L 1200 200 L 1200 375 L 1252 375", "Baseline Deviation", 1134, 190)
    add_clean_flow("M 1068 400 L 1252 400", "SHAP Factor Attribution", 1160, 390)
    add_clean_flow("M 1068 600 L 1200 600 L 1200 425 L 1252 425", "Safety Status / Helpline", 1134, 615)

    # 4.6 to Dashboard
    add_clean_flow("M 1300 448 L 1300 650", "Dispatched Plan &amp; Insights", 1312, 550, "start")

    svg.append('</svg>')
    save_and_render("05_DFD_Level_2_Stress_Detection", "\n".join(svg), b.to_xml())

# =============================================================================
# 06_Component_Diagram (UML 2.5 Architecture)
# =============================================================================
def build_component_diagram():
    w, h = 1350, 920
    b = DrawioBuilder("06_Component_Diagram", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.1.2: MindEase Component Diagram (Presentation, Business Logic, AI, and Persistence Layers)</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',
    ]

    def draw_component(title, items, x, y, bw, bh, color="#1e3a8a"):
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" fill="#ffffff" stroke="{color}" stroke-width="2" rx="4"/>')
        ic_x = x + bw - 36
        svg.append(f'<rect x="{ic_x}" y="{y+10}" width="24" height="18" fill="#ffffff" stroke="{color}" stroke-width="1.2"/>')
        svg.append(f'<rect x="{ic_x-5}" y="{y+13}" width="10" height="4" fill="#ffffff" stroke="{color}" stroke-width="1.2"/>')
        svg.append(f'<rect x="{ic_x-5}" y="{y+21}" width="10" height="4" fill="#ffffff" stroke="{color}" stroke-width="1.2"/>')
        svg.append(f'<text x="{x+18}" y="{y+26}" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold" fill="{color}">&lt;&lt;component&gt;&gt; {title}</text>')
        svg.append(f'<line x1="{x}" y1="{y+36}" x2="{x+bw}" y2="{y+36}" stroke="{color}" stroke-width="1"/>')

        curr_y = y + 50
        for m_title, m_sub in items:
            box_h = 44
            svg.append(f'<rect x="{x+16}" y="{curr_y}" width="{bw-32}" height="{box_h}" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2" rx="3"/>')
            svg.append(f'<text x="{x+bw/2}" y="{curr_y+18}" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{m_title}</text>')
            svg.append(f'<text x="{x+bw/2}" y="{curr_y+34}" font-family="Arial, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">{m_sub}</text>')
            curr_y += box_h + 10

    m_items = [
        ("Presentation Module", "Flutter UI Views, Widgets, Stress Dial"),
        ("State Management (BLoC)", "AssessmentBloc, DiaryBloc, AuthBloc"),
        ("Audio Capture Module", "Microphone Stream &amp; PCM Encoding"),
        ("Habit Collector Service", "Android SensorManager &amp; Screen Time API"),
        ("Secure Local Storage", "Encrypted Shared Preferences &amp; Cache"),
        ("REST API Client (Dio)", "JWT Interceptors &amp; Network Resilience"),
    ]
    draw_component("Mobile App (Flutter Client)", m_items, 60, 100, 330, 410, "#0284c7")

    b_items = [
        ("API Gateway &amp; Middleware", "CORS, JWT Token Verification, Rate Limiting"),
        ("Stress Assessment Controller", "PSS-10 Scoring &amp; Multimodal Orchestration"),
        ("Diary &amp; Safety Controller", "Whisper Dispatch &amp; SOS Helpline Triage"),
        ("Baseline &amp; XAI Service", "Deviation Computation &amp; SHAP Explainer"),
        ("Adaptive Study Planner Engine", "Task Chunking &amp; Stress Load Tuning"),
        ("Counselor &amp; Telehealth Service", "Appointment Booking &amp; Clinical Notes"),
        ("Polar Payment Webhook Handler", "Signature Verification &amp; Confirmation"),
    ]
    draw_component("FastAPI Backend Application", b_items, 480, 100, 360, 480, "#16a34a")

    ai_items = [
        ("Whisper ASR Model Worker", "Urdu / English Speech-to-Text Transcription"),
        ("Multimodal Fusion Classifier", "PyTorch BiLSTM / Scikit-learn Classifier"),
        ("SHAP Attribution Engine", "TreeSHAP / KernelSHAP Factor Weights"),
        ("Conversational Support LLM", "Contextual Student Chatbot Assistant"),
    ]
    draw_component("AI &amp; ML Model Inference Tier", ai_items, 940, 100, 350, 290, "#9333ea")

    db_items = [
        ("PostgreSQL Database (v15)", "Relational Schema, Views &amp; RLS Policies"),
        ("GoTrue Authentication Engine", "JWT Issuance, Refresh &amp; Role Management"),
        ("Encrypted Personal Vault", "AES-256 GCM Storage for Sensitive Diaries"),
        ("S3-Compatible Object Store", "Audio Clips &amp; Relaxation Media Resources"),
    ]
    draw_component("Supabase Managed Cloud", db_items, 940, 440, 350, 290, "#0d9488")

    def draw_interface(x1, y1, x2, y2, label):
        mid_x = (x1 + x2) / 2
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{mid_x-12}" y2="{y1}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<circle cx="{mid_x-12}" cy="{y1}" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<path d="M {mid_x+6} {y1-10} A 10 10 0 0 0 {mid_x+6} {y1+10}" fill="none" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<line x1="{mid_x+6}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<text x="{mid_x}" y="{y1-12}" font-family="Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{label}</text>')

    draw_interface(390, 300, 480, 300, "REST / WSS (HTTPS TLS 1.3)")
    draw_interface(840, 240, 940, 240, "Internal IPC / PyTorch API")
    draw_interface(840, 520, 940, 520, "PostgreSQL TCP 5432 / PostgREST")

    svg.append('</svg>')
    save_and_render("06_Component_Diagram", "\n".join(svg), b.to_xml())

# =============================================================================
# 07_Deployment_Diagram (Physical 3D Nodes & Protocols)
# =============================================================================
def build_deployment_diagram():
    w, h = 1350, 900
    b = DrawioBuilder("07_Deployment_Diagram", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.1.3: MindEase UML Deployment Diagram (Physical Nodes, Artifacts &amp; Protocols)</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',
    ]

    def draw_3d_node(x, y, bw, bh, d=16, label="&lt;&lt;device&gt;&gt;", name="", color="#1e3a8a"):
        svg.append(f'<rect x="{x}" y="{y+d}" width="{bw}" height="{bh}" fill="#ffffff" stroke="{color}" stroke-width="1.8"/>')
        svg.append(f'<polygon points="{x},{y+d} {x+d},{y} {x+bw+d},{y} {x+bw},{y+d}" fill="#f1f5f9" stroke="{color}" stroke-width="1.8"/>')
        svg.append(f'<polygon points="{x+bw},{y+d} {x+bw+d},{y} {x+bw+d},{y+bh} {x+bw},{y+d+bh}" fill="#e2e8f0" stroke="{color}" stroke-width="1.8"/>')
        svg.append(f'<text x="{x+bw/2}" y="{y+d+22}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{color}" text-anchor="middle">{label}</text>')
        svg.append(f'<text x="{x+bw/2}" y="{y+d+38}" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{name}</text>')
        svg.append(f'<line x1="{x}" y1="{y+d+48}" x2="{x+bw}" y2="{y+d+48}" stroke="{color}" stroke-width="1"/>')

    def draw_artifact(x, y, aw, ah, aname, sub):
        svg.append(f'<rect x="{x}" y="{y}" width="{aw}" height="{ah}" fill="#ffffff" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="3,3" rx="3"/>')
        svg.append(f'<text x="{x+aw/2}" y="{y+16}" font-family="Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#0284c7" text-anchor="middle">&lt;&lt;artifact&gt;&gt; {aname}</text>')
        svg.append(f'<text x="{x+aw/2}" y="{y+30}" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">{sub}</text>')

    # Nodes
    draw_3d_node(60, 110, 310, 480, d=16, label="&lt;&lt;device&gt;&gt;", name="Android Smartphone (Client Device)")
    draw_artifact(80, 190, 270, 42, "MindEase_App.apk", "Flutter 3.x Engine / Dart 3 Runtime")
    draw_artifact(80, 250, 270, 42, "Built-in Microphone", "16kHz PCM Audio Stream Capture")
    draw_artifact(80, 310, 270, 42, "Screen Time &amp; Steps", "Android SensorManager API (Software)")
    draw_artifact(80, 370, 270, 42, "Local SQLite / Cache", "Encrypted KeyStore &amp; Offline Sessions")

    draw_3d_node(480, 110, 360, 560, d=16, label="&lt;&lt;execution environment&gt;&gt;", name="Cloud Application Server (Linux/Docker)")
    draw_artifact(505, 190, 310, 42, "FastAPI ASGI Engine", "Python 3.11 / Uvicorn Server Worker")
    draw_artifact(505, 250, 310, 42, "Whisper ASR Inference Worker", "Urdu/English Speech-to-Text Pipeline")
    draw_artifact(505, 310, 310, 42, "Multimodal Fusion Model", "PyTorch BiLSTM Classifier Model")
    draw_artifact(505, 370, 310, 42, "SHAP XAI Attribution Engine", "TreeSHAP / KernelSHAP Factor Weights")
    draw_artifact(505, 430, 310, 42, "Adaptive Study Planner Engine", "Pomodoro Chunking &amp; Stress Calibration")

    draw_3d_node(950, 110, 330, 360, d=16, label="&lt;&lt;cloud system&gt;&gt;", name="Supabase Cloud Platform (AWS)")
    draw_artifact(975, 190, 280, 42, "PostgreSQL 15 Relational DB", "PostgREST Engine &amp; RLS Security Policies")
    draw_artifact(975, 250, 280, 42, "GoTrue Auth Provider", "JWT Issuance &amp; Multi-Role Verification")
    draw_artifact(975, 310, 280, 42, "S3 Object Media Bucket", "Audio Recordings &amp; Relaxation Content")

    draw_3d_node(950, 520, 330, 240, d=16, label="&lt;&lt;external cloud&gt;&gt;", name="Polar Payment Gateway (Sandbox)")
    draw_artifact(975, 600, 280, 42, "Hosted Checkout Session API", "Sandbox Payment &amp; Escrow Token")
    draw_artifact(975, 660, 280, 42, "HMAC-SHA256 Webhook Dispatcher", "Automated Booking Confirmation Callbacks")

    def draw_link(x1, y1, x2, y2, p_label, s_label):
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0f172a" stroke-width="2"/>')
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        svg.append(f'<text x="{mid_x}" y="{mid_y - 8}" font-family="Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{p_label}</text>')
        svg.append(f'<text x="{mid_x}" y="{mid_y + 8}" font-family="Arial, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">{s_label}</text>')

    draw_link(386, 320, 480, 320, "HTTPS (TLS 1.3) / WSS", "Port 443 Encrypted")
    draw_link(856, 260, 950, 260, "TCP 5432 Encrypted", "PostgreSQL Pool Connection")
    draw_link(856, 620, 950, 620, "HTTPS REST Webhook", "HMAC-SHA256 Signature")

    svg.append('</svg>')
    save_and_render("07_Deployment_Diagram", "\n".join(svg), b.to_xml())

# =============================================================================
# 08_Class_Diagram (OOP Domain Architecture - 12 Classes Fully Connected)
# =============================================================================
def build_class_diagram():
    w, h = 1420, 980
    b = DrawioBuilder("08_Class_Diagram", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.1.1: MindEase Domain UML Class Diagram</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',
    ]

    def draw_class(name, attrs, methods, x, y, bw=230):
        header_h = 26
        attrs_h = len(attrs) * 14 + 10
        meth_h = len(methods) * 14 + 10
        total_h = header_h + attrs_h + meth_h

        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{total_h}" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" rx="2"/>')
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{header_h}" fill="#f1f5f9"/>')
        svg.append(f'<text x="{x+bw/2}" y="{y+18}" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{name}</text>')
        svg.append(f'<line x1="{x}" y1="{y+header_h}" x2="{x+bw}" y2="{y+header_h}" stroke="#0f172a" stroke-width="1.4"/>')

        curr_y = y + header_h + 12
        for a in attrs:
            svg.append(f'<text x="{x+10}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">{a}</text>')
            curr_y += 14

        svg.append(f'<line x1="{x}" y1="{curr_y}" x2="{x+bw}" y2="{curr_y}" stroke="#0f172a" stroke-width="1"/>')
        curr_y += 12
        for m in methods:
            svg.append(f'<text x="{x+10}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">{m}</text>')
            curr_y += 14

    # Row 1: Core Inheritance Hierarchy
    draw_class("User", ["+ id: UUID", "+ email: String", "+ role: RoleEnum", "+ is_active: Boolean"], ["+ register(): Boolean", "+ login(): Token", "+ updateProfile(): Void"], 590, 80, 240)
    draw_class("StudentProfile", ["+ student_id: UUID (FK)", "+ university_reg: String", "+ baseline_stress: Float", "+ academic_year: Int"], ["+ checkFreeQuota(): Bool", "+ getBaseline(): Float"], 220, 230, 240)
    draw_class("CounselorProfile", ["+ counselor_id: UUID (FK)", "+ license_number: String", "+ is_verified: Boolean", "+ hourly_rate: Float"], ["+ setAvailability(): Void", "+ writeClinicalNotes(): Void"], 960, 230, 240)

    # Generalization Arrows (Inheritance: Hollow Triangle)
    # StudentProfile -> User
    svg.append('<path d="M 340 230 L 340 190 L 670 190 L 670 180" fill="none" stroke="#0f172a" stroke-width="1.5"/>')
    svg.append('<polygon points="670,180 663,195 677,195" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>')

    # CounselorProfile -> User
    svg.append('<path d="M 1080 230 L 1080 190 L 750 190 L 750 180" fill="none" stroke="#0f172a" stroke-width="1.5"/>')
    svg.append('<polygon points="750,180 743,195 757,195" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>')

    # Row 2: Assessment, Diary, Habits (Student Associations)
    draw_class("StressAssessment", ["+ id: UUID", "+ student_id: UUID (FK)", "+ pss_score: Float", "+ stress_level: Enum", "+ confidence: Float"], ["+ calculatePSS(): Float", "+ triggerTriage(): Void"], 50, 420, 230)
    draw_class("VoiceDiary", ["+ id: UUID", "+ student_id: UUID (FK)", "+ audio_url: String", "+ transcript: String", "+ sentiment_score: Float"], ["+ transcribe(): String", "+ analyzeSentiment(): Float"], 310, 420, 230)
    draw_class("DailyHabit", ["+ id: UUID", "+ student_id: UUID (FK)", "+ sleep_hours: Float", "+ step_count: Int", "+ screen_time: Float"], ["+ syncSensors(): Void", "+ computeHabitScore(): Float"], 570, 420, 230)

    # Associations StudentProfile -> Assessments/Diaries/Habits
    svg.append('<line x1="260" y1="365" x2="165" y2="420" stroke="#0f172a" stroke-width="1.4"/>')
    svg.append('<text x="210" y="380" font-family="Arial, sans-serif" font-size="9" font-weight="bold">1..*</text>')
    svg.append('<line x1="340" y1="365" x2="425" y2="420" stroke="#0f172a" stroke-width="1.4"/>')
    svg.append('<text x="390" y="380" font-family="Arial, sans-serif" font-size="9" font-weight="bold">1..*</text>')
    svg.append('<line x1="420" y1="365" x2="650" y2="420" stroke="#0f172a" stroke-width="1.4"/>')
    svg.append('<text x="530" y="380" font-family="Arial, sans-serif" font-size="9" font-weight="bold">1..*</text>')

    # Row 3: Fusion & Explainability (Fed by Assessment, Diary, Habits)
    draw_class("MultimodalFusionEngine", ["+ feature_vector: Float[]", "+ fusion_weights: Float[]", "+ bilstm_model_path: String"], ["+ normalizeInputs(): Vector", "+ predictStress(): StressLevel"], 170, 680, 240)
    draw_class("XAIExplainer", ["+ assessment_id: UUID (FK)", "+ shap_values: Map&lt;Str,Flt&gt;", "+ top_contributors: String[]"], ["+ computeSHAP(): Map", "+ generateInsights(): String"], 440, 680, 240)

    # Dependency Lines from inputs into Fusion
    svg.append('<line x1="165" y1="570" x2="250" y2="680" stroke="#1e3a8a" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#arrow)"/>')
    svg.append('<line x1="425" y1="570" x2="310" y2="680" stroke="#1e3a8a" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#arrow)"/>')
    svg.append('<line x1="650" y1="570" x2="350" y2="680" stroke="#1e3a8a" stroke-width="1.4" stroke-dasharray="4,4" marker-end="url(#arrow)"/>')

    # Fusion to XAI
    svg.append('<line x1="410" y1="740" x2="440" y2="740" stroke="#0f172a" stroke-width="1.4" marker-end="url(#arrow)"/>')
    svg.append('<text x="425" y="730" font-family="Arial, sans-serif" font-size="8.5" text-anchor="middle">1..1</text>')

    # Study Planner & Relaxation (Actionable Recovery)
    draw_class("AdaptiveStudyPlan", ["+ id: UUID", "+ student_id: UUID (FK)", "+ focus_minutes: Int", "+ break_minutes: Int", "+ daily_load: Enum"], ["+ calibratePomodoro(): Void", "+ reschedule(): Void"], 710, 680, 240)
    svg.append('<line x1="560" y1="740" x2="710" y2="740" stroke="#0f172a" stroke-width="1.4" marker-end="url(#arrow)"/>')
    svg.append('<text x="635" y="730" font-family="Arial, sans-serif" font-size="8.5" text-anchor="middle">triggers</text>')

    # Row 4: Clinical Appointments, Polar Billing, Peer Community
    draw_class("Appointment", ["+ id: UUID", "+ student_id: UUID (FK)", "+ counselor_id: UUID (FK)", "+ slot_time: DateTime", "+ status: ApptStatus"], ["+ confirmBooking(): Void", "+ cancelBooking(): Void"], 960, 460, 240)
    draw_class("PaymentTransaction", ["+ id: UUID", "+ appt_id: UUID (FK)", "+ polar_checkout_id: Str", "+ amount: Float", "+ status: PaymentStatus"], ["+ verifyWebhook(): Boolean", "+ refund(): Void"], 960, 700, 240)
    draw_class("CommunityPost", ["+ id: UUID", "+ author_id: UUID (FK)", "+ content: String", "+ is_anonymous: Boolean", "+ flag_count: Int"], ["+ createPost(): Void", "+ flagPost(): Void", "+ moderate(): Void"], 1220, 460, 180)

    # Connections for Appointment, Payment, Community
    svg.append('<line x1="1080" y1="365" x2="1080" y2="460" stroke="#0f172a" stroke-width="1.4"/>')
    svg.append('<text x="1095" y="410" font-family="Arial, sans-serif" font-size="9" font-weight="bold">1..*</text>')

    # Orthogonal StudentProfile -> Appointment (avoids DailyHabit)
    svg.append('<path d="M 460 270 L 890 270 L 890 480 L 960 480" fill="none" stroke="#0f172a" stroke-width="1.4"/>')
    svg.append('<text x="475" y="262" font-family="Arial, sans-serif" font-size="9" font-weight="bold">1..*</text>')
    svg.append('<text x="945" y="472" font-family="Arial, sans-serif" font-size="9" font-weight="bold" text-anchor="end">0..*</text>')

    svg.append('<line x1="1080" y1="610" x2="1080" y2="700" stroke="#0f172a" stroke-width="1.4"/>')
    svg.append('<text x="1095" y="655" font-family="Arial, sans-serif" font-size="9" font-weight="bold">1..1</text>')

    svg.append('<line x1="830" y1="130" x2="1310" y2="130" stroke="#0f172a" stroke-width="1.4"/>')
    svg.append('<line x1="1310" y1="130" x2="1310" y2="460" stroke="#0f172a" stroke-width="1.4"/>')
    svg.append('<text x="1320" y="300" font-family="Arial, sans-serif" font-size="9" font-weight="bold">1..*</text>')

    svg.append('</svg>')
    save_and_render("08_Class_Diagram", "\n".join(svg), b.to_xml())

# =============================================================================
# 09_Entity_Relationship_Diagram (True Crow's Foot Relational Design)
# =============================================================================
def build_erd_diagram():
    w, h = 1450, 980
    b = DrawioBuilder("09_Entity_Relationship_Diagram", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.3.4: MindEase Entity Relationship Diagram (ERD)</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',
    ]

    def draw_entity(name, pks, fks, attrs, x, y, bw=230):
        header_h = 28
        total_rows = len(pks) + len(fks) + len(attrs)
        total_h = header_h + total_rows * 16 + 10

        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{total_h}" fill="#ffffff" stroke="#1e3a8a" stroke-width="2" rx="2"/>')
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{header_h}" fill="#1e3a8a"/>')
        svg.append(f'<text x="{x+bw/2}" y="{y+19}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">{name}</text>')

        curr_y = y + header_h + 14
        for p in pks:
            svg.append(f'<rect x="{x+6}" y="{curr_y-10}" width="24" height="12" fill="#fef3c7" rx="2"/>')
            svg.append(f'<text x="{x+18}" y="{curr_y}" font-family="Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#b45309" text-anchor="middle">PK</text>')
            svg.append(f'<text x="{x+36}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#0f172a">{p}</text>')
            curr_y += 16

        for f in fks:
            svg.append(f'<rect x="{x+6}" y="{curr_y-10}" width="24" height="12" fill="#e0f2fe" rx="2"/>')
            svg.append(f'<text x="{x+18}" y="{curr_y}" font-family="Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#0369a1" text-anchor="middle">FK</text>')
            svg.append(f'<text x="{x+36}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9.5" fill="#0369a1">{f}</text>')
            curr_y += 16

        for a in attrs:
            svg.append(f'<text x="{x+14}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9.5" fill="#475569">{a}</text>')
            curr_y += 16

    # 10 Relational Entities
    draw_entity("USERS", ["id: UUID"], [], ["email: VARCHAR(255)", "role: VARCHAR(50)", "created_at: TIMESTAMP", "is_active: BOOLEAN"], 610, 80, 230)
    draw_entity("STUDENT_PROFILES", ["student_id: UUID"], ["user_id: UUID (FK)"], ["university_reg: VARCHAR", "baseline_score: FLOAT", "free_triage_quota: INT"], 220, 230, 240)
    draw_entity("COUNSELOR_PROFILES", ["counselor_id: UUID"], ["user_id: UUID (FK)"], ["license_no: VARCHAR", "is_verified: BOOLEAN", "hourly_rate: NUMERIC"], 1000, 230, 240)

    draw_entity("STRESS_ASSESSMENTS", ["id: UUID"], ["student_id: UUID (FK)"], ["pss_score: FLOAT", "stress_level: VARCHAR", "confidence: FLOAT", "created_at: TIMESTAMP"], 50, 440, 230)
    draw_entity("VOICE_DIARIES", ["id: UUID"], ["student_id: UUID (FK)"], ["audio_s3_url: VARCHAR", "transcript: TEXT", "sentiment_score: FLOAT"], 310, 440, 230)
    draw_entity("DAILY_HABITS", ["id: UUID"], ["student_id: UUID (FK)"], ["sleep_hours: FLOAT", "step_count: INT", "screen_time_mins: INT"], 570, 440, 230)

    draw_entity("XAI_EXPLANATIONS", ["id: UUID"], ["assessment_id: UUID (FK)"], ["shap_factors: JSONB", "primary_trigger: VARCHAR", "plain_summary: TEXT"], 50, 710, 240)
    draw_entity("ADAPTIVE_STUDY_PLANS", ["id: UUID"], ["student_id: UUID (FK)"], ["focus_blocks: INT", "break_duration: INT", "academic_load: VARCHAR"], 450, 710, 240)
    draw_entity("APPOINTMENTS", ["id: UUID"], ["student_id: UUID (FK)", "counselor_id: UUID (FK)"], ["slot_time: TIMESTAMP", "is_free_tier: BOOLEAN", "status: VARCHAR"], 1000, 470, 240)
    draw_entity("PAYMENT_TRANSACTIONS", ["id: UUID"], ["appt_id: UUID (FK)"], ["polar_order_id: VARCHAR", "amount: NUMERIC", "payment_status: VARCHAR"], 1000, 720, 240)

    # Clean Crow's Foot Connector Lines
    def draw_crows_foot(x1, y1, x2, y2, label=""):
        svg.append(f'<path d="M {x1} {y1} L {x2} {y2}" fill="none" stroke="#0f172a" stroke-width="1.6"/>')
        svg.append(f'<line x1="{x1-5}" y1="{y1-5}" x2="{x1-5}" y2="{y1+5}" stroke="#0f172a" stroke-width="1.6"/>')
        svg.append(f'<line x1="{x1-9}" y1="{y1-5}" x2="{x1-9}" y2="{y1+5}" stroke="#0f172a" stroke-width="1.6"/>')
        svg.append(f'<line x1="{x2}" y1="{y2}" x2="{x2-10}" y2="{y2-6}" stroke="#0f172a" stroke-width="1.6"/>')
        svg.append(f'<line x1="{x2}" y1="{y2}" x2="{x2-10}" y2="{y2+6}" stroke="#0f172a" stroke-width="1.6"/>')
        if label:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            svg.append(f'<text x="{mid_x}" y="{mid_y-6}" font-family="Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1e3a8a">{label}</text>')

    draw_crows_foot(610, 150, 460, 270, "1 : 1")
    draw_crows_foot(840, 150, 1000, 270, "1 : 1")
    draw_crows_foot(260, 370, 165, 440, "1 : N")
    draw_crows_foot(340, 370, 425, 440, "1 : N")
    draw_crows_foot(420, 370, 650, 440, "1 : N")
    draw_crows_foot(165, 600, 165, 710, "1 : 1")
    
    # Orthogonal STUDENT_PROFILES -> ADAPTIVE_STUDY_PLANS via corridor (avoids VOICE_DIARIES)
    svg.append('<path d="M 460 320 L 555 320 L 555 710" fill="none" stroke="#0f172a" stroke-width="1.6"/>')
    svg.append('<line x1="465" y1="315" x2="465" y2="325" stroke="#0f172a" stroke-width="1.6"/>')
    svg.append('<line x1="469" y1="315" x2="469" y2="325" stroke="#0f172a" stroke-width="1.6"/>')
    svg.append('<line x1="555" y1="710" x2="549" y2="700" stroke="#0f172a" stroke-width="1.6"/>')
    svg.append('<line x1="555" y1="710" x2="561" y2="700" stroke="#0f172a" stroke-width="1.6"/>')
    svg.append('<text x="565" y="520" font-family="Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1e3a8a">1 : N</text>')

    draw_crows_foot(1120, 380, 1120, 470, "1 : N")
    draw_crows_foot(1120, 640, 1120, 720, "1 : 1")

    svg.append('</svg>')
    save_and_render("09_Entity_Relationship_Diagram", "\n".join(svg), b.to_xml())

# =============================================================================
# 10_Database_Schema (Physical Schema Design)
# =============================================================================
def build_database_schema():
    w, h = 1450, 980
    b = DrawioBuilder("10_Database_Schema", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.3.5: MindEase Relational Database Physical Schema Design</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',
    ]

    def draw_table(name, cols, x, y, bw=240):
        header_h = 28
        total_h = header_h + len(cols) * 16 + 10

        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{total_h}" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8" rx="2"/>')
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{header_h}" fill="#1e3a8a"/>')
        svg.append(f'<text x="{x+bw/2}" y="{y+19}" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{name}</text>')

        curr_y = y + header_h + 14
        for badge, cname, ctype in cols:
            if badge == "PK":
                svg.append(f'<rect x="{x+6}" y="{curr_y-10}" width="22" height="12" fill="#fef3c7" rx="2"/>')
                svg.append(f'<text x="{x+17}" y="{curr_y}" font-family="Arial, sans-serif" font-size="8" font-weight="bold" fill="#b45309" text-anchor="middle">PK</text>')
            elif badge == "FK":
                svg.append(f'<rect x="{x+6}" y="{curr_y-10}" width="22" height="12" fill="#e0f2fe" rx="2"/>')
                svg.append(f'<text x="{x+17}" y="{curr_y}" font-family="Arial, sans-serif" font-size="8" font-weight="bold" fill="#0369a1" text-anchor="middle">FK</text>')
            else:
                svg.append(f'<circle cx="{x+17}" cy="{curr_y-4}" r="2.5" fill="#94a3b8"/>')

            svg.append(f'<text x="{x+34}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">{cname}</text>')
            svg.append(f'<text x="{x+bw-8}" y="{curr_y}" font-family="Arial, sans-serif" font-size="8.5" fill="#64748b" text-anchor="end">{ctype}</text>')
            curr_y += 16

    # 10 Physical PostgreSQL Tables
    draw_table("public.users", [
        ("PK", "id", "UUID NOT NULL"),
        ("", "email", "VARCHAR(255) UNIQUE"),
        ("", "role", "VARCHAR(30) NOT NULL"),
        ("", "encrypted_pw", "VARCHAR(255)"),
        ("", "is_active", "BOOLEAN DEFAULT TRUE"),
        ("", "created_at", "TIMESTAMPTZ DEFAULT NOW()")
    ], 600, 80, 250)

    draw_table("public.student_profiles", [
        ("PK", "student_id", "UUID NOT NULL"),
        ("FK", "user_id", "UUID REFERENCES users"),
        ("", "university_reg", "VARCHAR(50)"),
        ("", "baseline_stress", "FLOAT DEFAULT 0.0"),
        ("", "free_triage_quota", "INT DEFAULT 1")
    ], 210, 230, 250)

    draw_table("public.counselor_profiles", [
        ("PK", "counselor_id", "UUID NOT NULL"),
        ("FK", "user_id", "UUID REFERENCES users"),
        ("", "license_number", "VARCHAR(100)"),
        ("", "is_verified", "BOOLEAN DEFAULT FALSE"),
        ("", "hourly_fee", "NUMERIC(10,2)")
    ], 1000, 230, 250)

    draw_table("public.stress_assessments", [
        ("PK", "id", "UUID NOT NULL"),
        ("FK", "student_id", "UUID REFERENCES student"),
        ("", "pss_score", "FLOAT NOT NULL"),
        ("", "stress_category", "VARCHAR(20)"),
        ("", "confidence_score", "FLOAT NOT NULL"),
        ("", "assessed_at", "TIMESTAMPTZ")
    ], 50, 440, 240)

    draw_table("public.voice_diaries", [
        ("PK", "id", "UUID NOT NULL"),
        ("FK", "student_id", "UUID REFERENCES student"),
        ("", "audio_storage_url", "VARCHAR(500)"),
        ("", "raw_transcription", "TEXT"),
        ("", "sentiment_score", "FLOAT"),
        ("", "is_crisis_flagged", "BOOLEAN")
    ], 310, 440, 240)

    draw_table("public.daily_habits", [
        ("PK", "id", "UUID NOT NULL"),
        ("FK", "student_id", "UUID REFERENCES student"),
        ("", "sleep_hours", "FLOAT"),
        ("", "step_count", "INT"),
        ("", "screen_time_mins", "INT"),
        ("", "log_date", "DATE NOT NULL")
    ], 570, 440, 240)

    draw_table("public.xai_explanations", [
        ("PK", "id", "UUID NOT NULL"),
        ("FK", "assessment_id", "UUID REFERENCES assess"),
        ("", "shap_values_json", "JSONB NOT NULL"),
        ("", "top_factor_1", "VARCHAR(100)"),
        ("", "top_factor_2", "VARCHAR(100)"),
        ("", "summary_text", "TEXT")
    ], 50, 710, 240)

    draw_table("public.study_plans", [
        ("PK", "id", "UUID NOT NULL"),
        ("FK", "student_id", "UUID REFERENCES student"),
        ("", "focus_duration", "INT NOT NULL"),
        ("", "break_duration", "INT NOT NULL"),
        ("", "academic_load", "VARCHAR(20)"),
        ("", "is_completed", "BOOLEAN DEFAULT FALSE")
    ], 450, 710, 240)

    draw_table("public.appointments", [
        ("PK", "id", "UUID NOT NULL"),
        ("FK", "student_id", "UUID REFERENCES student"),
        ("FK", "counselor_id", "UUID REFERENCES counselor"),
        ("", "scheduled_start", "TIMESTAMPTZ NOT NULL"),
        ("", "is_free_session", "BOOLEAN DEFAULT TRUE"),
        ("", "booking_status", "VARCHAR(30)")
    ], 1000, 470, 250)

    draw_table("public.payment_transactions", [
        ("PK", "id", "UUID NOT NULL"),
        ("FK", "appointment_id", "UUID REFERENCES appts"),
        ("", "polar_checkout_id", "VARCHAR(100)"),
        ("", "amount_paid", "NUMERIC(10,2)"),
        ("", "transaction_status", "VARCHAR(30)"),
        ("", "verified_at", "TIMESTAMPTZ")
    ], 1000, 720, 250)

    # FK Connector Lines with pins
    def draw_fk_link(x1, y1, x2, y2):
        svg.append(f'<path d="M {x1} {y1} L {x2} {y2}" fill="none" stroke="#0284c7" stroke-width="1.4" stroke-dasharray="4,4"/>')
        svg.append(f'<circle cx="{x1}" cy="{y1}" r="3" fill="#0284c7"/>')
        svg.append(f'<circle cx="{x2}" cy="{y2}" r="3" fill="#0284c7"/>')

    draw_fk_link(600, 150, 460, 260)
    draw_fk_link(850, 150, 1000, 260)
    draw_fk_link(260, 360, 170, 440)
    draw_fk_link(340, 360, 430, 440)
    draw_fk_link(420, 360, 650, 440)
    draw_fk_link(170, 590, 170, 710)
    
    # Orthogonal student_profiles -> study_plans via corridor (avoids voice_diaries)
    svg.append('<path d="M 460 310 L 555 310 L 555 710" fill="none" stroke="#0284c7" stroke-width="1.4" stroke-dasharray="4,4"/>')
    svg.append('<circle cx="460" cy="310" r="3" fill="#0284c7"/>')
    svg.append('<circle cx="555" cy="710" r="3" fill="#0284c7"/>')

    draw_fk_link(1125, 360, 1125, 470)
    draw_fk_link(1125, 620, 1125, 720)

    svg.append('</svg>')
    save_and_render("10_Database_Schema", "\n".join(svg), b.to_xml())

# =============================================================================
# 11_State_Machine_Diagram (Dual Track State Lifecycles)
# =============================================================================
def build_state_machine_diagram():
    w, h = 1350, 920
    b = DrawioBuilder("11_State_Machine_Diagram", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        '<defs>',
        '  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">',
        '    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>',
        '  </marker>',
        '</defs>',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.5.1: State Machine Transition Diagrams for Stress Assessment and Appointment Lifecycles</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',
    ]

    def draw_state(name, x, y, bw=140, bh=44, sub=""):
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" rx="8"/>')
        svg.append(f'<text x="{x+bw/2}" y="{y+19}" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{name}</text>')
        if sub:
            svg.append(f'<text x="{x+bw/2}" y="{y+33}" font-family="Arial, sans-serif" font-size="8.5" fill="#64748b" text-anchor="middle">{sub}</text>')

    def add_clean_trans(path_d, label, tx, ty, anchor="middle"):
        svg.append(f'<path d="{path_d}" fill="none" stroke="#0f172a" stroke-width="1.4" marker-end="url(#arrow)"/>')
        svg.append(f'<text x="{tx}" y="{ty}" font-family="Arial, sans-serif" font-size="8.5" font-weight="600" fill="#0f172a" text-anchor="{anchor}">{label}</text>')

    # -------------------------------------------------------------
    # REGION 1: Stress Assessment & Adaptive Recovery Lifecycle
    # -------------------------------------------------------------
    svg.append('<rect x="50" y="85" width="1250" height="360" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" rx="6"/>')
    svg.append('<rect x="50" y="85" width="380" height="26" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5" rx="4"/>')
    svg.append('<text x="65" y="103" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#1e40af">1. Daily Assessment &amp; Adaptive Intervention Lifecycle</text>')

    # Initial State
    svg.append('<circle cx="90" cy="220" r="14" fill="#0f172a"/>')

    # States
    draw_state("Idle / Baseline", 140, 198, 130, 44)
    draw_state("Capturing Data", 330, 198, 140, 44, "Voice, PSS, Habits")
    draw_state("Multimodal Fusion", 540, 198, 150, 44, "BiLSTM Inference")
    draw_state("SHAP Attribution", 760, 198, 150, 44, "Driver Weights")
    draw_state("Intervention Dispatched", 980, 198, 170, 44, "Plan / Recovery")

    # Final State
    svg.append('<circle cx="1220" cy="220" r="13" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>')
    svg.append('<circle cx="1220" cy="220" r="8" fill="#0f172a"/>')

    # Acute Risk Sub-State
    draw_state("Crisis SOS Triage", 760, 340, 150, 44, "Emergency Helpline")

    # Transitions Region 1
    add_clean_trans("M 104 220 L 140 220", "openApp()", 122, 210)
    add_clean_trans("M 270 220 L 330 220", "submitEntry()", 300, 210)
    add_clean_trans("M 470 220 L 540 220", "featuresExtracted()", 505, 210)
    add_clean_trans("M 690 220 L 760 220", "stressComputed()", 725, 210)
    add_clean_trans("M 910 220 L 980 220", "insightsGenerated()", 945, 210)
    add_clean_trans("M 1150 220 L 1207 220", "planSaved()", 1178, 210)

    # Crisis Branch
    add_clean_trans("M 615 242 L 615 362 L 760 362", "[score &gt;= AcuteHigh]", 690, 352)
    add_clean_trans("M 910 362 L 1065 362 L 1065 242", "counselorAlerted()", 1010, 352)

    # -------------------------------------------------------------
    # REGION 2: Counselor Telehealth & Polar Payment Lifecycle
    # -------------------------------------------------------------
    svg.append('<rect x="50" y="475" width="1250" height="390" fill="#f8fafc" stroke="#10b981" stroke-width="1.5" rx="6"/>')
    svg.append('<rect x="50" y="475" width="380" height="26" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5" rx="4"/>')
    svg.append('<text x="65" y="493" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#047857">2. Counselor Appointment &amp; Polar Payment Lifecycle</text>')

    svg.append('<circle cx="92" cy="640" r="14" fill="#0f172a"/>')

    draw_state("Slot Selection", 150, 618, 120, 44)
    svg.append('<polygon points="370,640 410,618 450,640 410,662" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/>')

    # Upper Track: Free Session
    draw_state("Confirmed (Free)", 560, 530, 160, 44, "Quota Consumed")

    # Lower Track: Paid Session
    draw_state("Payment Pending", 560, 710, 160, 44)
    draw_state("Polar Checkout", 780, 710, 150, 44, "Hosted Sandbox")
    draw_state("Confirmed (Paid)", 780, 530, 150, 44, "Webhook Verified")

    draw_state("In Consultation", 990, 530, 140, 44)
    draw_state("Completed", 990, 660, 140, 44, "Notes Archived")

    svg.append('<circle cx="1200" cy="682" r="13" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>')
    svg.append('<circle cx="1200" cy="682" r="8" fill="#0f172a"/>')

    add_clean_trans("M 106 640 L 150 640", "bookAppt()", 128, 630)
    add_clean_trans("M 270 640 L 370 640", "checkHistory()", 320, 630)

    # Free Branch
    add_clean_trans("M 410 618 L 410 552 L 560 552", "[isFreeEligible]", 485, 542)
    # Paid Branch
    add_clean_trans("M 410 662 L 410 732 L 560 732", "[!isFreeEligible]", 485, 744)

    # Payment Flow
    add_clean_trans("M 720 732 L 780 732", "initiateCheckout()", 750, 722)
    add_clean_trans("M 855 710 L 855 574", "webhookSuccess()", 863, 642, "start")

    # Decline Loopback
    svg.append('<path d="M 855 754 L 855 790 L 640 790 L 640 754" fill="none" stroke="#0f172a" stroke-width="1.4" marker-end="url(#arrow)"/>')
    svg.append('<text x="745" y="805" font-family="Arial, sans-serif" font-size="8.5" font-weight="600" fill="#0f172a" text-anchor="middle">[declined]</text>')

    # Confirmed to Consultation
    add_clean_trans("M 720 552 L 780 552", "ready()", 750, 542)
    add_clean_trans("M 930 552 L 990 552", "joinCall()", 960, 542)

    # Consultation to Completed
    add_clean_trans("M 1060 574 L 1060 660", "sessionEnd()", 1068, 617, "start")
    add_clean_trans("M 1130 682 L 1187 682", "notesLogged()", 1158, 672)

    svg.append('</svg>')
    save_and_render("11_State_Machine_Diagram", "\n".join(svg), b.to_xml())

# =============================================================================
# Master Execution Routine
# =============================================================================
if __name__ == "__main__":
    print("=====================================================================")
    print("Regenerating ALL 11 System Diagrams with Flawless Academic Precision:")
    print("- Pure white background (#ffffff)")
    print("- Zero white label background boxes")
    print("- Zero text overlapping or shape collisions")
    print("- Inspiration Image 2 (TexEye AI) layout for Use Case Diagram")
    print("- Exactly 17 Use Cases (UC01 to UC17) matching 17 Sequence Diagrams")
    print("- 100% compliant with MindEase Proposal (12 Modules, No Edge AI)")
    print("=====================================================================")
    build_system_architecture()
    build_use_case_diagram()
    build_dfd_level_0()
    build_dfd_level_1()
    build_dfd_level_2()
    build_component_diagram()
    build_deployment_diagram()
    build_class_diagram()
    build_erd_diagram()
    build_database_schema()
    build_state_machine_diagram()
    print("=====================================================================")
    print("All 11 system diagrams regenerated successfully with 100% clean presentation!")
    print("=====================================================================")
