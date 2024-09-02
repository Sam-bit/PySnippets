
import urllib.request 
proxies =None#urllib.request.getproxies()
import os
import requests
from utils import download_file_with_progress
os.chdir ("D:\\FlutterProjects\\qrgifcodec\\example\\test\\telegram-20240411T171106Z-001\\telegram\\Test")
startnum= 1 #440
endnum = 999999

with open("startnum1.txt","r") as f:
    startnum = int(f.read())
    f.close()
try:
    loop = range(startnum,endnum)
    for urlid in loop:
        for frameid in range(1,13):
            print(urlid)
            try:
                r = requests.head("https://static.filedownloadlink.xyz/pview/{}/frame_{}.jpg".format(urlid,frameid),proxies = proxies )
                status_code = r.status_code
                if status_code == 200:
                    url = "https://static.filedownloadlink.xyz/pview/{}/frame_{}.jpg".format(urlid,frameid)
                    #print(url)
                    download_file_with_progress(url,str(urlid)+"_frame_"+str(frameid)+".jpg",proxies = proxies ,skip_above_mb = 500)
            except requests.ConnectionError:
                print("failed to connect")
        with open("startnum1.txt", "w") as f:
            f.write(str(urlid))
            f.close()
            #prints the int of the status code*
            
except requests.ConnectionError:
                print("failed to connect")
                