from selenium import webdriver
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
CHROME_DVR_DIR = 'C:\\YOUTUBE-DL\\chromedriver.exe'
driver=webdriver.Chrome(CHROME_DVR_DIR)

file = open("output.txt","w+")

driver.get('https://www.youtube.com/watch?v=_p2NvO6KrBs')
time.sleep(5)
'''
#new scrolling
while(len(driver.find_elements_by_css_selector('#spinnerContainer > div.spinner-layer.layer-4.style-scope.tp-yt-paper-spinner > div.circle-clipper.left.style-scope.tp-yt-paper-spinner > div')) > 0):
    #scroll 1000 px
    driver.execute_script('window.scrollTo(0,(window.pageYOffset+1000))')
    #waiting for the page to load
    time.sleep(1.5) 
'''
wait = WebDriverWait(driver,3)
for item in range(200): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
main_comments = driver.find_elements_by_css_selector('#contents > ytd-comment-thread-renderer:nth-child(1)') # get all the comments

for mc in main_comments:
    main_comment_channel = mc.find_element_by_id('author-text').get_attribute('href')
    file.write('The comments channel is: ' + main_comment_channel + '\n') #write the channel of the main comment to file

    replies = mc.find_element_by_xpath('..//*[@id="replies"]') # get the replies section of the above comment
    if replies.text.startswith('View'): # check if there are any replies
        reply = replies.find_element_by_css_selector('a');
        driver.execute_script("arguments[0].scrollIntoView();", reply) # bring view replies into view
        driver.execute_script('window.scrollTo(0,(window.pageYOffset-150))') # cater for the youtube header
        reply.click() # if so open the replies
        time.sleep(3) # wait for load (better strategy should be used here

        for reply in replies.find_elements_by_id('author-text'):
            reply_channel = reply.get_attribute('href')
            file.write('Reply channel: ' + reply_channel + '\n') # write the channel of each reply to file

file.close()
