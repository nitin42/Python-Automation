# Command line argument Google search.

# This script uses requests,bs4,sys and webbrowser modules.

import requests

import sys

import webbrowser

import bs4

#Downloading Google page 
print ('Let me search')
a = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
a.raise_for_status()

# Retrieving top search results from Google using bs4

b = bs4.BeautifulSoup(a.text)

#Opening a tab for each result

#Finding all the <a> element that are present in CSS class r
c = b.select('.r a')
d = min(5, len(c))
for i in range(d):
	webbrowser.open('http://google.com' + c[i].get('href'))
	




