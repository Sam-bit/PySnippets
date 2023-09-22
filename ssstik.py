import re
import time

import requests
from selenium import webdriver
browser = None

def download_video(url, name):
    print('Please wait while we found your video')
    browser.get('https://ssstik.io/')
    while True:
        try:
            time.sleep(4)
            browser.find_element_by_id('main_page_text')
            break
        except Exception:
            pass
    text_url = browser.find_element_by_id('main_page_text')
    text_url.send_keys(url)
    text_submit = browser.find_element_by_id('submit')
    time.sleep(5)
    text_submit.click()
    time.sleep(2)
    while True:
        try:
            time.sleep(1)
            browser.find_elements_by_xpath("//*[contains(text(), 'Without watermark [2]')]")[0].click()
            break
        except Exception:
            pass
    main_handler = browser.current_window_handle
    time.sleep(3)
    for handle in browser.window_handles:
        if handle != browser.current_window_handle:
            browser.switch_to.window(handle)
            video_url = browser.current_url
            browser.close()
            browser.switch_to.window(main_handler)
            break

    print(f'Video found downloading {name} please wait')
    r = requests.get(video_url, allow_redirects=True)
    import os
    
    with open(f'{name}.mp4', "wb") as f:
        f.write(r.content)
        print(f'Video {name} downloaded successfully')
    os.system("taskkill /f /im chrome.exe")
    time.sleep(20)


def initialize_selinuim():
    global browser
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data - Copy\\Default")
    options.add_argument("--disable-blink-features=AutomationControlled")
	#options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options)


if __name__ == '__main__':
    # Initialize selenium
    #match = None
    #while match is None:
    #    url = input('Please enter a valid tiktok url\n')
    #    match = re.match(r'https://www.tiktok.com/@[\w]+/video/[\d]+([?][\w])*', url.strip())
    #    if match is None:
    #        print(f'Invalid tiktok url')
    
    from csv import DictReader
	# iterate over each line as a ordered dictionary and print only few column by column name
    with open('URLs.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            url = row['URL']
            print('Initializing session please wait...') 
            groups = None
            
            name = url.split('/')[len(url.split('/')) - 1]
            id = name.split('?')[0]
            from pathlib import Path
            if Path(f'{name}.mp4').is_file():
                continue
            initialize_selinuim()
            download_video(f'{url}', id)
