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
import  os
from pathlib import Path
from urllib.request import urlretrieve
LOGIN_URL = 'https://www.facebook.com/login.php'
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--user-data-dir=C:\\Users\\Sambit Samal\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
PAUSE_TIME = 5
downloadfolder = "E:\\facebookalbums"
class FacebookLogin():
    def __init__(self, email, password):
        # Store credentials for login
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(service=Service(CHROME_DVR_DIR),options = options)
        self.driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load      
    def login(self):
        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give keyboard input
 
        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as input too
 
        login_button = self.driver.find_element_by_id('loginbutton')
        login_button.click() # Send mouse click
 
        time.sleep(2) # Wait for 2 seconds for the page to show up
    
    def download_image(self,image_url,folderpath):
        self.driver.get(image_url)
        time.sleep(PAUSE_TIME)
        actualimgsrc = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/img').get_attribute('src')
        imgsrc = actualimgsrc.split('?')[0]
        ext = os.path.splitext(imgsrc)[1]
        urlname = Path(imgsrc).stem
        filename = f'{folderpath}{os.sep}{urlname}{ext}'
        if not os.path.isfile(filename):
            if requests.get(actualimgsrc).status_code == 200:
                print(f'Downloading {filename}')
                urlretrieve(actualimgsrc, filename)
        else:
            print(f'File {filename} already exists')
            return
    def download_video(self,video_url,folderpath):
        self.driver.get(video_url)
        time.sleep(PAUSE_TIME)
        actualvdosrc = self.driver.find_element(By.XPATH, 
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/video').get_attribute('src')
        vdosrc = actualvdosrc.split('?')[0]
        ext = os.path.splitext(vdosrc)[1]
        urlname = Path(vdosrc).stem
        filename = f'{folderpath}{os.sep}{urlname}{ext}'
        if not os.path.isfile(filename):
            if requests.get(actualvdosrc).status_code == 200:
                print(f'Downloading {filename}')
                urlretrieve(actualvdosrc, filename)
        else:
            print(f'File {filename} already exists')
            return
    def scroll_page_videos_by(self, profile_id,downloadfolder):
        folderpath = f'{downloadfolder}{os.sep}{profile_id}{os.sep}videos_by'
        if not os.path.exists(folderpath):
            print(f'Created Directory {folderpath}')
            os.makedirs(folderpath)
            time.sleep(2)
        with open('videos_by.txt', 'r') as file:
            element = file.read().replace('\n', '')
            soup = BeautifulSoup(element,'html.parser')
            for elem in soup.find_all('div'):
                if elem.find('div'):
                    for imgelem in elem.find('div'):
                        if(imgelem.find("a")):
                            try:
                                self.download_video(imgelem.find("a")["href"],folderpath)
                            except:
                                pass
            file.close()
            
    def scroll_page_videos_of(self, profile_id,downloadfolder):
        folderpath = f'{downloadfolder}{os.sep}{profile_id}{os.sep}videos_of'
        if not os.path.exists(folderpath):
            print(f'Created Directory {folderpath}')
            os.makedirs(folderpath)
            time.sleep(2)
        with open('videos_of.txt', 'r') as file:
            element = file.read().replace('\n', '')
            soup = BeautifulSoup(element,'html.parser')
            for elem in soup.find_all('div'):
                if elem.find('div'):
                    for imgelem in elem.find('div'):
                        if(imgelem.find("a")):
                            try:
                                self.download_video(imgelem.find("a")["href"],folderpath)
                            except:
                                pass
            file.close()
    def get_album_photos(self, album_url, album_title, folderpath):
        folderpath = f'{folderpath}{os.sep}{album_title}'
        if not os.path.exists(folderpath):
            print(f'Created Directory {folderpath}')
            os.makedirs(folderpath)
            time.sleep(2)
        self.driver.get(album_url)
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        time.sleep(PAUSE_TIME)
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                time.sleep(PAUSE_TIME)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(PAUSE_TIME)
                if new_height == last_height:
                    xpathroot = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[2]/div/div'
                    divs = self.driver.find_element(by=By.XPATH, value=xpathroot)
                    element = divs.get_attribute('innerHTML')
                    soup = BeautifulSoup(element,'html.parser')
                    for elem in soup.find_all('div'):
                        if elem.find('a'):
                            self.download_image("https://www.facebook.com/"+elem.find('a')['href'],folderpath)
                    break
            time.sleep(PAUSE_TIME)
            last_height = new_height
    def scroll_page_photos_albums(self, profile_id,downloadfolder):
        folderpath = f'{downloadfolder}{os.sep}{profile_id}{os.sep}photos_albums'
        if not os.path.exists(folderpath):
            print(f'Created Directory {folderpath}')
            os.makedirs(folderpath)
            time.sleep(2)
        num_files=len([entry for entry in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, entry))])
        element = divs.get_attribute('innerHTML')
        soup = BeautifulSoup(element,'html.parser')
        for elem in soup.find_all('div'):
            if elem.find('div'):
                if elem.find('div').find('a'):
                    print(elem.find('div').find('a')['href'])
                    titlelist = []
                    for divelem in list(set(elem.find('div').find('a').find('div').find('div').find_all('div'))):
                        if(divelem.find('div')):
                            if(divelem.find('div').find('span')):
                                titlelist.append(divelem.find('div').find('span').text)
                    self.get_album_photos(elem.find('div').find('a')['href'],str(list(set(titlelist))[0]).replace('..',' '),folderpath)

    
    def scroll_page_photos_by(self, profile_id,downloadfolder):
        folderpath = f'{downloadfolder}{os.sep}{profile_id}{os.sep}photos_by'
        if not os.path.exists(folderpath):
            print(f'Created Directory {folderpath}')
            os.makedirs(folderpath)
            time.sleep(2)
        num_files=len([entry for entry in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, entry))])
        print(num_files)
        with open('photos_by.txt', 'r',encoding = 'utf-8') as file:
            element = file.read()
            soup = BeautifulSoup(element,'html.parser')
            for elem in soup.find_all('div'):
                if elem.find('div'):
                    for imgelem in elem.find('div'):
                        if(imgelem.find("a")):
                            try:
                                self.download_image(imgelem.find("a")["href"],folderpath)
                            except:
                                pass
            file.close()
            
    def scroll_page_photos(self, profile_id,downloadfolder):
        folderpath = f'{downloadfolder}{os.sep}{profile_id}{os.sep}photos'
        if not os.path.exists(folderpath):
            print(f'Created Directory {folderpath}')
            os.makedirs(folderpath)
            time.sleep(2)
        num_files=len([entry for entry in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, entry))])
        
        with open('photos.txt', 'r') as file:
            element = file.read()
            soup = BeautifulSoup(element,'html.parser')
            for elem in soup.find_all('div'):
                if elem.find('div'):
                    for imgelem in elem.find('div'):
                        if(imgelem.find("a")):
                            try:
                                self.download_image(imgelem.find("a")["href"],folderpath)
                            except:
                                pass
            file.close()
            
if __name__ == '__main__':
    # Enter your login credentials here
    profile = input("Enter the profile id : ")
    fb_login = FacebookLogin(email='mailsambit@yahoo.co.in', password='SUM#@BEET#@7172')
    #fb_login.login()
    #fb_login.scroll_page_photos(profile,downloadfolder)
    fb_login.scroll_page_photos_by(profile,downloadfolder)
    #fb_login.scroll_page_photos_albums(profile,downloadfolder)
    #os.system("taskkill /f /im chrome.exe")
    #fb_login.scroll_page_photos_by('shradhanjali.rout.1',downloadfolder)