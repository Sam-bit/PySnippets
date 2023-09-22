import os.path
import csv

csv_file = 'facts.csv'
field_names = ["ARTICLE_URL",
               "ARTICLE_DETAIL_URL",
               "ARTICLE_TITLE",
               "ARTICLE_THUMBNAIL",
               "ARTICLE_PUBLISHED_DATE",
               "ARTICLE_UPDATED_DATE",
               "ARTICLE_CLAIM",
               "ARTICLE_CLAIM_REVIEW",
               "ARTICLE_CONTENT",
               "ARTICLE_CHECKED_BY",
               "ARTICLE_VERDICT",
               "ARTICLE_ALT_VERDICT",
               "ARTICLE_SITE_ID"]


def csvColumnToList():
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='',encoding="utf-8") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(field_names)
            csvfile.close()
    filename = open(csv_file, 'r',encoding="utf-8")
    file = csv.DictReader(filename)
    fact_url = []
    for col in file:
        fact_url.append(col['ARTICLE_URL'])
    return fact_url


def csvAppendDictToCsv(dict, fact_url_list):
    if dict['ARTICLE_URL'] not in fact_url_list:
        with open(csv_file, 'a', newline='',encoding="utf-8") as f_object:
            dictwriter_object = csv.DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(dict)
            f_object.close()
