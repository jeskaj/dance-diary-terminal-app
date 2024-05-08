"""
This module defines functions for working with dance Syllabus
"""

import json, string


def print_step(step):
    # Print details of a single dance step
    print(f"{step['dance']} - Level {step['level']}: {step['step']}")


def view_syllabus(filename):
    # View syllabus data stored in .json file
    with open(filename) as f:
        syllabus = json.load(f)
        syllabus_sorted = sorted(syllabus, key=lambda d: d['dance'])
    for step in syllabus_sorted:
        # Call function to print details of dance step
        print_step(step)


def dance_set(filename):
    # Returns a set of unique dances within the syllabus
    with open(filename) as f:
        syllabus = json.load(f)
    # Create empty set
    dances = set()
    for step in syllabus:
        # Add names of dances to set
        dances.add(step['dance'].lower())
    return sorted(dances)


def print_dances(filename):
    # Prints all unique names of dances within the syllabus
    dances = dance_set(filename)
    for dance in dances:
        print(string.capwords(dance))


def view_dance(filename):
    # Find all steps for a single dance within the syllabus
    with open(filename) as f:
        syllabus = json.load(f)
    print('\nYour syllabus contains the following dances:\n')
    # Call function to list unique names of dances within syllabus
    print_dances(filename)
    # User to select one dance from printed list
    dance = input('\nPlease enter one of the above-listed dances, to view its syllabus of steps:  ')

    # Check user has input a valid dance
    dance_valid = False
    # Create set of unique dance names
    dances = dance_set(filename)
    # Check if user input exists in set
    if dance.lower() in dances:
        dance_valid = True
    # While user input invalid, keep requesting input
    while dance_valid == False:
        dance = input('Input invalid.  You must enter a dance from the list above:  ')
        # Check input validity
        if dance.lower() in dances:
            dance_valid = True
    # If input valid, print heading
    print(f'\n\n{dance.upper()} SYLLABUS:\n')
    # Find steps in syllabus where dance == selected dance
    for step in syllabus:
        if step['dance'].lower() == dance.lower():
            # Call function to print step details
            print_step(step)


if __name__ == '__main__':
    # print(view_syllabus('syllabus.json'))
    # view_syllabus('syllabus.json')
    # print(view_syllabus('syllabus.json'))
    # print_dances('syllabus.json')
    # view_dance('syllabus.json')
    pass