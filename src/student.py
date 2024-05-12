"""
This module defines the class Student and functions related to
creating, viewing and editing student data.
"""

from color50 import css, constants
import json
from repertoire import (
    repertoire_filename,
    new_repertoire,
    view_repertoire,
    update_repertoire,
)


# Define colors using color50 module
teal = css('teal')


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
    print(f"\n{teal.bg()}*** Create New Student ***{constants.RESET}")
    name = input("Enter student's full name (or 0 to cancel): ")

    # Unless user entered 0 to return to previous menu, check input is valid
    if name != "0":
        # Check that a student with name entered does not already exist
        with open("students.json") as f:
            students = json.load(f)
        # Create list of existing student names
        student_names = [name["name"].lower() for name in students]

        # Check if name input is in list of existing student names
        if name.lower() in student_names:
            # Advise user if student with name input already exists and return to menu
            print(
                f"\n{constants.RED}*** ERROR:  Student with name {name} already exists.  Cannot add student. ***{constants.RESET}"
            )
        # If a student with name input does not already exist, continue
        else:
            # Get student's email & mobile from user
            email = input("Enter student's email: ")
            mobile = input("Enter student's mobile phone number: ")
            # Give user opportunity to confirm data entered is correct before creating student
            print(
                f"\n{constants.RED}*** Please check that the following details are correct - student name cannot be changed once created ***{constants.RESET}\n"
            )
            print(f"{teal}Name: {name}\nEmail: {email}\nMobile: {mobile}{constants.RESET}")
            # Get user input to confirm user creation
            proceed = input(
                "\nEnter y to create this student, or any other key to cancel:  "
            )

            if proceed == "y":
                # Create new instance of Student using user input
                new_student = Student(name, email, mobile)
                # Store new student details in dicitonary format
                new_student_dict = {
                    "name": name,
                    "email": email,
                    "mobile": mobile,
                    "repertoire": repertoire_filename(name),
                }
                # Load existing students.json data into local variable (list of dictionaries)
                with open("students.json") as f:
                    students = json.load(f)
                    # Append new student dictionary to existing data
                    students.append(new_student_dict)
                # Output updated data back to students.json
                with open("students.json", "w") as f:
                    json.dump(students, f, indent=4)

                # Create repertoire file for new student
                new_repertoire(new_student_dict["repertoire"])

                # Print confirmation message displaying new student details and total number of students now stored
                print(f"\n{teal}You have added a new student with the following details:{constants.RESET}\n")
                print(
                    f"Name: {new_student.name}\nEmail: {new_student.email}\nMobile: {new_student.mobile}"
                )
                print(f"\n{teal}Your total number of students is now: {len(students)}{constants.RESET}")
            
            else:
                print(f"\n{constants.MAGENTA}*** CREATE STUDENT CANCELLED:  New student NOT added ***{constants.RESET}")


def select_student():
    """
    Allows user to select an existing student

    Returns
    -------
    str :
        The name of a valid student
    """
    # Load students.json and store data in local variable (a list of dictionaries)
    with open("students.json") as f:
        students = json.load(f)
    # Sort students by name
    students_sorted = sorted(students, key=lambda d: d["name"])
    # Create list of student names
    student_names = [name["name"].lower() for name in students_sorted]
    # Create variable to track whether or not student name has been found
    student_found = False
    # Get student name from user
    name = input("\nEnter name of student (or any key, to see a list of names):  ")
    # Check if name input is in list of student names
    if name.lower() in student_names:
        student_found = True
    # While valid student name has not been entered, ask user for input again
    while student_found == False:
        # Warn user name entered is not valid & display list of valid names
        print(
            f"\n{constants.RED}*** ERROR:  There is no student named {name}.  Please enter a name from the following list:  ***{constants.RESET}\n"
        )
        for student in students_sorted:
            print(f'{teal}{student["name"]}{constants.RESET}')
        # Get student name from user
        name = input("\nEnter the name of a student from the above list:  ")
        # Check validity of new name entered
        if name.lower() in student_names:
            # End loop if name is valid
            student_found = True
    # Return valid student name
    return name


def print_student_details(student: dict):
    """
    Prints student contact details in readable format

    Parameters
    ----------
    student : dict
        A dictionary contain student information, including the
        keys 'name', 'email' and 'mobile'
    """
    print(f"\n{teal}STUDENT: {student['name']}")
    print(f"Email: {student['email']}")
    print(f"Mobile: {student['mobile']}{constants.RESET}")


def view_student_deatils():
    """
    Prints contact details and repertoire for a single student
    """
    # Load students.json and store data in local variable (list of dictionaries)
    with open("students.json") as f:
        students = json.load(f)
        # Sort students by name
    students_sorted = sorted(students, key=lambda d: d["name"])
    # Call function to get valid student name from user
    name = select_student()
    for student in students_sorted:
        # Print student details, where input name is found in list of student names
        if student["name"].lower() == name.lower():
            # Call function to print student contact details
            print_student_details(student)
            # Call function to print student repertoire
            view_repertoire(student["name"])


def view_students():
    """
    Provides functionality to view contact details for all current students,
    or a single student's contact details & repertoire
    """
    # Load students.json and store data in local variable (list of dictionaries)
    with open("students.json") as f:
        students = json.load(f)
    # Sort students by name
    students_sorted = sorted(students, key=lambda d: d["name"])

    # Display VIEW STUDENT DETAILS menu to user
    print(f"\n{teal.bg()}View Student Details:{constants.RESET}")
    print(f"{teal}[a]  View contact details for all students")
    print(f"[s]  Select a single student to view contact details & repertoire progress{constants.RESET}")

    # Get menu selection input from user
    selection = input("\nEnter a or s to view student details:  ")

    # Validate user input
    while selection not in ("a", "s"):
        selection = input(f"\n{constants.RED}INVALID INPUT:{constants.RESET} Enter a or s (refer above menu):  ")

    # If a entered, display contact details of all students
    if selection == "a":
        print(f"\n{teal.bg()}STUDENT CONTACT DETAILS:{constants.RESET}")
        for student in students_sorted:
            print_student_details(student)
        # Print total number of students, based on length of list
        print(f"\n{teal}*** TOTAL STUDENTS: {len(students)} ***{constants.RESET}")

    # If s entered, run function to find & display contact details & repertoire of single student
    elif selection == "s":
        print(f'\n{teal.bg()}*** Select student to view ***{constants.RESET}')
        # Call function to find & display details of chosen student
        view_student_deatils()


def update_student():
    """
    Function to update student contact details
    """
    print(f'\n{teal.bg()}*** Select student to update ***{constants.RESET}')
    # Call function to get a valid student name from user
    name = select_student()
    # Load student data into local variable (list of dictionaries)
    with open("students.json") as f:
        students = json.load(f)
    print(f"\n{teal.bg()}CURRENT STUDENT DETAILS:{constants.RESET}")
    # Find matching student and print its data, so user can review current contact details
    for student in students:
        if student["name"].lower() == name.lower():
            print_student_details(student)
    # Print UPDATE STUDENT DETAILS menu
    print(f"\n{teal.bg()}Update Student Details{constants.RESET}")
    print(f"{teal}[e]  Update email")
    print("[m]  Update mobile")
    print(f"[0]  Return to Student Menu{constants.RESET}")
    # Get menu selection from user
    selection = input("\nEnter e or m to update student details (or 0 to cancel):  ")

    # Unless user entered 0 to return to previous menu, check input is valid
    while selection != "0":
        # Instruct user to try again, until they enter a valid selection
        while selection not in ("e", "m"):
            selection = input(f"{constants.RED}INVALID INPUT:{constants.RESET} Enter e or m (see Menu options above):  ")
            # Exit loop if 0 is entered
            if selection == "0":
                break

        if selection == "0":
            break

        # Once user has made a valid selection, find student data
        student_found = False
        while student_found == False:
            for student in students:
                if student["name"].lower() == name.lower():
                    student_found = True
                    # If e entered, update value of email and set relevant confirmation msg
                    if selection == "e":
                        new_email = input("Enter new email:  ")
                        student["email"] = new_email
                        confirmation_msg = f"\n{teal}{student['name']}'s email has been updated to:{constants.RESET} {student['email']}"
                    # If m entered, update value of mobile and set relevant confirmation msg
                    elif selection == "m":
                        new_mobile = input("Enter new mobile:  ")
                        student["mobile"] = new_mobile
                        confirmation_msg = f"\n{teal}{student['name']}'s mobile has been updated to:{constants.RESET} {student['mobile']}"

            # Output updated data back to students .json
            with open("students.json", "w") as f:
                json.dump(students, f, indent=4)
            # Print confirmation messag, confirming to user that either email or mobile was updated
            print(confirmation_msg)
        break


def update_student_repertoire():
    """
    Updates student's repertoire by either adding a new step (ie update status to Started)
    or indicating when student becomes competent in a step (ie update status from Started to Competent)
    """
    print(f'\n{teal.bg()}*** Select student for updating repertoire ***{constants.RESET}')
    # Call function to get a valid student name from the user
    name = select_student()
    # Call function to update repertoire for selected student
    update_repertoire(name)


if __name__ == "__main__":
    pass
