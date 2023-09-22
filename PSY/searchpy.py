import os.path

import requests
from selenium.webdriver.chrome.service import Service
from googlesearch import search
from time import sleep
from codecutils import *
from bs4 import BeautifulSoup
from selenium import webdriver

HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
import urllib3

urllib3.disable_warnings()
# MTI0MzIxIGhvdC1pbmRpYW4tZ2lybC1saXZlY2FtLXNleHktYm9vYnMtc2hvdw==
allsearches = [["159364", "cHJpeWFua2EgeWFkYXYgdGFuZ28gcHJpdmF0ZQ=="],
               ["124321", "aG90IGluZGlhbiBnaXJsIGxpdmVjYW0gc2V4eSBib29icyBzaG93"],
               ["143043", "ZGVzaSBnaXJsIHNob3dpbmcgb24gbGl2ZQ=="],
               ["159369", "cHJpeWFua2EgeWFkYXYgdGFuZ28gbGl2ZSBuaXBwbGUgc2hvdw=="],
               ["130133", "aW5kaWFuIGNhbSBnaXJsIHBpcnlhIGJoYWJoYWkgbmFrZWQgdGVhc2U="],
               ["224370", "aW5kaWFuIGhvdCBiYWJlIHJ1cHBzc2Egbmlwc2xpcCB2ZG8gZm9yIGZhbnM="],
               ["32145",  "ZGVzaSBnaXJsIG51ZGUgc2hvdyB3aXRoIGZhY2U="],
               ["224984", "ZGVzaSBob3QgZ2lybCBydXBzYSBzaG93IG51ZGUgb24gbGl2ZQ=="],
               ["191606", "cnVwc2FhIGhvdCB0YW5nbyBsaXZl"]
               ]

sbsearches = [["c3BhbmtiYW5n", "THJpZyBOYWlkbmk="],
              ["c3BhbmtiYW5n", "YXNpYW4gZ2lybCBvbiB0YW5nbw=="],
              ["ZXBvcm5lcg==", "aW5zdGFncmFtIHByaXlhbmthIHlhZGF2IHNob3cgaGVyIGJpZyBib29icyBvbiB0YW5nbyBsaXZl"],
              ["ZXBvcm5lcg==", "SW5kaWFuIGluc3RhZ3JhbWVyIHByaXlhbmth"],
              ["bXlkZXNp","cHJpeWFua2F5YWRhdl81IGhvdCB0YW5nbyBwcmVtaXVtIHZpZGVv"],
              ["bXlkZXNp","UHJpeWFua2EgWWFkYXYgaG90IHRhbmdvIHByZW1pdW0gc2hvdw=="]
              ]
searches = []
searchlist = []
againsearch = 0
NUM = 500
PAUSE = 20
# TBS = '0'
TBS = 'cdr:1,cd_min:11/1/2020,cd_max:01/20/2023'

def getSeleniumUrl(videourl):
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, service=Service(r'C:\DRIVERS\chromedriver.exe'))
    driver.get(videourl)
    return driver.current_url

for eachsearch in allsearches:
    searchid = eachsearch[0]
    searchstring = eachsearch[1]
    searchlist = []
    if againsearch in (0, 2):
        print("start searching")
        for a in search(decodestring(searchstring), num=NUM, tbs=TBS, pause=PAUSE, extra_params={'filter': '0'}):
            print("A")
            searchlist.append(a)
            sleep(PAUSE)
        print("1")
        for a in search("\"" + decodestring(searchstring) + "\"", num=NUM, tbs=TBS, pause=PAUSE,
                        extra_params={'filter': '0'}):
            print('B')
            searchlist.append(a)
            sleep(PAUSE)
        print("2")
        for a in search("\"" + decodestring(searchstring) + "\"" + " inurl:" + str(searchid), num=NUM, tbs=TBS,
                        pause=PAUSE, extra_params={'filter': '0'}):
            print('C')
            searchlist.append(a)
            sleep(PAUSE)
        print("3")
        print("removing duplicates")
        res = []
        [res.append(x) for x in searchlist if x not in res]
        encoderes = encodelist(res)
        print("saving")
        with open(searchstring, 'w+') as f:
            for line in encoderes:
                f.write(f"{line}\n")
    if againsearch in (1, 2):
        if os.path.exists(f"{searchstring}.direct"):
            os.remove(f"{searchstring}.direct")
        fr = open(searchstring, 'r+')
        fw = open(f"{searchstring}.direct", "w+")
        print("reading")
        lines = fr.readlines()
        print("matching")
        for line in lines:
            url = decodestring(line)
            url = url.replace(decodestring('bXlkZXNpLm5ldA=='), decodestring("bXlkZXNpMi5uZXQ="))
            if decodestring("aGlmaXh4eC5mdW4=") not in url and decodestring("bXlwb3Jud2FwLmZ1bg==") not in url:
                try:
                    #response = requests.get(url, headers=HEADERS)
                    response = requests.get(url, headers=HEADERS, verify=False)
                    if response.status_code == 200:
                        content = response.text
                        video_src = BeautifulSoup(content,"html.parser").find("link",attrs = {"rel":"video_src"})["href"]
                        videourl = getSeleniumUrl(video_src)
                        print(videourl)
                        if f"data-id=\"{searchid}\"" in content or decodestring(
                                "aGlmaXh4eC5mdW4=") in url or f"{searchid}.mp4" in content or f"{searchid}.mp4" in videourl:
                            print(line)
                            fw.write(line)
                except:
                    pass
            else:
                print(line)
                fw.write(line)
            fr.flush()
            fw.flush()
        fr.close()
        fw.close()
'''
for eachsearch in sbsearches:
    searchid = eachsearch[0]
    searchstring = eachsearch[1]
    searchlist = []
    print("start searching")
    for a in search("\""+decodestring(searchstring)+"\""+" inurl:"+str(decodestring(searchid)),num=20,pause=10):
        searchlist.append(a)
        print("1")
        sleep(10)
    print("3")
    print("removing duplicates")
    res = []
    [res.append(x) for x in searchlist if x not in res]
    encoderes = encodelist(res)
    print("saving")
    with open(searchstring, 'w+') as f:
        for line in encoderes:
            f.write(f"{line}\n")
'''
