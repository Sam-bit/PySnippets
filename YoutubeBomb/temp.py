
'''import csv

txt_file = r"E:\PySnippets\YoutubeBomb\first_names.all.csv"
csv_file = r"E:\PySnippets\YoutubeBomb\first_names.csv"

in_txt = csv.reader(open(txt_file, "r",encoding = "utf8"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'a+'))
out_txt = []
for row in in_txt:
    out_txt.append([
        "".join(a if ord(a) >=65 and ord(a) <= 122 else '' for a in i)
        for i in row])
out_csv.writerows(out_txt)
'''
import itertools

chars = "abcdef"
results = list(map(''.join, itertools.product(*zip(chars.upper(), chars.lower()))))

print(results)
