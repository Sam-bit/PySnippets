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
LOGIN_URL = 'https://www.instagram.com/reel/CfdQDZogJQN/'
options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument("--user-data-dir=C:\\Users\\Sambit Samal\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
PAUSE_TIME = 10
driver = webdriver.Chrome(service=Service(CHROME_DVR_DIR),options = options)
driver.get(LOGIN_URL)
def get_file_content_chrome(driver, uri):
    
    result = driver.execute_async_script("""
    var uri = arguments[0];
    var callback = arguments[1];
    var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'arraybuffer';
    xhr.onload = function(){ callback(toBase64(xhr.response)) };
    xhr.onerror = function(){ callback(xhr.status) };
    xhr.open('GET', %s);
    xhr.send();
    """%(uri))
    if type(result) == int :
        raise Exception("Request failed with status %s" % result)
    return base64.b64decode(result)
f = open('xyz.mp4', 'wb')
actualvdosrc = driver.find_element(By.XPATH, 
        '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div/div[1]/div/div/video').get_attribute('src')
bytes = get_file_content_chrome(driver, actualvdosrc)
f.write(bytes)
f.close()