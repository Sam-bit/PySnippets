import os , time , glob
from codecutils import decodestring

os.chdir ("E:\\FlutterProjects\\qr_gif_codec\\example\\android\\app\\src\\main\\res\\values\\INSTA")
from subprocess import call
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"
timeout = 86400
localappdata = os.getenv ("LOCALAPPDATA")
folderpath = os.path.join (localappdata , "Instaloader")
call (
    "instaloader priyankayadav026 --login=shyam_it9193 --fast-update --stories --request-timeout={} --user-agent=\"{}\"".format (
        timeout , useragent))
