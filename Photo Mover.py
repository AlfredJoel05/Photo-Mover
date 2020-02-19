from os import path , listdir ,mkdir
import shutil

source = 'C:/Users/Alfred Joel/Desktop/Client Folder'
raw_source = 'D:/Raw'
destination = 'D:/Temp/Test/PhotoMover'

for src_img in listdir(source):
    ext = path.splitext(src_img)[-1].lower()
    for raw_img in listdir(raw_source):  
        if ext == ".jpg" or ext == ".jpeg" or ext == '.png':
            if src_img == raw_img:
                new_source = path.abspath(path.join(raw_source, raw_img))
                shutil.copyfile(new_source,destination)
                break
        else:
            print("Files with Other-Extensions Found", ext) 



