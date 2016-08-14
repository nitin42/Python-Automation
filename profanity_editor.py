import requests

def profanity():
	file_obj = open('movies.txt', 'r')
	content = file_obj.read()
	# print content
	file_obj.close()
	check_profanity(content)

def check_profanity(text):
	obj = requests.get('http://www.wdylike.appspot.com/?q=' + str(text))
	if 'true' in obj.text:
		print "Profanity alert! Check your document"
	elif 'false' in obj.text:
		print "No curse words found"
	else:
		print "Unable to scan the document"


if __name__ == '__main__':
	profanity()