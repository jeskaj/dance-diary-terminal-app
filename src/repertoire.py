"""
This module defines functions for working with Students' Repertoires
"""

import json


def new_repertoire(student_name):
    # Create repertoire file for new student, based on current Syllabus
    # Load syllabus data and store in local variable
    with open('syllabus.json') as f:
        repertoire = json.load(f)
    # For each step in the repertoire, add keys 'started' and 'competent'
    for step in repertoire:
        step['started'] = False
        step['competent'] = False
    filename = f"{student_name}".replace(' ', '')
    # print(filename)
    with open(f'repertoire/{filename}', 'w') as f:
        json.dump(repertoire, f, indent = 4)

def view_repertoire(student_name):
    filename = f"{student_name}".replace(' ', '')
    # Load data from repertoire .json file based on student name provided
    with open(f'repertoire/{filename}.json') as f:
        repertoire = json.load(f)
    
    # Display dances student has started work on
    # for step in repertoire:
    #     if step['']



if __name__ == '__main__':
    view_repertoire('Penny Piper')
    pass