import io
import urllib

import requests
headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
csvfile ='https://www.nseindia.com/api/allIndices?csv=true'
for line in urllib.request.urlopen(csvfile):
    print(line.decode('utf-8'))