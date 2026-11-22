# MindEase: Hardware and Sensor Integration Documentation

## 1. Overview
MindEase operates on standard Android mobile devices, interfacing with onboard audio and motion hardware to capture multimodal stress signals.

---

## 2. Hardware Interfaces & Requirements

### 2.1 Audio Hardware (Microphone)
- **Component:** Onboard mobile microphone transducer.
- **Capture Specifications:**
  - Sampling Frequency: 16 kHz
  - Bit Depth: 16-bit
  - Channel Configuration: Mono channel
  - Max Recording Duration: 180 seconds (3 minutes) per diary check-in
- **Permission Requirements:** `android.permission.RECORD_AUDIO`

---

### 2.2 Physical Motion Sensors (Pedometer)
- **Sensors:** `Sensor.TYPE_STEP_COUNTER` and `Sensor.TYPE_STEP_DETECTOR`
- **Data Capture:** Aggregates cumulative steps taken throughout the academic day.
- **Fallback Integration:** Google Health Connect API for devices without continuous hardware pedometers.
- **Permission Requirements:** `android.permission.ACTIVITY_RECOGNITION`

---

### 2.3 Device Usage & Screen Time Telemetry
- **API Framework:** Android `UsageStatsManager`
- **Metric Captured:** Cumulative screen-on duration in active foreground use.
- **Permission Requirements:** `android.permission.PACKAGE_USAGE_STATS` (User-granted special access)

---

### 2.4 Device Minimum Platform Requirements
- **OS Version:** Android 9.0 (API Level 28 - Pie) or later
- **RAM:** Minimum 2.0 GB (Recommended: 4.0 GB)
- **Internal Storage:** 100 MB free space for local SQLite cache and audio buffer
- **Network Interface:** Wi-Fi (802.11 b/g/n/ac) or Cellular 4G/LTE/5G
