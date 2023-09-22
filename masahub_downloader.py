import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import requests
import  os
from selenium import webdriver
from pathlib import Path
from urllib.request import urlretrieve
folderdest = "E:\\masahub"
CHROME_DVR_DIR = 'C:\\YOUTUBE-DL\\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options, service=Service(CHROME_DVR_DIR))
driver.minimize_window()
homeurl = "https://masahub.net/page/1/"
def downloadvideo(driver,url,title):
    driver.get(url)
    html = driver.execute_script('return document.body.innerHTML;')
    soup = BeautifulSoup(html,'lxml')
    dllink = soup.find_all('div',class_= 'downLink')[-1].find('a',class_= 'btn').get('href')
    print(dllink)
    ext = os.path.splitext(dllink)[1]
    urlname = Path(dllink).stem
    filename = f'{folderdest}{os.sep}{title} {urlname}{ext}'
    print(f'Downloading {filename}')
    if not os.path.isfile(filename):
        if requests.get(dllink, verify=False).status_code == 200:
            urlretrieve(dllink, filename)
driver.get(homeurl)
html = driver.execute_script('return document.body.innerHTML;')
soup = BeautifulSoup(html,'lxml')
maxpagenum = int(soup.find_all('a',class_= "page-numbers")[-2].text.replace(',',''))
thumblists = soup.find('ul',class_= 'listThumbs')
liList = thumblists.find_all('li')
for li in liList:
    downloadvideo(driver,li.find('a',class_= 'title').get('href'),li.find('a',class_= 'title').text)
print(maxpagenum)
for i in range(2,maxpagenum+1):
    nexturl = "https://masahub.net/page/"+str(i)+"/"
    print(nexturl)
    driver.get(nexturl)
    html = driver.execute_script('return document.body.innerHTML;')
    soup = BeautifulSoup(html,'lxml')
    thumblists = soup.find('ul',class_= 'listThumbs')
    liList = thumblists.find_all('li')
    for li in liList:
        downloadvideo(driver,li.find('a',class_= 'title').get('href'),li.find('a',class_= 'title').text)
    