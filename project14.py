# Deleting Unneeded Files

'''Walking through a folder tree and seaching for exceptionally large files or folders. 
Printing the files with their absolute path'''

import os

# Walking through a folder tree
for folders,subfolders,filenames in os.walk('/home/nitin'):
	for folder in folders:
		print 'The current folder is :' + folder
	for subfolder in subfolders:
		print 'The subfolder of' + folder + ':' + subfolder
	for filename in filenames:
		print 'The file inside' + subfolder + ':' + filename
		a = os.path.getsize(filename)

print ('The file size is ' + a )
print ('The file path is ' + os.path.abspath('./filename'))

