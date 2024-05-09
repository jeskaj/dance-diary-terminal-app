"""
This module defines functions for working with Students' Repertoires
"""

import json
from syllabus import print_step, dance_set


def new_repertoire(student_name: str):
    """
    Create repertoire file for new student, based on current Syllabus
    """
    # Load syllabus data and store in local variable
    with open('syllabus.json') as f:
        repertoire = json.load(f)
    # For each step in the repertoire, add keys 'started' and 'competent'
    for step in repertoire:
        step['status'] = 'New'
    filename = f"{student_name}".replace(' ', '')
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
    filtered_steps = sort_steps([step for step in repertoire if step['status'] == status])
    return filtered_steps


def steps_from_dance(repertoire: list, dance: str):
    """
    Filter a list of step dictionaries to create a new list only including steps from
    the specified dance, sorted by level
    """
    filtered_steps = sort_steps([step for step in repertoire if step['dance'] == dance])
    return filtered_steps


def view_repertoire(student_name: str):
    """
    Display repertoire of Started and Competent steps for student
    """
    filename = f"{student_name}".replace(' ', '')
    # Load data from repertoire .json file based on student name provided
    with open(f'repertoire/{filename}.json') as f:
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
        print(dance.capitalize())
    # Get user selection
    dance_selection = input('\nEnter a dance from the above list:  ')

    # Validate user selection
    while dance_selection.lower() not in dances:
        dance_selection = input('\nINVALID INPUT.  Enter a dance from the above list:  ')

    return dance
    

# print(f'\nAVAILABLE NEW STEPS IN {dance_selection.upper()}')


def update_repertoire(student_name):
    """
    Updates student's repertoire by either adding a new step (ie update status to Started)
    or indicate when student becomes competent in a step (ie update status from Started to Competent)
    """
    # Load student's repertoire and store in local variable
    filename = f"{student_name}".replace(' ', '')
    with open(f'repertoire/{filename}.json') as f:
        repertoire = json.load(f)
    
    # Present user with add or update options
    print('\nOPTIONS:')
    print('[a]  Add new step')
    print('[u]  Update status of current step/s')
    print('[0]  Return to Student Menu')
    selection = input('\nEnter a, u or 0:  ')
    # print(selection)
    
    while selection != 0:
        # Check input validity
        if selection not in ('a', 'u'):
            selection = input('\nINPUT INVALID:  Please eEnter a, u or 0 (refer menu above):  ')

        elif selection == 'a':
            # Call function to display available dances & input a selection
            # GETTING STUCK IN A LOOP HERE????
            dance_selection = select_dance(f'repertoire/{filename}.json')
            # Create list of addable steps by calling functions to filter repertoire for steps from the chosen dance, with status New
            addable_steps = steps_with_status(steps_from_dance(repertoire, dance_selection), 'New')
            # For each addable step, call function to print step details in readable format
            for step in addable_steps:
                print_step(step)

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





if __name__ == '__main__':
    # view_repertoire('Andrea Tucker')
    for step in steps_with_status(steps_from_dance(test_repertoire, 'Waltz'), 'Started'):
        print_step(step)
    # pass