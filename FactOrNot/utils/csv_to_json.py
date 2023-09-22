import csv
import json
json_file = r"facts.json"
def csv_to_json(file):
    csv_rows = []
    with open(file,errors ='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        convert_write_json(csv_rows, json_file)

#Convert csv data into json
def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data,ensure_ascii = False)) #for pretty