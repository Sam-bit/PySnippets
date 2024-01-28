import os , time , glob
from datetime import datetime
from itertools import takewhile , dropwhile

import instaloader

from codecutils import decodestring

download_dir = "E:\\FlutterProjects\\qr_gif_codec\\example\\android\\app\\src\\main\\res\\values\\INSTA"
os.chdir (download_dir)
from subprocess import call
fastUpdate = True
profiles = [
    # 'filmygyan' ,
    # 'bollywoodsocietyy' ,
    # 'viralbhayani' ,
    'bollywoodbubble' ,
    'instantbollywood' ,
    # 'filmymantramedia' ,
    # 'bollywoodirect' ,
    # 'voompla' ,
    # 'manav.manglani'
]
captionToCheck = [
    'nora' ,
    'disha' ,
    'mouni' ,
    'alaya'
    'sherlyn' ,
    'malla' ,
    'giorgia' ,
    'malaika' ,
    'bhumi' ,
    'neha' ,
    'poonam' ,
    'Guess' ,
    'nia' ,
    'vacation',
    'vacay',
    'hot',
    'sexy',
    'sobhita'
]
shortCaptionToCheck = [
    'NF' ,
    'DP' ,
    'MR' ,
    'SC' ,
    'GA' ,
    'NS' ,
    'PP' ,
    'NS'
]
L = instaloader.Instaloader ()
if fastUpdate:
    UNTIL= datetime(2024,1,26)
else:
    UNTIL = datetime (2024 , 1 , 1)
# SINCE = datetime(2024,1,11)
for id in range (len (profiles)):
    L.load_session_from_file ("shyam_it9193")
    profile_name = profiles[id]
    print ("Scrapping {}".format (profile_name))
    # profile_dir = os.path.join(download_dir,profile_name)
    profile_dir = profile_name
    profile = instaloader.Profile.from_username (L.context , profile_name)
    id = 1
    for post in profile.get_posts ():
        print (post.date)

        if post.date < UNTIL and id < 4:
            id += 1
            continue
        elif post.date >= UNTIL:
            caption = post.caption
            if caption is not None:
                if any (cap.lower() in caption.lower() for cap in captionToCheck) or any (cap in caption for cap in shortCaptionToCheck):
                    # print (post.shortcode)
                    L.download_post (post , profile_dir)
                    id += 1
        else:
            break
    L.save_session ()
    time.sleep (60)

# call("instaloader filmygyan --login=shyam_it9193 --stories --post-filter=\"'nora' in caption or 'NF' in caption or 'disha' in caption or 'DP' in caption or 'mouni' in caption or 'MR' in caption\"")
# time.sleep(60)
# call("instaloader bollywoodsocietyy --login=shyam_it9193 --stories")
# time.sleep(60)
# call("instaloader viralbhayani --login=shyam_it9193 --stories")
# time.sleep(60)
# call("instaloader bollywoodbubble --login=shyam_it9193 --stories")
# time.sleep(60)
# call("instaloader instantbollywood --login=shyam_it9193 --stories")
# time.sleep(60)
# call("instaloader filmymantramedia --login=shyam_it9193 --stories")
# time.sleep(60)
# call("instaloader bollywoodirect --login=shyam_it9193 --stories")
# time.sleep(60)
# call("instaloader voompla --login=shyam_it9193 --stories")
# time.sleep(60)
# call("instaloader manav.manglani --login=shyam_it9193 --stories")
