#!/usr/bin/env python3
import sqlite3
import re
from subprocess import call
call("TASKKILL /f /IM chrome.exe")
# find your 'History' file
conn = sqlite3.connect('c:/Users/LENOVO/AppData/Local/Google/Chrome/User Data/Default/History')
c = conn.cursor()

print("history length", c.execute('SELECT count(1) FROM urls').fetchone()[0])

domainPattern = re.compile(r"https?://([^/]+)/")
domains = {}

result = True
id = 0
while result:
    result = False
    ids = []

    for row in c.execute('SELECT id, url, title FROM urls WHERE id > ? LIMIT 10000000', (id,)):
        result = True
        match = domainPattern.search(row[1])
        id = row[0]

        if match:
            domain = match.group(1)
            domains[domain] = domains.get(domain, 0) + 1
            # clean if this is true
            ids.append((id,))

    c.executemany('DELETE FROM urls WHERE id=?', ids)
    conn.commit()

conn.close()

import pprint
pprint.pprint(domains)