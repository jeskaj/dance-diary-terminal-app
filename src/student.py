"""
This module defines the class Student and functions related to creating, viewing and editing instances of student.
"""

import json
from repertoire import new_repertoire, view_repertoire


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
    name = input("Enter student's full name (or 0 to quit): ")
    # Check a student with name entered does not already exist
    with open('students.json') as f:
        students = json.load(f)
    # Create list of student names
    student_names = [name['name'].lower() for name in students]
    
    if name != '0':
        # Check if name input is in list of existing student names
        if name.lower() in student_names:
            print(f"\n*** ERROR:  Student with name {name} already exists.  Cannot add student. ***")
        else:
            email = input("Enter student's email: ")
            mobile = input("Enter student's mobile phone number: ")
            # Create new instance of Student using user input
            new_student = Student(name, email, mobile)
            # Store new student details in dicitonary format
            new_student_dict = {
                'name': name,
                'email': email,
                'mobile': mobile,
                'repertoire': f"{name}.json".replace(' ', '')
            }

            # Load existing students.json data
            with open('students.json') as f:
                students = json.load(f)
                # Append new student data to existing data
                students.append(new_student_dict)
            # Output updated data back to students.json
            with open('students.json', 'w') as f:
                json.dump(students, f, indent=4)

            # Create repertoire file for new student
            new_repertoire(new_student_dict['repertoire'])

            # Print confirmation message displaying new student details and total number of students now stored
            print('\nYou have added a new student with the following details:\n')
            print(f'Name: {new_student.name}\nEmail: {new_student.email}\nMobile: {new_student.mobile}')
            print(f"{new_student.name}'s repertoire is stored in the file {new_student_dict['repertoire']}")
            print(f'\nYour total number of students is now: {len(students)}')


def select_student():
    # Find and return a single valid student name
    with open('students.json') as f:
        students = json.load(f)
    # Sort students by name
    students_sorted = sorted(students, key=lambda d: d['name'])
    # Create list of student names
    student_names = [name['name'].lower() for name in students_sorted]
    # Create variable to track whether or not student name has been found
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


def print_student_details(student: dict):
    print(f"\nSTUDENT: {student['name']}")
    print(f"Email: {student['email']}")
    print(f"Mobile: {student['mobile']}")


def view_student_deatils():
    # Print details for a single student
    with open('students.json') as f:
        students = json.load(f)
        # Sort students by name
        students_sorted = sorted(students, key=lambda d: d['name'])
        # Get student name from user
        name = select_student()
        for student in students_sorted:
            # Print student details, where input name is found in list of student names
            if student['name'].lower() == name.lower():
                print_student_details(student)
                view_repertoire(student['name'])


def view_students():
    # View details for all current students, or a single student
    with open('students.json') as f:
        students = json.load(f)
        students_sorted = sorted(students, key=lambda d: d['name'])

    # Display VIEW STUDENT DETAILS menu to user
    print('\nVIEW STUDENT DETAILS')
    print('[a]  View contact details for all students')
    print('[s]  Select a single student to view contact details & repertoire progress')

    # Get menu selection input from user
    selection = input('\nEnter a or s to view student details:  ')

    # Validate user input
    while selection != 'a' and selection != 's':
        selection = input("\nInvalid input. Enter 'a' to view all students or 's' to select a single student:  ")
    
    # If a entered, display all students
    if selection == 'a':
        print('\nSTUDENT CONTACT DETAILS:')
        for student in students_sorted:
            print_student_details(student)
    # If s entered, run function to find & display details of single student
    elif selection == 's':
        view_student_deatils()


def update_student():
    # Call function to get name from user and check its validity
    name = select_student()
    # Load student data
    with open('students.json') as f:
        students = json.load(f)
    print('\nCURRENT STUDENT DETAILS:')
    # Find matching student and print its data
    for student in students:
        if student['name'].lower() == name.lower():
            print_student_details(student)
    # Print UPDATE STUDENT DETAILS menu
    print('\nUPDATE STUDENT DETAILS')
    print('[e]  Update email')
    print('[m]  Update mobile')
    print('[0]  Return to Student Menu')
    # Get menu selection from user
    selection = input('\nEnter n, e or m to update student details:  ')

    # Unless user entered 0 to return to previous menu, check input is valid
    while selection != '0':
        # Instruct user to try again, until they enter a valid selection
        while selection != 'e' and selection != 'm':
            selection = input("Invalid input. Enter 'n', 'e', or 'm' (see Menu options above):  ")
            # Exit loop if 0 is entered
            if selection == '0':
                break
        
        student_found = False
        while student_found == False:
            for student in students:
                if student['name'].lower() == name.lower():
                    student_found = True
                    # If e entered, update value of email and set relevant confirmation msg
                    if selection == 'e':
                        new_email = input('Enter new email:  ')
                        student['email'] = new_email
                        confirmation_msg = f"{student['name']}'s email has been updated to: {student['email']}"
                    # If m entered, update value of mobile and set relevant confirmation msg
                    elif selection == 'm':
                        new_mobile = input('Enter new mobile:  ')
                        student['mobile'] = new_mobile
                        confirmation_msg = f"{student['name']}'s mobile has been updated to: {student['mobile']}"

            # Output updated data back to students .json
            with open('students.json', 'w') as f:
                json.dump(students, f, indent=4)
            print(confirmation_msg)
        break
        

if __name__ == '__main__':
    # view_students()
    # view_student_deatils()
    # update_student()
    pass