# 🎙️ Interview Agent – PROCTOR AI

An AI-powered virtual interview proctoring system that analyzes user behavior in real-time through webcam footage. It detects emotions, head pose, object presence, and flags suspicious activity using state-of-the-art computer vision and machine learning models.

---

## 👨‍💻 Project By

- **Prinka Chugh**
- **Ubedullah Shaikh** 
- **Syed Umer**

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Installation & Setup](#-installation--setup)
- [Module Breakdown](#-module-breakdown)
- [Input / Output](#-input--output)
- [Sample Execution](#-sample-execution)
- [Screenshots](#-screenshots)
- [Challenges Faced](#-challenges-faced)
- [Conclusion](#-conclusion)
- [References](#-references)

---

## 🧠 Overview

**Interview Agent** is a smart monitoring system for virtual interviews that detects:

- Emotional states (happy, sad, angry, etc.)
- Head and eye movement patterns
- Object usage (e.g. mobile phone, book)
- Body posture
- Suspicious behavior via a trained classifier

This system combines multiple AI components to generate detailed reports in multiple formats.

---

## ✨ Features

- 📷 Real-time webcam monitoring  
- 😐 Emotion detection via Mini-XCEPTION on FER2013  
- 🧍 Pose tracking using MediaPipe  
- 📦 Object detection using YOLOv8 (Ultralytics)  
- 🤖 Cheating classification via Random Forest model  
- 📝 Auto-report generation (`.docx`, `.json`, `.csv`)  
- 🖥️ User-friendly GUI using Tkinter  

---

## 🏗️ System Architecture

```text
Webcam Input
   ↓
[main.py]
   ↓
[Face Detector] [Pose Detector] [Object Detector] [Emotion Detector]
   ↓
[Visualizer] → [generate.py] → DOCX / JSON / CSV
