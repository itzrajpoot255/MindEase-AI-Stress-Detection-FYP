# MindEase: Dataset and Machine Learning Documentation

## 1. Overview
MindEase integrates multimodal data streams to estimate student stress levels. This document outlines the datasets, psychometric validation instruments, speech acoustic corpora, and synthetic evaluation data used in developing and validating the system.

---

## 2. Psychometric Instruments & Survey Data
- **Perceived Stress Scale (PSS-10 / PSS-14):** Standardized clinical survey instrument utilized to evaluate perceived stress levels. Localized into:
  - English (Standard Cohen PSS)
  - Urdu (Validated Urdu psychometric translation)
  - Roman Urdu (Phonetic conversational transliteration)
- **Scoring Thresholds:**
  - `0 - 13`: Low Perceived Stress
  - `14 - 26`: Moderate Perceived Stress
  - `27 - 40`: High Perceived Stress (triggers counselor free triage eligibility)

---

## 3. Speech & Acoustic Models (Whisper ASR)
- **Model Architecture:** OpenAI Whisper (Medium / Small fine-tuned for South Asian accents).
- **Audio Preprocessing:**
  - Sampling Rate: 16,000 Hz (16 kHz mono)
  - Format: 16-bit Linear PCM WAV / WebM
  - Acoustic Feature Extraction: 80-channel log-magnitude Mel-filterbank representations.
- **Language Identification:** Multilingual routing supporting code-switching between Urdu and English.

---

## 4. Behavioral Lifestyle & Habit Metrics
- **Sleep Duration:** Ingested in hours per night (normal range: 4.0 – 10.0 hours).
- **Smartphone Screen Time:** Ingested in active screen-on minutes per day (0 – 720 minutes).
- **Physical Activity (Step Count):** Ingested via Android SensorManager pedometer hardware (0 – 25,000 steps).
- **Imputation Strategy:** 7-day rolling personal baseline average used when optional habit fields are omitted by the student.

---

## 5. Model Architecture & Explainability
- **Fusion Classifier:** Gradient Boosted Trees (Scikit-learn) and Multi-Layer Perceptron (PyTorch).
- **Feature Vector:** Normalized vector combining questionnaire PSS score, diary sentiment score, sleep hours, screen time, and step count.
- **Explainability:** SHAP (SHapley Additive exPlanations) TreeExplainer computing additive feature attributions for every individual inference.
