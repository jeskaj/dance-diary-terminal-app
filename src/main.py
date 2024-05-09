from student import add_student, view_students, update_student, update_student_repertoire
from syllabus import view_syllabus, view_dance


# DELETE THIS - Error text for later use: 'Invalid input - you must enter a numeric option from the menu.'

def print_main_menu():
    # Prints MAIN MENU options
    print('\nMAIN MENU:')
    print('[1]  Syllabus')
    print('[2]  Students')
    print('[3]  Lessons (Coming soon!)')
    print('[0]  Exit Program\n')


def print_syllabus_menu():
    # Prints 2nd level SYLLABUS MENU options
    print('\nSYLLABUS MENU:')
    print('[1]  View Entire Syllabus')
    print('[2]  View Syllabus by Dance')
    print('[0]  Return to Main Menu\n')


def print_student_menu():
    # Prints 2nd level STUDENT MENU options
    print('\nSTUDENT MENU:')
    print('[1]  Add New Student')
    print('[2]  View Student Contact Details & Repertoire')
    print('[3]  Update Student Contact Details')
    print('[4]  Update Student Repertoire')
    print('[0]  Return to Main Menu\n')


# Lessons module not yet implemented
def print_lesson_menu():
    # Prints 2nd level LESSON MENU options
    print('\nLESSON MENU:')
    print('[1]  Add Lesson')
    print('[2]  View Lessons')
    print('[3]  Update Lesson')
    print('[0]  Return to Main Menu\n')


def syllabus_menu():
    # Enables user to make a selection from SYLLABUS MENU
    print_syllabus_menu()
    selection_2 = int(input('Please enter 1, 2 or 0: '))

    while selection_2 !=0:
        if selection_2 == 1:
            view_syllabus('syllabus.json')
        elif selection_2 == 2:
            view_dance('syllabus.json')
        else:
            print('Invalid selection.  Please try again.')
        
        print_syllabus_menu()
        selection_2 = int(input('Please enter 1, 2, 3 or 0: '))

def student_menu():
    print_student_menu()
    selection_2 = int(input('Please enter 1, 2, 3 or 0: '))

    while selection_2 != 0:
        if selection_2 == 1:
            add_student()
        elif selection_2 == 2:
            view_students()
        elif selection_2 == 3:
            update_student()
        elif selection_2 == 4:
            update_student_repertoire()
        else:
            print('Invalid selection.  Please try again.')

        print_student_menu()
        selection_2 = int(input('Please enter 1, 2, 3 or 0: '))


def lesson_menu():
    print('\n*** You selected [3] LESSONS ***')
    print('This module will enable you to schedule lessons and create lesson plans for your students.')
    print('It will be released in a future update. Please make another selection.')


def main_menu():
    print('\nTo open your Dance Diary, please make a selection from the menu:')
    print_main_menu()
    selection_1 = int(input('Please enter 1, 2, 3 or 0: '))

    while selection_1 != 0:
        if selection_1 == 1:
            syllabus_menu()
        elif selection_1 == 2:
            student_menu()
        elif selection_1 == 3:
            lesson_menu()
        else:
            print('\nInvalid selection.  Please try again.')
        
        print_main_menu()
        selection_1 = int(input('Please enter 1, 2, 3 or 0: '))
    
    print('\nYou have closed your Dance Diary.  We hope you\'ll make another entry soon.  Goodbye!\n')
    quit()


print('\nWelcome to Dance Diary!')

main_menu()
