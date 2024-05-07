"""
This module defines the class Student and functions related to creating, viewing and editing instances of student.
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


# Functions for accessing & operating on Student data stored in students.json

def add_student():
    """
    Function to allow user to input new student details
    """
    # Get student details via user input
    print('\n*** CREATE NEW STUDENT ***')
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
    print(f'\nYour total number of students is now: {len(students)}')


def select_student():
    # Select a single student
     with open('students.json') as f:
        students = json.load(f)
        # Sort students by name
        students_sorted = sorted(students, key=lambda d: d['name'])
        # Create list of student names
        student_names = [name['name'].lower() for name in students_sorted]
        student_found = False
        # Get student name from user
        name = input('Enter name of student:  ')
        # Check if name input is in list of student names
        if name.lower() in student_names:
            student_found = True
        while student_found == False:
            print(f"\n*** ERROR:  There is no student named {name}.  Please enter a name from the following list:  ***\n")
            for student in students_sorted:
                print(student['name'])
            # Get student name from user
            name = input('\nEnter the name of a student from the above list:  ')
            if name.lower() in student_names:
                student_found = True
        return name



def view_student_details():
    # Select a single student for viewing their details
     with open('students.json') as f:
        students = json.load(f)
        # Sort students by name
        students_sorted = sorted(students, key=lambda d: d['name'])
        # Create list of student names
        student_names = [name['name'].lower() for name in students_sorted]
        student_found = False
        # Get student name from user
        name = input('Enter name of student:  ')
        # Check if name input is in list of student names
        if name.lower() in student_names:
            student_found = True
        while student_found == False:
            print(f"\n*** ERROR:  There is no student named {name}.  Please enter a name from the following list:  ***\n")
            for student in students_sorted:
                print(student['name'])
            # Get student name from user
            name = input('\nEnter the name of a student from the above list:  ')
            if name.lower() in student_names:
                student_found = True
        for student in students_sorted:
            if student['name'].lower() == name.lower():
                print(f"\n{student['name']}")
                print(f"Email: {student['email']}")
                print(f"Mobile: {student['mobile']}\n")


def view_all_students():
    # View details of all current students
    with open('students.json') as f:
        students = json.load(f)
        students_sorted = sorted(students, key=lambda d: d['name'])
        print('\nVIEW STUDENT DETAILS')
        print('[a]  View all students')
        print('[s]  Select a single student')
        selection = input('\nEnter a or s to view student details:  ')
        while selection != 'a' and selection != 's':
            selection = input("\nInvalid input. Enter 'a' to view all students or 's' to select a single student:  ")
        if selection == 'a':
            for student in students_sorted:
                print(student['name'])
                print(f"Email: {student['email']}")
                print(f"Mobile: {student['mobile']}\n")
        elif selection == 's':
            view_student_details()
        

# def view_student_deatils_v2():
#     with open('students.json') as f:
#         students = json.load(f)
#         students_sorted = sorted(students, key=lambda d: d['name'])
#         print('\nVIEW STUDENT DETAILS')
#         print('[a]  View all students')
#         print('[s]  Select a single student')
#         selection = input('\nEnter a or s to view student details:  ')
#         while selection != 'a' and selection != 's':
#             selection = input("\nInvalid input. Enter 'a' to view all students or 's' to select a single student:  ")
#         if selection == 'a':
#             for student in students_sorted:
#                 print(student['name'])
#                 print(f"Email: {student['email']}")
#                 print(f"Mobile: {student['mobile']}\n")
#         elif selection == 's':
#             view_student_details()


if __name__ == '__main__':
    view_all_students()
    # view_student_details()
