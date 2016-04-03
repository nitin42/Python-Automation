# Combining selected pages from different PDFs using PyPDF2 module 

# Combining all PDFS in cwd into a single PDF

# Review of PyPDF2

# --> pdf_file_object = open(filename,mode)
# --> pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)
# --> pdf_reader.numPages
# --> page_Object = pdf_reader.getPage(0)
# --> page_Object.extractText()

# Review of copy pdf files using PyPDF2

# --> file1 = open()
# --> file2 = open()
# --> read1 = PyPDF2.PdfFileReader(file1)
# --> read2 = PyPDF2.PdfFileReader(file2)
# --> Pdf_writer = PyPDF2.PdfFileWriter()
# --> Loop through read1 object's each page, get the page(page_object) and add using Pdf_writer.add(page_object)

# Review of saving pdf files into new pdf

# output_file = open(new_file,'wb')
# Pdf_writer.write(output_file)
# output_file.close()

import os

import PyPDF2

pdffile =[]

for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdffile.append(filename)

pdffile.sort()

pdf_write = PyPDF2.PdfFileWriter()

for filename in pdffile:
	obj = open(filename,'rb')
	read = PyPDF2.PdfFileWriter(obj)
	for pgn in range(1,read.numPages):
		pgo = read.getPage(pgn)
		pdf_write.addPage(pgo)

output_file = open(filename,'wb')
pdf_write.write(output_file)
output_file.close()



