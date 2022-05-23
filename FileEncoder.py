import os, os.path,base64
deleteOriginal =1
src_folder = input("directory to Search :") 
#src_folder = "E:\mydesi"
valid_exts = [".jpg",".gif",".png",".jpeg",'.m1v', '.mpeg', '.mov', '.mpa', '.mpg', '.mpe', '.avi', '.movie', '.mp4','.mkv']
for (dirpath, dirnames, filenames) in os.walk(src_folder):
    for file in filenames:
        filepath = os.path.join(dirpath, file)
        ext = os.path.splitext(file)[1]
        #encode files
        if ext.lower() in valid_exts:
            filenamewithext=os.path.basename(filepath)
            with open(filepath, "rb") as file:
                encoded_string = base64.b64encode(file.read())
                base64encfilename = base64.b64encode(filenamewithext.encode('utf-8', "ignore"))
                encodedfilepath=os.path.join(dirpath, base64encfilename.decode("utf-8")+".enc")
                print(encodedfilepath)
                print(base64encfilename.decode("utf-8"))
                with open(encodedfilepath, 'w+') as enc_file:
                    enc_file.write(str(encoded_string))
                    enc_file.close()
                    file.close()
                    if deleteOriginal == 1:
                        os.remove(filepath)