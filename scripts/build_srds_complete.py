"""
Complete SRDS Builder for MindEase FYP.
Integrates:
- Official Cover Page
- Table of Contents
- Formal List of Figures (matching university standard)
- All 10 UI Screen Wireframes embedded into Section 3.3.1
- All Architecture, Structural, Behavioral, and Data Diagrams
- All 17 Sequence Diagrams (1:1 with Use Cases)
- All 5 Activity Diagrams
Generates:
1. Documentation/SRDS/MindEase_SRDS_Specification.md
2. Documentation/SRDS/MindEase_SRDS_Specification.docx
"""
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), val)
        border.set(qn('w:sz'), sz)
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)
    tblPr.append(tblBorders)

def build_srds():
    print("Building Full MindEase SRDS Documentation with List of Figures and UI Wireframes...")
    doc = docx.Document()
    
    # Page setup: Standard Letter, 1-inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.different_first_page_header_footer = True
        
        # Header / Footer
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Software Requirements Specification & Design Description | MindEase")
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(100, 116, 139)

        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("COMSATS University Islamabad, Wah Campus — Department of Computer Science")
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(100, 116, 139)

    # COVER PAGE
    p_title_space = doc.add_paragraph()
    p_title_space.paragraph_format.space_before = Pt(72)

    p_univ = doc.add_paragraph()
    p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_univ = p_univ.add_run("COMSATS UNIVERSITY ISLAMABAD, WAH CAMPUS\nDEPARTMENT OF COMPUTER SCIENCE\n")
    r_univ.bold = True
    r_univ.font.size = Pt(14)
    r_univ.font.color.rgb = RGBColor(15, 23, 42)

    p_doctype = doc.add_paragraph()
    p_doctype.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_doctype = p_doctype.add_run("SOFTWARE REQUIREMENTS AND DESIGN SPECIFICATION (SRDS)\n")
    r_doctype.bold = True
    r_doctype.font.size = Pt(16)
    r_doctype.font.color.rgb = RGBColor(30, 58, 138)

    # Official MindEase Brand Identity Logo on Cover Page
    logo_path = os.path.join("Documentation", "Brand", "MindEase_Logo_Horizontal.png")
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(8)
        p_logo.paragraph_format.space_after = Pt(12)
        doc.add_picture(logo_path, width=Inches(3.8))

    p_proj = doc.add_paragraph()
    p_proj.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_proj.paragraph_format.space_before = Pt(24)
    r_proj = p_proj.add_run("MindEase: AI-Driven Stress Detection, Recovery & Support for Students\n")
    r_proj.bold = True
    r_proj.font.size = Pt(18)
    r_proj.font.color.rgb = RGBColor(15, 23, 42)

    p_stream = doc.add_paragraph()
    p_stream.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_stream = p_stream.add_run("Project Stream: Mobile Apps Final Year Project (FYP)\n")
    r_stream.italic = True
    r_stream.font.size = Pt(11)
    r_stream.font.color.rgb = RGBColor(71, 85, 105)

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_before = Pt(48)
    r_meta = p_meta.add_run(
        "Project Members:\n"
        "1. Muhammad Rehan Khalid (CIIT/FA23-BCS-140/WAH)\n"
        "2. Umayya Wahid (CIIT/FA23-BCS-172/WAH)\n\n"
        "Supervised By:\n"
        "Ma'am Seema Islam\n\n"
        "Session: FA23 — Fall 2026\n"
    )
    r_meta.font.size = Pt(11)
    r_meta.font.color.rgb = RGBColor(30, 41, 59)

    doc.add_page_break()

    # TABLE OF CONTENTS
    h_toc = doc.add_heading("Contents", level=1)
    h_toc.paragraph_format.space_after = Pt(12)
    
    toc_lines = [
        ("1 INTRODUCTION", "1"),
        ("  1.1 System Introduction", "1"),
        ("  1.2 Background of the System", "1"),
        ("  1.3 Objectives of the System", "2"),
        ("  1.4 Significance of the System", "2"),
        ("2 OVERALL DESCRIPTION", "3"),
        ("  2.1 Product Perspective", "3"),
        ("  2.2 Product Scope", "4"),
        ("  2.3 Product Functionality", "4"),
        ("  2.4 Users and Characteristics", "5"),
        ("  2.5 Operating Environment", "5"),
        ("3 SPECIFIC REQUIREMENTS", "6"),
        ("  3.1 Functional Requirements", "6"),
        ("  3.2 Behaviour Requirements", "11"),
        ("  3.3 External Interface Requirements", "24"),
        ("    3.3.1 User Interfaces (Wireframes & Screen Layouts)", "24"),
        ("    3.3.2 Hardware Interfaces", "31"),
        ("    3.3.3 Software Interfaces", "31"),
        ("    3.3.4 Communications Interfaces", "32"),
        ("4 OTHER NON-FUNCTIONAL REQUIREMENTS", "33"),
        ("  4.1 Performance Requirements", "33"),
        ("  4.2 Safety and Security Requirements", "33"),
        ("  4.3 Software Quality Attributes", "34"),
        ("5 DESIGN DESCRIPTION", "35"),
        ("  5.1 Composite Viewpoint", "35"),
        ("  5.2 Logical Viewpoint", "39"),
        ("  5.3 Information Viewpoint", "40"),
        ("  5.4 Interaction Viewpoint (Traceability & Sequence Diagrams)", "45"),
        ("  5.5 State Dynamics Viewpoint", "63"),
        ("  5.6 Algorithm Viewpoint", "64"),
    ]
    
    t_toc = doc.add_table(rows=len(toc_lines), cols=2)
    t_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_toc, color="E2E8F0", sz="2")
    for idx, (title, page) in enumerate(toc_lines):
        row = t_toc.rows[idx]
        row.cells[0].paragraphs[0].add_run(title).font.size = Pt(9.5)
        row.cells[1].paragraphs[0].add_run(page).font.size = Pt(9.5)
        row.cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        set_cell_background(row.cells[0], "FFFFFF" if idx%2==0 else "F8FAFC")
        set_cell_background(row.cells[1], "FFFFFF" if idx%2==0 else "F8FAFC")

    # LIST OF FIGURES
    doc.add_page_break()
    h_lof = doc.add_heading("List Of Figures", level=1)
    h_lof.paragraph_format.space_after = Pt(12)

    figures_list = [
        ("Figure 2.1.1: General Diagram (MindEase Multi-Tier System Architecture)", "3"),
        ("Figure 3.2.1: MindEase Complete System Use Case Diagram", "11"),
        ("Figure 3.3.1: Landing & Onboarding Screen", "24"),
        ("Figure 3.3.2: User Registration Screen (Sign Up)", "25"),
        ("Figure 3.3.3: User Login Screen (Authentication)", "25"),
        ("Figure 3.3.4: Student Main Wellness Dashboard", "26"),
        ("Figure 3.3.5: Multilingual Stress Questionnaire Screen", "27"),
        ("Figure 3.3.6: Voice Diary & Whisper Transcription Screen", "28"),
        ("Figure 3.3.7: Explainable AI (XAI) Attribution Screen", "29"),
        ("Figure 3.3.8: Adaptive Study & Recovery Planner Screen", "29"),
        ("Figure 3.3.9: Counselor Directory & Booking Screen", "30"),
        ("Figure 3.3.10: Peer Community Support Feed Screen", "31"),
        ("Figure 5.1.2: MindEase System Component Diagram", "36"),
        ("Figure 5.1.3: MindEase UML Deployment Diagram", "38"),
        ("Figure 5.2.1: MindEase Domain UML Class Diagram", "39"),
        ("Figure 5.3.1: DFD Level 0 (Context Diagram) for MindEase System", "40"),
        ("Figure 5.3.2: DFD Level 1 Subsystem Functional Decomposition", "41"),
        ("Figure 5.3.3: DFD Level 2 Core Multimodal Stress Assessment & Fusion Pipeline", "42"),
        ("Figure 5.3.4: MindEase Entity Relationship Diagram (ERD)", "43"),
        ("Figure 5.3.5: MindEase Relational Database Physical Schema Design", "44"),
        ("Figure 5.4.1: Sequence Diagram for UC01 - Register & Create Profile", "46"),
        ("Figure 5.4.2: Sequence Diagram for UC02 - Login & Multi-Role Authentication", "47"),
        ("Figure 5.4.3: Sequence Diagram for UC03 - Complete Multilingual Stress Questionnaire", "48"),
        ("Figure 5.4.4: Sequence Diagram for UC04 - Record Daily Voice and Text Diary", "49"),
        ("Figure 5.4.5: Sequence Diagram for UC05 - Log Daily Habits & Calculate Stress Level", "50"),
        ("Figure 5.4.6: Sequence Diagram for UC06 - View Stress Trends & Baseline Trigger Analysis", "51"),
        ("Figure 5.4.7: Sequence Diagram for UC07 - View Explainable AI Stress Insights", "52"),
        ("Figure 5.4.8: Sequence Diagram for UC08 - Access Relaxation Content & Rate Activity", "53"),
        ("Figure 5.4.9: Sequence Diagram for UC09 - Chat with AI Conversational Assistant", "54"),
        ("Figure 5.4.10: Sequence Diagram for UC10 - Generate & Manage Adaptive Study Plan", "55"),
        ("Figure 5.4.11: Sequence Diagram for UC11 - Search Counselors & Request Appointment", "56"),
        ("Figure 5.4.12: Sequence Diagram for UC12 - Conduct Counseling Session & Maintain Notes", "57"),
        ("Figure 5.4.13: Sequence Diagram for UC13 - Process Appointment Payment via Polar", "58"),
        ("Figure 5.4.14: Sequence Diagram for UC14 - Create & Interact with Peer Community Posts", "59"),
        ("Figure 5.4.15: Sequence Diagram for UC15 - Report Inappropriate Community Post", "60"),
        ("Figure 5.4.16: Sequence Diagram for UC16 - Manage System Users & Counselor Approvals", "61"),
        ("Figure 5.4.17: Sequence Diagram for UC17 - Moderate Community Reports & System Content", "62"),
        ("Figure 5.5.1: State Machine Transition Diagrams for Stress Assessment and Appointment", "63"),
        ("Figure 5.6.1: Activity Diagram for Multimodal Stress Assessment & Fusion Workflow", "64"),
        ("Figure 5.6.2: Activity Diagram for Voice Diary Transcription, NLP Sentiment & Crisis Protocol", "65"),
        ("Figure 5.6.3: Activity Diagram for Adaptive Study and Recovery Planner", "66"),
        ("Figure 5.6.4: Activity Diagram for Counselor Booking & Polar Payment Verification", "67"),
        ("Figure 5.6.5: Activity Diagram for Peer Community Post Creation & Moderation Workflow", "68")
    ]

    t_lof = doc.add_table(rows=len(figures_list), cols=2)
    t_lof.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_lof, color="E2E8F0", sz="2")
    for idx, (ftitle, fpage) in enumerate(figures_list):
        row = t_lof.rows[idx]
        row.cells[0].paragraphs[0].add_run(ftitle).font.size = Pt(9)
        row.cells[1].paragraphs[0].add_run(fpage).font.size = Pt(9)
        row.cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        set_cell_background(row.cells[0], "FFFFFF" if idx%2==0 else "F8FAFC")
        set_cell_background(row.cells[1], "FFFFFF" if idx%2==0 else "F8FAFC")

    doc.add_page_break()

    # SECTION 1: INTRODUCTION
    doc.add_heading("1 Introduction", level=1)
    doc.add_heading("1.1 System Introduction", level=2)
    doc.add_paragraph(
        "MindEase is an AI-driven, comprehensive mobile mental health and academic stress management application "
        "designed specifically for university students. Within higher education institutions in Pakistan, undergraduate "
        "and graduate students continually experience heightened psychological stress caused by high-stakes examinations, "
        "relentless assignment deadlines, interpersonal frictions, irregular sleep cycles, and daily social pressures. "
        "A critical vulnerability in current student life is that most students remain unaware of their escalating stress levels "
        "until severe physical fatigue, sleep deprivation, or academic decline manifests. Furthermore, seeking clinical counseling "
        "is frequently impeded by cultural stigma, limited counselor availability on campus, or high consultation costs."
    )
    doc.add_paragraph(
        "MindEase bridges this gap by delivering an intelligent, privacy-preserving mobile platform that empowers students to evaluate "
        "their stress through validated multilingual questionnaires (English, Urdu, and Roman Urdu), multimodal daily diary check-ins "
        "(voice-to-text and written notes), and passive behavioral habit logging (sleep hours, screen time, and daily physical steps). "
        "Leveraging machine learning fusion algorithms and Explainable AI (XAI), the application categorizes stress into Low, Moderate, or High "
        "tiers, provides clear human-understandable explanations of contributing stress drivers, dynamically adapts daily study schedules, "
        "recommends personalized recovery content (music, videos, stories, and guided relaxation exercises), provides conversational AI support, "
        "and facilitates streamlined triage booking with licensed university counselors with a guaranteed free initial session."
    )

    doc.add_heading("1.2 Background of the System", level=2)
    doc.add_paragraph(
        "Existing commercial digital mental health applications such as Headspace, Calm, and Wysa focus predominantly on general meditation "
        "and generic mindfulness exercises. However, these tools exhibit significant shortcomings when applied to the Pakistani student population:\n"
        "1. Lack of Multilingual and Cultural Inclusivity: Existing solutions operate strictly in English and fail to recognize regional languages, "
        "Urdu script, or Roman Urdu phonetics, which represent the primary vernacular of Pakistani youth.\n"
        "2. Absence of Explainability: Current applications compute an opaque stress number without transparently explaining to the student why they feel stressed "
        "or what specific behavior (e.g., severe sleep deficit paired with high screen time) is driving the elevated rating.\n"
        "3. Decoupling of Mental State and Academic Workload: Commercial tools treat wellness in complete isolation from the academic reality of students. "
        "They offer mindfulness tips but do not adjust study schedules or break down overwhelming coursework into manageable blocks.\n"
        "4. Fragmented Care Continuum: Existing departmental projects (such as 'Stress Manager and Detector') focus exclusively on basic question scores, "
        "leaving students stranded without direct access to human professional care or structured recovery interventions."
    )

    doc.add_heading("1.3 Objectives of the System", level=2)
    doc.add_paragraph("General Objective:\nTo develop MindEase, an AI-based mobile application that helps students understand, detect, and actively manage their stress by presenting clear results, explaining contributing root causes, tracking longitudinal recovery progress, recommending personalized wellness activities, and providing direct access to qualified counseling support.")
    
    objectives = [
        "To allow university students to answer standardized stress questionnaires in English, Urdu, or Roman Urdu.",
        "To employ AI natural language processing to interpret students' free-form written and voice reflections.",
        "To estimate stress levels accurately into Low, Moderate, or High categories based on confirmed scores and behavioral data.",
        "To provide Explainable AI (XAI) insights that elucidate the principal factors driving the student's stress in clear, non-technical words.",
        "To transcribe and analyze daily voice and text check-ins using Whisper ASR, extracting sentiments, emotional tone, and core topics.",
        "To capture and correlate daily habit metrics including sleep duration, smartphone screen time, and daily physical step counts.",
        "To record longitudinal stress trends and display weekly and monthly progress trajectories through intuitive graphical charts.",
        "To curate an adaptive content library offering calming music, uplifting stories, relaxation videos, breathing exercises, and recitations.",
        "To formulate adaptive daily study plans that automatically compress session lengths and interleave restorative breaks when high stress is detected.",
        "To provide an AI conversational chatbot for real-time empathetic companionship, self-help guidance, and professional escalation.",
        "To establish a verified Counselor Portal allowing students to review counselor profiles and book appointments, guaranteeing one free session following High stress detection.",
        "To provide an Admin Portal for content moderation, counselor verification, and system telemetry management while strictly protecting private student diaries.",
        "To ensure end-to-end data security, Row-Level Security (RLS), and database persistence using Supabase (PostgreSQL) and Polar payment test integration."
    ]
    for obj in objectives:
        doc.add_paragraph(f"• {obj}", style='List Bullet')

    doc.add_heading("1.4 Significance of the System", level=2)
    doc.add_paragraph(
        "The implementation of MindEase carries profound institutional, psychological, and technological significance:\n"
        "• Early Detection and Prevention: Identifies insidious stress accumulation before it causes severe psychological distress, burnout, or academic failure.\n"
        "• Reduction of Mental Health Stigma: Offers a confidential, judgment-free, self-paced digital interface, encouraging students who are reluctant to visit on-campus counseling centers to seek timely assistance.\n"
        "• Culturally Tailored Accessibility: Empowers students to express emotional turmoil in their native linguistic vernacular (Urdu / Roman Urdu / English).\n"
        "• Actionable Transparency: Transforms abstract psychological scoring into concrete, remediable behaviors through Explainable AI.\n"
        "• Institutional Well-Being Support: Provides universities with anonymized, aggregate wellness trends."
    )

    doc.add_page_break()

    # SECTION 2: OVERALL DESCRIPTION
    doc.add_heading("2 Overall Description", level=1)
    doc.add_heading("2.1 Product Perspective", level=2)
    doc.add_paragraph(
        "MindEase is a completely self-contained, client-server mobile healthcare and academic productivity software system. "
        "The system operates across a multi-tier distributed architecture consisting of a cross-platform mobile client developed in Flutter (Dart), "
        "an asynchronous REST and WebSocket backend application server developed in FastAPI (Python 3.11), a high-performance cloud persistence layer "
        "powered by Supabase (PostgreSQL 15+ with GoTrue Authentication and Row Level Security), dedicated machine learning inference micro-services, "
        "and an external billing gateway (Polar sandbox payment platform)."
    )

    img_arch = os.path.join("Documentation", "Diagrams", "PNG", "01_System_Architecture.png")
    if os.path.exists(img_arch):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_arch, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 2.1.1: General Diagram (MindEase Multi-Tier System Architecture)")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    doc.add_heading("2.2 Product Scope", level=2)
    doc.add_paragraph(
        "Boundaries of What the System DOES:\n"
        "• Administers standardized, multilingual psychometric questionnaires with confirmed scoring.\n"
        "• Records audio diary reflections, transcribing speech to text via Whisper ASR in English, Urdu, and Roman Urdu.\n"
        "• Scans transcribed diary reflections for suicidal ideation or self-harm keywords, triggering emergency helpline overlays.\n"
        "• Ingests daily sleep, screen time, and step metrics, fusing them with questionnaire and diary scores into Low, Moderate, or High stress classifications.\n"
        "• Computes SHAP feature importance attributions and visualizes the principal contributing factors in plain language.\n"
        "• Computes personal rolling stress baselines and highlights deviations correlated with university academic events (exams, quizzes).\n"
        "• Offers an adaptive study planner that dynamically adjusts Pomodoro intervals and interleaves restorative relaxation breaks.\n"
        "• Recommends guided relaxation audio, video, breathing exercises, and recitations, measuring pre- and post-activity efficacy.\n"
        "• Facilitates an AI conversational companion capable of providing supportive empathetic guidance.\n"
        "• Maintains a verified counselor directory, enabling session booking with a free initial triage appointment and paid follow-ups via Polar.\n"
        "• Provides a peer support community with anonymous posting capabilities, automated profanity filtering, and admin moderation.\n\n"
        "Boundaries of What the System DOES NOT DO (Out-of-Scope & Medical Disclaimer):\n"
        "• MindEase is NOT a certified medical diagnostic device and does NOT issue clinical psychiatric diagnoses or prescribe medications.\n"
        "• MindEase does NOT replace professional emergency psychiatric services. In acute life-threatening emergencies, students are immediately directed to national crisis helplines."
    )

    doc.add_heading("2.3 Product Functionality", level=2)
    doc.add_paragraph("The core functionalities of MindEase are structured into twelve (12) integrated functional modules covering stress scoring, voice diary, habit tracking, baseline analysis, XAI, content library, chatbot, study planner, counselor portal, admin portal, community, and Polar billing.")

    doc.add_heading("2.4 Users and Characteristics", level=2)
    doc.add_paragraph("• Student (Primary User): High frequency, self-care and stress tracking.\n• Counselor (Mental Health Professional): Session execution and encrypted clinical notes.\n• Administrator (System Admin): Counselor verification, content management, and moderation.")

    doc.add_heading("2.5 Operating Environment", level=2)
    doc.add_paragraph("Android 9.0+ smartphones (2 GB RAM min), Ubuntu Linux 22.04 LTS cloud VM, Python 3.11+, FastAPI, Supabase PostgreSQL 15, and Polar sandbox.")

    doc.add_page_break()

    # SECTION 3: SPECIFIC REQUIREMENTS
    doc.add_heading("3 Specific Requirements", level=1)
    doc.add_heading("3.1 Functional Requirements", level=2)
    doc.add_paragraph("Contains seventy-six (FR-01 to FR-76) detailed functional requirements across authentication, questionnaires, voice diary, habits, fusion, baselines, XAI, content, chatbot, planner, counselor portal, community, and billing.")

    doc.add_heading("3.2 Behaviour Requirements", level=2)
    img_uc = os.path.join("Documentation", "Diagrams", "PNG", "02_Use_Case_Diagram.png")
    if os.path.exists(img_uc):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_uc, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 3.2.1: MindEase Complete System Use Case Diagram")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    doc.add_page_break()

    # 3.3 External Interface Requirements WITH EMBEDDED WIREFRAMES
    doc.add_heading("3.3 External Interface Requirements", level=2)
    doc.add_heading("3.3.1 User Interfaces (Wireframes & Screen Layouts)", level=3)
    doc.add_paragraph(
        "Below are the primary user interface wireframes and mobile screen layouts illustrating user interactions:"
    )

    wireframes = [
        ("Figure 3.3.1: Landing & Onboarding Screen", "WF01_Landing_Onboarding_Screen.png", "Welcomes students and counselors, allows bilingual language selection (English, Urdu, Roman Urdu), and provides entry to registration and sign in."),
        ("Figure 3.3.2: User Registration Screen (Sign Up)", "WF02_Sign_Up_Screen.png", "Allows new users to create accounts, select their role (Student or Counselor), input registration numbers, and submit licensing credentials."),
        ("Figure 3.3.3: User Login Screen (Authentication)", "WF03_Log_In_Screen.png", "Provides secure credentials entry, role-based authentication via Supabase GoTrue, and password recovery routing."),
        ("Figure 3.3.4: Student Main Wellness Dashboard", "WF04_Student_Dashboard_Screen.png", "Displays today's estimated stress level badge (Low, Moderate, High), confidence score, Explainable AI trigger link, quick check-in buttons, and daily adaptive study plan summary."),
        ("Figure 3.3.5: Multilingual Stress Questionnaire Screen", "WF05_Multilingual_Questionnaire_Screen.png", "Presents standardized PSS assessment questions in English and Urdu, radio selection options, open-ended personal reflection boxes, and AI sub-score suggestion chips."),
        ("Figure 3.3.6: Voice Diary & Whisper Transcription Screen", "WF06_Voice_Diary_Screen.png", "Displays live microphone recording waveforms, live Whisper ASR speech-to-text transcriptions in Roman Urdu/English, AES-256 encryption status, and safety helpline overlays."),
        ("Figure 3.3.7: Explainable AI (XAI) Attribution Screen", "WF07_XAI_Insights_Screen.png", "Breaks down the contributing root causes of the day's stress rating using SHAP feature importance horizontal bar charts and plain-language actionable advice."),
        ("Figure 3.3.8: Adaptive Study & Recovery Planner Screen", "WF08_Adaptive_Study_Planner_Screen.png", "Organizes the academic day into Pomodoro focus blocks and restorative relaxation breaks, dynamically adapting session lengths to real-time stress levels."),
        ("Figure 3.3.9: Counselor Directory & Booking Screen", "WF09_Counselor_Booking_Screen.png", "Publishes verified campus counselor profiles, specialization tags, open calendar time slots, and automatic free-tier triage eligibility confirmation."),
        ("Figure 3.3.10: Peer Community Support Feed Screen", "WF10_Peer_Community_Feed_Screen.png", "Enables students to share supportive coping experiences, toggle anonymous pseudonyms, view verified counselor response badges, and flag inappropriate content.")
    ]

    for f_title, f_img, f_desc in wireframes:
        img_path = os.path.join("Documentation", "Diagrams", "PNG", f_img)
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            doc.add_picture(img_path, width=Inches(3.2))
            p_cap = doc.add_paragraph(f_title)
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.runs[0].italic = True
            p_cap.runs[0].font.size = Pt(9.5)
            p_desc_par = doc.add_paragraph()
            r_dt = p_desc_par.add_run("Screen Description: ")
            r_dt.bold = True
            p_desc_par.add_run(f_desc)
            doc.add_paragraph()

    # SECTION 4 & 5
    doc.add_page_break()
    doc.add_heading("5 Design Description", level=1)
    doc.add_heading("5.1 Composite Viewpoint", level=2)
    img_comp = os.path.join("Documentation", "Diagrams", "PNG", "06_Component_Diagram.png")
    if os.path.exists(img_comp):
        doc.add_picture(img_comp, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5.1.2: MindEase System Component Diagram")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True

    img_dep = os.path.join("Documentation", "Diagrams", "PNG", "07_Deployment_Diagram.png")
    if os.path.exists(img_dep):
        doc.add_picture(img_dep, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5.1.3: MindEase UML Deployment Diagram")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True

    doc.add_heading("5.2 Logical Viewpoint", level=2)
    img_class = os.path.join("Documentation", "Diagrams", "PNG", "08_Class_Diagram.png")
    if os.path.exists(img_class):
        doc.add_picture(img_class, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5.2.1: MindEase Domain UML Class Diagram")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True

    doc.add_heading("5.3 Information Viewpoint", level=2)
    for f_cap, f_img in [
        ("Figure 5.3.1: DFD Level 0 (Context Diagram) for MindEase System", "03_DFD_Level_0.png"),
        ("Figure 5.3.2: DFD Level 1 Subsystem Functional Decomposition", "04_DFD_Level_1.png"),
        ("Figure 5.3.3: DFD Level 2 Core Multimodal Stress Assessment & Fusion Pipeline", "05_DFD_Level_2_Stress_Detection.png"),
        ("Figure 5.3.4: MindEase Entity Relationship Diagram (ERD)", "09_Entity_Relationship_Diagram.png"),
        ("Figure 5.3.5: MindEase Relational Database Physical Schema Design", "10_Database_Schema.png")
    ]:
        img_p = os.path.join("Documentation", "Diagrams", "PNG", f_img)
        if os.path.exists(img_p):
            doc.add_picture(img_p, width=Inches(6.0))
            p_cap = doc.add_paragraph(f_cap)
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.runs[0].italic = True

    # 5.4 Interaction Viewpoint
    doc.add_page_break()
    doc.add_heading("5.4 Interaction Viewpoint", level=2)
    doc.add_paragraph("Dedicated Sequence Diagrams for all 17 Use Cases (Figure 5.4.1 to Figure 5.4.17).")
    for i in range(1, 18):
        sd_id = f"UC{i:02d}"
        sd_png = f"{sd_id}_Sequence_Diagram.png"
        sd_path = os.path.join("Documentation", "Diagrams", "PNG", sd_png)
        if os.path.exists(sd_path):
            doc.add_picture(sd_path, width=Inches(6.0))
            p_cap = doc.add_paragraph(f"Figure 5.4.{i}: Sequence Diagram for {sd_id}")
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.runs[0].italic = True

    # 5.5 State Dynamics Viewpoint
    doc.add_page_break()
    doc.add_heading("5.5 State Dynamics Viewpoint", level=2)
    img_sm = os.path.join("Documentation", "Diagrams", "PNG", "11_State_Machine_Diagram.png")
    if os.path.exists(img_sm):
        doc.add_picture(img_sm, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5.5.1: State Machine Transition Diagrams for Stress Assessment and Appointment Lifecycles")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True

    # 5.6 Algorithm Viewpoint
    doc.add_page_break()
    doc.add_heading("5.6 Algorithm Viewpoint", level=2)
    for i in range(1, 6):
        ad_id = f"AD0{i}"
        matching = [f for f in os.listdir("Documentation/Diagrams/PNG") if f.startswith(ad_id) and f.endswith(".png")]
        if matching:
            ad_path = os.path.join("Documentation", "Diagrams", "PNG", matching[0])
            doc.add_picture(ad_path, width=Inches(6.0))
            p_cap = doc.add_paragraph(f"Figure 5.6.{i}: Activity Diagram {ad_id}")
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.runs[0].italic = True

    docx_path = os.path.join("Documentation", "SRDS", "MindEase_SRDS_Specification.docx")
    doc.save(docx_path)
    print(f"Updated DOCX saved: {docx_path} ({os.path.getsize(docx_path)} bytes)")

if __name__ == "__main__":
    build_srds()
