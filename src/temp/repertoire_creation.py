import json
from repertoire import new_repertoire


def create_repertoires():
    with open('students.json') as f:
        students = json.load(f)
    for student in students:
        new_repertoire(student['name'])
