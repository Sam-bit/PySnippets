import requests
from html import unescape
from urllib.parse import unquote

url = 'https://www.facebook.com/photo.php?fbid=1283120832168860&set=pb.100014128659584.-2207520000..&type=3'

CHROME_DVR_DIR = 'C:\\YOUTUBE-DL\\chromedriver.exe'
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(CHROME_DVR_DIR)
browser.get(url)

html_source = browser.page_source
html_soup = BeautifulSoup(html_source, 'html.parser')
src = driver.find_element_by_xpath('//*[@id="mount_0_0_7s"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/img').get_attribute("src")

var urls = document.getElementsByTagName('a');
for (var i = 0; i < urls.length; i++) {
    if(urls[i].getAttribute('href') != null){
        if(urls[i].getAttribute('href').indexOf('photo.php') > -1) {
            console.log(urls[i].getAttribute('href'));
            /*window.open(urls[i].getAttribute('href'));
            var imgs = document.getElementsByTagName("img");
            for (var i = 0; i < imgs.length; i++) {
                //if(imgs[i].getAttribute("data-visualcompletion")=="media-vc-image"){
                    console.log (imgs[i].src);
                //}
            }*/
        }
    }
}

var urls = document.getElementsByTagName('a');
for (var i = 0; i < urls.length; i++) {
    if(urls[i].getAttribute('href') != null){
        if(urls[i].getAttribute('href').indexOf('photo.php') > -1) {
            console.log(urls[i].getAttribute('href'));
            window.open(urls[i].getAttribute('href'));
            var imgs = document.getElementsByTagName("img");
            for (var i = 0; i < imgs.length; i++) {
                //if(imgs[i].getAttribute("data-visualcompletion")=="media-vc-image"){
                    console.log (imgs[i].src);
                //}
            }
        }
    }
}