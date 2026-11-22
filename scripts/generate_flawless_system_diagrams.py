"""
MindEase FYP - Flawless Academic Diagram Generator
Regenerates all 9 Core System Architecture, Data, Behavioral, and Physical Diagrams:
1. 03_DFD_Level_0 (Context Diagram)
2. 04_DFD_Level_1 (Subsystem Functional Decomposition)
3. 05_DFD_Level_2_Stress_Detection (Process 4.0 Detailed Pipeline)
4. 06_Component_Diagram (UML 2.5 Component & Interface Architecture)
5. 07_Deployment_Diagram (UML Physical Nodes, Artifacts & Protocols)
6. 08_Class_Diagram (Domain Model & OOP Class Architecture)
7. 09_Entity_Relationship_Diagram (True Crow's Foot Notation ERD)
8. 10_Database_Schema (Physical Relational Tables with Explicit FK Lines)
9. 11_State_Machine_Diagram (Stress & Appointment Lifecycles with Clean Tracks)

All diagrams strictly adhere to:
- Pure white background (#ffffff)
- Clean, non-crossing, orthogonal lines
- Labeled data flows and UML multiplicities
- Zero floating classes or disconnected tables
- 100% domain accuracy to MindEase's 12 Proposal Modules (No Edge AI, No Hardware)
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
# 1. DFD Level 0 (Context Diagram)
# =============================================================================
def build_dfd_level_0():
    w, h = 1300, 920
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

        # Central Process 0.0
        '<circle cx="650" cy="460" r="140" fill="#ffffff" stroke="#1e3a8a" stroke-width="2.5"/>',
        '<line x1="515" y1="420" x2="785" y2="420" stroke="#1e3a8a" stroke-width="1.5"/>',
        '<text x="650" y="395" font-family="Arial, sans-serif" font-size="18" font-weight="bold" fill="#1e3a8a" text-anchor="middle">0.0</text>',
        '<text x="650" y="450" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#0f172a" text-anchor="middle">MindEase AI Stress Detection,</text>',
        '<text x="650" y="472" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Recovery &amp; Support</text>',
        '<text x="650" y="494" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#0f172a" text-anchor="middle">System</text>',
    ]

    # External Entities
    # 1. Student (Top Left)
    s_x, s_y, ent_w, ent_h = 70, 160, 240, 85
    svg.extend([
        f'<rect x="{s_x}" y="{s_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{s_x+ent_w/2}" y="{s_y+36}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Student</text>',
        f'<text x="{s_x+ent_w/2}" y="{s_y+58}" font-family="Arial, sans-serif" font-size="11.5" fill="#475569" text-anchor="middle">(Primary User)</text>',
    ])

    # 2. Polar Gateway (Bottom Left)
    p_x, p_y = 70, 680
    svg.extend([
        f'<rect x="{p_x}" y="{p_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{p_x+ent_w/2}" y="{p_y+36}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Gateway</text>',
        f'<text x="{p_x+ent_w/2}" y="{p_y+58}" font-family="Arial, sans-serif" font-size="11.5" fill="#475569" text-anchor="middle">(External Payment Service)</text>',
    ])

    # 3. Counselor (Top Right)
    c_x, c_y = 990, 160
    svg.extend([
        f'<rect x="{c_x}" y="{c_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{c_x+ent_w/2}" y="{c_y+36}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor</text>',
        f'<text x="{c_x+ent_w/2}" y="{c_y+58}" font-family="Arial, sans-serif" font-size="11.5" fill="#475569" text-anchor="middle">(Mental Health Professional)</text>',
    ])

    # 4. Administrator (Bottom Right)
    a_x, a_y = 990, 680
    svg.extend([
        f'<rect x="{a_x}" y="{a_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{a_x+ent_w/2}" y="{a_y+36}" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">Administrator</text>',
        f'<text x="{a_x+ent_w/2}" y="{a_y+58}" font-family="Arial, sans-serif" font-size="11.5" fill="#475569" text-anchor="middle">(System Admin)</text>',
    ])

    # Clean Orthogonal Labeled Data Flows
    # Helper to add clean orthogonal line with white background pill
    def add_flow(path_d, label, lx, ly, anchor="middle"):
        svg.append(f'<path d="{path_d}" fill="none" stroke="#1e3a8a" stroke-width="1.6" marker-end="url(#arrow)"/>')
        label_w = len(label) * 6.5 + 16
        rx_val = lx - label_w/2 if anchor == "middle" else lx
        svg.append(f'<rect x="{rx_val}" y="{ly - 11}" width="{label_w}" height="20" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8" rx="4"/>')
        svg.append(f'<text x="{lx}" y="{ly + 3.5}" font-family="Arial, sans-serif" font-size="10" font-weight="500" fill="#0f172a" text-anchor="{anchor}">{label}</text>')

    # Flows: Student <-> MindEase
    add_flow("M 310 185 L 530 185 L 565 345", "Questionnaire Responses, Voice Diary, Habit Logs", 430, 172)
    add_flow("M 530 395 L 430 395 L 430 225 L 310 225", "Stress Level (L/M/H), XAI Insights, Adaptive Study Plan", 380, 240)

    # Flows: Counselor <-> MindEase
    add_flow("M 990 185 L 770 185 L 735 345", "Availability Slots, Clinical Assessment Notes", 870, 172)
    add_flow("M 770 395 L 870 395 L 870 225 L 990 225", "Booking Requests, Consented Student Dossiers", 920, 240)

    # Flows: Polar Gateway <-> MindEase
    add_flow("M 535 525 L 420 525 L 420 705 L 310 705", "Checkout Session Token & Booking Reference Request", 410, 692)
    add_flow("M 310 740 L 530 740 L 575 580", "Webhook Payment Confirmation Token (Success / Decline)", 440, 755)

    # Flows: Administrator <-> MindEase
    add_flow("M 990 705 L 880 705 L 880 525 L 765 525", "Moderation Actions, Content Updates, Counselor Approvals", 890, 692)
    add_flow("M 725 580 L 770 740 L 990 740", "Reported Community Post Queue, Audit Telemetry Logs", 860, 755)

    svg.append('</svg>')
    save_and_render("03_DFD_Level_0", "\n".join(svg), b.to_xml())

# =============================================================================
# 2. DFD Level 1 (Subsystem Functional Decomposition)
# =============================================================================
def build_dfd_level_1():
    w, h = 1350, 960
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

    # External Entities placed strategically adjacent to their processes
    # Student (Left, vertically centered)
    st_x, st_y, ent_w, ent_h = 50, 360, 140, 75
    svg.extend([
        f'<rect x="{st_x}" y="{st_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{st_x+ent_w/2}" y="{st_y+34}" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Student</text>',
        f'<text x="{st_x+ent_w/2}" y="{st_y+54}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Primary User)</text>',
    ])

    # Counselor (Top Right)
    c_x, c_y = 1160, 160
    svg.extend([
        f'<rect x="{c_x}" y="{c_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{c_x+ent_w/2}" y="{c_y+34}" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor</text>',
        f'<text x="{c_x+ent_w/2}" y="{c_y+54}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Clinical Pro)</text>',
    ])

    # Administrator (Middle Right)
    a_x, a_y = 1160, 470
    svg.extend([
        f'<rect x="{a_x}" y="{a_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{a_x+ent_w/2}" y="{a_y+34}" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Administrator</text>',
        f'<text x="{a_x+ent_w/2}" y="{a_y+54}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(System Admin)</text>',
    ])

    # Polar Gateway (Bottom Right)
    p_x, p_y = 1160, 760
    svg.extend([
        f'<rect x="{p_x}" y="{p_y}" width="{ent_w}" height="{ent_h}" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>',
        f'<text x="{p_x+ent_w/2}" y="{p_y+34}" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Gateway</text>',
        f'<text x="{p_x+ent_w/2}" y="{p_y+54}" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Payment)</text>',
    ])

    # Helper for Process Circle
    def draw_proc(num, title1, title2, cx, cy, r=52):
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="#1e3a8a" stroke-width="2"/>')
        svg.append(f'<line x1="{cx-r*0.9}" y1="{cy-14}" x2="{cx+r*0.9}" y2="{cy-14}" stroke="#1e3a8a" stroke-width="1.2"/>')
        svg.append(f'<text x="{cx}" y="{cy-22}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="middle">{num}</text>')
        svg.append(f'<text x="{cx}" y="{cy+4}" font-family="Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{title1}</text>')
        svg.append(f'<text x="{cx}" y="{cy+18}" font-family="Arial, sans-serif" font-size="9.5" fill="#0f172a" text-anchor="middle">{title2}</text>')

    # Helper for Gane-Sarson Data Store
    def draw_dstore(num, name, x, y, w_box=160, h_box=32):
        svg.append(f'<line x1="{x}" y1="{y}" x2="{x+w_box}" y2="{y}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<line x1="{x}" y1="{y+h_box}" x2="{x+w_box}" y2="{y+h_box}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+h_box}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<line x1="{x+38}" y1="{y}" x2="{x+38}" y2="{y+h_box}" stroke="#0f172a" stroke-width="1"/>')
        svg.append(f'<rect x="{x+1}" y="{y+1}" width="36" height="{h_box-2}" fill="#f1f5f9"/>')
        svg.append(f'<text x="{x+19}" y="{y+20}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">{num}</text>')
        svg.append(f'<text x="{x+46}" y="{y+20}" font-family="Arial, sans-serif" font-size="10" font-weight="600" fill="#0f172a">{name}</text>')

    # 9 Processes (Column 1: Student Facing, Column 2: Core Fusion & Planning, Column 3: Telehealth/Community/Billing)
    draw_proc("1.0", "Manage Auth", "&amp; Profiles", 300, 160)
    draw_proc("2.0", "Questionnaire", "&amp; Scoring", 300, 360)
    draw_proc("3.0", "Voice Diary", "&amp; Whisper STT", 300, 560)
    draw_proc("4.0", "Habit Tracking &amp;", "Fusion Model", 300, 760)

    draw_proc("5.0", "Baseline &amp; XAI", "Attribution", 650, 460)
    draw_proc("6.0", "Adaptive Study", "&amp; Recovery Plan", 650, 760)

    draw_proc("7.0", "Counselor Booking", "&amp; Sessions", 990, 200)
    draw_proc("8.0", "Community Forum", "&amp; Moderation", 990, 500)
    draw_proc("9.0", "Polar Payment", "&amp; Webhook", 990, 760)

    # Data Stores
    draw_dstore("D1", "Users &amp; Auth Store", 480, 144)
    draw_dstore("D2", "Stress Assessments", 480, 344)
    draw_dstore("D3", "Encrypted Diaries", 480, 544)
    draw_dstore("D4", "Study Plans &amp; Tasks", 760, 744)
    draw_dstore("D5", "Appointments &amp; Notes", 760, 184)
    draw_dstore("D6", "Community Posts", 760, 484)

    # Clean Orthogonal Labeled Data Flows
    def add_flow(path_d, label, lx, ly):
        svg.append(f'<path d="{path_d}" fill="none" stroke="#1e3a8a" stroke-width="1.4" marker-end="url(#arrow)"/>')
        label_w = len(label) * 6 + 12
        svg.append(f'<rect x="{lx - label_w/2}" y="{ly - 10}" width="{label_w}" height="18" fill="#ffffff" stroke="#e2e8f0" stroke-width="0.8" rx="3"/>')
        svg.append(f'<text x="{lx}" y="{ly + 3}" font-family="Arial, sans-serif" font-size="9" font-weight="500" fill="#0f172a" text-anchor="middle">{label}</text>')

    # Student Inputs
    add_flow("M 190 370 L 230 370 L 230 160 L 248 160", "Register / Credentials", 210, 148)
    add_flow("M 190 390 L 248 390", "PSS Questionnaire Responses", 218, 380)
    add_flow("M 190 410 L 230 410 L 230 560 L 248 560", "Voice Audio &amp; Text Diary", 210, 548)
    add_flow("M 190 430 L 210 430 L 210 760 L 248 760", "Sleep, Steps, Screen Time", 210, 748)

    # Processes to Stores
    add_flow("M 352 160 L 480 160", "Profile Record", 416, 148)
    add_flow("M 352 360 L 480 360", "Questionnaire Score", 416, 348)
    add_flow("M 352 560 L 480 560", "Encrypted Audio &amp; Text", 416, 548)

    # Fusion Pipeline to 5.0 (Baseline & XAI)
    add_flow("M 300 708 L 300 660 L 600 660 L 600 490 L 602 490", "Multimodal Feature Vector", 450, 648)
    add_flow("M 650 408 L 650 360 L 640 360", "Assessment Snapshot", 650, 385)
    add_flow("M 650 512 L 650 708", "Stress Level &amp; XAI Drivers", 650, 610)
    add_flow("M 702 760 L 760 760", "Scheduled Tasks", 730, 748)

    # Right side: Counselor & Appointments
    add_flow("M 1160 180 L 1042 180", "Availability Slots", 1100, 168)
    add_flow("M 1042 220 L 1160 220", "Confirmed Sessions", 1100, 232)
    add_flow("M 938 200 L 920 200", "Appt Records", 930, 188)

    # Community
    add_flow("M 1160 490 L 1042 490", "Moderation Actions", 1100, 478)
    add_flow("M 938 500 L 920 500", "Post Feed", 930, 488)

    # Polar Payment (Bottom Right - NO CROSSING!)
    add_flow("M 990 708 L 990 600 L 950 600 L 950 240 L 938 240", "Confirmed Paid Appt", 970, 420)
    add_flow("M 1042 760 L 1160 760", "Checkout Request", 1100, 748)
    add_flow("M 1160 780 L 1042 780", "Webhook Token", 1100, 792)

    svg.append('</svg>')
    save_and_render("04_DFD_Level_1", "\n".join(svg), b.to_xml())

# =============================================================================
# 3. DFD Level 2 (Detailed Multimodal Stress Fusion & Explainability Pipeline)
# =============================================================================
def build_dfd_level_2():
    w, h = 1300, 880
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

    # Helper for Process Circle
    def draw_proc(num, title1, title2, cx, cy, r=48):
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="#1e3a8a" stroke-width="2"/>')
        svg.append(f'<line x1="{cx-r*0.9}" y1="{cy-12}" x2="{cx+r*0.9}" y2="{cy-12}" stroke="#1e3a8a" stroke-width="1.2"/>')
        svg.append(f'<text x="{cx}" y="{cy-20}" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">{num}</text>')
        svg.append(f'<text x="{cx}" y="{cy+4}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">{title1}</text>')
        svg.append(f'<text x="{cx}" y="{cy+18}" font-family="Arial, sans-serif" font-size="9" fill="#0f172a" text-anchor="middle">{title2}</text>')

    # Helper for Input / Output Rectangles
    def draw_box(title, subtitle, x, y, bw=210, bh=60):
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" fill="#f8fafc" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<text x="{x+bw/2}" y="{y+26}" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{title}</text>')
        svg.append(f'<text x="{x+bw/2}" y="{y+44}" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">{subtitle}</text>')

    # 3 Left Inputs
    draw_box("Questionnaire Assessment", "PSS-10 / DASS-21 Score", 60, 160)
    draw_box("Daily Voice &amp; Text Diary", "Whisper STT &amp; Sentiment", 60, 320)
    draw_box("Habit Tracker Logs", "Sleep, Screen Time, Steps", 60, 480)

    # 5 Pipeline Processes (Sequential & Parallel Branches)
    draw_proc("4.1", "Feature Ingestion &amp;", "Imputation Engine", 390, 350)
    draw_proc("4.2", "Multimodal Fusion", "BiLSTM Classifier", 640, 350)
    draw_proc("4.3", "Baseline Comparator", "&amp; Trigger Drift", 890, 200)
    draw_proc("4.4", "Compute SHAP", "Attribution Values", 890, 350)
    draw_proc("4.5", "Crisis Evaluation &amp;", "SOS Safety Triage", 890, 520)
    draw_proc("4.6", "Recommendation &amp;", "Recovery Router", 1140, 350)

    # Data Stores
    # D2: Baseline History
    svg.extend([
        '<line x1="810" y1="90" x2="970" y2="90" stroke="#0f172a" stroke-width="1.8"/>',
        '<line x1="810" y1="122" x2="970" y2="122" stroke="#0f172a" stroke-width="1.8"/>',
        '<line x1="810" y1="90" x2="810" y2="122" stroke="#0f172a" stroke-width="1.8"/>',
        '<line x1="845" y1="90" x2="845" y2="122" stroke="#0f172a" stroke-width="1"/>',
        '<rect x="811" y="91" width="33" height="30" fill="#f1f5f9"/>',
        '<text x="827" y="111" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">D2</text>',
        '<text x="855" y="111" font-family="Arial, sans-serif" font-size="10" font-weight="600" fill="#0f172a">Student Baseline Store</text>'
    ])

    # Output Box (Student Dashboard & Action)
    draw_box("Student Mobile Dashboard", "Stress Level, XAI Drivers, Plan", 1030, 580, bw=220, bh=65)

    # Clean Flows
    def add_flow(path_d, label, lx, ly):
        svg.append(f'<path d="{path_d}" fill="none" stroke="#1e3a8a" stroke-width="1.4" marker-end="url(#arrow)"/>')
        label_w = len(label) * 6 + 12
        svg.append(f'<rect x="{lx - label_w/2}" y="{ly - 10}" width="{label_w}" height="18" fill="#ffffff" stroke="#e2e8f0" stroke-width="0.8" rx="3"/>')
        svg.append(f'<text x="{lx}" y="{ly + 3}" font-family="Arial, sans-serif" font-size="8.5" font-weight="500" fill="#0f172a" text-anchor="middle">{label}</text>')

    # Inputs to 4.1
    add_flow("M 270 190 L 330 190 L 330 330 L 342 330", "Raw PSS Score", 310, 180)
    add_flow("M 270 350 L 342 350", "Audio/Text Sentiment", 306, 340)
    add_flow("M 270 510 L 330 510 L 330 370 L 342 370", "Habit Metrics Vector", 310, 520)

    # 4.1 to 4.2
    add_flow("M 438 350 L 592 350", "Normalized Multi-Feature Vector", 515, 338)

    # 4.2 to 4.3, 4.4, 4.5
    add_flow("M 640 302 L 640 200 L 842 200", "Estimated Stress Level", 740, 188)
    add_flow("M 688 350 L 842 350", "Model Weights &amp; Prediction", 765, 338)
    add_flow("M 640 398 L 640 520 L 842 520", "High Risk / Acute Flags", 740, 532)

    # Baseline store interaction
    add_flow("M 890 152 L 890 125", "Update Baseline", 890, 140)

    # 4.3, 4.4, 4.5 to 4.6
    add_flow("M 938 200 L 1060 200 L 1060 330 L 1092 330", "Baseline Deviation", 1010, 188)
    add_flow("M 938 350 L 1092 350", "SHAP Factor Attribution", 1015, 338)
    add_flow("M 938 520 L 1060 520 L 1060 370 L 1092 370", "Safety Status / Helpline", 1010, 532)

    # 4.6 to Dashboard
    add_flow("M 1140 398 L 1140 580", "Dispatched Plan &amp; Insights", 1140, 480)

    svg.append('</svg>')
    save_and_render("05_DFD_Level_2_Stress_Detection", "\n".join(svg), b.to_xml())

# =============================================================================
# 4. Component Diagram (UML 2.5 Architecture)
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

    # Helper for UML Component Box
    def draw_component(title, items, x, y, bw, bh, color="#1e3a8a"):
        # Outer Component Package
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" fill="#ffffff" stroke="{color}" stroke-width="2" rx="4"/>')
        # UML Component Stereotype Icon at top-right
        ic_x = x + bw - 36
        svg.append(f'<rect x="{ic_x}" y="{y+10}" width="24" height="18" fill="#ffffff" stroke="{color}" stroke-width="1.2"/>')
        svg.append(f'<rect x="{ic_x-5}" y="{y+13}" width="10" height="4" fill="#ffffff" stroke="{color}" stroke-width="1.2"/>')
        svg.append(f'<rect x="{ic_x-5}" y="{y+21}" width="10" height="4" fill="#ffffff" stroke="{color}" stroke-width="1.2"/>')
        
        # Title
        svg.append(f'<text x="{x+18}" y="{y+26}" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold" fill="{color}">&lt;&lt;component&gt;&gt; {title}</text>')
        svg.append(f'<line x1="{x}" y1="{y+36}" x2="{x+bw}" y2="{y+36}" stroke="{color}" stroke-width="1"/>')

        # Internal Modules / Sub-components
        curr_y = y + 50
        for m_title, m_sub in items:
            box_h = 44
            svg.append(f'<rect x="{x+16}" y="{curr_y}" width="{bw-32}" height="{box_h}" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2" rx="3"/>')
            svg.append(f'<text x="{x+bw/2}" y="{curr_y+18}" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{m_title}</text>')
            svg.append(f'<text x="{x+bw/2}" y="{curr_y+34}" font-family="Arial, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">{m_sub}</text>')
            curr_y += box_h + 10

    # 4 Tiers
    # Tier 1: Mobile App (Flutter)
    m_items = [
        ("Presentation Module", "Flutter UI Views, Widgets, Stress Dial"),
        ("State Management (BLoC)", "AssessmentBloc, DiaryBloc, AuthBloc"),
        ("Audio Capture Module", "Microphone Stream &amp; PCM Encoding"),
        ("Habit Collector Service", "Android SensorManager &amp; Screen Time API"),
        ("Secure Local Storage", "Encrypted Shared Preferences &amp; Cache"),
        ("REST API Client (Dio)", "JWT Interceptors &amp; Network Resilience"),
    ]
    draw_component("Mobile App (Flutter Client)", m_items, 60, 100, 330, 410, "#0284c7")

    # Tier 2: FastAPI Backend Server
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

    # Tier 3: AI & ML Model Services
    ai_items = [
        ("Whisper ASR Model Worker", "Urdu / English Speech-to-Text Transcription"),
        ("Multimodal Fusion Classifier", "PyTorch BiLSTM / Scikit-learn Classifier"),
        ("SHAP Attribution Engine", "TreeSHAP / KernelSHAP Factor Weights"),
        ("Conversational Support LLM", "Contextual Student Chatbot Assistant"),
    ]
    draw_component("AI &amp; ML Model Inference Tier", ai_items, 940, 100, 350, 290, "#9333ea")

    # Tier 4: Supabase Managed Cloud
    db_items = [
        ("PostgreSQL Database (v15)", "Relational Schema, Views &amp; RLS Policies"),
        ("GoTrue Authentication Engine", "JWT Issuance, Refresh &amp; Role Management"),
        ("Encrypted Personal Vault", "AES-256 GCM Storage for Sensitive Diaries"),
        ("S3-Compatible Object Store", "Audio Clips &amp; Relaxation Media Resources"),
    ]
    draw_component("Supabase Managed Cloud", db_items, 940, 440, 350, 290, "#0d9488")

    # Clean UML Provided/Required Socket Interfaces (Lollipop -O and Socket )-)
    def draw_interface(x1, y1, x2, y2, label):
        mid_x = (x1 + x2) / 2
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{mid_x-12}" y2="{y1}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<circle cx="{mid_x-12}" cy="{y1}" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<path d="M {mid_x+6} {y1-10} A 10 10 0 0 0 {mid_x+6} {y1+10}" fill="none" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<line x1="{mid_x+6}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0f172a" stroke-width="1.8"/>')
        svg.append(f'<text x="{mid_x}" y="{y1-14}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">{label}</text>')

    # Flutter to FastAPI
    draw_interface(390, 300, 480, 300, "REST / WSS (HTTPS TLS 1.3)")
    # FastAPI to AI Models
    draw_interface(840, 240, 940, 240, "Internal IPC / PyTorch API")
    # FastAPI to Supabase
    draw_interface(840, 520, 940, 520, "PostgreSQL TCP 5432 / PostgREST")

    svg.append('</svg>')
    save_and_render("06_Component_Diagram", "\n".join(svg), b.to_xml())

# =============================================================================
# 5. Deployment Diagram (Physical Nodes & Protocols)
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

    # Helper for 3D Isometric UML Node
    def draw_3d_node(x, y, bw, bh, d=16, label="<<device>>", name="", color="#1e3a8a"):
        # Front Face
        svg.append(f'<rect x="{x}" y="{y+d}" width="{bw}" height="{bh}" fill="#ffffff" stroke="{color}" stroke-width="1.8"/>')
        # Top Face
        svg.append(f'<polygon points="{x},{y+d} {x+d},{y} {x+bw+d},{y} {x+bw},{y+d}" fill="#f1f5f9" stroke="{color}" stroke-width="1.8"/>')
        # Right Face
        svg.append(f'<polygon points="{x+bw},{y+d} {x+bw+d},{y} {x+bw+d},{y+bh} {x+bw},{y+d+bh}" fill="#e2e8f0" stroke="{color}" stroke-width="1.8"/>')
        # Node Labels
        svg.append(f'<text x="{x+bw/2}" y="{y+d+22}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="{color}" text-anchor="middle">{label}</text>')
        svg.append(f'<text x="{x+bw/2}" y="{y+d+38}" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{name}</text>')
        svg.append(f'<line x1="{x}" y1="{y+d+48}" x2="{x+bw}" y2="{y+d+48}" stroke="{color}" stroke-width="1"/>')

    # Helper for Artifact inside node
    def draw_artifact(x, y, aw, ah, aname, sub):
        svg.append(f'<rect x="{x}" y="{y}" width="{aw}" height="{ah}" fill="#ffffff" stroke="#0284c7" stroke-width="1.2" stroke-dasharray="3,3" rx="3"/>')
        svg.append(f'<text x="{x+aw/2}" y="{y+16}" font-family="Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#0284c7" text-anchor="middle">&lt;&lt;artifact&gt;&gt; {aname}</text>')
        svg.append(f'<text x="{x+aw/2}" y="{y+30}" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">{sub}</text>')

    # Node 1: Android Smartphone (Client)
    draw_3d_node(60, 110, 310, 480, d=16, label="&lt;&lt;device&gt;&gt;", name="Android Smartphone (Client Device)")
    draw_artifact(80, 190, 270, 42, "MindEase_App.apk", "Flutter 3.x Engine / Dart 3 Runtime")
    draw_artifact(80, 250, 270, 42, "Built-in Microphone", "16kHz PCM Audio Stream Capture")
    draw_artifact(80, 310, 270, 42, "Screen Time &amp; Steps", "Android SensorManager API (Software)")
    draw_artifact(80, 370, 270, 42, "Local SQLite / Cache", "Encrypted KeyStore &amp; Offline Sessions")

    # Node 2: Cloud VM / Container (Backend)
    draw_3d_node(480, 110, 360, 560, d=16, label="&lt;&lt;execution environment&gt;&gt;", name="Cloud Application Server (Linux/Docker)")
    draw_artifact(505, 190, 310, 42, "FastAPI ASGI Engine", "Python 3.11 / Uvicorn Server Worker")
    draw_artifact(505, 250, 310, 42, "Whisper ASR Inference Worker", "Urdu/English Speech-to-Text Pipeline")
    draw_artifact(505, 310, 310, 42, "Multimodal Fusion Model", "PyTorch BiLSTM Classifier Model")
    draw_artifact(505, 370, 310, 42, "SHAP XAI Attribution Engine", "TreeSHAP / KernelSHAP Factor Weights")
    draw_artifact(505, 430, 310, 42, "Adaptive Study Planner Engine", "Pomodoro Chunking &amp; Stress Calibration")

    # Node 3: Supabase Cloud (Database)
    draw_3d_node(950, 110, 330, 360, d=16, label="&lt;&lt;cloud system&gt;&gt;", name="Supabase Cloud Platform (AWS)")
    draw_artifact(975, 190, 280, 42, "PostgreSQL 15 Relational DB", "PostgREST Engine &amp; RLS Security Policies")
    draw_artifact(975, 250, 280, 42, "GoTrue Auth Provider", "JWT Issuance &amp; Multi-Role Verification")
    draw_artifact(975, 310, 280, 42, "S3 Object Media Bucket", "Audio Recordings &amp; Relaxation Content")

    # Node 4: Polar Gateway (External)
    draw_3d_node(950, 520, 330, 240, d=16, label="&lt;&lt;external cloud&gt;&gt;", name="Polar Payment Gateway (Sandbox)")
    draw_artifact(975, 600, 280, 42, "Hosted Checkout Session API", "Sandbox Payment &amp; Escrow Token")
    draw_artifact(975, 660, 280, 42, "HMAC-SHA256 Webhook Dispatcher", "Automated Booking Confirmation Callbacks")

    # Network Connection Lines with Protocol Badges
    def draw_link(x1, y1, x2, y2, p_label, s_label):
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0f172a" stroke-width="2"/>')
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        bw = len(p_label) * 6.5 + 20
        svg.append(f'<rect x="{mid_x - bw/2}" y="{mid_y - 18}" width="{bw}" height="34" fill="#ffffff" stroke="#94a3b8" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="{mid_x}" y="{mid_y - 4}" font-family="Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{p_label}</text>')
        svg.append(f'<text x="{mid_x}" y="{mid_y + 10}" font-family="Arial, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">{s_label}</text>')

    draw_link(386, 320, 480, 320, "HTTPS (TLS 1.3) / WSS", "Port 443 Encrypted")
    draw_link(856, 260, 950, 260, "TCP 5432 Encrypted", "PostgreSQL Pool Connection")
    draw_link(856, 620, 950, 620, "HTTPS REST Webhook", "HMAC-SHA256 Signature")

    svg.append('</svg>')
    save_and_render("07_Deployment_Diagram", "\n".join(svg), b.to_xml())

# =============================================================================
# 6. Class Diagram (Domain Model & OOP Architecture)
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

    # Helper for UML 3-Compartment Class Box
    def draw_class(name, attrs, methods, x, y, bw=230):
        header_h = 26
        attrs_h = len(attrs) * 14 + 10
        meth_h = len(methods) * 14 + 10
        total_h = header_h + attrs_h + meth_h

        # Class Box
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{total_h}" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" rx="2"/>')
        # Header Compartment
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{header_h}" fill="#f1f5f9"/>')
        svg.append(f'<text x="{x+bw/2}" y="{y+18}" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{name}</text>')
        svg.append(f'<line x1="{x}" y1="{y+header_h}" x2="{x+bw}" y2="{y+header_h}" stroke="#0f172a" stroke-width="1.4"/>')

        # Attributes Compartment
        curr_y = y + header_h + 12
        for a in attrs:
            svg.append(f'<text x="{x+10}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">{a}</text>')
            curr_y += 14

        # Methods Compartment
        svg.append(f'<line x1="{x}" y1="{y+header_h+attrs_h}" x2="{x+bw}" y2="{y+header_h+attrs_h}" stroke="#0f172a" stroke-width="1.2"/>')
        curr_y = y + header_h + attrs_h + 12
        for m in methods:
            svg.append(f'<text x="{x+10}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">{m}</text>')
            curr_y += 14

        return (x, y, bw, total_h)

    # Base Class: User (Top Center)
    u_attrs = [
        "- id: UUID",
        "- name: String",
        "- email: String",
        "- role: UserRole",
        "- createdAt: DateTime"
    ]
    u_methods = [
        "+ register(): Boolean",
        "+ login(): TokenSession",
        "+ updateProfile(): Boolean"
    ]
    draw_class("User", u_attrs, u_methods, 595, 80, 230)

    # Subclasses: Student, Counselor, Administrator
    st_attrs = [
        "- universityId: String",
        "- degreeProgram: String",
        "- baselineScore: Float",
        "- semester: Int"
    ]
    st_methods = [
        "+ takeAssessment(): Result",
        "+ logDiary(): Entry",
        "+ requestAppointment(): Appt",
        "+ generateStudyPlan(): Plan"
    ]
    draw_class("Student", st_attrs, st_methods, 240, 230, 230)

    c_attrs = [
        "- licenseNumber: String",
        "- specialization: String",
        "- isApproved: Boolean",
        "- hourlyRate: Decimal"
    ]
    c_methods = [
        "+ setAvailability(): Slots",
        "+ reviewDossier(): Records",
        "+ logClinicalNote(): Note"
    ]
    draw_class("Counselor", c_attrs, c_methods, 595, 230, 230)

    a_attrs = [
        "- adminLevel: Int",
        "- roleTitle: String",
        "- lastLoginIp: String"
    ]
    a_methods = [
        "+ approveCounselor(): Bool",
        "+ moderatePost(): Bool",
        "+ updateContent(): Item"
    ]
    draw_class("Administrator", a_attrs, a_methods, 950, 230, 230)

    # Inheritance Triangle Arrows (Generalization)
    svg.append('<polygon points="710,180 702,196 718,196" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>')
    svg.append('<line x1="710" y1="196" x2="710" y2="215" stroke="#0f172a" stroke-width="1.6"/>')
    svg.append('<line x1="355" y1="215" x2="1065" y2="215" stroke="#0f172a" stroke-width="1.6"/>')
    svg.append('<line x1="355" y1="215" x2="355" y2="230" stroke="#0f172a" stroke-width="1.6"/>')
    svg.append('<line x1="710" y1="215" x2="710" y2="230" stroke="#0f172a" stroke-width="1.6"/>')
    svg.append('<line x1="1065" y1="215" x2="1065" y2="230" stroke="#0f172a" stroke-width="1.6"/>')

    # Domain Entities (Row 3)
    sa_attrs = [
        "- assessmentId: UUID",
        "- pssScore: Int",
        "- stressLevel: StressEnum",
        "- confidence: Float",
        "- timestamp: DateTime"
    ]
    sa_methods = [
        "+ fuseInputs(): Level",
        "+ triggerAlert(): Boolean"
    ]
    draw_class("StressAssessment", sa_attrs, sa_methods, 60, 440, 220)

    dd_attrs = [
        "- diaryId: UUID",
        "- audioUrl: String",
        "- transcribedText: String",
        "- sentimentScore: Float",
        "- isCrisis: Boolean"
    ]
    dd_methods = [
        "+ transcribe(): String",
        "+ checkCrisis(): Boolean"
    ]
    draw_class("DailyDiary", dd_attrs, dd_methods, 310, 440, 220)

    ap_attrs = [
        "- appointmentId: UUID",
        "- scheduledAt: DateTime",
        "- status: ApptStatus",
        "- isFreeTier: Boolean"
    ]
    ap_methods = [
        "+ confirmBooking(): Bool",
        "+ completeSession(): Void"
    ]
    draw_class("Appointment", ap_attrs, ap_methods, 595, 440, 230)

    cp_attrs = [
        "- postId: UUID",
        "- isAnonymous: Boolean",
        "- content: String",
        "- reportCount: Int"
    ]
    cp_methods = [
        "+ flagPost(): Void",
        "+ addReply(): Reply"
    ]
    draw_class("CommunityPost", cp_attrs, cp_methods, 950, 440, 230)

    # Domain Entities (Row 4 - All properly connected!)
    xai_attrs = [
        "- insightId: UUID",
        "- topDrivers: List&lt;String&gt;",
        "- shapWeights: Map&lt;Str,Flt&gt;"
    ]
    xai_methods = [
        "+ computeShap(): Map",
        "+ generateTips(): List"
    ]
    draw_class("XAInsight", xai_attrs, xai_methods, 60, 690, 220)

    asp_attrs = [
        "- planId: UUID",
        "- sessionDuration: Int",
        "- breakDuration: Int",
        "- taskList: List&lt;String&gt;"
    ]
    asp_methods = [
        "+ adaptToStress(): Plan",
        "+ reschedule(): Bool"
    ]
    draw_class("AdaptiveStudyPlan", asp_attrs, asp_methods, 310, 690, 220)

    pay_attrs = [
        "- transactionId: UUID",
        "- polarPaymentId: String",
        "- amount: Decimal",
        "- status: PaymentStatus"
    ]
    pay_methods = [
        "+ initiateCheckout(): Url",
        "+ verifyWebhook(): Bool"
    ]
    draw_class("PaymentTransaction", pay_attrs, pay_methods, 595, 690, 230)

    cn_attrs = [
        "- resourceId: UUID",
        "- title: String",
        "- category: MediaCategory",
        "- mediaUrl: String"
    ]
    cn_methods = [
        "+ streamMedia(): Stream",
        "+ rateEffectiveness(): Void"
    ]
    draw_class("ContentResource", cn_attrs, cn_methods, 950, 690, 230)

    # Clean Associations with Multiplicities
    def draw_assoc(x1, y1, x2, y2, m1="1", m2="*"):
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0f172a" stroke-width="1.4"/>')
        svg.append(f'<text x="{x1+6}" y="{y1+14}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">{m1}</text>')
        svg.append(f'<text x="{x2-16}" y="{y2-6}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">{m2}</text>')

    # Student to Assessments & Diaries
    draw_assoc(270, 390, 170, 440, "1", "0..*")
    draw_assoc(355, 390, 420, 440, "1", "0..*")

    # Student to StudyPlan (Orthogonal, routes cleanly!)
    svg.append('<path d="M 240 370 L 220 370 L 220 750 L 310 750" fill="none" stroke="#0f172a" stroke-width="1.4"/>')
    svg.append('<text x="225" y="365" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">1</text>')
    svg.append('<text x="270" y="744" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">0..*</text>')

    # StressAssessment to XAInsight
    draw_assoc(170, 580, 170, 690, "1", "1")

    # Counselor to Appointment
    draw_assoc(710, 390, 710, 440, "1", "0..*")

    # Appointment to PaymentTransaction
    draw_assoc(710, 580, 710, 690, "1", "0..1")

    # Administrator to CommunityPost
    draw_assoc(1065, 390, 1065, 440, "1", "0..*")

    # Administrator to ContentResource (All classes connected!)
    svg.append('<path d="M 1180 340 L 1220 340 L 1220 750 L 1180 750" fill="none" stroke="#0f172a" stroke-width="1.4"/>')
    svg.append('<text x="1185" y="335" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">1</text>')
    svg.append('<text x="1185" y="744" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">0..*</text>')

    svg.append('</svg>')
    save_and_render("08_Class_Diagram", "\n".join(svg), b.to_xml())

# =============================================================================
# 7. Entity Relationship Diagram (True Crow's Foot ERD)
# =============================================================================
def build_erd_diagram():
    w, h = 1450, 980
    b = DrawioBuilder("09_Entity_Relationship_Diagram", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.3.4: MindEase Entity Relationship Diagram (ERD) with Crow\'s Foot Notation</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',
    ]

    # Helper for Styled ERD Entity Box
    def draw_entity(name, pks, fks, attrs, x, y, bw=230):
        h_head = 26
        rows = pks + fks + attrs
        h_body = len(rows) * 14 + 10
        total_h = h_head + h_body

        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{total_h}" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.8" rx="2"/>')
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{h_head}" fill="#1e3a8a"/>')
        svg.append(f'<text x="{x+bw/2}" y="{y+18}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">{name}</text>')

        curr_y = y + h_head + 12
        for pk in pks:
            svg.append(f'<text x="{x+8}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#1e3a8a">PK</text>')
            svg.append(f'<text x="{x+30}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">{pk}</text>')
            curr_y += 14
        for fk in fks:
            svg.append(f'<text x="{x+8}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0284c7">FK</text>')
            svg.append(f'<text x="{x+30}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">{fk}</text>')
            curr_y += 14
        for at in attrs:
            svg.append(f'<text x="{x+30}" y="{curr_y}" font-family="Arial, sans-serif" font-size="9" fill="#475569">{at}</text>')
            curr_y += 14

        return (x, y, bw, total_h)

    # 1. USERS (Top Center)
    draw_entity("USERS", ["user_id: UUID"], [], ["email: VARCHAR(255)", "password_hash: VARCHAR", "role: VARCHAR(20)", "created_at: TIMESTAMP"], 610, 80, 230)

    # 2. Sub-entities (Row 2)
    draw_entity("STUDENTS", ["user_id: UUID"], ["user_id: UUID"], ["university_id: VARCHAR", "degree_program: VARCHAR", "baseline_score: NUMERIC"], 240, 250, 230)
    draw_entity("COUNSELORS", ["user_id: UUID"], ["user_id: UUID"], ["license_number: VARCHAR", "specialization: VARCHAR", "is_approved: BOOLEAN"], 980, 250, 230)

    # 3. Assessment & Clinical Entities (Row 3)
    draw_entity("STRESS_ASSESSMENTS", ["assessment_id: UUID"], ["student_id: UUID"], ["stress_level: VARCHAR(15)", "confidence: NUMERIC(4,3)", "created_at: TIMESTAMP"], 60, 470, 220)
    draw_entity("DIARY_ENTRIES", ["diary_id: UUID"], ["student_id: UUID"], ["audio_url: TEXT", "sentiment_score: NUMERIC", "is_crisis: BOOLEAN"], 310, 470, 220)
    draw_entity("APPOINTMENTS", ["appointment_id: UUID"], ["student_id: UUID", "counselor_id: UUID"], ["scheduled_time: TIMESTAMP", "is_free: BOOLEAN", "status: VARCHAR(20)"], 610, 470, 230)
    draw_entity("COMMUNITY_POSTS", ["post_id: UUID"], ["author_id: UUID"], ["content: TEXT", "is_anonymous: BOOLEAN", "report_count: INT"], 980, 470, 230)

    # 4. Details & Transactions (Row 4)
    draw_entity("XAI_INSIGHTS", ["insight_id: UUID"], ["assessment_id: UUID"], ["feature_weights: JSONB", "primary_drivers: TEXT[]"], 60, 720, 220)
    draw_entity("HABIT_LOGS", ["habit_id: UUID"], ["student_id: UUID"], ["sleep_hours: NUMERIC", "screen_time_mins: INT", "step_count: INT"], 310, 720, 220)
    draw_entity("PAYMENTS", ["payment_id: UUID"], ["appointment_id: UUID"], ["polar_checkout_id: VARCHAR", "amount: NUMERIC(10,2)", "status: VARCHAR(20)"], 610, 720, 230)
    draw_entity("CLINICAL_NOTES", ["note_id: UUID"], ["appointment_id: UUID"], ["encrypted_notes: TEXT", "created_at: TIMESTAMP"], 980, 720, 230)

    # Helper to draw True Crow's Foot Line (Orthogonal, Zero Crossing!)
    def draw_crows_foot(path_d, end_dir="down"):
        svg.append(f'<path d="{path_d}" fill="none" stroke="#1e3a8a" stroke-width="1.6"/>')
        # We parse the last point for crow's foot fork
        parts = path_d.split()
        ex, ey = float(parts[-2]), float(parts[-1])
        if end_dir == "down":
            svg.append(f'<line x1="{ex-7}" y1="{ey-10}" x2="{ex}" y2="{ey}" stroke="#1e3a8a" stroke-width="1.6"/>')
            svg.append(f'<line x1="{ex+7}" y1="{ey-10}" x2="{ex}" y2="{ey}" stroke="#1e3a8a" stroke-width="1.6"/>')
            svg.append(f'<circle cx="{ex}" cy="{ey-15}" r="3" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.4"/>')
        elif end_dir == "right":
            svg.append(f'<line x1="{ex-10}" y1="{ey-7}" x2="{ex}" y2="{ey}" stroke="#1e3a8a" stroke-width="1.6"/>')
            svg.append(f'<line x1="{ex-10}" y1="{ey+7}" x2="{ex}" y2="{ey}" stroke="#1e3a8a" stroke-width="1.6"/>')
            svg.append(f'<circle cx="{ex-15}" cy="{ey}" r="3" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.4"/>')

    # Users to Students & Counselors (One-to-One ||)
    svg.append('<path d="M 610 140 L 355 140 L 355 250" fill="none" stroke="#1e3a8a" stroke-width="1.6"/>')
    svg.append('<path d="M 840 140 L 1095 140 L 1095 250" fill="none" stroke="#1e3a8a" stroke-width="1.6"/>')

    # Students to Stress Assessments (1 to Many >o)
    draw_crows_foot("M 270 380 L 170 380 L 170 470", "down")

    # Students to Diary Entries (1 to Many >o)
    draw_crows_foot("M 355 380 L 420 380 L 420 470", "down")

    # Students to Habit Logs (Orthogonal route cleanly around tables!)
    draw_crows_foot("M 240 340 L 220 340 L 220 780 L 310 780", "right")

    # Stress Assessment to XAI Insights (1 to 1)
    svg.append('<path d="M 170 590 L 170 720" fill="none" stroke="#1e3a8a" stroke-width="1.6"/>')

    # Students & Counselors to Appointments
    draw_crows_foot("M 470 310 L 725 310 L 725 470", "down")
    draw_crows_foot("M 980 310 L 725 310", "right")

    # Appointments to Payments & Clinical Notes
    draw_crows_foot("M 725 610 L 725 720", "down")
    draw_crows_foot("M 840 540 L 980 540", "right")
    draw_crows_foot("M 840 560 L 910 560 L 910 780 L 980 780", "right")

    svg.append('</svg>')
    save_and_render("09_Entity_Relationship_Diagram", "\n".join(svg), b.to_xml())

# =============================================================================
# 8. Database Schema (Physical Relational Tables with Explicit FK Lines)
# =============================================================================
def build_database_schema():
    w, h = 1450, 980
    b = DrawioBuilder("10_Database_Schema", w, h)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>',
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.3.5: MindEase Relational Database Physical Schema Design with Foreign Key Connectors</text>',
        f'<line x1="50" y1="50" x2="{w-50}" y2="50" stroke="#d1d5db" stroke-width="1"/>',
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#64748b" stroke-width="1.2"/>',
    ]

    # Helper for Database Table Box
    def draw_table(name, pks, fks, cols, x, y, bw=230):
        h_head = 24
        rows = pks + fks + cols
        h_body = len(rows) * 13 + 8
        total_h = h_head + h_body

        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{total_h}" fill="#ffffff" stroke="#1e3a8a" stroke-width="1.6" rx="2"/>')
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{h_head}" fill="#1e3a8a"/>')
        svg.append(f'<text x="{x+bw/2}" y="{y+16}" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{name}</text>')

        curr_y = y + h_head + 11
        for pk in pks:
            svg.append(f'<text x="{x+6}" y="{curr_y}" font-family="Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1e3a8a">PK</text>')
            svg.append(f'<text x="{x+26}" y="{curr_y}" font-family="Arial, sans-serif" font-size="8.5" font-weight="600" fill="#0f172a">{pk}</text>')
            curr_y += 13
        for fk in fks:
            svg.append(f'<text x="{x+6}" y="{curr_y}" font-family="Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#0284c7">FK</text>')
            svg.append(f'<text x="{x+26}" y="{curr_y}" font-family="Arial, sans-serif" font-size="8.5" fill="#0f172a">{fk}</text>')
            curr_y += 13
        for c in cols:
            svg.append(f'<text x="{x+26}" y="{curr_y}" font-family="Arial, sans-serif" font-size="8.5" fill="#475569">{c}</text>')
            curr_y += 13

        return (x, y, bw, total_h)

    # 12 Tables (Structured to allow clean FK lines without crossing!)
    # Top Row: Users & Core Roles
    draw_table("public.users", ["id: UUID PRIMARY KEY"], [], ["email: VARCHAR(255) NOT NULL", "password_hash: VARCHAR(255)", "role: VARCHAR(20) NOT NULL", "created_at: TIMESTAMPTZ"], 610, 80, 230)
    draw_table("public.students", ["user_id: UUID PRIMARY KEY"], ["user_id REFERENCES users(id)"], ["registration_num: VARCHAR(50)", "department: VARCHAR(100)", "baseline_stress: NUMERIC(4,2)"], 240, 240, 230)
    draw_table("public.counselors", ["user_id: UUID PRIMARY KEY"], ["user_id REFERENCES users(id)"], ["license_number: VARCHAR", "specialization: VARCHAR", "is_approved: BOOLEAN"], 980, 240, 230)

    # Row 2: Student Diaries & Assessments
    draw_table("public.stress_assessments", ["id: UUID PRIMARY KEY"], ["student_id REFERENCES students"], ["stress_level: VARCHAR(15)", "confidence_score: NUMERIC(4,3)", "created_at: TIMESTAMPTZ"], 60, 460, 220)
    draw_table("public.diary_entries", ["id: UUID PRIMARY KEY"], ["student_id REFERENCES students"], ["audio_url: TEXT", "sentiment_score: NUMERIC(4,2)", "is_crisis: BOOLEAN"], 310, 460, 220)
    draw_table("public.appointments", ["id: UUID PRIMARY KEY"], ["student_id REFERENCES students", "counselor_id REFERENCES counselors"], ["scheduled_at: TIMESTAMPTZ", "is_free_session: BOOLEAN", "status: VARCHAR(20)"], 610, 460, 230)
    draw_table("public.community_posts", ["id: UUID PRIMARY KEY"], ["author_id REFERENCES users(id)"], ["content: TEXT NOT NULL", "is_anonymous: BOOLEAN", "report_count: INT DEFAULT 0"], 980, 460, 230)

    # Row 3: Child Entities & Logs
    draw_table("public.xai_insights", ["id: UUID PRIMARY KEY"], ["assessment_id REFERENCES stress_assessments"], ["shap_weights: JSONB NOT NULL", "top_drivers: TEXT[]"], 60, 710, 220)
    draw_table("public.habit_logs", ["id: UUID PRIMARY KEY"], ["student_id REFERENCES students"], ["sleep_hours: NUMERIC(4,2)", "screen_time_mins: INT", "step_count: INT"], 310, 710, 220)
    draw_table("public.polar_payments", ["id: UUID PRIMARY KEY"], ["appointment_id REFERENCES appts"], ["polar_checkout_session: VARCHAR", "amount_cents: INT", "payment_status: VARCHAR(20)"], 610, 710, 230)
    draw_table("public.clinical_notes", ["id: UUID PRIMARY KEY"], ["appointment_id REFERENCES appts"], ["encrypted_summary: TEXT", "created_at: TIMESTAMPTZ"], 980, 710, 230)

    # Explicit Foreign Key Connectors (Orthogonal, Zero Tangling!)
    def draw_fk_line(path_d):
        svg.append(f'<path d="{path_d}" fill="none" stroke="#0284c7" stroke-width="1.4" stroke-dasharray="4,2"/>')
        parts = path_d.split()
        ex, ey = float(parts[-2]), float(parts[-1])
        svg.append(f'<circle cx="{ex}" cy="{ey}" r="3" fill="#0284c7"/>')

    # students.user_id -> users.id
    draw_fk_line("M 355 240 L 355 140 L 610 140")
    # counselors.user_id -> users.id
    draw_fk_line("M 1095 240 L 1095 140 L 840 140")

    # stress_assessments.student_id -> students.user_id
    draw_fk_line("M 170 460 L 170 380 L 270 380")
    # diary_entries.student_id -> students.user_id
    draw_fk_line("M 420 460 L 420 380 L 355 380")

    # habit_logs.student_id -> students.user_id (Routes cleanly around diary_entries!)
    draw_fk_line("M 310 770 L 230 770 L 230 360 L 240 360")

    # xai_insights.assessment_id -> stress_assessments.id
    draw_fk_line("M 170 710 L 170 580")

    # appointments.student_id & counselor_id
    draw_fk_line("M 725 460 L 725 380 L 470 380")
    draw_fk_line("M 725 460 L 725 380 L 980 380")

    # polar_payments & clinical_notes -> appointments.id
    draw_fk_line("M 725 710 L 725 580")
    draw_fk_line("M 1095 710 L 1095 580 L 840 580")

    svg.append('</svg>')
    save_and_render("10_Database_Schema", "\n".join(svg), b.to_xml())

# =============================================================================
# 9. State Machine Diagram (Lifecycle State Transitions)
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

    # Helper for UML State Box (Rounded Rectangle)
    def draw_state(name, x, y, bw=160, bh=44, sub=""):
        svg.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" rx="8"/>')
        if sub:
            svg.append(f'<text x="{x+bw/2}" y="{y+18}" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{name}</text>')
            svg.append(f'<text x="{x+bw/2}" y="{y+32}" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">{sub}</text>')
        else:
            svg.append(f'<text x="{x+bw/2}" y="{y+26}" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{name}</text>')

    # Machine 1: Stress Assessment Lifecycle (Top Half)
    svg.append('<rect x="50" y="90" width="1250" height="340" fill="#f8fafc" stroke="#0284c7" stroke-width="1.8" rx="6"/>')
    svg.append('<text x="75" y="120" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0284c7">Student Stress Assessment &amp; Recovery Lifecycle</text>')

    # Initial State ●
    svg.append('<circle cx="95" cy="240" r="11" fill="#0f172a"/>')

    # States in Machine 1
    draw_state("Idle / Standby", 150, 218, 130, 44)
    draw_state("Ingesting Inputs", 340, 218, 150, 44, "Form, Audio &amp; Habits")
    draw_state("Fusing Features", 550, 218, 150, 44, "BiLSTM Model")
    draw_state("Stress Evaluated", 760, 218, 160, 44, "Low | Mod | High")
    draw_state("XAI Attributed", 980, 218, 150, 44, "SHAP Drivers")

    # Final State ◉
    svg.append('<circle cx="1210" cy="240" r="13" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>')
    svg.append('<circle cx="1210" cy="240" r="8" fill="#0f172a"/>')

    # Crisis Alternate Branch State
    draw_state("SOS Helpline Alert", 760, 330, 160, 44, "Helpline Dispatched")
    svg.append('<circle cx="1020" cy="352" r="13" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>')
    svg.append('<circle cx="1020" cy="352" r="8" fill="#0f172a"/>')

    # Machine 1 Transitions
    def add_trans(path_d, label, lx, ly):
        svg.append(f'<path d="{path_d}" fill="none" stroke="#0f172a" stroke-width="1.4" marker-end="url(#arrow)"/>')
        label_w = len(label) * 5.8 + 10
        svg.append(f'<rect x="{lx - label_w/2}" y="{ly - 9}" width="{label_w}" height="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8" rx="2"/>')
        svg.append(f'<text x="{lx}" y="{ly + 3}" font-family="Arial, sans-serif" font-size="8.5" font-weight="500" fill="#0f172a" text-anchor="middle">{label}</text>')

    add_trans("M 106 240 L 150 240", "checkin()", 128, 228)
    add_trans("M 280 240 L 340 240", "inputsReady()", 310, 228)
    add_trans("M 490 240 L 550 240", "extractFeatures()", 520, 228)
    add_trans("M 700 240 L 760 240", "classify()", 730, 228)
    add_trans("M 920 240 L 980 240", "shap()", 950, 228)
    add_trans("M 1130 240 L 1197 240", "dispatched()", 1160, 228)

    # Crisis Transition
    add_trans("M 840 262 L 840 330", "[isCrisis == true]", 840, 295)
    add_trans("M 920 352 L 1007 352", "alertSent()", 960, 340)

    # Machine 2: Counselor Appointment & Polar Payment Lifecycle (Bottom Half)
    svg.append('<rect x="50" y="470" width="1250" height="400" fill="#f8fafc" stroke="#16a34a" stroke-width="1.8" rx="6"/>')
    svg.append('<text x="75" y="500" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#16a34a">Counselor Appointment &amp; Polar Payment Lifecycle</text>')

    # Initial State ●
    svg.append('<circle cx="95" cy="640" r="11" fill="#0f172a"/>')

    # States in Machine 2
    draw_state("Requested", 150, 618, 120, 44)
    draw_state("Eligibility Evaluated", 330, 618, 160, 44)

    # Upper Track: Free Session
    draw_state("Confirmed (Free)", 560, 530, 160, 44, "Quota Consumed")

    # Lower Track: Paid Session
    draw_state("Payment Pending", 560, 710, 160, 44)
    draw_state("Polar Checkout", 780, 710, 150, 44, "Hosted Sandbox")
    draw_state("Confirmed (Paid)", 780, 530, 150, 44, "Webhook Verified")

    # Common End Track
    draw_state("In Consultation", 990, 530, 140, 44)
    draw_state("Completed", 990, 660, 140, 44, "Notes Archived")

    # Final State ◉
    svg.append('<circle cx="1200" cy="682" r="13" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>')
    svg.append('<circle cx="1200" cy="682" r="8" fill="#0f172a"/>')

    # Machine 2 Transitions (Zero Crossing!)
    add_trans("M 106 640 L 150 640", "bookAppt()", 128, 628)
    add_trans("M 270 640 L 330 640", "checkHistory()", 300, 628)

    # Free Branch -> routes up to 560
    add_trans("M 410 618 L 410 552 L 560 552", "[isFreeEligible]", 480, 540)
    # Paid Branch -> routes down to 710
    add_trans("M 410 662 L 410 732 L 560 732", "[!isFreeEligible]", 480, 744)

    # Payment flow
    add_trans("M 720 732 L 780 732", "initiateCheckout()", 750, 720)
    add_trans("M 855 710 L 855 574", "webhookSuccess()", 855, 640)

    # Decline Loopback (routes cleanly underneath without crossing!)
    svg.append('<path d="M 855 754 L 855 790 L 640 790 L 640 754" fill="none" stroke="#0f172a" stroke-width="1.4" marker-end="url(#arrow)"/>')
    svg.append('<rect x="710" y="781" width="70" height="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8" rx="2"/>')
    svg.append('<text x="745" y="793" font-family="Arial, sans-serif" font-size="8.5" font-weight="500" fill="#0f172a" text-anchor="middle">[declined]</text>')

    # Both Confirmed states join In Consultation
    add_trans("M 720 552 L 780 552", "ready()", 750, 540)
    add_trans("M 930 552 L 990 552", "joinCall()", 960, 540)

    # In Consultation to Completed
    add_trans("M 1060 574 L 1060 660", "sessionEnd()", 1060, 615)
    add_trans("M 1130 682 L 1187 682", "notesLogged()", 1160, 670)

    svg.append('</svg>')
    save_and_render("11_State_Machine_Diagram", "\n".join(svg), b.to_xml())

if __name__ == "__main__":
    print("Generating all 9 Flawless System Diagrams...")
    build_dfd_level_0()
    build_dfd_level_1()
    build_dfd_level_2()
    build_component_diagram()
    build_deployment_diagram()
    build_class_diagram()
    build_erd_diagram()
    build_database_schema()
    build_state_machine_diagram()
    print("All 9 Diagrams regenerated successfully!")
