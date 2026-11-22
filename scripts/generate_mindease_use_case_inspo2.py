"""
MindEase AI System - Pristine Use Case Diagram conforming to Inspiration Image 2 visual quality.
Completely removes the bottom dashed compartment (No Edge AI, No SRV01-08).
Contains strictly the 17 proposal use cases (UC01 to UC17) matching the 17 Sequence Diagrams.
"""
import os
import pymupdf
from drawio_builder import DrawioBuilder

def build_mindease_use_case_clean():
    w, h = 1250, 1020
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
        f'<text x="{w/2}" y="36" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#000000" text-anchor="middle">Figure 5.1: UML Use Case Diagram of MindEase AI System</text>',
        f'<line x1="40" y1="48" x2="{w-40}" y2="48" stroke="#d1d5db" stroke-width="1"/>',
        
        # Outer Border Frame
        f'<rect x="25" y="60" width="{w-50}" height="{h-80}" fill="none" stroke="#4b5563" stroke-width="1.2"/>',
        
        # Inner System Boundary
        f'<rect x="240" y="78" width="770" height="{h-116}" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>',
        
        # System Boundary Title Header
        '<text x="625" y="104" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#000000" text-anchor="middle" letter-spacing="1">SYSTEM BOUNDARY: MindEase AI Platform</text>',
        '<line x1="240" y1="116" x2="1010" y2="116" stroke="#000000" stroke-width="1.2"/>',
    ]

    # Draw.io system boundary
    b.add_cell(
        "SYSTEM BOUNDARY: MindEase AI Platform",
        "swimlane;whiteSpace=wrap;html=1;startSize=35;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontFamily=Arial;fontSize=13;fontStyle=1;align=center;",
        x=240, y=78, w=770, h=h-116
    )

    # Centered Top Authentication Use Case: UC02
    uc02_x, uc02_y, uc02_w, uc02_h = 625, 148, 250, 42
    svg_parts.extend([
        f'<ellipse cx="{uc02_x}" cy="{uc02_y}" rx="{uc02_w/2}" ry="{uc02_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.4"/>',
        f'<text x="{uc02_x}" y="{uc02_y-3}" font-family="Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#000000" text-anchor="middle">UC02</text>',
        f'<text x="{uc02_x}" y="{uc02_y+11}" font-family="Arial, sans-serif" font-size="10" fill="#000000" text-anchor="middle">Login &amp; Multi-Role Auth (JWT)</text>'
    ])
    b.add_cell(
        "<b>UC02</b><br>Login &amp; Multi-Role Auth (JWT)",
        "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;",
        x=uc02_x-uc02_w/2, y=uc02_y-uc02_h/2, w=uc02_w, h=uc02_h
    )

    # Column geometry
    col_w, col_h = 225, 38
    lc_x = 405
    rc_x = 845

    # Left Column Use Cases (Student Assessment, Tracking & Recovery)
    left_cases = [
        ("UC01", "Register & Onboard Profile", 210, False),
        ("UC03", "Complete Stress Questionnaire", 270, False),
        ("UC04", "Record Daily Voice &amp; Text Diary", 330, False),
        ("UC05", "Log Daily Habits &amp; Biometrics", 390, False),
        ("UC06", "View Stress Trends &amp; Baseline", 465, False),
        ("UC07", "View Explainable AI Insights", 530, False),
        ("UC08", "Access Relaxation Content", 605, False),
        ("UC09", "Chat with AI Support Assistant", 670, False),
        ("UC10", "Generate Adaptive Study Plan", 735, False),
        ("sub_pomodoro", "Calculate Stress-Calibrated Pomodoro", 805, True),
    ]

    for cid, cname, cy, is_sub in left_cases:
        txt_top = "" if is_sub else f'<text x="{lc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>'
        y_name = cy+4 if is_sub else cy+10
        svg_parts.extend([
            f'<ellipse cx="{lc_x}" cy="{cy}" rx="{col_w/2}" ry="{col_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            txt_top,
            f'<text x="{lc_x}" y="{y_name}" font-family="Arial, sans-serif" font-size="9" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        label = f"<b>{cid}</b><br>{cname}" if not is_sub else cname
        b.add_cell(
            label,
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=9.5;",
            x=lc_x-col_w/2, y=cy-col_h/2, w=col_w, h=col_h
        )

    # Right Column Use Cases (Counseling, Community & Administration)
    right_cases = [
        ("UC11", "Search Counselors &amp; Request Slot", 210),
        ("UC12", "Conduct Counseling Session &amp; Notes", 280),
        ("UC13", "Process Polar Payment (Test Mode)", 355),
        ("UC14", "Create &amp; Interact in Peer Posts", 460),
        ("UC15", "Report Inappropriate Post", 530),
        ("UC16", "Manage Accounts &amp; Approvals", 650),
        ("UC17", "Moderate Content &amp; Logs", 725),
    ]

    for cid, cname, cy in right_cases:
        svg_parts.extend([
            f'<ellipse cx="{rc_x}" cy="{cy}" rx="{col_w/2}" ry="{col_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>',
            f'<text x="{rc_x}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">{cid}</text>',
            f'<text x="{rc_x}" y="{cy+10}" font-family="Arial, sans-serif" font-size="9" fill="#000000" text-anchor="middle">{cname}</text>'
        ])
        b.add_cell(
            f"<b>{cid}</b><br>{cname}",
            "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=9.5;",
            x=rc_x-col_w/2, y=cy-col_h/2, w=col_w, h=col_h
        )

    # UML Relationships
    # 1. <<extend>> UC07 -> UC06 (XAI extends Stress Trends)
    svg_parts.extend([
        '<path d="M 518 530 L 545 530 L 545 465 L 518 465" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="580" y="500" font-family="Arial, sans-serif" font-size="8.5" fill="#000000" text-anchor="middle">&lt;&lt;extend&gt;&gt;</text>',
        
        # 2. <<include>> UC10 -> sub_pomodoro (Study Plan includes Pomodoro)
        '<path d="M 518 735 L 545 735 L 545 805 L 518 805" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="580" y="772" font-family="Arial, sans-serif" font-size="8.5" fill="#000000" text-anchor="middle">&lt;&lt;include&gt;&gt;</text>',

        # 3. <<include>> UC11 -> UC13 (Book appointment includes Polar Payment)
        '<path d="M 732 210 L 705 210 L 705 355 L 732 355" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="672" y="285" font-family="Arial, sans-serif" font-size="8.5" fill="#000000" text-anchor="middle">&lt;&lt;include&gt;&gt;</text>',

        # 4. <<extend>> UC15 -> UC14 (Report post extends community interaction)
        '<path d="M 732 530 L 705 530 L 705 460 L 732 460" fill="none" stroke="#000000" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>',
        '<text x="672" y="497" font-family="Arial, sans-serif" font-size="8.5" fill="#000000" text-anchor="middle">&lt;&lt;extend&gt;&gt;</text>',
    ])

    # Stick Figures for Actors
    def draw_actor_svg(cx, cy, label1, label2=""):
        res = [
            f'<circle cx="{cx}" cy="{cy-32}" r="13" fill="#ffffff" stroke="#000000" stroke-width="1.7"/>',
            f'<line x1="{cx}" y1="{cy-19}" x2="{cx}" y2="{cy+12}" stroke="#000000" stroke-width="1.7"/>',
            f'<line x1="{cx-20}" y1="{cy-6}" x2="{cx+20}" y2="{cy-6}" stroke="#000000" stroke-width="1.7"/>',
            f'<line x1="{cx}" y1="{cy+12}" x2="{cx-16}" y2="{cy+42}" stroke="#000000" stroke-width="1.7"/>',
            f'<line x1="{cx}" y1="{cy+12}" x2="{cx+16}" y2="{cy+42}" stroke="#000000" stroke-width="1.7"/>',
            f'<text x="{cx}" y="{cy+62}" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">{label1}</text>'
        ]
        if label2:
            res.append(f'<text x="{cx}" y="{cy+75}" font-family="Arial, sans-serif" font-size="9.5" fill="#444444" text-anchor="middle">{label2}</text>')
        return "\n".join(res)

    # Actors:
    # 1. Left Top: Student (Daily Tracking & Diary)
    svg_parts.append(draw_actor_svg(130, 290, "Student", "(Daily Check-in)"))
    b.add_cell("Student<br>(Daily Check-in)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;fontStyle=1;", x=105, y=255, w=50, h=85)

    # 2. Left Bottom: Student (Wellness & Study Recovery)
    svg_parts.append(draw_actor_svg(130, 640, "Student", "(Wellness &amp; Study)"))
    b.add_cell("Student<br>(Wellness &amp; Study)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;fontStyle=1;", x=105, y=605, w=50, h=85)

    # 3. Right Top: Counselor (Mental Health Professional)
    svg_parts.append(draw_actor_svg(1120, 245, "Counselor", "(Mental Health Pro)"))
    b.add_cell("Counselor<br>(Mental Health Pro)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;fontStyle=1;", x=1095, y=210, w=50, h=85)

    # 4. Right Middle: Student (Appointments & Community)
    svg_parts.append(draw_actor_svg(1120, 485, "Student", "(Community &amp; Booking)"))
    b.add_cell("Student<br>(Community &amp; Booking)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;fontStyle=1;", x=1095, y=450, w=50, h=85)

    # 5. Right Bottom: System Administrator
    svg_parts.append(draw_actor_svg(1120, 685, "Administrator", "(System Admin)"))
    b.add_cell("Administrator<br>(System Admin)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;fontStyle=1;", x=1095, y=650, w=50, h=85)

    # Clean Actor Association Lines (NO CROSSING!)
    # Left Actor 1: connects to UC01, UC03, UC04, UC05
    for ty in [210, 270, 330, 390]:
        svg_parts.append(f'<line x1="160" y1="290" x2="{lc_x - col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Left Actor 2: connects to UC06, UC07, UC08, UC09, UC10
    for ty in [465, 530, 605, 670, 735]:
        svg_parts.append(f'<line x1="160" y1="640" x2="{lc_x - col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 1: connects to UC11, UC12
    for ty in [210, 280]:
        svg_parts.append(f'<line x1="1090" y1="245" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 2: connects to UC13, UC14
    for ty in [355, 460]:
        svg_parts.append(f'<line x1="1090" y1="485" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    # Right Actor 3: connects to UC16, UC17
    for ty in [650, 725]:
        svg_parts.append(f'<line x1="1090" y1="685" x2="{rc_x + col_w/2}" y2="{ty}" stroke="#000000" stroke-width="1.1"/>')

    svg_parts.append('</svg>')
    svg_final = "\n".join(svg_parts)

    return svg_final, b.to_xml()

def render_and_save():
    svg_content, drawio_content = build_mindease_use_case_clean()

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
