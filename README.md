# EHR System — AI-Integrated Electronic Health Record Platform

🔗 **Live Demo:** [https://tanmaysharma.pythonanywhere.com](https://tanmaysharma.pythonanywhere.com)

A full-stack Electronic Health Record (EHR) system built with Django, featuring role-based access control for patients, doctors, and admins, along with GenAI-powered features for medical report explanation and symptom checking.

## Features

- **Role-based authentication** — separate flows for Patient, Doctor, and Admin
- **Appointment management** — patients book appointments, doctors confirm/cancel/complete them
- **Medical records** — doctors add diagnosis, notes, and prescriptions per visit
- **Lab report uploads** — patients can upload and view lab reports (PDF/image)
- **AI-powered features (Google Gemini API):**
  - **Report Explainer** — converts clinical diagnosis/notes into simple, patient-friendly language
  - **Symptom Checker** — patients describe symptoms and receive possible causes with an urgency level, with appropriate medical disclaimers
- **Role-based dashboards** with quick-glance stats for each user type

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django |
| Database | SQLite (dev) |
| Frontend | Django Templates, Bootstrap 5 |
| AI | Google Gemini API (`google-genai`) |
| Auth | Django session-based auth, custom user model with roles |

## Setup Instructions

1. **Clone the repository**
```bash
   git clone <repo-url>
   cd EHR_system
```

2. **Create and activate a virtual environment**
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Set up environment variables**

   Create a `.env` file in the root directory:
   Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey).

5. **Run migrations**
```bash
   python manage.py makemigrations
   python manage.py migrate
```

6. **Create a superuser (optional, for admin access)**
```bash
   python manage.py createsuperuser
```

7. **Run the development server**
```bash
   python manage.py runserver
```

8. Visit `http://127.0.0.1:8000/register/` to create an account.

## Usage

- **Register** as a Patient or Doctor
- **Patients** can book appointments, upload lab reports, view medical history, and use the AI symptom checker
- **Doctors** can confirm appointments and add diagnosis/prescriptions
- **Admin** can access the Django admin panel for full data management

## AI Integration Notes

Both AI features use the Google Gemini API (`gemini-flash-latest` model) with structured prompts. Explanations are cached in the database after first generation to avoid redundant API calls. Symptom checker responses always include a disclaimer that the tool does not provide medical diagnoses.

## Disclaimer

This is an academic mini-project built for learning purposes. The AI-generated content should not be used as a substitute for professional medical advice.