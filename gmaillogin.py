from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
email = 'itsme.sambit1991@gmail.com'
password="SUM@#BEET@#717171"
driver = webdriver.Chrome(service=Service(executable_path="C:\\DRIVERS\chromedriver.exe"))
driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
driver.find_element(By.XPATH,'//*[@id="openid-buttons"]/button[1]').click()
driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys(email)
input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))
    )
input.click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))
    )
input.click()
driver.implicitly_wait(1)
driver.get('https://www.google.com/')
