# 📚 The Grand Tour of Libraries Web Service

A minimalist web service built with Flask that showcases beautiful libraries worldwide, designed with a clean, Notion-like aesthetic.

## 🔗 Quick Access

You can access the live service deployed on Render at the following address:

**[https://library-app-9est.onrender.com](https://library-app-9est.onrender.com)**

-----

## ✨ Features

  * **Notion-Like Design:** Clean, distraction-free interface using modern CSS (`Inter` font, simple card layout).
  * **Responsive Grid:** Library cards adjust automatically for mobile and desktop screens.
  * **Python/Flask Backend:** Lightweight and scalable application logic.
  * **Dynamic Routing:** Each library card links to a specific detail page (`/library/<id>`).

-----

## 🛠️ Local Development Setup

Follow these steps to get a copy of the project running on your local machine for development and testing.

### 1\. Prerequisites

You need **Python 3.x** installed on your system.

### 2\. Clone the Repository

```bash
git clone [YOUR_REPO_URL_HERE]
cd library-service
```

### 3\. Create a Virtual Environment (Recommended)

This isolates your project's dependencies from other Python projects.

```bash
# For Windows/macOS/Linux
python -m venv venv

# Activate the virtual environment
# Windows (Command Prompt):
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 4\. Install Dependencies

Install Flask, Gunicorn (used for deployment configuration), and any other required packages:

```bash
pip install -r requirements.txt
```

### 5\. Run the Application

You can start the application using the Flask development server:

```bash
# Set environment variable for Flask (needed only once per terminal session)
export FLASK_APP=app.py 
# (For Windows Command Prompt: set FLASK_APP=app.py)

# Run the app
flask run
```

The service will be available at: **[http://127.0.0.1:5000/](https://www.google.com/search?q=http://127.0.0.1:5000/)**

-----

## 📦 Project Structure

```
library-service/
├── app.py              # Main Flask application file and routing logic
├── Procfile            # Deployment file for Render (uses Gunicorn)
├── requirements.txt    # Python dependencies list
├── static/             # Static assets (CSS, Images)
│   ├── style.css       # All styling for the service
│   └── placeholder1.jpg
└── templates/          # HTML templates (Jinja2)
    ├── index.html      # The main library listing page
    └── detail.html     # The single library detail page
```

-----

## ☁️ Deployment Information

  * **Platform:** Render
  * **WSGI Server:** Gunicorn
  * **Start Command (Procfile):** `web: gunicorn app:app`
