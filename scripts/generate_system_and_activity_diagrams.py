"""
Generates all System Architecture, Structural, Behavioral, and Activity Diagrams for MindEase FYP SRDS
Includes:
- 01_System_Architecture
- 02_Use_Case_Diagram
- 03_DFD_Level_0
- 04_DFD_Level_1
- 05_DFD_Level_2_Stress_Detection
- 06_Component_Diagram
- 07_Deployment_Diagram
- 08_Class_Diagram
- 09_Entity_Relationship_Diagram
- 10_Database_Schema
- 11_State_Machine_Diagram
- AD01_Multimodal_Stress_Assessment_Workflow
- AD02_Voice_Diary_Whisper_Analysis
- AD03_Adaptive_Study_Planner
- AD04_Counselor_Booking_Polar_Payment
- AD05_Community_Post_Moderation
"""
import os
import xml.etree.ElementTree as ET
from drawio_builder import DrawioBuilder

def write_files(name, svg_content, drawio_content):
    svg_dir = os.path.join("Documentation", "Diagrams", "SVG")
    editable_dir = os.path.join("Documentation", "Diagrams", "Editable")
    visio_dir = os.path.join("Documentation", "Diagrams", "Visio")
    os.makedirs(svg_dir, exist_ok=True)
    os.makedirs(editable_dir, exist_ok=True)
    os.makedirs(visio_dir, exist_ok=True)

    svg_path = os.path.join(svg_dir, f"{name}.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    drawio_path = os.path.join(editable_dir, f"{name}.drawio")
    with open(drawio_path, "w", encoding="utf-8") as f:
        f.write(drawio_content)

    visio_path = os.path.join(visio_dir, f"{name}.drawio")
    with open(visio_path, "w", encoding="utf-8") as f:
        f.write(drawio_content)

    print(f"Generated: {name} (.svg, .drawio)")

# -------------------------------------------------------------
# 01_System_Architecture
# -------------------------------------------------------------
def build_system_architecture():
    w, h = 1150, 850
    b = DrawioBuilder("01_System_Architecture", w, h)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>
  </marker>
</defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<!-- Outer Frame -->
<rect x="30" y="30" width="{w-60}" height="{h-80}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<rect x="30" y="30" width="300" height="35" fill="#1e3a8a" stroke="#1e293b" stroke-width="1.5"/>
<text x="45" y="53" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff">MindEase: High-Level System Architecture</text>

<!-- TIER 1: Presentation Tier (Mobile Client) -->
<rect x="60" y="90" width="1030" height="130" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" rx="6"/>
<rect x="60" y="90" width="260" height="26" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5" rx="4"/>
<text x="75" y="108" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#1e40af">Presentation Layer (Flutter Mobile App)</text>

<!-- Mobile Components -->
<rect x="80" y="130" width="180" height="70" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="170" y="155" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Student Mobile App</text>
<text x="170" y="175" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Assessment, Diary, Habits</text>
<text x="170" y="190" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">XAI Insights, Study Planner</text>

<rect x="290" y="130" width="180" height="70" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="380" y="155" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor Portal</text>
<text x="380" y="175" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Appointment Schedule</text>
<text x="380" y="190" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Patient Trends, Clinical Notes</text>

<rect x="500" y="130" width="180" height="70" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="590" y="155" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Admin Management</text>
<text x="590" y="175" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Counselor Approvals, Content</text>
<text x="590" y="190" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Community Post Moderation</text>

<rect x="710" y="130" width="170" height="70" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="795" y="155" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">State Management</text>
<text x="795" y="175" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Flutter BLoC / Cubit</text>
<text x="795" y="190" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Event / State Streams</text>

<rect x="905" y="130" width="165" height="70" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="987" y="155" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Network &amp; Storage</text>
<text x="987" y="175" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Dio HTTP / WebSockets</text>
<text x="987" y="190" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Flutter Secure Storage</text>

<!-- Connection Arrow 1 -->
<line x1="575" y1="220" x2="575" y2="260" stroke="#0f172a" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="585" y="245" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">REST APIs &amp; WebSockets (TLS 1.3 / HTTPS)</text>

<!-- TIER 2: Application Tier (FastAPI Backend Server) -->
<rect x="60" y="260" width="1030" height="170" fill="#f8fafc" stroke="#10b981" stroke-width="1.5" rx="6"/>
<rect x="60" y="260" width="280" height="26" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5" rx="4"/>
<text x="75" y="278" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#047857">Application Tier (FastAPI Python Backend)</text>

<!-- Micro-Modules inside Backend -->
<rect x="80" y="300" width="150" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="155" y="322" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Auth &amp; RBAC Service</text>
<text x="155" y="338" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">JWT, Multi-Role Guard</text>

<rect x="245" y="300" width="150" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="320" y="322" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Questionnaire Service</text>
<text x="320" y="338" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Multilingual Scoring</text>

<rect x="410" y="300" width="150" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="485" y="322" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Diary &amp; Safety Service</text>
<text x="485" y="338" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Crisis Detection Pipeline</text>

<rect x="575" y="300" width="150" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="650" y="322" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Habits &amp; Fusion Router</text>
<text x="650" y="338" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Sleep, Steps, Screen Time</text>

<rect x="740" y="300" width="150" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="815" y="322" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Baseline &amp; Triggers</text>
<text x="815" y="338" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Trend Analysis Engine</text>

<rect x="905" y="300" width="165" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="987" y="322" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Adaptive Study Planner</text>
<text x="987" y="338" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Pomodoro &amp; Load Tuning</text>

<!-- Second row backend services -->
<rect x="80" y="365" width="180" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="170" y="387" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Content &amp; Recovery Service</text>
<text x="170" y="403" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Recommendation Engine</text>

<rect x="275" y="365" width="180" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="365" y="387" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor Booking Service</text>
<text x="365" y="403" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Free Triage &amp; Clinical Notes</text>

<rect x="470" y="365" width="180" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="560" y="387" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Peer Community Service</text>
<text x="560" y="403" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Anonymous Posts &amp; Reports</text>

<rect x="665" y="365" width="180" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="755" y="387" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Billing Controller</text>
<text x="755" y="403" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Webhooks &amp; Transactions</text>

<rect x="860" y="365" width="210" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="965" y="387" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Admin Portal Controller</text>
<text x="965" y="403" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Approvals, Content &amp; Audit Logs</text>

<!-- Connection Arrow 2 -->
<line x1="350" y1="430" x2="350" y2="470" stroke="#0f172a" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="360" y="455" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Internal Pipeline &amp; Models</text>

<line x1="800" y1="430" x2="800" y2="470" stroke="#0f172a" stroke-width="1.5" marker-end="url(#arrow)"/>
<text x="810" y="455" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">PostgreSQL Connection Pool</text>

<!-- TIER 3: AI & Machine Learning Subsystem -->
<rect x="60" y="470" width="500" height="150" fill="#f8fafc" stroke="#8b5cf6" stroke-width="1.5" rx="6"/>
<rect x="60" y="470" width="280" height="26" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5" rx="4"/>
<text x="75" y="488" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#6d28d9">AI &amp; Machine Learning Engine</text>

<rect x="80" y="510" width="210" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="185" y="530" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Whisper ASR Model</text>
<text x="185" y="545" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Speech-to-Text (Urdu / English)</text>

<rect x="310" y="510" width="230" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="425" y="530" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Multimodal Stress Classifier</text>
<text x="425" y="545" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Scikit-learn / PyTorch (Fusion Model)</text>

<rect x="80" y="565" width="210" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="185" y="585" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">SHAP XAI Engine</text>
<text x="185" y="600" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Feature Attribution &amp; Drivers</text>

<rect x="310" y="565" width="230" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="425" y="585" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Conversational Chatbot</text>
<text x="425" y="600" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Hugging Face Transformers / RAG</text>

<!-- TIER 4: Persistence Layer (Supabase PostgreSQL) -->
<rect x="590" y="470" width="500" height="150" fill="#f8fafc" stroke="#0284c7" stroke-width="1.5" rx="6"/>
<rect x="590" y="470" width="280" height="26" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5" rx="4"/>
<text x="605" y="488" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0369a1">Persistence Tier (Supabase Cloud)</text>

<rect x="610" y="510" width="220" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="720" y="530" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">PostgreSQL Database</text>
<text x="720" y="545" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Users, Assessments, Habits, Plans</text>

<rect x="850" y="510" width="220" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="960" y="530" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Supabase Auth (GoTrue)</text>
<text x="960" y="545" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Row Level Security (RLS) Isolation</text>

<rect x="610" y="565" width="220" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="720" y="585" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Encrypted Diary Store</text>
<text x="720" y="600" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">AES-256 Student Private Diaries</text>

<rect x="850" y="565" width="220" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="960" y="585" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Supabase Storage</text>
<text x="960" y="600" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Audio Files, Relaxation Media</text>

<!-- TIER 5: External Services (Polar Gateway) -->
<rect x="60" y="640" width="1030" height="90" fill="#f8fafc" stroke="#f59e0b" stroke-width="1.5" rx="6"/>
<rect x="60" y="640" width="240" height="26" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5" rx="4"/>
<text x="75" y="658" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#b45309">External Gateway Tier</text>

<rect x="80" y="675" width="450" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="305" y="695" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Payment Gateway (Test Mode)</text>
<text x="305" y="710" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Sandbox Checkout, Card Tokenization, Webhook Signature Verification</text>

<rect x="560" y="675" width="510" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="815" y="695" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Crisis Helplines &amp; Emergency Telephony</text>
<text x="815" y="710" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Pakistan Mental Health Helplines, University Counseling Center Hotline</text>

<!-- Caption -->
<text x="{w/2}" y="{h-20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.1.1: MindEase High-Level Multi-Tier System Architecture</text>
</svg>'''

    b.add_cell("Presentation Layer", "swimlane;fontStyle=1;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#eff6ff;strokeColor=#3b82f6;", x=60, y=90, w=1030, h=130)
    b.add_cell("Application Tier", "swimlane;fontStyle=1;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#ecfdf5;strokeColor=#10b981;", x=60, y=260, w=1030, h=170)
    b.add_cell("AI Subsystem", "swimlane;fontStyle=1;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#f5f3ff;strokeColor=#8b5cf6;", x=60, y=470, w=500, h=150)
    b.add_cell("Persistence Tier", "swimlane;fontStyle=1;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#f0f9ff;strokeColor=#0284c7;", x=590, y=470, w=500, h=150)
    b.add_cell("External Gateways", "swimlane;fontStyle=1;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#fffbeb;strokeColor=#f59e0b;", x=60, y=640, w=1030, h=90)
    
    write_files("01_System_Architecture", svg, b.to_xml())

# -------------------------------------------------------------
# 02_Use_Case_Diagram
# -------------------------------------------------------------
def build_use_case_diagram():
    w, h = 1200, 1100
    b = DrawioBuilder("02_Use_Case_Diagram", w, h)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>
  </marker>
  <marker id="dashed-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#475569"/>
  </marker>
</defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>

<!-- System Boundary -->
<rect x="230" y="40" width="720" height="{h-100}" fill="#fafbfc" stroke="#0f172a" stroke-width="2" rx="4"/>
<text x="590" y="70" font-family="Arial, sans-serif" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">System Boundary: MindEase Stress Detection &amp; Support System</text>

<!-- ACTOR 1: Student (Left Top) -->
<circle cx="100" cy="220" r="16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<line x1="100" y1="236" x2="100" y2="280" stroke="#0f172a" stroke-width="2"/>
<line x1="75" y1="250" x2="125" y2="250" stroke="#0f172a" stroke-width="2"/>
<line x1="100" y1="280" x2="80" y2="315" stroke="#0f172a" stroke-width="2"/>
<line x1="100" y1="280" x2="120" y2="315" stroke="#0f172a" stroke-width="2"/>
<text x="100" y="335" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Student</text>
<text x="100" y="350" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Primary Actor)</text>

<!-- ACTOR 2: Counselor (Right Top) -->
<circle cx="1070" cy="220" r="16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<line x1="1070" y1="236" x2="1070" y2="280" stroke="#0f172a" stroke-width="2"/>
<line x1="1045" y1="250" x2="1095" y2="250" stroke="#0f172a" stroke-width="2"/>
<line x1="1070" y1="280" x2="1050" y2="315" stroke="#0f172a" stroke-width="2"/>
<line x1="1070" y1="280" x2="1090" y2="315" stroke="#0f172a" stroke-width="2"/>
<text x="1070" y="335" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor</text>
<text x="1070" y="350" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Mental Health Pro)</text>

<!-- ACTOR 3: Administrator (Right Bottom) -->
<circle cx="1070" cy="750" r="16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<line x1="1070" y1="766" x2="1070" y2="810" stroke="#0f172a" stroke-width="2"/>
<line x1="1045" y1="780" x2="1095" y2="780" stroke="#0f172a" stroke-width="2"/>
<line x1="1070" y1="810" x2="1050" y2="845" stroke="#0f172a" stroke-width="2"/>
<line x1="1070" y1="810" x2="1090" y2="845" stroke="#0f172a" stroke-width="2"/>
<text x="1070" y="865" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Administrator</text>
<text x="1070" y="880" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(System Admin)</text>

<!-- SECONDARY ACTOR: External AI & Services (Left Bottom) -->
<circle cx="100" cy="750" r="16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<line x1="100" y1="766" x2="100" y2="810" stroke="#0f172a" stroke-width="2"/>
<line x1="75" y1="780" x2="125" y2="780" stroke="#0f172a" stroke-width="2"/>
<line x1="100" y1="810" x2="80" y2="845" stroke="#0f172a" stroke-width="2"/>
<line x1="100" y1="810" x2="120" y2="845" stroke="#0f172a" stroke-width="2"/>
<text x="100" y="865" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">&lt;&lt;System&gt;&gt;</text>
<text x="100" y="880" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">AI &amp; Payment Services</text>

<!-- USE CASES (17 Ovals) -->
'''
    # We will lay out the 17 use cases in 2 columns inside the boundary
    # Col 1: x = 380, Col 2: x = 760
    ucs = [
        ("UC01", "Register & Create Profile", 380, 110),
        ("UC02", "Login & Multi-Role Authentication", 760, 110),
        ("UC03", "Complete Multilingual Stress Questionnaire", 380, 180),
        ("UC04", "Record Daily Voice and Text Diary", 380, 250),
        ("UC05", "Log Daily Habits & Calculate Stress Level", 380, 320),
        ("UC06", "View Stress Trends & Baseline Trigger Analysis", 380, 390),
        ("UC07", "View Explainable AI Stress Insights", 380, 460),
        ("UC08", "Access Relaxation Content & Rate Activity", 380, 530),
        ("UC09", "Chat with AI Conversational Assistant", 380, 600),
        ("UC10", "Generate & Manage Adaptive Study Plan", 380, 670),
        ("UC11", "Search Counselors & Request Appointment", 760, 250),
        ("UC12", "Conduct Counseling Session & Maintain Notes", 760, 330),
        ("UC13", "Process Appointment Payment via Polar", 760, 420),
        ("UC14", "Create & Interact with Peer Community Posts", 760, 510),
        ("UC15", "Report Inappropriate Community Post", 760, 600),
        ("UC16", "Manage System Users & Counselor Approvals", 760, 750),
        ("UC17", "Moderate Community Reports & System Content", 760, 840),
    ]

    for uid, name, cx, cy in ucs:
        w_box, h_box = 280, 45
        svg += f'''
<ellipse cx="{cx}" cy="{cy}" rx="{w_box/2}" ry="{h_box/2}" fill="#ffffff" stroke="#1e293b" stroke-width="1.5"/>
<text x="{cx}" y="{cy-3}" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">{uid}:</text>
<text x="{cx}" y="{cy+12}" font-family="Arial, sans-serif" font-size="10" fill="#0f172a" text-anchor="middle">{name}</text>
'''
        b.add_cell(f"{uid}: {name}", "ellipse;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1e293b;strokeWidth=1.5;fontFamily=Arial;fontSize=10;", x=cx-140, y=cy-22, w=280, h=45)

    # Actor association lines
    # Student to UC01, UC02, UC03, UC04, UC05, UC06, UC07, UC08, UC09, UC10, UC11, UC13, UC14, UC15
    student_lines = [
        (120, 230, 240, 110),
        (120, 240, 240, 180),
        (120, 250, 240, 250),
        (120, 260, 240, 320),
        (120, 270, 240, 390),
        (120, 280, 240, 460),
        (120, 290, 240, 530),
        (120, 300, 240, 600),
        (120, 310, 240, 670),
        (120, 320, 620, 250),
        (120, 330, 620, 420),
        (120, 340, 620, 510),
        (120, 350, 620, 600),
    ]
    for x1, y1, x2, y2 in student_lines:
        svg += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#64748b" stroke-width="1.1"/>\n'

    # Counselor to UC01, UC02, UC12, UC14
    counselor_lines = [
        (1050, 240, 900, 110),
        (1050, 260, 900, 330),
        (1050, 280, 900, 510),
    ]
    for x1, y1, x2, y2 in counselor_lines:
        svg += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#64748b" stroke-width="1.1"/>\n'

    # Admin to UC02, UC16, UC17
    admin_lines = [
        (1050, 770, 900, 750),
        (1050, 800, 900, 840),
    ]
    for x1, y1, x2, y2 in admin_lines:
        svg += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#64748b" stroke-width="1.1"/>\n'

    # Include / Extend relationships
    # UC05 includes UC07 (Explainable AI)
    svg += f'''
<path d="M 380 342 L 380 438" stroke="#475569" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>
<text x="390" y="390" font-family="Arial, sans-serif" font-size="9" fill="#1e293b">&lt;&lt;include&gt;&gt;</text>

<!-- UC11 extends to UC13 (Payment) -->
<path d="M 760 272 L 760 398" stroke="#475569" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>
<text x="770" y="340" font-family="Arial, sans-serif" font-size="9" fill="#1e293b">&lt;&lt;extend&gt;&gt;</text>

<!-- UC14 extends to UC15 (Report) -->
<path d="M 760 532 L 760 578" stroke="#475569" stroke-width="1.2" stroke-dasharray="4,4" marker-end="url(#dashed-arrow)"/>
<text x="770" y="555" font-family="Arial, sans-serif" font-size="9" fill="#1e293b">&lt;&lt;extend&gt;&gt;</text>
'''

    svg += f'''
<!-- Caption -->
<text x="{w/2}" y="{h-25}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 3.2.1: MindEase Complete System Use Case Diagram</text>
</svg>'''

    write_files("02_Use_Case_Diagram", svg, b.to_xml())

# -------------------------------------------------------------
# 03_DFD_Level_0 (Context Diagram)
# -------------------------------------------------------------
def build_dfd_level_0():
    w, h = 1000, 700
    b = DrawioBuilder("03_DFD_Level_0", w, h)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>
  </marker>
</defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="30" y="30" width="{w-60}" height="{h-70}" fill="none" stroke="#1e293b" stroke-width="1.5"/>

<!-- Center Process 0.0 -->
<circle cx="500" cy="350" r="115" fill="#f8fafc" stroke="#1e3a8a" stroke-width="2.5"/>
<line x1="400" y1="310" x2="600" y2="310" stroke="#1e3a8a" stroke-width="1.5"/>
<text x="500" y="295" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a" text-anchor="middle">0.0</text>
<text x="500" y="340" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">MindEase Stress Detection,</text>
<text x="500" y="360" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Recovery &amp; Support</text>
<text x="500" y="380" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">System</text>

<!-- EXTERNAL ENTITIES -->
<!-- Student (Top-Left) -->
<rect x="70" y="100" width="160" height="70" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<text x="150" y="130" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Student</text>
<text x="150" y="150" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Primary User)</text>

<!-- Counselor (Top-Right) -->
<rect x="770" y="100" width="160" height="70" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<text x="850" y="130" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor</text>
<text x="850" y="150" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(Mental Health Pro)</text>

<!-- Administrator (Bottom-Right) -->
<rect x="770" y="520" width="160" height="70" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<text x="850" y="550" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Administrator</text>
<text x="850" y="570" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(System Admin)</text>

<!-- Polar Payment Gateway (Bottom-Left) -->
<rect x="70" y="520" width="160" height="70" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<text x="150" y="550" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Gateway</text>
<text x="150" y="570" font-family="Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">(External Payment)</text>

<!-- FLOWS: Student <-> System -->
<path d="M 230 120 L 415 280" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="280" y="185" font-family="Arial, sans-serif" font-size="10" fill="#0f172a" transform="rotate(38 280 185)">Questionnaires, Diary, Habits, Tasks</text>

<path d="M 400 320 L 225 155" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="340" y="240" font-family="Arial, sans-serif" font-size="10" fill="#0f172a" transform="rotate(38 340 240)">Stress Level, XAI Insights, Study Plans</text>

<!-- FLOWS: Counselor <-> System -->
<path d="M 770 130 L 590 280" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="640" y="190" font-family="Arial, sans-serif" font-size="10" fill="#0f172a" transform="rotate(-38 640 190)">Availability, Clinical Notes</text>

<path d="M 575 320 L 780 160" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="700" y="245" font-family="Arial, sans-serif" font-size="10" fill="#0f172a" transform="rotate(-38 700 245)">Bookings, Consented Student Trends</text>

<!-- FLOWS: Admin <-> System -->
<path d="M 770 540 L 590 410" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="700" y="465" font-family="Arial, sans-serif" font-size="10" fill="#0f172a" transform="rotate(35 700 465)">Moderation Actions, Content Updates</text>

<path d="M 605 385 L 775 520" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="660" y="520" font-family="Arial, sans-serif" font-size="10" fill="#0f172a" transform="rotate(35 660 520)">Reports Queue, System Logs</text>

<!-- FLOWS: Polar <-> System -->
<path d="M 230 535 L 415 410" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="290" y="465" font-family="Arial, sans-serif" font-size="10" fill="#0f172a" transform="rotate(-35 290 465)">Webhook Payment Success</text>

<path d="M 400 380 L 225 515" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="330" y="515" font-family="Arial, sans-serif" font-size="10" fill="#0f172a" transform="rotate(-35 330 515)">Checkout Token Request</text>

<!-- Caption -->
<text x="{w/2}" y="{h-20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.3.1: DFD Level 0 (Context Diagram) for MindEase System</text>
</svg>'''

    b.add_cell("0.0 MindEase Stress System", "ellipse;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#1e3a8a;strokeWidth=2;", x=400, y=250, w=200, h=200)
    b.add_cell("Student", "whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;", x=70, y=100, w=160, h=70)
    b.add_cell("Counselor", "whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;", x=770, y=100, w=160, h=70)
    b.add_cell("Administrator", "whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;", x=770, y=520, w=160, h=70)
    b.add_cell("Polar Gateway", "whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;", x=70, y=520, w=160, h=70)

    write_files("03_DFD_Level_0", svg, b.to_xml())

# -------------------------------------------------------------
# 04_DFD_Level_1
# -------------------------------------------------------------
def build_dfd_level_1():
    w, h = 1100, 850
    b = DrawioBuilder("04_DFD_Level_1", w, h)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>
  </marker>
</defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="20" y="20" width="{w-40}" height="{h-50}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="40" y="45" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">DFD Level 1: Subsystem Functional Decomposition</text>

<!-- External Entities Left -->
<rect x="40" y="100" width="130" height="60" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<text x="105" y="135" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Student</text>

<rect x="40" y="650" width="130" height="60" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<text x="105" y="685" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Gateway</text>

<!-- External Entities Right -->
<rect x="930" y="100" width="130" height="60" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<text x="995" y="135" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor</text>

<rect x="930" y="650" width="130" height="60" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<text x="995" y="685" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Administrator</text>

<!-- PROCESS CIRCLES (Grouped) -->
<!-- 1.0 Auth -->
<circle cx="300" cy="120" r="45" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="255" y1="105" x2="345" y2="105" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="300" y="98" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">1.0</text>
<text x="300" y="125" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Manage Auth</text>
<text x="300" y="140" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">&amp; Profiles</text>

<!-- 2.0 Assessment & Scoring -->
<circle cx="530" cy="120" r="45" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="485" y1="105" x2="575" y2="105" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="530" y="98" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">2.0</text>
<text x="530" y="125" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Questionnaire</text>
<text x="530" y="140" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">&amp; Scoring</text>

<!-- 3.0 Voice & Text Diary -->
<circle cx="750" cy="120" r="45" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="705" y1="105" x2="795" y2="105" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="750" y="98" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">3.0</text>
<text x="750" y="125" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Voice Diary &amp;</text>
<text x="750" y="140" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Sentiment</text>

<!-- 4.0 Habits & Fusion -->
<circle cx="300" cy="300" r="45" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="255" y1="285" x2="345" y2="285" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="300" y="278" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">4.0</text>
<text x="300" y="305" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Habits &amp; Fusion</text>
<text x="300" y="320" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Detection</text>

<!-- 5.0 Baseline & XAI -->
<circle cx="530" cy="300" r="45" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="485" y1="285" x2="575" y2="285" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="530" y="278" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">5.0</text>
<text x="530" y="305" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Baseline &amp; XAI</text>
<text x="530" y="320" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Attribution</text>

<!-- 6.0 Adaptive Study Planner -->
<circle cx="750" cy="300" r="45" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="705" y1="285" x2="795" y2="285" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="750" y="278" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">6.0</text>
<text x="750" y="305" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Adaptive Study</text>
<text x="750" y="320" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Planner</text>

<!-- 7.0 Counselor Booking & Sessions -->
<circle cx="300" cy="500" r="45" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="255" y1="485" x2="345" y2="485" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="300" y="478" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">7.0</text>
<text x="300" y="505" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor Booking</text>
<text x="300" y="520" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">&amp; Sessions</text>

<!-- 8.0 Community & Moderation -->
<circle cx="530" cy="500" r="45" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="485" y1="485" x2="575" y2="485" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="530" y="478" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">8.0</text>
<text x="530" y="505" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Community &amp;</text>
<text x="530" y="520" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Moderation</text>

<!-- 9.0 Polar Billing & Payments -->
<circle cx="750" cy="500" r="45" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="705" y1="485" x2="795" y2="485" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="750" y="478" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">9.0</text>
<text x="750" y="505" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Billing &amp;</text>
<text x="750" y="520" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Verification</text>

<!-- DATA STORES (Parallel lines) -->
<!-- D1 Users -->
<path d="M 240 200 L 360 200 M 240 225 L 360 225" stroke="#0f172a" stroke-width="1.5"/>
<text x="300" y="217" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">D1: Users &amp; Profiles</text>

<!-- D2 Assessment Records -->
<path d="M 470 200 L 590 200 M 470 225 L 590 225" stroke="#0f172a" stroke-width="1.5"/>
<text x="530" y="217" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">D2: Stress Assessments</text>

<!-- D3 Diaries -->
<path d="M 690 200 L 810 200 M 690 225 L 810 225" stroke="#0f172a" stroke-width="1.5"/>
<text x="750" y="217" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">D3: Encrypted Diaries</text>

<!-- D4 Study Plans -->
<path d="M 240 400 L 360 400 M 240 425 L 360 425" stroke="#0f172a" stroke-width="1.5"/>
<text x="300" y="417" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">D4: Study Plans &amp; Tasks</text>

<!-- D5 Appointments & Notes -->
<path d="M 470 400 L 590 400 M 470 425 L 590 425" stroke="#0f172a" stroke-width="1.5"/>
<text x="530" y="417" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">D5: Appointments &amp; Notes</text>

<!-- D6 Community & Billing -->
<path d="M 690 400 L 810 400 M 690 425 L 810 425" stroke="#0f172a" stroke-width="1.5"/>
<text x="750" y="417" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">D6: Community &amp; Billing</text>

<!-- Interconnecting lines -->
<line x1="170" y1="120" x2="255" y2="120" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="300" y1="165" x2="300" y2="200" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="345" y1="120" x2="485" y2="120" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="575" y1="120" x2="705" y2="120" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>

<line x1="530" y1="165" x2="530" y2="200" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="750" y1="165" x2="750" y2="200" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>

<line x1="300" y1="225" x2="300" y2="255" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="530" y1="225" x2="530" y2="255" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>

<line x1="345" y1="300" x2="485" y2="300" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="575" y1="300" x2="705" y2="300" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>

<line x1="170" y1="670" x2="300" y2="545" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="750" y1="545" x2="170" y2="690" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>

<line x1="930" y1="120" x2="795" y2="120" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="930" y1="680" x2="575" y2="520" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- Caption -->
<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.3.2: DFD Level 1 Subsystem Functional Decomposition for MindEase</text>
</svg>'''

    write_files("04_DFD_Level_1", svg, b.to_xml())

# -------------------------------------------------------------
# 05_DFD_Level_2_Stress_Detection
# -------------------------------------------------------------
def build_dfd_level_2():
    w, h = 1000, 750
    b = DrawioBuilder("05_DFD_Level_2_Stress_Detection", w, h)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>
  </marker>
</defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="25" y="25" width="{w-50}" height="{h-60}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="45" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">DFD Level 2: Core Multimodal Stress Assessment &amp; Fusion Engine (Process 4.0)</text>

<!-- External Inputs -->
<rect x="50" y="100" width="140" height="45" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<text x="120" y="127" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Habit Logs (Sleep, Steps)</text>

<rect x="50" y="180" width="140" height="45" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<text x="120" y="207" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Questionnaire PSS Score</text>

<rect x="50" y="260" width="140" height="45" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<text x="120" y="287" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Diary Sentiment Score</text>

<!-- Sub-process 4.1 Feature Extraction & Normalization -->
<circle cx="320" cy="190" r="50" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="270" y1="175" x2="370" y2="175" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="320" y="168" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">4.1</text>
<text x="320" y="195" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Normalize &amp;</text>
<text x="320" y="210" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Impute Features</text>

<!-- Sub-process 4.2 ML Fusion Classifier -->
<circle cx="560" cy="190" r="50" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="510" y1="175" x2="610" y2="175" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="560" y="168" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">4.2</text>
<text x="560" y="195" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Multimodal</text>
<text x="560" y="210" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Fusion Model</text>

<!-- Sub-process 4.3 Baseline Comparison -->
<circle cx="800" cy="190" r="50" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="750" y1="175" x2="850" y2="175" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="800" y="168" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">4.3</text>
<text x="800" y="195" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Compare With</text>
<text x="800" y="210" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Personal Baseline</text>

<!-- Sub-process 4.4 SHAP XAI Attribution -->
<circle cx="560" cy="400" r="50" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="510" y1="385" x2="610" y2="385" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="560" y="378" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">4.4</text>
<text x="560" y="405" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Compute SHAP</text>
<text x="560" y="420" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Attributions</text>

<!-- Sub-process 4.5 Persist & Trigger Actions -->
<circle cx="560" cy="580" r="50" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.8"/>
<line x1="510" y1="565" x2="610" y2="565" stroke="#1e3a8a" stroke-width="1.2"/>
<text x="560" y="558" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e3a8a" text-anchor="middle">4.5</text>
<text x="560" y="585" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Persist &amp; Route</text>
<text x="560" y="600" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">To Recovery / Plan</text>

<!-- Data Stores -->
<path d="M 730 300 L 870 300 M 730 330 L 870 330" stroke="#0f172a" stroke-width="1.5"/>
<text x="800" y="320" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">D2: Baseline History</text>

<path d="M 250 565 L 390 565 M 250 595 L 390 595" stroke="#0f172a" stroke-width="1.5"/>
<text x="320" y="585" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">D3: Assessment Log</text>

<!-- Flows -->
<line x1="190" y1="120" x2="275" y2="170" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="190" y1="200" x2="270" y2="190" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<line x1="190" y1="280" x2="275" y2="210" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>

<line x1="370" y1="190" x2="510" y2="190" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<text x="440" y="180" font-family="Arial, sans-serif" font-size="9" fill="#0f172a" text-anchor="middle">Feature Vector</text>

<line x1="610" y1="190" x2="750" y2="190" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<text x="680" y="180" font-family="Arial, sans-serif" font-size="9" fill="#0f172a" text-anchor="middle">Stress Level (L/M/H)</text>

<line x1="800" y1="240" x2="800" y2="300" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>

<line x1="560" y1="240" x2="560" y2="350" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<text x="570" y="295" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">Prediction &amp; Weights</text>

<line x1="560" y1="450" x2="560" y2="530" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>
<text x="570" y="490" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">Attributions &amp; Triggers</text>

<line x1="510" y1="580" x2="390" y2="580" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- Final Output to User -->
<rect x="740" y="555" width="180" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<text x="830" y="577" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Student Mobile Dashboard</text>
<text x="830" y="593" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Level, XAI Factors, Recovery Plan</text>

<line x1="610" y1="580" x2="740" y2="580" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- Caption -->
<text x="{w/2}" y="{h-20}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.3.3: DFD Level 2 Detailed Multimodal Stress Fusion &amp; Explainability Pipeline</text>
</svg>'''

    write_files("05_DFD_Level_2_Stress_Detection", svg, b.to_xml())

# -------------------------------------------------------------
# 06_Component_Diagram
# -------------------------------------------------------------
def build_component_diagram():
    w, h = 1100, 800
    b = DrawioBuilder("06_Component_Diagram", w, h)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>
  </marker>
</defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="25" y="25" width="{w-50}" height="{h-60}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="45" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">MindEase System Component Diagram</text>

<!-- Component 1: Mobile App Package -->
<rect x="50" y="80" width="300" height="630" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" rx="4"/>
<text x="70" y="105" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e40af">&lt;&lt;component&gt;&gt; Mobile App (Flutter)</text>

<rect x="70" y="130" width="260" height="60" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="200" y="155" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Presentation Module</text>
<text x="200" y="175" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">UI Screens, Widgets, Charts</text>

<rect x="70" y="210" width="260" height="60" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="200" y="235" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">State Management (BLoC)</text>
<text x="200" y="255" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">AssessmentBloc, DiaryBloc, AuthBloc</text>

<rect x="70" y="290" width="260" height="60" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="200" y="315" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Audio Recording Module</text>
<text x="200" y="335" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Microphone Stream &amp; Codec</text>

<rect x="70" y="370" width="260" height="60" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="200" y="395" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Sensors &amp; Habit Collector</text>
<text x="200" y="415" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Step Counter, Screen Time API</text>

<rect x="70" y="450" width="260" height="60" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="200" y="475" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">API Client &amp; Dio Service</text>
<text x="200" y="495" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">REST Client, Interceptors, Tokens</text>

<rect x="70" y="530" width="260" height="60" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="200" y="555" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Local Secure Storage</text>
<text x="200" y="575" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Encrypted SharedPreferences, Cache</text>

<!-- Component 2: Backend Application Package -->
<rect x="400" y="80" width="340" height="630" fill="#f8fafc" stroke="#10b981" stroke-width="1.5" rx="4"/>
<text x="420" y="105" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#047857">&lt;&lt;component&gt;&gt; FastAPI Backend Server</text>

<rect x="420" y="130" width="300" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="570" y="152" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">API Gateway &amp; Middleware</text>
<text x="570" y="168" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">CORS, JWT Authentication, Logging</text>

<rect x="420" y="195" width="300" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="570" y="217" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Stress Assessment Controller</text>
<text x="570" y="233" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Scoring, PSS Rules, Habit Fusion</text>

<rect x="420" y="260" width="300" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="570" y="282" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Diary &amp; Safety Controller</text>
<text x="570" y="298" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Whisper Dispatch, Crisis Triggers</text>

<rect x="420" y="325" width="300" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="570" y="347" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Baseline &amp; XAI Service</text>
<text x="570" y="363" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Historical Deviation, SHAP Explainer</text>

<rect x="420" y="390" width="300" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="570" y="412" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Adaptive Study Planner Engine</text>
<text x="570" y="428" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Task Chunking &amp; Stress Load Tuning</text>

<rect x="420" y="455" width="300" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="570" y="477" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor &amp; Community Service</text>
<text x="570" y="493" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Booking, Clinical Notes, Moderation</text>

<rect x="420" y="520" width="300" height="50" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="570" y="542" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Payment Webhook Handler</text>
<text x="570" y="558" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Signature Verification &amp; Confirmation</text>

<!-- Component 3: Machine Learning Subsystem -->
<rect x="780" y="80" width="280" height="300" fill="#f8fafc" stroke="#8b5cf6" stroke-width="1.5" rx="4"/>
<text x="800" y="105" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#6d28d9">&lt;&lt;component&gt;&gt; ML &amp; NLP Models</text>

<rect x="800" y="125" width="240" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="920" y="147" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Whisper ASR Model</text>
<text x="920" y="162" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Speech Transcription (Urdu/English)</text>

<rect x="800" y="180" width="240" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="920" y="202" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Multimodal Stress Classifier</text>
<text x="920" y="217" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Scikit-learn / PyTorch Fusion</text>

<rect x="800" y="235" width="240" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="920" y="257" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">SHAP Attribution Engine</text>
<text x="920" y="272" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Explainability Heatmap &amp; Drivers</text>

<rect x="800" y="290" width="240" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="920" y="312" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Conversational Chatbot LLM</text>
<text x="920" y="327" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Contextual Student Support</text>

<!-- Component 4: Persistence Subsystem -->
<rect x="780" y="410" width="280" height="300" fill="#f8fafc" stroke="#0284c7" stroke-width="1.5" rx="4"/>
<text x="800" y="435" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0369a1">&lt;&lt;component&gt;&gt; Supabase Cloud</text>

<rect x="800" y="455" width="240" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="920" y="477" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">PostgreSQL Database</text>
<text x="920" y="492" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Relational Schema &amp; Views</text>

<rect x="800" y="510" width="240" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="920" y="532" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Supabase Auth (GoTrue)</text>
<text x="920" y="547" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">JWT, RLS Policy Security</text>

<rect x="800" y="565" width="240" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="920" y="587" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Encrypted Diary Store</text>
<text x="920" y="602" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">AES-256 Storage Isolation</text>

<rect x="800" y="620" width="240" height="45" fill="#ffffff" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="920" y="642" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Object Media Storage</text>
<text x="920" y="657" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Audio &amp; Video Relaxation Files</text>

<!-- Connectors -->
<line x1="350" y1="200" x2="400" y2="200" stroke="#0f172a" stroke-width="1.5" marker-end="url(#arrow)"/>
<line x1="740" y1="200" x2="780" y2="200" stroke="#0f172a" stroke-width="1.5" marker-end="url(#arrow)"/>
<line x1="740" y1="500" x2="780" y2="500" stroke="#0f172a" stroke-width="1.5" marker-end="url(#arrow)"/>

<!-- Caption -->
<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.1.2: MindEase Component Diagram (Presentation, Business Logic, AI, and Persistence Layers)</text>
</svg>'''

    write_files("06_Component_Diagram", svg, b.to_xml())

# -------------------------------------------------------------
# 07_Deployment_Diagram
# -------------------------------------------------------------
def build_deployment_diagram():
    w, h = 1100, 750
    b = DrawioBuilder("07_Deployment_Diagram", w, h)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>
  </marker>
</defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="25" y="25" width="{w-50}" height="{h-60}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="45" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">MindEase UML Deployment Diagram</text>

<!-- NODE 1: Mobile Device (Student / Counselor) -->
<path d="M 60 120 L 75 100 L 335 100 L 320 120 Z M 335 100 L 335 480 L 320 500 L 320 120 Z" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.5"/>
<rect x="60" y="120" width="260" height="380" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<text x="190" y="145" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">&lt;&lt;device&gt;&gt;</text>
<text x="190" y="165" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Android Smartphone</text>
<text x="190" y="180" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">OS: Android 9.0+ (Pie / 10 / 11 / 12 / 13 / 14)</text>

<!-- Artifact inside mobile -->
<rect x="80" y="200" width="220" height="60" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.2" rx="4"/>
<text x="190" y="225" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e40af" text-anchor="middle">&lt;&lt;artifact&gt;&gt;</text>
<text x="190" y="245" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">MindEase_App.apk</text>

<rect x="80" y="275" width="220" height="50" fill="#f8fafc" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="190" y="297" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Hardware: Microphone</text>
<text x="190" y="313" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Audio capture (16kHz PCM)</text>

<rect x="80" y="340" width="220" height="50" fill="#f8fafc" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="190" y="362" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Hardware: Step Sensors</text>
<text x="190" y="378" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Pedometer / Activity recognition</text>

<rect x="80" y="405" width="220" height="50" fill="#f8fafc" stroke="#64748b" stroke-width="1.2" rx="4"/>
<text x="190" y="427" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Secure SQLite Storage</text>
<text x="190" y="443" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Offline cache &amp; session tokens</text>

<!-- NODE 2: Cloud Application Server (FastAPI + AI) -->
<path d="M 420 120 L 435 100 L 735 100 L 720 120 Z M 735 100 L 735 550 L 720 570 L 720 120 Z" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.5"/>
<rect x="420" y="120" width="300" height="450" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<text x="570" y="145" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">&lt;&lt;execution environment&gt;&gt;</text>
<text x="570" y="165" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Cloud VM / Container</text>
<text x="570" y="180" font-family="Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Ubuntu Linux 22.04 LTS / Docker</text>

<!-- Artifact inside Server -->
<rect x="440" y="200" width="260" height="60" fill="#f8fafc" stroke="#10b981" stroke-width="1.2" rx="4"/>
<text x="570" y="225" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">&lt;&lt;artifact&gt;&gt;</text>
<text x="570" y="245" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">FastAPI ASGI Application (Python 3.11)</text>

<rect x="440" y="275" width="260" height="60" fill="#f8fafc" stroke="#8b5cf6" stroke-width="1.2" rx="4"/>
<text x="570" y="300" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#6d28d9" text-anchor="middle">&lt;&lt;artifact&gt;&gt;</text>
<text x="570" y="320" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Whisper ASR Inference Worker</text>

<rect x="440" y="350" width="260" height="60" fill="#f8fafc" stroke="#8b5cf6" stroke-width="1.2" rx="4"/>
<text x="570" y="375" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#6d28d9" text-anchor="middle">&lt;&lt;artifact&gt;&gt;</text>
<text x="570" y="395" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Multimodal Fusion Model (PyTorch)</text>

<rect x="440" y="425" width="260" height="60" fill="#f8fafc" stroke="#8b5cf6" stroke-width="1.2" rx="4"/>
<text x="570" y="450" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#6d28d9" text-anchor="middle">&lt;&lt;artifact&gt;&gt;</text>
<text x="570" y="470" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">SHAP XAI Explainer Engine</text>

<!-- NODE 3: Supabase Cloud Managed -->
<path d="M 800 120 L 815 100 L 1055 100 L 1040 120 Z M 1055 100 L 1055 380 L 1040 400 L 1040 120 Z" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.5"/>
<rect x="800" y="120" width="240" height="280" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<text x="920" y="145" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">&lt;&lt;cloud system&gt;&gt;</text>
<text x="920" y="165" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Supabase Managed Cloud</text>

<rect x="820" y="190" width="200" height="50" fill="#f8fafc" stroke="#0284c7" stroke-width="1.2" rx="4"/>
<text x="920" y="212" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">PostgreSQL Database (v15)</text>
<text x="920" y="228" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">PostgREST &amp; RLS Engine</text>

<rect x="820" y="250" width="200" height="50" fill="#f8fafc" stroke="#0284c7" stroke-width="1.2" rx="4"/>
<text x="920" y="272" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">GoTrue Auth Provider</text>
<text x="920" y="288" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">JWT Issue &amp; Verify</text>

<rect x="820" y="310" width="200" height="50" fill="#f8fafc" stroke="#0284c7" stroke-width="1.2" rx="4"/>
<text x="920" y="332" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">S3 Object Storage</text>
<text x="920" y="348" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Media &amp; Audio Store</text>

<!-- NODE 4: Polar Payment Cloud Gateway -->
<path d="M 800 450 L 815 430 L 1055 430 L 1040 450 Z M 1055 430 L 1055 580 L 1040 600 L 1040 450 Z" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.5"/>
<rect x="800" y="450" width="240" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<text x="920" y="475" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">&lt;&lt;external service&gt;&gt;</text>
<text x="920" y="495" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Payment Gateway</text>

<rect x="820" y="515" width="200" height="50" fill="#f8fafc" stroke="#f59e0b" stroke-width="1.2" rx="4"/>
<text x="920" y="537" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Sandbox Payment &amp; Webhook</text>
<text x="920" y="553" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">HMAC-SHA256 Webhooks</text>

<!-- Communication Paths -->
<line x1="320" y1="280" x2="420" y2="280" stroke="#0f172a" stroke-width="1.8"/>
<text x="370" y="270" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">HTTPS / WSS</text>
<text x="370" y="295" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">TLS 1.3</text>

<line x1="720" y1="260" x2="800" y2="260" stroke="#0f172a" stroke-width="1.8"/>
<text x="760" y="250" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">TCP 5432</text>
<text x="760" y="275" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Encrypted</text>

<line x1="720" y1="520" x2="800" y2="520" stroke="#0f172a" stroke-width="1.8"/>
<text x="760" y="510" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">HTTPS</text>
<text x="760" y="535" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">REST Webhook</text>

<!-- Caption -->
<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.1.3: MindEase UML Deployment Diagram (Physical Nodes, Artifacts &amp; Protocols)</text>
</svg>'''

    write_files("07_Deployment_Diagram", svg, b.to_xml())

# -------------------------------------------------------------
# 08_Class_Diagram
# -------------------------------------------------------------
def build_class_diagram():
    w, h = 1200, 1000
    b = DrawioBuilder("08_Class_Diagram", w, h)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <marker id="inheritance" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
  </marker>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>
  </marker>
</defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="20" y="20" width="{w-40}" height="{h-50}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="40" y="45" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">MindEase Domain UML Class Diagram</text>

<!-- Class 1: User (Base) -->
<rect x="490" y="60" width="220" height="130" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="490" y="60" width="220" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="600" y="78" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">User</text>
<text x="500" y="100" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- id: UUID</text>
<text x="500" y="114" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- name: String</text>
<text x="500" y="128" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- email: String</text>
<text x="500" y="142" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- role: UserRole</text>
<line x1="490" y1="148" x2="710" y2="148" stroke="#0f172a" stroke-width="1"/>
<text x="500" y="162" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ register(): Boolean</text>
<text x="500" y="176" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ login(): TokenSession</text>

<!-- Class 2: Student (extends User) -->
<rect x="220" y="240" width="220" height="130" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="220" y="240" width="220" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="330" y="258" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Student</text>
<text x="230" y="280" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- universityId: String</text>
<text x="230" y="294" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- academicProgram: String</text>
<text x="230" y="308" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- baselineScore: Float</text>
<line x1="220" y1="314" x2="440" y2="314" stroke="#0f172a" stroke-width="1"/>
<text x="230" y="328" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ takeAssessment(): Result</text>
<text x="230" y="342" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ logDiary(): DiaryEntry</text>
<text x="230" y="356" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ bookCounselor(): Appt</text>

<!-- Class 3: Counselor (extends User) -->
<rect x="490" y="240" width="220" height="130" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="490" y="240" width="220" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="600" y="258" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Counselor</text>
<text x="500" y="280" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- licenseNumber: String</text>
<text x="500" y="294" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- specialization: String</text>
<text x="500" y="308" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- isApproved: Boolean</text>
<line x1="490" y1="314" x2="710" y2="314" stroke="#0f172a" stroke-width="1"/>
<text x="500" y="328" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ reviewHistory(): Records</text>
<text x="500" y="342" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ addClinicalNote(): Note</text>
<text x="500" y="356" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ setAvailability(): Slots</text>

<!-- Class 4: Administrator (extends User) -->
<rect x="760" y="240" width="220" height="130" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="760" y="240" width="220" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="870" y="258" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Administrator</text>
<text x="770" y="280" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- adminLevel: Int</text>
<text x="770" y="294" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- lastLoginIp: String</text>
<line x1="760" y1="304" x2="980" y2="304" stroke="#0f172a" stroke-width="1"/>
<text x="770" y="320" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ approveCounselor(): Bool</text>
<text x="770" y="336" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ moderateReport(): Bool</text>
<text x="770" y="352" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ manageContent(): Item</text>

<!-- Inheritance arrows to User -->
<line x1="330" y1="240" x2="330" y2="210" stroke="#0f172a" stroke-width="1.5"/>
<line x1="330" y1="210" x2="600" y2="210" stroke="#0f172a" stroke-width="1.5"/>
<line x1="600" y1="210" x2="600" y2="190" stroke="#0f172a" stroke-width="1.5" marker-end="url(#inheritance)"/>

<line x1="600" y1="240" x2="600" y2="190" stroke="#0f172a" stroke-width="1.5"/>

<line x1="870" y1="240" x2="870" y2="210" stroke="#0f172a" stroke-width="1.5"/>
<line x1="870" y1="210" x2="600" y2="210" stroke="#0f172a" stroke-width="1.5"/>

<!-- Class 5: StressAssessment -->
<rect x="50" y="440" width="220" height="140" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="50" y="440" width="220" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="160" y="458" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">StressAssessment</text>
<text x="60" y="480" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- assessmentId: UUID</text>
<text x="60" y="494" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- stressLevel: StressEnum</text>
<text x="60" y="508" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- confidence: Float</text>
<text x="60" y="522" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- timestamp: DateTime</text>
<line x1="50" y1="528" x2="270" y2="528" stroke="#0f172a" stroke-width="1"/>
<text x="60" y="544" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ fuseInputs(): Level</text>
<text x="60" y="560" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ triggerAlert(): Boolean</text>

<!-- Class 6: XAIInsight -->
<rect x="50" y="650" width="220" height="130" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="50" y="650" width="220" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="160" y="668" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">XAIInsight</text>
<text x="60" y="690" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- insightId: UUID</text>
<text x="60" y="704" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- topDrivers: List&lt;String&gt;</text>
<text x="60" y="718" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- shapWeights: Map&lt;Str,Flt&gt;</text>
<line x1="50" y1="724" x2="270" y2="724" stroke="#0f172a" stroke-width="1"/>
<text x="60" y="740" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ computeShap(): Map</text>
<text x="60" y="756" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ generateTips(): List</text>

<!-- Class 7: DailyDiary -->
<rect x="300" y="440" width="200" height="140" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="300" y="440" width="200" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="400" y="458" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">DailyDiary</text>
<text x="310" y="480" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- diaryId: UUID</text>
<text x="310" y="494" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- audioUrl: String</text>
<text x="310" y="508" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- transcribedText: String</text>
<text x="310" y="522" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- sentimentScore: Float</text>
<line x1="300" y1="528" x2="500" y2="528" stroke="#0f172a" stroke-width="1"/>
<text x="310" y="544" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ transcribe(): String</text>
<text x="310" y="560" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ checkCrisis(): Boolean</text>

<!-- Class 8: AdaptiveStudyPlan -->
<rect x="300" y="650" width="200" height="130" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="300" y="650" width="200" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="400" y="668" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">AdaptiveStudyPlan</text>
<text x="310" y="690" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- planId: UUID</text>
<text x="310" y="704" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- sessionDuration: Int</text>
<text x="310" y="718" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- breakDuration: Int</text>
<line x1="300" y1="724" x2="500" y2="724" stroke="#0f172a" stroke-width="1"/>
<text x="310" y="740" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ adaptToStress(): Plan</text>
<text x="310" y="756" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ reschedule(): Bool</text>

<!-- Class 9: Appointment -->
<rect x="530" y="440" width="210" height="140" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="530" y="440" width="210" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="635" y="458" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Appointment</text>
<text x="540" y="480" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- appointmentId: UUID</text>
<text x="540" y="494" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- scheduledAt: DateTime</text>
<text x="540" y="508" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- status: ApptStatus</text>
<text x="540" y="522" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- isFreeTier: Boolean</text>
<line x1="530" y1="528" x2="740" y2="528" stroke="#0f172a" stroke-width="1"/>
<text x="540" y="544" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ confirmBooking(): Bool</text>
<text x="540" y="560" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ completeSession(): Void</text>

<!-- Class 10: PaymentTransaction -->
<rect x="530" y="650" width="210" height="130" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="530" y="650" width="210" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="635" y="668" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">PaymentTransaction</text>
<text x="540" y="690" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- transactionId: UUID</text>
<text x="540" y="704" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- polarPaymentId: String</text>
<text x="540" y="718" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- amount: Decimal</text>
<line x1="530" y1="724" x2="740" y2="724" stroke="#0f172a" stroke-width="1"/>
<text x="540" y="740" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ initiateCheckout(): Url</text>
<text x="540" y="756" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ verifyWebhook(): Bool</text>

<!-- Class 11: CommunityPost -->
<rect x="770" y="440" width="210" height="140" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="770" y="440" width="210" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="875" y="458" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">CommunityPost</text>
<text x="780" y="480" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- postId: UUID</text>
<text x="780" y="494" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- isAnonymous: Boolean</text>
<text x="780" y="508" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- content: String</text>
<text x="780" y="522" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- reportCount: Int</text>
<line x1="770" y1="528" x2="980" y2="528" stroke="#0f172a" stroke-width="1"/>
<text x="780" y="544" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ flagPost(): Void</text>
<text x="780" y="560" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ addReply(): Reply</text>

<!-- Class 12: ContentResource -->
<rect x="770" y="650" width="210" height="130" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="770" y="650" width="210" height="26" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<text x="875" y="668" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">ContentResource</text>
<text x="780" y="690" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- contentId: UUID</text>
<text x="780" y="704" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- title: String</text>
<text x="780" y="718" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">- mediaType: MediaEnum</text>
<line x1="770" y1="724" x2="980" y2="724" stroke="#0f172a" stroke-width="1"/>
<text x="780" y="740" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ streamMedia(): Stream</text>
<text x="780" y="756" font-family="Arial, sans-serif" font-size="10" fill="#0f172a">+ rateEffectiveness(): Void</text>

<!-- Relationships / Multiplicities -->
<line x1="250" y1="370" x2="160" y2="440" stroke="#0f172a" stroke-width="1.3"/>
<text x="210" y="415" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">1 .. *</text>

<line x1="160" y1="580" x2="160" y2="650" stroke="#0f172a" stroke-width="1.3"/>
<text x="170" y="620" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">1 .. 1</text>

<line x1="330" y1="370" x2="350" y2="440" stroke="#0f172a" stroke-width="1.3"/>
<text x="350" y="415" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">1 .. *</text>

<line x1="635" y1="370" x2="635" y2="440" stroke="#0f172a" stroke-width="1.3"/>
<text x="645" y="415" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">1 .. *</text>

<line x1="635" y1="580" x2="635" y2="650" stroke="#0f172a" stroke-width="1.3"/>
<text x="645" y="620" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">0 .. 1</text>

<!-- Caption -->
<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.2.1: MindEase Domain UML Class Diagram with Relationships &amp; Multiplicities</text>
</svg>'''

    write_files("08_Class_Diagram", svg, b.to_xml())

# -------------------------------------------------------------
# 09_Entity_Relationship_Diagram
# -------------------------------------------------------------
def build_erd_diagram():
    w, h = 1150, 850
    b = DrawioBuilder("09_Entity_Relationship_Diagram", w, h)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="20" y="20" width="{w-40}" height="{h-50}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="40" y="45" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Entity Relationship Diagram (ERD) - Crow's Foot Notation</text>

<!-- ENTITY: USERS -->
<rect x="475" y="70" width="200" height="120" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="475" y="70" width="200" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
<text x="575" y="86" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">USERS</text>
<text x="485" y="106" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">PK  user_id: UUID</text>
<text x="485" y="120" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">    email: VARCHAR(255)</text>
<text x="485" y="134" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">    password_hash: VARCHAR</text>
<text x="485" y="148" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">    role: VARCHAR(20)</text>
<text x="485" y="162" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">    created_at: TIMESTAMP</text>

<!-- ENTITY: STUDENTS -->
<rect x="180" y="220" width="200" height="110" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="180" y="220" width="200" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
<text x="280" y="236" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">STUDENTS</text>
<text x="190" y="256" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">PK,FK user_id: UUID</text>
<text x="190" y="270" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">      university_id: VARCHAR</text>
<text x="190" y="284" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">      program: VARCHAR(100)</text>
<text x="190" y="298" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">      baseline_score: NUMERIC</text>

<!-- ENTITY: COUNSELORS -->
<rect x="770" y="220" width="200" height="110" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="770" y="220" width="200" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
<text x="870" y="236" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">COUNSELORS</text>
<text x="780" y="256" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">PK,FK user_id: UUID</text>
<text x="780" y="270" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">      license_number: VARCHAR</text>
<text x="780" y="284" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">      specialization: VARCHAR</text>
<text x="780" y="298" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">      is_approved: BOOLEAN</text>

<!-- ENTITY: STRESS_ASSESSMENTS -->
<rect x="50" y="380" width="220" height="120" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="50" y="380" width="220" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
<text x="160" y="396" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">STRESS_ASSESSMENTS</text>
<text x="60" y="416" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">PK  assessment_id: UUID</text>
<text x="60" y="430" font-family="Arial, sans-serif" font-size="9">FK  student_id: UUID</text>
<text x="60" y="444" font-family="Arial, sans-serif" font-size="9">    stress_level: VARCHAR(15)</text>
<text x="60" y="458" font-family="Arial, sans-serif" font-size="9">    confidence: NUMERIC(4,3)</text>
<text x="60" y="472" font-family="Arial, sans-serif" font-size="9">    created_at: TIMESTAMP</text>

<!-- ENTITY: XAI_INSIGHTS -->
<rect x="50" y="550" width="220" height="110" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="50" y="550" width="220" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
<text x="160" y="566" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">XAI_INSIGHTS</text>
<text x="60" y="586" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">PK  insight_id: UUID</text>
<text x="60" y="600" font-family="Arial, sans-serif" font-size="9">FK  assessment_id: UUID</text>
<text x="60" y="614" font-family="Arial, sans-serif" font-size="9">    feature_weights: JSONB</text>
<text x="60" y="628" font-family="Arial, sans-serif" font-size="9">    primary_drivers: TEXT[]</text>

<!-- ENTITY: DIARY_ENTRIES -->
<rect x="300" y="380" width="210" height="120" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="300" y="380" width="210" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
<text x="405" y="396" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">DIARY_ENTRIES</text>
<text x="310" y="416" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">PK  entry_id: UUID</text>
<text x="310" y="430" font-family="Arial, sans-serif" font-size="9">FK  student_id: UUID</text>
<text x="310" y="444" font-family="Arial, sans-serif" font-size="9">    encrypted_content: TEXT</text>
<text x="310" y="458" font-family="Arial, sans-serif" font-size="9">    sentiment_score: NUMERIC</text>
<text x="310" y="472" font-family="Arial, sans-serif" font-size="9">    is_crisis: BOOLEAN</text>

<!-- ENTITY: HABIT_LOGS -->
<rect x="300" y="550" width="210" height="120" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="300" y="550" width="210" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
<text x="405" y="566" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">HABIT_LOGS</text>
<text x="310" y="586" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">PK  habit_id: UUID</text>
<text x="310" y="600" font-family="Arial, sans-serif" font-size="9">FK  student_id: UUID</text>
<text x="310" y="614" font-family="Arial, sans-serif" font-size="9">    sleep_hours: NUMERIC(4,2)</text>
<text x="310" y="628" font-family="Arial, sans-serif" font-size="9">    screen_time_mins: INT</text>
<text x="310" y="642" font-family="Arial, sans-serif" font-size="9">    step_count: INT</text>

<!-- ENTITY: APPOINTMENTS -->
<rect x="540" y="380" width="200" height="130" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="540" y="380" width="200" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
<text x="640" y="396" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">APPOINTMENTS</text>
<text x="550" y="416" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">PK  appointment_id: UUID</text>
<text x="550" y="430" font-family="Arial, sans-serif" font-size="9">FK  student_id: UUID</text>
<text x="550" y="444" font-family="Arial, sans-serif" font-size="9">FK  counselor_id: UUID</text>
<text x="550" y="458" font-family="Arial, sans-serif" font-size="9">    scheduled_time: TIMESTAMP</text>
<text x="550" y="472" font-family="Arial, sans-serif" font-size="9">    is_free: BOOLEAN</text>
<text x="550" y="486" font-family="Arial, sans-serif" font-size="9">    status: VARCHAR(20)</text>

<!-- ENTITY: PAYMENTS -->
<rect x="540" y="550" width="200" height="120" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="540" y="550" width="200" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
<text x="640" y="566" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">PAYMENTS</text>
<text x="550" y="586" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">PK  payment_id: UUID</text>
<text x="550" y="600" font-family="Arial, sans-serif" font-size="9">FK  appointment_id: UUID</text>
<text x="550" y="614" font-family="Arial, sans-serif" font-size="9">    polar_checkout_id: VARCHAR</text>
<text x="550" y="628" font-family="Arial, sans-serif" font-size="9">    amount: NUMERIC(10,2)</text>
<text x="550" y="642" font-family="Arial, sans-serif" font-size="9">    status: VARCHAR(20)</text>

<!-- ENTITY: COMMUNITY_POSTS -->
<rect x="770" y="380" width="200" height="120" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="770" y="380" width="200" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
<text x="870" y="396" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">COMMUNITY_POSTS</text>
<text x="780" y="416" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">PK  post_id: UUID</text>
<text x="780" y="430" font-family="Arial, sans-serif" font-size="9">FK  author_id: UUID</text>
<text x="780" y="444" font-family="Arial, sans-serif" font-size="9">    is_anonymous: BOOLEAN</text>
<text x="780" y="458" font-family="Arial, sans-serif" font-size="9">    content: TEXT</text>
<text x="780" y="472" font-family="Arial, sans-serif" font-size="9">    report_count: INT</text>

<!-- ENTITY: CLINICAL_NOTES -->
<rect x="770" y="550" width="200" height="120" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="770" y="550" width="200" height="24" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.5"/>
<text x="870" y="566" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">CLINICAL_NOTES</text>
<text x="780" y="586" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#0f172a">PK  note_id: UUID</text>
<text x="780" y="600" font-family="Arial, sans-serif" font-size="9">FK  appointment_id: UUID</text>
<text x="780" y="614" font-family="Arial, sans-serif" font-size="9">    encrypted_notes: TEXT</text>
<text x="780" y="628" font-family="Arial, sans-serif" font-size="9">    created_at: TIMESTAMP</text>

<!-- Crow's Foot Connector Lines -->
<line x1="475" y1="130" x2="380" y2="230" stroke="#0f172a" stroke-width="1.2"/>
<line x1="675" y1="130" x2="770" y2="230" stroke="#0f172a" stroke-width="1.2"/>

<line x1="220" y1="330" x2="160" y2="380" stroke="#0f172a" stroke-width="1.2"/>
<line x1="280" y1="330" x2="350" y2="380" stroke="#0f172a" stroke-width="1.2"/>
<line x1="330" y1="330" x2="350" y2="550" stroke="#0f172a" stroke-width="1.2"/>

<line x1="160" y1="500" x2="160" y2="550" stroke="#0f172a" stroke-width="1.2"/>
<line x1="640" y1="510" x2="640" y2="550" stroke="#0f172a" stroke-width="1.2"/>
<line x1="740" y1="440" x2="770" y2="580" stroke="#0f172a" stroke-width="1.2"/>

<!-- Caption -->
<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.3.4: MindEase Entity Relationship Diagram (ERD) with Primary/Foreign Keys</text>
</svg>'''

    write_files("09_Entity_Relationship_Diagram", svg, b.to_xml())

# -------------------------------------------------------------
# 10_Database_Schema
# -------------------------------------------------------------
def build_database_schema():
    w, h = 1100, 750
    b = DrawioBuilder("10_Database_Schema", w, h)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="20" y="20" width="{w-40}" height="{h-50}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="40" y="45" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">MindEase Relational Database Schema Design (PostgreSQL / Supabase)</text>

<!-- Tables side by side -->
<!-- T1: users -->
<rect x="50" y="80" width="220" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="50" y="80" width="220" height="22" fill="#1e3a8a"/>
<text x="160" y="96" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.users</text>
<text x="60" y="118" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK  id: UUID (DEFAULT gen_random_uuid())</text>
<text x="60" y="132" font-family="Arial, sans-serif" font-size="9">    email: VARCHAR(255) UNIQUE NOT NULL</text>
<text x="60" y="146" font-family="Arial, sans-serif" font-size="9">    encrypted_password: VARCHAR(255)</text>
<text x="60" y="160" font-family="Arial, sans-serif" font-size="9">    role: VARCHAR(20) NOT NULL</text>
<text x="60" y="174" font-family="Arial, sans-serif" font-size="9">    is_active: BOOLEAN DEFAULT TRUE</text>
<text x="60" y="188" font-family="Arial, sans-serif" font-size="9">    created_at: TIMESTAMPTZ DEFAULT NOW()</text>

<!-- T2: students -->
<rect x="310" y="80" width="230" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="310" y="80" width="230" height="22" fill="#1e3a8a"/>
<text x="425" y="96" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.students</text>
<text x="320" y="118" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK,FK user_id: UUID REFERENCES users(id)</text>
<text x="320" y="132" font-family="Arial, sans-serif" font-size="9">      registration_num: VARCHAR(50)</text>
<text x="320" y="146" font-family="Arial, sans-serif" font-size="9">      department: VARCHAR(100)</text>
<text x="320" y="160" font-family="Arial, sans-serif" font-size="9">      current_semester: INT</text>
<text x="320" y="174" font-family="Arial, sans-serif" font-size="9">      baseline_stress: NUMERIC(4,2)</text>
<text x="320" y="188" font-family="Arial, sans-serif" font-size="9">      consent_share_data: BOOLEAN</text>

<!-- T3: stress_assessments -->
<rect x="580" y="80" width="240" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="580" y="80" width="240" height="22" fill="#1e3a8a"/>
<text x="700" y="96" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.stress_assessments</text>
<text x="590" y="118" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK  id: UUID PRIMARY KEY</text>
<text x="590" y="132" font-family="Arial, sans-serif" font-size="9">FK  student_id: UUID REFERENCES students</text>
<text x="590" y="146" font-family="Arial, sans-serif" font-size="9">    stress_level: VARCHAR(15) -- Low/Mod/High</text>
<text x="590" y="160" font-family="Arial, sans-serif" font-size="9">    confidence_score: NUMERIC(4,3)</text>
<text x="590" y="174" font-family="Arial, sans-serif" font-size="9">    feature_snapshot: JSONB</text>
<text x="590" y="188" font-family="Arial, sans-serif" font-size="9">    created_at: TIMESTAMPTZ DEFAULT NOW()</text>

<!-- T4: appointments -->
<rect x="850" y="80" width="210" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="850" y="80" width="210" height="22" fill="#1e3a8a"/>
<text x="955" y="96" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.appointments</text>
<text x="860" y="118" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK  id: UUID PRIMARY KEY</text>
<text x="860" y="132" font-family="Arial, sans-serif" font-size="9">FK  student_id: UUID REFERENCES students</text>
<text x="860" y="146" font-family="Arial, sans-serif" font-size="9">FK  counselor_id: UUID REFERENCES counselors</text>
<text x="860" y="160" font-family="Arial, sans-serif" font-size="9">    slot_start: TIMESTAMPTZ NOT NULL</text>
<text x="860" y="174" font-family="Arial, sans-serif" font-size="9">    is_free_session: BOOLEAN DEFAULT FALSE</text>
<text x="860" y="188" font-family="Arial, sans-serif" font-size="9">    status: VARCHAR(20) DEFAULT 'Pending'</text>

<!-- Row 2 -->
<!-- T5: habit_logs -->
<rect x="50" y="270" width="220" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="50" y="270" width="220" height="22" fill="#1e3a8a"/>
<text x="160" y="286" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.habit_logs</text>
<text x="60" y="308" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK  id: UUID PRIMARY KEY</text>
<text x="60" y="322" font-family="Arial, sans-serif" font-size="9">FK  student_id: UUID REFERENCES students</text>
<text x="60" y="336" font-family="Arial, sans-serif" font-size="9">    sleep_duration_hours: NUMERIC(4,2)</text>
<text x="60" y="350" font-family="Arial, sans-serif" font-size="9">    screen_time_minutes: INT</text>
<text x="60" y="364" font-family="Arial, sans-serif" font-size="9">    daily_steps: INT</text>
<text x="60" y="378" font-family="Arial, sans-serif" font-size="9">    log_date: DATE DEFAULT CURRENT_DATE</text>

<!-- T6: diary_entries -->
<rect x="310" y="270" width="230" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="310" y="270" width="230" height="22" fill="#1e3a8a"/>
<text x="425" y="286" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.diary_entries</text>
<text x="320" y="308" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK  id: UUID PRIMARY KEY</text>
<text x="320" y="322" font-family="Arial, sans-serif" font-size="9">FK  student_id: UUID REFERENCES students</text>
<text x="320" y="336" font-family="Arial, sans-serif" font-size="9">    entry_type: VARCHAR(10) -- Voice/Text</text>
<text x="320" y="350" font-family="Arial, sans-serif" font-size="9">    encrypted_text: TEXT NOT NULL</text>
<text x="320" y="364" font-family="Arial, sans-serif" font-size="9">    sentiment_valence: NUMERIC(4,2)</text>
<text x="320" y="378" font-family="Arial, sans-serif" font-size="9">    danger_flag: BOOLEAN DEFAULT FALSE</text>

<!-- T7: xai_insights -->
<rect x="580" y="270" width="240" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="580" y="270" width="240" height="22" fill="#1e3a8a"/>
<text x="700" y="286" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.xai_insights</text>
<text x="590" y="308" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK  id: UUID PRIMARY KEY</text>
<text x="590" y="322" font-family="Arial, sans-serif" font-size="9">FK  assessment_id: UUID REFERENCES stress</text>
<text x="590" y="336" font-family="Arial, sans-serif" font-size="9">    shap_attribution: JSONB NOT NULL</text>
<text x="590" y="350" font-family="Arial, sans-serif" font-size="9">    top_contributing_factors: TEXT[]</text>
<text x="590" y="364" font-family="Arial, sans-serif" font-size="9">    plain_english_summary: TEXT</text>
<text x="590" y="378" font-family="Arial, sans-serif" font-size="9">    recommended_actions: TEXT[]</text>

<!-- T8: polar_payments -->
<rect x="850" y="270" width="210" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="850" y="270" width="210" height="22" fill="#1e3a8a"/>
<text x="955" y="286" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.polar_payments</text>
<text x="860" y="308" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK  id: UUID PRIMARY KEY</text>
<text x="860" y="322" font-family="Arial, sans-serif" font-size="9">FK  appointment_id: UUID REFERENCES appts</text>
<text x="860" y="336" font-family="Arial, sans-serif" font-size="9">    polar_checkout_session: VARCHAR(100)</text>
<text x="860" y="350" font-family="Arial, sans-serif" font-size="9">    amount_cents: INT NOT NULL</text>
<text x="860" y="364" font-family="Arial, sans-serif" font-size="9">    currency: VARCHAR(10) DEFAULT 'PKR'</text>
<text x="860" y="378" font-family="Arial, sans-serif" font-size="9">    payment_status: VARCHAR(20)</text>

<!-- Row 3 -->
<!-- T9: adaptive_study_plans -->
<rect x="50" y="460" width="220" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="50" y="460" width="220" height="22" fill="#1e3a8a"/>
<text x="160" y="476" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.adaptive_study_plans</text>
<text x="60" y="498" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK  id: UUID PRIMARY KEY</text>
<text x="60" y="512" font-family="Arial, sans-serif" font-size="9">FK  student_id: UUID REFERENCES students</text>
<text x="60" y="526" font-family="Arial, sans-serif" font-size="9">    plan_date: DATE DEFAULT CURRENT_DATE</text>
<text x="60" y="540" font-family="Arial, sans-serif" font-size="9">    stress_adaptation_mode: VARCHAR(20)</text>
<text x="60" y="554" font-family="Arial, sans-serif" font-size="9">    task_schedule: JSONB NOT NULL</text>
<text x="60" y="568" font-family="Arial, sans-serif" font-size="9">    completion_percentage: NUMERIC(5,2)</text>

<!-- T10: community_posts -->
<rect x="310" y="460" width="230" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="310" y="460" width="230" height="22" fill="#1e3a8a"/>
<text x="425" y="476" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.community_posts</text>
<text x="320" y="498" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK  id: UUID PRIMARY KEY</text>
<text x="320" y="512" font-family="Arial, sans-serif" font-size="9">FK  author_id: UUID REFERENCES users(id)</text>
<text x="320" y="526" font-family="Arial, sans-serif" font-size="9">    is_anonymous: BOOLEAN DEFAULT FALSE</text>
<text x="320" y="540" font-family="Arial, sans-serif" font-size="9">    content: TEXT NOT NULL</text>
<text x="320" y="554" font-family="Arial, sans-serif" font-size="9">    flag_count: INT DEFAULT 0</text>
<text x="320" y="568" font-family="Arial, sans-serif" font-size="9">    is_hidden: BOOLEAN DEFAULT FALSE</text>

<!-- T11: content_library -->
<rect x="580" y="460" width="240" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="580" y="460" width="240" height="22" fill="#1e3a8a"/>
<text x="700" y="476" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.content_library</text>
<text x="590" y="498" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK  id: UUID PRIMARY KEY</text>
<text x="590" y="512" font-family="Arial, sans-serif" font-size="9">    title: VARCHAR(200) NOT NULL</text>
<text x="590" y="526" font-family="Arial, sans-serif" font-size="9">    category: VARCHAR(50) -- Music/Stories</text>
<text x="590" y="540" font-family="Arial, sans-serif" font-size="9">    media_url: TEXT NOT NULL</text>
<text x="590" y="554" font-family="Arial, sans-serif" font-size="9">    effectiveness_rating: NUMERIC(3,2)</text>
<text x="590" y="568" font-family="Arial, sans-serif" font-size="9">    is_active: BOOLEAN DEFAULT TRUE</text>

<!-- T12: counselor_clinical_notes -->
<rect x="850" y="460" width="210" height="150" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<rect x="850" y="460" width="210" height="22" fill="#1e3a8a"/>
<text x="955" y="476" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">public.clinical_notes</text>
<text x="860" y="498" font-family="Arial, sans-serif" font-size="9" font-weight="bold">PK  id: UUID PRIMARY KEY</text>
<text x="860" y="512" font-family="Arial, sans-serif" font-size="9">FK  appointment_id: UUID REFERENCES appts</text>
<text x="860" y="526" font-family="Arial, sans-serif" font-size="9">FK  counselor_id: UUID REFERENCES counselors</text>
<text x="860" y="540" font-family="Arial, sans-serif" font-size="9">    encrypted_clinical_summary: TEXT</text>
<text x="860" y="554" font-family="Arial, sans-serif" font-size="9">    follow_up_recommendation: TEXT</text>
<text x="860" y="568" font-family="Arial, sans-serif" font-size="9">    created_at: TIMESTAMPTZ DEFAULT NOW()</text>

<!-- Caption -->
<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.3.5: MindEase Relational Database Physical Schema Design with Primary &amp; Foreign Keys</text>
</svg>'''

    write_files("10_Database_Schema", svg, b.to_xml())

# -------------------------------------------------------------
# 11_State_Machine_Diagram
# -------------------------------------------------------------
def build_state_machine_diagram():
    w, h = 1100, 750
    b = DrawioBuilder("11_State_Machine_Diagram", w, h)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>
  </marker>
</defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="25" y="25" width="{w-50}" height="{h-60}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="45" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">MindEase State Machine Lifecycle Diagrams</text>

<!-- REGION 1: Stress Assessment Lifecycle -->
<rect x="50" y="80" width="1000" height="260" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5" rx="6"/>
<text x="70" y="105" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#1e40af">Stress Assessment Lifecycle</text>

<!-- Initial state 1 -->
<circle cx="90" cy="190" r="12" fill="#0f172a"/>

<!-- State: Idle -->
<rect x="140" y="165" width="120" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="200" y="195" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Idle / Standby</text>

<!-- State: IngestingInputs -->
<rect x="310" y="165" width="140" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="380" y="195" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Ingesting Inputs</text>

<!-- State: FusingFeatures -->
<rect x="500" y="165" width="140" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="570" y="195" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Fusing Features</text>

<!-- State: StressClassified -->
<rect x="690" y="165" width="150" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="765" y="188" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Stress Classified</text>
<text x="765" y="204" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">[Low | Mod | High]</text>

<!-- State: XAI_Attributed -->
<rect x="880" y="165" width="130" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="945" y="195" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">XAI Attributed</text>

<!-- Final state 1 -->
<circle cx="945" cy="275" r="14" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="945" cy="275" r="9" fill="#0f172a"/>

<!-- Transitions 1 -->
<line x1="102" y1="190" x2="140" y2="190" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<line x1="260" y1="190" x2="310" y2="190" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="285" y="180" font-family="Arial, sans-serif" font-size="8" fill="#475569" text-anchor="middle">checkIn()</text>

<line x1="450" y1="190" x2="500" y2="190" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="475" y="180" font-family="Arial, sans-serif" font-size="8" fill="#475569" text-anchor="middle">inputsReady()</text>

<line x1="640" y1="190" x2="690" y2="190" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="665" y="180" font-family="Arial, sans-serif" font-size="8" fill="#475569" text-anchor="middle">classify()</text>

<line x1="840" y1="190" x2="880" y2="190" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="860" y="180" font-family="Arial, sans-serif" font-size="8" fill="#475569" text-anchor="middle">shap()</text>

<line x1="945" y1="215" x2="945" y2="261" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="975" y="240" font-family="Arial, sans-serif" font-size="8" fill="#475569">persisted()</text>

<!-- REGION 2: Appointment & Payment Lifecycle -->
<rect x="50" y="370" width="1000" height="300" fill="#f8fafc" stroke="#10b981" stroke-width="1.5" rx="6"/>
<text x="70" y="395" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#047857">Counselor Appointment &amp; Polar Payment Lifecycle</text>

<circle cx="90" cy="490" r="12" fill="#0f172a"/>

<rect x="140" y="465" width="120" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="200" y="495" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Requested</text>

<rect x="310" y="465" width="140" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="380" y="495" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Eligibility Evaluated</text>

<!-- Branching -->
<!-- Free path -->
<rect x="520" y="415" width="140" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="590" y="445" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Confirmed (Free)</text>

<!-- Paid path -->
<rect x="520" y="525" width="140" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="590" y="555" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Payment Pending</text>

<!-- Polar checkout -->
<rect x="710" y="525" width="140" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="780" y="555" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Polar Checkout</text>

<!-- Confirmed Paid -->
<rect x="710" y="415" width="140" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="780" y="445" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Confirmed (Paid)</text>

<!-- In Session & Completed -->
<rect x="890" y="465" width="120" height="50" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="10"/>
<text x="950" y="495" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Completed</text>

<circle cx="950" cy="580" r="14" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="950" cy="580" r="9" fill="#0f172a"/>

<line x1="102" y1="490" x2="140" y2="490" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<line x1="260" y1="490" x2="310" y2="490" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<line x1="450" y1="480" x2="520" y2="440" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="475" y="450" font-family="Arial, sans-serif" font-size="8" fill="#475569">[isFreeTier]</text>

<line x1="450" y1="500" x2="520" y2="540" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="475" y="530" font-family="Arial, sans-serif" font-size="8" fill="#475569">[paidSession]</text>

<line x1="660" y1="550" x2="710" y2="550" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="685" y="540" font-family="Arial, sans-serif" font-size="8" fill="#475569">redirect()</text>

<line x1="780" y1="525" x2="780" y2="465" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="790" y="500" font-family="Arial, sans-serif" font-size="8" fill="#475569">webhookSuccess()</text>

<line x1="660" y1="440" x2="890" y2="480" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<line x1="850" y1="440" x2="890" y2="480" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<line x1="950" y1="515" x2="950" y2="566" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="975" y="545" font-family="Arial, sans-serif" font-size="8" fill="#475569">notesArchived()</text>

<!-- Caption -->
<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.5.1: State Machine Transition Diagrams for Stress Assessment and Appointment Lifecycles</text>
</svg>'''

    write_files("11_State_Machine_Diagram", svg, b.to_xml())

# -------------------------------------------------------------
# Activity Diagrams (AD01 to AD05)
# -------------------------------------------------------------
def build_activity_diagrams():
    # AD01
    w, h = 950, 750
    b1 = DrawioBuilder("AD01_Multimodal_Stress_Assessment_Workflow", w, h)
    svg1 = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/></marker></defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="25" y="25" width="{w-50}" height="{h-60}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="45" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Activity Diagram: Multimodal Stress Assessment &amp; Fusion Workflow</text>

<!-- Start node -->
<circle cx="150" cy="100" r="14" fill="#0f172a"/>

<!-- Actions -->
<rect x="70" y="140" width="160" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="150" y="167" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Submit PSS Answers</text>

<rect x="70" y="220" width="160" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="150" y="247" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Log Voice/Text Diary</text>

<rect x="70" y="300" width="160" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="150" y="327" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Log Daily Habits (Sleep, Steps)</text>

<!-- Fork / Join Bar -->
<rect x="280" y="120" width="8" height="240" fill="#0f172a"/>

<line x1="150" y1="114" x2="150" y2="140" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<line x1="230" y1="162" x2="280" y2="162" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<line x1="230" y1="242" x2="280" y2="242" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<line x1="230" y1="322" x2="280" y2="322" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<!-- Synchronized Feature Matrix -->
<rect x="330" y="215" width="180" height="50" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="420" y="245" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Feature Normalization</text>

<line x1="288" y1="240" x2="330" y2="240" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<rect x="550" y="215" width="170" height="50" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="635" y="245" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Multimodal Fusion Model</text>

<line x1="510" y1="240" x2="550" y2="240" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<!-- Decision Diamond -->
<polygon points="780,240 830,215 880,240 830,265" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<line x1="720" y1="240" x2="780" y2="240" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<!-- High stress branch -->
<rect x="740" y="340" width="180" height="50" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="830" y="362" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Trigger Counselor Free Triage</text>
<text x="830" y="378" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">&amp; Emergency Crisis Help</text>

<line x1="830" y1="265" x2="830" y2="340" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="840" y="300" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">[High Stress]</text>

<!-- Low / Moderate branch -->
<rect x="740" y="100" width="180" height="50" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="830" y="122" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Generate Adaptive Recovery</text>
<text x="830" y="138" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">&amp; Balanced Study Sessions</text>

<line x1="830" y1="215" x2="830" y2="150" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="840" y="180" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">[Low / Moderate]</text>

<!-- Merge and XAI -->
<rect x="540" y="460" width="200" height="50" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="640" y="485" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Compute SHAP Feature Insights</text>

<line x1="830" y1="390" x2="830" y2="485" stroke="#0f172a" stroke-width="1.3"/>
<line x1="830" y1="485" x2="740" y2="485" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<line x1="920" y1="125" x2="940" y2="125" stroke="#0f172a" stroke-width="1.3"/>
<line x1="940" y1="125" x2="940" y2="485" stroke="#0f172a" stroke-width="1.3"/>
<line x1="940" y1="485" x2="740" y2="485" stroke="#0f172a" stroke-width="1.3"/>

<!-- Final state -->
<circle cx="640" cy="580" r="14" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="640" cy="580" r="9" fill="#0f172a"/>
<line x1="640" y1="510" x2="640" y2="566" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.6.1: Activity Diagram for Multimodal Stress Assessment &amp; Fusion Workflow</text>
</svg>'''
    write_files("AD01_Multimodal_Stress_Assessment_Workflow", svg1, b1.to_xml())

    # AD02
    w, h = 950, 750
    b2 = DrawioBuilder("AD02_Voice_Diary_Whisper_Analysis", w, h)
    svg2 = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/></marker></defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="25" y="25" width="{w-50}" height="{h-60}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="45" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Activity Diagram: Voice Diary Transcription &amp; Safety Analysis</text>

<circle cx="475" cy="90" r="14" fill="#0f172a"/>

<rect x="385" y="130" width="180" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="157" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Capture Audio Stream</text>
<line x1="475" y1="104" x2="475" y2="130" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<rect x="385" y="205" width="180" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="232" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Whisper ASR Model (STT)</text>
<line x1="475" y1="175" x2="475" y2="205" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<rect x="385" y="280" width="180" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="307" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">NLP Sentiment &amp; Keywords</text>
<line x1="475" y1="250" x2="475" y2="280" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<!-- Crisis Decision Diamond -->
<polygon points="425,370 475,345 525,370 475,395" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<line x1="475" y1="325" x2="475" y2="345" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<!-- Crisis detected path -->
<rect x="620" y="347" width="220" height="45" fill="#f8fafc" stroke="#dc2626" stroke-width="1.5" rx="8"/>
<text x="730" y="375" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">Emergency Helpline Alert &amp; Support</text>
<line x1="525" y1="370" x2="620" y2="370" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="560" y="360" font-family="Arial, sans-serif" font-size="9" fill="#dc2626">[Crisis Flagged]</text>

<!-- Normal path -->
<rect x="375" y="440" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="467" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Encrypt &amp; Store Diary Entry</text>
<line x1="475" y1="395" x2="475" y2="440" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="485" y="420" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">[Normal]</text>

<line x1="730" y1="392" x2="730" y2="462" stroke="#0f172a" stroke-width="1.3"/>
<line x1="730" y1="462" x2="575" y2="462" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<rect x="375" y="520" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="547" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Update Personal Baseline</text>
<line x1="475" y1="485" x2="475" y2="520" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<circle cx="475" cy="620" r="14" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="475" cy="620" r="9" fill="#0f172a"/>
<line x1="475" y1="565" x2="475" y2="606" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.6.2: Activity Diagram for Voice Diary Transcription, NLP Sentiment &amp; Crisis Protocol</text>
</svg>'''
    write_files("AD02_Voice_Diary_Whisper_Analysis", svg2, b2.to_xml())

    # AD03
    w, h = 950, 750
    b3 = DrawioBuilder("AD03_Adaptive_Study_Planner", w, h)
    svg3 = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/></marker></defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="25" y="25" width="{w-50}" height="{h-60}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="45" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Activity Diagram: Adaptive Study and Recovery Planner Workflow</text>

<circle cx="475" cy="90" r="14" fill="#0f172a"/>

<rect x="375" y="130" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="157" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Enter Tasks &amp; Deadlines</text>
<line x1="475" y1="104" x2="475" y2="130" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<rect x="375" y="205" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="232" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Fetch Current Stress State</text>
<line x1="475" y1="175" x2="475" y2="205" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<!-- Diamond -->
<polygon points="425,295 475,270 525,295 475,320" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<line x1="475" y1="250" x2="475" y2="270" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<!-- High stress branch -->
<rect x="180" y="340" width="220" height="50" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="290" y="362" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Generate Light Study Plan</text>
<text x="290" y="378" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">(25m focus, 15m mindfulness)</text>
<line x1="425" y1="295" x2="290" y2="295" stroke="#0f172a" stroke-width="1.3"/>
<line x1="290" y1="295" x2="290" y2="340" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="340" y="285" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">[High Stress]</text>

<!-- Normal branch -->
<rect x="550" y="340" width="220" height="50" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="660" y="362" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Generate Standard Pomodoro</text>
<text x="660" y="378" font-family="Arial, sans-serif" font-size="9" fill="#475569" text-anchor="middle">(50m study, 10m break)</text>
<line x1="525" y1="295" x2="660" y2="295" stroke="#0f172a" stroke-width="1.3"/>
<line x1="660" y1="295" x2="660" y2="340" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="590" y="285" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">[Low / Moderate]</text>

<!-- Merge -->
<polygon points="440,445 475,425 510,445 475,465" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<line x1="290" y1="390" x2="290" y2="445" stroke="#0f172a" stroke-width="1.3"/>
<line x1="290" y1="445" x2="440" y2="445" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<line x1="660" y1="390" x2="660" y2="445" stroke="#0f172a" stroke-width="1.3"/>
<line x1="660" y1="445" x2="510" y2="445" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<rect x="375" y="495" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="522" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Execute Sessions &amp; Track</text>
<line x1="475" y1="465" x2="475" y2="495" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<circle cx="475" cy="590" r="14" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="475" cy="590" r="9" fill="#0f172a"/>
<line x1="475" y1="540" x2="475" y2="576" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.6.3: Activity Diagram for Adaptive Study and Recovery Planner</text>
</svg>'''
    write_files("AD03_Adaptive_Study_Planner", svg3, b3.to_xml())

    # AD04
    w, h = 950, 750
    b4 = DrawioBuilder("AD04_Counselor_Booking_Polar_Payment", w, h)
    svg4 = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/></marker></defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="25" y="25" width="{w-50}" height="{h-60}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="45" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Activity Diagram: Counselor Booking &amp; Polar Payment Verification</text>

<circle cx="475" cy="90" r="14" fill="#0f172a"/>

<rect x="375" y="130" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="157" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Select Counselor &amp; Slot</text>
<line x1="475" y1="104" x2="475" y2="130" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<polygon points="425,225 475,200 525,225 475,250" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<line x1="475" y1="175" x2="475" y2="200" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<!-- Free branch -->
<rect x="180" y="270" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="280" y="297" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Confirm Free Triage Session</text>
<line x1="425" y1="225" x2="280" y2="225" stroke="#0f172a" stroke-width="1.3"/>
<line x1="280" y1="225" x2="280" y2="270" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="330" y="215" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">[Free Eligible]</text>

<!-- Paid branch -->
<rect x="570" y="270" width="210" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="675" y="297" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Redirect Polar Sandbox URL</text>
<line x1="525" y1="225" x2="675" y2="225" stroke="#0f172a" stroke-width="1.3"/>
<line x1="675" y1="225" x2="675" y2="270" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="590" y="215" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">[Paid Session]</text>

<rect x="570" y="350" width="210" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="675" y="377" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Execute Test Card Payment</text>
<line x1="675" y1="315" x2="675" y2="350" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<rect x="570" y="430" width="210" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="675" y="457" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Verify Polar Webhook Event</text>
<line x1="675" y1="395" x2="675" y2="430" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<!-- Merge and complete -->
<rect x="375" y="520" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="547" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Dispatch Booking Confirmation</text>

<line x1="280" y1="315" x2="280" y2="542" stroke="#0f172a" stroke-width="1.3"/>
<line x1="280" y1="542" x2="375" y2="542" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<line x1="675" y1="475" x2="675" y2="542" stroke="#0f172a" stroke-width="1.3"/>
<line x1="675" y1="542" x2="575" y2="542" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<circle cx="475" cy="620" r="14" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="475" cy="620" r="9" fill="#0f172a"/>
<line x1="475" y1="565" x2="475" y2="606" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.6.4: Activity Diagram for Counselor Booking &amp; Polar Payment Verification</text>
</svg>'''
    write_files("AD04_Counselor_Booking_Polar_Payment", svg4, b4.to_xml())

    # AD05
    w, h = 950, 750
    b5 = DrawioBuilder("AD05_Community_Post_Moderation", w, h)
    svg5 = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/></marker></defs>
<rect width="{w}" height="{h}" fill="#ffffff"/>
<rect x="25" y="25" width="{w-50}" height="{h-60}" fill="none" stroke="#1e293b" stroke-width="1.5"/>
<text x="45" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">Activity Diagram: Peer Community Post Creation &amp; Moderation</text>

<circle cx="475" cy="90" r="14" fill="#0f172a"/>

<rect x="375" y="130" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="157" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Compose Peer Message</text>
<line x1="475" y1="104" x2="475" y2="130" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<rect x="375" y="205" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="232" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Automated Toxicity Filter</text>
<line x1="475" y1="175" x2="475" y2="205" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<polygon points="425,295 475,270 525,295 475,320" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>
<line x1="475" y1="250" x2="475" y2="270" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<!-- Rejected -->
<rect x="650" y="272" width="180" height="45" fill="#f8fafc" stroke="#dc2626" stroke-width="1.5" rx="8"/>
<text x="740" y="300" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">Reject &amp; Warn Author</text>
<line x1="525" y1="295" x2="650" y2="295" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="580" y="285" font-family="Arial, sans-serif" font-size="9" fill="#dc2626">[Toxic]</text>

<!-- Approved -->
<rect x="375" y="360" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="387" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Publish to Community Feed</text>
<line x1="475" y1="320" x2="475" y2="360" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>
<text x="485" y="345" font-family="Arial, sans-serif" font-size="9" fill="#0f172a">[Clean]</text>

<rect x="375" y="440" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="467" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">User Peer Reporting Loop</text>
<line x1="475" y1="405" x2="475" y2="440" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<rect x="375" y="520" width="200" height="45" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5" rx="8"/>
<text x="475" y="547" font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Admin Review &amp; Resolution</text>
<line x1="475" y1="485" x2="475" y2="520" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<circle cx="475" cy="620" r="14" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="475" cy="620" r="9" fill="#0f172a"/>
<line x1="475" y1="565" x2="475" y2="606" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<line x1="740" y1="317" x2="740" y2="620" stroke="#0f172a" stroke-width="1.3"/>
<line x1="740" y1="620" x2="489" y2="620" stroke="#0f172a" stroke-width="1.3" marker-end="url(#arrow)"/>

<text x="{w/2}" y="{h-15}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 5.6.5: Activity Diagram for Peer Community Post Creation &amp; Moderation Workflow</text>
</svg>'''
    write_files("AD05_Community_Post_Moderation", svg5, b5.to_xml())

def generate_all_system_diagrams():
    print("Generating System Architecture, DFD, Component, Deployment, Class, ERD, Schema, State, and Activity Diagrams...")
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
    build_activity_diagrams()
    print("All system diagrams generated successfully!")

if __name__ == "__main__":
    generate_all_system_diagrams()
