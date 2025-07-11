# FitGeek 🏋️✨

**A Machine Learning-powered fitness and wellness recommendation system.**

Live Demo: _Coming Soon_

---

## 📌 Introduction

FitGeek is a comprehensive Django-based web application that promotes fitness and well-being using machine learning. It provides features such as:

- **Personalized workout plans**
- **Custom diet recommendations**
- **Body type tracking (BMI-based)**
- **Real-time stress level detection**
- **Interactive exercise guide**
- **Calorie tracking and food insights using Nutritionix API**
- **Health news and daily motivational quotes**

The system aims to make fitness accessible, intelligent, and interactive.

---

## 🛠️ Technologies Used

- **Backend:** Django, SQLite
- **Frontend:** HTML/CSS/JS, Bootstrap
- **Machine Learning:** SVM (Diabetes Prediction), NLP (Stress Detection)
- **APIs:** NewsAPI, Nutritionix, ZenQuotes
- **Visualization:** Plotly, Pandas

---

## 📁 Project Structure

FitGeek/
│
├── healthapp/ # Core Django app
│ ├── templates/ # HTML templates
│ ├── static/ # CSS, JS, and image files
│ ├── views.py # View logic
│ ├── models.py # DB Models
│ └── urls.py # App-level routing
│
├── fitgeek_project/ # Django project folder
│ ├── settings.py # Main settings
│ └── urls.py # Project routing
│
├── db.sqlite3 # Database
├── manage.py # Django CLI entry
├── requirements.txt # Required Python packages
└── README.md # Project documentation

---

## 🚀 How to Run the Project Locally

> **Pre-requisites:**
> - Python 3.7+
> - `pip` installed
> - Virtual environment (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/shreyamahajan5/FitGeek.git
cd FitGeek
````

### 2. Create Virtual Environment

```bash
python -m venv healthvenv
source healthvenv/bin/activate     # Mac/Linux
# OR
healthvenv\Scripts\activate.bat    # Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

> Open your browser and go to `http://127.0.0.1:8000/` 🎉

---

## 📸 Features Showcase

* BMI Classification (Underweight, Normal, Overweight, Obese)
* Full body and targeted exercise suggestions with animation guides
* Payment gateway simulation (UPI/GPay)
* Trainer application and appointment booking
* Nutrition input → Exercise output using ML API
* Live health news feed & motivational quotes
* Timer & Shop integration

---

## 🏆 Achievements

* 🥇 *Best Project Award* among 50+ teams
* 📃 Published in **ICACEBD-24 Conference**: [DOI Link](https://doi.org/10.1063/5.0239053)

---

## 📚 Research Components

* **Stress Detector**: Implemented using NLP on the Perceived Stress Scale (PSS)
* **Diabetes Predictor**: Trained on PIMA Indian Diabetes Dataset using SVM
* **Real-time data parsing**: Nutritionix API for food to calorie → workout mapping

---

## 🙋 Authors

* **Shreya Mahajan**
  [LinkedIn](https://linkedin.com/in/shreyamahajan5) | [GitHub](https://github.com/shreyamahajan5)

---

## 📄 License

This project is for academic and educational purposes. Contact the author for permission if you wish to reuse.

---
