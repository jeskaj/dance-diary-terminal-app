# T1A3 Terminal Application:  Dance Diary

## Overview & Purpose
**Dance Diary** is a terminal application to assist dance teachers by storing their students' contact information, creating lesson plans and keep track of students’ progress through the syllabus.

## Source Code Repository

The source code for this project is available on Github in the following repository:

[dancing-diary-terminal-app](https://github.com/jeskaj/dancing-diary-terminal-app)

## Style Guide

**ASSIGNMENT REQUIREMENTS**
- Identify any code style guide or styling conventions that the application will adhere to.
- Reference the chosen style guide appropriately.

**CHECK & UPDATE THIS - TAKEN DIRECTLY FROM EXAMPLE PROJECT:**
- 4 spaces per indentation level
- Maximum line length is 79 characters
- Imports on separate lines
- Using single-quoted strings consistently, except when an apostrophe appears in the string, in which case double-quotes were used to avoid backslashes, and hence improve readability
- Comments in complete sentences and the first word is capitalised. Also inline comments were avoided
- Function names are in lower case and words are separated by underscores to improve readability.

**MY TEXT**


PEP8
- Blank lines:
  - Surround top-level function and class definitions with two blank lines.
  - Method definitions inside a class are surrounded by a single blank line.
  - Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).
  - Use blank lines in functions, sparingly, to indicate logical sections.

numpy

## Features

Develop a list of features that will be included in the application. It must include:

- at least THREE features
- describe each feature, providing a walkthrough of the logic of the application.

Note: Ensure that your features above allow you to demonstrate your understanding of the following language elements and concepts:

- use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

### Dance Syllabus
- Dance styles to be taught
- Steps in each dance, grouped into 3 levels

### Students
- Create new student and store:
    - Name, Email, Mobile
    - Dances student is learning
        - Steps within each dance they have learnt & whether they are competent in that step yet or not
        - Level of student within each dance (student cannot progress to next level until competent in all steps from previous level)
- View student information
- Update student information

### Lessons
- Create lesson plan to store:
    - Student
    - Date & time of lesson (checks no lesson already scheduled for chosen date/time)
    - Dance styles/steps to be taught in lesson (level 2 & 3 steps can only be added if student is competent in all lower-level steps in chosen style)
- Update lesson to add notes about student progress
- Update student competency in steps taught after completion of lesson
- View individual lesson information
- View list of upcoming lessons scheduled

## Implementation Plan

Develop an implementation plan which:
- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

Utilise a suitable project management platform to track this implementation plan.

Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan. 

> Your checklists for each feature should have at least 5 items.

-------------------------
The implementation plan for this project was created using [Trello](https://trello.com/) and can be access via the following link:

INSERT LINK TO BOARD - check access

https://trello.com/b/bFwCFIW8/terminal-app-dancing-diary

Initial stages:

![initial planning - Sunday](docs/trello1-sun.png)

## Installation & Manual

Design help documentation which includes a set of instructions which accurately describe how to use and install the application.

You must include:
- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application

### Dependendcies

Mention all imported packages and modules

### Installation Instructions

### Application Manual

INCLUDE LINK TO MANUAL CREATED BY PYDOCS

## References

Provide full attribution to referenced sources (where applicable).

PEP8

numpy
