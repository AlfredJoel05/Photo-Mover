from tkinter import *
from os import path , listdir ,mkdir
import shutil

root =Tk()
root.title("Photo Mover Version(1.0)")
root.geometry('640x480')

#_______________________photo mover Functioan__________________________
def PhotoMover():
    source=str(src.get())
    raw_source=str(rsrc.get())
    destination=str(dest.get())
    print(source,raw_source,destination)
    for src_img in listdir(source):
        ext = path.splitext(src_img)[-1].lower()
        for raw_img in listdir(raw_source):  
            if ext == ".jpg" or ext == ".jpeg" or ext == '.png':
                if src_img == raw_img:
                    new_source = path.abspath(path.join(raw_source, raw_img))
                    shutil.copy(new_source,destination)
                    break
            else:
                print("Files with Other-Extensions Found", ext) 

#____________________GUI_______________________
sourceLabel = Label(root, text="Client Path: ").grid(row=0, column=0, sticky=E)
rawLabel = Label(root, text="Raw Path: ").grid(row=1, column=0, sticky=E)
destLabel = Label(root, text="Destination Path: ").grid(row=2, column=0, sticky=E)

src=StringVar()
rsrc=StringVar()
dest=StringVar()

sourceLabel_entry = Entry(root, textvariable=src).grid(row=0, column=1)
rawLabel_entry = Entry(root, textvariable=rsrc).grid(row=1, column=1)
destLabel_entry = Entry(root, textvariable=dest).grid(row=2, column=1)

Move_button = Button(root, text="Copy", command=PhotoMover).grid(row=3, column=1, sticky=W)
  

root.mainloop()