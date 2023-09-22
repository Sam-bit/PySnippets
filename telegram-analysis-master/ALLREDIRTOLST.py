import re
import requests
import os
import glob
import fileinput
import openpyxl
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
proxy = {'https': 'http://127.0.0.1:9666'} 
file = open('E:\\telegram-combined\\ALLTELEGRAMLINKS.TXT',"r")
linklist = file.readlines()
seen = set()
linklist =  [x for x in linklist if x not in seen and not seen.add(x)]            
lstfilename = "E:\\telegram-combined\\ALLPDISKREDIRLINKS.TXT"
outfile = open(lstfilename,"a+")  
for link in linklist:
        print("{} ; Completed : {}/{}".format(link.strip(),linklist.index(link)+1,len(linklist)))
        try:
            r = requests.get(link,proxies = proxy)
        except ConnectionError as e:
            continue
        if r.content.lower() == b'invalid':
            continue
        if r.status_code != 200:
            continue
        if r.headers['Content-Type'] != "text/html":
            continue
        second_col=r.url
        soup = BeautifulSoup(r.content, 'html.parser')
        third_col=soup.select_one('title').text
        if not soup.find_all('div', class_='co-empty') and third_col.startswith("PDisk - "):
            outfile.write(link.strip()+","+str(second_col)+"\n")
            outfile.flush()