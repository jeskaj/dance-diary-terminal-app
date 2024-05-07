import csv, json

def import_csv_syllabus(filename):
    # Function to input .csv of syllabus data and transform into a list of dictionaries
    with open(filename) as f:
        reader = csv.DictReader(f)
        syllabus_list = []
        for row in reader:
            syllabus_list.append(row)
        return(syllabus_list)
    
def create_json_syllabus(syllabus_list_of_dicts):
    # function to output list of dictionaries as .json file
    with open('syllabus.json', 'w') as f:
        json.dump(syllabus_list_of_dicts, f, indent=4)

new_syllabus = import_csv_syllabus('syllabus.csv')

create_json_syllabus(new_syllabus)
