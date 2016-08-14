import requests

def take_input(text):
	normalized = str(text)
	obj = requests.get('http://isithackday.com/arrpi.php?text=' + normalized)
	if obj.text is not None:
		print obj.text
	else:
		print "Wrong input or something"

if __name__ == '__main__':
	take_input(raw_input())


	