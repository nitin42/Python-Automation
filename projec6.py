# Regex search 

# Traversing all the .txt files in a folder and searching for any line that matches regex

# Printing the result

import os

import re

# Opening .txt file
file_open = open(filename,'r')

try:
	# User supplied regular expression
	regex_in = raw_input("Enter the regular expression")

	# Performing search initially 
	match = re.search(regex_in,filename)

	# If Regular expression search successful
	if match!=None:

		# Make a complete search throughout the whole file
		match_all = re.findall(regex_in,filename)

        # Print the result
		print "Result:" + str(match_all)

except IOError as e:
	print ("File requested doesn't exist. Try again!")


file_open.close()


