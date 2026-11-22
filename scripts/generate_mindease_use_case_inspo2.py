"""
MindEase AI System - Pristine Use Case Diagram conforming to Inspiration Image 2 (Figure 5.1 layout)
100% authentic MindEase domain artifacts, actors, and use cases.
Completely removes 'Edge AI' and 'Inspection' (not in project proposal).
Strictly adheres to:
- Mobile Apps FYP stream
- Flutter Android Frontend + FastAPI AI Backend + Supabase PostgreSQL
- Human actors: Student, Counselor, System Administrator
- Top Centered UC02: Login / Authenticate (JWT)
- 17 Proposal Use Cases (UC01-UC17) matching the 17 Sequence Diagrams
- Lower dashed compartment: 'Automated Backend AI & Cloud Services'
"""
import os
import pymupdf
from drawio_builder import DrawioBuilder

def build_mindease_use_case_inspo2():
    w, h = 1350, 1540
    b = DrawioBuilder("02_Use_Case_Diagram", w, h)

    # SVG Container
    svg_parts = [
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
        
        # Top Figure Caption
        f'<text x="{w/2}" y="38" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.1: UML Use Case Diagram of MindEase AI System</text>',
        f'<line x1="50" y1="52" x2="{w-50}" y2="52" stroke="#d1d5db" stroke-width="1"/>',
        
        # Outer Border Frame
        f'<rect x="25" y="65" width="{w-50}" height="{h-85}" fill="none" stroke="#4b5563" stroke-width="1.2"/>',
        
        # Inner System Boundary
        f'<rect x="250" y="85" width="850" height="{h-125}" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>',
        
        # System Boundary Title Header
        '<text x="675" y="112" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#000000" text-anchor="middle" letter-spacing="1">SYSTEM BOUNDARY: MindEase AI Platform</text>',
        '<line x1="250" y1="124" x2="1100" y2="124" stroke="#000000" stroke-width="1.2"/>',
    ]

    # Draw.io system boundary
    b.add_cell(
        "SYSTEM BOUNDARY: MindEase AI Platform",
        "swimlane;whiteSpace=wrap;html=1;startSize=35;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontFamily=Arial;fontSize=13;fontStyle=1;align=center;",
        x=250, y=85, w=850, h=h-125
    )

    # Centered Top Authentication Use Case: UC02
    uc02_x, uc02_y, uc02_w, uc02_h = 675, 158, 260, 44
    svg_parts.extend([
        f'<ellipse cx="{uc02_x}" cy="{uc02_y}" rx="{uc02_w/2}" ry="{uc02_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.4"/>',
        f'<text x="{uc02_x}" y="{uc02_y-3}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">UC02</text>',
        f'<text x="{uc02_x}" y="{uc02_y+11}" font-family="Arial, sans-serif" font-size="10.5" fill="#000000" text-anchor="middle">Login &amp; Multi-Role Auth (JWT)</text>'
    ])
    b.add_cell(
        "<b>UC02</b><br>Login &amp; Multi-Role Auth (JWT)",
        "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;",
        x=uc02_x-uc02_w/2, y=uc02_y-uc02_h/2, w=uc02_w, h=uc02_h
    )

    # Column geometry
    col_w, col_h = 230, 42
    lc_x = 420
    rc_x = 930

    # Left Column Use Cases (Student Assessment, Tracking & Recovery)
    left_cases = [
        ("UC01", "Register & Onboard Profile", 220, False),
        ("UC03", "Complete Stress Questionnaire", 280, False),
        ("UC04", "Record Daily Voice &amp; Text Diary", 340, False),
        ("UC05", "Log Daily Habits &amp; Biometrics", 400, False),
        ("UC06", "View Stress Trends &amp; Baseline", 470, False),
        ("UC07", "View Explainable AI Insights", 535, False),
        ("UC08", "Access Relaxation Content", 600, False),
        ("UC09", "Chat with AI Support Assistant", 665, False),
        ("UC10", "Generate Adaptive Study Plan", 730, False),
        ("sub_pomodoro", "Calculate Stress-Calibrated Pomodoro", 795, True),
    ]

    for cid, cname, cy, is_sub in left_cases:
        txt_top = "" if is_sub else f'<text x="{lc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>'
        y_name = cy+4 if is_sub else cy+10
        svg_parts.extend([
            f'<ellipse cx="{lc_x}" cy="{cy}" rx="{col_w/2}" ry="{col_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            txt_top,
            f'<text x="{lc_x}" y="{y_name}" font-family="Arial, sans-serif" font-size="9.5" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        label = f"<b>{cid}</b><br>{cname}" if not is_sub else cname
        b.add_cell(
            label,
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;",
            x=lc_x-col_w/2, y=cy-col_h/2, w=col_w, h=col_h
        )

    # Right Column Use Cases (Counseling, Community & Administration)
    right_cases = [
        ("UC11", "Search Counselors &amp; Request Slot", 220, False),
        ("UC12", "Conduct Counseling Session &amp; Notes", 280, False),
        ("UC13", "Process Polar Payment (Test Mode)", 340, False),
        ("UC14", "Create &amp; Interact in Peer Posts", 420, False),
        ("UC15", "Report Inappropriate Post", 485, False),
        ("UC16", "Manage Accounts &amp; Approvals", 600, False),
        ("UC17", "Moderate Content &amp; Logs", 665, False),
    ]

    for cid, cname, cy, is_sub in right_cases:
        svg_parts.extend([
            f'<ellipse cx="{rc_x}" cy="{cy}" rx="{col_w/2}" ry="{col_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            f'<text x="{rc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>',
            f'<text x="{rc_x}" y="{cy+10}" font-family="Arial, sans-serif" font-size="9.5" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        b.add_cell(
            f"<b>{cid}</b><br>{cname}",
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;",
            x=rc_x-col_w/2, y=cy-col_h/2, w=col_w, h=col_h
        )

    # UML Relationships in Upper Section
    # 1. <<extend>> UC07 -> UC06 (XAI extends Stress Trends)
    svg_parts.extend([
        '<path d="M 535 535 L 565 535 L 565 470 L 535 470" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="600" y="505" font-family="Arial, sans-serif" font-size="9" fill="#000000" text-anchor="middle">&lt;&lt;extend&gt;&gt;</text>',
        
        # 2. <<include>> UC10 -> sub_pomodoro (Study Plan includes Pomodoro)
        '<path d="M 535 730 L 565 730 L 565 795 L 535 795" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="600" y="765" font-family="Arial, sans-serif" font-size="9" fill="#000000" text-anchor="middle">&lt;&lt;include&gt;&gt;</text>',

        # 3. <<include>> UC11 -> UC13 (Book appointment includes Polar Payment)
        '<path d="M 815 220 L 785 220 L 785 340 L 815 340" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="750" y="280" font-family="Arial, sans-serif" font-size="9" fill="#000000" text-anchor="middle">&lt;&lt;include&gt;&gt;</text>',

        # 4. <<extend>> UC15 -> UC14 (Report post extends community interaction)
        '<path d="M 815 485 L 785 485 L 785 420 L 815 420" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="750" y="455" font-family="Arial, sans-serif" font-size="9" fill="#000000" text-anchor="middle">&lt;&lt;extend&gt;&gt;</text>',
    ])

    # Lower Dashed Compartment: "Automated Backend AI & Cloud Services"
    dash_x, dash_y, dash_w, dash_h = 265, 855, 820, 580
    svg_parts.extend([
        f'<rect x="{dash_x}" y="{dash_y}" width="{dash_w}" height="{dash_h}" fill="none" stroke="#000000" stroke-width="1.4" stroke-dasharray="5,4"/>',
        f'<text x="{w/2}" y="{dash_y+30}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Automated Backend AI &amp; Cloud Services</text>'
    ])
    b.add_cell(
        "Automated Backend AI & Cloud Services",
        "swimlane;whiteSpace=wrap;html=1;startSize=25;fillColor=none;strokeColor=#000000;strokeWidth=1.5;dashed=1;fontFamily=Arial;fontSize=12;fontStyle=1;align=center;",
        x=dash_x, y=dash_y, w=dash_w, h=dash_h
    )

    auto_lc_x = 445
    auto_rc_x = 905
    auto_w, auto_h = 240, 42

    auto_left = [
        ("SRV01", "Whisper STT Speech-to-Text", 935),
        ("SRV02", "Extract Linguistic &amp; Audio Features", 1015),
        ("SRV03", "Multimodal Stress Fusion (BiLSTM)", 1095),
        ("SRV04", "Trigger Crisis Helpline SOS Alert", 1185),
    ]

    auto_right = [
        ("SRV05", "Compute SHAP Feature Explanations", 935),
        ("SRV06", "Verify Polar Payment Webhooks", 1015),
        ("SRV07", "Sync Encrypted Data to Supabase", 1095),
        ("SRV08", "Redact Sensitive Diary Information", 1185),
    ]

    for cid, cname, cy in auto_left:
        svg_parts.extend([
            f'<ellipse cx="{auto_lc_x}" cy="{cy}" rx="{auto_w/2}" ry="{auto_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            f'<text x="{auto_lc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>',
            f'<text x="{auto_lc_x}" y="{cy+10}" font-family="Arial, sans-serif" font-size="9.5" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        b.add_cell(
            f"<b>{cid}</b><br>{cname}",
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;",
            x=auto_lc_x-auto_w/2, y=cy-auto_h/2, w=auto_w, h=auto_h
        )

    for cid, cname, cy in auto_right:
        svg_parts.extend([
            f'<ellipse cx="{auto_rc_x}" cy="{cy}" rx="{auto_w/2}" ry="{auto_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            f'<text x="{auto_rc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>',
            f'<text x="{auto_rc_x}" y="{cy+10}" font-family="Arial, sans-serif" font-size="9.5" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        b.add_cell(
            f"<b>{cid}</b><br>{cname}",
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;",
            x=auto_rc_x-auto_w/2, y=cy-auto_h/2, w=auto_w, h=auto_h
        )

    # <<extend>> in lower compartment: SRV04 -> SRV03 (crisis SOS alert extends stress fusion)
    svg_parts.extend([
        f'<line x1="{auto_lc_x}" y1="1164" x2="{auto_lc_x}" y2="1116" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        f'<text x="{auto_lc_x+55}" y="1144" font-family="Arial, sans-serif" font-size="9" fill="#000000" text-anchor="middle">&lt;&lt;extend&gt;&gt;</text>',
    ])

    # Stick Figures for Actors
    def draw_actor_svg(cx, cy, label1, label2=""):
        res = [
            f'<circle cx="{cx}" cy="{cy-36}" r="15" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>',
            f'<line x1="{cx}" y1="{cy-21}" x2="{cx}" y2="{cy+14}" stroke="#000000" stroke-width="1.8"/>',
            f'<line x1="{cx-24}" y1="{cy-7}" x2="{cx+24}" y2="{cy-7}" stroke="#000000" stroke-width="1.8"/>',
            f'<line x1="{cx}" y1="{cy+14}" x2="{cx-20}" y2="{cy+48}" stroke="#000000" stroke-width="1.8"/>',
            f'<line x1="{cx}" y1="{cy+14}" x2="{cx+20}" y2="{cy+48}" stroke="#000000" stroke-width="1.8"/>',
            f'<text x="{cx}" y="{cy+70}" font-family="Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#000000" text-anchor="middle">{label1}</text>'
        ]
        if label2:
            res.append(f'<text x="{cx}" y="{cy+85}" font-family="Arial, sans-serif" font-size="10" fill="#444444" text-anchor="middle">{label2}</text>')
        return "\n".join(res)

    # Actors:
    # 1. Left Top: Student (Daily Tracking & Diary)
    svg_parts.append(draw_actor_svg(135, 310, "Student", "(Daily Check-in)"))
    b.add_cell("Student<br>(Daily Check-in)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=110, y=270, w=50, h=90)

    # 2. Left Bottom: Student (Wellness & Study Recovery)
    svg_parts.append(draw_actor_svg(135, 600, "Student", "(Wellness &amp; Study)"))
    b.add_cell("Student<br>(Wellness &amp; Study)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=110, y=560, w=50, h=90)

    # 3. Right Top: Counselor (Mental Health Professional)
    svg_parts.append(draw_actor_svg(1215, 250, "Counselor", "(Mental Health Pro)"))
    b.add_cell("Counselor<br>(Mental Health Pro)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=1190, y=210, w=50, h=90)

    # 4. Right Middle: Student (Appointments & Community)
    svg_parts.append(draw_actor_svg(1215, 420, "Student", "(Community &amp; Booking)"))
    b.add_cell("Student<br>(Community &amp; Booking)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=1190, y=380, w=50, h=90)

    # 5. Right Bottom: System Administrator
    svg_parts.append(draw_actor_svg(1215, 630, "Administrator", "(System Admin)"))
    b.add_cell("Administrator<br>(System Admin)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=1190, y=590, w=50, h=90)

    # Clean Actor Association Lines (NO CROSSING!)
    # Left Actor 1: connects to UC01, UC03, UC04, UC05
    for ty in [220, 280, 340, 400]:
        svg_parts.append(f'<line x1="165" y1="310" x2="{lc_x - col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Left Actor 2: connects to UC06, UC07, UC08, UC09, UC10
    for ty in [470, 535, 600, 665, 730]:
        svg_parts.append(f'<line x1="165" y1="600" x2="{lc_x - col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 1: connects to UC11, UC12
    for ty in [220, 280]:
        svg_parts.append(f'<line x1="1185" y1="250" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 2: connects to UC13, UC14
    for ty in [340, 420]:
        svg_parts.append(f'<line x1="1185" y1="420" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 3: connects to UC16, UC17
    for ty in [600, 665]:
        svg_parts.append(f'<line x1="1185" y1="630" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    svg_parts.append('</svg>')
    svg_final = "\n".join(svg_parts)

    return svg_final, b.to_xml()

def render_and_save():
    svg_content, drawio_content = build_mindease_use_case_inspo2()

    # Paths
    svg_path = os.path.join("Documentation", "Diagrams", "SVG", "02_Use_Case_Diagram.svg")
    drawio_path = os.path.join("Documentation", "Diagrams", "Editable", "02_Use_Case_Diagram.drawio")
    visio_path = os.path.join("Documentation", "Diagrams", "Visio", "02_Use_Case_Diagram.drawio")
    png_path = os.path.join("Documentation", "Diagrams", "PNG", "02_Use_Case_Diagram.png")
    pdf_path = os.path.join("Documentation", "Diagrams", "PDF", "02_Use_Case_Diagram.pdf")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    with open(drawio_path, "w", encoding="utf-8") as f:
        f.write(drawio_content)
    with open(visio_path, "w", encoding="utf-8") as f:
        f.write(drawio_content)

    # Render to PDF and PNG via PyMuPDF
    doc = pymupdf.open("svg", svg_content.encode("utf-8"))
    pdf_bytes = doc.convert_to_pdf()
    doc_pdf = pymupdf.open("pdf", pdf_bytes)
    doc_pdf.save(pdf_path)

    page = doc_pdf[0]
    pix = page.get_pixmap(dpi=300)
    pix.save(png_path)

    print(f"Rendered: {svg_path}")
    print(f"Rendered: {drawio_path}")
    print(f"Rendered: {png_path} ({os.path.getsize(png_path)} bytes)")
    print(f"Rendered: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")

if __name__ == "__main__":
    render_and_save()
