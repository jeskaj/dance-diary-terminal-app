"""
Main module of application, containing menu structure and
functionality, from which the program is run
"""

from art import tprint
from color50 import css, constants
from student import (
    add_student,
    view_students,
    update_student,
    update_student_repertoire,
)
from syllabus import view_syllabus, view_dance


# Define colors using color50 module
blueviolet = css('blueviolet')
lightcoral = css('lightcoral')
darkgreen = css('darkgreen')


def print_main_menu():
    """
    Prints MAIN MENU options
    """
    print(f"\n{blueviolet.bg()}MAIN MENU:{constants.RESET}")
    print(f"{blueviolet}[1]  Syllabus")
    print(f"[2]  Students")
    print(f"[3]  Lessons (Coming soon!)")
    print(f"[0]  Exit Program{constants.RESET}\n")


def print_syllabus_menu():
    """
    Prints 2nd level SYLLABUS MENU options
    """
    print(f"\n{darkgreen.bg()}SYLLABUS MENU:{constants.RESET}")
    print(f"{darkgreen}[1]  View Entire Syllabus")
    print(f"[2]  View Syllabus by Dance")
    print(f"[0]  Return to Main Menu\n{constants.RESET}")


def print_student_menu():
    """
    Prints 2nd level STUDENT MENU options
    """
    print(f"\n{constants.BLUE_BG}STUDENT MENU:{constants.RESET}")
    print(f"{constants.BLUE}[1]  Add New Student")
    print(f"[2]  View Student Contact Details & Repertoire")
    print(f"[3]  Update Student Contact Details")
    print(f"[4]  Update Student Repertoire")
    print(f"[0]  Return to Main Menu{constants.RESET}\n")


# Lessons module not yet implemented
def print_lesson_menu():
    """
    Prints 2nd level LESSON MENU options
    """
    print("\nLESSON MENU:")
    print("[1]  Add Lesson")
    print("[2]  View Lessons")
    print("[3]  Update Lesson")
    print("[0]  Return to Main Menu\n")


def syllabus_menu():
    """
    Enables user to make a selection from SYLLABUS MENU
    """
    # Call function to print syllabus menu
    print_syllabus_menu()
    # Get user input
    selection_2 = input("Please enter 1, 2 or 0: ")

    # Unless user has entered 0 to exit menu, check input against valid options
    while selection_2 != "0":
        # Call relevant function, depnding on user input
        if selection_2 == "1":
            view_syllabus("syllabus.json")
        elif selection_2 == "2":
            view_dance("syllabus.json")
        else:
            # If selection is invalid, ask for new input
            print(f"\n{constants.RED}INVALID INPUT:  Please try again.{constants.RESET}")

        # When user returns from above-chosen function, print syllabus menu and ask for input
        print_syllabus_menu()
        selection_2 = input("Please enter 1, 2, 3 or 0: ")


def student_menu():
    """
    Enables user to make a selection from STUDENT MENU
    """
    # Call function to print student menu
    print_student_menu()
    # Get user input
    selection_2 = input("Please enter 1, 2, 3 or 0: ")

    # Unless user has entered 0 to exit menu, check input against valid options
    while selection_2 != "0":
        # Call relevant function, depnding on user input
        if selection_2 == "1":
            add_student()
        elif selection_2 == "2":
            view_students()
        elif selection_2 == "3":
            update_student()
        elif selection_2 == "4":
            update_student_repertoire()
        else:
            # If selection is invalid, ask for new input
            print(f"\n{constants.RED}INVALID INPUT:  Please try again.{constants.RESET}")

        # When user returns from above-chosen function, print student menu and ask for input
        print_student_menu()
        selection_2 = input("Please enter 1, 2, 3 or 0: ")


def lesson_menu():
    """
    Intended to enable user to make a selection from LESSON MENU
    (functionality not yet developed)
    """
    print(f"\n{lightcoral.bg()}*** You selected [3] LESSONS ***{constants.RESET}")
    print(
        f"{lightcoral}This module will enable you to schedule lessons and create lesson plans for your students."
    )
    print(f"It will be released in a future update. Please make another selection.{constants.RESET}")


def main_menu():
    """
    Start of program - enables user to make a selection from MAIN MENU
    """
    print("\nTo open your Dance Diary, please make a selection from the menu:")
    # Call function to print main menu
    print_main_menu()
    # Get user selection
    selection_1 = input("Please enter 1, 2, 3 or 0: ")

    # Unless user has entered 0 to exit the program, check input against valid options
    while selection_1 != "0":
        # Call relevant function to display 2nd level menu, based on user input
        if selection_1 == "1":
            syllabus_menu()
        elif selection_1 == "2":
            student_menu()
        elif selection_1 == "3":
            lesson_menu()
        else:
            # If selection is invalid, ask for new input
            print(f"\n{constants.RED}INVALID INPUT:  Please try again.{constants.RESET}")

        # When user returns from above-chosen function, print main menu and ask for input
        print_main_menu()
        selection_1 = input("Please enter 1, 2, 3 or 0: ")

    # Print farewell message
    print(f'\n{blueviolet}=========================================================================')
    print(
        "\nYou have closed your Dance Diary. We hope you'll make another entry soon!"
    )
    tprint(f'\n                GOODBYE\n', font='sheqi')
    print(f'========================================================================={constants.RESET}')
    quit()

# Start of program - print welcome message
print(f'\n{blueviolet}=========================================================================')
tprint(f'\n         WELCOME    TO', font='sheqi')
tprint(f'   Dance Diary!')
print(f'========================================================================={constants.RESET}')

# Call function to display main menu
main_menu()
