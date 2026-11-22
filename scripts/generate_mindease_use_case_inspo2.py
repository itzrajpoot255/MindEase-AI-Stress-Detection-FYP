"""
MindEase AI System - Pristine Use Case Diagram conforming to Inspiration Image 2 (Figure 5.1 layout)
100% authentic MindEase domain artifacts, actors, and use cases.
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
        '<text x="675" y="112" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#000000" text-anchor="middle" letter-spacing="1">SYSTEM BOUNDARY: MindEase AI</text>',
        '<line x1="250" y1="124" x2="1100" y2="124" stroke="#000000" stroke-width="1.2"/>',
    ]

    # Draw.io system boundary
    b.add_cell(
        "SYSTEM BOUNDARY: MindEase AI",
        "swimlane;whiteSpace=wrap;html=1;startSize=35;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontFamily=Arial;fontSize=13;fontStyle=1;align=center;",
        x=250, y=85, w=850, h=h-125
    )

    # Centered Top Authentication Use Case: UC-00
    uc00_x, uc00_y, uc00_w, uc00_h = 675, 158, 250, 44
    svg_parts.extend([
        f'<ellipse cx="{uc00_x}" cy="{uc00_y}" rx="{uc00_w/2}" ry="{uc00_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.4"/>',
        f'<text x="{uc00_x}" y="{uc00_y-3}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">UC-00</text>',
        f'<text x="{uc00_x}" y="{uc00_y+11}" font-family="Arial, sans-serif" font-size="10.5" fill="#000000" text-anchor="middle">Login / Authenticate (JWT)</text>'
    ])
    b.add_cell(
        "<b>UC-00</b><br>Login / Authenticate (JWT)",
        "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;",
        x=uc00_x-uc00_w/2, y=uc00_y-uc00_h/2, w=uc00_w, h=uc00_h
    )

    # Column geometry
    col_w, col_h = 230, 42
    lc_x = 420
    rc_x = 930

    # Left Column Use Cases (Student Assessment & Self-Care)
    left_cases = [
        ("UC-01", "Register & Onboard Profile", 220, False),
        ("UC-02", "Complete Multilingual Form", 280, False),
        ("UC-03", "Receive Assessment Alerts", 340, False),
        ("UC-04", "Record Daily Voice Diary", 400, False),
        ("UC-05", "View Baseline Stress Map", 470, False),
        ("UC-06", "Inspect XAI Feature Details", 535, False),
        ("UC-07", "Log Habit & Trigger Record", 600, False),
        ("UC-08", "Generate Adaptive Study Plan", 665, False),
        ("sub_pomodoro", "Calculate Adaptive Pomodoro", 730, True),
        ("UC-09", "Generate Wellness Report", 795, False),
    ]

    for cid, cname, cy, is_sub in left_cases:
        txt_top = "" if is_sub else f'<text x="{lc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>'
        y_name = cy+4 if is_sub else cy+10
        svg_parts.extend([
            f'<ellipse cx="{lc_x}" cy="{cy}" rx="{col_w/2}" ry="{col_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            txt_top,
            f'<text x="{lc_x}" y="{y_name}" font-family="Arial, sans-serif" font-size="10" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        label = f"<b>{cid}</b><br>{cname}" if not is_sub else cname
        b.add_cell(
            label,
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;",
            x=lc_x-col_w/2, y=cy-col_h/2, w=col_w, h=col_h
        )

    # Right Column Use Cases (Counseling, Appointment & Administration)
    right_cases = [
        ("UC-10", "View Student Dashboard", 220),
        ("UC-11", "View Stress Statistics", 280),
        ("UC-12", "View Clinical Records", 340),
        ("UC-13", "View Telehealth Schedule", 410),
        ("UC-14", "Book Appointment Session", 475),
        ("UC-15", "Process Polar Payment", 540),
        ("UC-16", "Manage User Accounts", 645),
        ("UC-17", "Configure Clinical Rules", 715),
    ]

    for cid, cname, cy in right_cases:
        svg_parts.extend([
            f'<ellipse cx="{rc_x}" cy="{cy}" rx="{col_w/2}" ry="{col_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            f'<text x="{rc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>',
            f'<text x="{rc_x}" y="{cy+10}" font-family="Arial, sans-serif" font-size="10" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        b.add_cell(
            f"<b>{cid}</b><br>{cname}",
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;",
            x=rc_x-col_w/2, y=cy-col_h/2, w=col_w, h=col_h
        )

    # UML Relationships in Upper Section
    # <<extend>> UC-07 -> UC-06
    svg_parts.extend([
        '<path d="M 535 600 L 565 600 L 565 535 L 535 535" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="600" y="572" font-family="Arial, sans-serif" font-size="9" fill="#000000" text-anchor="middle">&lt;&lt;extend&gt;&gt;</text>',
        
        # <<include>> UC-08 -> sub_pomodoro
        '<path d="M 535 665 L 565 665 L 565 730 L 535 730" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="600" y="702" font-family="Arial, sans-serif" font-size="9" fill="#000000" text-anchor="middle">&lt;&lt;include&gt;&gt;</text>',
    ])

    # Lower Dashed Compartment: "Automated Edge AI & Inspection Processes"
    dash_x, dash_y, dash_w, dash_h = 265, 855, 820, 580
    svg_parts.extend([
        f'<rect x="{dash_x}" y="{dash_y}" width="{dash_w}" height="{dash_h}" fill="none" stroke="#000000" stroke-width="1.4" stroke-dasharray="5,4"/>',
        f'<text x="{w/2}" y="{dash_y+30}" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Automated Edge AI &amp; Inspection Processes</text>'
    ])
    b.add_cell(
        "Automated Edge AI & Inspection Processes",
        "swimlane;whiteSpace=wrap;html=1;startSize=25;fillColor=none;strokeColor=#000000;strokeWidth=1.5;dashed=1;fontFamily=Arial;fontSize=12;fontStyle=1;align=center;",
        x=dash_x, y=dash_y, w=dash_w, h=dash_h
    )

    auto_lc_x = 445
    auto_rc_x = 905
    auto_w, auto_h = 240, 42

    auto_left = [
        ("UC-18", "Capture Biometric Samples", 935),
        ("UC-19", "Read Wearable Pulse &amp; HRV", 1015),
        ("UC-20", "Monitor Stress Reliability", 1095),
        ("UC-21", "Mark Baseline Outlier", 1185),
    ]

    auto_right = [
        ("UC-22", "Detect Multimodal Stress", 935),
        ("UC-23", "Track Triggers Across Sessions", 1015),
        ("UC-24", "Store Records Locally", 1095),
        ("UC-25", "Synchronize Records Online", 1185),
    ]

    for cid, cname, cy in auto_left:
        svg_parts.extend([
            f'<ellipse cx="{auto_lc_x}" cy="{cy}" rx="{auto_w/2}" ry="{auto_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            f'<text x="{auto_lc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>',
            f'<text x="{auto_lc_x}" y="{cy+10}" font-family="Arial, sans-serif" font-size="10" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        b.add_cell(
            f"<b>{cid}</b><br>{cname}",
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;",
            x=auto_lc_x-auto_w/2, y=cy-auto_h/2, w=auto_w, h=auto_h
        )

    for cid, cname, cy in auto_right:
        svg_parts.extend([
            f'<ellipse cx="{auto_rc_x}" cy="{cy}" rx="{auto_w/2}" ry="{auto_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            f'<text x="{auto_rc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>',
            f'<text x="{auto_rc_x}" y="{cy+10}" font-family="Arial, sans-serif" font-size="10" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        b.add_cell(
            f"<b>{cid}</b><br>{cname}",
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;",
            x=auto_rc_x-auto_w/2, y=cy-auto_h/2, w=auto_w, h=auto_h
        )

    # <<extend>> in lower compartment: UC-21 -> UC-20 (bottom to top)
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

    # Actors matching Inspo Image 2 layout with MindEase domain names:
    # 1. Left Top: Student (Self-Care & Daily Ingestion)
    svg_parts.append(draw_actor_svg(135, 300, "Student User", "(Daily Ingestion)"))
    b.add_cell("Student User<br>(Daily Ingestion)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=110, y=260, w=50, h=90)

    # 2. Left Bottom: Student (Recovery & Study Planning)
    svg_parts.append(draw_actor_svg(135, 620, "Student Lead", "(Recovery &amp; Plan)"))
    b.add_cell("Student Lead<br>(Recovery &amp; Plan)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=110, y=580, w=50, h=90)

    # 3. Right Top: Counselor (Mental Health Professional)
    svg_parts.append(draw_actor_svg(1215, 275, "Counselor", "(Mental Health Pro)"))
    b.add_cell("Counselor<br>(Mental Health Pro)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=1190, y=235, w=50, h=90)

    # 4. Right Middle: Telehealth Lead / Consultation Booking
    svg_parts.append(draw_actor_svg(1215, 475, "Telehealth Client", "(Consultation Lead)"))
    b.add_cell("Telehealth Client<br>(Consultation Lead)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=1190, y=435, w=50, h=90)

    # 5. Right Bottom: System Administrator
    svg_parts.append(draw_actor_svg(1215, 680, "System Administrator", "(System Admin)"))
    b.add_cell("System Administrator<br>(System Admin)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=1190, y=640, w=50, h=90)

    # Clean Actor Association Lines (NO CROSSING!)
    # Left Actor 1: connects to UC-01, UC-02, UC-03, UC-04
    for ty in [220, 280, 340, 400]:
        svg_parts.append(f'<line x1="165" y1="300" x2="{lc_x - col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Left Actor 2: connects to UC-05, UC-06, UC-08, UC-09
    for ty in [470, 535, 665, 795]:
        svg_parts.append(f'<line x1="165" y1="620" x2="{lc_x - col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 1: connects to UC-10, UC-11, UC-12
    for ty in [220, 280, 340]:
        svg_parts.append(f'<line x1="1185" y1="275" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 2: connects to UC-13, UC-14, UC-15
    for ty in [410, 475, 540]:
        svg_parts.append(f'<line x1="1185" y1="475" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 3: connects to UC-16, UC-17
    for ty in [645, 715]:
        svg_parts.append(f'<line x1="1185" y1="680" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

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
