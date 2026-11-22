"""
Comprehensive SRDS Builder for MindEase FYP.
Generates:
1. Documentation/SRDS/MindEase_SRDS_Specification.md
2. Documentation/SRDS/MindEase_SRDS_Specification.docx
"""
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
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

def add_callout(doc, text, title="NOTE"):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.4)
    p.paragraph_format.right_indent = Inches(0.4)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    run_t = p.add_run(f"[{title}] ")
    run_t.bold = True
    run_t.font.color.rgb = RGBColor(30, 58, 138)
    run = p.add_run(text)
    run.italic = True
    run.font.color.rgb = RGBColor(71, 85, 105)

def build_srds():
    print("Building Full MindEase SRDS Documentation...")
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

    # -------------------------------------------------------------
    # COVER PAGE
    # -------------------------------------------------------------
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

    # -------------------------------------------------------------
    # TABLE OF CONTENTS
    # -------------------------------------------------------------
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
        ("4 OTHER NON-FUNCTIONAL REQUIREMENTS", "26"),
        ("  4.1 Performance Requirements", "26"),
        ("  4.2 Safety and Security Requirements", "26"),
        ("  4.3 Software Quality Attributes", "27"),
        ("5 DESIGN DESCRIPTION", "28"),
        ("  5.1 Composite Viewpoint", "28"),
        ("  5.2 Logical Viewpoint", "32"),
        ("  5.3 Information Viewpoint", "33"),
        ("  5.4 Interaction Viewpoint (Traceability & Sequence Diagrams)", "38"),
        ("  5.5 State Dynamics Viewpoint", "56"),
        ("  5.6 Algorithm Viewpoint", "57"),
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

    doc.add_page_break()

    print("Writing Section 1: Introduction...")
    # -------------------------------------------------------------
    # 1 INTRODUCTION
    # -------------------------------------------------------------
    doc.add_heading("1 Introduction", level=1)
    
    doc.add_heading("1.1 System Introduction", level=2)
    p = doc.add_paragraph(
        "MindEase is an AI-driven, comprehensive mobile mental health and academic stress management application "
        "designed specifically for university students. Within higher education institutions in Pakistan, undergraduate "
        "and graduate students continually experience heightened psychological stress caused by high-stakes examinations, "
        "relentless assignment deadlines, interpersonal frictions, irregular sleep cycles, and daily social pressures. "
        "A critical vulnerability in current student life is that most students remain unaware of their escalating stress levels "
        "until severe physical fatigue, sleep deprivation, or academic decline manifests. Furthermore, seeking clinical counseling "
        "is frequently impeded by cultural stigma, limited counselor availability on campus, or high consultation costs."
    )
    p = doc.add_paragraph(
        "MindEase bridges this gap by delivering an intelligent, privacy-preserving mobile platform that empowers students to evaluate "
        "their stress through validated multilingual questionnaires (English, Urdu, and Roman Urdu), multimodal daily diary check-ins "
        "(voice-to-text and written notes), and passive behavioral habit logging (sleep hours, screen time, and daily physical steps). "
        "Leveraging machine learning fusion algorithms and Explainable AI (XAI), the application categorizes stress into Low, Moderate, or High "
        "tiers, provides clear human-understandable explanations of contributing stress drivers, dynamically adapts daily study schedules, "
        "recommends personalized recovery content (music, videos, stories, and guided relaxation exercises), provides conversational AI support, "
        "and facilitates streamlined triage booking with licensed university counselors with a guaranteed free initial session."
    )

    doc.add_heading("1.2 Background of the System", level=2)
    p = doc.add_paragraph(
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
    p = doc.add_paragraph(
        "MindEase directly solves these limitations by uniting multilingual NLP (Whisper ASR and Hugging Face text models), multimodal feature fusion, "
        "Explainable AI (SHAP attributions), adaptive Pomodoro study planning, a supportive peer community, and integrated counselor appointment booking "
        "backed by Polar payment verification—all hosted within an enterprise-grade Supabase PostgreSQL security architecture."
    )

    doc.add_heading("1.3 Objectives of the System", level=2)
    p = doc.add_paragraph("General Objective:\nTo develop MindEase, an AI-based mobile application that helps students understand, detect, and actively manage their stress by presenting clear results, explaining contributing root causes, tracking longitudinal recovery progress, recommending personalized wellness activities, and providing direct access to qualified counseling support.")
    
    p = doc.add_paragraph("Specific Objectives:")
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
    p = doc.add_paragraph(
        "The implementation of MindEase carries profound institutional, psychological, and technological significance:\n"
        "• Early Detection and Prevention: Identifies insidious stress accumulation before it causes severe psychological distress, burnout, or academic failure.\n"
        "• Reduction of Mental Health Stigma: Offers a confidential, judgment-free, self-paced digital interface, encouraging students who are reluctant to visit on-campus counseling centers to seek timely assistance.\n"
        "• Culturally Tailored Accessibility: Empowers students to express emotional turmoil in their native linguistic vernacular (Urdu / Roman Urdu / English).\n"
        "• Actionable Transparency: Transforms abstract psychological scoring into concrete, remediable behaviors through Explainable AI (e.g., highlighting that 4 hours of sleep and 6 hours of screen time were the primary contributors to today's High stress).\n"
        "• Institutional Well-Being Support: Provides universities with anonymized, aggregate wellness trends that aid academic administrations in scheduling exams, workload distributions, and mental health awareness campaigns."
    )

    doc.add_page_break()

    print("Writing Section 2: Overall Description...")
    # -------------------------------------------------------------
    # 2 OVERALL DESCRIPTION
    # -------------------------------------------------------------
    doc.add_heading("2 Overall Description", level=1)

    doc.add_heading("2.1 Product Perspective", level=2)
    p = doc.add_paragraph(
        "MindEase is a completely self-contained, client-server mobile healthcare and academic productivity software system. "
        "The system operates across a multi-tier distributed architecture consisting of a cross-platform mobile client developed in Flutter (Dart), "
        "an asynchronous REST and WebSocket backend application server developed in FastAPI (Python 3.11), a high-performance cloud persistence layer "
        "powered by Supabase (PostgreSQL 15+ with GoTrue Authentication and Row Level Security), dedicated machine learning inference micro-services "
        "(Whisper ASR, Scikit-learn/PyTorch multimodal classifier, SHAP explainer, and Hugging Face transformer models), and an external billing gateway "
        "(Polar sandbox payment platform)."
    )

    # Insert Architecture Diagram
    img_arch = os.path.join("Documentation", "Diagrams", "PNG", "01_System_Architecture.png")
    if os.path.exists(img_arch):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_arch, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 2.1.1: MindEase Subsystem Interconnections & Multi-Tier Architecture")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    doc.add_heading("2.2 Product Scope", level=2)
    p = doc.add_paragraph(
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
    p = doc.add_paragraph("The core functionalities of MindEase are structured into twelve (12) integrated functional modules:")
    modules_desc = [
        ("Module 1: Multilingual Stress Questionnaire and Scoring", "Enables students to complete stress assessments in English, Urdu, or Roman Urdu with AI scoring assistance for written text and manual score confirmation."),
        ("Module 2: Voice and Text Check-in (Daily Diary)", "Captures audio and text reflections, transcribes audio using Whisper ASR, extracts emotional sentiment, and scans for danger/crisis indicators."),
        ("Module 3: Habit Tracking and Stress Level Detection", "Gathers sleep duration, screen time, and daily steps, fusing habit metrics with psychological scores to classify overall stress into Low, Moderate, or High."),
        ("Module 4: Personal Baseline and Trigger Analysis", "Calculates a dynamic rolling baseline over longitudinal check-ins, identifying trend trajectories (improving, stable, escalating) and academic correlations."),
        ("Module 5: Explainable AI (XAI) and Insights", "Deploys SHAP game-theoretic feature attribution to show students the exact behavioral factors responsible for their stress rating."),
        ("Module 6: Recommendations and Content Library", "Curates calming media (music, videos, stories, recitations) and measures delta stress relief via pre- and post-activity rating scales."),
        ("Module 7: AI Chatbot and Conversational Support", "Delivers 24/7 conversational assistance, contextualized with recent stress history upon student consent, offering empathetic companionship and triage recommendations."),
        ("Module 8: Adaptive Study and Recovery Planner", "Generates daily task schedules that adapt block lengths and break frequencies according to the student's real-time stress state."),
        ("Module 9: Counselor Portal and Professional Support", "Enables verified counselors to manage availability, conduct sessions, review consented student stress histories, and archive encrypted clinical notes."),
        ("Module 10: Admin Portal and Content Management", "Empowers university administrators to manage user accounts, approve counselor licenses, curate the content library, and resolve moderation reports without accessing private diaries."),
        ("Module 11: Community Support", "Provides a peer interaction platform featuring anonymous posts, verified counselor badges, and community report safety mechanisms."),
        ("Module 12: Payments and Appointment Billing (Polar)", "Manages appointment financial transactions using Polar's test mode sandbox, enforcing the free-tier triage rule and verifying payments via HMAC webhooks.")
    ]
    for m_title, m_det in modules_desc:
        p_m = doc.add_paragraph()
        r_mt = p_m.add_run(f"• {m_title}: ")
        r_mt.bold = True
        p_m.add_run(m_det)

    doc.add_heading("2.4 Users and Characteristics", level=2)
    users_info = [
        ("Student (Primary User)", "High frequency (daily to multiple times per week). Moderate technical expertise. Primary goal: track wellness, understand stress causes, plan study tasks, and access confidential help without social stigma."),
        ("Counselor (Mental Health Professional)", "Moderate frequency (scheduled weekly/daily appointment slots). High professional clinical expertise, moderate technical expertise. Primary goal: review consented student histories, conduct therapy sessions, and record clinical observations."),
        ("Administrator (System Admin)", "Regular administrative frequency. High technical expertise, privileged system access. Primary goal: review counselor applications, moderate flagged community posts, maintain media libraries, and inspect platform telemetry.")
    ]
    for u_name, u_det in users_info:
        p_u = doc.add_paragraph()
        r_ut = p_u.add_run(f"• {u_name}: ")
        r_ut.bold = True
        p_u.add_run(u_det)

    doc.add_heading("2.5 Operating Environment", level=2)
    p = doc.add_paragraph(
        "• Mobile Operating System: Android 9.0 (API Level 28) and above. Minimum 2 GB RAM, 100 MB free storage, active microphone hardware.\n"
        "• Server Operating System: Ubuntu Linux 22.04 LTS (x86_64 / ARM64) hosted on cloud virtual machine containers.\n"
        "• Server Runtime & Framework: Python 3.11+, FastAPI ASGI framework, Uvicorn server, PyTorch, Scikit-learn, Hugging Face Transformers.\n"
        "• Database Management System: Supabase Cloud Managed PostgreSQL 15+ with PostgREST, GoTrue Auth, and Row-Level Security.\n"
        "• External Gateways: Polar Payment Gateway (Sandbox API), Whisper ASR model service."
    )

    doc.add_page_break()

    print("Writing Section 3: Specific Requirements & Fully Dressed Use Cases...")
    # -------------------------------------------------------------
    # 3 SPECIFIC REQUIREMENTS
    # -------------------------------------------------------------
    doc.add_heading("3 Specific Requirements", level=1)

    doc.add_heading("3.1 Functional Requirements", level=2)
    fr_sections = [
        ("3.1.1 User Authentication & Role Management", [
            ("FR-01", "The system shall permit students and counselors to register accounts using their institutional or personal email addresses."),
            ("FR-02", "The system shall enforce email verification before activating new user accounts."),
            ("FR-03", "The system shall support multi-role authentication (Student, Counselor, Admin) using Supabase Auth JWT tokens."),
            ("FR-04", "The system shall require counselor applicants to upload licensing credentials, retaining their status as 'Pending' until admin approval."),
            ("FR-05", "The system shall provide secure password reset functionality via time-limited cryptographic email tokens."),
            ("FR-06", "The system shall enforce Row-Level Security (RLS) policies at the database layer to prevent unauthorized cross-tenant data access.")
        ]),
        ("3.1.2 Multilingual Stress Questionnaire & Scoring", [
            ("FR-07", "The system shall provide standardized stress assessment questionnaires localized in English, Urdu, and Roman Urdu."),
            ("FR-08", "The system shall support both multiple-choice selection and free-form text input for questionnaire questions."),
            ("FR-09", "The system shall employ an NLP text evaluator to suggest numerical scores for open-ended written responses."),
            ("FR-10", "The system shall require students to review and confirm or adjust any AI-suggested score before final tabulation."),
            ("FR-11", "The system shall compute the cumulative Perceived Stress Scale (PSS) questionnaire score."),
            ("FR-12", "The system shall persist confirmed questionnaire assessments with timestamps in the PostgreSQL database.")
        ]),
        ("3.1.3 Voice & Text Daily Diary Check-in", [
            ("FR-13", "The system shall allow students to record audio reflections up to 3 minutes in duration in English, Urdu, or Roman Urdu."),
            ("FR-14", "The system shall allow students to submit text diary entries in supported languages."),
            ("FR-15", "The system shall transcribe voice audio into text using the Whisper ASR deep learning model."),
            ("FR-16", "The system shall extract sentiment polarity, emotional valence, and primary topic tags (academics, sleep, relationships) from diary text."),
            ("FR-17", "The system shall assign a normalized diary stress score based on NLP sentiment analysis."),
            ("FR-18", "The system shall automatically scan diary text for danger or self-harm keywords, instantly triggering crisis helpline resources if flagged."),
            ("FR-19", "The system shall encrypt diary contents using AES-256 before persisting records to ensure absolute privacy.")
        ]),
        ("3.1.4 Habit Tracking & Multimodal Stress Fusion", [
            ("FR-20", "The system shall provide an intuitive interface for students to log daily sleep hours, smartphone screen time, and step counts."),
            ("FR-21", "The system shall permit students to skip any optional habit metric without blocking assessment completion."),
            ("FR-22", "The system shall impute missing habit values using the student's rolling 7-day personal average."),
            ("FR-23", "The system shall combine questionnaire scores, diary sentiment, and habit metrics into a unified feature vector."),
            ("FR-24", "The multimodal ML fusion model shall classify the student's stress level into Low, Moderate, or High categories along with a confidence metric."),
            ("FR-25", "The system shall store the daily stress classification and feature snapshot in the database.")
        ]),
        ("3.1.5 Personal Baseline & Trigger Analysis", [
            ("FR-26", "The system shall establish a baseline stress profile after a student completes three initial check-ins."),
            ("FR-27", "The system shall continuously calculate a rolling 14-day baseline to accommodate natural stress fluctuations."),
            ("FR-28", "The system shall classify stress trend trajectories as Improving, Stable, or Escalating."),
            ("FR-29", "The system shall correlate stress spikes with user-inputted university academic events (exams, project submissions)."),
            ("FR-30", "The system shall generate interactive weekly and monthly graphical charts showing stress progress over time.")
        ]),
        ("3.1.6 Explainable AI (XAI) & Insights", [
            ("FR-31", "The system shall compute SHAP (SHapley Additive exPlanations) values for each daily multimodal stress assessment."),
            ("FR-32", "The system shall rank the top three contributing factors driving the estimated stress level."),
            ("FR-33", "The system shall translate mathematical SHAP attributions into clear, human-understandable English/Urdu explanations."),
            ("FR-34", "The system shall render an intuitive feature importance bar chart illustrating positive and negative stress drivers."),
            ("FR-35", "The system shall map identified primary stress drivers to targeted, actionable recovery recommendations.")
        ]),
        ("3.1.7 Recommendations & Relaxation Content Library", [
            ("FR-36", "The system shall filter and recommend calming content based on the student's real-time stress level and identified drivers."),
            ("FR-37", "The content library shall support ambient music, uplifting stories, guided breathing exercises, and spiritual recitations."),
            ("FR-38", "The system shall allow students to bookmark favourite media resources into a personalized 'My Collection' list."),
            ("FR-39", "The system shall prompt students to record self-reported stress ratings (1-10) before and after completing a relaxation activity."),
            ("FR-40", "The system shall track delta stress reduction to calculate and display individualized content effectiveness scores.")
        ]),
        ("3.1.8 AI Chatbot & Conversational Support", [
            ("FR-41", "The system shall provide an interactive conversational AI interface supporting text and voice messaging."),
            ("FR-42", "The system shall support conversational interactions in English, Urdu, and Roman Urdu."),
            ("FR-43", "With explicit student permission, the chatbot shall ingest recent stress levels to tailor its supportive dialogue."),
            ("FR-44", "The chatbot shall provide cognitive reframing suggestions, breathing exercises, and motivational guidance."),
            ("FR-45", "The chatbot shall detect clinical distress and proactively suggest scheduling a session with a campus counselor."),
            ("FR-46", "The system shall maintain encrypted conversation history accessible only to the authenticated student.")
        ]),
        ("3.1.9 Adaptive Study & Recovery Planner", [
            ("FR-47", "The system shall allow students to create academic tasks, assign deadlines, and specify subject weights."),
            ("FR-48", "The system shall generate daily study schedules divided into structured Pomodoro focus sessions and breaks."),
            ("FR-49", "When High stress is detected, the planner shall automatically compress session durations (e.g., to 25 mins) and expand rest periods."),
            ("FR-50", "The planner shall schedule mindfulness and relaxation exercises during extended break periods."),
            ("FR-51", "The system shall allow students to reschedule or roll over uncompleted study tasks to the subsequent day."),
            ("FR-52", "The system shall track study task completion rates and display academic productivity statistics.")
        ]),
        ("3.1.10 Counselor Portal & Professional Support", [
            ("FR-53", "The system shall publish verified counselor profiles displaying qualifications, specializations, languages, and open time slots."),
            ("FR-54", "The system shall allow students to request virtual counseling appointments."),
            ("FR-55", "The system shall provide the first counseling appointment completely free of charge when triggered by a High stress assessment."),
            ("FR-56", "The system shall require payment verification for subsequent counseling appointments according to institutional policy."),
            ("FR-57", "With student consent, counselors shall be authorized to inspect historical stress trends, baselines, and XAI insights."),
            ("FR-58", "The system shall provide an encrypted clinical notes editor for counselors to record post-session evaluations.")
        ]),
        ("3.1.11 Peer Community Support & Moderation", [
            ("FR-59", "The system shall allow students to publish text posts, share personal coping experiences, and comment on peer posts."),
            ("FR-60", "The system shall allow students to publish community posts under an anonymous pseudonym."),
            ("FR-61", "The system shall highlight comments posted by verified counselors with a distinct, tamper-proof 'Counselor Badge'."),
            ("FR-62", "The system shall execute automated keyword filtering to block profane, abusive, or explicitly harmful content."),
            ("FR-63", "The system shall provide a 'Flag / Report' mechanism allowing users to report inappropriate community contributions."),
            ("FR-64", "The system shall temporarily quarantine community posts that exceed a predefined flag threshold pending admin review.")
        ]),
        ("3.1.12 Polar Payment Gateway & Billing Service", [
            ("FR-65", "The system shall integrate with the Polar payment platform operating in test/sandbox mode."),
            ("FR-66", "The system shall generate secure checkout sessions for paid counseling appointments."),
            ("FR-67", "The system shall process webhook events dispatched by Polar to verify successful transactions."),
            ("FR-68", "The system shall verify HMAC-SHA256 signatures on all incoming Polar webhooks before confirming bookings."),
            ("FR-69", "The system shall display digital payment receipts with transaction reference numbers to students."),
            ("FR-70", "The system shall never store raw credit card numbers or CVV codes, ensuring strict PCI-DSS compliance.")
        ]),
        ("3.1.13 Admin Portal & Content Management", [
            ("FR-71", "The system shall provide an administrative console accessible exclusively to authorized university admins."),
            ("FR-72", "The system shall allow admins to inspect pending counselor registration requests and approve or reject licenses."),
            ("FR-73", "The system shall allow admins to upload, edit, categorize, and archive content library media resources."),
            ("FR-74", "The system shall display reported community posts in an actionable moderation queue for deletion or dismissal."),
            ("FR-75", "The system shall display anonymized campus-wide stress trends and platform engagement analytics."),
            ("FR-76", "The system shall strictly block administrative access to student private diaries, voice recordings, and chatbot logs.")
        ])
    ]

    for sec_title, fr_list in fr_sections:
        doc.add_heading(sec_title, level=3)
        for fid, ftext in fr_list:
            p_fr = doc.add_paragraph()
            r_fid = p_fr.add_run(f"[{fid}] ")
            r_fid.bold = True
            p_fr.add_run(ftext)

    # -------------------------------------------------------------
    # 3.2 Behaviour Requirements (Use Cases & Fully Dressed Tables)
    # -------------------------------------------------------------
    doc.add_page_break()
    doc.add_heading("3.2 Behaviour Requirements", level=2)
    p = doc.add_paragraph(
        "The functional behavior of MindEase is specified through a unified Use Case Diagram encapsulating all actors, "
        "system boundaries, and operational use cases. The system defines three primary human actors (Student, Counselor, Administrator) "
        "and four secondary system actors (Whisper ASR, Multimodal ML Fusion Model, SHAP XAI Engine, Polar Payment Gateway). "
        "Below is the complete Use Case Diagram followed by the inventory table and seventeen (17) fully dressed use-case specifications."
    )

    # Insert Use Case Diagram
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

    doc.add_heading("3.2.1 System Use Case Inventory", level=3)
    uc_inventory = [
        ("UC01", "Register & Create Profile", "Student, Counselor", "Account creation and profile registration."),
        ("UC02", "Login & Multi-Role Authentication", "Student, Counselor, Admin", "Credentials verification and role-based routing."),
        ("UC03", "Complete Multilingual Stress Questionnaire", "Student", "PSS assessment in English/Urdu/Roman Urdu with text scoring."),
        ("UC04", "Record Daily Voice and Text Diary", "Student", "Audio recording, Whisper ASR STT, sentiment analysis, crisis check."),
        ("UC05", "Log Daily Habits & Calculate Stress Level", "Student", "Habit data entry and multimodal ML stress classification."),
        ("UC06", "View Stress Trends & Baseline Trigger Analysis", "Student", "Longitudinal progress graphs and exam trigger correlation."),
        ("UC07", "View Explainable AI Stress Insights", "Student", "SHAP feature attribution charts and actionable recommendations."),
        ("UC08", "Access Relaxation Content & Rate Activity", "Student", "Browsing calming media and pre/post activity rating."),
        ("UC09", "Chat with AI Conversational Assistant", "Student", "Contextual empathetic support and escalation suggestions."),
        ("UC10", "Generate & Manage Adaptive Study Plan", "Student", "Task chunking and stress-adaptive Pomodoro scheduling."),
        ("UC11", "Search Counselors & Request Appointment", "Student", "Directory filtering, free triage check, and appointment request."),
        ("UC12", "Conduct Counseling Session & Maintain Notes", "Counselor", "Virtual session execution, trend review, encrypted clinical notes."),
        ("UC13", "Process Appointment Payment via Polar", "Student", "Test mode checkout, payment capture, webhook confirmation."),
        ("UC14", "Create & Interact with Peer Community Posts", "Student, Counselor", "Sharing peer messages, anonymous posting, counselor badges."),
        ("UC15", "Report Inappropriate Community Post", "Student", "Flagging abusive content and automated quarantine."),
        ("UC16", "Manage System Users & Counselor Approvals", "Administrator", "Reviewing credentials, granting counselor permissions."),
        ("UC17", "Moderate Community Reports & System Content", "Administrator", "Triage reported posts queue and curate relaxation media.")
    ]

    t_uci = doc.add_table(rows=len(uc_inventory)+1, cols=4)
    t_uci.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_uci)
    headers = ["Use Case ID", "Use Case Name", "Actors", "Summary Scope"]
    for ci, htext in enumerate(headers):
        c = t_uci.rows[0].cells[ci]
        c.paragraphs[0].add_run(htext).bold = True
        set_cell_background(c, "1E3A8A")
        c.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        c.paragraphs[0].runs[0].font.size = Pt(9.5)

    for ri, (uid, uname, uact, udesc) in enumerate(uc_inventory):
        row = t_uci.rows[ri+1]
        row.cells[0].paragraphs[0].add_run(uid).bold = True
        row.cells[1].paragraphs[0].add_run(uname)
        row.cells[2].paragraphs[0].add_run(uact)
        row.cells[3].paragraphs[0].add_run(udesc)
        for ci in range(4):
            row.cells[ci].paragraphs[0].runs[0].font.size = Pt(9)
            set_cell_background(row.cells[ci], "FFFFFF" if ri%2==0 else "F8FAFC")

    # -------------------------------------------------------------
    # 3.2.2 Fully Dressed Use Cases (Exact Inspiration Format)
    # -------------------------------------------------------------
    doc.add_page_break()
    doc.add_heading("3.2.2 Fully Dressed Use Case Specifications", level=3)
    p = doc.add_paragraph("Each of the seventeen (17) identified use cases is formally detailed below according to university specification standards:")

    # Detailed specifications for all 17 UCs matching inspiration layout
    fully_dressed_data = [
        {
            "id": "UC01",
            "title": "Use Case #1: Register & Create Profile",
            "primary": "Student, Counselor",
            "secondary": "Supabase Auth, ProfileRepository",
            "desc": "A new student or counselor registers an account in MindEase by providing personal credentials, institutional details, and role specifications.",
            "pre": "The user must have a valid institutional or personal email address and not already possess an active registered account.",
            "steps": [
                "1. The user launches the MindEase application and selects 'Register'.",
                "2. The user inputs their full name, email, password, and selects their role (Student or Counselor).",
                "3. If Counselor is selected, the user enters license number, specialization, and uploads credential documentation.",
                "4. The system validates the input fields for format correctness and checks for duplicate registrations.",
                "5. The system creates the user record in Supabase Auth and stores profile details in the database.",
                "6. For students, the account is marked active upon email confirmation; for counselors, status remains 'Pending' awaiting admin review."
            ],
            "post": "A new user account is successfully provisioned and an activation confirmation message is displayed.",
            "exceptions": "If the email is already registered or passwords do not satisfy complexity requirements, the system displays an error and denies submission.",
            "rel": "Extended by Manage System Users & Counselor Approvals (UC16) for counselor credential validation."
        },
        {
            "id": "UC02",
            "title": "Use Case #2: Login & Multi-Role Authentication",
            "primary": "Student, Counselor, Administrator",
            "secondary": "Supabase Auth (GoTrue)",
            "desc": "Registered users authenticate with their email and password to receive secure JWT tokens and be routed to their respective role dashboards.",
            "pre": "The user must possess a registered and verified account.",
            "steps": [
                "1. The user opens the MindEase login screen.",
                "2. The user enters their registered email address and password.",
                "3. The system verifies credentials against Supabase Auth.",
                "4. The system inspects the user's assigned role (Student, Counselor, or Admin).",
                "5. The system issues a session token and redirects the user to their designated dashboard (Student Home, Counselor Portal, or Admin Console)."
            ],
            "post": "The user is authenticated and authorized to access features corresponding to their privilege level.",
            "exceptions": "If credentials are invalid or if a counselor account is still 'Pending', the system displays an error and blocks portal entry.",
            "rel": "Foundational use case prerequisite for all core interactive features."
        },
        {
            "id": "UC03",
            "title": "Use Case #3: Complete Multilingual Stress Questionnaire",
            "primary": "Student",
            "secondary": "ScoringEngine, StressRepository",
            "desc": "A student completes a standardized psychological stress questionnaire in their preferred language (English, Urdu, or Roman Urdu), confirming AI suggestions for open-ended text.",
            "pre": "The student must be logged in.",
            "steps": [
                "1. The student navigates to the Stress Assessment section and selects their preferred language.",
                "2. The system loads localized assessment questions.",
                "3. The student submits answers to multiple-choice items and optional open-ended written text.",
                "4. For written responses, the AI Scoring Engine evaluates the text and suggests an estimated sub-score.",
                "5. The student reviews, confirms, or modifies the suggested score.",
                "6. The system computes the final questionnaire score (PSS metric) and saves the result in the database."
            ],
            "post": "The questionnaire score is stored and immediately integrated into the daily stress calculation.",
            "exceptions": "If mandatory questions are left unanswered, the system prompts the student to complete all required items before submission.",
            "rel": "Included in Log Daily Habits & Calculate Stress Level (UC05)."
        },
        {
            "id": "UC04",
            "title": "Use Case #4: Record Daily Voice and Text Diary",
            "primary": "Student",
            "secondary": "WhisperASREngine, NLPSafetyMonitor, DiaryRepository",
            "desc": "A student records a spoken audio reflection or writes a journal entry. The system transcribes audio, extracts emotional sentiments, and monitors for safety risks.",
            "pre": "The student must be authenticated and microphone permissions must be granted for audio input.",
            "steps": [
                "1. The student opens the Daily Diary section and chooses Voice or Text check-in.",
                "2. If voice is chosen, the student records up to 3 minutes of audio; if text, the student types their thoughts.",
                "3. The system dispatches audio to Whisper ASR to produce accurate text in English, Urdu, or Roman Urdu.",
                "4. The NLP Safety Monitor evaluates the text for emotional sentiment, dominant topics (exams, sleep), and safety crisis keywords.",
                "5. If crisis or self-harm keywords are flagged, the system immediately presents an emergency alert with national crisis helplines.",
                "6. The system calculates a diary sentiment score, encrypts the diary text with AES-256, and stores the record."
            ],
            "post": "The diary is securely encrypted, sentiment scores are logged, and crisis triage is activated if necessary.",
            "exceptions": "If audio recording is distorted or exceeds time limits, the system prompts the user to re-record.",
            "rel": "Integrates with Log Daily Habits & Calculate Stress Level (UC05)."
        },
        {
            "id": "UC05",
            "title": "Use Case #5: Log Daily Habits & Calculate Stress Level",
            "primary": "Student",
            "secondary": "MultimodalFusionEngine, StressRepository",
            "desc": "The student logs lifestyle metrics (sleep, screen time, steps). The system fuses habit data with questionnaire and diary scores to classify overall stress as Low, Moderate, or High.",
            "pre": "The student must be authenticated.",
            "steps": [
                "1. The student navigates to the Daily Habit Tracker.",
                "2. The student logs sleep hours, smartphone screen time, and daily steps (or skips optional metrics).",
                "3. The system imputes any omitted fields using the student's rolling 7-day average.",
                "4. The system retrieves the day's latest questionnaire and diary sentiment scores.",
                "5. The Multimodal Fusion Model processes the unified feature vector and predicts stress: Low, Moderate, or High.",
                "6. The system displays the estimated stress category with confidence metrics and triggers downstream recovery workflows."
            ],
            "post": "Daily stress level is classified, persisted, and linked to explainability insights and study planning.",
            "exceptions": "If no prior questionnaire or diary exists for the day, the system prompts the student to complete a quick check-in.",
            "rel": "Includes View Explainable AI Stress Insights (UC07)."
        },
        {
            "id": "UC06",
            "title": "Use Case #6: View Stress Trends & Baseline Trigger Analysis",
            "primary": "Student",
            "secondary": "BaselineAnalysisEngine, StressRepository",
            "desc": "The student inspects their longitudinal stress progress graphs, evaluating how their stress fluctuates against personal baselines and academic deadlines.",
            "pre": "The student must have completed at least three prior check-ins to establish a baseline.",
            "steps": [
                "1. The student navigates to 'Stress Trends & Analytics' from the dashboard.",
                "2. The student selects the time horizon (Weekly or Monthly).",
                "3. The system retrieves historical assessment records and calculates the rolling baseline.",
                "4. The system identifies trend trajectories (improving, stable, escalating) and overlays university exam dates.",
                "5. The system renders interactive graphical charts with explanatory summaries."
            ],
            "post": "The student gains clear visibility into longitudinal mental health patterns and academic stress triggers.",
            "exceptions": "If fewer than three assessments exist, the system informs the student that baseline calculation is still accumulating data.",
            "rel": "None."
        },
        {
            "id": "UC07",
            "title": "Use Case #7: View Explainable AI Stress Insights",
            "primary": "Student",
            "secondary": "SHAPExplainerService, ActionableRecommender",
            "desc": "The student examines plain-language explanations of why their stress was classified as Low, Moderate, or High, powered by SHAP feature attributions.",
            "pre": "An active stress assessment must exist for the selected day.",
            "steps": [
                "1. The student clicks 'Why do I feel this way?' on their stress assessment result card.",
                "2. The system queries the SHAP Explainer Service with the assessment's feature snapshot.",
                "3. The SHAP service computes mathematical feature attributions for sleep deficit, screen time, diary valence, and PSS score.",
                "4. The system translates the top 3 contributing factors into conversational insights (e.g., 'Your 4 hours of sleep and high screen time contributed most to your High stress today').",
                "5. The system presents an intuitive horizontal attribution chart paired with actionable self-care tips."
            ],
            "post": "The student receives transparent, non-black-box explanations of their stress drivers.",
            "exceptions": "If the SHAP service is temporarily unavailable, default rule-based explanations are presented gracefully.",
            "rel": "Included in Log Daily Habits & Calculate Stress Level (UC05)."
        },
        {
            "id": "UC08",
            "title": "Use Case #8: Access Relaxation Content & Rate Activity",
            "primary": "Student",
            "secondary": "MediaStreamingService, ActivityRatingRepository",
            "desc": "The student browses recommended relaxation media (music, stories, exercises, recitations) and evaluates activity efficacy by rating their stress before and after completion.",
            "pre": "The student must be authenticated.",
            "steps": [
                "1. The student navigates to the 'Relaxation & Recovery' content library.",
                "2. The system presents personalized recommendations based on the current stress level.",
                "3. The student selects an activity and rates their immediate pre-activity stress level (1 to 10).",
                "4. The system streams the audio, video, or guided exercise.",
                "5. Upon completion, the student rates their post-activity stress level (1 to 10).",
                "6. The system calculates delta stress relief and saves the rating to personalize future recommendations."
            ],
            "post": "Activity is logged, effectiveness is quantified, and the item may be saved to 'My Collection'.",
            "exceptions": "If streaming fails due to poor internet connection, the system provides local offline cached exercises.",
            "rel": "None."
        },
        {
            "id": "UC09",
            "title": "Use Case #9: Chat with AI Conversational Assistant",
            "primary": "Student",
            "secondary": "LLMConversationalEngine, ChatRepository",
            "desc": "The student engages in a supportive 24/7 conversation with an AI assistant to discuss daily academic worries, practice breathing, or seek self-help advice.",
            "pre": "The student must be authenticated.",
            "steps": [
                "1. The student opens the AI Chatbot interface and types or speaks a message.",
                "2. The system optionally loads the student's latest stress summary if consent was provided.",
                "3. The Conversational Engine generates an empathetic, supportive response adhering to clinical safety guidelines.",
                "4. If the student expresses severe anxiety or clinical distress, the chatbot gently prompts the student to book an appointment with a counselor.",
                "5. The conversation turn is encrypted and saved to the student's personal chat history."
            ],
            "post": "The student receives immediate companionship and coping guidance; messages remain strictly confidential.",
            "exceptions": "If explicit crisis statements are detected, the chatbot displays emergency helpline numbers and urges human contact.",
            "rel": "Extends to Search Counselors & Request Appointment (UC11)."
        },
        {
            "id": "UC10",
            "title": "Use Case #10: Generate & Manage Adaptive Study Plan",
            "primary": "Student",
            "secondary": "AdaptivePlannerEngine, StudyTaskRepository",
            "desc": "The student inputs academic tasks and deadlines. The system generates an adaptive Pomodoro study schedule that automatically tunes work blocks and rest periods based on stress levels.",
            "pre": "The student must be authenticated.",
            "steps": [
                "1. The student inputs study tasks, upcoming assignment/exam deadlines, and estimated completion times.",
                "2. The system retrieves the student's real-time stress level.",
                "3. If stress is High, the system creates shorter focus intervals (25 mins) and longer restorative breaks (15 mins) with calming exercises.",
                "4. If stress is Low/Moderate, the system creates standard 50-minute study blocks with 10-minute breaks.",
                "5. The student reviews the schedule, checks off completed tasks, and rolls over uncompleted items to the next day."
            ],
            "post": "An optimized, stress-conscious study plan is generated and persisted.",
            "exceptions": "If no tasks are inputted, the system prompts the user to add at least one academic task.",
            "rel": "None."
        },
        {
            "id": "UC11",
            "title": "Use Case #11: Search Counselors & Request Appointment",
            "primary": "Student",
            "secondary": "FreeTierEligibilityRule, AppointmentRepository",
            "desc": "The student browses qualified counselor profiles, checks open slots, and books an appointment. The first session after High stress is granted free; subsequent sessions require payment.",
            "pre": "The student must be logged in.",
            "steps": [
                "1. The student opens the Counselor Directory and filters by language, specialization, and availability.",
                "2. The system displays verified counselor profiles and calendar slots.",
                "3. The student selects an available appointment time slot.",
                "4. The system checks eligibility for a free appointment (triggered if the student recently recorded High stress and has not used their free triage session).",
                "5. If free, the system immediately confirms the appointment and notifies the counselor.",
                "6. If paid, the system directs the student to the Polar payment checkout flow."
            ],
            "post": "An appointment is scheduled (either Confirmed if free, or Pending Payment if paid).",
            "exceptions": "If a selected time slot is taken concurrently by another user, the system prompts the student to choose another slot.",
            "rel": "Extended by Process Appointment Payment via Polar (UC13)."
        },
        {
            "id": "UC12",
            "title": "Use Case #12: Conduct Counseling Session & Maintain Notes",
            "primary": "Counselor",
            "secondary": "AccessControlService, ClinicalNotesRepository",
            "desc": "A counselor initiates a scheduled appointment, reviews consented student stress trends, conducts the therapy session, and files encrypted clinical notes.",
            "pre": "The counselor must be logged in with verified credentials, and the appointment must be in 'Confirmed' status.",
            "steps": [
                "1. The counselor opens their Appointment Portal and launches the confirmed session room.",
                "2. If the student granted data disclosure consent, the counselor reviews the student's stress baselines, XAI drivers, and trend charts.",
                "3. The counselor conducts the counseling consultation (chat, audio, or video).",
                "4. Following the consultation, the counselor types clinical observations, assessment findings, and follow-up guidance.",
                "5. The system encrypts the clinical notes and archives the appointment as 'Completed'."
            ],
            "post": "The appointment is completed, and clinical notes are securely stored with restricted counselor-only access.",
            "exceptions": "If the student withheld consent for data sharing, the counselor is presented with a standard consultation room without historical stress logs.",
            "rel": "Follows Search Counselors & Request Appointment (UC11)."
        },
        {
            "id": "UC13",
            "title": "Use Case #13: Process Appointment Payment via Polar",
            "primary": "Student",
            "secondary": "PolarPaymentGateway, AppointmentRepository",
            "desc": "The student completes payment for a paid counselor session via the Polar test sandbox, verifying success through backend webhooks.",
            "pre": "An appointment must be requested that is ineligible for free tier triage.",
            "steps": [
                "1. The student proceeds to checkout from the appointment confirmation screen.",
                "2. The system requests a checkout session from the Polar API in sandbox test mode.",
                "3. The student is presented with the Polar payment sheet and enters test card credentials.",
                "4. Polar processes the transaction and dispatches an asynchronous webhook to the FastAPI backend.",
                "5. The backend verifies the HMAC signature of the webhook, validates the payment ID, and updates the appointment status to 'Confirmed'.",
                "6. The student is redirected to an on-screen confirmation receipt with the transaction reference."
            ],
            "post": "The appointment payment is confirmed, and the booking is finalized without storing sensitive card data.",
            "exceptions": "If test payment is declined, the system notifies the student and retains the appointment in 'Pending Payment' status for 15 minutes.",
            "rel": "Extends Search Counselors & Request Appointment (UC11)."
        },
        {
            "id": "UC14",
            "title": "Use Case #14: Create & Interact with Peer Community Posts",
            "primary": "Student, Counselor",
            "secondary": "ContentSafetyFilter, CommunityRepository",
            "desc": "Users share coping experiences, ask questions, and reply to peers in a supportive community space, with anonymous options and verified counselor badges.",
            "pre": "The user must be authenticated.",
            "steps": [
                "1. The user navigates to the Community Feed and clicks 'New Post'.",
                "2. The user types post content, selects topic tags, and toggles 'Post Anonymously' if desired.",
                "3. The system scans the post content using the automated Content Safety Filter for profanity or abusive language.",
                "4. If clean, the post is saved and published to the live feed.",
                "5. Peers can like or reply to the post; replies by licensed counselors automatically display a 'Verified Counselor' badge."
            ],
            "post": "The post or reply is published in the community feed.",
            "exceptions": "If the post contains toxic or prohibited keywords, submission is rejected with a policy warning prompt.",
            "rel": "Extended by Report Inappropriate Community Post (UC15)."
        },
        {
            "id": "UC15",
            "title": "Use Case #15: Report Inappropriate Community Post",
            "primary": "Student",
            "secondary": "ModerationQueueService, CommunityRepository",
            "desc": "A student flags a post or comment that violates community safety standards, queuing it for administrative review and automated temporary quarantine.",
            "pre": "The student must be authenticated.",
            "steps": [
                "1. The student clicks 'Report' on a community post or reply.",
                "2. The student selects the violation reason (Harassment, Inappropriate Language, Self-Harm, Spam).",
                "3. The system records the report and increments the post's flag counter.",
                "4. If the flag count exceeds the safety threshold (>= 3 flags), the system automatically hides the post from the public feed.",
                "5. The ticket is queued for administrative review, and the reporting user receives an acknowledgment notice."
            ],
            "post": "The post is flagged, potentially hidden, and enqueued in the admin moderation dashboard.",
            "exceptions": "A user cannot report the same post multiple times from a single account.",
            "rel": "Extends Create & Interact with Peer Community Posts (UC14)."
        },
        {
            "id": "UC16",
            "title": "Use Case #16: Manage System Users & Counselor Approvals",
            "primary": "Administrator",
            "secondary": "SupabaseAuth, CounselorRepository",
            "desc": "The university administrator reviews pending counselor registrations, verifies credentials, and approves or denies counselor privileges.",
            "pre": "The administrator must be logged in with admin role credentials.",
            "steps": [
                "1. The admin accesses 'Counselor Applications' from the Admin Portal.",
                "2. The system lists all pending counselor submissions.",
                "3. The admin inspects uploaded degree certificates, license numbers, and professional bios.",
                "4. The admin selects 'Approve' or 'Reject' (with a mandatory feedback reason).",
                "5. If approved, the system updates the counselor's status to 'Approved' and unlocks the Counselor Portal for that user.",
                "6. An automated notification email is sent to the applicant."
            ],
            "post": "Counselor verification status is resolved, and role permissions are updated.",
            "exceptions": "If uploaded documents are illegible, the admin requests credential re-upload.",
            "rel": "Follows Register & Create Profile (UC01)."
        },
        {
            "id": "UC17",
            "title": "Use Case #17: Moderate Community Reports & System Content",
            "primary": "Administrator",
            "secondary": "CommunityRepository, ContentLibraryRepository",
            "desc": "The administrator resolves reported community post tickets and curates the relaxation media library (uploading music, stories, and videos).",
            "pre": "The administrator must be authenticated with admin privileges.",
            "steps": [
                "1. The admin opens the 'Content Moderation' dashboard.",
                "2. The system displays all reported community posts with violation categories and reporter counts.",
                "3. The admin reviews the content and selects 'Delete Post' or 'Dismiss Report'.",
                "4. The system executes the decision, removing prohibited posts permanently or restoring falsely flagged posts.",
                "5. The admin navigates to the 'Media Library' section to add, update, or deactivate relaxation audio, video, or exercise assets."
            ],
            "post": "Moderation queue tickets are cleared, and the platform content library is updated.",
            "exceptions": "The administrator has zero access to private student diary entries or personal chatbot conversation histories.",
            "rel": "Resolves tickets generated by Report Inappropriate Community Post (UC15)."
        }
    ]

    for uc in fully_dressed_data:
        doc.add_heading(f"{uc['title']}", level=4)
        t_uc = doc.add_table(rows=8, cols=2)
        t_uc.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(t_uc)
        
        # Set column widths
        for row in t_uc.rows:
            row.cells[0].width = Inches(1.8)
            row.cells[1].width = Inches(4.7)

        rows_content = [
            ("Primary Actors", uc["primary"]),
            ("Secondary Actors", uc["secondary"]),
            ("Description", uc["desc"]),
            ("Pre-Condition", uc["pre"]),
            ("Steps", "\n".join(uc["steps"])),
            ("Post-Condition", uc["post"]),
            ("Exceptions", uc["exceptions"]),
            ("Relationships", uc["rel"])
        ]

        for ri, (field, details) in enumerate(rows_content):
            cell_f = t_uc.rows[ri].cells[0]
            cell_d = t_uc.rows[ri].cells[1]
            
            p_f = cell_f.paragraphs[0]
            p_f.add_run(field).bold = True
            p_f.runs[0].font.size = Pt(9.5)
            set_cell_background(cell_f, "F1F5F9")
            
            p_d = cell_d.paragraphs[0]
            p_d.add_run(details).font.size = Pt(9)
            set_cell_background(cell_d, "FFFFFF")

        p_spacer = doc.add_paragraph()
        p_spacer.paragraph_format.space_before = Pt(6)

    # -------------------------------------------------------------
    # 3.3 External Interface Requirements
    # -------------------------------------------------------------
    doc.add_page_break()
    doc.add_heading("3.3 External Interface Requirements", level=2)

    doc.add_heading("3.3.1 User Interfaces", level=3)
    p = doc.add_paragraph(
        "The MindEase user interface is built using Flutter, adhering to Material 3 design specifications with a calm, "
        "restrained aesthetic designed to minimize cognitive overload for stressed students. The interface maintains pure white backgrounds, "
        "deep slate text (#0F172A), navy blue primary action buttons (#1E3A8A), and subtle pastel cards (#F8FAFC).\n"
        "The application provides the following primary screens:\n"
        "• Onboarding & Role Authentication Screen: Clean login and registration forms supporting student ID input, counselor licensing uploads, and language toggles.\n"
        "• Daily Wellness Dashboard: Visual summary showing today's stress level badge, rolling 7-day trend chart, quick check-in buttons, and daily study task progress.\n"
        "• Multilingual Questionnaire Screen: Paginated question cards supporting radio selections and text boxes, with instant AI score suggestion chips in English, Urdu, and Roman Urdu.\n"
        "• Voice & Text Diary Check-in Screen: Audio visualizer displaying microphone waveforms during recording, live transcription preview, and emergency helpline overlay modal.\n"
        "• Explainable AI (XAI) Insights Sheet: Bottom-sheet modal presenting plain-language summaries of top stress contributors and horizontal feature weight bars.\n"
        "• Adaptive Study Planner Screen: Timeline view dividing the academic day into Pomodoro focus intervals, adaptive rest periods, and task completion checkboxes.\n"
        "• Relaxation Media Library & Player: Categorized grid (Music, Stories, Exercises, Recitations) with pre/post stress rating modal sliders.\n"
        "• Counselor Directory & Booking Modal: Filterable cards showing counselor qualifications, language badges, calendar time-slot pickers, and free/paid indicators.\n"
        "• Polar Payment Checkout Sheet: Embedded secure webview presenting test credit card fields with instant verification receipts.\n"
        "• Peer Community Feed: Scrollable feed supporting anonymous post creation, verified counselor response badges, and flag/report action sheets.\n"
        "• Admin Console: Desktop/tablet-optimized web dashboard showing counselor licensing queues, reported content moderation tables, and platform telemetry."
    )

    doc.add_heading("3.3.2 Hardware Interfaces", level=3)
    p = doc.add_paragraph(
        "• Audio Input Interface (Microphone): Captures raw mono audio input sampled at 16 kHz, 16-bit PCM for dispatch to the Whisper ASR speech-to-text pipeline.\n"
        "• Physical Activity Sensors (Pedometer / Step Counter): Interfaces with standard Android SensorManager hardware step counters and Google Health Connect APIs to record daily physical movement.\n"
        "• Screen Time Hardware Telemetry: Queries Android UsageStatsManager permissions to capture daily device active screen-on time in minutes.\n"
        "• Device Local Storage: Interfaces with internal flash storage using encrypted SharedPreferences (AES-256 GCM) for offline session cache."
    )

    doc.add_heading("3.3.3 Software Interfaces", level=3)
    p = doc.add_paragraph(
        "• Supabase Managed Cloud Platform: Connects via HTTPS REST (PostgREST) and WebSockets for real-time updates. Handles user authentication (GoTrue), relational data storage (PostgreSQL 15), Row Level Security (RLS), and S3-compatible media storage.\n"
        "• OpenAI Whisper ASR Model: Deployed as a dedicated Python inference worker to transcribe Urdu, Roman Urdu, and English speech audio into text.\n"
        "• Machine Learning Classification Engine: Scikit-learn and PyTorch deep learning modules executing feature normalization, multimodal fusion, and stress tier estimation.\n"
        "• SHAP (SHapley Additive exPlanations) Library: Computes game-theoretic local feature attributions for every inference record.\n"
        "• Hugging Face Transformers & Conversational LLM: Provides contextual natural language understanding and empathetic response generation for the AI chatbot.\n"
        "• Polar Payment Platform (Sandbox API): Processes payment tokenization, checkout URL generation, and asynchronous webhook dispatching for paid counseling sessions."
    )

    doc.add_heading("3.3.4 Communications Interfaces", level=3)
    p = doc.add_paragraph(
        "• HTTPS / TLS 1.3: All client-to-server REST communication occurs over encrypted TLS 1.3 channels using standard JSON payload formatting.\n"
        "• Secure WebSockets (WSS): Real-time communication channels utilized for interactive AI chatbot conversations and virtual counseling chat rooms.\n"
        "• Webhook Ingestion: FastAPI listens on dedicated HTTPS webhook endpoints to ingest asynchronous event payloads from Polar, verifying authenticity using HMAC-SHA256 signatures.\n"
        "• Offline Data Synchronization: The mobile client buffers local diary entries and habit metrics during intermittent connectivity, performing atomic background sync upon network reconnection."
    )

    # -------------------------------------------------------------
    # 4 OTHER NON-FUNCTIONAL REQUIREMENTS
    # -------------------------------------------------------------
    doc.add_page_break()
    doc.add_heading("4 Other Non-functional Requirements", level=1)

    doc.add_heading("4.1 Performance Requirements", level=2)
    p = doc.add_paragraph(
        "• API Response Time: Standard REST API queries (habit logging, profile retrieval, content browsing) shall respond in less than 500 milliseconds under nominal load.\n"
        "• ML Stress Fusion Latency: Multimodal stress inference and baseline comparison shall complete execution in under 800 milliseconds.\n"
        "• Whisper ASR Transcription Time: A 60-second voice diary recording shall be transcribed into text in less than 2.5 seconds on server GPU/CPU inference nodes.\n"
        "• SHAP Attribution Computation: XAI feature importance calculations shall complete within 1.0 second upon student request.\n"
        "• Concurrent User Scalability: The backend application server shall support up to 500 concurrent active student sessions without memory exhaustion or degradation of response latency beyond 1.5 seconds.\n"
        "• Database Query Execution: 95% of indexed PostgreSQL database queries shall execute in under 100 milliseconds."
    )

    doc.add_heading("4.2 Safety and Security Requirements", level=2)
    p = doc.add_paragraph(
        "• Crisis Detection & Emergency Safety: The system shall continuously analyze diary entries and chatbot interactions for acute distress signals. When self-harm or danger keywords are flagged, the system shall immediately display national crisis helplines and campus emergency contacts.\n"
        "• Absolute Diary Privacy: Student daily diary entries, voice recordings, and chatbot logs shall be encrypted using AES-256 and protected by Supabase Row-Level Security (RLS). Under no circumstances shall university administrators have access to private student reflections.\n"
        "• Student Consent for Counseling Data: Counselors shall only access historical stress trends and XAI insights if the student explicitly toggles the data-sharing consent permission.\n"
        "• Password Security & Authentication: Passwords shall be hashed using modern Argon2 or Bcrypt cryptographic algorithms. JWT access tokens shall expire after 60 minutes and be refreshed using secure httpOnly refresh tokens.\n"
        "• Payment Card Safety: MindEase shall never capture, transmit, or store raw credit card numbers or CVVs. All payment processing is delegated to Polar's PCI-DSS compliant sandbox checkout."
    )

    doc.add_heading("4.3 Software Quality Attributes", level=2)
    qa_list = [
        ("4.3.1 Reliability", "The system shall achieve 99.9% uptime during university operating semesters. The mobile client shall support graceful offline degradation, storing check-in records locally if internet connectivity drops."),
        ("4.3.2 Availability", "The backend server and Supabase database shall be hosted on redundant cloud infrastructure with automated daily database backups and failover replication."),
        ("4.3.3 Usability", "The application UI shall adhere to accessible design principles (WCAG 2.1 Level AA), providing full bilingual localization (English and Urdu), high contrast text ratios, and self-evident navigation requiring zero user training."),
        ("4.3.4 Maintainability", "The codebase shall enforce clean architectural separation (Flutter BLoC pattern on client; modular controller-service-repository pattern on FastAPI backend). Micro-services and ML models shall be containerized using Docker for reproducible deployment."),
        ("4.3.5 Portability", "The Flutter client shall build seamlessly for Android 9.0+ and be cross-compilable for iOS devices. The backend server shall execute independently across Linux and Windows environments."),
        ("4.3.6 Data Privacy & Compliance", "The system architecture aligns with international digital health privacy standards (GDPR/HIPAA-informed principles), giving students full rights to export or delete their account data at any time.")
    ]
    for qtitle, qdesc in qa_list:
        doc.add_heading(qtitle, level=3)
        doc.add_paragraph(qdesc)

    # -------------------------------------------------------------
    # 5 DESIGN DESCRIPTION
    # -------------------------------------------------------------
    doc.add_page_break()
    doc.add_heading("5 Design Description", level=1)

    doc.add_heading("5.1 Composite Viewpoint", level=2)
    p = doc.add_paragraph(
        "The Composite Viewpoint describes the system's structural decomposition into subsystems, components, and physical deployment nodes. "
        "MindEase employs a modern modular architecture where the Flutter mobile presentation layer communicates over encrypted REST/WebSocket APIs "
        "with an asynchronous FastAPI backend application server, supported by an isolated ML inference cluster and managed Supabase persistence."
    )

    # Component Diagram
    img_comp = os.path.join("Documentation", "Diagrams", "PNG", "06_Component_Diagram.png")
    if os.path.exists(img_comp):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_comp, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5.1.2: MindEase System Component Diagram")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    p = doc.add_paragraph(
        "The Component Diagram illustrates the internal architectural packages: the Flutter Mobile Client Package (Presentation, State BLoC, Audio Recorder, Sensor Manager, Dio API Client), "
        "the FastAPI Server Package (Gateway, Controllers for Stress, Diary, Baseline, Planner, Counselor, Community, and Payments), the ML Inference Cluster (Whisper ASR, Multimodal Classifier, SHAP Engine, Chatbot LLM), "
        "and the Supabase Persistence Layer (PostgreSQL Engine, GoTrue Auth, and S3 Media Storage)."
    )

    # Deployment Diagram
    img_dep = os.path.join("Documentation", "Diagrams", "PNG", "07_Deployment_Diagram.png")
    if os.path.exists(img_dep):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_dep, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5.1.3: MindEase UML Deployment Diagram")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    p = doc.add_paragraph(
        "The Deployment Diagram visualizes the physical nodes: the Android Smartphone client runtime running the compiled MindEase Flutter APK, "
        "the Cloud Application Server hosting the containerized FastAPI Python runtime and PyTorch inference engine over HTTPS/TLS 1.3, "
        "the managed Supabase Cloud Node hosting PostgreSQL 15 over TCP 5432, and the external Polar Payment Gateway node handling sandbox billing."
    )

    # -------------------------------------------------------------
    # 5.2 Logical Viewpoint (Class Diagram)
    # -------------------------------------------------------------
    doc.add_page_break()
    doc.add_heading("5.2 Logical Viewpoint", level=2)
    p = doc.add_paragraph(
        "The Logical Viewpoint provides an object-oriented structural model of the domain entities, attributes, methods, inheritance hierarchies, "
        "and multiplicity associations comprising the MindEase system."
    )

    img_class = os.path.join("Documentation", "Diagrams", "PNG", "08_Class_Diagram.png")
    if os.path.exists(img_class):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_class, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5.2.1: MindEase Domain UML Class Diagram")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    p = doc.add_paragraph(
        "The Class Diagram models core domain entities: the User base class with Student, Counselor, and Administrator subclasses; "
        "StressAssessment capturing multimodal classification results; XAIInsight encapsulating SHAP feature weights; "
        "DailyDiary managing encrypted content and sentiment scores; HabitLog recording lifestyle metrics; AdaptiveStudyPlan managing chunked study sessions; "
        "Appointment and ClinicalNote coordinating counseling workflows; PaymentTransaction tracking Polar billing references; and CommunityPost supporting peer interaction."
    )

    # -------------------------------------------------------------
    # 5.3 Information Viewpoint (DFDs, ERD, Schema)
    # -------------------------------------------------------------
    doc.add_page_break()
    doc.add_heading("5.3 Information Viewpoint", level=2)
    p = doc.add_paragraph(
        "The Information Viewpoint models the flow of data through the system and the logical and physical structures of stored entities. "
        "It includes Data Flow Diagrams (Context Level 0, Decomposition Level 1, and Detailed Level 2 for Stress Detection), the Crow's Foot Entity Relationship Diagram, "
        "and the physical relational database schema."
    )

    # DFD Level 0
    img_dfd0 = os.path.join("Documentation", "Diagrams", "PNG", "03_DFD_Level_0.png")
    if os.path.exists(img_dfd0):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_dfd0, width=Inches(6.0))
        p_cap = doc.add_paragraph("Figure 5.3.1: DFD Level 0 (Context Diagram) for MindEase System")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    # DFD Level 1
    img_dfd1 = os.path.join("Documentation", "Diagrams", "PNG", "04_DFD_Level_1.png")
    if os.path.exists(img_dfd1):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_dfd1, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5.3.2: DFD Level 1 Subsystem Functional Decomposition")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    # DFD Level 2
    img_dfd2 = os.path.join("Documentation", "Diagrams", "PNG", "05_DFD_Level_2_Stress_Detection.png")
    if os.path.exists(img_dfd2):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_dfd2, width=Inches(6.0))
        p_cap = doc.add_paragraph("Figure 5.3.3: DFD Level 2 Core Multimodal Stress Assessment & Fusion Pipeline")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    # ERD
    img_erd = os.path.join("Documentation", "Diagrams", "PNG", "09_Entity_Relationship_Diagram.png")
    if os.path.exists(img_erd):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_erd, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5.3.4: MindEase Entity Relationship Diagram (ERD) with Primary/Foreign Keys")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    # Database Schema
    img_sch = os.path.join("Documentation", "Diagrams", "PNG", "10_Database_Schema.png")
    if os.path.exists(img_sch):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_sch, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5.3.5: MindEase Relational Database Physical Schema Design")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    # -------------------------------------------------------------
    # 5.4 Interaction Viewpoint (CRITICAL: ALL 17 SEQUENCE DIAGRAMS)
    # -------------------------------------------------------------
    doc.add_page_break()
    doc.add_heading("5.4 Interaction Viewpoint", level=2)
    p = doc.add_paragraph(
        "The Interaction Viewpoint captures dynamic collaborations between actors and system components over time. "
        "To comply strictly with the project's core architectural standards, a dedicated Sequence Diagram is provided "
        "for every single identified Use Case, maintaining an exact 1-to-1 traceability mapping (17 Use Cases = 17 Sequence Diagrams). "
        "Below is the Traceability Matrix followed by each sequence diagram with its functional narrative."
    )

    doc.add_heading("Table 5.4.1: Use Case to Sequence Diagram Traceability Matrix", level=3)
    t_tm = doc.add_table(rows=len(uc_inventory)+1, cols=4)
    t_tm.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_tm)
    tm_headers = ["Use Case ID", "Use Case Name", "Sequence Diagram Figure", "Verification Status"]
    for ci, htext in enumerate(tm_headers):
        c = t_tm.rows[0].cells[ci]
        c.paragraphs[0].add_run(htext).bold = True
        set_cell_background(c, "1E3A8A")
        c.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        c.paragraphs[0].runs[0].font.size = Pt(9.5)

    for ri, (uid, uname, _, _) in enumerate(uc_inventory):
        row = t_tm.rows[ri+1]
        row.cells[0].paragraphs[0].add_run(uid).bold = True
        row.cells[1].paragraphs[0].add_run(uname)
        row.cells[2].paragraphs[0].add_run(f"Figure 5.4.{ri+1}")
        row.cells[3].paragraphs[0].add_run("Complete (100%)")
        for ci in range(4):
            row.cells[ci].paragraphs[0].runs[0].font.size = Pt(9)
            set_cell_background(row.cells[ci], "FFFFFF" if ri%2==0 else "F8FAFC")

    # Sequence Diagrams 1 to 17
    sd_descriptions = [
        ("Figure 5.4.1: Sequence Diagram for UC01 - Register & Create Profile",
         "UC01_Sequence_Diagram.png",
         "Illustrates the multi-role registration flow. The user submits details through AuthUI; AuthController validates input fields; SupabaseAuth creates authentication records; ProfileRepository stores role metadata; an alt fragment branches between successful pending registration and duplicate email error handling."),
        
        ("Figure 5.4.2: Sequence Diagram for UC02 - Login & Multi-Role Authentication",
         "UC02_Sequence_Diagram.png",
         "Depicts credential verification and multi-role routing. The user enters credentials; AuthController authenticates with SupabaseAuth; RoleManager inspects the assigned role (Student, Counselor, or Admin); an alt fragment handles successful session redirection vs invalid credential error display."),
        
        ("Figure 5.4.3: Sequence Diagram for UC03 - Complete Multilingual Stress Questionnaire",
         "UC03_Sequence_Diagram.png",
         "Demonstrates localized question loading in English, Urdu, or Roman Urdu. The student submits answers; an opt fragment invokes the AI Scoring Engine to suggest scores for custom written responses, allowing student confirmation before computing final PSS scores and saving records."),
        
        ("Figure 5.4.4: Sequence Diagram for UC04 - Record Daily Voice and Text Diary",
         "UC04_Sequence_Diagram.png",
         "Details the audio recording and transcription workflow. Voice audio is processed by Whisper ASR; NLPSafetyMonitor extracts sentiments and checks for crisis indicators; an opt fragment activates emergency helpline overlays if danger is detected; clean entries are encrypted with AES-256 and persisted."),
        
        ("Figure 5.4.5: Sequence Diagram for UC05 - Log Daily Habits & Calculate Stress Level",
         "UC05_Sequence_Diagram.png",
         "Models lifestyle metric logging (sleep, screen time, steps). HabitController gathers daily metrics, retrieves recent questionnaire and diary scores, and dispatches the combined feature vector to the Multimodal Fusion Model to classify stress as Low, Moderate, or High."),
        
        ("Figure 5.4.6: Sequence Diagram for UC06 - View Stress Trends & Baseline Trigger Analysis",
         "UC06_Sequence_Diagram.png",
         "Shows retrieval of longitudinal assessments over weekly or monthly ranges. BaselineAnalysisEngine calculates rolling baselines, detects trend trajectories (improving, stable, escalating), and overlays university exam dates to highlight academic triggers."),
        
        ("Figure 5.4.7: Sequence Diagram for UC07 - View Explainable AI Stress Insights",
         "UC07_Sequence_Diagram.png",
         "Illustrates Explainable AI generation. When the student clicks 'Why do I feel this way?', XAIController calls SHAPExplainerService to compute mathematical feature attributions, mapping top drivers (e.g., severe sleep deficit) to conversational insights and actionable recovery tips."),
        
        ("Figure 5.4.8: Sequence Diagram for UC08 - Access Relaxation Content & Rate Activity",
         "UC08_Sequence_Diagram.png",
         "Traces personalized media recommendation and efficacy evaluation. The student selects relaxing media, rates pre-activity stress (1-10), streams content, and rates post-activity stress (1-10); the system records delta stress relief to optimize future suggestions."),
        
        ("Figure 5.4.9: Sequence Diagram for UC09 - Chat with AI Conversational Assistant",
         "UC09_Sequence_Diagram.png",
         "Captures conversational support. The student sends text or voice prompts; the controller retrieves chat history and consented stress context; the LLM engine returns supportive responses; an opt fragment suggests counselor booking if elevated anxiety is detected."),
        
        ("Figure 5.4.10: Sequence Diagram for UC10 - Generate & Manage Adaptive Study Plan",
         "UC10_Sequence_Diagram.png",
         "Depicts adaptive Pomodoro generation. The student inputs study tasks and deadlines; AdaptivePlannerEngine checks real-time stress; an alt fragment schedules lighter 25-minute blocks with calming breaks for High stress, or standard 50-minute blocks for Low/Moderate stress."),
        
        ("Figure 5.4.11: Sequence Diagram for UC11 - Search Counselors & Request Appointment",
         "UC11_Sequence_Diagram.png",
         "Models counselor directory filtering and slot selection. FreeTierEligibilityRule verifies whether the student qualifies for a free triage session following High stress; an alt fragment confirms free booking immediately or initiates the Polar payment checkout flow."),
        
        ("Figure 5.4.12: Sequence Diagram for UC12 - Conduct Counseling Session & Maintain Notes",
         "UC12_Sequence_Diagram.png",
         "Illustrates session room management. AccessControlService checks student consent; if granted, the counselor reviews historical stress trends; following consultation, the counselor files encrypted clinical notes, archiving the appointment as Completed."),
        
        ("Figure 5.4.13: Sequence Diagram for UC13 - Process Appointment Payment via Polar",
         "UC13_Sequence_Diagram.png",
         "Details Polar sandbox payment processing. The student accesses the Polar checkout sheet; the backend ingests the asynchronous payment webhook, validates HMAC-SHA256 signatures, confirms the booking, and outputs a digital transaction receipt."),
        
        ("Figure 5.4.14: Sequence Diagram for UC14 - Create & Interact with Peer Community Posts",
         "UC14_Sequence_Diagram.png",
         "Traces peer message publication. ContentSafetyFilter screens text for toxicity; clean posts are published to the feed with optional anonymous pseudonyms; replies submitted by verified counselors automatically receive a distinct 'Counselor Badge'."),
        
        ("Figure 5.4.15: Sequence Diagram for UC15 - Report Inappropriate Community Post",
         "UC15_Sequence_Diagram.png",
         "Shows post flagging and quarantine. The student submits a violation report; ModerationQueueService increments the flag counter; an opt fragment temporarily hides the post from public view if the flag threshold is reached, queuing it for admin review."),
        
        ("Figure 5.4.16: Sequence Diagram for UC16 - Manage System Users & Counselor Approvals",
         "UC16_Sequence_Diagram.png",
         "Models administrative user supervision. The admin inspects pending counselor credential uploads; an alt fragment branches between approval (granting counselor permissions and sending notifications) and rejection (recording feedback reasons)."),
        
        ("Figure 5.4.17: Sequence Diagram for UC17 - Moderate Community Reports & System Content",
         "UC17_Sequence_Diagram.png",
         "Depicts administrative moderation and content management. The admin resolves flagged community tickets (deleting abusive posts or dismissing false alarms) and curates relaxation audio/video resources in the public media catalog.")
    ]

    for cap, png_name, narrative in sd_descriptions:
        doc.add_page_break()
        doc.add_heading(cap, level=3)
        png_path = os.path.join("Documentation", "Diagrams", "PNG", png_name)
        if os.path.exists(png_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            doc.add_picture(png_path, width=Inches(6.2))
            p_cap = doc.add_paragraph(cap)
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.runs[0].italic = True
            p_cap.runs[0].font.size = Pt(9.5)

        p_nar = doc.add_paragraph()
        r_nart = p_nar.add_run("Technical Workflow Narrative: ")
        r_nart.bold = True
        p_nar.add_run(narrative)

    # -------------------------------------------------------------
    # 5.5 State Dynamics Viewpoint
    # -------------------------------------------------------------
    doc.add_page_break()
    doc.add_heading("5.5 State Dynamics Viewpoint", level=2)
    p = doc.add_paragraph(
        "The State Dynamics Viewpoint models the operational states and transition events governing key system artifacts. "
        "MindEase models two critical lifecycles: the Stress Assessment Lifecycle (from input ingestion to XAI attribution and persistence) "
        "and the Counselor Appointment & Polar Payment Lifecycle (from booking request and eligibility evaluation through sandbox payment, session execution, and clinical archiving)."
    )

    img_sm = os.path.join("Documentation", "Diagrams", "PNG", "11_State_Machine_Diagram.png")
    if os.path.exists(img_sm):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(12)
        doc.add_picture(img_sm, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 5.5.1: State Machine Transition Diagrams for Stress Assessment and Appointment Lifecycles")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].italic = True
        p_cap.runs[0].font.size = Pt(9.5)

    # -------------------------------------------------------------
    # 5.6 Algorithm Viewpoint (All 5 Activity Diagrams)
    # -------------------------------------------------------------
    doc.add_page_break()
    doc.add_heading("5.6 Algorithm Viewpoint", level=2)
    p = doc.add_paragraph(
        "The Algorithm Viewpoint models the procedural control logic, decision branching, fork-join concurrencies, "
        "and exception paths for the core business algorithms of MindEase using UML Activity Diagrams."
    )

    activity_descriptions = [
        ("Figure 5.6.1: Activity Diagram for Multimodal Stress Assessment & Fusion Workflow",
         "AD01_Multimodal_Stress_Assessment_Workflow.png",
         "Models the concurrent ingestion of PSS questionnaire answers, voice/text diary reflections, and habit metrics via a fork bar, followed by feature normalization, multimodal ML model fusion, stress level branching (Low/Moderate vs High), counselor triage escalation, and SHAP feature attribution calculation."),
        
        ("Figure 5.6.2: Activity Diagram for Voice Diary Transcription, NLP Sentiment & Crisis Protocol",
         "AD02_Voice_Diary_Whisper_Analysis.png",
         "Illustrates audio capture, Whisper ASR speech-to-text conversion, NLP sentiment extraction, and decision logic for crisis detection; if danger keywords are flagged, the emergency crisis helpline overlay is immediately presented before encrypting and persisting the diary entry."),
        
        ("Figure 5.6.3: Activity Diagram for Adaptive Study and Recovery Planner",
         "AD03_Adaptive_Study_Planner.png",
         "Details task and deadline ingestion, real-time stress state evaluation, and branching into either a lightweight study schedule (25m focus with 15m mindfulness) or a standard Pomodoro schedule (50m study with 10m break), with end-of-day task roll-over capability."),
        
        ("Figure 5.6.4: Activity Diagram for Counselor Booking & Polar Payment Verification",
         "AD04_Counselor_Booking_Polar_Payment.png",
         "Captures counselor slot selection, free-tier triage eligibility evaluation, redirection to the Polar sandbox payment sheet for paid sessions, asynchronous webhook signature verification, and final booking confirmation dispatch."),
        
        ("Figure 5.6.5: Activity Diagram for Peer Community Post Creation & Moderation Workflow",
         "AD05_Community_Post_Moderation.png",
         "Demonstrates post composition, automated toxicity screening (rejecting profane content), publication to the live community feed, peer report logging, and administrative review and queue resolution.")
    ]

    for cap, png_name, narrative in activity_descriptions:
        doc.add_heading(cap, level=3)
        png_path = os.path.join("Documentation", "Diagrams", "PNG", png_name)
        if os.path.exists(png_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            doc.add_picture(png_path, width=Inches(6.0))
            p_cap = doc.add_paragraph(cap)
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.runs[0].italic = True
            p_cap.runs[0].font.size = Pt(9.5)

        p_nar = doc.add_paragraph()
        r_nart = p_nar.add_run("Process Workflow Narrative: ")
        r_nart.bold = True
        p_nar.add_run(narrative)
        doc.add_paragraph()

    # Save Word document
    docx_path = os.path.join("Documentation", "SRDS", "MindEase_SRDS_Specification.docx")
    doc.save(docx_path)
    print(f"Successfully generated DOCX SRDS at: {docx_path} ({os.path.getsize(docx_path)} bytes)")

    # -------------------------------------------------------------
    # 2. GENERATE MARKDOWN SRDS SPECIFICATION
    # -------------------------------------------------------------
    md_path = os.path.join("Documentation", "SRDS", "MindEase_SRDS_Specification.md")
    print("Writing complete Markdown SRDS Specification...")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Software Requirements Specification & Design Description (SRDS)\n\n")
        f.write("## MindEase: AI-Driven Stress Detection, Recovery & Support for Students\n\n")
        f.write("**COMSATS University Islamabad, Wah Campus**  \n")
        f.write("**Department of Computer Science**  \n")
        f.write("**Project Stream:** Mobile Apps Final Year Project (FYP)  \n")
        f.write("**Session:** FA23 — Fall 2026  \n\n")
        f.write("### Project Members:\n")
        f.write("1. **Muhammad Rehan Khalid** (CIIT/FA23-BCS-140/WAH)\n")
        f.write("2. **Umayya Wahid** (CIIT/FA23-BCS-172/WAH)\n\n")
        f.write("**Supervised By:** Ma'am Seema Islam\n\n")
        f.write("---\n\n")
        f.write("## Table of Contents\n")
        for title, page in toc_lines:
            f.write(f"- {title.strip()}\n")
        f.write("\n---\n\n")

        f.write("# 1 Introduction\n\n")
        f.write("## 1.1 System Introduction\n")
        f.write("MindEase is an AI-driven, comprehensive mobile mental health and academic stress management application designed specifically for university students in Pakistan. Undergraduates frequently encounter severe stress stemming from exams, deadlines, sleep deficits, and personal challenges. MindEase provides early detection, human-understandable Explainable AI (XAI) insights, personalized recovery content, adaptive study scheduling, conversational AI support, and direct access to university counselors.\n\n")

        f.write("## 1.2 Background of the System\n")
        f.write("Commercial wellness tools (Calm, Headspace, Wysa) fail to accommodate the regional linguistic reality of Pakistani students (Urdu, Roman Urdu) and treat mindfulness in total isolation from academic schedules. MindEase bridges these critical gaps through multilingual Whisper speech transcription, multimodal feature fusion, SHAP attribution, and integrated counselor appointments with guaranteed free triage.\n\n")

        f.write("## 1.3 Objectives of the System\n")
        f.write("### General Objective\nTo develop MindEase, an AI-based mobile app helping students understand, detect, and actively manage stress with explainable root causes, progress tracking, relaxation activities, adaptive study planning, and counselor access.\n\n")
        f.write("### Specific Objectives\n")
        for obj in objectives:
            f.write(f"- {obj}\n")
        f.write("\n")

        f.write("## 1.4 Significance of the System\n")
        f.write("MindEase delivers early stress intervention, destigmatizes mental healthcare through privacy-first digital engagement, bridges language barriers via Urdu/Roman Urdu NLP, and connects students seamlessly to university counselors.\n\n")

        f.write("# 2 Overall Description\n\n")
        f.write("## 2.1 Product Perspective\n")
        f.write("MindEase operates across a multi-tier client-server architecture: Flutter Mobile Client, FastAPI Backend Application Server, ML Inference Micro-services (Whisper ASR, Multimodal PyTorch classifier, SHAP explainer), Supabase Cloud PostgreSQL, and Polar Payment Gateway.\n\n")
        f.write("![Figure 2.1.1: System Architecture](../Diagrams/PNG/01_System_Architecture.png)\n\n")

        f.write("## 2.2 Product Scope\n")
        f.write("- **In Scope:** Multilingual questionnaire, voice/text daily diary with safety crisis checks, habit tracking, multimodal stress classification (Low/Moderate/High), SHAP XAI factor attribution, adaptive study planning, relaxation content library, AI chatbot, counselor booking with free triage, Polar billing, and community support.\n")
        f.write("- **Out of Scope (Medical Disclaimer):** MindEase is not a certified diagnostic device and does not issue medical diagnoses or prescribe psychiatric medication.\n\n")

        f.write("## 2.3 Product Functionality\n")
        for m_title, m_det in modules_desc:
            f.write(f"### {m_title}\n{m_det}\n\n")

        f.write("## 2.4 Users and Characteristics\n")
        for u_name, u_det in users_info:
            f.write(f"- **{u_name}:** {u_det}\n")
        f.write("\n")

        f.write("## 2.5 Operating Environment\n")
        f.write("Android 9.0+ smartphones (2 GB RAM min), Ubuntu Linux 22.04 LTS cloud server, Python 3.11+, FastAPI, Supabase PostgreSQL 15, and Polar sandbox.\n\n")

        f.write("# 3 Specific Requirements\n\n")
        f.write("## 3.1 Functional Requirements\n")
        for sec_title, fr_list in fr_sections:
            f.write(f"### {sec_title}\n")
            for fid, ftext in fr_list:
                f.write(f"- **[{fid}]** {ftext}\n")
            f.write("\n")

        f.write("## 3.2 Behaviour Requirements\n\n")
        f.write("![Figure 3.2.1: Use Case Diagram](../Diagrams/PNG/02_Use_Case_Diagram.png)\n\n")
        f.write("### System Use Case Inventory\n")
        f.write("| Use Case ID | Use Case Name | Actors | Scope Summary |\n|:---:|:---|:---|:---|\n")
        for uid, uname, uact, udesc in uc_inventory:
            f.write(f"| **{uid}** | {uname} | {uact} | {udesc} |\n")
        f.write("\n")

        f.write("### Fully Dressed Use Cases\n\n")
        for uc in fully_dressed_data:
            f.write(f"#### {uc['title']}\n\n")
            f.write("| Field | Details |\n|---|---|\n")
            f.write(f"| **Primary Actors** | {uc['primary']} |\n")
            f.write(f"| **Secondary Actors** | {uc['secondary']} |\n")
            f.write(f"| **Description** | {uc['desc']} |\n")
            f.write(f"| **Pre-Condition** | {uc['pre']} |\n")
            f.write(f"| **Steps** | {'<br>'.join(uc['steps'])} |\n")
            f.write(f"| **Post-Condition** | {uc['post']} |\n")
            f.write(f"| **Exceptions** | {uc['exceptions']} |\n")
            f.write(f"| **Relationships** | {uc['rel']} |\n\n")

        f.write("## 3.3 External Interface Requirements\n\n")
        f.write("### 3.3.1 User Interfaces\nMaterial 3 Flutter interface, calm palette, paginated questionnaire, audio waveform recorder, XAI bottom sheet, Pomodoro study timeline, and counselor directory.\n\n")
        f.write("### 3.3.2 Hardware Interfaces\nMicrophone (16kHz PCM), Android step sensor, screen time usage manager, and flash storage.\n\n")
        f.write("### 3.3.3 Software Interfaces\nSupabase Auth/DB, Whisper ASR, PyTorch classifier, SHAP explainer, and Polar sandbox API.\n\n")
        f.write("### 3.3.4 Communications Interfaces\nHTTPS TLS 1.3 REST endpoints, Secure WebSockets (WSS), and HMAC-SHA256 verified webhooks.\n\n")

        f.write("# 4 Other Non-functional Requirements\n\n")
        f.write("## 4.1 Performance Requirements\nAPI latency <500ms, Whisper transcription <2.5s, SHAP explanation <1.0s, 500 concurrent connections.\n\n")
        f.write("## 4.2 Safety and Security Requirements\nAutomated self-harm crisis triage, AES-256 encrypted diary storage, zero administrative access to private diaries, Row Level Security, and zero credit card storage.\n\n")
        f.write("## 4.3 Software Quality Attributes\nReliability (99.9% uptime, offline caching), 24/7 availability, WCAG 2.1 AA usability, modular maintainability, cross-platform portability, and GDPR-aligned data privacy.\n\n")

        f.write("# 5 Design Description\n\n")
        f.write("## 5.1 Composite Viewpoint\n\n")
        f.write("![Figure 5.1.2: Component Diagram](../Diagrams/PNG/06_Component_Diagram.png)\n\n")
        f.write("![Figure 5.1.3: Deployment Diagram](../Diagrams/PNG/07_Deployment_Diagram.png)\n\n")

        f.write("## 5.2 Logical Viewpoint\n\n")
        f.write("![Figure 5.2.1: Class Diagram](../Diagrams/PNG/08_Class_Diagram.png)\n\n")

        f.write("## 5.3 Information Viewpoint\n\n")
        f.write("![Figure 5.3.1: DFD Level 0](../Diagrams/PNG/03_DFD_Level_0.png)\n\n")
        f.write("![Figure 5.3.2: DFD Level 1](../Diagrams/PNG/04_DFD_Level_1.png)\n\n")
        f.write("![Figure 5.3.3: DFD Level 2](../Diagrams/PNG/05_DFD_Level_2_Stress_Detection.png)\n\n")
        f.write("![Figure 5.3.4: ERD](../Diagrams/PNG/09_Entity_Relationship_Diagram.png)\n\n")
        f.write("![Figure 5.3.5: Database Schema](../Diagrams/PNG/10_Database_Schema.png)\n\n")

        f.write("## 5.4 Interaction Viewpoint\n\n")
        f.write("### Table 5.4.1: Use Case to Sequence Diagram Traceability Matrix\n\n")
        f.write("| Use Case ID | Use Case Name | Sequence Diagram Figure | Verification Status |\n|:---:|:---|:---:|:---:|\n")
        for ri, (uid, uname, _, _) in enumerate(uc_inventory):
            f.write(f"| **{uid}** | {uname} | Figure 5.4.{ri+1} | Complete (100%) |\n")
        f.write("\n")

        for cap, png_name, narrative in sd_descriptions:
            f.write(f"### {cap}\n\n")
            f.write(f"![{cap}](../Diagrams/PNG/{png_name})\n\n")
            f.write(f"**Technical Workflow Narrative:** {narrative}\n\n")

        f.write("## 5.5 State Dynamics Viewpoint\n\n")
        f.write("![Figure 5.5.1: State Machine Diagram](../Diagrams/PNG/11_State_Machine_Diagram.png)\n\n")

        f.write("## 5.6 Algorithm Viewpoint\n\n")
        for cap, png_name, narrative in activity_descriptions:
            f.write(f"### {cap}\n\n")
            f.write(f"![{cap}](../Diagrams/PNG/{png_name})\n\n")
            f.write(f"**Process Workflow Narrative:** {narrative}\n\n")

    print(f"Successfully generated Markdown SRDS at: {md_path} ({os.path.getsize(md_path)} bytes)")

if __name__ == "__main__":
    build_srds()
