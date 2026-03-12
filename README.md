<img width="1601" height="766" alt="image" src="https://github.com/user-attachments/assets/f26194fb-51f6-4373-85ca-8660282114df" />
# 🧠 MindMate AI – Mental Health Support App for Students

MindMate AI is an AI-powered mental health support application designed to help college students manage stress, track emotional wellbeing, and receive supportive guidance.

The app provides a safe digital space where students can track moods, talk with an AI companion, connect with peers, and access emergency support resources.

This project was developed for a hackathon to demonstrate how AI can assist with student mental wellbeing.

---

# 🚀 Features

### 🤖 AI Emotional Support

Students can chat with an AI companion that provides supportive responses and coping suggestions using an LLM.

### 😊 Mood Tracker

Users can log daily emotions and monitor their mood trends.

### 🧑‍🤝‍🧑 Peer Support Community

Anonymous community where students can share experiences and support each other.

### 🎵 Music Therapy

Calming music suggestions to help students relax and reduce stress.

### 🚨 Crisis Support

Emergency help page with quick access to mental health helplines such as the Sneha Suicide Prevention Helpline.

### 🔒 Privacy & Security

* User login
* Anonymous mode
* Chat lock option
* Privacy-focused design

---

# 🏗 System Architecture

```
Flutter Mobile App
        │
        │ HTTP API
        ▼
FastAPI Backend
        │
        │ AI Prompt Processing
        ▼
Ollama LLM
```

The Flutter application communicates with the backend API, which processes user input and generates responses using a local LLM.

---

# 🛠 Tech Stack

Frontend

* Flutter (Dart)

Backend

* Python
* FastAPI

AI

* Ollama
* Mistral / LLaMA LLM

Other Tools

* Stitch (UI Design)
* Antigravity (AI workflow)
* SQLite (lightweight database)

---

# 📱 App Screens

* Login / Signup
* User Onboarding
* Dashboard
* AI Chat Companion
* Mood Tracker
* Peer Support Community
* Music Therapy
* Crisis Support
* Settings & Privacy

---

# ⚙ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/mindmate-ai.git
cd mindmate-ai
```

---

### 2️⃣ Run Backend

Install dependencies:

```
pip install fastapi uvicorn requests
```

Start the server:

```
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

### 3️⃣ Start Ollama

Run the LLM model:

```
ollama run mistral
```

---

### 4️⃣ Run Flutter App

```
flutter pub get
flutter run
```

---

# 🧠 Example AI Interaction

User Input

```
I feel stressed about my exams.
```

AI Response

```
It’s normal to feel stressed before exams. Try breaking your study sessions into smaller blocks and take short breaks between them.
```

---

# 🎯 Future Improvements

* AI emotion detection
* Personalized wellness recommendations
* Campus counseling integration
* Wearable stress data integration
* Advanced mood analytics

---

# 🤝 Contributors

Team MindMate AI

* Developer – Flutter App
* AI Integration – Backend + LLM
* UI/UX – Stitch Design

---

# ⚠ Disclaimer

This project provides supportive guidance but does not replace professional medical or psychological care.

If you are experiencing severe distress, please contact a qualified mental health professional or a crisis helpline.

---

# ❤️ Motivation

Student mental health is a growing concern worldwide. MindMate AI aims to provide accessible emotional support using technology and AI.
