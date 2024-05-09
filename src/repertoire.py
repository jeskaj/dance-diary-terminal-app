"""
This module defines functions for working with Students' Repertoires
"""

import json
import string
from syllabus import print_step, dance_set


def repertoire_filename(student_name):
    """Function to format name of student into name of .json repertoire file for that student

    Parameters
    ----------
    student_name : str
        Name of student

    Returns
    -------
    str :
        Name of .json repertoire file for student
    """
    return f"{student_name}.json".replace(' ', '').lower()
    

def new_repertoire(filename: str):
    """
    Create repertoire file for new student, based on current Syllabus
    """
    # Load current syllabus data and store in local variable
    with open('syllabus.json') as f:
        repertoire = json.load(f)
    # For each step in the repertoire, add 'status' with value 'New'
    for step in repertoire:
        step['status'] = 'New'
    # print(filename)
    with open(f'repertoire/{filename}', 'w') as f:
        json.dump(repertoire, f, indent = 4)


def sort_steps(repertoire: list):
    """
    Sorts a list of step dictionaries by dance then level
    """
    repertoire_sorted = sorted(repertoire, key=lambda s: (s['dance'], s['level']))
    return repertoire_sorted


def steps_with_status(repertoire: list, status: str):
    """
    Filter a list of step dictionaries to create a new list only including steps with
    the specified status ('New', 'Started' or 'Competent'), sorted by dance then level
    """
    filtered_steps = sort_steps([step for step in repertoire if step['status'].lower() == status.lower()])
    return filtered_steps


def steps_from_dance(repertoire: list, dance: str):
    """
    Filter a list of step dictionaries to create a new list only including steps from
    the specified dance, sorted by level
    """
    filtered_steps = sort_steps([step for step in repertoire if step['dance'].lower() == dance.lower()])
    return filtered_steps


def view_repertoire(student_name: str):
    """
    Display repertoire of Started and Competent steps for student
    """
    filename = repertoire_filename(student_name)
    # Load data from repertoire .json file based on student name provided
    with open(f'repertoire/{filename}') as f:
        repertoire = json.load(f)
    
    # Display dances student has learnt and is in the process of learning
    # Create list of steps in progress
    current_steps = steps_with_status(repertoire, 'Started')
    # Create list of completed steps
    completed_steps = steps_with_status(repertoire, 'Competent')
    
    print(f'\nREPERTOIRE STATUS FOR {student_name.upper()}')

    # Advise if student has not started or completed any steps
    if len(current_steps) == 0 and len(completed_steps) == 0:
        print(f'{student_name} is a new student - you can start them on any Level 1 steps. ')

    # Display steps currently in progress
    current_steps_sorted = sorted(current_steps, key=lambda d: d['dance'])
    if len(current_steps) != 0:
        print('\nSTEPS IN PROGRESS (student is currently learning these steps):')
        for step in current_steps_sorted:
            print_step(step)

    # Display steps student has completed
    completed_steps_sorted = sorted(completed_steps, key=lambda d: d['dance'])
    if len(completed_steps) != 0:
        print('\nSTEPS COMPLETED (student is competent in these steps):')
        for step in completed_steps_sorted:
            print_step(step)


def select_dance(repertroire_filepath: str):
    """
    Allow user to select a dance from those within the student's repertoire
    """
    # Call function to create set of unique dances from student's repertoire
    dances = dance_set(repertroire_filepath)
    # Display list of available dances
    print('\nAVAILABLE DANCES:')
    for dance in dances:
        print(string.capwords(dance))
    # Get user selection
    dance_selection = input('\nEnter a dance from the above list:  ')

    # Validate user selection
    while dance_selection.lower() not in dances:
        dance_selection = input('\nINVALID INPUT.  Enter a dance from the above list:  ')

    return dance_selection
    

def validate_step_choice(new_steps: list):
    # Get name of step to add from user
    step_choice = input('\nEnter the name of a step from the above list to be added:  ')
    # Validate user input
    # Create list of step names
    step_names = [step['step'].lower() for step in new_steps]
    # Check if chosen step is in list of step names
    while step_choice.lower() not in step_names:
        step_choice = input('\nINVALID INPUT:  You must enter the name of a step from above list (or 0 to quit):  ')
        if step_choice == '0':
            break
    return step_choice
    

def update_repertoire(student_name):
    """
    Updates student's repertoire by either adding a new step (ie update status to Started)
    or indicate when student becomes competent in a step (ie update status from Started to Competent)
    """
    # Load student's repertoire and store in local variable
    filename = repertoire_filename(student_name)
    with open(f'repertoire/{filename}') as f:
        repertoire = json.load(f)
    
    # Present user with add or update options
    print('\nOPTIONS:')
    print('[a]  Add new step')
    print('[u]  Update status of current step')
    print('[0]  Return to Student Menu')
    selection = input('\nEnter a or u (or 0 to cancel):  ')
    
    # If user has not input 0 to quit, check validity of input
    if selection != '0':
        # Check input validity
        while selection not in ('a', 'u'):
            selection = input('\nINPUT INVALID:  Please enter a, u or 0 (refer menu above):  ')
            if selection == '0':
                break

        if selection == 'a':
            # Check that student has New steps available (across all dances in syllabus)
            new_steps = steps_with_status(repertoire, 'New')
            if len(new_steps) == 0:
                print(f'{string.capwords(student_name)} has already started learning or become competent in all steps in the syllabus. There are no new steps left to be added.')
            else:
                # Call function to display available dances & allow user to input a selection
                dance_selection = select_dance(f'repertoire/{filename}')
                # Call function to create list of steps from the chosen dance
                dance_steps = steps_from_dance(repertoire, dance_selection)
                # Call function to create list filter the above list down to those with status New
                new_steps = steps_with_status(dance_steps, 'New')

                # Check that student still has some new steps left to learn in chosen dance
                if len(new_steps) == 0:
                    print(f'This student has already started learning all steps in the {dance_selection} syllabus.')
                else:
                    # Create a list for each level of steps found in list of available new steps
                    new_steps_lvl1 = [step for step in new_steps if step['level'] == '1']
                    new_steps_lvl2 = [step for step in new_steps if step['level'] == '2']
                    new_steps_lvl3 = [step for step in new_steps if step['level'] == '3']
                    # Check if student has completed all level 1 steps in dance
                    if len(new_steps_lvl1) != 0:
                        print(f'\nAVAILABLE NEW LEVEL 1 STEPS IN {dance_selection.capitalize()}:')
                        # For each new step, call function to print step details in readable format
                        for step in new_steps_lvl1:
                            print_step(step)
                        # Call function to get user step choice & validate input
                        step_choice = validate_step_choice(new_steps_lvl1)
                    
                    # If level 1 steps all completed, check if student has completed all level 2 steps in dance
                    elif len(new_steps_lvl2) != 0:
                        print(f'\nStudent has completed all Level 1 steps in {dance_selection.upper()}')
                        print(f'\nAVAILABLE NEW LEVEL 2 STEPS IN {dance_selection.upper()}:')
                        # For each new step, call function to print step details in readable format
                        for step in new_steps_lvl2:
                            print_step(step)
                        # Call function to get user step choice & validate input
                        step_choice = validate_step_choice(new_steps_lvl2)

                    # If level 1 & 2 steps all completed, display remaining level 3 steps in dance
                    else:
                        print(f'\nStudent has completed all Level 1 & 2 steps in {dance_selection.upper()}')
                        print(f'\nAVAILABLE NEW LEVEL 3 STEPS IN {dance_selection.upper()}:')
                        # For each new step, call function to print step details in readable format
                        for step in new_steps_lvl3:
                            print_step(step)
                        # Call function to get user step choice & validate input
                        step_choice = validate_step_choice(new_steps_lvl3)

                print(step_choice) # ADD IN CODE TO UPDATE STEP STATUS TO STARTED IN STUDENT REPERTOIRE

        elif selection == 'u':
            print('\nYou have selected Update Step - functionality not yet completed')


test_repertoire = [
    {
        "dance": "Waltz",
        "level": "1",
        "step": "Left Turning Box",
        "status": "Competent"
    },
    {
        "dance": "Waltz",
        "level": "1",
        "step": "Underarm Turn Right",
        "status": "Competent"
    },
    {
        "dance": "Waltz",
        "level": "2",
        "step": "Right Turning Box",
        "status": "Started"
    },
    {
        "dance": "Waltz",
        "level": "2",
        "step": "Simple Twinkle",
        "status": "Started"
    },
    {
        "dance": "Waltz",
        "level": "2",
        "step": "Two Way Underarm Turn",
        "status": "Started"
    },
    {
        "dance": "Waltz",
        "level": "2",
        "step": "Balance and Box",
        "status": "New"
    },
    {
        "dance": "Waltz",
        "level": "2",
        "step": "Face-to-Face Back-to-Back",
        "status": "New"
    },
    {
        "dance": "Waltz",
        "level": "3",
        "step": "Natural Turn",
        "status": "New"
    },
    {
        "dance": "Waltz",
        "level": "3",
        "step": "Natural Turn w/UAT",
        "status": "New"
    },
    {
        "dance": "Rumba",
        "level": "3",
        "step": "Reverse Underarm Turn",
        "status": "New"
    },
    {
        "dance": "Rumba",
        "level": "3",
        "step": "Quick Underarm Turn and Loop",
        "status": "New"
    },
    {
        "dance": "Waltz",
        "level": "3",
        "step": "Progressive Twinkles",
        "status": "New"
    },
    {
        "dance": "Rumba",
        "level": "1",
        "step": "Box Step",
        "status": "New"
    },
    {
        "dance": "Rumba",
        "level": "1",
        "step": "Slow Underarm Turn",
        "status": "New"
    },
    {
        "dance": "Rumba",
        "level": "1",
        "step": "Rumba Walks Fwd and Back",
        "status": "New"
    },
    {
        "dance": "Rumba",
        "level": "1",
        "step": "5th Position Breaks",
        "status": "New"
    },
    {
        "dance": "Rumba",
        "level": "2",
        "step": "Open Break UAT",
        "status": "New"
    },
    {
        "dance": "Rumba",
        "level": "2",
        "step": "Cross Body Lead",
        "status": "New"
    }
]


new_steps_test = [
    {'dance': 'Rumba', 'level': '1', 'step': 'Rumba Walks Fwd and Back', 'status': 'New'},
    {'dance': 'Rumba', 'level': '1', 'step': '5th Position Breaks', 'status': 'New'}
]


if __name__ == '__main__':
    # view_repertoire('Andrea Tucker')
    # for step in steps_from_dance(test_repertoire, 'wALTZ'):
    #     print_step(step)
    # for step in steps_with_status(test_repertoire, 'new'):
    #     print_step(step)
    # print(select_dance('repertoire/sarahrogers.json'))
    # validate_step_choice(new_steps_test)
    pass