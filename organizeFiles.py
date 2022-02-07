from msilib.schema import File
import os
import shutil

FilePath=input("enter a directory name ")
fileList=os.listdir(FilePath)

for file in fileList:
    name,ext=os.path.splitext(file)
    ext=ext[1:]

    if(ext==""):
        continue
    
    if os.path.exists(FilePath+'/'+ext):
        shutil.move(FilePath+'/'+file,FilePath+'/'+ext+'/'+file)
    
    else:
        os.makedirs(FilePath+'/'+ext)
        shutil.move(FilePath+'/'+file,FilePath+'/'+ext+'/'+file)
    print("The folder has been organized")
