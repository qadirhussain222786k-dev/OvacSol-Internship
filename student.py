class Student:
    """
    Student class represents a single student's information.
    """

    def __init__(self, name, roll_number, marks):
        """
        Constructor

        Parameters:
        name (str): Student name
        roll_number (str): Student roll number
        marks (dict): Subject-wise marks
        """

        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def to_dict(self):
        """
        Convert Student object into dictionary
        so it can be stored in JSON.
        """

        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        """
        Convert dictionary back into Student object.
        """

        return cls(
            data["name"],
            data["roll_number"],
            data["marks"]
        )

    def display(self):
        """
        Print student details.
        """

        print("\n========== Student Details ==========")
        print(f"Name        : {self.name}")
        print(f"Roll Number : {self.roll_number}")

        print("\nMarks:")

        for subject, mark in self.marks.items():
            print(f"{subject:<15}: {mark}")
            