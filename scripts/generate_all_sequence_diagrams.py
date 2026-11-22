"""
Generates all 17 Sequence Diagrams for MindEase FYP SRDS
Strict 1-to-1 mapping with the 17 identified Use Cases (UC01 to UC17).
Generates SVG and Draw.io files.
"""
import os
from sequence_diagram_engine import SequenceDiagramRenderer

def get_sequence_diagram_definitions():
    diagrams = []

    # UC01
    diagrams.append({
        "id": "UC01",
        "title": "UC01: Register & Create Profile",
        "caption": "Figure 5.4.1: Sequence Diagram for Register & Create Profile",
        "participants": [
            ("user", "Student / Counselor", True),
            ("ui", "AuthUI", False),
            ("ctrl", "AuthController", False),
            ("auth", "SupabaseAuth", False),
            ("repo", "ProfileRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "user", "to": "ui", "text": "register(name, email, password, role)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "submitRegistration(userData)"},
            {"type": "self", "from": "ctrl", "text": "validateFields()"},
            {"type": "call", "from": "ctrl", "to": "auth", "text": "signUp(email, password)"},
            {"type": "frag_start", "kind": "alt", "condition": "[valid registration data]"},
            {"type": "return", "from": "auth", "to": "ctrl", "text": "authSuccess(userId)"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "createProfile(userId, role, profileData)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "profileCreated()"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "registrationPending(verifyEmail)"},
            {"type": "return", "from": "ui", "to": "user", "text": "displaySuccessPrompt()"},
            {"type": "frag_divider", "condition": "[email already registered or invalid fields]"},
            {"type": "return", "from": "auth", "to": "ctrl", "text": "authError(duplicateEmail)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "registrationFailed(errorMsg)"},
            {"type": "return", "from": "ui", "to": "user", "text": "displayErrorMessage()"},
            {"type": "frag_end"}
        ]
    })

    # UC02
    diagrams.append({
        "id": "UC02",
        "title": "UC02: Login & Multi-Role Authentication",
        "caption": "Figure 5.4.2: Sequence Diagram for Login & Multi-Role Authentication",
        "participants": [
            ("user", "User (All Roles)", True),
            ("ui", "LoginUI", False),
            ("ctrl", "AuthController", False),
            ("auth", "SupabaseAuth", False),
            ("role", "RoleManager", False)
        ],
        "steps": [
            {"type": "call", "from": "user", "to": "ui", "text": "login(email, password)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "authenticate(email, password)"},
            {"type": "call", "from": "ctrl", "to": "auth", "text": "signInWithPassword(email, password)"},
            {"type": "frag_start", "kind": "alt", "condition": "[valid credentials]"},
            {"type": "return", "from": "auth", "to": "ctrl", "text": "sessionToken(userId)"},
            {"type": "call", "from": "ctrl", "to": "role", "text": "getUserRole(userId)"},
            {"type": "return", "from": "role", "to": "ctrl", "text": "assignedRole(Student | Counselor | Admin)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "authSuccess(role, session)"},
            {"type": "return", "from": "ui", "to": "user", "text": "redirectRoleDashboard(role)"},
            {"type": "frag_divider", "condition": "[invalid credentials or unverified account]"},
            {"type": "return", "from": "auth", "to": "ctrl", "text": "authFailed(invalidCredentials)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "loginError(reason)"},
            {"type": "return", "from": "ui", "to": "user", "text": "displayLoginError()"},
            {"type": "frag_end"}
        ]
    })

    # UC03
    diagrams.append({
        "id": "UC03",
        "title": "UC03: Complete Multilingual Stress Questionnaire",
        "caption": "Figure 5.4.3: Sequence Diagram for Complete Multilingual Stress Questionnaire",
        "participants": [
            ("student", "Student", True),
            ("ui", "QuestionnaireUI", False),
            ("ctrl", "QuestionnaireController", False),
            ("ai", "ScoringEngine", False),
            ("repo", "StressRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "student", "to": "ui", "text": "selectLanguage(English | Urdu | RomanUrdu)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "loadLocalizedQuestions(langCode)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "questionSet(items)"},
            {"type": "call", "from": "student", "to": "ui", "text": "submitResponses(answers, customText)"},
            {"type": "frag_start", "kind": "opt", "condition": "[contains custom written response]"},
            {"type": "call", "from": "ui", "to": "ai", "text": "estimateTextScore(customText, langCode)"},
            {"type": "return", "from": "ai", "to": "ui", "text": "suggestedScore(value)"},
            {"type": "call", "from": "student", "to": "ui", "text": "confirmOrAdjustScore(confirmedScore)"},
            {"type": "frag_end"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "computeFinalScore(confirmedResponses)"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "saveQuestionnaireResult(studentId, pssScore)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "saved(resultId)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "questionnaireSummary(pssScore, level)"},
            {"type": "return", "from": "ui", "to": "student", "text": "displayQuestionnaireResult()"}
        ]
    })

    # UC04
    diagrams.append({
        "id": "UC04",
        "title": "UC04: Record Daily Voice and Text Diary",
        "caption": "Figure 5.4.4: Sequence Diagram for Record Daily Voice and Text Diary",
        "participants": [
            ("student", "Student", True),
            ("ui", "DiaryUI", False),
            ("ctrl", "DiaryController", False),
            ("whisper", "WhisperASREngine", False),
            ("nlp", "NLPSafetyMonitor", False),
            ("repo", "DiaryRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "student", "to": "ui", "text": "recordVoiceOrText(audioStream | textEntry)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "submitDiaryEntry(mediaPayload, langCode)"},
            {"type": "frag_start", "kind": "opt", "condition": "[audio voice input]"},
            {"type": "call", "from": "ctrl", "to": "whisper", "text": "transcribeSpeech(audioBytes, langCode)"},
            {"type": "return", "from": "whisper", "to": "ctrl", "text": "transcribedText(text)"},
            {"type": "frag_end"},
            {"type": "call", "from": "ctrl", "to": "nlp", "text": "analyzeSentimentAndSafety(text)"},
            {"type": "return", "from": "nlp", "to": "ctrl", "text": "analysisResult(sentimentScore, topics, isDanger)"},
            {"type": "frag_start", "kind": "opt", "condition": "[isDanger == true]"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "showCrisisSupportAlert()"},
            {"type": "return", "from": "ui", "to": "student", "text": "renderHelplineAndCounselorPrompt()"},
            {"type": "frag_end"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "saveDiary(studentId, encryptedText, sentimentScore)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "diarySaved(entryId)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "entryLoggedConfirmation(topics, sentimentScore)"},
            {"type": "return", "from": "ui", "to": "student", "text": "displayDailyDiarySummary()"}
        ]
    })

    # UC05
    diagrams.append({
        "id": "UC05",
        "title": "UC05: Log Daily Habits & Calculate Stress Level",
        "caption": "Figure 5.4.5: Sequence Diagram for Log Daily Habits & Calculate Stress Level",
        "participants": [
            ("student", "Student", True),
            ("ui", "HabitUI", False),
            ("ctrl", "HabitController", False),
            ("fusion", "MultimodalFusionEngine", False),
            ("repo", "StressRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "student", "to": "ui", "text": "inputHabits(sleepHours, screenTime, steps)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "processHabitMetrics(habitData)"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "getRecentQuestionnaireAndDiaryScores(studentId)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "priorScores(pssScore, diaryScore)"},
            {"type": "call", "from": "ctrl", "to": "fusion", "text": "combineFeatures(habits, pssScore, diaryScore)"},
            {"type": "self", "from": "fusion", "text": "predictStressLevel(featureVector)"},
            {"type": "return", "from": "fusion", "to": "ctrl", "text": "stressPrediction(Low | Moderate | High, conf)"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "saveDailyAssessment(studentId, stressLevel, vector)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "assessmentStored(assessmentId)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "displayStressLevel(stressLevel, confidence)"},
            {"type": "return", "from": "ui", "to": "student", "text": "renderStressAssessmentResult()"}
        ]
    })

    # UC06
    diagrams.append({
        "id": "UC06",
        "title": "UC06: View Stress Trends & Baseline Trigger Analysis",
        "caption": "Figure 5.4.6: Sequence Diagram for View Stress Trends & Baseline Trigger Analysis",
        "participants": [
            ("student", "Student", True),
            ("ui", "TrendsUI", False),
            ("ctrl", "TrendsController", False),
            ("engine", "BaselineAnalysisEngine", False),
            ("repo", "StressRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "student", "to": "ui", "text": "selectTrendRange(Weekly | Monthly)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "fetchTrendData(studentId, timeRange)"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "getAssessmentHistory(studentId, timeRange)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "assessmentRecords(history)"},
            {"type": "call", "from": "ctrl", "to": "engine", "text": "calculateBaselinePattern(history)"},
            {"type": "self", "from": "engine", "text": "correlateEvents(examMarkers, stressSpikes)"},
            {"type": "return", "from": "engine", "to": "ctrl", "text": "trendAnalytics(trajectory, baselineDiff, summary)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "renderGraphsAndSummary(trendAnalytics)"},
            {"type": "return", "from": "ui", "to": "student", "text": "displayTrendCharts()"}
        ]
    })

    # UC07
    diagrams.append({
        "id": "UC07",
        "title": "UC07: View Explainable AI Stress Insights",
        "caption": "Figure 5.4.7: Sequence Diagram for View Explainable AI Stress Insights",
        "participants": [
            ("student", "Student", True),
            ("ui", "XAI_UI", False),
            ("ctrl", "XAIController", False),
            ("shap", "SHAPExplainerService", False),
            ("recom", "ActionableRecommender", False)
        ],
        "steps": [
            {"type": "call", "from": "student", "to": "ui", "text": "requestExplanation(assessmentId)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "getFeatureExplanation(assessmentId)"},
            {"type": "call", "from": "ctrl", "to": "shap", "text": "computeSHAPValues(assessmentFeatures)"},
            {"type": "return", "from": "shap", "to": "ctrl", "text": "featureWeights(topFactors: sleep, screen, diary)"},
            {"type": "call", "from": "ctrl", "to": "recom", "text": "mapFactorsToActions(topFactors)"},
            {"type": "return", "from": "recom", "to": "ctrl", "text": "actionableSuggestions(recoveryTips)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "xaiInsights(chartData, factorSummary, actions)"},
            {"type": "return", "from": "ui", "to": "student", "text": "displayExplainabilityView()"}
        ]
    })

    # UC08
    diagrams.append({
        "id": "UC08",
        "title": "UC08: Access Relaxation Content & Rate Activity Effectiveness",
        "caption": "Figure 5.4.8: Sequence Diagram for Access Relaxation Content & Rate Activity Effectiveness",
        "participants": [
            ("student", "Student", True),
            ("ui", "ContentLibraryUI", False),
            ("ctrl", "RecommendationController", False),
            ("media", "MediaStreamingService", False),
            ("repo", "ActivityRatingRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "student", "to": "ui", "text": "browseRecommendations(stressLevel)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "getPersonalizedContent(studentId, stressLevel)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "contentList(music, stories, exercises, recitations)"},
            {"type": "call", "from": "student", "to": "ui", "text": "selectContentItem(contentId)"},
            {"type": "call", "from": "student", "to": "ui", "text": "ratePreStress(preRating: 1-10)"},
            {"type": "call", "from": "ui", "to": "media", "text": "streamAudioVideo(contentId)"},
            {"type": "return", "from": "media", "to": "ui", "text": "playbackFinished()"},
            {"type": "call", "from": "student", "to": "ui", "text": "ratePostStress(postRating: 1-10)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "recordRating(contentId, preRating, postRating)"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "saveRating(studentId, deltaStress)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "ratingSaved()"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "thankYouFeedback(deltaStress)"},
            {"type": "return", "from": "ui", "to": "student", "text": "displayRecoveryImpactSummary()"}
        ]
    })

    # UC09
    diagrams.append({
        "id": "UC09",
        "title": "UC09: Chat with AI Conversational Assistant",
        "caption": "Figure 5.4.9: Sequence Diagram for Chat with AI Conversational Assistant",
        "participants": [
            ("student", "Student", True),
            ("ui", "ChatbotUI", False),
            ("ctrl", "ChatbotController", False),
            ("llm", "LLMConversationalEngine", False),
            ("repo", "ChatRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "student", "to": "ui", "text": "sendMessage(textPrompt, langCode)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "processUserMessage(studentId, textPrompt)"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "getRecentChatContext(studentId)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "conversationHistory(history)"},
            {"type": "call", "from": "ctrl", "to": "llm", "text": "generateEmpatheticResponse(prompt, history)"},
            {"type": "return", "from": "llm", "to": "ctrl", "text": "llmReply(responseText, counselorPromptNeeded)"},
            {"type": "frag_start", "kind": "opt", "condition": "[high stress / counselor suggestion indicated]"},
            {"type": "self", "from": "ctrl", "text": "appendCounselorRecommendation()"},
            {"type": "frag_end"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "saveInteraction(studentId, textPrompt, llmReply)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "interactionSaved()"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "displayReply(llmReply)"},
            {"type": "return", "from": "ui", "to": "student", "text": "renderChatBubble()"}
        ]
    })

    # UC10
    diagrams.append({
        "id": "UC10",
        "title": "UC10: Generate & Manage Adaptive Study Plan",
        "caption": "Figure 5.4.10: Sequence Diagram for Generate & Manage Adaptive Study Plan",
        "participants": [
            ("student", "Student", True),
            ("ui", "StudyPlannerUI", False),
            ("ctrl", "StudyPlannerController", False),
            ("engine", "AdaptivePlannerEngine", False),
            ("repo", "StudyTaskRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "student", "to": "ui", "text": "enterStudyTasks(taskList, deadlines)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "generateDailySchedule(studentId, taskList)"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "getStudentStressLevel(studentId)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "currentStress(High | Moderate | Low)"},
            {"type": "call", "from": "ctrl", "to": "engine", "text": "createAdaptivePlan(taskList, currentStress)"},
            {"type": "frag_start", "kind": "alt", "condition": "[currentStress == High]"},
            {"type": "self", "from": "engine", "text": "scheduleLighterSessions(25min study, 15min rest)"},
            {"type": "frag_divider", "condition": "[currentStress == Low / Moderate]"},
            {"type": "self", "from": "engine", "text": "scheduleStandardSessions(50min study, 10min rest)"},
            {"type": "frag_end"},
            {"type": "return", "from": "engine", "to": "ctrl", "text": "optimizedSchedule(blocks)"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "saveSchedule(studentId, optimizedSchedule)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "planSaved()"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "renderDailySchedule(optimizedSchedule)"},
            {"type": "return", "from": "ui", "to": "student", "text": "displayScheduleWithBreaks()"}
        ]
    })

    # UC11
    diagrams.append({
        "id": "UC11",
        "title": "UC11: Search Counselors & Request Appointment",
        "caption": "Figure 5.4.11: Sequence Diagram for Search Counselors & Request Appointment",
        "participants": [
            ("student", "Student", True),
            ("ui", "CounselorDirectoryUI", False),
            ("ctrl", "AppointmentController", False),
            ("rules", "FreeTierEligibilityRule", False),
            ("repo", "AppointmentRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "student", "to": "ui", "text": "browseCounselors(filterCriteria)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "getCounselorDirectory(filterCriteria)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "counselorList(profiles, availableSlots)"},
            {"type": "call", "from": "student", "to": "ui", "text": "selectSlot(counselorId, slotTime)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "requestBooking(studentId, counselorId, slotTime)"},
            {"type": "call", "from": "ctrl", "to": "rules", "text": "checkFreeTierEligibility(studentId)"},
            {"type": "frag_start", "kind": "alt", "condition": "[eligible for free session (high stress triggered)]"},
            {"type": "return", "from": "rules", "to": "ctrl", "text": "eligibilityConfirmed(isFree = true)"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "createConfirmedAppointment(studentId, counselorId, slotTime, isFree)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "appointmentBooked(bookingId)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "bookingConfirmedFree()"},
            {"type": "frag_divider", "condition": "[ineligible for free session: requires payment]"},
            {"type": "return", "from": "rules", "to": "ctrl", "text": "paymentRequired(feeAmount)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "promptPaymentFlow(counselorId, slotTime, feeAmount)"},
            {"type": "frag_end"},
            {"type": "return", "from": "ui", "to": "student", "text": "displayBookingOutcome()"}
        ]
    })

    # UC12
    diagrams.append({
        "id": "UC12",
        "title": "UC12: Conduct Counseling Session & Maintain Clinical Notes",
        "caption": "Figure 5.4.12: Sequence Diagram for Conduct Counseling Session & Maintain Clinical Notes",
        "participants": [
            ("counselor", "Counselor", True),
            ("ui", "CounselorPortalUI", False),
            ("ctrl", "CounselingSessionController", False),
            ("access", "AccessControlService", False),
            ("repo", "ClinicalNotesRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "counselor", "to": "ui", "text": "openScheduledSession(appointmentId)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "initiateSessionRoom(appointmentId)"},
            {"type": "call", "from": "ctrl", "to": "access", "text": "checkStudentConsent(studentId)"},
            {"type": "frag_start", "kind": "opt", "condition": "[student granted consent to share stress data]"},
            {"type": "return", "from": "access", "to": "ctrl", "text": "consentApproved()"},
            {"type": "call", "from": "ctrl", "to": "ui", "text": "loadAuthorizedStressTrends(studentId)"},
            {"type": "frag_end"},
            {"type": "call", "from": "counselor", "to": "ui", "text": "conductSession(chat | audio | video)"},
            {"type": "call", "from": "counselor", "to": "ui", "text": "enterClinicalNotes(privateNotes, recommendations)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "saveSessionNotes(appointmentId, privateNotes)"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "storeEncryptedNotes(appointmentId, privateNotes)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "notesSaved()"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "sessionCompletedStatus()"},
            {"type": "return", "from": "ui", "to": "counselor", "text": "displaySessionSummary()"}
        ]
    })

    # UC13
    diagrams.append({
        "id": "UC13",
        "title": "UC13: Process Appointment Payment via Polar",
        "caption": "Figure 5.4.13: Sequence Diagram for Process Appointment Payment via Polar",
        "participants": [
            ("student", "Student", True),
            ("ui", "PaymentCheckoutUI", False),
            ("ctrl", "PaymentController", False),
            ("polar", "PolarPaymentGateway", False),
            ("repo", "AppointmentRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "student", "to": "ui", "text": "proceedToPayment(appointmentDetails)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "createCheckoutSession(studentId, feeAmount)"},
            {"type": "call", "from": "ctrl", "to": "polar", "text": "initiateCheckout(amount, testMode=true)"},
            {"type": "return", "from": "polar", "to": "ctrl", "text": "checkoutUrl(sessionUrl, paymentId)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "redirectCheckout(checkoutUrl)"},
            {"type": "call", "from": "student", "to": "ui", "text": "submitPaymentDetails(testCardCredentials)"},
            {"type": "call", "from": "polar", "to": "ctrl", "text": "webhookPaymentSuccess(paymentPayload, signature)"},
            {"type": "self", "from": "ctrl", "text": "verifyWebhookSignature()"},
            {"type": "frag_start", "kind": "alt", "condition": "[signature verified & payment captured]"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "confirmAppointment(appointmentId, paymentId)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "statusUpdated('Confirmed')"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "paymentConfirmed(receiptRef)"},
            {"type": "return", "from": "ui", "to": "student", "text": "renderBookingSuccessReceipt()"},
            {"type": "frag_divider", "condition": "[payment declined / verification failed]"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "paymentDeclined(reason)"},
            {"type": "return", "from": "ui", "to": "student", "text": "renderPaymentErrorPrompt()"},
            {"type": "frag_end"}
        ]
    })

    # UC14
    diagrams.append({
        "id": "UC14",
        "title": "UC14: Create & Interact with Peer Community Posts",
        "caption": "Figure 5.4.14: Sequence Diagram for Create & Interact with Peer Community Posts",
        "participants": [
            ("user", "Student / Counselor", True),
            ("ui", "CommunityFeedUI", False),
            ("ctrl", "CommunityController", False),
            ("filter", "ContentSafetyFilter", False),
            ("repo", "CommunityRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "user", "to": "ui", "text": "createPost(postContent, isAnonymous, tags)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "submitPost(postContent, isAnonymous, tags)"},
            {"type": "call", "from": "ctrl", "to": "filter", "text": "screenProfanityAndSafety(postContent)"},
            {"type": "frag_start", "kind": "alt", "condition": "[content clean]"},
            {"type": "return", "from": "filter", "to": "ctrl", "text": "contentClean()"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "insertPost(authorId, isAnonymous, postContent)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "postCreated(postId)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "postPublishedSuccess()"},
            {"type": "return", "from": "ui", "to": "user", "text": "renderNewPostInFeed()"},
            {"type": "frag_divider", "condition": "[harmful or abusive keywords flagged]"},
            {"type": "return", "from": "filter", "to": "ctrl", "text": "flagViolation(keywordFound)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "postRejectedNotice(policyViolation)"},
            {"type": "return", "from": "ui", "to": "user", "text": "displayPolicyWarning()"},
            {"type": "frag_end"}
        ]
    })

    # UC15
    diagrams.append({
        "id": "UC15",
        "title": "UC15: Report Inappropriate Community Post",
        "caption": "Figure 5.4.15: Sequence Diagram for Report Inappropriate Community Post",
        "participants": [
            ("student", "Student", True),
            ("ui", "CommunityPostUI", False),
            ("ctrl", "ModerationController", False),
            ("queue", "ModerationQueueService", False),
            ("repo", "CommunityRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "student", "to": "ui", "text": "flagPost(postId, reportReason)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "submitReport(studentId, postId, reportReason)"},
            {"type": "self", "from": "ctrl", "text": "validateReportEligibility()"},
            {"type": "call", "from": "ctrl", "to": "queue", "text": "enqueueModerationTicket(postId, reportReason)"},
            {"type": "return", "from": "queue", "to": "ctrl", "text": "ticketEnqueued(ticketId, reportCount)"},
            {"type": "frag_start", "kind": "opt", "condition": "[reportCount >= threshold (e.g. 3 flags)]"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "temporarilyHidePost(postId)"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "postHidden()"},
            {"type": "frag_end"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "reportAcknowledged()"},
            {"type": "return", "from": "ui", "to": "student", "text": "displayThankYouNotice()"}
        ]
    })

    # UC16
    diagrams.append({
        "id": "UC16",
        "title": "UC16: Manage System Users & Counselor Approvals",
        "caption": "Figure 5.4.16: Sequence Diagram for Manage System Users & Counselor Approvals",
        "participants": [
            ("admin", "Administrator", True),
            ("ui", "AdminDashboardUI", False),
            ("ctrl", "UserAdminController", False),
            ("auth", "SupabaseAuth", False),
            ("repo", "CounselorRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "admin", "to": "ui", "text": "viewPendingCounselorApplications()"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "fetchPendingCounselors()"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "getPendingCounselorRecords()"},
            {"type": "return", "from": "repo", "to": "ctrl", "text": "counselorList(applicants)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "displayApplicantCards(applicants)"},
            {"type": "call", "from": "admin", "to": "ui", "text": "reviewCredentials(counselorId, statusDecision)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "updateCounselorStatus(counselorId, statusDecision)"},
            {"type": "frag_start", "kind": "alt", "condition": "[statusDecision == 'Approved']"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "setApprovalStatus(counselorId, isApproved=true)"},
            {"type": "call", "from": "ctrl", "to": "auth", "text": "grantCounselorRolePermissions(counselorId)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "counselorApprovedNotification()"},
            {"type": "frag_divider", "condition": "[statusDecision == 'Rejected']"},
            {"type": "call", "from": "ctrl", "to": "repo", "text": "setApprovalStatus(counselorId, isApproved=false)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "applicationRejected()"},
            {"type": "frag_end"},
            {"type": "return", "from": "ui", "to": "admin", "text": "refreshApplicantList()"}
        ]
    })

    # UC17
    diagrams.append({
        "id": "UC17",
        "title": "UC17: Moderate Community Reports & System Content",
        "caption": "Figure 5.4.17: Sequence Diagram for Moderate Community Reports & System Content",
        "participants": [
            ("admin", "Administrator", True),
            ("ui", "AdminContentUI", False),
            ("ctrl", "ContentAdminController", False),
            ("c_repo", "CommunityRepository", False),
            ("m_repo", "ContentLibraryRepository", False)
        ],
        "steps": [
            {"type": "call", "from": "admin", "to": "ui", "text": "openModerationQueue()"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "fetchReportedItems()"},
            {"type": "call", "from": "ctrl", "to": "c_repo", "text": "getPendingTickets()"},
            {"type": "return", "from": "c_repo", "to": "ctrl", "text": "ticketList(flaggedPosts)"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "displayFlaggedPosts(flaggedPosts)"},
            {"type": "call", "from": "admin", "to": "ui", "text": "resolveTicket(ticketId, action: RemovePost | Dismiss)"},
            {"type": "frag_start", "kind": "alt", "condition": "[action == RemovePost]"},
            {"type": "call", "from": "ctrl", "to": "c_repo", "text": "deletePostPermanent(postId)"},
            {"type": "return", "from": "c_repo", "to": "ctrl", "text": "postRemoved()"},
            {"type": "frag_divider", "condition": "[action == Dismiss]"},
            {"type": "call", "from": "ctrl", "to": "c_repo", "text": "restorePost(postId)"},
            {"type": "frag_end"},
            {"type": "frag_start", "kind": "opt", "condition": "[admin uploads new relaxation media]"},
            {"type": "call", "from": "admin", "to": "ui", "text": "uploadRelaxationResource(title, category, url)"},
            {"type": "call", "from": "ui", "to": "ctrl", "text": "addNewContent(resourceData)"},
            {"type": "call", "from": "ctrl", "to": "m_repo", "text": "insertContent(resourceData)"},
            {"type": "frag_end"},
            {"type": "return", "from": "ctrl", "to": "ui", "text": "moderationActionComplete()"},
            {"type": "return", "from": "ui", "to": "admin", "text": "renderUpdatedAdminDashboard()"}
        ]
    })

    return diagrams

def generate_all_sequence_diagrams():
    diagrams = get_sequence_diagram_definitions()
    svg_dir = os.path.join("Documentation", "Diagrams", "SVG")
    editable_dir = os.path.join("Documentation", "Diagrams", "Editable")
    visio_dir = os.path.join("Documentation", "Diagrams", "Visio")
    os.makedirs(svg_dir, exist_ok=True)
    os.makedirs(editable_dir, exist_ok=True)
    os.makedirs(visio_dir, exist_ok=True)

    print(f"Total Sequence Diagrams to generate: {len(diagrams)}")
    generated = []

    for d in diagrams:
        uid = d["id"]
        renderer = SequenceDiagramRenderer(
            title=d["title"],
            figure_caption=d["caption"],
            participants=d["participants"],
            steps=d["steps"],
            width=1050,
            height=850
        )
        
        # SVG
        svg_content = renderer.generate_svg()
        svg_path = os.path.join(svg_dir, f"{uid}_Sequence_Diagram.svg")
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)

        # Draw.io XML
        drawio_content = renderer.generate_drawio()
        drawio_path = os.path.join(editable_dir, f"{uid}_Sequence_Diagram.drawio")
        with open(drawio_path, "w", encoding="utf-8") as f:
            f.write(drawio_content)

        # Visio compatible copy
        visio_path = os.path.join(visio_dir, f"{uid}_Sequence_Diagram.drawio")
        with open(visio_path, "w", encoding="utf-8") as f:
            f.write(drawio_content)

        generated.append((uid, d["title"], d["caption"], svg_path, drawio_path))
        print(f"Generated: {uid}_Sequence_Diagram (.svg, .drawio)")

    return generated

if __name__ == "__main__":
    generate_all_sequence_diagrams()
