# AI Resume Analyzer & Job Recommendation System

## Project Overview

AI Resume Analyzer & Job Recommendation System is a full-stack web application that analyzes uploaded resumes, extracts technical skills using NLP-based techniques, and recommends relevant jobs based on skill matching.

The project is built using Django REST Framework for the backend and React.js for the frontend with PostgreSQL as the database.


# Features

## Authentication System

- User Registration
- User Login
- JWT Authentication
- Protected Routes
- Logout Functionality

## Resume Analyzer

- Upload Resume in PDF format
- Extract text from resume
- Extract technical skills automatically
- Store extracted skills in PostgreSQL

## Job Recommendation System

- Admin can add jobs
- Match user skills with job requirements
- Calculate similarity/match percentage
- Recommend best matching jobs

## Dashboard

- Upload Resume
- View Extracted Skills
- View Recommended Jobs
- Responsive User Interface


# Tech Stack

## Frontend

- React.js
- React Router DOM
- Axios
- CSS

## Backend

- Django
- Django REST Framework
- JWT Authentication

## Database

- PostgreSQL

## Machine Learning / NLP

- Python
- Skill Extraction
- Keyword Matching


# Project Structure

```bash
ai-resume-analyzer/
│
├── backend/
│   ├── ai_resume_analyzer/
│   ├── users/
│   ├── resumes/
│   ├── jobs/
│   └── manage.py
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   └── assets/
│   └── package.json
│
├── requirements.txt
└── .gitignore
