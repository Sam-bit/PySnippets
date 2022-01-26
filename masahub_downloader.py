import requests
from bs4 import BeautifulSoup
import urllib3
import certifi
import requests

try:
    print('Checking connection to Github...')
    test = requests.get('https://masahub.com/page/1/')
    print('Connection to Github OK.')
except requests.exceptions.SSLError as err:
    print('SSL Error. Adding custom certs to Certifi store...')
    cafile = certifi.where()
    with open('certicate.pem', 'rb') as infile:
        customca = infile.read()
    with open(cafile, 'ab') as outfile:
        outfile.write(customca)
    print('That might have worked.')
homeurl = "https://masahub.com/page/1/"
# User Agent to prevent Response 429
userAgent = {
    'User-agent': 'Masahub Downloader Bot 1.0 (by Sambit)'
}
'''
response = requests.get(homeurl, headers=userAgent,verify = True,cert= "C:\\Python37\\Lib\\site-packages\\certifi\\cacert.pem")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    maxpagenum = soup.find_all('a',class_= "page-numbers")[-2].text'''