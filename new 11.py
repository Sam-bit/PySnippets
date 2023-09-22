import sys, unittest, time, datetime
import urllib.request, urllib.error, urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.chrome.options import Options
browser = None
CHROME_DVR_DIR = 'C:\\YOUTUBE-DL\\chromedriver.exe'
def initialize_selinuim():
    global browser
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=C:\\Users\\Sambit Samal\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    options.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(CHROME_DVR_DIR,options = options)
url = "https://www.youtube.com/channel/UC1uZXqCLkgznYsI74eamASg/videos"
channelid = url.split('/')[4]
#driver=webdriver.Firefox()
initialize_selinuim()
browser.get(url)
time.sleep(5)
height = browser.execute_script("return document.documentElement.scrollHeight")
lastheight = 0

while True:
    if lastheight == height:
        break
    lastheight = height
    browser.execute_script("window.scrollTo(0, " + str(height) + ");")
    time.sleep(2)
    height = browser.execute_script("return document.documentElement.scrollHeight")

user_data = browser.find_elements_by_xpath('//*[@id="video-title"]')
for i in user_data:
    print(i.get_attribute('href'))
    link = (i.get_attribute('href'))
    browser.get(link)
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH , '//body/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-watch-flexy[1]/div[5]/div[1]/div[1]/div[8]/div[2]/ytd-video-primary-info-renderer[1]/div[1]/div[1]/div[3]/div[1]/ytd-menu-renderer[1]/div[1]/ytd-toggle-button-renderer[1]/a[1]/yt-icon-button[1]/button[1]/yt-icon[1]')))
    button.click()