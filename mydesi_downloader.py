import requests
from bs4 import BeautifulSoup
import certifi
import requests
import  os
from pathlib import Path
from urllib.request import urlretrieve
folderdest = "E:\\mydesi"
import urllib3
urllib3.disable_warnings()
#homeurl = 'https://mydesi2.net/page/1/'
if not os.path.exists(folderdest):
    print(f'Created Directory {folderdest}{os.sep}')
    os.makedirs(folderdest)
def downloadvideo(url,title):
    html = requests.get(url, verify=False).text
    soup = BeautifulSoup(html,'lxml')
    dllink = soup.find('div',class_= 'video-actions-box').find('a',class_= 'button').get('href')
    print(url)
    ext = os.path.splitext(dllink)[1]
    urlname = Path(dllink).stem
    filename = f'{folderdest}{os.sep}{title} {urlname}{ext}'
    print(f'Downloading {filename}')
    if not os.path.isfile(filename) and not ':0' in dllink:
        if requests.get(dllink, verify=False).status_code == 200:
            urlretrieve(dllink, filename)
'''       
html = requests.get(homeurl).text
soup = BeautifulSoup(html,'lxml')
maxpagenum = int(soup.find_all('a',class_= "page-link")[-3].text.replace(',',''))
liList = soup.find_all('div',class_= 'video-block video-with-trailer')
for li in liList:
    downloadvideo(li.find('a',class_= 'infos').get('href'),li.find('a',class_= 'infos').get('title'))
print(maxpagenum)
for i in range(2,maxpagenum+1):
    nexturl = "https://mydesi2.net/page/"+str(i)+"/"
    print(nexturl)
    html = requests.get(nexturl).text
    soup = BeautifulSoup(html,'lxml')
    liList = soup.find_all('div',class_= 'video-block video-with-trailer')
    for li in liList:
        downloadvideo(li.find('a',class_= 'infos').get('href'),li.find('a',class_= 'infos').get('title'))
'''
maxid = 5000
homeurl ='https://www.mydesi2.net/mix-tg-collection-1/'
html = requests.get(homeurl).text
soup = BeautifulSoup(html,'html.parser')
print(soup)
