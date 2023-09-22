import os
import glob
import fileinput
import json
from datetime import date, datetime
# some functions to parse json date
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        if isinstance(o, bytes):
            return list(o)

        return json.JSONEncoder.default(self, o)
for filename in glob.glob(os.path.join('E:\\telegram-data\\', '*.json')):
    with open(filename) as infile:
        content = infile.read()
        with open('E:\\telegram-data\\ALLJSONS.json', 'a+') as outfile:
            outfile.write(json.dumps(content, indent=2, cls=DateTimeEncoder))