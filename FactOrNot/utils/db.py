import sqlite3

database = r"facts.db"
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn
def create_table():
    conn = create_connection()
    sql_create_articles_table = """
    CREATE TABLE "articles" (
	"article_url"	TEXT NOT NULL,
	"article_title"	TEXT NOT NULL,
	"article_thumbnail"	TEXT,
	"article_date"	TEXT,
	"article_subtitle"	TEXT,
	"article_content"	TEXT NOT NULL,
	"article_checked_by"	TEXT,
	"article_verdict"	TEXT,
	"article_alt_verdict" TEXT,
	"article_site_id"	INTEGER,
	"article_sync_date"	date
)
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_articles_table)
    except sqlite3.Error as e:
        print(e)
def insert_article(conn,article):
    sql = '''INSERT INTO articles(article_url,article_title,article_thumbnail,article_date,article_subtitle,article_content,article_checked_by,article_verdict,article_alt_verdict,article_site_id)
            VALUES(?,?,?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,article)
    conn.commit()
    print(article)
    return cur.lastrowid

def check_if_url_exists(conn,url):
    cur = conn.cursor()
    cur.execute("SELECT rowid FROM articles WHERE article_url = ?",(url,))
    data = cur.fetchall()
    if len(data) == 0:
        return False
    return True

def count_rows(conn):
    cur = conn.cursor()
    cur.execute("SELECT seq FROM sqlite_sequence")
    return cur.fetchone()