import os 
import shutil

source=input("Enter your source folder  name")
destination=input("enter your destination folder")

source=source+'/'
destination=destination+'/'

files=os.listdir(source)
for file in files :
    shutil.copy((source+file),destination)
    