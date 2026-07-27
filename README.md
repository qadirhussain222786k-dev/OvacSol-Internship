# Student Record & Grade Management System (CLI)

**AI Internship Training Program - Week 1 Project**

**Intern:** Qadir Hussain 
**Intern Batch:**  2026 Week 1 AI Internship Program  
**Company:** OvacSol Pvt. Ltd.

---

## 📌 Project Overview

The Student Record & Grade Management System is a Command Line Interface (CLI) application developed in Python. It allows users to add, update, search, sort, view, and delete student records. The application automatically calculates total marks, average marks, and letter grades while permanently storing data in a JSON file. It also validates user input, prevents duplicate records, and provides a clean table-based interface using the Tabulate library.

This project was developed as part of the Week 1 AI Internship Training Program and demonstrates the concepts learned during the week, including Python fundamentals, Object-Oriented Programming, File Handling, Exception Handling, Modules, Virtual Environments, and Pip.

---

## 🚀 Features

- Add Student
- Update Student Marks
- View Single Student
- View All Students
- Search Student by Name
- Sort Students by Average (Ascending/Descending)
- Delete Student with Confirmation
- Calculate Total Marks
- Calculate Average Marks
- Calculate Letter Grade
- Display Subject Count
- Prevent Duplicate Roll Numbers
- Prevent Duplicate Subject Names
- Validate Subject Names
- Validate Marks (0–100)
- Store Data in JSON File
- Exception Handling
- Table Display using Tabulate (Fancy Grid)

## ⭐ Bonus Features

- Search students using partial names (case-insensitive)
- Sort students by average marks
- Delete confirmation before removing records
- Display total number of subjects
- Prevent duplicate subject names
- Input validation for empty subject names
- Improved table formatting using `fancy_grid`

## 🛠 Technologies Used

- Python 3.10
- JSON
- Tabulate Library
- Virtual Environment (venv)

---

## 📂 Project Structure

```
student-grade-management-system/
│
├── main.py
├── student.py
├── file_manager.py
├── grade_utils.py
├── students.json
├── requirements.txt
├── README.md
├── writeup.md
├── .gitignore
└── venv/
```

---

## ⚙ Installation

### 1. Clone Repository

```bash
git clone https://github.com/qadirhussain222786k-dev/student-grade-management-system.git
```

### 2. Open Project

```bash
cd student-grade-management-system
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

```bash
python main.py
```

or

```bash
py main.py
```

---

## 📦 Dependencies

```
tabulate
```

---

## 📄 Sample Student Data

```json
[
    {
        "name": "Ali",
        "roll_number": "SE-101",
        "marks": {
            "Math": 90,
            "English": 85,
            "Programming": 95
        }
    }
]
```

---

## 📚 Concepts Covered

- Variables
- Data Types
- Loops
- Functions
- Object-Oriented Programming (OOP)
- File Handling
- Exception Handling
- JSON
- Modules
- Virtual Environment
- Pip
- Third-Party Package (Tabulate)
- Input Validation
- Searching Algorithms
- Sorting
---

## 👨‍💻 Author

**Name:** Qadir Hussain

**University:** Capital University of Science and Technology (CUST)

**Program:** BS Software Engineering

---

## 📄 License

This project was developed for educational purposes as part of the OvacSol AI Internship Training Program.
