from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

# This demo data is intentionally isolated so the backend can later be
# connected to SQLite and real Flask routes without changing the templates.
DEMO_DATA = {
    "students": [
        {"id": 1, "name": "Ariana Smith", "year_level": "Year 2", "family_contact": "Ms. Smith - 0400 123 456", "status": "Active"},
        {"id": 2, "name": "Liam Johnson", "year_level": "Year 1", "family_contact": "Mr. Johnson - 0401 987 654", "status": "Active"},
        {"id": 3, "name": "Sophie Nguyen", "year_level": "Year 3", "family_contact": "Mrs. Nguyen - 0402 654 321", "status": "Inactive"},
    ],
    "tutors": [
        {"id": 1, "name": "Dr. Emily Ross", "subjects": ["Mathematics", "Physics"], "availability": "Mon / Wed / Fri", "status": "Active"},
        {"id": 2, "name": "Marcus Lee", "subjects": ["Biology", "Chemistry"], "availability": "Tue / Thu", "status": "Active"},
        {"id": 3, "name": "Nina Patel", "subjects": ["English"], "availability": "Weekends", "status": "Inactive"},
    ],
    "availability_windows": [
        {"id": 1, "tutor": "Dr. Emily Ross", "day": "Monday", "start": "09:00", "end": "12:00"},
        {"id": 2, "tutor": "Dr. Emily Ross", "day": "Wednesday", "start": "13:00", "end": "16:00"},
        {"id": 3, "tutor": "Marcus Lee", "day": "Tuesday", "start": "10:00", "end": "14:00"},
    ],
    "sessions": [
        {"id": 1, "student": "Ariana Smith", "tutor": "Dr. Emily Ross", "subject": "Mathematics", "date": "2026-10-01", "time": "09:30", "duration": 60, "status": "Booked"},
        {"id": 2, "student": "Liam Johnson", "tutor": "Marcus Lee", "subject": "Biology", "date": "2026-10-01", "time": "11:00", "duration": 90, "status": "Booked"},
        {"id": 3, "student": "Sophie Nguyen", "tutor": "Dr. Emily Ross", "subject": "Physics", "date": "2026-09-30", "time": "14:00", "duration": 60, "status": "Completed"},
        {"id": 4, "student": "Ariana Smith", "tutor": "Marcus Lee", "subject": "Chemistry", "date": "2026-10-04", "time": "10:00", "duration": 75, "status": "Booked"},
        {"id": 5, "student": "Liam Johnson", "tutor": "Dr. Emily Ross", "subject": "Mathematics", "date": "2026-10-02", "time": "15:00", "duration": 60, "status": "Cancelled"},
    ],
    "activity": [
        {"title": "Student profile updated", "detail": "Ariana Smith record reviewed and updated."},
        {"title": "New tutoring availability added", "detail": "Marcus Lee added Tuesday afternoon availability."},
        {"title": "Session moved", "detail": "Liam Johnson session was rescheduled for next week."},
    ],
}


def get_student_by_id(student_id):
    for student in DEMO_DATA["students"]:
        if student["id"] == student_id:
            return student
    return None


@app.route("/")
def home():
    return redirect(url_for("dashboard"))


@app.route("/dashboard")
def dashboard():
    total_students = len(DEMO_DATA["students"])
    active_tutors = sum(1 for tutor in DEMO_DATA["tutors"] if tutor["status"] == "Active")
    todays_sessions = sum(1 for session in DEMO_DATA["sessions"] if session["date"] == "2026-10-01")
    upcoming_sessions = sum(1 for session in DEMO_DATA["sessions"] if session["status"] == "Booked")

    summary = {
        "total_students": total_students,
        "active_tutors": active_tutors,
        "todays_sessions": todays_sessions,
        "upcoming_sessions": upcoming_sessions,
    }

    return render_template(
        "dashboard.html",
        page_title="Dashboard",
        summary=summary,
        upcoming_sessions=DEMO_DATA["sessions"],
        recent_activity=DEMO_DATA["activity"],
    )


@app.route("/students")
def students():
    return render_template(
        "students.html",
        page_title="Students",
        students=DEMO_DATA["students"],
    )


@app.route("/students/add")
def add_student():
    return render_template("add_student.html", page_title="Add Student")


@app.route("/students/<int:student_id>/edit")
def edit_student(student_id):
    student = get_student_by_id(student_id)
    return render_template("edit_student.html", page_title="Edit Student", student=student)


@app.route("/tutors")
def tutors():
    return render_template(
        "tutors.html",
        page_title="Tutors",
        tutors=DEMO_DATA["tutors"],
    )


@app.route("/tutors/add")
def add_tutor():
    return render_template("add_tutor.html", page_title="Add Tutor")


@app.route("/availability")
def availability():
    return render_template(
        "availability.html",
        page_title="Tutor Availability",
        availability_windows=DEMO_DATA["availability_windows"],
        tutors=DEMO_DATA["tutors"],
    )


@app.route("/sessions")
def sessions():
    return render_template(
        "sessions.html",
        page_title="Sessions",
        sessions=DEMO_DATA["sessions"],
    )


@app.route("/sessions/book")
def book_session():
    return render_template(
        "book_session.html",
        page_title="Book Session",
        students=DEMO_DATA["students"],
        tutors=DEMO_DATA["tutors"],
    )


@app.route("/schedule")
def schedule():
    return render_template(
        "schedule.html",
        page_title="Schedule",
        sessions=DEMO_DATA["sessions"],
    )


@app.route("/reports")
def reports():
    return render_template(
        "reports.html",
        page_title="Reports & History",
        sessions=DEMO_DATA["sessions"],
        students=DEMO_DATA["students"],
    )


if __name__ == "__main__":
    app.run(debug=True)
