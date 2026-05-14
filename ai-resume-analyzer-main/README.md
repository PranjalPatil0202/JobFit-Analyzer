# 🚀 AI Resume Analyzer & Career Recommendation Platform

An AI-powered full-stack web application that analyzes resumes, calculates ATS scores, extracts technical skills, recommends career paths, and provides personalized job recommendations using Machine Learning and NLP techniques.

---

## 🌟 Project Highlights

✅ Upload and analyze PDF resumes

✅ ATS Resume Score Calculation

✅ Skill Extraction using NLP

✅ Experience Level Detection

✅ AI Resume Suggestions

✅ Career Path Recommendations

✅ Machine Learning Job Recommendation System

✅ Interactive Analytics Dashboard

✅ Resume Validation System

✅ JWT Authentication

---

## 🖥️ Demo Features

### 📄 Resume Analysis

* Upload resume PDFs
* Extract resume text automatically
* Detect technical skills
* Calculate ATS score
* Identify strengths and improvements

### 🤖 AI Suggestions

* Resume improvement recommendations
* Missing skills suggestions
* Resume optimization tips

### 🎯 Career Recommendations

* Backend Developer
* Frontend Developer
* Full Stack Developer
* Machine Learning Engineer
* Cloud Engineer
* Data Analyst

### 📊 Interactive Dashboard

* ATS Circular Graph
* Skills Radar Chart
* Job Match Bar Graph
* Recommended Jobs Section

---

## 🛠️ Tech Stack

### Frontend

* React.js
* Axios
* Recharts
* React Router DOM

### Backend

* Django
* Django REST Framework
* JWT Authentication

### Machine Learning & NLP

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* NLP-based Skill Extraction

### Database

* SQLite (Development)
* PostgreSQL (Recommended for Deployment)

---

## 📂 Project Structure

An AI-powered full-stack web application that analyzes resumes, calculates ATS scores, extracts technical skills, recommends career paths, and suggests relevant jobs using Machine Learning.

---

# Features

## Resume Upload & Parsing

* Upload PDF resumes
* Extract text using PyMuPDF
* Validate uploaded resumes
* Reject invalid PDFs like marksheets/certificates

## AI Resume Analysis

* ATS Resume Score Calculation
* Experience Level Detection
* Technical Skill Extraction
* AI Resume Suggestions
* Strengths & Improvements Analysis

## Career Recommendations

* Recommend career paths based on skills
* Backend Developer
* Frontend Developer
* Full Stack Developer
* Machine Learning Engineer
* Cloud Engineer
* Data Analyst

## Machine Learning Job Recommendation Engine

* TF-IDF Vectorization
* Cosine Similarity Matching
* Personalized Job Recommendations
* Missing Skills Detection

## Analytics Dashboard

* ATS Score Circular Chart
* Skills Radar Chart
* Job Match Bar Graph
* Interactive Dashboard UI

## Authentication

* JWT Authentication
* User Registration/Login
* Protected APIs

---

# Tech Stack

## Frontend

* React.js
* Axios
* Recharts
* React Router DOM

## Backend

* Django
* Django REST Framework
* JWT Authentication

## Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* NLP-based Skill Extraction

## Database

* SQLite (Development)
* PostgreSQL (Recommended for Deployment)

---

# Project Structure

```bash
AI-RESUME-ANALYZER/
│
├── backend/
│   ├── datasets/
│   ├── jobs/
│   ├── resumes/
│   ├── users/
│   └── manage.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation Guide

## Clone Repository

```bash
git clone <your-github-repo-link>
cd AI-Resume-Analyzer
```

---

# Backend Setup

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Migrations

```bash
python manage.py migrate
```

---

## Start Django Server

```bash
python manage.py runserver
```

Backend runs on:

```bash
http://127.0.0.1:8000/
```

---

# Frontend Setup

## Move To Frontend Folder

```bash
cd frontend
```

---

## Install Dependencies

```bash
npm install
```

---

## Start React App

```bash
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173/
```

---

# API Endpoints

## Authentication

| Method | Endpoint       | Description   |
| ------ | -------------- | ------------- |
| POST   | /api/register/ | Register user |
| POST   | /api/login/    | Login user    |

---

## Resume APIs

| Method | Endpoint             | Description      |
| ------ | -------------------- | ---------------- |
| POST   | /api/resumes/upload/ | Upload resume    |
| GET    | /api/resumes/        | Get user resumes |

---

## Job Recommendation APIs

| Method | Endpoint             | Description                |
| ------ | -------------------- | -------------------------- |
| GET    | /api/recommend-jobs/ | Get ML job recommendations |

---

# Screenshots

Add screenshots here:

* Dashboard
* Resume Analytics
* ATS Score Graph
* Skills Radar Chart
* Job Recommendations

---

# Future Improvements

* Live Job APIs
* OpenAI Resume Feedback
* Resume vs Job Description Matching
* Docker Deployment
* Email Reports
* Interview Question Generator
* Admin Analytics Dashboard

---

# Deployment

## Recommended Platforms

| Service  | Platform        |
| -------- | --------------- |
| Frontend | Vercel          |
| Backend  | Render          |
| Database | Neon PostgreSQL |

---

# Resume Description

```text
AI Resume Analyzer & Career Recommendation Platform
Built a full-stack AI-powered platform using Django, React.js, and Machine Learning to analyze resumes, calculate ATS scores, extract skills, recommend career paths, and provide personalized job recommendations using TF-IDF and cosine similarity.
```

---

# Author

Pranjal Patil

GitHub: [https://github.com/](https://github.com/)
LinkedIn: [https://linkedin.com/](https://linkedin.com/)

