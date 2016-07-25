# Let's have some fun

finput = raw_input("Enter the file name: ")
if finput:
	try:
		fopen = open(finput)
	except:
		print 'File cannot be read:', finput
		exit()
	count = 0 
	for line in fopen.read():
		count += 1

	print 'There were total ' + count + ' lines'

elif finput == 'na na boo boo or easter eggs':
	print 'NA NA BOO BOO TO YOU, you\'ve been punked ! LOL'

