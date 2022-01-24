import os
import shutil
path=input("enter file name")
filenames=os.listdir(path)
for file in filenames:
    root,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext==" ":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)