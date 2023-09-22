from datetime import datetime
import json
import requests
from langdetect import detect
from firebase import firebase
API_GETALLARTICLEURLS = 'http://localhost//api//getallarticleurls.php'
API_MAXDATE = "http://localhost//api//getmaxdate.php"
API_ARTICLE_ENDPOINT = "http://localhost//api//pusharticle.php"
API_SOURCES_ENDPOINT = "http://localhost//api//pushsource.php"
FBConn = firebase.FirebaseApplication('https://whatsthefact-2a4c1.firebaseio.com/',None)

def push_to_firebase(conn,article_url):
    cur = conn.cursor()
    cur.execute('SELECT * FROM articles where article_url = "%s" order by article_date desc',article_url)
    rows = cur.fetchall()
    for row in rows:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        row_article_url = row[0]
        row_article_title = row[1]
        row_article_thumbnail = row[2]
        row_article_date = row[3]
        row_article_subtitle = row[4]
        row_article_content = row[5]
        row_article_checked_by = row[6]
        row_article_verdict = row[7]
        row_article_alt_verdict = row[8]
        row_article_site_id = row[9]
        row_article_sync_date = now
        data = {
            'article_url': row_article_url,
            'article_title': row_article_title,
            'article_thumbnail': row_article_thumbnail,
            'article_date': row_article_date,
            'article_subtitle': row_article_subtitle,
            'article_content': row_article_content,
            'article_checked_by': row_article_checked_by,
            'article_verdict': row_article_verdict,
            'article_alt_verdict': row_article_alt_verdict,
            'article_site_id': row_article_site_id,
            'article_sync_date': row_article_sync_date
        }
        print('pushing ' + str(row_article_url))
def push_article_to_firebase(conn):
    cur = conn.cursor()
    # cur.execute('SELECT * FROM articles where article_date > "%s" order by article_date' % maxdate)
    cur.execute('SELECT * FROM articles order by article_date desc')
    rows = cur.fetchall()
    for row in rows:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        row_article_url = row[0]
        row_article_title = row[1]
        row_article_thumbnail = row[2]
        row_article_date = row[3]
        row_article_subtitle = row[4]
        row_article_content = row[5]
        row_article_checked_by = row[6]
        row_article_verdict = row[7]
        row_article_alt_verdict = row[8]
        row_article_site_id = row[9]
        row_article_sync_date = now
        data = {
            'article_url': row_article_url,
            'article_title': row_article_title,
            'article_thumbnail': row_article_thumbnail,
            'article_date': row_article_date,
            'article_subtitle': row_article_subtitle,
            'article_content': row_article_content,
            'article_checked_by': row_article_checked_by,
            'article_verdict': row_article_verdict,
            'article_alt_verdict': row_article_alt_verdict,
            'article_site_id': row_article_site_id,
            'article_sync_date': row_article_sync_date
        }
        print('pushing ' + str(row_article_url))
        FBConn.post('/articles/',data)
def push_article_to_cloud(conn):
    cur = conn.cursor()
    from langdetect import DetectorFactory
    DetectorFactory.seed = 0
    cur.execute('SELECT * FROM articles WHERE article_is_pushed is NULL order by article_date')
    #cur.execute('SELECT * FROM articles order by article_date desc')
    rows = cur.fetchall()
    for row in rows:
        row_article_url = row[0]
        row_article_title = row[1]
        row_article_thumbnail = row[2]
        row_article_date = row[3]
        row_article_subtitle = row[4]
        row_article_content = row[5]
        row_article_checked_by = row[6]
        row_article_verdict = row[7]
        row_article_alt_verdict = row[8]
        row_article_site_id = row[9]
        data = {
                'insert_option' : 'INSERT',
                'push_article_url' : row_article_url,
                'push_article_title' : row_article_title,
                'push_article_thumbnail' : row_article_thumbnail,
                'push_article_date' : row_article_date,
                'push_article_subtitle' : row_article_subtitle,
                'push_article_content' : row_article_content,
                'push_article_checked_by' : row_article_checked_by,
                'push_article_verdict' : row_article_verdict,
                'push_article_alt_verdict' : row_article_alt_verdict,
                'push_article_site_id' : row_article_site_id,
                'push_article_is_pushed' : 1
                }

        conn.execute("""UPDATE articles SET article_alt_verdict = :alt WHERE article_url = :url;""" , {"alt":
            'False' if any(x in row_article_title.lower() for x in (
                'no', 'false', 'did not', 'didn\'t', 'fake', 'old ', 'old,', 'cannot', 'can\'t', 'photoshop', 'hoax',
                'misreport', 'mis-report', 'misquote', 'mislead', 'fox', 'plagiarise', 'shared as', 'doesnt',
                'doesn\'t', 'shared with', 'wrong', 'unrelated')) == True and row_article_verdict in (
                           'Lost Legend',
                           'Research In Progress',
                           'Miscaptioned',
                           'Mostly False',
                           'Unproven',
                           'FALSE, SATIRE',
                           'SATIRE',
                           'FASLE',
                           'MISLEADING',
                           'Unknown',
                           'Outdated',
                           'Misattributed',
                           'Scam',
                           'Legend',
                           'Misleading',
                           'Labeled Satire',
                           'Hard to Categorise') else '', "url":row_article_url})

        conn.execute("""UPDATE articles SET article_language = :lang WHERE article_url = :url;""" , {"lang":
        detect(row_article_title + row_article_subtitle) if (row_article_title + row_article_subtitle).strip() != '' else '',
        "url":row_article_url})
        print('pushing ' + str(row_article_url))
        r = requests.post(url=API_ARTICLE_ENDPOINT, data=data)
        conn.execute("""UPDATE articles SET article_is_pushed = 1 WHERE article_url = :url;""" , {"url":row_article_url})
        conn.commit()
def push_sources_to_cloud(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM sources')
    rows = cur.fetchall()
    for row in rows:
        row_src_id = row[0]
        row_src_name = row[1]
        row_src_alt_name = row[2]
        row_src_logo = row[3]
        row_src_is_ifcn_approved = row[4]
        row_src_address = row[5]
        row_src_is_active = row[6]
        row_src_country = row[7]
        row_src_supported_by = row[8]
        row_src_language = row[9]
        row_src_added_date = row[10]
        data = {
            'push_src_id': row_src_id,
            'push_src_name': row_src_name,
            'push_src_alt_name': row_src_alt_name,
            'push_src_logo': row_src_logo,
            'push_src_is_ifcn_approved': row_src_is_ifcn_approved,
            'push_src_address': row_src_address,
            'push_src_is_active': row_src_is_active,
            'push_src_country': row_src_country,
            'push_src_supported_by': row_src_supported_by,
            'push_src_language': row_src_language,
            'push_src_added_date': row_src_added_date
        }
        print('pushing ' + str(row_src_address))
        r = requests.post(url=API_SOURCES_ENDPOINT, data=data)
