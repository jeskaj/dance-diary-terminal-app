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
    
    # Print confirmation message
    print((f'You have added a new student with the following details:\nName: {new_student.name}\nEmail: {new_student.email}\nMobile: {new_student.mobile}'))
    
    # Store new student details in dicitonary format
    new_student_dict = {
        'name': name,
        'email': email,
        'mobile': mobile
    }
    print(new_student_dict)

    # Store student details dictionary in list and export to .json file
    with open('students.json', 'w') as f:
        students = [new_student_dict]
        json.dump(students, f, indent=4)


    # with open('students.json', 'w') as f:
        # students = json.load(f)
        # students.append(new_student_dict)
        # print(students)
        # json.dump(students, f, indent=4)

def view_students():
    with open('students.json') as f:
        students = json.load(f)
        print(students)