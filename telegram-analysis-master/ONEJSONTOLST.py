import re
import requests
import os
import glob
import fileinput
import openpyxl
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
proxy = {'https': 'http://127.0.0.1:9666'} 
for filename in glob.glob('E:\\telegram-data\\ALLJSONS.json'):
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
                linklist.append(("https"+m).replace("\",","").replace("\\",""))
    seen = set()
    linklist =  [x for x in linklist if x not in seen and not seen.add(x)]            
    lstfilename = "E:\\telegram-combined\\ALLTELEGRAMLINKS.txt"
    outfile = open(lstfilename,"a+")
    contents = outfile.readlines()       
    for link in linklist:
        if link not in contents:
            outfile.write(link+"\n")