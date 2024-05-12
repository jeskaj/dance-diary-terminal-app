"""
This module defines functions for working with Students' Repertoire data
"""

from color50 import css, constants
import json
import string
from syllabus import print_step, dance_set


# Define colors using color50 module
greensteps = css("lightgreen")
teal = css("teal")
forestgreen = css("forestgreen")


def repertoire_filename(student_name):
    """
    Function to format name of student into name of .json
    repertoire file for that student

    Parameters
    ----------
    student_name : str
        Name of student

    Returns
    -------
    str :
        Name of .json repertoire file for student
    """
    return f"{student_name}.json".replace(" ", "").lower()


def new_repertoire(filename: str):
    """
    Create repertoire file for new student, by copying the current Syllabus and adding
    a status of 'New', indicating student has not yet started learning the step
    """
    # Load current syllabus data and store in local variable (list of dictionaries)
    with open("syllabus.json") as f:
        repertoire = json.load(f)
    # For each step in the repertoire, add 'status' with value 'New'
    for step in repertoire:
        step["status"] = "New"
    # Export student's repertoire data into repertoire/studentname.json file
    with open(f"repertoire/{filename}", "w") as f:
        json.dump(repertoire, f, indent=4)


def sort_steps(repertoire: list):
    """
    Sorts a list of steps (stored as dictionaries) by dance then level

    Parameters
    ----------
    repertoire : list
        A list of dictionaries, where each dictionary represents a dance step

    Returns
    -------
    list :
        A list of dictionaries, where each dictionary represents a dance step,
        sorted by dance then level
    """
    # Sorts repertoire list
    repertoire_sorted = sorted(repertoire, key=lambda s: (s["dance"], s["level"]))
    # Returns sorted repertoire list
    return repertoire_sorted


def steps_with_status(repertoire: list, status: str):
    """
    Filter a list of step dictionaries to create a new list only including steps of
    the specified status ('New', 'Started' or 'Competent'), sorted by dance then level

    Parameters
    ----------
    repertoire : list
        A list of dictionaries, where each dictionary represents a dance step
    status : str
        The status of a dance step ('New', 'Started' or 'Competent')

    Returns
    -------
    list :
        A list of dictionaries, where each dictionary represents a dance step,
        sorted by dance then level
    """
    filtered_steps = sort_steps(
        [step for step in repertoire if step["status"].lower() == status.lower()]
    )
    return filtered_steps


def steps_from_dance(repertoire: list, dance: str):
    """
    Filter a list of step dictionaries to create a new list only including steps from
    the specified dance, sorted by level

    Parameters
    ----------
    repertoire : list
        A list of dictionaries, where each dictionary represents a dance step
    dance : str
        The dance from which the user wants to view steps

    Returns
    -------
    list :
        A list of dictionaries, where each dictionary represents a dance step, sorted by level
    """
    # Filter list to create new list containing only steps of specified dance
    filtered_steps = sort_steps(
        [step for step in repertoire if step["dance"].lower() == dance.lower()]
    )
    # Return filtered list
    return filtered_steps


def view_repertoire(student_name: str):
    """
    Display repertoire of Started and Competent steps for student (ie exclude
    steps with status of New, which student has not yet started learning)

    Parameters
    ----------
    student_name : str
        Name of a student
    """
    # Call function to format student name provided into repertoire filename format
    filename = repertoire_filename(student_name)
    # Load data from repertoire .json file based on student name provided
    with open(f"repertoire/{filename}") as f:
        repertoire = json.load(f)

    # Create list of steps in progress ie call function to filter for steps with status Started
    current_steps = steps_with_status(repertoire, "Started")
    # Create list of completed steps ie call function to filter for steps with status Competent
    completed_steps = steps_with_status(repertoire, "Competent")

    print(f"\n{teal.bg()}REPERTOIRE STATUS FOR {student_name.upper()}{constants.RESET}")

    # If length of both of these lists is 0, then student is new and hasn't started learning any steps
    if len(current_steps) == 0 and len(completed_steps) == 0:
        # Advise user this is a new student - no repertoire to display
        print(
            f"{student_name} is a new student - you can start them on any Level 1 steps. "
        )

    # If student is not completely new, display steps currently in progress & completed
    # If student has steps in progress
    if len(current_steps) != 0:
        # Sort current steps by dance name
        current_steps_sorted = sorted(current_steps, key=lambda d: d["dance"])
        print(
            f"\n{forestgreen.bg()}STEPS IN PROGRESS (student is currently learning these steps):{constants.RESET}"
        )
        # Display current steps
        for step in current_steps_sorted:
            print_step(step)

    # If student has completed (competent) steps
    if len(completed_steps) != 0:
        # Sort completed steps by dance name
        completed_steps_sorted = sorted(completed_steps, key=lambda d: d["dance"])
        print(
            f"\n{forestgreen.bg()}STEPS COMPLETED (student is competent in these steps):{constants.RESET}"
        )
        # Display steps student has completed
        for step in completed_steps_sorted:
            print_step(step)


def select_dance(repertroire_filepath: str):
    """
    Allow user to select a dance from those within the student's repertoire

    Parameters
    ----------
    repertroire_filepath : str
        Full filepath and name of student's repertoire .json file

    Returns
    -------
    str :
        The name of the dance selected by the user from the student's repertoire
    """
    # Call function to create set of unique dances from student's repertoire
    dances = dance_set(repertroire_filepath)
    # Display list of available dances
    print(f"\n{teal.bg()}AVAILABLE DANCES:{constants.RESET}")
    for dance in dances:
        print(f"{teal}{string.capwords(dance)}{constants.RESET}")
    # Get user selection
    dance_selection = input("\nEnter a dance from the above list:  ")

    # Validate user selection
    while dance_selection.lower() not in dances:
        dance_selection = input(
            f"\n{constants.RED}INVALID INPUT.{constants.RESET}  Enter a dance from the above list:  "
        )
    # Return name of dance user selected
    return dance_selection


def validate_step_choice(new_steps: list):
    """
    Allow user to select a dance step to be added (ie updated to status Started)
    in the student's repertoire and confirm their input is a valid available step
    (ie name matches to a step with status New in the student's repertoire)

    Parameters
    ----------
    new_steps : list
        A list of dictionaries, containing steps with status New

    Returns
    -------
    str :
        The name of a valid step with status New
    """
    # Get name of step to add from user
    step_choice = input("\nEnter the name of a step from the above list:  ")
    # Validate user input
    # Create list of step names
    step_names = [step["step"].lower() for step in new_steps]
    # Check if chosen step is in list of step names
    while step_choice.lower() not in step_names:
        # Request new input, until a valid step name is entered
        step_choice = input(
            f"\n{constants.RED}INVALID INPUT:{constants.RESET}  You must enter the name of a step from above list (or 0 to quit):  "
        )
        # Exit the process if 0 is entered
        if step_choice == "0":
            break
    # return name of step chosen to be added
    return step_choice


def update_step_status(
    repertoire: list, dance_name: str, step_name: str, new_status: str
):
    """
    Updates the status of a step in a student's repertoire

    Parameters
    ----------
    repertoire : list
        List of dictionaries (created from a repertoire .json file), each dictionary
        representing a dance step, including the keys 'dance', 'step' and 'status'
    dance_name : str
        Name of dance - value of key 'dance'
    step_name : str
        Name of step - value of key 'step'
    new_status : str
        Status to which the step will be updated
    """
    step_found = False
    while step_found == False:
        # Check each step in repertoire
        for step in repertoire:
            # If dance and name of step match selection, update status
            if (
                step["step"].lower() == step_name.lower()
                and step["dance"].lower() == dance_name.lower()
            ):
                step["status"] = new_status
                step_found = True


def update_repertoire(student_name):
    """
    Updates student's repertoire by either adding a new step (ie update status to Started)
    or indicating when student becomes competent in a step (ie update status from Started to Competent)
    """
    # Load student's repertoire and store in local variable
    filename = repertoire_filename(student_name)
    with open(f"repertoire/{filename}") as f:
        repertoire = json.load(f)

    # Check if student has already completed the entire syllabus
    completed_steps = steps_with_status(repertoire, "Competent")
    if len(completed_steps) == len(repertoire):
        print(
                f"{constants.MAGENTA}Congratulations! {string.capwords(student_name)} has completed the current syllabus. There are no more steps to be added or updated.{constants.RESET}"
            )

    # If student has not completed the entire syllabus, proceed
    else:
        # Present user with add or update options
        print(f"\n{teal.bg()}Options:{constants.RESET}")
        print(f"{teal}[a]  Add new step")
        print("[u]  Update step in progress to Competent")
        print(f"[0]  Return to Student Menu{constants.RESET}")
        selection = input("\nEnter a or u (or 0 to cancel):  ")

        # If user has not input 0 to quit, check validity of input
        if selection != "0":
            # Check input validity
            while selection not in ("a", "u"):
                selection = input(
                    f"\n{constants.RED}INVALID INPUT:{constants.RESET}  Please enter a, u or 0 (refer menu above):  "
                )
                if selection == "0":
                    break

            if selection == "a":
                # Check that student has New steps available (across all dances in syllabus)
                new_steps = steps_with_status(repertoire, "New")
                if len(new_steps) == 0:
                    print(
                        f"{constants.MAGENTA}{string.capwords(student_name)} has already started learning or become competent in all steps in the syllabus. There are no new steps left to be added.{constants.RESET}"
                    )
                else:
                    # Call function to display available dances & allow user to input a selection
                    dance_selection = select_dance(f"repertoire/{filename}")
                    # Call function to create list of steps from the chosen dance
                    dance_steps = steps_from_dance(repertoire, dance_selection)
                    # Call function to create list filtering the above list down to those with status New
                    new_steps = steps_with_status(dance_steps, "New")

                    # Check that student still has some new steps left to learn in chosen dance
                    if len(new_steps) == 0:
                        print(
                            f"\n{constants.MAGENTA}*** NO NEW STEPS TO ADD: This student has already started learning all steps in the {string.capwords(dance_selection)} syllabus.{constants.RESET}"
                        )
                    else:
                        # Create a list for each level of steps found in list of available new steps
                        new_steps_lvl1 = [
                            step for step in new_steps if step["level"] == "1"
                        ]
                        new_steps_lvl2 = [
                            step for step in new_steps if step["level"] == "2"
                        ]
                        new_steps_lvl3 = [
                            step for step in new_steps if step["level"] == "3"
                        ]
                        # Check if student has completed all level 1 steps in dance
                        if len(new_steps_lvl1) != 0:
                            print(
                                f"\n{teal.bg()}AVAILABLE NEW LEVEL 1 STEPS IN {dance_selection.capitalize()}:{constants.RESET}"
                            )
                            # For each new step, call function to print step details in readable format
                            for step in new_steps_lvl1:
                                print_step(step)
                            # Call function to get user step choice & validate input
                            step_choice = validate_step_choice(new_steps_lvl1)

                        # If level 1 steps all completed, check if student has completed all level 2 steps in dance
                        elif len(new_steps_lvl2) != 0:
                            print(
                                f"\n{teal}Student has completed all Level 1 steps in {dance_selection.upper()}{constants.RESET}"
                            )
                            print(
                                f"\n{teal.bg()}AVAILABLE NEW LEVEL 2 STEPS IN {dance_selection.upper()}:{constants.RESET}"
                            )
                            # For each new step, call function to print step details in readable format
                            for step in new_steps_lvl2:
                                print_step(step)
                            # Call function to get user step choice & validate input
                            step_choice = validate_step_choice(new_steps_lvl2)

                        # If level 1 & 2 steps all completed, display remaining level 3 steps in dance
                        else:
                            print(
                                f"\n{teal}Student has completed all Level 1 & 2 steps in {dance_selection.upper()}{constants.RESET}"
                            )
                            print(
                                f"\n{teal.bg()}AVAILABLE NEW LEVEL 3 STEPS IN {dance_selection.upper()}:{constants.RESET}"
                            )
                            # For each new step, call function to print step details in readable format
                            for step in new_steps_lvl3:
                                print_step(step)
                            # Call function to get user step choice & validate input
                            step_choice = validate_step_choice(new_steps_lvl3)

                        if step_choice != "0":
                            # Call function to update status of step to be added to Started
                            update_step_status(
                                repertoire, dance_selection, step_choice, "Started"
                            )
                            with open(f"repertoire/{filename}", "w") as f:
                                json.dump(repertoire, f, indent=4)
                            print(
                                f"\n{teal}STEP ADDED: {string.capwords(dance_selection)} - {string.capwords(step_choice)} has been added to {string.capwords(student_name)}'s repertoire with status Started{constants.RESET}"
                            )

            elif selection == "u":
                # Check that student has at least one step in progress ie status = started (across all dances in syllabus)
                started_steps = steps_with_status(repertoire, "Started")
                if len(started_steps) == 0:
                    print(
                        f"{teal}{string.capwords(student_name)} has no steps in progress. You will need to add a new step.{constants.RESET}"
                    )
                else:
                    # Call function to display available dances & allow user to input a selection
                    dance_selection = select_dance(f"repertoire/{filename}")
                    # Call function to create list of steps from the chosen dance
                    dance_steps = steps_from_dance(repertoire, dance_selection)
                    # Call function to create list filtering the above list down to those with status Started
                    started_steps = steps_with_status(dance_steps, "Started")

                    # Check that student has some steps in progress in chosen dance
                    if len(started_steps) == 0:
                        print(
                            f"\n{constants.MAGENTA}*** NO STEPS IN PROGRESS: This student has no steps in progress for {string.capwords(dance_selection)}.{constants.RESET}"
                        )
                    else:
                        # Create a list for each level of steps found in list of available new steps
                        started_steps_lvl1 = [
                            step for step in started_steps if step["level"] == "1"
                        ]
                        started_steps_lvl2 = [
                            step for step in started_steps if step["level"] == "2"
                        ]
                        started_steps_lvl3 = [
                            step for step in started_steps if step["level"] == "3"
                        ]
                        # Check if student has completed all level 1 steps in dance
                        if len(started_steps_lvl1) != 0:
                            print(
                                f"\n{teal.bg()}STEPS IN PROGRESS FOR LEVEL 1 {dance_selection.capitalize()}:{constants.RESET}"
                            )
                            # For each new step, call function to print step details in readable format
                            for step in started_steps_lvl1:
                                print_step(step)
                            # Call function to get user step choice & validate input
                            step_choice = validate_step_choice(started_steps_lvl1)

                        # If level 1 steps all completed, check if student has completed all level 2 steps in dance
                        elif len(started_steps_lvl2) != 0:
                            print(
                                f"\n{teal}Student has completed all Level 1 steps in {dance_selection.upper()}{constants.RESET}"
                            )
                            print(
                                f"\n{teal.bg()}STEPS IN PROGRESS FOR LEVEL 2 {dance_selection.upper()}:{constants.RESET}"
                            )
                            # For each new step, call function to print step details in readable format
                            for step in started_steps_lvl2:
                                print_step(step)
                            # Call function to get user step choice & validate input
                            step_choice = validate_step_choice(started_steps_lvl2)

                        # If level 1 & 2 steps all completed, display remaining level 3 steps in dance
                        else:
                            print(
                                f"\n{teal}Student has completed all Level 1 & 2 steps in {dance_selection.upper()}{constants.RESET}"
                            )
                            print(
                                f"\n{teal.bg()}STEPS IN PROGRESS FOR LEVEL 3 {dance_selection.upper()}:{constants.RESET}"
                            )
                            # For each new step, call function to print step details in readable format
                            for step in started_steps_lvl3:
                                print_step(step)
                            # Call function to get user step choice & validate input
                            step_choice = validate_step_choice(started_steps_lvl3)

                        if step_choice != "0":
                            # Call function to update status of step to Competent
                            update_step_status(
                                repertoire, dance_selection, step_choice, "Competent"
                            )
                            with open(f"repertoire/{filename}", "w") as f:
                                json.dump(repertoire, f, indent=4)
                            print(
                                f"\n{teal}STEP COMPLETED: The status of {string.capwords(dance_selection)} - {string.capwords(step_choice)} has been updated to Competent in {string.capwords(student_name)}'s repertoire{constants.RESET}"
                            )


if __name__ == "__main__":
    pass
