# Week 1 Project Write-up

## Student Record & Grade Management System

This project was developed as part of the Week 1 AI Internship Training Program at OvacSol Pvt. Ltd. The objective was to build a command-line application that applies all the Python concepts learned during the first week.

### Variables

Variables are used throughout the project to store student names, roll numbers, subject marks, menu choices, totals, averages, and grades.

### Data Types

The project uses different Python data types, including strings for names and roll numbers, integers and floats for marks, dictionaries for storing subject-wise marks, and lists for storing multiple student records.

### Loops

Loops are used throughout the application to display the menu continuously, iterate through student records, collect subject information, search students by name, display sorted student lists, and print student marks.

### Functions

The project uses multiple reusable functions such as adding students, updating marks, searching students, sorting students, viewing student records, deleting students, calculating total marks, calculating average marks, and calculating grades.

### Object-Oriented Programming (OOP)

The Student class was implemented using Object-Oriented Programming principles. It contains student attributes such as name, roll number, and subject marks. Methods were also implemented to convert student objects to dictionaries and vice versa.

### File Handling

Student data is permanently stored in a JSON file (students.json). The application reads existing data when it starts and writes updated data whenever changes are made.

### Exception Handling

The application uses try-except blocks to handle invalid user input, missing JSON files, invalid JSON data, incorrect marks, and unexpected runtime errors. Input validation also prevents empty subject names, duplicate subject names, duplicate roll numbers, and invalid marks.


### Modules

The project is divided into four modules:

- main.py
- student.py
- file_manager.py
- grade_utils.py

This modular structure improves readability, maintainability, and code reusability.

### Virtual Environment

A dedicated virtual environment (venv) was created to isolate project dependencies from the global Python installation.

### Pip

The project uses the third-party package **tabulate**, which was installed using pip. The installed packages are listed in requirements.txt for easy setup on another system.

### Conclusion

This project successfully demonstrates the practical implementation of Python fundamentals through a real-world command-line application. It incorporates Object-Oriented Programming, Functions, Loops, File Handling, Exception Handling, Modules, Virtual Environments, Pip, JSON data storage, searching, sorting, and input validation.

