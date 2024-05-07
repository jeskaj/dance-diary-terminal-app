from student import Student, add_student, view_students


def main_menu():
    print('\nPlease select from the following options:')
    selection_1 = input(print('Syllabus: 1\nStudents: 2\nLessons: 3'))

    if selection_1 == 1:
        print('You have selected Syllabus.  This part of the program is yet to be written')
        
    elif selection_1 == 2:
        print('\nPlease select from the following options:')
        selection_2 = input(print('\nView student details: 1\nAdd a new student: 2'))
            
        if selection_2 == 1:
            view_students()
        elif selection_2 == 2:
            add_student()
        else:
            print('Invalid selection')

    elif selection_1 == 3:
        print('You have selected Lessons.  This part of the program is yet to be written')
    else:
        print('Invalid selection')

print('\nWelcome to Dance Diary!')

main_menu()
