# Renaming Files with American-Style date format to European-Style date format

# (MM-DD-YYYY) --> American-Style format

# (DD-MM-YYYY) --> European Style format

# Searching the filename in the current working directory for American-Style dates. 

import shutil 

import os 

import re

american_regex = re.compile(r'''^(.*?)   # Text before date
 	((0|1)?\d)-                          # month
 	((0|1|2|3)?\d)-                      # day
 	((19|20)\d\d)                        # four digit year
 	(.*?)$
 	''',re.VERBOSE)

# Looping over the current working directory for American Filenames

for american_file in os.listdir('.'):
	match1 = american_regex.search(american_file)

	# If file not found then don't break out of the loop
	if match1 == None:
		continue

	# Grouping the date format

	before_date = match1.group(1)
	month_part  = match1.group(2)
	day_part    = match1.group(4)
	year_part   = match1.group(6)
	after_part  = match1.group(8)

	# European-Style format

	european_file = before_date + day_part + '-' + month_part + '-' + year_part + after_part

	# Get the absolute path of both files

	absolute = os.path.abspath('.')
	american_file = os.path.join(absolute,american_file)
	european_file = os.path.join(absolute,european_file)

	# Renaming the file to European-Style format

	shutil.move(american_file,european_file)

