import os.path
import csv
csv_file = 'drugs.csv'
med_url = []
field_names = ['MED_NAME',
               'MED_URL',
               'MANUFACTURE_NAME',
               'SALT_COMP_NAME',
               'CONSUME_TYPE',
               'HOW_TO_USE',
               'NUM_OF_UNITS_OR_VARIANTS',
               'QUANTITY',
               'MRP_PRICE',
               'DISCOUNT_PRICE']
def csvColumnToList():
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(field_names)
            csvfile.close()
    filename = open(csv_file, 'r')
    file = csv.DictReader(filename)
    med_url = []
    for col in file:
        med_url.append(col['MED_URL'])
    return med_url
def csvAppendDictToCsv(dict,med_url_list):
    if dict['MED_URL'] not in med_url_list:
        with open(csv_file, 'a', newline='') as f_object:
            dictwriter_object = csv.DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(dict)
            f_object.close()