from base64 import b64decode,b64encode
def decodestring(string):
    return b64decode(string).decode("utf-8")
def encodestring(string):
    return b64encode(bytes(string, 'utf-8')).decode("utf-8")
def encodelist(stringlist):
    res = []
    [res.append(encodestring(s)) for s in stringlist]
    return res
def decodelist(stringlist):
    res = []
    [res.append(decodestring(s)) for s in stringlist]
    return res