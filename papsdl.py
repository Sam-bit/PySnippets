import os,time,glob
from datetime import datetime

import instaloader

from codecutils import decodestring
download_dir ="E:\\FlutterProjects\\qr_gif_codec\\example\\android\\app\\src\\main\\res\\values\\INSTA"
os.chdir(download_dir)
from subprocess import call
localappdata =os.getenv("LOCALAPPDATA")
folderpath = os.path.join(localappdata,"Instaloader")
profiles =['filmygyan',
           'bollywoodsocietyy',
           'viralbhayani',
           'bollywoodbubble',
           'instantbollywood',
           'filmymantramedia',
           'bollywoodirect',
           'voompla',
           'manav.manglani'
           ]
captionToCheck = [
    'nora',
    'NF',
    'disha',
    'DP',
    'mouni',
    'MR',
    'SC',
    'sherlyn',
    'malla',
    'giorgia',
    'GA'
]
L = instaloader.Instaloader()

for id in range(len(profiles)):
    L.load_session_from_file("shyam_it9193")
    profile_name = profiles[id]
    print("Scrapping {}".format(profile_name))
    #profile_dir = os.path.join(download_dir,profile_name)
    profile_dir  = profile_name
    profile = instaloader.Profile.from_username(L.context,profile_name)
    for post in profile.get_posts():
        print(post.date)
        if post.date >= datetime(2023,12,1):
            caption = post.caption
            if caption is not None:
                if any(cap.lower() in caption.lower() for cap in captionToCheck):
                    print(post.shortcode)
                    L.download_post(post,profile_dir)
        else:
            break
    L.save_session()
    time.sleep(60)


#call("instaloader filmygyan --login=shyam_it9193 --stories --post-filter=\"'nora' in caption or 'NF' in caption or 'disha' in caption or 'DP' in caption or 'mouni' in caption or 'MR' in caption\"")
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
