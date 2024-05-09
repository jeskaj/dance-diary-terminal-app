import json
import string

# From student.py

# Version of function to select a single student which also included printing the student's details
# updated version paired down to only include selection of single student, so it could be re-used for editing as well
def view_student_details_V1():
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

# Changing new student validation
# if name != '0':
#         # Check that a student with name entered does not already exist
#         if student_name_check(name) == True:
#             name = (f"\n*** ERROR:  Student with name {name} already exists.  Please enter a different name (or 0 to cancel):  ")


def student_name_check(name: str):
    """ Checks that a student of the name entered does not already exist

    Returns
    -------
    bool :
        Returns True if a student of the name entered already exists
    """
    with open('students.json') as f:
        students = json.load(f)
    # Create list of student names
    student_names = [name['name'].lower() for name in students]
    # Check if name input is in list of student names
    if name.lower() in student_names:
        return True
    else:
        return False


# New Student - removed test line that prints name of repertoire .json file created
# print(f"{new_student.name}'s repertoire is stored in the file {new_student_dict['repertoire']}")


# Started writing code to incorporate Edit/Update functionality within View functionality ie view_students() function
# Not sure how to achieve passing student selection from one function to another, decided to leave as separate functions
        # Present menu options for updating student details
        # print('\nOPTIONS:')
        # print('[c]  Update contact details')
        # print('[r]  Update repertoire')
        # print('[0]  Return to Student Menu')
        # # Get user selection
        # selection2 = input('\nPlease enter c, r or 0:  ')

        # while selection2 != '0':
        #     # Handle invalid input
        #     if selection2 not in ('c', 'r'):
        #         selection2 = input("\nInvalid input. Enter c, r or 0 (refer menu above):  ")
            
        #     # If c entered, call function to edit student contact details
        #     elif selection2 == 'c':
        #         update_student()

        #     # If r entered, call function to update student repertoire
        #     elif selection2 == 'r':
        #         print('\nYou have selected Update Repertoire - functionality not yet completed.')
        #         break 


# Adding 'repertoire' filename to existing students
def add_repertoire_existing_students():
    with open('students.json') as f:
        students = json.load(f)
    for student in students:
        student['repertoire'] = f"{student['name']}.json".replace(' ', '')
    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)

# From syllabus.py

# Original simple function that returns syllabus data in raw list of dictionaries format
def view_syllabus(filename):
    # Function to view syllabus data stored in .json file
    with open(filename) as f:
        syllabus_list_of_dicts = json.load(f)
        return syllabus_list_of_dicts
    

# From repertoire.py

def create_repertoires():
    with open('students.json') as f:
        students = json.load(f)
    for student in students:
        # Call function to create repertoire file for each existing student
        new_repertoire(student['name'])

name = 'sarah rogers'
print(string.capwords(name))