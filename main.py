from tabulate import tabulate

from student import Student
from file_manager import load_students, save_students
from grade_utils import (
    calculate_total,
    calculate_average,
    calculate_grade
)


# Load existing students when program starts
students = load_students()


def find_student(roll_number):
    """
    Find a student by roll number.

    Returns:
        Student object if found, otherwise None.
    """

    for student in students:
        if student.roll_number == roll_number:
            return student

    return None


def add_student():
    """
    Add a new student.
    """

    print("\n========== Add Student ==========")

    try:
        name = input("Enter student name: ").strip()

        roll_number = input("Enter roll number: ").strip()

        # Check duplicate roll number
        if find_student(roll_number):
            print("\nStudent with this roll number already exists.")
            return

        number_of_subjects = int(
            input("Enter number of subjects: ")
        )

        if number_of_subjects <= 0:
            print("Number of subjects must be greater than zero.")
            return

        marks = {}

        for i in range(number_of_subjects):

            subject = input(f"\nSubject {i+1} Name: ").strip()

            # Validate subject name is not empty
            if subject == "":
                print("Subject name cannot be empty.")
                return

            # Prevent duplicate subject names (case-insensitive)
            if subject.lower() in [s.lower() for s in marks]:
                print(f"Subject '{subject}' already entered. Duplicate subjects are not allowed.")
                return

            mark = float(
                input(f"Marks in {subject}: ")
            )

            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100.")
                return

            marks[subject] = mark

        student = Student(
            name,
            roll_number,
            marks
        )

        students.append(student)

        save_students(students)

        print("\nStudent added successfully.")

    except ValueError:
        print("\nInvalid input. Please enter numeric values correctly.")

    except Exception as e:
        print(f"\nError: {e}")


def update_marks():
    """
    Update marks of an existing student.
    """

    print("\n========== Update Student Marks ==========")

    try:

        roll_number = input("Enter Roll Number: ").strip()

        student = find_student(roll_number)

        if student is None:
            print("\nStudent not found.")
            return

        print("\nCurrent Subjects")

        for subject, mark in student.marks.items():
            print(f"{subject} : {mark}")

        subject = input(
            "\nEnter subject to update: "
        ).strip()

        if subject not in student.marks:
            print("\nSubject does not exist.")
            return

        new_marks = float(
            input("Enter new marks: ")
        )

        if new_marks < 0 or new_marks > 100:
            print("Marks should be between 0 and 100.")
            return

        student.marks[subject] = new_marks

        save_students(students)

        print("\nMarks updated successfully.")

    except ValueError:
        print("\nInvalid marks entered.")

    except Exception as e:
        print(f"\nError: {e}")


def display_student(student):
    """
    Display complete student information.
    """

    total = calculate_total(student.marks)

    average = calculate_average(student.marks)

    grade = calculate_grade(average)

    subject_count = len(student.marks)

    print("\n===================================")
    print(f"Name          : {student.name}")
    print(f"Roll Number   : {student.roll_number}")
    print(f"Subject Count : {subject_count}")

    print("\nSubject Marks")

    for subject, mark in student.marks.items():
        print(f"{subject:<15}: {mark}")

    print("-----------------------------------")
    print(f"Total        : {total}")
    print(f"Average      : {average:.2f}")
    print(f"Grade        : {grade}")
    print("===================================")


def view_student():
    """
    View a single student's complete information.
    """

    print("\n========== View Student ==========")

    roll_number = input("Enter Roll Number: ").strip()

    student = find_student(roll_number)

    if student is None:
        print("\nStudent not found.")
        return

    display_student(student)


def search_student_by_name():
    """
    Search for students whose name contains the given text
    (case-insensitive, partial match supported).
    """

    print("\n========== Search Student by Name ==========")

    query = input("Enter name (or part of it) to search: ").strip()

    if query == "":
        print("Search text cannot be empty.")
        return

    matches = [
        student for student in students
        if query.lower() in student.name.lower()
    ]

    if not matches:
        print(f"\nNo students found matching '{query}'.")
        return

    table = []

    for student in matches:
        total = calculate_total(student.marks)
        average = calculate_average(student.marks)
        grade = calculate_grade(average)

        table.append([
            student.name,
            student.roll_number,
            len(student.marks),
            total,
            f"{average:.2f}",
            grade
        ])

    print(f"\nFound {len(matches)} matching student(s):\n")

    print(
        tabulate(
            table,
            headers=[
                "Name",
                "Roll Number",
                "Subjects",
                "Total",
                "Average",
                "Grade"
            ],
            tablefmt="fancy_grid",
            colalign=("left", "center", "center", "center", "center", "center")
        )
    )


def view_all_students():
    """
    Display all students in a table.
    """

    print("\n========== All Students ==========")

    if len(students) == 0:
        print("No student records found.")
        return

    table = []

    for index, student in enumerate(students, start=1):

        total = calculate_total(student.marks)
        average = calculate_average(student.marks)
        grade = calculate_grade(average)

        table.append([
            index,
            student.name,
            student.roll_number,
            len(student.marks),
            total,
            f"{average:.2f}",
            grade
        ])

    print(
        tabulate(
            table,
            headers=[
                "#",
                "Name",
                "Roll Number",
                "Subjects",
                "Total",
                "Average",
                "Grade"
            ],
            tablefmt="fancy_grid",
            colalign=("center", "left", "center", "center", "center", "center", "center")
        )
    )


def sort_students_by_average():
    """
    Display all students sorted by average marks.
    """

    print("\n========== Sort Students by Average ==========")

    if len(students) == 0:
        print("No student records found.")
        return

    order = input("Sort order - (D)escending or (A)scending? [D/A]: ").strip().lower()

    reverse = order != "a"

    sorted_students = sorted(
        students,
        key=lambda s: calculate_average(s.marks),
        reverse=reverse
    )

    table = []

    for index, student in enumerate(sorted_students, start=1):

        total = calculate_total(student.marks)
        average = calculate_average(student.marks)
        grade = calculate_grade(average)

        table.append([
            index,
            student.name,
            student.roll_number,
            len(student.marks),
            total,
            f"{average:.2f}",
            grade
        ])

    print(
        tabulate(
            table,
            headers=[
                "Rank",
                "Name",
                "Roll Number",
                "Subjects",
                "Total",
                "Average",
                "Grade"
            ],
            tablefmt="fancy_grid",
            colalign=("center", "left", "center", "center", "center", "center", "center")
        )
    )


def delete_student():
    """
    Delete a student record, after confirmation.
    """

    print("\n========== Delete Student ==========")

    roll_number = input("Enter Roll Number: ").strip()

    student = find_student(roll_number)

    if student is None:
        print("\nStudent not found.")
        return

    display_student(student)

    confirm = input(
        f"\nAre you sure you want to delete '{student.name}' (Roll No: {student.roll_number})? (Y/N): "
    ).strip().lower()

    if confirm != "y":
        print("\nDeletion cancelled.")
        return

    students.remove(student)

    save_students(students)

    print("\nStudent deleted successfully.")


def show_menu():
    """
    Display the main menu.
    """

    print("\n")
    print("=" * 45)
    print(" Student Record & Grade Management System ")
    print("=" * 45)
    print("1. Add Student")
    print("2. Update Student Marks")
    print("3. View Student")
    print("4. View All Students")
    print("5. Delete Student")
    print("6. Search Student by Name")
    print("7. Sort Students by Average")
    print("8. Exit")
    print("=" * 45)


def main():
    """
    Main program loop.
    """

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            update_marks()

        elif choice == "3":
            view_student()

        elif choice == "4":
            view_all_students()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            search_student_by_name()

        elif choice == "7":
            sort_students_by_average()

        elif choice == "8":

            save_students(students)

            print("\nThank you for using the system.")
            print("Data saved successfully.")

            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
    