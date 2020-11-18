import numpy as np
#import PyPDF2

'''
reader = PyPDF2.PdfFileReader("2020.04.10.20060681v2.full.pdf")

#print(reader.documentInfo)
print("Number of pages = {}".format(reader.numPages))

Text = []
for page in range(reader.numPages):
	Text.append(reader.getPage(page-1).extractText())

print(Text)
'''

'''
import PyPDF2
pdfFileObj = open('2020.04.10.20060681v2.full.pdf', 'rb') # reading in binary mode
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print("Number of pages = {}".format(pdfReader.numPages)) # number of pages

pageObj = pdfReader.getPage(1)
Text = pageObj.extractText()

print(Text)
'''


from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()

def PDF_to_TXT_regex(title):
	
	#print("\n\n ~~~~~~~~ \n\n ~~~~~~~~ \n\n")
	print("Title: {}".format(title))
	
	with open(title, 'rb') as in_file:
		parser = PDFParser(in_file)
		doc = PDFDocument(parser)
		rsrcmgr = PDFResourceManager()
		device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		for page in PDFPage.create_pages(doc):
			interpreter.process_page(page)

	#print(output_string.getvalue())

	import re 
	
	# Let us createa an empty array to append incubation periods that we find
	
	for sentence in output_string.getvalue().split(". "):
		if "incubation" in sentence:
			#print(sentence)
			#day = re.findall(r" \d{1.2} day", sentence)
			day = re.findall(r" ((\d{1,2}\.)?\d{1,2}) day[s]?", sentence)
			
			#day = re.findall(r" (\d{1,2}\.(\d{1,2})?) day[s]?", sentence)
			
			print(day)
			
			
			# let's print the numbers where we found them:
			if (len(day) >0):
				#print("\nDays: {}, Array length = {}".format(day, len(day)))
				#print("Corresponding sentence is:\n{}".format(sentence))
				incubations.append(float(day[0][0]) )
			else:
				pass 
				#print(day)
				
			
			'''
			# let's print now the numbers and their sentences 
			# only when there is 1 number found
			if len(day) == 1:
				print("\nday[0][0] = {}  day[s]".format(day[0][0]))
				print("\nSentence: {}".format(sentence))
			
				incubations.append(day)
			
			'''
			
			'''
			day2 = re.findall(r"(?:\d{1,2}\.)?\d{1,2}", sentence)
			#print(day2)
			
			day3 = re.findall(r"(\d{1,2}(\.\d{1,2})? day[s]?)", sentence)
			day3 = re.findall(r"(\d{1,2}(\.\d{1,2})?) day[s]?", sentence)
			#day3 = re.findall(r" \d{1,2}(\.\d{1,2})? day[s]?", sentence)
			#print(day3)
			
			if len(day2) == 1:
				print(day2[0])
				print(sentence)
			
			if len(day3) == 1:
				print("day3[0] = {}  day[s]".format(day3[0][0]))
				print("Sentence: {}".format(sentence))
				
				incubations.append(day3[0][0])
			'''
	#print("Incubation days from the paper:\n{}".format(incubations))
	print(incubations)
	print(sorted(incubations))
	import matplotlib.pyplot as plt
	
	bins = [0., 2., 4., 6., 8., 10., 12., 14., 16., 18., 20., 22., 24., 26., 28.]
	
	fig = plt.figure(figsize=[14,16])
	plt.rc('font', size=18)
	
	#plt.hist(sorted(incubations), bins=bins)
	plt.hist((incubations), bins=bins)
	
	plt.xlabel('Incubation period')
	plt.ylabel('Frequency/Probability')
	plt.title('Histogram of Coronavirus incubation periods')
	
	plt.show()
	plt.close()
	
titles = ['2020.03.10.20032136v1.full.pdf']#, '2020.04.10.20060681v2.full.pdf', '2020.05.24.20109215v2.full.pdf']

#titles = ['2020.05.24.20109215v2.full.pdf']

def PDF_to_TXT_regex2(title):
	
	#print("\n\n ~~~~~~~~ \n\n ~~~~~~~~ \n\n")
	print("Title: {}".format(title))
	
	with open(title, 'rb') as in_file:
		parser = PDFParser(in_file)
		doc = PDFDocument(parser)
		rsrcmgr = PDFResourceManager()
		device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		for page in PDFPage.create_pages(doc):
			interpreter.process_page(page)

	print(output_string.getvalue())


for title in titles:
	
	incubations = []
	
	PDF_to_TXT_regex(title)
