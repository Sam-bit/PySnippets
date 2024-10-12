import os
import sys
import urllib
from datetime import datetime,timedelta,time
import bs4
import requests
def imageurl_to_base64(url):
    #return base64.b64encode(requests.get(url).content).decode()
    return url

def base_url(url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')
    return parsed.geturl()
def getUTF8Soup(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup
def unicodetoascii(text):
    TEXT = (text.
    		replace('\\xe2\\x80\\x99', "'").
            replace('\\xc3\\xa9', 'e').
            replace('\\xe2\\x80\\x90', '-').
            replace('\\xe2\\x80\\x91', '-').
            replace('\\xe2\\x80\\x92', '-').
            replace('\\xe2\\x80\\x93', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x98', "'").
            replace('\\xe2\\x80\\x9b', "'").
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9d', '"').
            replace('\\xe2\\x80\\x9e', '"').
            replace('\\xe2\\x80\\x9f', '"').
            replace('\\xe2\\x80\\xa6', '...').
            replace('\\xe2\\x80\\xb2', "'").
            replace('\\xe2\\x80\\xb3', "'").
            replace('\\xe2\\x80\\xb4', "'").
            replace('\\xe2\\x80\\xb5', "'").
            replace('\\xe2\\x80\\xb6', "'").
            replace('\\xe2\\x80\\xb7', "'").
            replace('\\xe2\\x81\\xba', "+").
            replace('\\xe2\\x81\\xbb', "-").
            replace('\\xe2\\x81\\xbc', "=").
            replace('\\xe2\\x81\\xbd', "(").
            replace('\\xe2\\x81\\xbe', ")").
            replace('\xa0', "")
                 )
    return TEXT

def format_date(from_date,from_format):
    return datetime.strptime(from_date,from_format).strftime('%Y-%m-%d %H:%M:%S')

def download_file_with_progress(url,filename=None,proxies = None,headers = None,skip_above_mb = None,verbose = False,filename_prefix = '',filename_postfix = ''):
    if url is None or url == '':
        return
    if filename is None:
        filename = os.path.basename(url)
    if filename_prefix != "":
        filename = filename_prefix + filename
    if filename_postfix != "":
        name, ext = os.path.splitext(filename)
        filename = f"{name}{filename_postfix}{ext}"
    with open(filename,"wb") as f:
        if verbose:
            print(f"Input URL       : {url}")
            print(f"Output FileName : {filename}")
        try:
            response = requests.get(url,stream=True,proxies=proxies,headers=headers)
            total_length = response.headers.get('content-length')
            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                file_size_kb = total_length / 1024
                file_size_mb = file_size_kb / 1024
                try:
                    filesize_kb = os.path.getsize(filename)/1024
                except:
                    filesize_kb = 0
                if (skip_above_mb is not None and file_size_mb > skip_above_mb) or filesize_kb == file_size_kb:
                    pass
                else:
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(50 * dl / total_length)
                        sys.stdout.write("\r[%s%s] %.2f MB"%('='*done,' '*(50-done),file_size_mb))
                        sys.stdout.flush()
                    sys.stdout.write("\n")
        except:
            pass

def inputbox(prompt, title=None, default=None):
    try:
        import easygui_qt
    except ImportError:
        os.system("pip install easygui_qt")
    return easygui_qt.get_string(prompt,title,default)
