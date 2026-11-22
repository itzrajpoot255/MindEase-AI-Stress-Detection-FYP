"""
MindEase FYP - Comprehensive Native Draw.io Diagram Suite Generator
Final Year Project: MindEase - AI-Driven Stress Detection, Recovery & Support for Students
COMSATS University Islamabad, Wah Campus

Generates 100% editable, native Draw.io XML files for ALL MindEase diagrams:
- 11 Core System & Design Diagrams (01 to 11)
- 5 Activity Diagrams (AD01 to AD05)
- 10 UI Mobile Wireframe Diagrams (WF01 to WF10)
- Master Multi-Tab Draw.io Workbook (MindEase_Master_System_Diagrams.drawio)
"""
import os
import xml.etree.ElementTree as ET
from drawio_builder import DrawioBuilder

EDITABLE_DIR = os.path.join("Documentation", "Diagrams", "Editable")
VISIO_DIR = os.path.join("Documentation", "Diagrams", "Visio")
os.makedirs(EDITABLE_DIR, exist_ok=True)
os.makedirs(VISIO_DIR, exist_ok=True)

def save_drawio_file(name, builder):
    p1 = os.path.join(EDITABLE_DIR, f"{name}.drawio")
    p2 = os.path.join(VISIO_DIR, f"{name}.drawio")
    xml_data = builder.to_xml()
    with open(p1, "w", encoding="utf-8") as f:
        f.write(xml_data)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(xml_data)
    print(f"Saved Draw.io file: {name}.drawio ({len(builder.cells)} elements)")
    return p1

# =============================================================================
# 01_System_Architecture
# =============================================================================
def make_system_architecture():
    b = DrawioBuilder("01_System_Architecture", 1400, 1050)
    # Title Frame
    b.add_cell("MindEase AI - Multi-Tier System Architecture", "shape=umlFrame;whiteSpace=wrap;html=1;width=320;height=35;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=14;fontStyle=1;align=center;", x=30, y=20, w=1340, h=1000)

    # Layer 1: Client Presentation Layer
    l1 = b.add_cell("<b>PRESENTATION LAYER (Mobile Client - React Native &amp; Expo)</b>", "swimlane;whiteSpace=wrap;html=1;startSize=28;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=60, y=70, w=1280, h=160)
    c1 = b.add_cell("Student Mobile App<br><small>PSS-10, Audio Diary, SHAP UI, Planner</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l1, x=80, y=40, w=260, h=90)
    c2 = b.add_cell("Counselor Portal<br><small>Slot Management, Dossier Review</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l1, x=380, y=40, w=260, h=90)
    c3 = b.add_cell("Admin Dashboard<br><small>User Approvals, Moderation Logs</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l1, x=680, y=40, w=260, h=90)
    c4 = b.add_cell("Offline Cache &amp; Storage<br><small>WatermelonDB / MMKV Encrypted</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l1, x=980, y=40, w=240, h=90)

    # Layer 2: API Gateway & Application Layer
    l2 = b.add_cell("<b>APPLICATION &amp; GATEWAY LAYER (FastAPI &amp; JWT Microservices)</b>", "swimlane;whiteSpace=wrap;html=1;startSize=28;fillColor=#f0fdf4;strokeColor=#15803d;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=60, y=260, w=1280, h=170)
    g1 = b.add_cell("API Gateway &amp; Reverse Proxy<br><small>HTTPS / TLS 1.3, Rate Limiting</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l2, x=80, y=45, w=260, h=95)
    g2 = b.add_cell("JWT Auth &amp; RBAC Guard<br><small>Multi-Role Access Control</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l2, x=380, y=45, w=260, h=95)
    g3 = b.add_cell("Assessment &amp; Habit Service<br><small>PSS-10 Ingestion, Habit Logs</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l2, x=680, y=45, w=260, h=95)
    g4 = b.add_cell("Counselor &amp; Peer Forum Service<br><small>Polar Webhooks, Feed Moderation</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l2, x=980, y=45, w=240, h=95)

    # Layer 3: AI / ML Inference Pipeline
    l3 = b.add_cell("<b>INTELLIGENT AI &amp; ML SERVICES LAYER (PyTorch, Whisper, SHAP)</b>", "swimlane;whiteSpace=wrap;html=1;startSize=28;fillColor=#fefce8;strokeColor=#ca8a04;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=60, y=460, w=1280, h=170)
    m1 = b.add_cell("Whisper ASR Audio Engine<br><small>OpenAI Whisper-v3, Urdu/English STT</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d97706;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l3, x=80, y=45, w=260, h=95)
    m2 = b.add_cell("Multimodal BiLSTM Fusion<br><small>Acoustic + NLP + Habit Vectors (89% Acc)</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d97706;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l3, x=380, y=45, w=260, h=95)
    m3 = b.add_cell("SHAP XAI Attribution Engine<br><small>Feature Shapley Values &amp; Triggers</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d97706;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l3, x=680, y=45, w=260, h=95)
    m4 = b.add_cell("Adaptive Study Scheduler<br><small>Calibrated Pomodoro Interval Engine</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d97706;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l3, x=980, y=45, w=240, h=95)

    # Layer 4: Data & Cloud Infrastructure Layer
    l4 = b.add_cell("<b>DATA PERSISTENCE &amp; CLOUD INFRASTRUCTURE (Supabase, Vault, Polar)</b>", "swimlane;whiteSpace=wrap;html=1;startSize=28;fillColor=#faf5ff;strokeColor=#7e22ce;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=60, y=660, w=1280, h=170)
    d1 = b.add_cell("Supabase PostgreSQL DB<br><small>Row-Level Security (RLS), Profiles, Posts</small>", "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#ffffff;strokeColor=#9333ea;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l4, x=80, y=45, w=260, h=95)
    d2 = b.add_cell("AES-256 Encrypted Vault<br><small>Encrypted Student Audio Diaries &amp; Notes</small>", "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#ffffff;strokeColor=#9333ea;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l4, x=380, y=45, w=260, h=95)
    d3 = b.add_cell("Supabase Storage &amp; Edge Sync<br><small>Encrypted S3-Compatible Buckets</small>", "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#ffffff;strokeColor=#9333ea;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l4, x=680, y=45, w=260, h=95)
    d4 = b.add_cell("Polar Payment Gateway<br><small>Merchant API &amp; Webhook Verifier</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#9333ea;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", parent=l4, x=980, y=45, w=240, h=95)

    # Layer 5: Cross-Cutting Concerns
    l5 = b.add_cell("<b>CROSS-CUTTING CONCERNS (Security, Logging, Observability &amp; Ethics)</b>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#475569;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;align=center;", x=60, y=860, w=1280, h=70)
    b.add_cell("Prometheus / Grafana Telemetry", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#64748b;fontFamily=Arial;fontSize=10;", parent=l5, x=40, y=22, w=260, h=35)
    b.add_cell("Zero-Knowledge Anonymization Guard", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#64748b;fontFamily=Arial;fontSize=10;", parent=l5, x=340, y=22, w=280, h=35)
    b.add_cell("Audit Logging &amp; Regulatory Compliance", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#64748b;fontFamily=Arial;fontSize=10;", parent=l5, x=660, y=22, w=280, h=35)
    b.add_cell("Automated Crisis Helpline Trigger", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#64748b;fontFamily=Arial;fontSize=10;", parent=l5, x=980, y=22, w=260, h=35)

    # Inter-layer Connectors
    b.add_cell("HTTPS / REST / WSS", "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", edge=True, source=c1, target=g1)
    b.add_cell("JWT Bearer Validation", "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", edge=True, source=c2, target=g2)
    b.add_cell("Async Task Queue", "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#15803d;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", edge=True, source=g3, target=m2)
    b.add_cell("Feature Attributions", "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#ca8a04;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", edge=True, source=m2, target=m3)
    b.add_cell("Encrypted Data Sync", "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#7e22ce;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", edge=True, source=g3, target=d1)
    b.add_cell("Webhook Callbacks", "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#7e22ce;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", edge=True, source=d4, target=g4)

    save_drawio_file("01_System_Architecture", b)
    return b

# =============================================================================
# 02_Use_Case_Diagram
# =============================================================================
def make_use_case_diagram():
    w, h = 1350, 1000
    b = DrawioBuilder("02_Use_Case_Diagram", w, h)

    # System boundary box
    bnd = b.add_cell("SYSTEM BOUNDARY: MindEase Stress Detection &amp; Support Platform", "swimlane;whiteSpace=wrap;html=1;startSize=35;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2;fontFamily=Arial;fontSize=13;fontStyle=1;align=center;", x=260, y=80, w=830, h=h-120)

    # Centered Top Use Case: UC02
    uc02 = b.add_cell("<b>UC02</b><br>Login &amp; Multi-Role Auth (JWT)", "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", parent=bnd, x=290, y=45, w=250, h=44)

    # 8 Left Use Cases
    col_w, col_h = 240, 42
    lc_x = 55
    left_cases_def = [
        ("UC01", "Register &amp; Onboard Profile", 115),
        ("UC03", "Complete Stress Questionnaire", 180),
        ("UC04", "Record Daily Voice &amp; Text Diary", 245),
        ("UC05", "Log Daily Habits &amp; Biometrics", 310),
        ("UC06", "View Stress Trends &amp; Baseline", 385),
        ("UC07", "View Explainable AI Insights", 465),
        ("UC08", "Access Relaxation Content", 545),
        ("UC09", "Chat with AI Support Assistant", 625),
    ]
    left_nodes = {}
    for cid, cname, cy in left_cases_def:
        node = b.add_cell(f"<b>{cid}</b><br>{cname}", "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.4;fontFamily=Arial;fontSize=9.5;", parent=bnd, x=lc_x, y=cy, w=col_w, h=col_h)
        left_nodes[cid] = node

    # 8 Right Use Cases
    rc_x = 535
    right_cases_def = [
        ("UC10", "Generate Adaptive Study Plan", 115),
        ("UC11", "Search Counselors &amp; Request Slot", 180),
        ("UC12", "Conduct Counseling Session &amp; Notes", 245),
        ("UC13", "Process Polar Payment (Test Mode)", 310),
        ("UC14", "Create &amp; Interact in Peer Posts", 385),
        ("UC15", "Report Inappropriate Post", 465),
        ("UC16", "Manage Accounts &amp; Approvals", 545),
        ("UC17", "Moderate Content &amp; Logs", 625),
    ]
    right_nodes = {}
    for cid, cname, cy in right_cases_def:
        node = b.add_cell(f"<b>{cid}</b><br>{cname}", "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.4;fontFamily=Arial;fontSize=9.5;", parent=bnd, x=rc_x, y=cy, w=col_w, h=col_h)
        right_nodes[cid] = node

    # Actors:
    # 1. Left Top: Student (Assessment & Tracking)
    act_s1 = b.add_cell("Student<br>(Assessment &amp; Tracking)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", x=105, y=250, w=55, h=90)
    # 2. Left Bottom: Student (Intervention & Recovery)
    act_s2 = b.add_cell("Student<br>(Intervention &amp; Recovery)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", x=105, y=575, w=55, h=90)
    # 3. Right Top: Counselor (Mental Health Pro)
    act_c = b.add_cell("Counselor<br>(Mental Health Pro)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", x=1185, y=250, w=55, h=90)
    # 4. Right Middle: Student (Community & Planning)
    act_s3 = b.add_cell("Student<br>(Community &amp; Planning)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", x=1185, y=455, w=55, h=90)
    # 5. Right Bottom: Administrator (System Admin)
    act_a = b.add_cell("Administrator<br>(System Admin)", "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", x=1185, y=660, w=55, h=90)

    # Actor Association Lines
    # Student 1 -> UC01, UC03, UC04, UC05, UC02
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s1, target=left_nodes["UC01"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s1, target=left_nodes["UC03"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s1, target=left_nodes["UC04"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s1, target=left_nodes["UC05"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s1, target=uc02)

    # Student 2 -> UC06, UC07, UC08, UC09
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s2, target=left_nodes["UC06"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s2, target=left_nodes["UC07"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s2, target=left_nodes["UC08"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s2, target=left_nodes["UC09"])

    # Counselor -> UC02, UC11, UC12
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_c, target=uc02)
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_c, target=right_nodes["UC11"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_c, target=right_nodes["UC12"])

    # Student 3 -> UC10, UC11, UC13, UC14, UC15
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s3, target=right_nodes["UC10"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s3, target=right_nodes["UC11"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s3, target=right_nodes["UC13"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s3, target=right_nodes["UC14"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_s3, target=right_nodes["UC15"])

    # Admin -> UC02, UC16, UC17
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_a, target=uc02)
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_a, target=right_nodes["UC16"])
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;", edge=True, source=act_a, target=right_nodes["UC17"])

    # Gutter UML Relationships:
    # <<extend>> UC07 -> UC06
    b.add_cell("&lt;&lt;extend&gt;&gt;", "edgeStyle=orthogonalEdgeStyle;rounded=0;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.2;fontFamily=Arial;fontSize=9;", edge=True, source=left_nodes["UC07"], target=left_nodes["UC06"])
    # <<include>> UC11 -> UC13
    b.add_cell("&lt;&lt;include&gt;&gt;", "edgeStyle=orthogonalEdgeStyle;rounded=0;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.2;fontFamily=Arial;fontSize=9;", edge=True, source=right_nodes["UC11"], target=right_nodes["UC13"])
    # <<extend>> UC15 -> UC14
    b.add_cell("&lt;&lt;extend&gt;&gt;", "edgeStyle=orthogonalEdgeStyle;rounded=0;dashed=1;html=1;strokeColor=#000000;strokeWidth=1.2;fontFamily=Arial;fontSize=9;", edge=True, source=right_nodes["UC15"], target=right_nodes["UC14"])

    save_drawio_file("02_Use_Case_Diagram", b)
    return b

# =============================================================================
# 03_DFD_Level_0 (Context Diagram)
# =============================================================================
def make_dfd_level_0():
    w, h = 1600, 950
    b = DrawioBuilder("03_DFD_Level_0", w, h)
    b.add_cell("Figure 5.3.1: DFD Level 0 (Context Diagram) for MindEase System", "shape=umlFrame;whiteSpace=wrap;html=1;width=420;height=35;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=13;fontStyle=1;align=center;", x=30, y=20, w=1540, h=910)

    # Central System Bubble 0.0
    p0 = b.add_cell("<b>0.0</b><br><br><b>MindEase AI Stress Detection,<br>Recovery &amp; Support System</b>", "ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=2.5;fontFamily=Arial;fontSize=12;align=center;", x=650, y=340, w=300, h=300)

    # 4 External Entities
    e_student = b.add_cell("<b>Student</b><br><small>(Primary User)</small>", "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=12;", x=80, y=140, w=220, h=90)
    e_counselor = b.add_cell("<b>Counselor</b><br><small>(Mental Health Professional)</small>", "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=12;", x=1300, y=140, w=220, h=90)
    e_polar = b.add_cell("<b>Polar Gateway</b><br><small>(External Payment Service)</small>", "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=12;", x=80, y=720, w=220, h=90)
    e_admin = b.add_cell("<b>Administrator</b><br><small>(System Admin)</small>", "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=12;", x=1300, y=720, w=220, h=90)

    # Connecting Flow Arrows
    b.add_cell("Questionnaire Responses, Voice Diary, Habit Logs", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", edge=True, source=e_student, target=p0)
    b.add_cell("Stress Level (L/M/H), XAI Insights, Adaptive Study Plan", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", edge=True, source=p0, target=e_student)

    b.add_cell("Availability Slots, Clinical Assessment Notes", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", edge=True, source=e_counselor, target=p0)
    b.add_cell("Booking Requests, Consented Student Dossiers", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", edge=True, source=p0, target=e_counselor)

    b.add_cell("Checkout Session Token &amp; Booking Reference", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", edge=True, source=p0, target=e_polar)
    b.add_cell("Webhook Payment Confirmation Token (Success/Decline)", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", edge=True, source=e_polar, target=p0)

    b.add_cell("Moderation Actions, Content Updates, Counselor Approvals", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", edge=True, source=e_admin, target=p0)
    b.add_cell("Reported Community Post Queue, Audit Telemetry Logs", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", edge=True, source=p0, target=e_admin)

    save_drawio_file("03_DFD_Level_0", b)
    return b

# =============================================================================
# 04_DFD_Level_1
# =============================================================================
def make_dfd_level_1():
    w, h = 1750, 1000
    b = DrawioBuilder("04_DFD_Level_1", w, h)
    b.add_cell("Figure 5.3.2: DFD Level 1 (Decomposition Diagram) for MindEase System", "shape=umlFrame;whiteSpace=wrap;html=1;width=450;height=35;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=13;fontStyle=1;", x=30, y=20, w=1690, h=960)

    # 6 Processes
    p1 = b.add_cell("<b>1.0</b><br>User Auth &amp; Profile Management", "ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=450, y=80, w=220, h=80)
    p2 = b.add_cell("<b>2.0</b><br>Assessments &amp; Diary Ingestion", "ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=450, y=230, w=220, h=80)
    p3 = b.add_cell("<b>3.0</b><br>Multimodal AI Stress Detection", "ellipse;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#d97706;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=450, y=390, w=220, h=80)
    p4 = b.add_cell("<b>4.0</b><br>Adaptive Study Plan Engine", "ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=450, y=550, w=220, h=80)
    p5 = b.add_cell("<b>5.0</b><br>Counselor Booking &amp; Polar Payment", "ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=450, y=700, w=220, h=80)
    p6 = b.add_cell("<b>6.0</b><br>Peer Community &amp; Moderation", "ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=450, y=850, w=220, h=80)

    # External Entities
    e_student = b.add_cell("<b>Student</b>", "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=12;", x=80, y=350, w=160, h=120)
    e_counselor = b.add_cell("<b>Counselor</b>", "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=12;", x=1480, y=550, w=160, h=100)
    e_polar = b.add_cell("<b>Polar Gateway</b>", "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=12;", x=80, y=700, w=160, h=80)
    e_admin = b.add_cell("<b>Administrator</b>", "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;fontFamily=Arial;fontSize=12;", x=1480, y=850, w=160, h=80)

    # 5 Data Stores
    d1 = b.add_cell("<b>D1: Users &amp; Profiles</b>", "shape=partialRectangle;right=0;left=0;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=980, y=95, w=220, h=50)
    d2 = b.add_cell("<b>D2: Stress Logs &amp; Audio Vault</b>", "shape=partialRectangle;right=0;left=0;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=980, y=310, w=220, h=50)
    d3 = b.add_cell("<b>D3: Adaptive Study Plans</b>", "shape=partialRectangle;right=0;left=0;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=980, y=565, w=220, h=50)
    d4 = b.add_cell("<b>D4: Appointments &amp; Payments</b>", "shape=partialRectangle;right=0;left=0;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=980, y=715, w=220, h=50)
    d5 = b.add_cell("<b>D5: Community Posts &amp; Reports</b>", "shape=partialRectangle;right=0;left=0;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=980, y=865, w=220, h=50)

    # Connections
    b.add_cell("Credentials", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_student, target=p1)
    b.add_cell("User Record", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=p1, target=d1)
    b.add_cell("Voice / PSS-10", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_student, target=p2)
    b.add_cell("Processed Features", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=p2, target=p3)
    b.add_cell("Store Assessment", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=p3, target=d2)
    b.add_cell("Calibrated Stress Level", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=p3, target=p4)
    b.add_cell("Save Plan Tasks", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=p4, target=d3)
    b.add_cell("Study Schedule", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=p4, target=e_student)
    b.add_cell("Book Appointment", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_student, target=p5)
    b.add_cell("Checkout Webhook", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_polar, target=p5)
    b.add_cell("Confirmed Slot", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=p5, target=d4)
    b.add_cell("Booking Dossier", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=d4, target=e_counselor)
    b.add_cell("Forum Post / Flag", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_student, target=p6)
    b.add_cell("Store Moderated Post", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=p6, target=d5)
    b.add_cell("Flagged Queue Action", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_admin, target=p6)

    save_drawio_file("04_DFD_Level_1", b)
    return b

# =============================================================================
# 05_DFD_Level_2_Stress_Detection
# =============================================================================
def make_dfd_level_2():
    w, h = 1500, 920
    b = DrawioBuilder("05_DFD_Level_2_Stress_Detection", w, h)
    b.add_cell("Figure 5.3.3: DFD Level 2 (Sub-Process 3.0: AI Stress Detection Pipeline)", "shape=umlFrame;whiteSpace=wrap;html=1;width=480;height=35;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=13;fontStyle=1;", x=30, y=20, w=1440, h=880)

    # Sub-processes
    p31 = b.add_cell("<b>3.1</b><br>Ingest Raw Multi-Sensor Data<br><small>(Voice Audio + PSS-10 + Habits)</small>", "ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=80, y=360, w=220, h=90)
    p32 = b.add_cell("<b>3.2</b><br>Whisper STT &amp; Feature Extraction<br><small>(Acoustic Prosody + NLP Vectors)</small>", "ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=380, y=360, w=240, h=90)
    p33 = b.add_cell("<b>3.3</b><br>Multimodal BiLSTM Fusion Model<br><small>(Early/Late Fusion Classification)</small>", "ellipse;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#d97706;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=700, y=360, w=240, h=90)
    p34 = b.add_cell("<b>3.4</b><br>SHAP Explainability Computation<br><small>(Feature Importance Weights)</small>", "ellipse;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=1020, y=360, w=230, h=90)
    p35 = b.add_cell("<b>3.5</b><br>Dispatch Alert &amp; Clinical Action<br><small>(SOS Crisis or Calibrated Plan)</small>", "ellipse;whiteSpace=wrap;html=1;fillColor=#fee2e2;strokeColor=#dc2626;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=1020, y=600, w=230, h=90)

    # Stores
    d_vault = b.add_cell("<b>D2.1: AES-256 Audio Vault</b>", "shape=partialRectangle;right=0;left=0;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=380, y=180, w=240, h=50)
    d_model = b.add_cell("<b>D2.2: Pre-trained Weights</b>", "shape=partialRectangle;right=0;left=0;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=700, y=180, w=240, h=50)
    d_stress = b.add_cell("<b>D2.3: Stress History DB</b>", "shape=partialRectangle;right=0;left=0;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=2;fontFamily=Arial;fontSize=11;", x=1020, y=180, w=230, h=50)

    # Connections
    b.add_cell("Raw Audio &amp; Form Data", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;", edge=True, source=p31, target=p32)
    b.add_cell("Sync Raw Audio", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=p31, target=d_vault)
    b.add_cell("Normalized Feature Vectors", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;", edge=True, source=p32, target=p33)
    b.add_cell("Model Embeddings", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=d_model, target=p33)
    b.add_cell("Fusion Stress Score", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;", edge=True, source=p33, target=p34)
    b.add_cell("Store Inferred Level", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=p34, target=d_stress)
    b.add_cell("High Severity Trigger", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#dc2626;strokeWidth=1.5;", edge=True, source=p34, target=p35)

    save_drawio_file("05_DFD_Level_2_Stress_Detection", b)
    return b

# =============================================================================
# 06_Component_Diagram
# =============================================================================
def make_component_diagram():
    w, h = 1350, 900
    b = DrawioBuilder("06_Component_Diagram", w, h)
    b.add_cell("Figure 5.4.1: UML Component Diagram for MindEase Platform", "shape=umlFrame;whiteSpace=wrap;html=1;width=420;height=35;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=13;fontStyle=1;", x=30, y=20, w=1290, h=860)

    # Package: Client Side
    p_client = b.add_cell("Client Application (Mobile Front-End)", "swimlane;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=60, y=80, w=340, h=760)
    c_ui = b.add_cell("«component»<br><b>Mobile UI Navigation</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;", parent=p_client, x=40, y=60, w=260, h=80)
    c_audio = b.add_cell("«component»<br><b>Audio Recording Handler</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;", parent=p_client, x=40, y=190, w=260, h=80)
    c_quest = b.add_cell("«component»<br><b>PSS-10 Assessment Engine</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;", parent=p_client, x=40, y=320, w=260, h=80)
    c_planner = b.add_cell("«component»<br><b>Adaptive Study Planner UI</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;", parent=p_client, x=40, y=450, w=260, h=80)
    c_cache = b.add_cell("«component»<br><b>Encrypted Local Cache</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;", parent=p_client, x=40, y=580, w=260, h=80)

    # Package: Backend Services
    p_srv = b.add_cell("FastAPI Backend Microservices", "swimlane;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#15803d;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=460, y=80, w=420, h=760)
    c_auth = b.add_cell("«component»<br><b>Auth &amp; RBAC Controller</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;", parent=p_srv, x=40, y=60, w=340, h=75)
    c_stress_svc = b.add_cell("«component»<br><b>Stress Pipeline Coordinator</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;", parent=p_srv, x=40, y=170, w=340, h=75)
    c_whisper = b.add_cell("«component»<br><b>Whisper STT &amp; Prosody Service</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;", parent=p_srv, x=40, y=280, w=340, h=75)
    c_bilstm = b.add_cell("«component»<br><b>Multimodal BiLSTM Fusion Model</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;", parent=p_srv, x=40, y=390, w=340, h=75)
    c_shap = b.add_cell("«component»<br><b>SHAP Attribution Explainer</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;", parent=p_srv, x=40, y=500, w=340, h=75)
    c_booking = b.add_cell("«component»<br><b>Counselor Booking &amp; Polar Bridge</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;", parent=p_srv, x=40, y=610, w=340, h=75)

    # Package: Cloud & Storage
    p_cloud = b.add_cell("Data Persistence &amp; External APIs", "swimlane;whiteSpace=wrap;html=1;fillColor=#faf5ff;strokeColor=#7e22ce;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=940, y=80, w=350, h=760)
    c_db = b.add_cell("«component»<br><b>Supabase Cloud PostgreSQL</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#9333ea;", parent=p_cloud, x=40, y=100, w=270, h=80)
    c_vault = b.add_cell("«component»<br><b>Encrypted Diary Storage Vault</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#9333ea;", parent=p_cloud, x=40, y=270, w=270, h=80)
    c_polar = b.add_cell("«component»<br><b>Polar.sh Merchant API</b>", "shape=module;align=left;spacingLeft=20;align=center;verticalAlign=top;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#9333ea;", parent=p_cloud, x=40, y=450, w=270, h=80)

    # Connectors
    b.add_cell("REST / HTTPS", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;", edge=True, source=c_ui, target=c_auth)
    b.add_cell("Audio Upload", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;", edge=True, source=c_audio, target=c_stress_svc)
    b.add_cell("Dispatch STT", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#15803d;strokeWidth=1.5;", edge=True, source=c_stress_svc, target=c_whisper)
    b.add_cell("Acoustic Features", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#15803d;strokeWidth=1.5;", edge=True, source=c_whisper, target=c_bilstm)
    b.add_cell("Feature Explanations", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#15803d;strokeWidth=1.5;", edge=True, source=c_bilstm, target=c_shap)
    b.add_cell("Persist Vectors", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#7e22ce;strokeWidth=1.5;", edge=True, source=c_stress_svc, target=c_db)
    b.add_cell("AES-256 Sync", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#7e22ce;strokeWidth=1.5;", edge=True, source=c_audio, target=c_vault)
    b.add_cell("Webhook Verify", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#7e22ce;strokeWidth=1.5;", edge=True, source=c_polar, target=c_booking)

    save_drawio_file("06_Component_Diagram", b)
    return b

# =============================================================================
# 07_Deployment_Diagram
# =============================================================================
def make_deployment_diagram():
    w, h = 1350, 900
    b = DrawioBuilder("07_Deployment_Diagram", w, h)
    b.add_cell("Figure 5.4.2: UML Deployment Diagram for MindEase Platform", "shape=umlFrame;whiteSpace=wrap;html=1;width=420;height=35;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=13;fontStyle=1;", x=30, y=20, w=1290, h=860)

    # Node: Student Client
    n_client = b.add_cell("«device»<br><b>Student Mobile Smartphone</b><br><small>iOS 15+ / Android 11+</small>", "shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;darkOpacity=0.05;darkOpacity2=0.1;size=20;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=60, y=100, w=300, h=300)
    a_apk = b.add_cell("«artifact»<br><b>MindEase Mobile Client.apk</b><br><small>React Native Runtime, MMKV Cache</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.2;", parent=n_client, x=30, y=70, w=240, h=80)

    # Node: Counselor Client
    n_counselor = b.add_cell("«device»<br><b>Counselor Workstation</b><br><small>Desktop Browser / Web App</small>", "shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;darkOpacity=0.05;darkOpacity2=0.1;size=20;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=60, y=480, w=300, h=300)
    a_web = b.add_cell("«artifact»<br><b>Counselor Portal Web Build</b><br><small>React / Vite Dashboard SPA</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#2563eb;strokeWidth=1.2;", parent=n_counselor, x=30, y=70, w=240, h=80)

    # Node: Application Server
    n_server = b.add_cell("«device»<br><b>Cloud Application Host</b><br><small>Ubuntu 22.04 LTS Container</small>", "shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;darkOpacity=0.05;darkOpacity2=0.1;size=20;fillColor=#f0fdf4;strokeColor=#15803d;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=500, y=250, w=340, h=400)
    a_api = b.add_cell("«artifact»<br><b>MindEase FastAPI Backend</b><br><small>Uvicorn ASGI Server, JWT Guard</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;strokeWidth=1.2;", parent=n_server, x=40, y=70, w=260, h=90)
    a_ai = b.add_cell("«artifact»<br><b>PyTorch / Whisper Model Runner</b><br><small>CUDA / TorchServe Inference Engine</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#16a34a;strokeWidth=1.2;", parent=n_server, x=40, y=200, w=260, h=90)

    # Node: Supabase Managed Cloud
    n_db = b.add_cell("«executionEnvironment»<br><b>Supabase Cloud Managed Platform</b><br><small>PostgreSQL 15 + PostgREST + Auth</small>", "shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;darkOpacity=0.05;darkOpacity2=0.1;size=20;fillColor=#faf5ff;strokeColor=#7e22ce;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=960, y=100, w=320, h=320)
    a_db = b.add_cell("«database»<br><b>MindEase Relational Schema</b><br><small>RLS Policies, Triggers, Indexes</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#9333ea;strokeWidth=1.2;", parent=n_db, x=35, y=70, w=250, h=80)
    a_vault = b.add_cell("«storage»<br><b>Encrypted Audio Diary Buckets</b><br><small>AES-256 S3-Compatible Buckets</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#9333ea;strokeWidth=1.2;", parent=n_db, x=35, y=180, w=250, h=80)

    # Node: Polar Payment API
    n_polar = b.add_cell("«cloud»<br><b>Polar Payment Cloud</b><br><small>SaaS Checkout &amp; Webhooks</small>", "shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;darkOpacity=0.05;darkOpacity2=0.1;size=20;fillColor=#fffbeb;strokeColor=#b45309;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=960, y=500, w=320, h=250)
    a_polar = b.add_cell("«service»<br><b>Polar Checkout API</b><br><small>Secure Payment Session Tokens</small>", "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#d97706;strokeWidth=1.2;", parent=n_polar, x=35, y=70, w=250, h=80)

    # Deployment Communications Protocols
    b.add_cell("HTTPS / TLS 1.3 (Port 443)", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;", edge=True, source=n_client, target=n_server)
    b.add_cell("HTTPS / REST (Port 443)", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;", edge=True, source=n_counselor, target=n_server)
    b.add_cell("TCP / TLS (Port 5432 - PostgREST)", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#15803d;strokeWidth=1.5;", edge=True, source=n_server, target=n_db)
    b.add_cell("HTTPS Webhook Post", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#b45309;strokeWidth=1.5;", edge=True, source=n_polar, target=n_server)

    save_drawio_file("07_Deployment_Diagram", b)
    return b

# =============================================================================
# 08_Class_Diagram
# =============================================================================
def make_class_diagram():
    w, h = 1450, 1050
    b = DrawioBuilder("08_Class_Diagram", w, h)
    b.add_cell("Figure 5.4.3: UML Class Diagram for MindEase Object Architecture", "shape=umlFrame;whiteSpace=wrap;html=1;width=450;height=35;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=13;fontStyle=1;", x=30, y=20, w=1390, h=1000)

    # Base User Class
    c_user = b.add_cell("<b>User</b><br>--<br>- id: UUID<br>- email: String<br>- passwordHash: String<br>- role: UserRole<br>- isVerified: Boolean<br>- createdAt: DateTime<br>--<br>+ authenticate(): Boolean<br>+ updateProfile(): Void<br>+ resetPassword(): Void", "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=580, y=70, w=240, h=160)

    # Student Child Class
    c_student = b.add_cell("<b>Student</b><br>--<br>- registrationNo: String<br>- department: String<br>- currentSemester: Int<br>- baselineStress: Float<br>--<br>+ submitAssessment(): UUID<br>+ recordAudioDiary(): UUID<br>+ generateStudyPlan(): Plan<br>+ bookCounselor(): Booking", "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=260, y=280, w=250, h=155)

    # Counselor Child Class
    c_counselor = b.add_cell("<b>Counselor</b><br>--<br>- licenseNumber: String<br>- specialization: String<br>- isVerifiedCounselor: Boolean<br>- hourlyRate: Decimal<br>--<br>+ setAvailability(): Void<br>+ reviewDossier(): Dossier<br>+ recordClinicalNotes(): Void", "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=890, y=280, w=250, h=155)

    # StressAssessment Class
    c_stress = b.add_cell("<b>StressAssessment</b><br>--<br>- id: UUID<br>- studentId: UUID<br>- pssScore: Int<br>- speechStressScore: Float<br>- multimodalFusionScore: Float<br>- classifiedTier: StressTier<br>- createdAt: DateTime<br>--<br>+ computeFusion(): Float<br>+ triggerCrisisAlert(): Boolean", "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#d97706;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=60, y=510, w=260, h=165)

    # XAIInsight Class
    c_xai = b.add_cell("<b>XAIInsight</b><br>--<br>- id: UUID<br>- assessmentId: UUID<br>- shapSleepImpact: Float<br>- shapScreenImpact: Float<br>- shapAcademicImpact: Float<br>- recommendationText: String<br>--<br>+ explainTriggers(): JSON<br>+ getActionableSteps(): List", "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#d97706;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=60, y=760, w=260, h=155)

    # VoiceDiaryEntry Class
    c_voice = b.add_cell("<b>VoiceDiaryEntry</b><br>--<br>- id: UUID<br>- studentId: UUID<br>- audioVaultPath: String<br>- whisperTranscript: String<br>- detectedLanguage: String<br>- acousticPitchVariance: Float<br>--<br>+ decryptAudio(): Bytes<br>+ runWhisperSTT(): Text", "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=390, y=510, w=250, h=165)

    # AdaptiveStudyPlan Class
    c_plan = b.add_cell("<b>AdaptiveStudyPlan</b><br>--<br>- id: UUID<br>- studentId: UUID<br>- focusMinutes: Int<br>- breakMinutes: Int<br>- isStressAdapted: Boolean<br>- scheduledDate: Date<br>--<br>+ rescheduleOverload(): Void<br>+ markTaskComplete(): Void", "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=390, y=760, w=250, h=155)

    # Appointment Class
    c_apt = b.add_cell("<b>Appointment</b><br>--<br>- id: UUID<br>- studentId: UUID<br>- counselorId: UUID<br>- scheduledSlot: DateTime<br>- status: AppointmentStatus<br>- clinicalNotes: String<br>--<br>+ confirmSlot(): Boolean<br>+ cancelAppointment(): Void", "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=760, y=510, w=260, h=165)

    # PaymentTransaction Class
    c_pay = b.add_cell("<b>PaymentTransaction</b><br>--<br>- id: UUID<br>- appointmentId: UUID<br>- polarCheckoutId: String<br>- amount: Decimal<br>- currency: String<br>- paymentStatus: PaymentStatus<br>--<br>+ verifyWebhookToken(): Boolean<br>+ refundTransaction(): Void", "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=760, y=760, w=260, h=155)

    # CommunityPost Class
    c_post = b.add_cell("<b>CommunityPost</b><br>--<br>- id: UUID<br>- authorStudentId: UUID<br>- isAnonymous: Boolean<br>- contentText: String<br>- flagCount: Int<br>- isModerated: Boolean<br>--<br>+ publishPost(): Void<br>+ flagInappropriate(): Void<br>+ removeByAdmin(): Void", "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=1100, y=510, w=250, h=165)

    # Inheritance Lines (Generalization)
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=0;strokeColor=#000000;strokeWidth=1.5;", edge=True, source=c_student, target=c_user)
    b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=0;strokeColor=#000000;strokeWidth=1.5;", edge=True, source=c_counselor, target=c_user)

    # Associations (Composition / Aggregation)
    b.add_cell("1..* assesses", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=c_student, target=c_stress)
    b.add_cell("1 explains", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#d97706;strokeWidth=1.3;", edge=True, source=c_stress, target=c_xai)
    b.add_cell("1..* records", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=c_student, target=c_voice)
    b.add_cell("1 adapts", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=c_student, target=c_plan)
    b.add_cell("1..* books", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=c_student, target=c_apt)
    b.add_cell("1 conducts", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=c_counselor, target=c_apt)
    b.add_cell("1 billings", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=c_apt, target=c_pay)
    b.add_cell("1..* authors", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=c_student, target=c_post)

    save_drawio_file("08_Class_Diagram", b)
    return b

# =============================================================================
# 09_Entity_Relationship_Diagram & 10_Database_Schema
# =============================================================================
def make_erd_diagram():
    w, h = 1450, 1000
    b = DrawioBuilder("09_Entity_Relationship_Diagram", w, h)
    b.add_cell("Figure 5.5.1: Entity-Relationship Diagram (ERD) for MindEase Database", "shape=umlFrame;whiteSpace=wrap;html=1;width=450;height=35;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=13;fontStyle=1;", x=30, y=20, w=1390, h=950)

    # 8 Entities
    e_user = b.add_cell("<b>USERS</b><br>--<br>[PK] user_id: UUID<br>email: VARCHAR(255)<br>password_hash: VARCHAR(255)<br>role: VARCHAR(20)<br>created_at: TIMESTAMPTZ", "swimlane;startSize=24;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=580, y=70, w=240, h=140)
    e_student = b.add_cell("<b>STUDENTS</b><br>--<br>[PK, FK] student_id: UUID<br>reg_number: VARCHAR(50)<br>department: VARCHAR(100)<br>semester: INT<br>baseline_score: NUMERIC(4,2)", "swimlane;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=240, y=270, w=240, h=140)
    e_counselor = b.add_cell("<b>COUNSELORS</b><br>--<br>[PK, FK] counselor_id: UUID<br>license_no: VARCHAR(50)<br>specialization: VARCHAR(100)<br>hourly_rate: NUMERIC(8,2)<br>is_approved: BOOLEAN", "swimlane;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=920, y=270, w=240, h=140)
    e_stress = b.add_cell("<b>STRESS_LOGS</b><br>--<br>[PK] log_id: UUID<br>[FK] student_id: UUID<br>pss_score: INT<br>audio_subscore: NUMERIC(4,2)<br>fusion_level: VARCHAR(20)<br>confidence: NUMERIC(4,2)<br>created_at: TIMESTAMPTZ", "swimlane;startSize=24;fillColor=#fef3c7;strokeColor=#d97706;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=60, y=480, w=240, h=160)
    e_audio = b.add_cell("<b>VOICE_DIARIES</b><br>--<br>[PK] entry_id: UUID<br>[FK] student_id: UUID<br>encrypted_audio_url: VARCHAR<br>transcript_text: TEXT<br>sentiment_weight: NUMERIC<br>recorded_at: TIMESTAMPTZ", "swimlane;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=350, y=480, w=240, h=160)
    e_plan = b.add_cell("<b>STUDY_PLANS</b><br>--<br>[PK] plan_id: UUID<br>[FK] student_id: UUID<br>focus_duration: INT<br>break_duration: INT<br>is_stress_adapted: BOOLEAN<br>plan_date: DATE", "swimlane;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=200, y=720, w=240, h=150)
    e_apt = b.add_cell("<b>APPOINTMENTS</b><br>--<br>[PK] booking_id: UUID<br>[FK] student_id: UUID<br>[FK] counselor_id: UUID<br>scheduled_slot: TIMESTAMPTZ<br>status: VARCHAR(20)<br>clinical_notes: TEXT", "swimlane;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=760, y=480, w=250, h=160)
    e_pay = b.add_cell("<b>PAYMENTS</b><br>--<br>[PK] payment_id: UUID<br>[FK] booking_id: UUID<br>polar_order_id: VARCHAR(100)<br>amount_paid: NUMERIC(8,2)<br>payment_status: VARCHAR(20)<br>verified_at: TIMESTAMPTZ", "swimlane;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=760, y=720, w=250, h=150)
    e_post = b.add_cell("<b>COMMUNITY_POSTS</b><br>--<br>[PK] post_id: UUID<br>[FK] student_id: UUID<br>is_anonymous: BOOLEAN<br>content: TEXT<br>report_count: INT<br>is_hidden: BOOLEAN", "swimlane;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10.5;", x=1100, y=480, w=240, h=160)

    # Relationships
    b.add_cell("1 : 1", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_user, target=e_student)
    b.add_cell("1 : 1", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_user, target=e_counselor)
    b.add_cell("1 : N", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_student, target=e_stress)
    b.add_cell("1 : N", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_student, target=e_audio)
    b.add_cell("1 : N", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_student, target=e_plan)
    b.add_cell("1 : N", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_student, target=e_apt)
    b.add_cell("1 : N", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_counselor, target=e_apt)
    b.add_cell("1 : 1", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_apt, target=e_pay)
    b.add_cell("1 : N", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=e_student, target=e_post)

    save_drawio_file("09_Entity_Relationship_Diagram", b)
    return b

def make_database_schema():
    # Uses tabular relational table representation matching Supabase PostgreSQL
    w, h = 1500, 1000
    b = DrawioBuilder("10_Database_Schema", w, h)
    b.add_cell("Figure 5.5.2: Relational Database Physical Schema for MindEase Platform", "shape=umlFrame;whiteSpace=wrap;html=1;width=480;height=35;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=13;fontStyle=1;", x=30, y=20, w=1440, h=950)

    t_users = b.add_cell("<b>public.users</b><br>--<br>PK user_id: UUID (gen_random_uuid())<br>email: VARCHAR(255) UNIQUE NOT NULL<br>password_hash: VARCHAR(255) NOT NULL<br>role: VARCHAR(20) DEFAULT 'student'<br>is_verified: BOOLEAN DEFAULT FALSE<br>created_at: TIMESTAMPTZ DEFAULT now()", "swimlane;fontStyle=0;startSize=24;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", x=600, y=70, w=260, h=140)
    t_students = b.add_cell("<b>public.students</b><br>--<br>PK,FK student_id: UUID REFERENCES users(user_id)<br>reg_number: VARCHAR(50) UNIQUE<br>department: VARCHAR(100)<br>semester: INTEGER<br>baseline_score: NUMERIC(4,2) DEFAULT 14.0", "swimlane;fontStyle=0;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", x=250, y=270, w=270, h=135)
    t_counselors = b.add_cell("<b>public.counselors</b><br>--<br>PK,FK counselor_id: UUID REFERENCES users(user_id)<br>license_no: VARCHAR(50) UNIQUE<br>specialization: VARCHAR(100)<br>hourly_rate: NUMERIC(8,2) DEFAULT 0.0<br>is_approved: BOOLEAN DEFAULT FALSE", "swimlane;fontStyle=0;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", x=920, y=270, w=270, h=135)
    t_stress = b.add_cell("<b>public.stress_logs</b><br>--<br>PK log_id: UUID<br>FK student_id: UUID REFERENCES students(student_id)<br>pss_score: INT CHECK (pss_score BETWEEN 0 AND 40)<br>speech_score: NUMERIC(4,2)<br>multimodal_score: NUMERIC(4,2)<br>tier: VARCHAR(20) CHECK (tier IN ('MILD','MODERATE','SEVERE'))<br>created_at: TIMESTAMPTZ DEFAULT now()", "swimlane;fontStyle=0;startSize=24;fillColor=#fef3c7;strokeColor=#d97706;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", x=60, y=480, w=260, h=165)
    t_audio = b.add_cell("<b>public.voice_diaries</b><br>--<br>PK entry_id: UUID<br>FK student_id: UUID REFERENCES students(student_id)<br>audio_vault_path: TEXT NOT NULL<br>transcript_text: TEXT<br>detected_lang: VARCHAR(20)<br>acoustic_pitch: NUMERIC(6,2)<br>recorded_at: TIMESTAMPTZ DEFAULT now()", "swimlane;fontStyle=0;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", x=370, y=480, w=260, h=165)
    t_plan = b.add_cell("<b>public.study_plans</b><br>--<br>PK plan_id: UUID<br>FK student_id: UUID REFERENCES students(student_id)<br>focus_minutes: INT DEFAULT 25<br>break_minutes: INT DEFAULT 5<br>is_adapted: BOOLEAN DEFAULT FALSE<br>plan_date: DATE DEFAULT CURRENT_DATE", "swimlane;fontStyle=0;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", x=220, y=720, w=260, h=150)
    t_apt = b.add_cell("<b>public.appointments</b><br>--<br>PK booking_id: UUID<br>FK student_id: UUID REFERENCES students(student_id)<br>FK counselor_id: UUID REFERENCES counselors(counselor_id)<br>scheduled_slot: TIMESTAMPTZ NOT NULL<br>status: VARCHAR(20) DEFAULT 'PENDING'<br>clinical_notes: TEXT", "swimlane;fontStyle=0;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", x=780, y=480, w=270, h=165)
    t_pay = b.add_cell("<b>public.payments</b><br>--<br>PK payment_id: UUID<br>FK booking_id: UUID REFERENCES appointments(booking_id)<br>polar_order_id: VARCHAR(100) UNIQUE<br>amount_paid: NUMERIC(8,2) NOT NULL<br>payment_status: VARCHAR(20) DEFAULT 'PAID'<br>verified_at: TIMESTAMPTZ", "swimlane;fontStyle=0;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", x=780, y=720, w=270, h=150)
    t_post = b.add_cell("<b>public.community_posts</b><br>--<br>PK post_id: UUID<br>FK student_id: UUID REFERENCES students(student_id)<br>is_anonymous: BOOLEAN DEFAULT TRUE<br>content_text: TEXT NOT NULL<br>flag_count: INT DEFAULT 0<br>is_hidden: BOOLEAN DEFAULT FALSE", "swimlane;fontStyle=0;startSize=24;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", x=1130, y=480, w=260, h=165)

    # Foreign Key Connectors
    b.add_cell("FK user_id", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=t_students, target=t_users)
    b.add_cell("FK user_id", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=t_counselors, target=t_users)
    b.add_cell("FK student_id", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=t_stress, target=t_students)
    b.add_cell("FK student_id", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=t_audio, target=t_students)
    b.add_cell("FK student_id", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=t_plan, target=t_students)
    b.add_cell("FK student_id", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=t_apt, target=t_students)
    b.add_cell("FK counselor_id", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=t_apt, target=t_counselors)
    b.add_cell("FK booking_id", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=t_pay, target=t_apt)
    b.add_cell("FK student_id", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.3;", edge=True, source=t_post, target=t_students)

    save_drawio_file("10_Database_Schema", b)
    return b

# =============================================================================
# 11_State_Machine_Diagram
# =============================================================================
def make_state_machine_diagram():
    w, h = 1350, 850
    b = DrawioBuilder("11_State_Machine_Diagram", w, h)
    b.add_cell("Figure 5.4.4: UML State Machine Diagram for Student Wellness Lifecycle", "shape=umlFrame;whiteSpace=wrap;html=1;width=450;height=35;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=13;fontStyle=1;", x=30, y=20, w=1290, h=800)

    # Initial State
    s0 = b.add_cell("", "shape=ellipse;fillColor=#000000;strokeColor=#000000;", x=80, y=360, w=30, h=30)

    # States
    s_base = b.add_cell("<b>Baseline Normal</b><br>--<br>entry / Calibrate Moving Average<br>do / Routine Daily PSS-10 Check-in", "rounded=1;whiteSpace=wrap;html=1;fillColor=#eff6ff;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", x=180, y=330, w=230, h=90)
    s_mild = b.add_cell("<b>Mild Stress Tier</b><br>--<br>entry / Recommend Audio Relaxation<br>do / Track Sleep &amp; Habit Drift", "rounded=1;whiteSpace=wrap;html=1;fillColor=#f0fdf4;strokeColor=#15803d;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", x=480, y=330, w=230, h=90)
    s_mod = b.add_cell("<b>Moderate Stress Tier</b><br>--<br>entry / Trigger Adaptive Study Plan<br>do / Restructure Pomodoro 25m/15m", "rounded=1;whiteSpace=wrap;html=1;fillColor=#fef3c7;strokeColor=#d97706;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", x=780, y=330, w=240, h=90)
    s_high = b.add_cell("<b>Severe Stress / Crisis Tier</b><br>--<br>entry / Activate Crisis SOS Alert<br>do / Priority Triage Counselor Booking", "rounded=1;whiteSpace=wrap;html=1;fillColor=#fee2e2;strokeColor=#dc2626;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", x=780, y=550, w=240, h=90)
    s_counsel = b.add_cell("<b>Clinical Intervention</b><br>--<br>entry / Share Consented XAI Dossier<br>do / Conduct 1-on-1 Counseling Session", "rounded=1;whiteSpace=wrap;html=1;fillColor=#faf5ff;strokeColor=#7e22ce;strokeWidth=1.5;fontFamily=Arial;fontSize=11;", x=480, y=550, w=230, h=90)

    # End State
    s_end = b.add_cell("", "shape=ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#0f172a;strokeWidth=2;", x=1180, y=360, w=30, h=30)

    # Transitions
    b.add_cell("Student Onboarding", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;", edge=True, source=s0, target=s_base)
    b.add_cell("[PSS Score 14-26 or Acoustic Drift &gt; 15%]", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;", edge=True, source=s_base, target=s_mild)
    b.add_cell("[BiLSTM Fusion &gt; 0.65]", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#d97706;strokeWidth=1.5;", edge=True, source=s_mild, target=s_mod)
    b.add_cell("[Score &gt;= 27 or Crisis NLP Keyword]", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#dc2626;strokeWidth=1.5;", edge=True, source=s_mod, target=s_high)
    b.add_cell("Free Triage Booking Confirmed", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#7e22ce;strokeWidth=1.5;", edge=True, source=s_high, target=s_counsel)
    b.add_cell("Therapy Completed &amp; Symptoms Alleviated", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#15803d;strokeWidth=1.5;", edge=True, source=s_counsel, target=s_base)
    b.add_cell("30-Day Sustained Baseline Recovery", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#15803d;strokeWidth=1.5;", edge=True, source=s_mild, target=s_base)
    b.add_cell("Account Graduation / Exit", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#0f172a;strokeWidth=1.5;", edge=True, source=s_mod, target=s_end)

    save_drawio_file("11_State_Machine_Diagram", b)
    return b

# =============================================================================
# 5 Activity Diagrams (AD01 to AD05)
# =============================================================================
def make_activity_diagrams():
    configs = [
        ("AD01_Multimodal_Stress_Assessment_Workflow", "Activity Diagram: Multimodal Stress Assessment Workflow", [
            ("Start", "shape=ellipse;fillColor=#000000;", 50, 50),
            ("Submit Daily PSS-10 Questionnaire", "rounded=1;", 160, 60),
            ("Record 60s Voice Reflection Diary", "rounded=1;", 380, 60),
            ("Extract Acoustic Prosody & Speech Pitch", "rounded=1;", 600, 60),
            ("Run Multimodal BiLSTM Fusion Inference", "rounded=1;fillColor=#fef3c7;", 840, 60),
            ("Generate SHAP Explainability Weights", "rounded=1;", 1100, 60),
            ("Present Holistic Wellness Dashboard", "rounded=1;", 1320, 60),
            ("End", "shape=ellipse;shape=endState;", 1540, 50)
        ]),
        ("AD02_Voice_Diary_Whisper_Analysis", "Activity Diagram: Voice Diary Whisper ASR & Acoustic Extraction", [
            ("Start", "shape=ellipse;fillColor=#000000;", 50, 50),
            ("Capture Microphone Audio Stream", "rounded=1;", 160, 60),
            ("Encrypt Audio Stream with AES-256", "rounded=1;", 380, 60),
            ("Run OpenAI Whisper STT Transcription", "rounded=1;fillColor=#eff6ff;", 600, 60),
            ("Compute Lexical Sentiment & Urdu NLP Subscore", "rounded=1;", 840, 60),
            ("Extract Pitch, Jitter & Shimmer Acoustic Vectors", "rounded=1;", 1100, 60),
            ("Persist Audio Metadata to Supabase Vault", "rounded=1;", 1340, 60),
            ("End", "shape=ellipse;shape=endState;", 1560, 50)
        ]),
        ("AD03_Adaptive_Study_Planner", "Activity Diagram: Stress-Calibrated Adaptive Study Planner", [
            ("Start", "shape=ellipse;fillColor=#000000;", 50, 50),
            ("Fetch Current Daily Multimodal Stress Tier", "rounded=1;", 160, 60),
            ("Evaluate Cognitive Workload Capacity", "shape=rhombus;", 400, 80),
            ("Configure Pomodoro Interval (Focus/Break)", "rounded=1;fillColor=#eff6ff;", 640, 60),
            ("Insert Targeted Mindfulness & Breathing Breaks", "rounded=1;", 900, 60),
            ("Sync Dynamic Study Schedule to Student Device", "rounded=1;", 1160, 60),
            ("End", "shape=ellipse;shape=endState;", 1380, 50)
        ]),
        ("AD04_Counselor_Booking_Polar_Payment", "Activity Diagram: Counselor Booking & Polar Payment Flow", [
            ("Start", "shape=ellipse;fillColor=#000000;", 50, 50),
            ("Browse Certified Campus Counselor Directory", "rounded=1;", 160, 60),
            ("Select Available Date & Time Consultation Slot", "rounded=1;", 400, 60),
            ("Initiate Checkout Session via Polar Gateway", "rounded=1;fillColor=#fef3c7;", 660, 60),
            ("Verify Polar Webhook Cryptographic Signature", "shape=rhombus;", 920, 80),
            ("Lock Counselor Calendar Slot & Issue Confirmation", "rounded=1;", 1180, 60),
            ("Transmit Encrypted Dossier to Counselor Portal", "rounded=1;", 1420, 60),
            ("End", "shape=ellipse;shape=endState;", 1640, 50)
        ]),
        ("AD05_Community_Post_Moderation", "Activity Diagram: Peer Community Support & Moderation", [
            ("Start", "shape=ellipse;fillColor=#000000;", 50, 50),
            ("Draft Anonymous Peer Wellness Experience Post", "rounded=1;", 160, 60),
            ("Client-Side PII & Abuse Regex Filter Check", "shape=rhombus;", 420, 80),
            ("Publish Post to Ephemeral Student Feed", "rounded=1;fillColor=#eff6ff;", 680, 60),
            ("Evaluate Student Report Flag Threshold (>= 3)", "shape=rhombus;", 940, 80),
            ("Hide Post & Escalate to Admin Moderation Queue", "rounded=1;fillColor=#fee2e2;", 1200, 60),
            ("Admin Reviews & Enforces Permanent Sanction", "rounded=1;", 1440, 60),
            ("End", "shape=ellipse;shape=endState;", 1660, 50)
        ]),
    ]
    builders = {}
    for name, title, steps in configs:
        b = DrawioBuilder(name, 1800, 400)
        b.add_cell(title, "shape=umlFrame;whiteSpace=wrap;html=1;width=420;height=35;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=12;fontStyle=1;", x=20, y=20, w=1760, h=360)
        prev_id = None
        for i, (label, style, cur_x, cur_w) in enumerate(steps):
            cell_id = b.add_cell(label, f"{style}whiteSpace=wrap;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;fontFamily=Arial;fontSize=10;fontStyle=1;", x=cur_x, y=160, w=cur_w, h=70 if "rhombus" not in style else 80)
            if prev_id:
                b.add_cell("", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#1e3a8a;strokeWidth=1.5;", edge=True, source=prev_id, target=cell_id)
            prev_id = cell_id
        save_drawio_file(name, b)
        builders[name] = b
    return builders

# =============================================================================
# 10 Mobile Wireframe Screens (WF01 to WF10)
# =============================================================================
def make_wireframe_drawio_suite():
    wf_configs = [
        ("WF01_Landing_Onboarding_Screen", "Landing & Onboarding Screen", [
            ("MindEase Brand Emblem (Neural Lotus & Pulse)", "fillColor=#1e3a8a;fontColor=#ffffff;fontStyle=1;rounded=1;", 120, 80, 260, 65),
            ("Title: MindEase AI Stress Detection & Academic Support", "fontStyle=1;fontSize=12;rounded=1;", 90, 160, 320, 40),
            ("Language Selector: English | Urdu (Nastaliq) | Roman Urdu", "fillColor=#f8fafc;rounded=1;", 90, 220, 320, 80),
            ("Features: PSS-10 Assessment • Voice Diary • Explainable AI", "fillColor=#eff6ff;rounded=1;", 90, 320, 320, 90),
            ("Action Button: Get Started (Student / Counselor) →", "fillColor=#1e3a8a;fontColor=#ffffff;fontStyle=1;rounded=1;", 90, 430, 320, 50),
            ("Action Button: Sign In to Existing Account", "fillColor=#ffffff;strokeColor=#1e3a8a;fontColor=#1e3a8a;fontStyle=1;rounded=1;", 90, 495, 320, 50),
            ("Security Notice: 🔒 100% Confidential • End-to-End Encrypted", "fillColor=none;strokeColor=none;fontSize=9.5;", 90, 560, 320, 30)
        ]),
        ("WF02_Sign_Up_Screen", "User Registration Screen (Sign Up)", [
            ("Header: MindEase • Student & Counselor Registration", "fontStyle=1;fontSize=12;", 90, 80, 320, 40),
            ("Role Toggle Segment: [Student Profile] | [Counselor Profile]", "fillColor=#eff6ff;fontStyle=1;", 90, 130, 320, 40),
            ("Input Field: Full Name (Muhammad Rehan Khalid)", "fillColor=#ffffff;", 90, 185, 320, 45),
            ("Input Field: University Email (student@cuiwah.edu.pk)", "fillColor=#ffffff;", 90, 245, 320, 45),
            ("Input Field: Registration Number (CIIT/FA23-BCS-140/WAH)", "fillColor=#ffffff;", 90, 305, 320, 45),
            ("Input Field: Password (bcrypt hashed)", "fillColor=#ffffff;", 90, 365, 320, 45),
            ("Ethics Checkbox: I agree to Confidentiality Policy", "fillColor=#f0fdf4;fontStyle=1;", 90, 425, 320, 35),
            ("Submit Button: Register Account →", "fillColor=#1e3a8a;fontColor=#ffffff;fontStyle=1;", 90, 475, 320, 50),
            ("Footer: Already have an account? Sign In Here", "fillColor=none;strokeColor=none;fontSize=10;", 90, 540, 320, 30)
        ]),
        ("WF03_Log_In_Screen", "User Login Screen (Authentication)", [
            ("MindEase Brand Emblem (Neural Lotus & Pulse)", "fillColor=#1e3a8a;fontColor=#ffffff;fontStyle=1;rounded=1;", 120, 80, 260, 65),
            ("Title: Welcome Back (Sign In to Dashboard)", "fontStyle=1;fontSize=12;", 90, 160, 320, 40),
            ("Security Badge: MULTI-ROLE JWT AUTHENTICATION GUARD", "fillColor=#eff6ff;fontStyle=1;", 90, 210, 320, 30),
            ("Input Field: Institutional Email (student@cuiwah.edu.pk)", "fillColor=#ffffff;", 90, 255, 320, 45),
            ("Input Field: Password (••••••••••••)", "fillColor=#ffffff;", 90, 315, 320, 45),
            ("Link: Forgot Password?", "fillColor=none;strokeColor=none;align=right;", 90, 370, 320, 25),
            ("Submit Button: Sign In to Dashboard →", "fillColor=#1e3a8a;fontColor=#ffffff;fontStyle=1;", 90, 410, 320, 50),
            ("Footer: Don't have an account? Register Here", "fillColor=none;strokeColor=none;fontSize=10;", 90, 480, 320, 30)
        ]),
        ("WF04_Student_Dashboard_Screen", "Student Main Wellness Dashboard", [
            ("Top Greeting Bar: Welcome back, Rehan Khalid (Bell Alert)", "fillColor=#eff6ff;fontStyle=1;", 90, 80, 320, 45),
            ("Stress Card: 68% Estimated Stress Level (MODERATE - BiLSTM)", "fillColor=#fef3c7;fontStyle=1;", 90, 140, 320, 100),
            ("Quick Check-in: PSS-10 Assessment (10 Standard Items)", "fillColor=#ffffff;", 90, 255, 150, 75),
            ("Quick Check-in: Voice Diary (Whisper ASR Speech Model)", "fillColor=#ffffff;", 260, 255, 150, 75),
            ("Adaptive Study Plan: Pomodoro 25m Focus | 15m Recovery", "fillColor=#eff6ff;fontStyle=1;", 90, 345, 320, 95),
            ("Bottom Navigation: Home | Check-in | Planner | Counselor | Community", "fillColor=#ffffff;fontStyle=1;", 90, 460, 320, 45)
        ]),
        ("WF05_Multilingual_Questionnaire_Screen", "Multilingual Stress Questionnaire Screen", [
            ("Progress Header: PSS-10 Stress Assessment (Question 3 of 10)", "fontStyle=1;", 90, 80, 320, 35),
            ("Question Prompt (English): In the last month, how often have you felt nervous and stressed?", "fillColor=#f8fafc;fontStyle=1;", 90, 125, 320, 60),
            ("Subtitle (Roman Urdu): Pichle maheene aap ne kitni baar be-cheeni mehsoos ki?", "fillColor=#eff6ff;fontStyle=2;", 90, 195, 320, 40),
            ("Option 1: Never (Kabhi nahi)", "fillColor=#ffffff;", 90, 245, 320, 32),
            ("Option 2: Sometimes (Kabhi kabhar)", "fillColor=#ffffff;", 90, 285, 320, 32),
            ("Option 3: Fairly Often (Aksar auqat) [✓ Selected]", "fillColor=#eff6ff;fontStyle=1;strokeColor=#2563eb;", 90, 325, 320, 32),
            ("Option 4: Very Often (Bohat zyada)", "fillColor=#ffffff;", 90, 365, 320, 32),
            ("Personal Reflection Note & NLP Sub-Score (+2.1 Moderate)", "fillColor=#ecfdf5;fontStyle=1;", 90, 410, 320, 60),
            ("Navigation Button: Next Question (4 of 10) →", "fillColor=#1e3a8a;fontColor=#ffffff;fontStyle=1;", 90, 485, 320, 45)
        ]),
        ("WF06_Voice_Diary_Screen", "Voice Diary & Whisper Transcription Screen", [
            ("Header: Daily Voice Diary Check-in (Urdu / English)", "fontStyle=1;", 90, 80, 320, 35),
            ("Audio Waveform Visualizer: RECORDING LIVE • 01:24 / 03:00", "fillColor=#0f172a;fontColor=#38bdf8;fontStyle=1;", 90, 125, 320, 110),
            ("Live Whisper ASR: 'Aaj assignment ka kafi load tha, 4 ghante so saka'", "fillColor=#f8fafc;fontStyle=1;", 90, 245, 320, 85),
            ("Confidence Badge: Roman Urdu (Whisper-v3 Confidence 96%)", "fillColor=#ecfdf5;fontStyle=1;", 90, 340, 320, 30),
            ("Privacy Shield: 🔒 End-to-End AES-256 Vault Encryption", "fillColor=#f0f9ff;fontStyle=1;", 90, 380, 320, 45),
            ("Submit Button: Stop & Save Diary Entry →", "fillColor=#1e3a8a;fontColor=#ffffff;fontStyle=1;", 90, 440, 320, 48)
        ]),
        ("WF07_XAI_Insights_Screen", "Explainable AI (XAI) Attribution Screen", [
            ("Header: Explainable AI (XAI) Attribution Insights", "fontStyle=1;", 90, 80, 320, 35),
            ("Summary: Predicted Stress: MODERATE (68/100) • Trigger: Acute sleep deficit", "fillColor=#eff6ff;fontStyle=1;", 90, 125, 320, 75),
            ("SHAP Feature Attribution: Sleep Deficit (+0.42)", "fillColor=#fee2e2;strokeColor=#dc2626;", 90, 215, 320, 30),
            ("SHAP Feature Attribution: High Screen Time (+0.28)", "fillColor=#ffedd5;strokeColor=#ea580c;", 90, 255, 320, 30),
            ("SHAP Feature Attribution: PSS-10 Score (+0.18)", "fillColor=#fef3c7;strokeColor=#d97706;", 90, 295, 320, 30),
            ("SHAP Feature Attribution: Physical Activity (-0.14 Healing)", "fillColor=#ecfdf5;strokeColor=#10b981;", 90, 335, 320, 30),
            ("Clinical Action: Listen to Theta Wave Deep Relaxation Audio Guide", "fillColor=#f8fafc;fontStyle=1;", 90, 380, 320, 70),
            ("Action Button: Start Relaxation Session Now →", "fillColor=#1e3a8a;fontColor=#ffffff;fontStyle=1;", 90, 465, 320, 45)
        ]),
        ("WF08_Adaptive_Study_Planner_Screen", "Adaptive Study & Recovery Planner Screen", [
            ("Header: Adaptive Study Planner (Pomodoro Intervals)", "fontStyle=1;", 90, 80, 320, 35),
            ("Status Badge: ⚡ Stress Mode Active: Lighter 25m Focus + 15m Break", "fillColor=#fef3c7;fontStyle=1;", 90, 125, 320, 40),
            ("Session 1: 10:00 AM - 10:25 AM (Focus: UML Sequence Diagrams)", "fillColor=#ffffff;", 90, 175, 320, 50),
            ("Recovery Break: 10:25 AM - 10:40 AM (4-7-8 Breathing & Hydration)", "fillColor=#eff6ff;fontStyle=1;", 90, 235, 320, 45),
            ("Session 2: 10:40 AM - 11:05 AM (Focus: FastAPI Habit Tracker)", "fillColor=#ffffff;", 90, 290, 320, 50),
            ("Task Roll-over Queue: Data Structures Assignment (Due Tomorrow)", "fillColor=#f8fafc;", 90, 350, 320, 60),
            ("Action Button: + Add New Academic Task", "fillColor=#1e3a8a;fontColor=#ffffff;fontStyle=1;", 90, 425, 320, 45)
        ]),
        ("WF09_Counselor_Booking_Screen", "Counselor Directory & Booking Screen", [
            ("Header: Counselor Directory (Confidential Campus Booking)", "fontStyle=1;", 90, 80, 320, 35),
            ("Triage Promotion: 🎉 Free Triage Eligible! (High Stress Detected)", "fillColor=#ecfdf5;fontStyle=1;", 90, 125, 320, 45),
            ("Counselor Card 1: Dr. Ayesha Tariq, Ph.D. (Slot: 2:00 PM Selected)", "fillColor=#ffffff;strokeColor=#2563eb;fontStyle=1;", 90, 180, 320, 110),
            ("Counselor Card 2: Mr. Bilal Ahmed, M.Sc. (CUI Verified)", "fillColor=#ffffff;", 90, 300, 320, 95),
            ("Action Button: Confirm Free Booking (2:00 PM) →", "fillColor=#1e3a8a;fontColor=#ffffff;fontStyle=1;", 90, 410, 320, 48),
            ("Payment Notice: Polar Payment Integration (Test Sandbox)", "fillColor=none;strokeColor=none;fontSize=9.5;", 90, 470, 320, 30)
        ]),
        ("WF10_Peer_Community_Feed_Screen", "Peer Community Support Feed Screen", [
            ("Header: Student Community Feed (Safe Peer Forum)", "fontStyle=1;", 90, 80, 320, 35),
            ("Post 1: Anonymous Student #402: 'Overwhelmed by FYP deadlines...'", "fillColor=#ffffff;", 90, 125, 320, 85),
            ("Verified Reply: Dr. Ayesha Tariq: 'Break tasks into 25m Pomodoro!'", "fillColor=#eff6ff;fontStyle=1;", 110, 220, 280, 45),
            ("Post Actions: ❤️ 24 Likes   💬 8 Replies   🚩 Report Post", "fillColor=none;strokeColor=none;fontSize=9.5;", 90, 275, 320, 25),
            ("Post 2: CS Senior Wah: '10-minute guided breathing helped my lab viva!'", "fillColor=#ffffff;", 90, 310, 320, 80),
            ("Action Button: + Share Anonymous Experience", "fillColor=#1e3a8a;fontColor=#ffffff;fontStyle=1;", 90, 410, 320, 48)
        ])
    ]
    builders = {}
    for name, title, items in wf_configs:
        b = DrawioBuilder(name, 500, 750)
        # Phone Frame
        b.add_cell(f"Figure: {title}", "shape=umlFrame;whiteSpace=wrap;html=1;width=250;height=30;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=1.5;fontFamily=Arial;fontSize=11;fontStyle=1;", x=20, y=20, w=460, h=710)
        b.add_cell("", "rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0f172a;strokeWidth=2.5;", x=50, y=55, w=400, h=650)
        # Notch
        b.add_cell("", "rounded=1;arcSize=30;fillColor=#0f172a;", x=180, y=65, w=140, h=16)
        # Items
        for label, style, ix, iy, iw, ih in items:
            b.add_cell(label, f"whiteSpace=wrap;html=1;strokeColor=#cbd5e1;strokeWidth=1.2;fontFamily=Arial;fontSize=10;{style}", x=ix-30, y=iy+30, w=iw+60, h=ih)
        save_drawio_file(name, b)
        builders[name] = b
    return builders

# =============================================================================
# Master Multi-Tab Draw.io Workbook
# =============================================================================
def build_master_drawio_file(all_diagrams):
    root = ET.Element("mxfile", host="app.diagrams.net", version="21.0.0", type="device")
    for name, b in all_diagrams.items():
        diagram = ET.SubElement(root, "diagram", id=f"tab_{name}", name=name)
        model = ET.SubElement(diagram, "mxGraphModel", dx=str(b.width), dy=str(b.height), grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth=str(b.width), pageHeight=str(b.height), background="#ffffff", math="0", shadow="0")
        root_cell = ET.SubElement(model, "root")
        ET.SubElement(root_cell, "mxCell", id="0")
        ET.SubElement(root_cell, "mxCell", id="1", parent="0")

        for c in b.cells:
            cell_elem = ET.SubElement(root_cell, "mxCell", id=c["id"], parent=c["parent"])
            if c["value"]:
                cell_elem.set("value", c["value"])
            if c["style"]:
                cell_elem.set("style", c["style"])
            if c.get("vertex"):
                cell_elem.set("vertex", c["vertex"])
            if c.get("edge"):
                cell_elem.set("edge", c["edge"])
            if c.get("source"):
                cell_elem.set("source", c["source"])
            if c.get("target"):
                cell_elem.set("target", c["target"])

            geom = ET.SubElement(cell_elem, "mxGeometry")
            if c.get("edge"):
                geom.set("relative", "1")
                geom.set("as", "geometry")
                if c.get("points"):
                    arr = ET.SubElement(geom, "Array", **{"as": "points"})
                    for px, py in c["points"]:
                        ET.SubElement(arr, "mxPoint", x=str(px), y=str(py))
            else:
                geom.set("x", str(c["x"]))
                geom.set("y", str(c["y"]))
                geom.set("width", str(c["w"]))
                geom.set("height", str(c["h"]))
                geom.set("as", "geometry")

    # Append the 17 Sequence Diagrams to the Master Workbook
    seq_count = 0
    for i in range(1, 18):
        uid = f"UC{i:02d}"
        seq_path = os.path.join(EDITABLE_DIR, f"{uid}_Sequence_Diagram.drawio")
        if os.path.exists(seq_path):
            try:
                tree = ET.parse(seq_path)
                diag = tree.getroot().find("diagram")
                if diag is not None:
                    root.append(diag)
                    seq_count += 1
            except Exception as e:
                print(f"Warning loading sequence diagram {uid}: {e}")

    master_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True).decode("utf-8")
    master_p1 = os.path.join(EDITABLE_DIR, "MindEase_Master_System_Diagrams.drawio")
    master_p2 = os.path.join(VISIO_DIR, "MindEase_Master_System_Diagrams.drawio")
    with open(master_p1, "w", encoding="utf-8") as f:
        f.write(master_xml)
    with open(master_p2, "w", encoding="utf-8") as f:
        f.write(master_xml)
    total_tabs = len(all_diagrams) + seq_count
    print(f"\nCreated MASTER Draw.io Workbook: {master_p1} ({total_tabs} Interactive Tabs!)")

def main():
    print("=================================================================")
    print("Building 100% Native Editable Draw.io Diagram Suite for MindEase")
    print("=================================================================\n")
    all_diagrams = {}

    all_diagrams["01_System_Architecture"] = make_system_architecture()
    all_diagrams["02_Use_Case_Diagram"] = make_use_case_diagram()
    all_diagrams["03_DFD_Level_0"] = make_dfd_level_0()
    all_diagrams["04_DFD_Level_1"] = make_dfd_level_1()
    all_diagrams["05_DFD_Level_2_Stress_Detection"] = make_dfd_level_2()
    all_diagrams["06_Component_Diagram"] = make_component_diagram()
    all_diagrams["07_Deployment_Diagram"] = make_deployment_diagram()
    all_diagrams["08_Class_Diagram"] = make_class_diagram()
    all_diagrams["09_Entity_Relationship_Diagram"] = make_erd_diagram()
    all_diagrams["10_Database_Schema"] = make_database_schema()
    all_diagrams["11_State_Machine_Diagram"] = make_state_machine_diagram()

    ad_builders = make_activity_diagrams()
    all_diagrams.update(ad_builders)

    wf_builders = make_wireframe_drawio_suite()
    all_diagrams.update(wf_builders)

    build_master_drawio_file(all_diagrams)
    print("\nSuccessfully built all editable Draw.io files for MindEase FYP!")

if __name__ == "__main__":
    main()
