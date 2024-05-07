"""
This module defines the class Student and functions related to creating and editing instances of student.
"""

import json


class Student:
    """
    Represents a dance student
    """
    def __init__(self, name: str, email: str, mobile: str) -> None:
        """
        Creates a new instance of Student

        Parameters
        ----------
        name : str
            Name of student
        email : str
            Email of student
        mobile : str
            Mobile telephone number of student
        """
        self.name = name
        self.email = email
        self.mobile = mobile


def add_student():
    """
    Function to allow user to input new student details
    """
    # Get student details via user input
    name = input("Enter student's full name: ")
    email = input("Enter student's email: ")
    mobile = input("Enter student's mobile phone number: ")
    # Create new instance of Student using user input
    new_student = Student(name, email, mobile)
    # Store new student details in dicitonary format
    new_student_dict = {
        'name': name,
        'email': email,
        'mobile': mobile
    }

    # Load existing students.json data & add new student data
    with open('students.json') as f:
        students = json.load(f)
        students.append(new_student_dict)
    # Output updated data back to students .json
    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)

    # Print confirmation message displaying new student details and total number of students now stored
    print('\nYou have added a new student with the following details:\n')
    print(f'Name: {new_student.name}\nEmail: {new_student.email}\nMobile: {new_student.mobile}')
    print(f'\nTotal Number of Students: {len(students)}')

def view_students():
    # View details of all current students
    with open('students.json') as f:
        students = json.load(f)
        print(students)
    