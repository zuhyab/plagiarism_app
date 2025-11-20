📘 Flask Plagiarism Checker

A simple yet functional Flask-based plagiarism detection system with:

✔ User Authentication
✔ Admin Dashboard
✔ File Upload System
✔ Plagiarism Checking using SequenceMatcher
✔ Role-based Access (Admin/User)

This project allows users to upload text files, and administrators can compare them for plagiarism.

🚀 Features
🔐 Authentication System
User registration & login
Password hashing using Werkzeug
Role-based dashboard (Admin/User)
Admin created automatically on first run

📂 File Upload (Users)
Users can upload .txt or text-based files
Files stored securely in static/uploads/

🛡 Admin Dashboard
View all uploaded files
Compare files pairwise using difflib.SequenceMatcher
Displays plagiarism percentage for each pair

📄 File Viewing & Downloading
Open text files inside the app
Secure downloading with path sanitization

📁 Project Structure
Based on your project screenshot:

Flask-Plagiarism-Checker/
│
├── .idea/                     # (IDE folder - optional)
├── __pycache__/               # Python cache files
├── instance/                  # Flask instance folder
│   └── users.db               # SQLite database
│
├── static/
│   └── uploads/               # Uploaded user files
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── user_dashboard.html
│   ├── admin_dashboard.html
│   ├── view_file.html
│   └── ...(other templates if any)
│
├── app.py                     # Main Flask application
├── auth.py                    # Authentication Blueprint
├── database.py                # DB initialization + default admin
├── models.py                  # User model + SQLAlchemy setup
├── plagiarism_checker.py      # Plagiarism logic + dashboards
│
└── users                      # Database file (SQLite)
