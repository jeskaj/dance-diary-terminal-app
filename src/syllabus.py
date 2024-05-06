import csv

with open('syllabus.csv') as f:
    reader = csv.DictReader(f)
    syllabus_list = []
    for row in reader:
        # print(row)
        syllabus_list.append(row)
    print(syllabus_list)
