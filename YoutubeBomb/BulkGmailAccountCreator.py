from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pandas_datareader as dr
from selenium import webdriver
CHROME_DVR_DIR = 'C:\\YOUTUBE-DL\\chromedriver.exe'
FULLNAME =""
def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.3)
signup_url = 'https://accounts.google.com/signup/v2/webcreateaccount?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp'
driver = webdriver.Chrome(CHROME_DVR_DIR)
driver.get(signup_url)
time.sleep(2)
username = browser.find_element_by_id('firstName')
# username.send_keys('John Doe')
slow_typing(username, 'John Doe')

time.sleep(1)
# Fill user's email ID
email = browser.find_element_by_id('user_email_login')
slow_typing(email, EMAIL_ID)

time.sleep(2)
# Fill user's password
password = browser.find_element_by_id('user_password')

# Reads password from a text file because
# it's silly to save the password in a script.
with open('password.txt', 'r') as myfile:
       Password = myfile.read().replace('\n', '')
slow_typing(password, Password)

time.sleep(1)
# click on Terms and Conditions
toc = browser.find_element_by_name('terms_and_conditions')
toc.click()

# click on signup page
signupbutton = browser.find_element_by_id('user_submit')
signupbutton.click()

time.sleep(20)