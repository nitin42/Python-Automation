# Backup of folder into a zip file

# Copies the whole contents of any folder into a zip file whose filename increaments

# File format should be like this filename_number.zip (number should be increamented)

def backup(folder):
	# Backup the content of folder into a zip file

	folder = os.path.abspath(folder)

	number = 1

	while True:
		zip_name = os.path.basename(folder) + '_' + str(number) + '.zip'

		if not os.path.exists(zip_name):
			break
		number = number + 1

		print ("Creating file %s" %(zip_name))

		backupzip = zipfile.ZipFile(zip_name,'w')

		# Walking through the whole directory

		for foldername, subfolders, filenames in os.walk(folder):
			print ('Adding the file %s'%(foldername))
			backupzip.write(foldername)

		backupzip.close()

		print ('Succeeded')

		