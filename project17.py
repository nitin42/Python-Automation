# ZIP password cracker

# This script iterates through a user provided dictionary and finds the password for the encrypted 

import zipfile

'''
zipfile has a method call extractall().
extractall(self, path=None, members=None, pwd=None)
    Extract all members from the archive to the current working
    directory. `path' specifies a different directory to extract to.
    `members' is optional and must be a subset of the list returned
    by namelist().
'''

def test_pass(zipfile, password):
	try:
		zipfile.extractall(password)
		return password
	except Exception as ex:
		print("An error occured "%(ex))
		return

def main():
	zip_obj = zipfile.ZipFile('''Use zip file you want to crack''')
	filepass = open('dictionary.txt')
	for word in filepass.readlines():
		password = word.split('\n')
		guess_password = test_pass(zip_obj, password)
		if guess_password:
			print("[+] Password found:" + password + "\n")
			exit(0)

if __name__ == '__main__':
	main()
