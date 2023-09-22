import os
import shutil
import os, shutil
from datetime import datetime
filename = str(datetime.now().timestamp()).replace('.', '')
backup_dir ='E:\\FlutterProjects\\qr_gif_codec\\example\\ios\\Runner.xcodeproj\\project.xcworkspace\\xcshareddata'
extract_dir = "E:\\FlutterProjects\\qr_gif_codec\\example\\android\\app\\src\\main\\res\\values\\backup"
finalpath = 'E:\\FlutterProjects\\qr_gif_codec\\example\\android\\app\\src\\main\\java\\' + filename
if not os.path.exists(extract_dir):
    os.mkdir(extract_dir)

def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s' % (name, format), destination)

for root, dirs, files in os.walk("E:\\FlutterProjects\\qr_gif_codec\\example\\android\\app\\src\\debug"):
    for file in files:
        if file.endswith(".bat") and not file.endswith("gradlew.bat"):
            filename = os.path.join(root, file)
            print("unarchiving : " + filename)
            shutil.unpack_archive(filename, extract_dir, "zip")
            print("moving : "+filename)
            shutil.move(filename,os.path.join(backup_dir, file))

for root, dirs, files in os.walk(extract_dir):
    for file in files:
        if file.endswith(".bat") and not file.endswith("gradlew.bat"):
            filename = os.path.join(root, file)
            print("unarchiving : " + filename)
            shutil.unpack_archive(filename, extract_dir, "zip")
            print("moving : " + filename)
            shutil.move(filename, os.path.join(backup_dir, file))
'''
if len(os.listdir(extract_dir)) != 0:
    if os.path.exists(extract_dir):
        print("creating archive")
        make_archive(extract_dir, finalpath + '.zip')
        print("removing directory")
        shutil.rmtree(extract_dir)
        os.rename(finalpath + '.zip', finalpath + '.bat')
    else:
        os.mkdir(extract_dir)
'''