# Brute-Force PDF Password Breaker

# Brute-Forcing the pdf files to break the encryption using dictionary attack

import os

import PyPDF2

# Opening the dictionary file that contains all the possible combinations of words
read_file = open('dictionary.txt')
file_content = read_file.read()

# Making a list of word strings by reading this file
wordlist = file_content.split('\n')

# Using PyPDF2 module to read pdf files
pdfreader = PyPDF2.PdfFileReader(open('pdf_file','rb'))

# Checking whether the file is encrypted or not
try:
	if pdfreader.isEncrypted == True:
		for word in wordlist:
			pdfreader.decrypt(word)
			if (decrypt()): return 1
			elif not (decrypt()): return 0
	else:

		# If the file is not encrypted then simply open the file
		pdfreader.numPages


