import re
from FactOrNot.utils.utils import *
_FactCheckedById = 2

def readEachArticle(url,thumbnail,title,facts_url_list):
#def readEachArticle(url):
    soup = getUTF8Soup(url)
    if soup.find("div",class_ = "bg-404") is not None:
        return
    elif not soup.find('div',class_ = 'row short-factcheck-snippet'):
        if title is None or title == '':
            title = soup.find('h1',class_="entry-title title is-size-2-touch is-2 article-title is-custom-title")
        detail_url=soup.find("div",class_="cta").find("a")['href']
        authorname = soup.find('a',class_=lambda value: value and value.startswith("author-link")).text if soup.find('a',class_=lambda value: value and value.startswith("author-link")) is not None else 'BoomLive Staff'
        fact_verdict = ''
        article_claim = soup.find("meta", property="og:description")["content"]
        # tag = soup.find('div', class_='story')
        # for content in tag.findAll('p'):
        #     textcontent = textcontent + (" ".join(content.strings)).replace('\n', ' ').replace('\t', ' ') + " "
        #updateddate = soup.find('span',class_="convert-to-localtime").attrs.get('data-datestring')
        published_time = soup.find("meta", property="article:published_time")["content"][0:19]
        if soup.find('div', class_='claim-review-block') is not None:
            fact_verdict = soup.find('div', class_='claim-review-block').find_all('span', class_='value')[-1].text
            #article_claim = soup.find('div', class_='claim-review-block').find_all('span', class_='value')[0].text.replace('\n', ' ').replace('\t', '')
        # textcontent = textcontent + tag.text.replace('\n', ' ').replace('\t', ' ')
        string = soup.prettify()
        bodypattern = '(?:"articleBody" : ")(.*?)(?:")'
        bodymatch = re.search(bodypattern, string)
        if bodymatch:
            textcontent = " ".join(re.sub("<.*?>", "", bodymatch.group(1)).replace('\n', ' ').replace('\t', '').split())
        else:
            textcontent = ''
        verdictpattern = '(?:"alternateName" : ")(.*?)(?:")'
        verdictmatch = re.search(verdictpattern, string)
        if verdictmatch and fact_verdict == '':
            fact_verdict = verdictmatch.group(1)
        article = {"ARTICLE_URL": unicodetoascii(url),
                   "ARTICLE_DETAIL_URL": unicodetoascii(detail_url),
                   "ARTICLE_TITLE": unicodetoascii(title),
                   "ARTICLE_THUMBNAIL": thumbnail,
                   "ARTICLE_PUBLISHED_DATE": format_date(published_time, "%Y-%m-%dT%H:%M:%S"),
                   #"ARTICLE_UPDATED_DATE": format_date(modified_time, "%Y-%m-%dT%H:%M:%S"),
                   "ARTICLE_CLAIM": unicodetoascii(article_claim),
                   #"ARTICLE_CLAIM_REVIEW": unicodetoascii(claim_review),
                   "ARTICLE_CONTENT": unicodetoascii(textcontent),
                   "ARTICLE_CHECKED_BY": unicodetoascii(authorname),
                   "ARTICLE_VERDICT": fact_verdict,
                   "ARTICLE_ALT_VERDICT": 'False' if any(x in title.lower() for x in (
                       'no', 'false', 'did not', 'didn\'t', 'fake', 'old ', 'old,', 'cannot', 'can\'t', 'photoshop',
                       'hoax',
                       'misreport', 'mis-report', 'misquote', 'mislead', 'fox', 'plagiarise', 'shared as', 'doesnt',
                       'doesn\'t', 'shared with', 'wrong', 'unrelated', 'baseless')) == True else '',
                   "ARTICLE_SITE_ID": _FactCheckedById
                   }
        print(article)
#        insert_article(conn, article)
        #push_to_firebase(conn, url)
#readEachArticle('https://www.boomlive.in/fake-news/photos-of-mould-on-leather-goods-in-malaysian-store-viral-as-india-8072')
def boomlive_fetch(facts_url_list):
    i = 1
    while True:
        urlfast = 'https://www.boomlive.in/fast-check/%d'% i
        urlfact= 'https://www.boomlive.in/fact-check/%d'% i
        print(urlfast)
        soupfast = getUTF8Soup(urlfast)
        if not soupfast.find('div',id = 'post-404'):
            for article in soupfast.find('div',class_='row item-data').find_all('div',recursive=False):
                article_url = urllib.parse.urljoin(base_url(urlfast), article.find('a',class_='img_link')['href'])
                if article_url not in facts_url_list:
                    thumbnail = article.find('a',class_='img_link').find('img')['data-src']
                    article_title =  article.find('h4').text
                    readEachArticle(article_url,
                                    thumbnail,
                                    article_title,
                                    facts_url_list)
                else:
                    return
        else:
            break
        soupfact = getUTF8Soup(urlfact)
        if not soupfact.find('div', id='post-404'):
            for article in soupfact.find('div', class_='row item-data').find_all('div', recursive=False):
                article_url = urllib.parse.urljoin(base_url(urlfact), article.find('a', class_='img_link')['href'])
                if article_url not in facts_url_list:
                    thumbnail = article.find('a', class_='img_link').find('img')['data-src']
                    article_title = article.find('h4').text
                    readEachArticle(article_url,
                                    thumbnail,
                                    article_title,
                                    facts_url_list)
                else:
                    return
        else:
            break
        i = i + 1