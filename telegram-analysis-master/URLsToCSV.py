import re
import requests
import os
import io
import glob
import fileinput
import csv
import urllib3
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
proxy = {'https': 'http://127.0.0.1:9666'} 
def appendToCsv(f,read_file,linklist):
    current_first_col = []
    file = csv.DictReader(f)
    for col in file:
        current_first_col.append(col['url'])
        
    for link in linklist:
        if link not in current_first_col:
            first_col=link
            print("{} ; Completed : {}/{}".format(link,linklist.index(link)+1,len(linklist)))
            try:
                r = requests.get(link,proxies = proxy)
            except ConnectionError as e:
                read_file.writerow([link,link,'=HYPERLINK("{}", "{}")'.format(link, link)])
                continue
            if r.content.lower() == b'invalid':
                read_file.writerow([link,link,'=HYPERLINK("{}", "{}")'.format(link, link),"--------------------"])
                continue
            if r.status_code != 200:
                read_file.writerow([link,link,'=HYPERLINK("{}", "{}")'.format(link, link),"--------------------"])
                continue
            second_col=r.url
            soup = BeautifulSoup(r.content, 'html.parser')
            third_col=soup.select_one('title').text
            read_file.writerow([first_col,second_col,'=HYPERLINK("{}", "{}")'.format(second_col, second_col),third_col])
for filename in glob.glob(os.path.join('E:\\telegram-data\\', '*.json')):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace("\\n", " "), end='')
    print("Working on "+filename)
    import re
    linklist = []
    with open(filename) as fh: 
        for line in fh: 
            match = re.findall("(?s)(?<=https).+?(?= )", line) 
            for m in match:
                linklist.append(("https"+m).replace("\",",""))
    seen = set()
    linklist =  [x for x in linklist if x not in seen and not seen.add(x)]            
    csvfilename = "E:\\telegram-combined\\ALLTELEGRAMLINKS.csv"
    with open(csvfilename, "a+", encoding="utf-8") as f:
        read_file = csv.writer(f)
        appendToCsv(f,read_file,linklist)