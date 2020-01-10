import csv

def load_csv(path_to_load):
    with open(path_to_load, 'r') as csv_file:
        csv_lines = csv.reader(csv_file, quoting=csv.QUOTE_ALL, delimiter=',')
        return list(csv_lines)

