# mapit

import sys
import webbrowser
import pyperclip

#Get address from the command line argument
if len(sys.argv)>1:
	address = ' '.join(sys.argv[1:])
else:
	#Get address from the clipboard
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


