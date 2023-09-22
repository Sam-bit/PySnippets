import re
import requests
import os
import glob
import fileinput
for filename in glob.glob(os.path.join(os.path.dirname(os.path.realpath(__file__)), '*.json')):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace("\\n", " "), end='')
    print("Working on "+filename)
    import re
    linklist = []
    with open(filename) as fh: 
        for line in fh: 
            match = re.findall("(?s)(?<=https).+?(?= )", line) 
            for m in match:
                linklist.append(("https"+m).replace("\",",""))
    lstfile = open(filename+".lst","a+", encoding="utf-8")
    print("Writing to URL file")
    for line in linklist:
        lstfile.write(line+"\n")
    print("Removing duplicates from URL file")
    lines_seen = set() # holds lines already seen
    outfile = open('E:\\telegram-data\\'+filename+".lst", "w")
    infile = open('E:\\telegram-data\\'+filename+".lst", "r")
    alllines = outfile.read()
    firstcolumn = [row.split(",")[0] for row in infile]
    last_seen.add(firstcolumn)
    for line in infile:
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()