import json

def view_syllabus(filename):
    # Function to view syllabus data stored in .json file
    with open(filename) as f:
        syllabus = json.load(f)
    for step in syllabus:
        print(f"{step['dance']} - Level {step['level']}: {step['step']}")
        # for key, value in element:
        #     print(f'{key}: {value}')

# print(view_syllabus('syllabus.json'))
# view_syllabus('syllabus.json')
# print(view_syllabus('syllabus.json'))