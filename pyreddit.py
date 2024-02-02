import argparse
import requests
import os,re,sys
import time
from urllib.request import urlretrieve
from pathlib import Path
from codecutils import decodestring

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
# Parser
# subreddits = ['malluhorny' , 'IndianHotModels' , 'eHh4bnNmd2dpZnM=' , 'U3VubnlMZW9uZQ==' , 'Ym9uZ2JlYXV0eQ==' ,
#               'Qm9uZ0N1Y2tvbGQ=' , 'SW5kaWFuUG9ybg==' , 'TWFrZU1lRmVlbEdvb2Q=' , 'Q2hlbm5haUdX' ,
#               'eW91dHViZXRpdHRpZXM=' , 'SW5kaWFSZXlub2xkc18=' , 'QmlnZ2VyVGhhbllvdVRob3VnaHQ=' ,
#               'c25hcGNoYXRfaW5kaWE=' , 'aW5zdGFnaXJsc2NsdWI=' , 'SW5kaWFuTnVkZUV4Y2hhbmdl' , 'V29tZW5PZkNvbG9y' ,
#               'SW5kaWFuX3Bvcm5kb2U=' , 'cG9tbWVsaW5ldGlsbGllcmVfT0Y=' , 'TnVkZUluZGlhbkNlbGVicw==' ,
#               'U2hlTGlrZXNJdFJvdWdo' , 'U21hbGxDdXRpZQ==' , 'cmVzbWlybmFpcg==' , 'VHdlbnR5UGx1cw==' ,
#               'SW5kaWFuQ2VsZWJTY2VuZXM=' , 'SG90SW5kaWFuR2lybHNY' , 'VGl0c0FuZEJvbmdSaXBz' , 'RGVzaUNlbGViTWlsZnM=' ,
#               'cGFja3NEYW5h' , 'SW5kaWFuX0JoYWJoaV9sb3ZlcnM=' , 'TmVwYWxpQ2VsZWJyaXR5' , 'QnJvd25Ib3R0aWVz' ,
#               'U2hyZW51UGFyaWtoSG90' , 'R2lybHNKb3k=' , 'aW5kaWFuc2V4c3RvcmllczI=' , 'TWFsYWlrYUFyb3JhRmFwcGVycw==' ,
#               'SW5kaWFuQ2VsZWJJbWFnZXM=' , 'QmFuZ2xhZGVzaEdvbmVTZXh5' , 'SW5kaWFuT1RUYmVzdG9m' ,
#               'SW50ZXJlc3RpbmdTdWJzSW5kaWE=' , 'SG90dGllc09mVFZhbmRZVA==' , 'TWFsbHVJbmRpYW5QaWVGYW5z' ,
#               'TnVkZUluZGlhbldvbWVu' , 'bmlwc2xpcF8=' , 'UHVzc3lfUGVyZmVjdGlvbg==' , 'R09PTkVE' ,
#               'SW5kaWFuUmVlbHNHb25lTWlsZA==' , 'aW5kaWFueXRmZWV0' , 'bnVkZV9JbmRpYW5fZ2lybHM=' , 'Ym9uZ3JpcHM=' ,
#               'cmVlbHNnb25ld2lsZA==' , 'VXJmaUphdmVk' , 'Ym9sbHl3b29kbnNmdw==' , 'SW5kaWFuQWN0cmVzc1Bob3Rvcw==' ,
#               'SW5kaWFuWG51ZGVfUGhvdG9z' , 'Z29uZXdpbGQ=' , 'YnJlYXN0c3Vja2luZw==' , 'QmVuZ2FsaUNsaXBz' ,
#               'ZG93bmJsb3VzZUluZGlh' , 'SW5kaWFuQWN0cmVzc2VzUGljcw==' , 'SW5kaWFuQmFiZXNHVw==' , 'QmFuZ2Fsb3JlR1c=' ,
#               'SW5kaWFuQWN0cmVzc0h1Yg==' , 'VXBza2lydA==' , 'TU9ERUxTX0FMTE5VREVT' , 'U2FyYWlHYW1ib2FPRg==' ,
#               'SW5kaWFuSW5zdGFjZWxlYg==' , 'ZG93bmJsb3VzZQ==' , 'SW5kaWFuU2V4U2NlbmU=' ,
#               'cGFraXN0YW5jdWNrb2xkY2x1Yg==' , 'VW5yYXRlZFBhbmRh' , 'RG93bmJsb3VzZV9iYWJlcw==' , 'MmJ1c3R5MmhpZGU=' ,
#               'RGlhbW9uZEphY2tzb24=' , 'SW5kaWFuY291cGxlZmFudGFjaWVz' , 'c21hbGxib29icw==' , 'Qm9uZ0dvbmVXcm9uZw==' ,
#               'SW5kaWFuV2lsZEdpcmxz' , 'TWFrZUZyaWVuZHNJbkluZGlh' , 'SW5kaWFuTmV3c0JpYXM=' ,
#               'Ym9sbHl3b29kX2JoYWJoaXM=' , 'TG9yZF9vZl9Cb29icw==' , 'TW9kZWxzR29uZU1pbGQ=' , 'aW5kaWFuZ29vbmh1Yg==' ,
#               'UHJlc2VudGluZ051ZGVOU0ZX' , 'TWFsYWlrYUFyb3JhSG90' , 'UmFzaG1pa2FNYW5kYW5uYUhvdA==' ,
#               'ZGVzaWhvcm55YmhhYmhp' , 'QmVhdXRpZnVsSW5kaWFuV29tZW4=' , 'VGFtaWxHVw==' , 'TnVkZUNlbGVic09ubHk=' ,
#               'ZGF0YXNldHM=' , 'aW5kaWFuX2V4aGliaXRpb25pc20=' , 'aW5zdGFib2xkcmVlbHM=' ,
#               'SW5kaWFuQWN0cmVzc0ZhY2VQaWNz' , 'YmFuZ2xhX2N1Y2tvbGQ=' , 'S2VyYWxhR1c=' ,
#               'SW5kaWFuT25seWZhbnNHaXJscw==' , 'c2VnaGVzdWFtaWNoZXR0ZQ==' , 'TmlkaGlfQ19Mb3ZlcnM=' ,
#               'U2V4eV9Bc2lhbnM=' , 'dHJlZXNnb25ld2lsZA==' , 'dWtob3RtYWxheWFsZWU=' , 'Ym9uZ21pbGY=' ,
#               'VGlrVGhvdEJhYmVz' , 'dGhpZ2h6b25l' , 'U2hhZ09uSG90dGllcw==' , 'aW5kaWFsZXNiaWFu' , 'aGFwcHljdWNrb2xk' ,
#               'aW5kaWFuc2F1Y2VmaW5kZXI=' , 'VUtTbHV0c2FuZExhZHM=' , 'bmlwc2xpcF9f' , 'VGlmZmFueVRhdHVt' ,
#               'bWl4bWFzYWxhYQ==' , 'c2xvcHB5c29sbw==' , 'UGFzc2lvbmF0ZUdpcmxz' , 'TWFsbHVjaGlja3M=' ,
#               'QmloYXJIb29rVXBz' , 'R2lybHNHVw==' , 'T25seWZhbnNfX0hvdEJhYmVz' , 'YWxsbnVkZXRoaW5nc19pbmRpYW4=' ,
#               'TlNGV19OZXQ=' , 'ZGFuc2tlY2VsZXBzb2NrcGlja3M=' , 'Ym9uZ3NuYnV0dHM=' , 'aW5kaWFuc2dvbmVudWRl' ,
#               'bnNmd2NlbGVicw==' , 'Qm9sbHl3b29kU3Rvcmllcw==' , 'SW5kaWFuaW5zdGFncmFt' , 'SW5kaWFuQWN0cmVzc2VzSG90' ,
#               'aW5kaWFuZ3Jhbm5pZXM=' , 'Qm9sbHl3b29kTWlsZnNIdWI=' , 'SW5kaWFzZXhjb25mZXNzaW9ucw==' ,
#               'cmVzbWluYWlyXw==' , 'U3VwZXJNb2RlbEluZGlh' , 'QmVhdXR5b2ZQYWtpc3Rhbg==' , 'aXdhbnR0b2JlaGVy' ,
#               'SW5kaWFuZ2Zz' , 'anVsaWFhX2JheW9uZXR0YQ==' , 'Qm9uZ29naXJs' , 'Ym9uZ3NpbmRlbGhp' ,
#               'QXNpYW5BbWF0ZXVyUG9ybg==' , 'aW5kaWFucG9ybmNsaXBzcw==' , 'aW5kaWFuaG90Y2VsZWI=' , 'UGV0aXRlVGl0cw==' ,
#               'U2hyYWRkaGFfS2Fwb29yX0N1bQ==' , 'VGlrdG9rU2NhbW1lcnNCZWdnYXJ6' , 'cHV0aWNsdWI=' ,
#               'UG9vbmFtUGFuZGV5RmFuYXRpY3M=' , 'Ym9vYnNpbmRpYW4=' , 'QmlnQm9vYnNHVw==' , 'QmxlYWNoZWRJbmRpYW5zTkVX' ,
#               'YmlmZW1hbGVzX29mX1Bha2lzdGFu' , 'bWFsbHVyZXNtaQ==' , 'QWN0cmVzc191aGQ=' , 'UGVyZmVjdEJvZHk=' ,
#               'U2V4eWluZGlh' , 'TmVwYWxpRmVtYm9pcw==' , 'aG90dGFtaWxjZWxlYnM=' , 'ZmFwdG9kZXNpYWN0cmVzcw==' ,
#               'QXNpYW5XZWJjYW1HaXJscw==' , 'TnVkZV9TZWxmaWU=' , 'VmlyZ2luaXR5Xw==' , 'Q2h1YmJ5R2lybFRpa3Rva3M=' ,
#               'aW5kaWFub25seWZhbnM=' , 'TWlha2hhbGlmYQ==' , 'QmFuZ2xhZGVzaDY5c2V4' , 'Ym9uZ19ib3Vkb2ly' ,
#               'VGlrVG9rU2VlVGhyb3VnaA==' , 'QWxpY2VCb25n' , 'RmFwVG9EZXNp' , 'NDIwX0dpcmxz' , 'aG9va3VwX2NsdWI=' ,
#               'c2V4eWRlc2k=' , 'SW5kaWFuX3JhYW5kX2xvdmVycw==' , 'Ym9sbHlhcm0=' , 'TWFsbHVCYWJlcw==' ,
#               'QnJhY2VzTlNGVw==' , 'cHV0aXRhc19zbHV0d2Vhcg==' , 'TWFsZVN1cGVyaW9yaXR5' , 'VGFuZ29fbGl2ZXM=' ,
#               'aW5kaWFubmlwcGxlcw==' , 'VmluZGljdGE=' , 'bnNmd3Nwb3J0cw==' , 'ZGVzaV9xdWVlbnM=' ,
#               'SW5kaWFuQWN0cmVzc1Npbmdlcg==' , 'TnVkZU5vbk51ZGU=' , 'SW5kaWFuX0FjdHJlc3Nlc19QaWNz' ,
#               'dG9wbGVzc2luc3dlYXRwYW50cw==' , 'aHVnZWJvb2Jz' , 'SW5kaWFubW9kZWxzbnVkZQ==' , 'SW5kaWFuaG90dGllc18=' ,
#               'VGlrVG9rQXNpYW5Ib3R0aWVz' , 'TWFrZU1lRmVlbEdvb2RNYWxhaWthQXJvcmFGYXBwZXJz' , 'T25seUZhbnMxMDE=' ,
#               'UGFraXN0YW5pSG9va3Vwcw==' , 'aW5kaWFubGFkaWVzeA==' , 'dGl0c19mb3JfdHdlYWtlcnM=' ,
#               'UHJpdmF0ZV9Db2xsZWN0aW9u' , 'V3Jlc3RsZUZhcA==' , 'RXJvdGljRW50ZXJ0YWlubWVudA==' , 'bWZsYg==' ,
#               'c2V4eWluZGlhbmdpcmxzcw==' , 'VGlrVG9rb25seWZhbnMx' , 'SW5kaWFuX0NlbGVi' , 'Qm9sbHl3b29kVUhRb25seQ==' ,
#               'U2FyZWVWc0Jpa2luaQ==' , 'YmhhZGJoYWJpZV9jYW0=' , 'RGFuaURhbmllbHM=' , 'UGlja29uZXBvcm5zdGFy' ,
#               'bGl6enp5c21vb3RoZ29vZGllcw==' , 'Ym9vYnM=' , 'VG9sbHl3b29kQ2VsZWJyaXRpZXM=' , 'aW5kaWFuZmVldA==' ,
#               'SW5kaWFuR2lybFNtb2tpbmc=' , 'Qm9uZ2FDYW1zTWVkaWE=' , 'Ym9uZ3NfYmFiZXM=' , 'SW5kaWFuR2xhbW91ckdpcmxz' ,
#               'QXZlcmFnZUdpcmxOdWRl' , 'SW5kaWFuSnVpY3lHaXJscw==' , 'Qm9uZ2FjYW1zX0dpcmxz' , 'SW5kaWFuR2lybHNHVw==' ,
#               'TXVtYmFpQ3Vja29sZHNz' , 'RmFjaWFsZXhwcmVzc2lvbg==' , 'SW5kaWFuRWRpdHNOU0ZX' , 'RGVzaTR5b3U=' ,
#               'Q2FtR2lybHM=']
subreddits = [
    #'Tm9yYUZhdGVoaV9GQw=='
]
subreddits.reverse()
for i in range(len(subreddits)):
    subreddit = decodestring(subreddits[i])
    sort = 'all'
    duplicatecaption = 'n'
    downloadfolder = "E:\\FlutterProjects\\qr_gif_codec\\example\\android\\app\\src\\main\\res\\values\\REDDIT"
    # Defining URLS
    if sort == 'all':
        allsorts = ['new','top','hot']
        url = f'https://www.reddit.com/r/{subreddit}/new.json?t=all'
        print(f'\nSubreddit: r/{subreddit} \nSort: new posts of all time')
        time.sleep(2.5)
        connection(url,downloadfolder,subreddit)
        time.sleep(2.5)
        url = f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=all'
        print(f'\nSubreddit: r/{subreddit} \nSort: top posts of all time')
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
#
# subreddits = ['UmFoaWxTaGFpa2hGdWNr', 'c2hlcmxvY2tfYXRocmV5YQ==', 'QmxhY2tTaW5uZXJXb3JsZA==', 'RWR1Y2F0aW9uYWxfU2NoZW1lNjM=', 'RGVzaWZpbGU=']
# for i in range(len(subreddits)):
#     subreddit = decodestring(subreddits[i])
#     sort = 'all'
#     duplicatecaption = 'n'
#     downloadfolder = "E:\\reddit"
#     # Defining URLS
#     if sort == 'all':
#         allsorts = ['new','top','hot']
#         url = f'https://www.reddit.com/u/{subreddit}/new.json?t=all'
#         print(f'\nSubreddit: r/{subreddit} \nSort: new posts of all time')
#         time.sleep(2.5)
#         connection(url,downloadfolder,subreddit)
#         time.sleep(2.5)
#         url = f'https://www.reddit.com/u/{subreddit}/top.json?sort=top&t=all'
#         print(f'\nSubreddit: r/{subreddit} \nSort: top posts of all time')
#         time.sleep(2.5)
#         connection(url,downloadfolder,subreddit)
#         time.sleep(2.5)
#         url = f'https://www.reddit.com/u/{subreddit}/hot.json?'
#         print(f'\nSubreddit: r/{subreddit} \nSort: hot posts')
#         time.sleep(2.5)
#         connection(url,downloadfolder,subreddit)
#         time.sleep(2.5)
#     elif sort == 'top':
#         url = f'https://www.reddit.com/u/{subreddit}/top.json?sort=top&t=all'
#         print(f'\nSubreddit: r/{subreddit} \nSort: {sort} posts of all time')
#         time.sleep(2.5)
#         connection(url,downloadfolder,subreddit)
#     elif sort == 'new':
#         url = f'https://www.reddit.com/u/{subreddit}/new.json'
#         print(f'\nSubreddit: r/{subreddit} \nSort: {sort} posts of all time')
#         time.sleep(2.5)
#         connection(url,downloadfolder,subreddit)
#     else:
#         url = f'https://www.reddit.com/u/{subreddit}/.json?'
#         print(f'\nSubreddit: r/{subreddit} \nSort: {sort} posts')
#         time.sleep(2.5)
#         connection(url,downloadfolder,subreddit)