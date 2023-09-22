import re

from facts.db import insert_article, check_if_url_exists
from facts.sync_to_cloud import push_to_firebase
from facts.utils import *
_FactCheckedById = 3
def readEachArticle(url,thumbnail, conn):
    soup = getUTF8Soup(url)
    title = soup.find('h1',class_="title")
    authorname = soup.find('a',class_="author").text if soup.find('a',class_="author") is not None else soup.find('span',class_="author").text
    if 'This article has been moved here:' in soup.prettify():
        pass
    else:
        contents = soup.find('div',class_='content').find_all(['ol', 'li', 'ul', 'p', 'em', "blockquote", 'h4'],
                                   class_=lambda x: x not in ['smg-zone smg-zone-smg-post-body-1', 'smg-zone smg-zone-content-after'], recursive=False)
        textcontent = ""
        article_claim  = ''
        if soup.find('h2', class_='subtitle') is not None:
            article_claim = article_claim + soup.find('h2', class_='subtitle').text+" "
        if soup.find('div', class_='subtitle') is not None:
            article_claim = article_claim + soup.find('div', class_='claim').find('p').text
        for content in contents:
            textcontent = textcontent + content.text.replace("\xa0", "").replace('\n','')
        string = soup.prettify()
        updateddatepattern = '(?:"datePublished":")(.*?)(?:")'
        updateddatematch = re.search(updateddatepattern, string)
        updateddate = updateddatematch.group(1)
        if updateddate.startswith('-'):
            updateddatepattern = '(?:"dateModified":")(.*?)(?:")'
            updateddatematch = re.search(updateddatepattern, string)
            updateddate = updateddatematch.group(1)
        verdictpattern = '(?:"alternateName":")(.*?)(?:")'
        verdictmatch = re.search(verdictpattern, string)
        if url == 'https://www.snopes.com/fact-check/anti-trump-protesters-block-ambulance/':
            updateddate = "2016-11-15T00:00:00+00:00"
        if url == 'https://www.snopes.com/fact-check/obama-signs-executive-order-declaring-investigation-into-election-results/':
            updateddate = "2016-12-18T00:44:07+00:00"
        fact_verdict = ''
        if soup.find('div', class_='claim-review-block') is not None:
            fact_verdict = soup.find('div', class_='claim-review-block').find_all('span', class_='value')[-1].text
        if soup.find('h5', class_=lambda value: value and value.startswith("rating-label")) is not None:
            fact_verdict = soup.find('h5',class_=lambda value: value and value.startswith("rating-label")).text
        if verdictmatch:
            fact_verdict = verdictmatch.group(1)
        textcontent = textcontent + soup.find('div',class_='content').text.replace('\n', ' ').replace('\t', ' ')
        textcontent = " ".join(textcontent.split())
        head,sep,tail = textcontent.partition(' Snopes.com Since 1994')
        if article_claim.strip()=='':
            article_claim = soup.find("meta", property="og:description")["content"]
        article = (unicodetoascii(url),
                   unicodetoascii(title.text),
                   thumbnail,
                   format_date(updateddate[0:19], "%Y-%m-%dT%H:%M:%S"),
                   unicodetoascii(" ".join(article_claim.split())),
                   unicodetoascii(head),
                   unicodetoascii(authorname),
                   fact_verdict,
                   'False' if any(x in title.text.lower() for x in (
                       'no', 'false', 'did not', 'didn\'t', 'fake', 'old ', 'old,', 'cannot', 'can\'t', 'photoshop', 'hoax',
                       'misreport', 'mis-report', 'misquote', 'mislead', 'fox', 'plagiarise', 'shared as', 'doesnt',
                       'doesn\'t', 'shared with','wrong')) == True and fact_verdict == '' else '',
                   _FactCheckedById
                   )
        # print(article)
        insert_article(conn,article)
        #push_to_firebase(conn, url)

def snopes_fetch(conn):
    i = 1
    while True:
        url = 'https://www.snopes.com/fact-check/page/%d/'% i
        print(url)
        soup = getUTF8Soup(url)
        if not soup.find('article'):
            break
        else:
            for article in soup.find_all('article',class_ ="media-wrapper"):
                record_found = check_if_url_exists(conn,article.find('a')['href'])
                if not record_found:
                    thumbnail = imageurl_to_base64(
                        article.find('figure', class_='featured-media').find('img').attrs.get('data-lazy-src'))
                    readEachArticle(article.find('a')['href'],thumbnail, conn)
                else:
                    return
        i = i + 1
