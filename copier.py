import base64
import os
from codecutils import decodestring
srcpath =decodestring("VGhpcyBQQ1xPUFBPIEE1IDIwMjBcSW50ZXJuYWwgc2hhcmVkIHN0b3JhZ2Vcc2lkZXNsaWRlclxhbmRyb2lkXGFwcFxzcmNcZGVidWc=")
for root, dirs, files in os.walk(srcpath):
    for file in files:
        if file.endswith(".bat"):
             filename = os.path.join(root, file)
             print(filename)