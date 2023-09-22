from selenium import webdriver
import time,os
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
CHROME_DVR_DIR = 'C:\\YOUTUBE-DL\\chromedriver.exe'
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import  os,openpyxl
from pathlib import Path
from urllib.request import urlretrieve
LOGIN_URL = 'https://web.snapchat.com'
options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument("--user-data-dir=C:\\Users\\LENOVO\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
PAUSE_TIME = 10
driver = webdriver.Chrome(service=Service(CHROME_DVR_DIR),options = options)
driver.get(LOGIN_URL)

#https://web.snapchat.com/0c09c485-3a17-5dcb-8b26-bcea54616f27