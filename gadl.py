import os,time,glob
from datetime import datetime

import instaloader

from codecutils import decodestring
download_dir ="E:\\FlutterProjects\\qr_gif_codec\\example\\android\\app\\src\\main\\res\\values\\INSTA"
os.chdir(download_dir)
from subprocess import call
L = instaloader.Instaloader()
L.load_session_from_file("shyam_it9193")
hashtags = instaloader.Hashtag.from_name(L.context,'giorgiaandriani')
for post in hashtags.get_top_posts():
    print(post.date)
    L.download_post(post, "#giorgiaandriani")
    L.save_session()