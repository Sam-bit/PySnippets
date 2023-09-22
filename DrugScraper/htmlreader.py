import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def getRequestSoup(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def getChromeSoup(url):
    options = Options()
    # options.headless = True
    browser = webdriver.Chrome(service=Service("C:\\DRIVERS\\chromedriver.exe"), options=options)
    # get source code
    browser.get(url)
    html = browser.page_source
    time.sleep(2)
    # close web browser
    browser.close()
    soup = BeautifulSoup(html, 'html.parser')
    return soup
