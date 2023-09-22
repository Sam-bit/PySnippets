import re

from facts.db import insert_article, check_if_url_exists
from facts.sync_to_cloud import push_to_firebase
from facts.utils import *
_FactCheckedById = 4

def readEachArticle(url,conn):
#def readEachArticle(url):
    soup = getUTF8Soup(url)
    string = soup.prettify()
    thumbnail = re.search('(?:"image":")(.*?)(?:")', string).group(1)
    publishedtime = re.search('(?:"datePublished":")(.*?)(?:")', string).group(1)
    title = re.search('(?:"headline":")(.*?)(?:")', string).group(1)
    articleclaim = re.search('(?:"articleBody":")(.*?)(?:")', string).group(1)
    textcontent = re.findall( '(?:"text":")(.*?)(?:")',string)
    article = (unicodetoascii(url),
                   unicodetoascii(title),
                   thumbnail,
                   format_date(publishedtime[0:19], "%Y-%m-%dT%H:%M:%S"),
                   unicodetoascii(articleclaim),
                   #unicodetoascii(textcontent),
                   #unicodetoascii(authorname),
                   #fact_verdict,
                   # 'False' if any(x in title.text.lower() for x in (
                   # 'no', 'false', 'did not', 'didn\'t', 'fake', 'old ', 'old,', 'cannot', 'can\'t', 'photoshop', 'hoax',
                   # 'misreport', 'mis-report', 'misquote', 'mislead', 'fox', 'plagiarise', 'shared as', 'doesnt',
                   # 'doesn\'t', 'shared with','wrong')) == True and fact_verdict == '' else '',
                   _FactCheckedById
                   )
    print(article)
        #insert_article(conn, article)
        #push_to_firebase(conn, url)
#readEachArticle('https://www.boomlive.in/fake-news/photos-of-mould-on-leather-goods-in-malaysian-store-viral-as-india-8072')
def thequint_fetch(conn):
    i = 1
    while True:
        url = 'https://www.thequint.com/news/webqoof/%d'% i
        print(url)
        soup = getUTF8Soup(url)
        if not soup.find('div',class_ = 'story-card-small col-small ctg-news'):
            break
        else:
            allurlslist = re.findall( r'(?:"url":"https://www.thequint.com/news/webqoof/)(.*?)(?:")', soup.prettify())
            print(allurlslist)
            for article in soup.find_all('div',class_='card-elements story-card-block ctg-news'):
                article_url = urllib.parse.urljoin(base_url(url), article.find('a',class_='card-elements__link device-hide')['href'])
                print(article_url)
                record_found = check_if_url_exists(conn, article_url)
                if not record_found:
                    readEachArticle(article_url, conn)

        i = i + 1