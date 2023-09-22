#!/usr/bin/python2.7
import requests
import sys
from urllib.parse import urlparse


# This will return last modified time of given web page url
def get_last_modified(url):
    result = urlparse(url)
    if True if [result.scheme, result.netloc, result.path] else False:
        header = requests.head(url).headers
        if 'Last-Modified' in header:
            return header['Last-Modified']
        print("Data is not available")
        return -1
    else:
        return -1


# Demonstration of function call
if __name__ == '__main__':
    try:
        url = 'https://iicb.res.in/recruitment'
        print(get_last_modified(url))
    except:
        print("Please provide proper url as a first argument.")
