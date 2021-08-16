import os
import shutil

folderPath = input("Enter the path of folder to be sorted : ")

list_of_files = os.listdir(folderPath)

for eachFile in list_of_files:
    name, ext = os.path.splitext(eachFile)
    ext = ext[1:]


    if ext == '':
        continue

#home/yash/project/sample.txt

    if os.path.exists(folderPath + '/' +ext):
        shutil.move(folderPath + '/' +eachFile, folderPath+'/'+ext +'/'+eachFile)

    else :
        os.makedirs(folderPath + '/' + ext)
        shutil.move(folderPath + '/' +eachFile, folderPath+'/'+ext +'/'+eachFile)

print("Task Accomplished")