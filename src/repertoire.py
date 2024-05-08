"""
This module defines functions for working with Students' Repertoires
"""

import json
from syllabus import print_step


def new_repertoire(student_name):
    # Create repertoire file for new student, based on current Syllabus
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

def view_repertoire(student_name):
    filename = f"{student_name}".replace(' ', '')
    # Load data from repertoire .json file based on student name provided
    with open(f'repertoire/{filename}.json') as f:
        repertoire = json.load(f)
    
    # Display dances student has learnt and is in the process of learning
    current_steps = []
    completed_steps = []
    for step in repertoire:
        # Create list of steps in progress
        if step['status'] == 'Started':
            current_steps.append(step)
        # Create list of completed steps
        elif step['status'] == 'Competent':
            completed_steps.append(step)
    
    print(f'\nREPERTOIRE STATUS FOR {student_name.upper()}')

    # Advise if student has not started or completed any steps
    if len(current_steps) == 0 and len(completed_steps) == 0:
        print(f'{student_name} is a new student - you can start them on any Level 1 steps. ')

    # Display steps currently in progress
    current_steps_sorted = sorted(current_steps, key=lambda d: d['dance'])
    if len(current_steps) != 0:
        print('\nSteps in progress (currently learning):')
        for step in current_steps_sorted:
            print_step(step)

    # Display steps student has completed
    completed_steps_sorted = sorted(completed_steps, key=lambda d: d['dance'])
    if len(completed_steps) != 0:
        print('\nSteps completed (student is competent in these steps):')
        for step in completed_steps_sorted:
            print_step(step)


if __name__ == '__main__':
    view_repertoire('Andrea Tucker')
    pass