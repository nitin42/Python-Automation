# Regular expression search for .txt files

import re

import os

# Give any regular expression
regex = re.compile(r'')

# opening all .txt files present in current working directories

for filename in os.listdirs('.'):
	if filename.endswith('.txt'):
		print('Filname')
		file_object = open(filename,'r')
		a = regex.search(file_object.read())
		print a.group()

