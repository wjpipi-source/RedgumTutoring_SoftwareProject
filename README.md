# RedgumTutoring_SoftwareProject

ISYS3001 Software Build Project for Tutoring Management

## Overview
This project is a Flask web application designed to manage a tutoring service. It provides a simple dashboard and interface for viewing and organising students, tutors, availability, sessions, and reports using demo data.

The application is currently built as a front-end prototype with in-memory data, making it suitable for classroom demonstration and future extension to a database-backed system.

## Features
- Dashboard summary with key counts
- Student listing and management views
- Tutor information and status tracking
- Availability scheduling overview
- Session booking and session tracking
- Reports and history display
- Responsive browser-based UI using Flask templates and static assets

## Technology Stack
- Python
- Flask
- HTML
- CSS
- JavaScript

## Project Structure
- app.py — main Flask application and route definitions
- templates/ — HTML pages for each screen
- static/ — CSS and JavaScript assets
- requirements.txt — Python dependencies
- run.bat — Windows launcher script

## Installation
1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

   Windows:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
Start the app with:

```bash
python app.py
```

Then open the following URL in a browser:

```text
http://127.0.0.1:5000
```

You can also run the included Windows batch file:

```bash
run.bat
```

## Main Pages
- / — redirects to the dashboard
- /dashboard — overview of tutoring data
- /students — student records
- /students/add — add a new student
- /students/<id>/edit — edit an individual student
- /tutors — tutor records
- /tutors/add — add a new tutor
- /availability — tutor availability windows
- /sessions — session records
- /sessions/book — book a new session
- /schedule — scheduled tutoring view
- /reports — summary reports and session history

## Demo Data
The current version uses sample in-memory data to simulate real application behaviour. This allows the UI and routes to be tested before connecting to a persistent database such as MySQL.

## Future Enhancements
- Connect to MySQL
- Add CRUD functionality for students, tutors, and sessions
- Add authentication and role-based access
- Implement validation and form submission handling
- Improve reporting and filtering features

## License
This project is for educational use as part of the ISYS3001 Software Build and Management Project.
