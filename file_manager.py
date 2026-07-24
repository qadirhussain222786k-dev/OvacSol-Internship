import json
from student import Student


FILE_NAME = "students.json"


def load_students():
    """
    Load all students from students.json.

    Returns:
        list: List of Student objects.
    """

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

            students = []

            for student_data in data:
                students.append(Student.from_dict(student_data))

            return students

    except FileNotFoundError:
        print("students.json not found. Creating a new file...")
        return []

    except json.JSONDecodeError:
        print("Error: students.json contains invalid data.")
        return []

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return []


def save_students(students):
    """
    Save all Student objects into students.json.

    Parameters:
        students (list): List of Student objects.
    """

    try:
        data = []

        for student in students:
            data.append(student.to_dict())

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"Error saving data: {e}")
        