#from facts.db import create_connection
#from facts.sync_to_cloud import push_article_to_cloud,push_sources_to_cloud
from scraper.boomlive import boomlive_fetch
from scraper.altnews import altnews_fetch
from utils.csv_utils import csvColumnToList
#from facts.boomlive import boomlive_fetch
#from facts.snopes import snopes_fetch
#from facts.thequint import thequint_fetch
#conn = create_connection()

if __name__ == '__main__':
    article_url = csvColumnToList()
    altnews_fetch(article_url)
    #boomlive_fetch(article_url)
#boomlive_fetch(conn)
#snopes_fetch(conn)
#thequint_fetch(conn)
#csv_to_json(filename)
#push_article_to_cloud(conn)
#push_sources_to_cloud(conn)