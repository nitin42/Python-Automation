# Multiclipboard 

#Usage is in the form of commmand line argument

#file name save <keyword> - saves clipboard to keyword

#file name <keyword> - loads keyword content to clipboard

#file name list - copies list of all keywords to clipboard

#We are using shelve module which saves variables in our python program to binary shelf files

import pyperclip

import sys

import shelve

#For saving and loading the text in the shelve file.
a = shelve.open('mcb')

#Saving clipboard content to the keyword

if len(sys.argv)==3 and sys.argv[1].lower()=='save':
	a[sys.argv[2]] == pyperclip.paste()
elif len(sys.argv)==2:
	# List keywords and load content
	if sys.argv[1]=='list':
		pyperclip.copy(str(list(a.keys())))
	elif sys.argv[1] in a:
		pyperclip.copy(a[sys.argv[1]])

a.close()





