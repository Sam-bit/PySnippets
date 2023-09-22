from bs4 import *
import requests
import os
import re
# CREATE FOLDER
def folder_create(title,i,images):
    if not os.path.exists(title):
        os.makedirs(title)
    if not os.path.exists(os.path.join(title,i)):
        os.makedirs(os.path.join(title,i))
    # image downloading start
    download_images(images, os.path.join(title,i))


# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):
    count = 0
    print(f"Total {len(images)} Image Found!")
    if len(images) != 0:
        for i, image in enumerate(images):
            # From image tag ,Fetch image Source URL

                        # 1.data-srcset
                        # 2.data-src
                        # 3.data-fallback-src
                        # 4.src

            # Here we will use exception handling

            # first we will search for "data-srcset" in img tag
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["data-srcset"]
                
            # then we will search for "data-src" in img
            # tag and so on..
            except:
                try:
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]
                except:
                    try:
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            # In image tag ,searching for "src"
                            image_link = image["src"]

                        # if no Source URL found
                        except:
                            pass

            # After getting Image Source URL
            # We will try to get the content of image
            try:
                r = requests.get(image_link).content
                try:

                    # possibility of decode
                    r = str(r, 'utf-8')

                except UnicodeDecodeError:

                    # After checking above condition, Image Download start
                    with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
                        f.write(r)

                    # counting number of image downloaded
                    count += 1
            except:
                pass

        # There might be possible, that all
        # images not download
        # if all images download
        if count == len(images):
            print("All Images Downloaded!")
            
        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")

# MAIN FUNCTION START
def main(url,i):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = re.sub('\W+',' ', soup.find('title').text)
    images = soup.findAll('img')
    folder_create(title,i,images)
#https://xossipz.com/forum-pics-n-vids-adult?page=2
#https://xossipz.com/Thread-desi-pics-desi-sexy-and-horny-desi-girls-100-satisfication?page=268
#https://xossipz.com/Thread-desi-vids-dhamakedar-desi-video-thread-2020-daily-update?page=2
#https://xossipz.com/Thread-desi-vids-new-leaked-desi-girl-sex-mms-video-updated-daily?page=2
#https://xossipz.com/Thread-desi-pics-exclusive-pics-vids-of-desi-girls?page=2
#https://xossipz.com/Thread-desi-pics-beauty-desi-nude-hot-sex-videos-and-nude-videos-collection
#https://xossipz.com/Thread-desi-pics-my-jerk-collection
#https://xossipz.com/Thread-desi-vids-desi-new-leaked-mms-2020-and-2021?page=2
url = "https://xossipz.com/Thread-desi-pics-desi-sexy-and-horny-desi-girls-100-satisfication?page="
for i in range(73,118):
    newurl = url + str(i)
    main(newurl,str(i))
