# 🏋️‍♀️ FitGeek – AI-Powered Fitness and Wellness App

🚀 Hosted Demo: [Streamlit App](https://fitgeek.streamlit.app)  
📦 GitHub Repo: [github.com/shreyamahajan5/FitGeek](https://github.com/shreyamahajan5/FitGeek)

---

## 📌 Overview

**FitGeek** is a full-stack Django application designed to personalize fitness, wellness, and nutrition experiences. It combines multiple features including workout plans, dietary suggestions, stress detection, and dynamic health dashboards — all in one AI-powered platform.

---

## 🔑 Features

- 💪 Personalized **Workout Plan** Tabs (core, legs, arms, etc.)
- 🧠 **Stress Level Detector** using NLP (Perceived Stress Scale)
- 💬 Motivational **Daily Quote & Health News** Feed via APIs
- 🍽️ Smart **Diet Recommendation** System
- 💧 **Hydration Calculator** & Wellness Trackers
- 💸 Integrated **Payment Simulation** (UPI, Google Pay)
- 📊 Dynamic **BMI Dashboard** with Categorized Routes
- 📍 Clean modular routing with 50+ interactive templates

---

## 🛠️ Tech Stack

| Layer           | Tools Used                              |
|----------------|-------------------------------------------|
| Backend         | Python, Django, Django ORM               |
| Frontend        | HTML/CSS, Bootstrap, Django Templates    |
| NLP             | TextBlob, spaCy, NLTK                    |
| APIs            | NewsAPI, ZenQuotes, Nutritionix          |
| Data Visualization | Plotly, Pandas                       |
| Auth            | Django Auth (Login, Logout, Superuser)   |

---

## 🗂️ Project Structure

FitGeek/
├── core_project/ # Actual Django app with views, templates
│ ├── healthapp/ # Main app: views, urls, templates
│ ├── manage.py # Django entry point
│ └── requirements.txt # Dependencies
├── fitgeek_project/ # Archived or zip-based code backup
├── documents/ # Reports, presentations, assets
├── healthvenv/ # DO NOT TRACK – Virtual environment
└── .gitignore # Ensures no virtualenv or cache is committed


---

## ⚙️ Setup Instructions

1. **Clone Repo**
   ```bash
   git clone https://github.com/shreyamahajan5/FitGeek.git
   cd FitGeek

Create Virtual Environment
  ```bash
python3 -m venv env
source env/bin/activate   # or env\Scripts\activate on Windows

Install Dependencies
  ```bash
pip install -r core_project/requirements.txt

Run Server
  ```bash
cd core_project
  ```bash
python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

📌 Notes

⚠️ The venv/ and zip files are excluded using .gitignore.
🤖 AI stress analysis is based on scoring text responses via spaCy/TextBlob NLP pipelines.
🗂 Multiple apps like exercise rec, hydrationcalc, and HealthGeek-Stress... are included as sub-modules inside healthvenv.
🏆 Recognition

🟢 Best Project Award – Among 50+ teams during final year showcase
📝 Published at ICACEBD 2024 – DOI: 10.1063/5.0239053

🙋‍♀️ Author

Shreya Mahajan
Graduate Student – MS CSE @ Santa Clara University
📧 samahajan@scu.edu
🌐 LinkedIn
