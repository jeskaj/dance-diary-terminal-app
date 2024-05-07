import json

def view_syllabus(filename):
    # Function to view syllabus data stored in .json file
    with open(filename) as f:
        syllabus_list_of_dicts = json.load(f)
        # return syllabus_list_of_dicts
    for index, element in syllabus_list_of_dicts:
        print(f'{index}: {element}')
        # for key, value in element:
        #     print(f'{key}: {value}')

# print(view_syllabus('syllabus.json'))
view_syllabus('syllabus.json')



# Original simple function that returns syllabus data in raw list of dictionaries format
# def view_syllabus(filename):
#     # Function to view syllabus data stored in .json file
#     with open(filename) as f:
#         syllabus_list_of_dicts = json.load(f)
#         return syllabus_list_of_dicts

# print(view_syllabus('syllabus.json'))