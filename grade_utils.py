"""
Utility functions for grade calculation.
"""


def calculate_total(marks):
    """
    Calculate total marks.

    Parameters:
    marks (dict)

    Returns:
    int
    """

    return sum(marks.values())


def calculate_average(marks):
    """
    Calculate average marks.

    Parameters:
    marks (dict)

    Returns:
    float
    """

    if len(marks) == 0:
        return 0

    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    """
    Return letter grade based on average.
    """

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"
    