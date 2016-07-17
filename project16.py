# A UNIX password cracker 
# The following script uses SHA-512 hashing algorithm

import crypt

def test_password(crypted_password):
	salt = crypted_password[0:2]

	file_obj = open('dictionary.txt','r')
	for word in file_obj.readlines():
		word = word.split('\n')
		crypt_pass = crypt.crypt(word, salt)
		if crypt_pass == crypted_password:
			print('[+] Password found:' + word + '\n')
			return
	print('[-] Password not found')
	return

def main():
	file_obj = open('passwords.txt')
	for word in file_obj.readlines():
		if ":" in word:
			user = word.split(':')[0]
			crypt_word = word.split(':')[1].strip(' ') # strip off any white space
			print('[*] Cracking the UNIX password:'+ user)
			test_password(crypt_word)


if __name__ == '__main__':
	main()
