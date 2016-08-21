import re
import string

def count_me():
	freq = {} # To store the word and its corresponding word count
	file_obj = open('count.txt', 'r')
	word_content = file_obj.read().lower() # Turn all the words in our document into lowercase.

	reg_exp = re.findall(r'\b[a-z]{3,15}\b', word_content)

	for word in reg_exp:
		count = freq.get(word, 0) # Count the frequency for a word present in our document.
		freq[word] = count + 1 # Increase the count for each word occurring more than once

	freq_list = freq.keys()

	for word in freq_list:
		print word, freq[word]


if __name__ == '__main__':
	count_me()
