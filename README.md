# T1A3 Terminal Application:  Dance Diary

## Overview & Purpose
**Dance Diary** is a terminal application to designed assist dance teachers, by storing their students' contact information and keeping track of students’ progress through the repertoire.

*NOTE: The initial project proposal also included a feature to develop lesson plans, which has not been completed for the initial release.*

## Source Code Repository

The source code for this project is available on Github in the following repository:

[dancing-diary-terminal-app](https://github.com/jeskaj/dancing-diary-terminal-app)

## Style Guide

The following style guide was used for this project:

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

## System Requirements

This application requires:
- Python3
- pip3

### Dependendcies

- art==6.2 (refer [art 6.2](https://pypi.org/project/art/))
- color50==1.0.1 (refer [color50 1.0.1](https://pypi.org/project/color50/))

## Installation Instructions

The Dance Diary application should be run by executing the script `dance_diary.sh`, from within in the `src` folder of this project.

From `/src`, run the following command:

`./dance_diary.sh`

This script will check that:
- Python3 is installed; and
- pip3 is installed

Assuming this is the case, it will then:
- install the required dependencies (as detailed above)
- run `main.py` to start the application

The user will then be presented with the application's Main Menu.

*NOTE:  The script's permissions have been set to executable for all users, but in case of permission errors, run the command:*  `chmod +x dance_diary.sh`

## Program Features & Manual

### Main Menu

On running the program, the Main Menu is presented:

![Main Menu](docs/main-menu.png)

If any input is provided other than 1, 2, 3 or 0, the user is advised to try again and the Main Menu is presented again:

![Main Menu - Invalid Input](docs/main-menu-invalid-input.png)

### [1] Syllabus

Syllabus data is stored in the file: `syllabus.json`

When `Syllabus` is selected from the Main Menu, the Syllabus Menu is presented:

![Syllabus Menu](docs/syllabus-menu.png)

If any input is provided other than 1, 2 or 0, the user is advised to try again (as shows above for Main Menu) and the Syllabus Menu is immediately presented again.

*NOTE:  The initial release of Dance Diary contains a single syllabus.json file, which comprises the Bronze Syllabus of five common styles taught in American Style ballroom dancing - Cha Cha, Foxtrot, Rumba, Swing and Waltz.  The syllabus for each dance is further divided into three levels (1, 2 and 3).*

*If the application is developed further, the intention would be to add additional features to allow dance teachers add and edit the dances and dance steps in the syllabus.  This functionality was not attempted in the initial release due to time constraints.*

#### [1] View Entire Syllabus

If this feature is chosen, the all steps in the syllabus.json file is displayed in readable format for the user to view, sorted by dance, then level:

![Syllabus View Start](docs/syllabus-start.png)

At the end of the list, the total number of steps in the syllabus is display and the Syllabus Menu is presented again:

![Syllabus View End](docs/syllabus-end.png)

#### [2] View Syllabus by Dance

This feature can be selected to view only the steps for a single dance.  The user is presented with a list of the unique names of dances in the current syllabus and invited to make a selection.

Invalid selections produce a warning and instruct the user to enter a dance from the list provided.  To reduce the likelihood of invalid input, input is not case-sensitive.  Once a valid selection has been made, the steps for the chosen dance are displayed and the Syllabus Menu is presented again.

![Syllabus by Dance](docs/syllabus-by-dance.png)

### [2] Students

Student data is stored in the file: `students.json`

When `Students` is selected from the Main Menu, the Student Menu is presented:

![Student Menu](docs/student-menu.png)

If any input is provided other than 1, 2, 3, 4 or 0, the user is advised to try again (as shows above for Main Menu) and the Student Menu is immediately presented again.

*NOTE: For the purposes of T1A3 assignment submission, the application contains some dummy student data to allow for easy testing.  All names and contact details are ficticious.*

#### [1] Add New Student

This feature request's the user enter the new student's full name.  If the name already exists, a warning is presented, to avoid duplication.  Validation is not case sensitive:

![Student Add - Start](docs/student-create-start.png)

If a unique name is entered, the user is then prompted to provide the student's email and mobile.  The new student's information is then presented back to the user to check and confirm, with a warning that a student's name cannot be changed once the student is created.  If the creation is confirmed, a confirmation message is displayed, along with the total number of students now stored:

![Student Add - End](docs/student-create-end.png)

When a new student is created, as well as adding their data to the `students.json` file, a repertoire file is also created for the student in the `repertoire` folder.  This file is created by taking a copy of all of the steps in the syllabus.json file and adding a `status` of `New` to each step, to indicate that the student has not yet started learning the step.  The repertoire file is named in the format `studentname.json` eg Peter Parker's repertoire file is named `peterparker.json`.

#### [2] View Student Contact Details & Repertoire

This feature presents a choice between viewing a list of contact details for all students, or selecting a single student, to view both their contact details and repertoire progress.  Invalid input results in a warning and the user is remindered to select from the menu:

![Student View - Start](docs/student-view-start.png)

`[a]  View contact details for all students`

If `a` is selected, all student contact details are printed.  The total number of students is shown at the end of the list and the Student Menu is presented again:

![Student Contacts - Start](docs/student-contacts-start.png)

![Student Contacts - End](docs/student-contacts-end.png)

`[s]  Select a single student to view contact details & repertoire progress`

If `s` is selected, the user is invited to enter a student name, or press any key to see a list of student names:

![Student View Single - Start](docs/student-view-single-start.png)

If the student is new and has not started learning any steps, the below message is displayed:

![Student View New](docs/student-view-new.png)

Once a student is selected who has started and/or completed learning at least one step, their contact details are displayed along with their dance steps, divided into two sections - those they are currently learning (status = Started) and those they have completed (status = Competent).  The Student Menu is then presented again:

![Student View Single - End](docs/student-view-single-end.png)

#### [3] Update Student Contact Details

When this feature is selected, the user is requested to enter the name of a student, or any key to see a list of current student names (as described in the previous feature).

Once a valid name has been entered, the user is presented with the student's current contact details and given the 

must choose to update the student's email or mobile.  The user will receive an `INVALID INPUT` warning if anything other than `e` or `m` is entered:

![Student Update Details](docs/student-update-details.png)

If `e` is entered, the user is prompted to enter the new email address and a confirmation message is displayed once submitted:

![Student Update Email](docs/student-email-update.png)

If `m` is entered, the user is prompted to enter the new mobile number and a confirmation message is displayed once submitted.  In both cases, the Student Menu is then presented again:

![Student Update Mobile](docs/student-mobile-update.png)

This data is updated accordingly in the `students.json` file.

#### [4]  Update Student Repertoire Progress

1. User selects student
3. User selects from options to:
  a) Add a new step
    1. User is presented with a list of dances to choose from
    2. User selects dance
    3. User is presented a list of steps from the selected dance that may be added, which:
      - if all steps for the dance are completed:
        - advise user student has completed all steps for this dance
        - end
      - excludes steps already started or completed
      - unless all level 1 steps are completed, excludes level 2 & 3 steps
      - unless all level 2 steps are completed, excludes level 3 steps
    4. User selects a step to be added
    5. Step is added to student's repertoire with status Started

  u) Update an existing step
    1. User is presented with a list of dances to choose from
    2. User selects dance
    3. User is presented a list of steps from the selected dance that may be added, which:
      - if all steps for the dance are completed:
        - advise user student has completed all steps for this dance
        - end
      - excludes steps already started or completed
      - unless all level 1 steps are completed, excludes level 2 & 3 steps
      - unless all level 2 steps are completed, excludes level 3 steps
    4. User selects a step to be added
    5. Step is added to student's repertoire with status Started

### [3] Lessons

As mentioned above, the Lessons module has not been completed for this initial release of the project.  Lessons is shown as `Coming Soon!` in the Main Menu.

If `Lessons` is selected from the main menu, the user is presented with the below message and the Main Menu is immediately presented again, so the user can make another selection:

![Lessons Module Message](docs/lessons-msg.png)

Planned features for this module include:

- Create lesson plan to store:
    - Student
    - Date & time of lesson (checks no lesson already scheduled for chosen date/time)
    - Dance styles/steps to be taught in lesson (level 2 & 3 steps can only be added if student is competent in all lower-level steps in chosen style)
- Update lesson to add notes about student progress
- Update student competency in steps taught after completion of lesson
- View individual lesson information
- View list of upcoming lessons scheduled

## Implementation Plan

The implementation plan for this project was created using [Trello](https://trello.com/) and can be access via the following link:

[Terminal App - Dance Diary](https://trello.com/b/bFwCFIW8/terminal-app-dance-diary)

The Trello workspace has been set to Public, but screenshots are also provided.

One or more cards was created to track the development of each feature (depending on complexity) and checklists were created within each major card to further track the stages of developing each feature.  Due dates were added to cards and sometimes also to individual checklist items within cards.

![Trell board is set to Public](docs/trello-board-public.png)

5 May, 2024:

![Trello on Sunday](docs/trello1-sun.png)

7 May, 2024:

![Trello on Tuesday](docs/trello3-tues.png)

8 May 2024 - At this stage, determined that the Lesson module could not be developed for the initial project submission, so moved to Backlog:

![Trello on Wednesday](docs/trello7-wed.png)

9 May, 2024:

![Trello on Thursday](docs/trello11-thurs.png)

10 May, 2024:

![Trello on Friday](docs/trello15-fri.png)

11 May, 2024 - Excluding Backlog tasks, final task remaining was to complete the documentation:

![Trello on Saturday](docs/trello18-sat.png)

## References

Van Rossum, Warsaw & Coghlan 2001, *PEP 8 – Style Guide for Python Code*, 7 May 2024, https://peps.python.org/pep-0008/

Fletcher, D 2024, *This is color50*, 10 May, 2024, https://color50.readthedocs.io/

Art Development Team 2017, *ASCII Art Library for Python*, 10 May, 2024, https://pypi.org/project/art/