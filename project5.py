# Mad libs 

# Reading text files and let user add their own text anywhere the word adjective,noun,verb or adverb appears

import os

word = ['adjective','adverb','noun','verb']

key =  []

# Listing all the '.txt' files present in current working directories
for filename in os.listdirs('.'):
	if filename.endswith('.txt'):
		file_object1 = open(filename,r)

		# Print the content of text files for easyness
		object2 = file_object1.read()
		print object2

# Loop through read object for searching the word and appending it with user input
for i in object2:
	if i in word:
		key.append(raw_input("Enter the {0}:".format(i)))
	else:
		key.append(i)

# Writing all the words to the file and saving it
file_object1 = open(filename,'w')
file_object1.write(''.join(key))
file_object1.close()



