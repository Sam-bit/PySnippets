
from datetime import datetime
from urllib.request import urlretrieve

import requests,os
from bs4 import BeautifulSoup
import json
import urllib3
urllib3.disable_warnings()
from codecutils import decodestring
folderpath= decodestring('RTpcXEZsdXR0ZXJQcm9qZWN0c1xccXJfZ2lmX2NvZGVjXFxleGFtcGxlXFxhbmRyb2lkXFxhcHBcXHNyY1xcbWFpblxca290bGluXFxjb21cXHNvbWViaXRlc1xccGx1Z2luXFxxcl9naWZfY29kZWNfZXhhbXBsZQ==')
recent =4
print(str(datetime.now().timestamp()).replace('.', ''))
with open("latestnum.txt","r") as f:
    latestnum = int(f.read())
    f.close()
def downloadFileId(fileid):
    url = decodestring('aHR0cHM6Ly9tb2phcHAuaW4vQHByaXlhbmthXzY2MDUvdmlkZW8v') + str(fileid)
    #url = decodestring('aHR0cHM6Ly9tb2phcHAuaW4vQDcyMDY5NDYzMDExL3ZpZGVvLw==') + str(fileid)
    #url = decodestring('aHR0cHM6Ly9tb2phcHAuaW4vQHByaXlhbmtheWFkYXY2NjA1L3ZpZGVvLw==') + str(fileid)
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'html.parser')
    print(response.text)
    if soup.find('script', attrs={"sveltekit:data-type": "data"}):
        jsonText = soup.find('script', attrs={"sveltekit:data-type": "data"}).text
        resp = json.loads(jsonText)
        authorId = json.loads(resp['body'])['payload']['d']['authorId']
        if str(authorId) == "77514096901" or str(authorId) == "72296579811" or str(authorId) == "72069463011":
            fileurl = json.loads(resp['body'])['payload']['d']['v']
            ext = os.path.splitext(fileurl)[1]
            filename = f'{folderpath}{os.sep}{fileid}{ext}'
            if not os.path.isfile(filename):
                if requests.get(fileurl, verify=False).status_code == 200:
                    print(f'Downloading {fileid}')
                    urlretrieve(fileurl, filename)
if recent == 1:
    url = decodestring('aHR0cHM6Ly9tb2phcHAuaW4vQHByaXlhbmthXzY2MDU=')
    #url = decodestring('aHR0cHM6Ly9tb2phcHAuaW4vQDcyMDY5NDYzMDEx')
    #url = decodestring('aHR0cHM6Ly9tb2phcHAuaW4vQHByaXlhbmtheWFkYXY2NjA1')
    response = requests.get(url)
    response.encoding = "utf-8"
    #print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    jsonText =soup.find_all('script')[-3].text
    resp = json.loads(jsonText)
    all_vids =json.loads(resp['body'])['payload']['d']
    latest_num = all_vids[0]['i']
    with open("latestnum.txt", "w") as f:
        f.write(str(latest_num))
        f.close()
    for vid in all_vids:
        fileid =vid['i']
        print(fileid)
        #if int(fileid)== latestnum:
        #    break
        with open("fileids.txt", "r+") as file:
            for line in file:
                if fileid in line:
                    break
            else:
                file.write(fileid + "\n")
                file.flush()
        downloadFileId(fileid)
elif recent == 2:
    jsonText = open("lists.json","r",encoding="utf-8").read()
    resp = json.dumps(json.loads(jsonText))
    all_vids =  json.loads(resp)
    for vid in all_vids:
        fileid = vid['i']
        print(fileid)
        downloadFileId(fileid)
elif recent== 3:
    jsonText = open('E:\\FlutterProjects\\DUMMY\\qrgifcodec\\New Text Document.txt', "r", encoding="utf-8").read()
    resp = json.dumps(json.loads(jsonText))
    all_vids = json.loads(resp)
    latest_num = all_vids[0]['i']
    for vid in all_vids:
        fileid = vid['i']
        print(fileid)
        if int(fileid) == latestnum:
            break
        with open("fileids.txt", "r+") as file:
            for line in file:
                if fileid in line:
                    break
            else:
                file.write(fileid + "\n")
                file.flush()
        fileurl = vid['v']
        with open("latestnum.txt", "w") as f:
            f.write(str(latest_num))
            f.close()
        head, sep, tail = fileurl.partition('?')
        ext = os.path.splitext(head)[1]
        filename = f'{folderpath}{os.sep}{fileid}{ext}'
        if not os.path.isfile(filename):
            if requests.get(fileurl, verify=False).status_code == 200:

                print(f'Downloading {fileid}')
                urlretrieve(fileurl, filename)
else:
    import webbrowser
    #url = decodestring('aHR0cDovL3dhLm1lLys5MTc0MTY2MjEyMTk=')
    url = decodestring('aHR0cHM6Ly9hcGkud2hhdHNhcHAuY29tL3NlbmQvP3Bob25lPSUyQjkxNzQxNjYyMTIxOSZ0ZXh0JnR5cGU9cGhvbmVfbnVtYmVyJmFwcF9hYnNlbnQ9MA==')
    import winreg
    import re
    command = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "ChromeHTML\\shell\open\\command", 0, winreg.KEY_READ), "")[0]
    exe=re.search("\"(.*?)\"", command).group(1)
    chrome_path = exe.replace("\\","\\\\")
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)
    #print(jsonText)

#url = 'd2EubWUvKzkxNzQxNjYyMTIxOQ=='
