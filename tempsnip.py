import re
with open ('input.txt', 'r' ) as f:
    content = f.read()
    content_new = re.sub('(\d{2}|[a-yA-Y]{3})\/(\d{2})\/(\d{4})', r'', content, flags = re.M)