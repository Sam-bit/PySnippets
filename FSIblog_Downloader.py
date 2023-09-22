import 
import requests
from bs4 import BeautifulSoup
import certifi
import requests
import  os
from pathlib import Path
from urllib.request import urlretrieve
import cloudscraper

scraper = cloudscraper.create_scraper()  # returns a CloudflareScraper instance
folderdest = "E:\\fsiblog2"
import urllib3
urllib3.disable_warnings()
homeurl = 'https://www.fsiblog2.com/porn-videos/'
def downloadvideo(url,title):
    html = requests.get(url, verify=False).text
    soup = BeautifulSoup(html,'lxml')
    dllink = soup.find('div',class_= 'video-actions-box').find('a',class_= 'button').get('href')
    print(url)
    ext = os.path.splitext(dllink)[1]
    urlname = Path(dllink).stem
    filename = f'{folderdest}{os.sep}{title} {urlname}{ext}'
    print(f'Downloading {filename}')
    if not os.path.isfile(filename):
        if requests.get(dllink, verify=False).status_code == 200:
            urlretrieve(dllink, filename)
       
html = scraper.get(homeurl).content
print(html)
soup = BeautifulSoup(html,'lxml')
maxpagenum = soup.find_all('a',class_= "page-numbers")
liList = soup.find_all('div',class_= 'video-block video-with-trailer')
for li in liList:
    downloadvideo(li.find('a',class_= 'infos').get('href'),li.find('a',class_= 'infos').get('title'))
print(maxpagenum)
for i in range(1,maxpagenum+1):
    nexturl = "https://www.fsiblog2.com/porn-videos/page/"+str(i)+"/"
    print(nexturl)
    html = requests.get(nexturl).text
    soup = BeautifulSoup(html,'lxml')
    liList = soup.find_all('div',class_= 'video-block video-with-trailer')
    for li in liList:
        downloadvideo(li.find('a',class_= 'infos').get('href'),li.find('a',class_= 'infos').get('title'))
    