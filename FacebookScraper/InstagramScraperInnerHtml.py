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
LOGIN_URL = 'https://www.instagram.com/'
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--user-data-dir=C:\\Users\\Sambit Samal\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
PAUSE_TIME = 10
class InstagramLogin():
    def __init__(self, email, password,profile):
        # Store credentials for login
        self.email = email
        self.profile = profile
        self.password = password
        self.workbook_obj = openpyxl.load_workbook(self.profile+".xlsx")
        self.sheet_obj = self.workbook_obj.active
        self.driver = webdriver.Chrome(service=Service(CHROME_DVR_DIR),options = options)
        self.driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load      
    def login(self):
        email_element = self.driver.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        email_element.send_keys(self.email) # Give keyboard input
 
        password_element = self.driver.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        password_element.send_keys(self.password) # Give password as input too
 
        login_button = self.driver.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
        login_button.click() # Send mouse click
 
        time.sleep(2) # Wait for 2 seconds for the page to show up
    def get_post_page(self,post_url):
        self.driver.get(post_url)
        
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            #time.sleep(PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            time.sleep(PAUSE_TIME)
            if new_height == last_height:
                #time.sleep(PAUSE_TIME)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(PAUSE_TIME)
                if new_height == last_height:
                    xpathroot = '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul'
                    uls = self.driver.find_element(by=By.XPATH, value=xpathroot)
                    element = uls.get_attribute('innerHTML')
                    soup = BeautifulSoup(element,'html.parser')
                    for elem in soup.find_all('ul'):
                        user_comments = []
                        user_comments.append(post_url)
                        user_comments.append(elem.find('div').find('li').find('div').find('div').find_all('div')[2].find('h3').text)
                        user_comments.append(elem.find('div').find('li').find('div').find('div').find_all('div')[2].find_all('div')[1].text)
                        self.sheet_obj.append(user_comments)
                        self.workbook_obj.save(self.profile+".xlsx")
                    break
            #time.sleep(PAUSE_TIME)
            last_height = new_height
                        
    def scroll_page_profile(self, profile_id):
        photos_id_url = 'https://www.instagram.com/'+profile_id+'/'
        self.driver.get(photos_id_url)
        with open('insta.txt', 'r', encoding="utf-8") as file:
            element = file.read()
            soup = BeautifulSoup(element,'html.parser')
            for elem in soup.find_all('div'):
                if elem.find('div'):
                    #print(elem)
                    for divelem in elem.find_all('div'):
                        for imgelem in divelem.find_all('a'):
                            #print(imgelem)
                            try:
                                print(LOGIN_URL+(imgelem["href"][1:]))
                                self.get_post_page(LOGIN_URL+(imgelem["href"][1:]))
                            except:
                                pass
            file.close()
if __name__ == '__main__':
    # Enter your login credentials here
    
    profile = "impriyankayadav_official"
    insta_login = InstagramLogin(email='sam_bytes', password='SUM@#BEET@#2022',profile = profile)
    #insta_login.login()
    
    insta_login.scroll_page_profile(profile)
    #insta_login.get_post_page('https://www.instagram.com/p/CfEUmE-KA8D/')
    #os.system("taskkill /f /im chrome.exe")
    #insta_login.scroll_page_photos_by('shradhanjali.rout.1',downloadfolder)