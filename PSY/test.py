from selenium.webdriver.chrome.service import Service

import codecutils
import cfscrape
import requests
from bs4 import BeautifulSoup
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
import urllib3
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, service=Service(r'C:\DRIVERS\chromedriver.exe'))
urllib3.disable_warnings()
a = 'aHR0cHM6Ly9vbmx5aW5kaWFucG9ybnguY29tL21vdi8xNTkzNjQvcHJpeWFua2EteWFkYXYtdGFuZ28tcHJpdmF0ZS5odG1s'
url = codecutils.decodestring(a)
#response = requests.get(url, headers=HEADERS)
response = requests.get(url, headers=HEADERS, verify=False)
if response.status_code == 200:
    content = response.text
    video_src = BeautifulSoup(content,"html.parser").find("link",attrs = {"rel":"video_src"})["href"]
    print(video_src)
    driver.get(video_src)
    print(driver.current_url)