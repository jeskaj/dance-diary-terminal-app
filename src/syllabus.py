"""
This module defines functions for working with dance Syllabus data
"""

from color50 import constants, css
import json
import string


# Define colors using color50 module
greensteps = css('lightgreen')
darkgreen = css('darkgreen')


def print_step(step: dict):
    """
    Prints the dance, level and name of a step

    Parameters
    ----------
    step : dict
        Dictionary with keys dance, level and step (name of step)
    """
    print(f"{greensteps}{step['dance']} - Level {step['level']}: {step['step']}{constants.RESET}")


def view_syllabus(filename: str):
    """
    Prints the entire syllabus, displaying each step on a new line, sorted by dance
    then level. Filename not hard-coded to better allow for future development of
    program to handle multiple syllabuses.

    Parameters
    ----------
    filename : str
        Filename of the .json file containing the syllabus to be printed
    """
    # Loads .json syllabus file and stores data in a list of dictionaries
    with open(filename) as f:
        syllabus = json.load(f)
        # Sorts dictionary elements within list, by dance, then level
        syllabus_sorted = sorted(syllabus, key=lambda s: (s['dance'], s['level']))
    print(f'\n\n{darkgreen.bg()}*** DANCE SYLLABUS ***{constants.RESET}\n')
    # Print details of each step on a new line, for readability
    for step in syllabus_sorted:
        # Call function to print details of dance step
        print_step(step)
    # Show total number of steps at end of syllabus
    print (f'\n{darkgreen}** END OF SYLLABUS - Total steps: {len(syllabus)} ***{constants.RESET}')


def dance_set(filename: str):
    """
    Finds unique dance names within a syllabus .json file

    Parameters
    ----------
    filename : str
        Filename of .json file containing a syllabus (ie a 
        list of dictionaries, each representing a dance step)

    Returns
    -------
    set :
        A set of unique dance names contained in the syllabus
    """
    # Load syllabus .json file and store data in local variable (list of dictionaries)
    with open(filename) as f:
        syllabus = json.load(f)
    # Create empty set
    dances = set()
    # Add each dance name to the set
    for step in syllabus:
        # Add names of dances to set
        dances.add(step['dance'].lower())
    # returns set of unique dance names, sorted alphabetically
    return sorted(dances)


def print_dances(filename: str):
    """
    Prints all unique names of dances within a syllabus .json file

    Parameters
    ----------
    filename : str
        Filename of .json file containing a syllabus (ie a 
        list of dictionaries, each representing a dance step)
    """
    # Call function to create a set of unique dance names
    dances = dance_set(filename)
    # Print each dance name
    for dance in dances:
        print(f'{greensteps}{string.capwords(dance)}{constants.RESET}')


def view_dance(filename: str):
    """
    Displays all steps for a single dance within the syllabus

    Parameters
    ----------
    filename : str
        Filename of .json file containing a syllabus (ie a 
        list of dictionaries, each representing a dance step)
    """
    # Load syllabus .json file and store data in local variable (list of dictionaries)
    with open(filename) as f:
        syllabus = json.load(f)
    print('\nYour syllabus contains the following dances:\n')
    # Call function to display unique names of dances within syllabus
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
        dance = input(f'{constants.RED}INVALID INPUT:{constants.RESET}  You must enter a dance from the list above:  ')
        # Check input validity
        if dance.lower() in dances:
            dance_valid = True
    # If input valid, print heading
    print(f'\n\n{darkgreen.bg()}{dance.upper()} SYLLABUS:{constants.RESET}\n')
    # Find steps in syllabus where dance == selected dance
    for step in syllabus:
        if step['dance'].lower() == dance.lower():
            # Call function to print step details
            print_step(step)


if __name__ == '__main__':
    pass
