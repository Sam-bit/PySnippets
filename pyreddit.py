import argparse
import requests
import os,re,sys
import time
from urllib.request import urlretrieve
from pathlib import Path

def download(imageurl, filename, source, foldername):
    try:
        filepath = foldername
        if not os.path.exists(filepath):
            print(f'Created Directory {filepath}{os.sep}')
            os.makedirs(filepath)
            time.sleep(2)

        elif source == 'i.imgur.com':
            imageurl = imageurl.replace('.gifv', '.mp4')
            fileurl = os.path.splitext(imageurl)[1]
            filename = re.sub('\W+',' ', filename)
            filename = f'{filepath}{os.sep}{filename}{fileurl}'
            if os.path.exists(filename):
                if duplicatecaption == 'y':
                    file_response = requests.head(imageurl)
                    size = file_response.headers.get('content-length',-1)
                    filesize=os.stat(filename).st_size
                    if size == filesize:
                        return
                    x = filename.rsplit(".", 1)
                    i = 1
                    x[0] = x[0]+"("+str(i)+")"
                    x[1] = "."+x[1]
                    dupfilename = ''.join(map(str, x))
                    urlretrieve(imageurl, dupfilename)
                    i += 1
                    return False
                else:
                    print(f'File {filename} already exists')
                    return
                return False

            print(f'Downloading {filename}')
            urlretrieve(imageurl, filename)

        elif source == 'i.redd.it':
            fileurl = os.path.splitext(imageurl)[1]
            filename = re.sub('\W+',' ', filename)
            filename = f'{filepath}{os.sep}{filename}{fileurl}'

            if os.path.exists(filename):
                if duplicatecaption == 'y':
                    file_response = requests.head(imageurl)
                    size = file_response.headers.get('content-length',-1)
                    filesize=os.stat(filename).st_size
                    if size == filesize:
                        return
                    x = filename.rsplit(".", 1)
                    i = 1
                    x[0] = x[0]+"("+str(i)+")"
                    x[1] = "."+x[1]
                    dupfilename = ''.join(map(str, x))
                    urlretrieve(imageurl, dupfilename)
                    i += 1
                    return False
                else:
                    print(f'File {filename} already exists')
                    return
                return False

            print(f'\nDownloading {filename}')
            urlretrieve(imageurl, filename)

    except Exception as e:
        print(e)

def connection(url,downloadfolder,subreddit):

    # User Agent to prevent Response 429
    userAgent = {
        'User-agent': 'Python Reddit Media Downloader Bot : 0.1 (by Sambit)'
    }

    response = requests.get(url, headers=userAgent)
    if response.status_code == 200:
        print("\nConnection Successful!")
        time.sleep(2)
        print(f"Starting Download...")
        time.sleep(1)

        responsejson = response.json()
        nextpage = responsejson['data']['after']
        posts = responsejson['data']['children']
        for post in posts:
            source = post['data']['domain']
            mediaurl = post['data']['url']
            filename = post['data']['title']
            article_date = post['data']['created']
            formatted_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(article_date)))
            urlname = Path(mediaurl).stem
            # Works on Windows, Linux and Mac!
            if downloadfolder is None:
                downloadfolder = os.path.dirname(os.path.abspath(__file__))
            #download(mediaurl, re.sub('\W+',' ', filename+" "+formatted_date), source, downloadfolder +
             #        os.sep + subreddit+" (New)")
            download(mediaurl, re.sub('\W+',' ', filename+" "+urlname), source, downloadfolder +
                    os.sep + subreddit)
        if nextpage is not None:
            print("\nLoading Next Page")
            url = url + '&after=' + nextpage
            connection(url,downloadfolder,subreddit)
    else:
        print(response)
#SuperModelIndia
#faptodesiactress
#BeautifulIndianWomen
#xxxycelebs
#nsfwsports
#nsfwcelebs
# Parser
subreddits = ['WomenOfColor','instaboldreels','OnlyFansSlutClub','sexyindiangirlss','indianonlyfans','BeautifulIndianWomen','faptodesiactress','MODELS_ALLNUDES','ModelsGoneMild','nsfwcelebs','nsfwsports','SuperModelIndia','xxxycelebs','2busty2hide','UrfiJaved','BrownHotties']
for i in range(len(subreddits)):
    subreddit = subreddits[i]
    sort = 'all'
    duplicatecaption = 'n'
    downloadfolder = "E:\\reddit"
    # Defining URLS
    if sort == 'all':
        allsorts = ['top','new','hot']
        url = f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=all'
        print(f'\nSubreddit: r/{subreddit} \nSort: top posts of all time')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
        time.sleep(2.5)
        url = f'https://www.reddit.com/r/{subreddit}/new.json?t=all'
        print(f'\nSubreddit: r/{subreddit} \nSort: new posts of all time')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
        time.sleep(2.5)
        url = f'https://www.reddit.com/r/{subreddit}/.json?'
        print(f'\nSubreddit: r/{subreddit} \nSort: hot posts')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
        time.sleep(2.5)
    elif sort == 'top':
        url = f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=all'
        print(f'\nSubreddit: r/{subreddit} \nSort: {sort} posts of all time')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
    elif sort == 'new':
        url = f'https://www.reddit.com/r/{subreddit}/new.json'
        print(f'\nSubreddit: r/{subreddit} \nSort: {sort} posts of all time')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
    else:
        url = f'https://www.reddit.com/r/{subreddit}/.json?'
        print(f'\nSubreddit: r/{subreddit} \nSort: {sort} posts')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
 
subreddits = ['RahilShaikhFuck']
for i in range(len(subreddits)):
    subreddit = subreddits[i]
    sort = 'all'
    duplicatecaption = 'n'
    downloadfolder = "E:\\reddit"
    # Defining URLS
    if sort == 'all':
        allsorts = ['top','new','hot']
        url = f'https://www.reddit.com/u/{subreddit}/top.json?sort=top&t=all'
        print(f'\nSubreddit: r/{subreddit} \nSort: top posts of all time')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
        time.sleep(2.5)
        url = f'https://www.reddit.com/u/{subreddit}/new.json?t=all'
        print(f'\nSubreddit: r/{subreddit} \nSort: new posts of all time')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
        time.sleep(2.5)
        url = f'https://www.reddit.com/u/{subreddit}/hot.json?'
        print(f'\nSubreddit: r/{subreddit} \nSort: hot posts')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
        time.sleep(2.5)
    elif sort == 'top':
        url = f'https://www.reddit.com/u/{subreddit}/top.json?sort=top&t=all'
        print(f'\nSubreddit: r/{subreddit} \nSort: {sort} posts of all time')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
    elif sort == 'new':
        url = f'https://www.reddit.com/u/{subreddit}/new.json'
        print(f'\nSubreddit: r/{subreddit} \nSort: {sort} posts of all time')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
    else:
        url = f'https://www.reddit.com/u/{subreddit}/.json?'
        print(f'\nSubreddit: r/{subreddit} \nSort: {sort} posts')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)