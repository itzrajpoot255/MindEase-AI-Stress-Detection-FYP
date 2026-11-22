# MindEase: AI-Driven Stress Detection, Recovery & Support for Students

[![Final Year Project](https://img.shields.io/badge/FYP-FA23--Fall2026-blue.svg)](https://www.comsats.edu.pk/)
[![Department](https://img.shields.io/badge/Department-Computer%20Science-navy.svg)](https://wah.comsats.edu.pk/)
[![Campus](https://img.shields.io/badge/Institution-COMSATS%20University%20Islamabad%20(Wah%20Campus)-green.svg)](https://wah.comsats.edu.pk/)
[![Status](https://img.shields.io/badge/Documentation-SRDS%20Complete-brightgreen.svg)]()
[![Diagrams](https://img.shields.io/badge/UML%20Diagrams-43%20Verified%20(300%20DPI)-orange.svg)]()

> **Final Year Project (FYP) Software Requirements and Design Specification (SRDS)**  
> **Stream:** Mobile Apps FYPs  
> **Institution:** Department of Computer Science, COMSATS University Islamabad, Wah Campus  

---

## 👥 Project Team & Supervision

| Role | Name | Registration Number | Module Ownership |
|:---|:---|:---|:---|
| **Student 1** | **Muhammad Rehan Khalid** | `CIIT/FA23-BCS-140/WAH` | Modules 1, 2, 5, 7, 10, 12 |
| **Student 2** | **Umayya Wahid** | `CIIT/FA23-BCS-172/WAH` | Modules 3, 4, 6, 8, 9, 11 |
| **Supervisor** | **Ma'am Seema Islam** | Faculty Supervisor | Project Mentorship & Guidance |

---

## 🌟 Executive Summary

**MindEase** is an AI-driven, comprehensive mobile mental health and academic stress management platform designed specifically for university students in Pakistan. Undergraduates frequently encounter severe stress stemming from examinations, assignment deadlines, irregular sleep cycles, and daily life pressures. Many students do not recognize their escalating stress until it adversely impacts their health and academic performance, and seeking professional help is often hindered by social stigma, cost, or counselor unavailability.

MindEase resolves these challenges by uniting:
1. **Multilingual Psychometric Assessment:** Validated questionnaires available in English, Urdu, and Roman Urdu with AI text scoring.
2. **Multimodal Daily Diary:** Voice and text check-ins transcribed via Whisper ASR, analyzed for emotional sentiment, with automated crisis/self-harm safety triage.
3. **Passive & Behavioral Habit Tracking:** Logging sleep duration, screen time, and daily step counts with missing value imputation.
4. **Multimodal Stress Fusion:** Machine learning models that classify stress into Low, Moderate, or High tiers.
5. **Explainable AI (XAI):** Plain-language explanations of primary stress drivers powered by SHAP (SHapley Additive exPlanations).
6. **Adaptive Study & Recovery Planner:** Generating daily Pomodoro study sessions that dynamically compress focus intervals and schedule relaxation breaks during elevated stress.
7. **Personalized Recovery Content:** Calming music, stories, videos, breathing exercises, and spiritual recitations with pre/post activity efficacy tracking.
8. **24/7 Conversational AI:** Empathetic chat companion with context-aware support.
9. **Verified Counselor Portal:** Session scheduling with one guaranteed **free** appointment following High stress detection and subsequent paid sessions verified via **Polar** sandbox payment webhooks.
10. **Peer Community & Administration:** Safe, supportive peer forums with anonymous posting, counselor response badges, profanity filtering, and privacy-preserving administrative moderation.

---

## 🏛️ System Architecture

MindEase is built on an enterprise multi-tier architecture ensuring data privacy, high availability, and rapid machine learning inference:

```
+-----------------------------------------------------------------------------------+
|                        PRESENTATION TIER (Flutter Mobile App)                     |
|  - Student Mobile View   - Counselor Portal View   - Admin Telemetry View         |
|  - Audio Recording (PCM) - Sensor Step Collector   - BLoC State Management        |
+-----------------------------------------------------------------------------------+
                                         │
                 HTTPS / WSS (TLS 1.3)   ▼   JSON REST Endpoints
+-----------------------------------------------------------------------------------+
|                     APPLICATION TIER (FastAPI Python Backend)                     |
|  - Auth & RBAC Guard    - Questionnaire Service    - Diary & Safety Pipeline      |
|  - Habit Fusion Router  - Baseline Trigger Engine  - Adaptive Study Planner       |
|  - Counselor Booking    - Community Moderation     - Polar Webhook Verifier       |
+-----------------------------------------------------------------------------------+
             │                                                 │
             ▼ Internal Pipelines                              ▼ TCP 5432 (SSL)
+-----------------------------------------+   +-------------------------------------+
|        AI & MACHINE LEARNING TIER       |   |       PERSISTENCE TIER (Supabase)   |
|  - Whisper ASR (Speech-to-Text)         |   |  - PostgreSQL 15 Relational DB      |
|  - Multimodal Stress Classifier         |   |  - GoTrue JWT Authentication        |
|  - SHAP Explainability Engine           |   |  - Row Level Security (RLS)         |
|  - Conversational LLM / Transformers    |   |  - AES-256 Encrypted Diary Store    |
|  - Content Toxicity & Sentiment NLP     |   |  - S3-Compatible Media Storage      |
+-----------------------------------------+   +-------------------------------------+
                                         │
                                         ▼ HTTPS REST
+-----------------------------------------------------------------------------------+
|                         EXTERNAL GATEWAY TIER (Polar Sandbox)                     |
|  - Test-Mode Card Checkout Sheets      - Webhook HMAC-SHA256 Signature Validator  |
+-----------------------------------------------------------------------------------+
```

---

## 📊 Complete Diagram Inventory (43 Verified Diagrams)

All diagrams adhere strictly to university academic standards: pure white background (`#FFFFFF`), high-contrast professional styling, clean UML notation, and zero overlapping elements. Every diagram is available in five (5) distinct deliverable formats:

1. **Draw.io Native Editable (`.drawio`)** in `Documentation/Diagrams/Editable/`
2. **Microsoft Visio Compatible (`.drawio`)** in `Documentation/Diagrams/Visio/`
3. **W3C Standard Vector SVG (`.svg`)** in `Documentation/Diagrams/SVG/`
4. **High-Resolution 300 DPI PNG (`.png`)** in `Documentation/Diagrams/PNG/`
5. **Print-Ready Vector PDF (`.pdf`)** in `Documentation/Diagrams/PDF/` and compiled in `All_MindEase_Diagrams.pdf`.

### 1. System Architecture & UML Structural Diagrams
- `01_System_Architecture`: Multi-tier distributed architecture.
- `02_Use_Case_Diagram`: Complete system boundary, 3 human actors, 4 system actors, and all 17 use cases.
- `03_DFD_Level_0`: Context diagram with external entities and data flows.
- `04_DFD_Level_1`: Functional decomposition across all 12 modules and 6 major data stores.
- `05_DFD_Level_2_Stress_Detection`: Granular Level 2 data flow for multimodal stress fusion and SHAP attribution.
- `06_Component_Diagram`: UML component packages (Client, Server, AI, Persistence).
- `07_Deployment_Diagram`: Physical nodes, artifacts, execution environments, and network protocols.
- `08_Class_Diagram`: Domain class diagram showing attributes, operations, inheritance, and multiplicities.
- `09_Entity_Relationship_Diagram`: Crow's Foot ERD with primary/foreign keys and cardinalities.
- `10_Database_Schema`: Relational schema design with PostgreSQL data types and constraints.
- `11_State_Machine_Diagram`: Dual state machine modeling stress assessment and appointment/payment lifecycles.

### 2. Activity Diagrams (Algorithm & Workflow Viewpoint)
- `AD01_Multimodal_Stress_Assessment_Workflow`: Multimodal ingestion fork-join and stress triage logic.
- `AD02_Voice_Diary_Whisper_Analysis`: Audio capture, Whisper STT, sentiment analysis, and crisis safety protocol.
- `AD03_Adaptive_Study_Planner`: Study task intake and stress-adaptive Pomodoro generation.
- `AD04_Counselor_Booking_Polar_Payment`: Free tier evaluation, Polar sandbox checkout, and webhook verification.
- `AD05_Community_Post_Moderation`: Post publishing, automated toxicity filtering, and administrative queue triage.

### 3. UML Sequence Diagrams (1:1 Use Case Mapping)
In strict accordance with the mandatory project requirement, **every single Use Case has exactly one corresponding Sequence Diagram**:

| Use Case ID | Use Case Name | Sequence Diagram File | Traceability Figure |
|:---:|:---|:---|:---:|
| **UC01** | Register & Create Profile | `UC01_Sequence_Diagram.drawio` | Figure 5.4.1 |
| **UC02** | Login & Multi-Role Authentication | `UC02_Sequence_Diagram.drawio` | Figure 5.4.2 |
| **UC03** | Complete Multilingual Stress Questionnaire | `UC03_Sequence_Diagram.drawio` | Figure 5.4.3 |
| **UC04** | Record Daily Voice and Text Diary | `UC04_Sequence_Diagram.drawio` | Figure 5.4.4 |
| **UC05** | Log Daily Habits & Calculate Stress Level | `UC05_Sequence_Diagram.drawio` | Figure 5.4.5 |
| **UC06** | View Stress Trends & Baseline Trigger Analysis | `UC06_Sequence_Diagram.drawio` | Figure 5.4.6 |
| **UC07** | View Explainable AI Stress Insights | `UC07_Sequence_Diagram.drawio` | Figure 5.4.7 |
| **UC08** | Access Relaxation Content & Rate Activity | `UC08_Sequence_Diagram.drawio` | Figure 5.4.8 |
| **UC09** | Chat with AI Conversational Assistant | `UC09_Sequence_Diagram.drawio` | Figure 5.4.9 |
| **UC10** | Generate & Manage Adaptive Study Plan | `UC10_Sequence_Diagram.drawio` | Figure 5.4.10 |
| **UC11** | Search Counselors & Request Appointment | `UC11_Sequence_Diagram.drawio` | Figure 5.4.11 |
| **UC12** | Conduct Counseling Session & Maintain Notes | `UC12_Sequence_Diagram.drawio` | Figure 5.4.12 |
| **UC13** | Process Appointment Payment via Polar | `UC13_Sequence_Diagram.drawio` | Figure 5.4.13 |
| **UC14** | Create & Interact with Peer Community Posts | `UC14_Sequence_Diagram.drawio` | Figure 5.4.14 |
| **UC15** | Report Inappropriate Community Post | `UC15_Sequence_Diagram.drawio` | Figure 5.4.15 |
| **UC16** | Manage System Users & Counselor Approvals | `UC16_Sequence_Diagram.drawio` | Figure 5.4.16 |
| **UC17** | Moderate Community Reports & System Content | `UC17_Sequence_Diagram.drawio` | Figure 5.4.17 |

### 4. UI Screen Wireframe Diagrams (Material 3 Visual Interface Design)
To satisfy the official university SRDS List of Figures, 10 high-fidelity user interface wireframes were architected according to Google Material 3 standards and mental health UI guidelines:

| Wireframe ID | Screen Name | Diagram Reference | Key Elements |
|:---:|:---|:---|:---|
| **WF01** | Landing & Onboarding Screen | `WF01_Landing_Onboarding_Screen.drawio` | Value propositions, multi-tier trust badges, primary student CTAs |
| **WF02** | Student & Counselor Sign Up | `WF02_Sign_Up_Screen.drawio` | Role selection toggle, university domain email check, password meter |
| **WF03** | Log In & Multi-Factor Auth | `WF03_Log_In_Screen.drawio` | Credential inputs, biometric login option, password reset link |
| **WF04** | Student Core Dashboard | `WF04_Student_Dashboard_Screen.drawio` | Stress score dial (0-100), baseline HRV chart, quick-checkin card |
| **WF05** | Multilingual Questionnaire | `WF05_Multilingual_Questionnaire_Screen.drawio` | PSS-10 / DASS-21 Likert slider, EN/UR toggle, question pagination |
| **WF06** | Voice Diary & Audio Studio | `WF06_Voice_Diary_Screen.drawio` | Real-time audio waveform recorder, Whisper transcription preview |
| **WF07** | Explainable AI (XAI) Modal | `WF07_XAI_Insights_Screen.drawio` | SHAP feature contribution bar chart, plain-language student advice |
| **WF08** | Adaptive Pomodoro Planner | `WF08_Adaptive_Study_Planner_Screen.drawio` | Stress-calibrated work/rest intervals, active study task tracker |
| **WF09** | Counselor Booking Directory | `WF09_Counselor_Booking_Screen.drawio` | Verified practitioner cards, time-slot selector, Polar sandbox checkout |
| **WF10** | Anonymous Peer Community | `WF10_Peer_Community_Feed_Screen.drawio` | Anonymous posting interface, crisis detection banner, empathy reaction chips |

---

## 📁 Repository Directory Structure

```
FYP_Project/
├── Documentation/
│   ├── SRDS/
│   │   ├── MindEase_SRDS_Specification.docx    # Complete University Formatted Word Doc (11.1 MB)
│   │   └── MindEase_SRDS_Specification.md      # Full Markdown Specification Document (60 KB)
│   ├── Diagrams/
│   │   ├── Editable/                           # 43 Native Draw.io XML files (.drawio)
│   │   ├── Visio/                              # 33 Microsoft Visio-compatible files (.drawio)
│   │   ├── SVG/                                # 43 Scalable Vector Graphics (.svg)
│   │   ├── PNG/                                # 43 High-Resolution 300 DPI PNGs (.png)
│   │   └── PDF/                                # 43 Single-page PDFs + All_MindEase_Diagrams.pdf (6.93 MB)
│   ├── Reports/
│   │   ├── Traceability_Matrix.md              # 1:1 Use Case to Sequence Diagram Audit Matrix
│   │   └── QA_Verification_Report.md           # Technical Verification & Quality Sign-Off Report
│   └── References/                             # Reference materials and guidelines
├── Dataset_Documentation/
│   └── README.md                               # Psychometric scales, Whisper acoustic data, habit metrics
├── Hardware_Documentation/
│   └── README.md                               # Mobile microphone, pedometer sensors, UsageStats telemetry
├── Source_Code/                                # Application codebase repository root
├── scripts/                                    # Automated diagram generation & rendering pipelines
├── .gitignore                                  # Standard Git exclusion filters
└── README.md                                   # Master project overview & index
```

---

## 🛠️ Technology Stack

| Layer | Technologies & Tools |
|:---|:---|
| **Mobile Client** | Flutter 3.x, Dart, Android Studio, VS Code, BLoC State Management, Dio HTTP |
| **Backend Server** | Python 3.11, FastAPI, Uvicorn ASGI Server, Pydantic, Postman |
| **AI & Machine Learning** | OpenAI Whisper ASR, PyTorch, Scikit-learn, Hugging Face Transformers, SHAP XAI |
| **Database & Auth** | Supabase Cloud, PostgreSQL 15, GoTrue Auth, Row-Level Security (RLS), AES-256 Storage |
| **Payments** | Polar Payment Gateway (Sandbox Mode), HMAC-SHA256 Webhooks |
| **Diagramming & Design** | Draw.io (diagrams.net), Microsoft Visio XML, PyMuPDF, W3C SVG |

---

## 🚀 Quality Assurance Sign-Off
All 33 UML diagrams and the complete Software Requirements and Design Specification document have been verified for internal consistency, academic rigor, technical fidelity to the FYP Proposal, and strict adherence to the university template.
