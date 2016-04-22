# Selective copy

'''Walking through a folder tree and searching for files with a certain file extension('.jpg','.pdf')
 and copying from whatever location they are present at to a new folder'''

 import shutil

 import os

 # Walking through a folder tree
 for folders,subfoldes,filenames in os.walk('/home/nitin'):
 	for filename in filenames:
 		if filename.endswith('.jpg') or filename.endswith('.pdf'):
 			shutil.copy(file_name,'/home/nitin/NEW_FOLDER')
 			