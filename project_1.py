#E-mail and phone number extractor

import pyperclip

import re

#Text containing email's and phone number to be pasted from clipboard
text = str(pyperclip.paste())

#Regular expression for phone numbers

phone_regex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?    # Non greedy approach for area code
	(\s|-|\.)?            # hypen or a dot (Phone number format) 
	(\d{3})               # first 3 digit
	(\s|-|\.)?            # seperator
	(\d{4})               # Last 4 digit
	)''', re.VERBOSE)

email_regex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+      # Username
	@                      # symbol
	[a-zA-Z0-9.-]+         # domain name
	(\.[a-z{2,4}])         # dot-something
	)''', re.VERBOSE)

match =[] # list for storing all the matched found

for groups in phone_regex.findall(text):
	phone_number = '-'.join([groups[1],groups[3],groups[5]])
	match.append(phone_number)

for groups in email_regex.findall(text):
	match.append(groups[0])

# Copy results to clipboard

if len(match)>0:
	pyperclip.copy('\n'.join(match))
	print ('Copied to clipboard')
	print ('\n'.join(match))
else:
	print ('Nothing found')




