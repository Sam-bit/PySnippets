import os, os.path,base64
deleteOriginal =1
#src_folder = input("directory to Search :") 
src_folder = "E:\mydesi"
for (dirpath, dirnames, filenames) in os.walk(src_folder):
    for file in filenames:
        filepath = os.path.join(dirpath, file)
        ext = os.path.splitext(file)[1]
        #encode files
        if ext.lower() == ".enc":
            filenamewithoutext=os.path.basename(os.path.splitext(filepath)[0])
            base64decfilename = base64.b64decode(filenamewithoutext).decode('utf-8')
            with open(filepath, "rb") as file:
                decoded_string = base64.b64decode(file.read())
                decodedfilepath=os.path.join(dirpath, base64decfilename)
                with open(decodedfilepath, 'wb+') as dec_file:
                    dec_file.write(decoded_string)
                    dec_file.close()
                    file.close()
                    if deleteOriginal == 1:
                        os.remove(filepath)