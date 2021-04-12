'''
# importing required modules 
import PyPDF2 
	
pdfFileObj = open('C:\\Users\\suneel\\Downloads\\The_PDF.pdf', 'rb') 

pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
	
print(pdfReader.numPages) 
	
pageObj = pdfReader.getPage(5)
	
print(pageObj.extractText()) 
	
pdfFileObj.close() 

'''
import PyPDF2
#Write a for-loop to open many files (leave a comment if you'd like to learn how).
filename = 'C:\\Users\\suneel\\Downloads\\ThePDF.pdf'
#open allows you to read the file.
pdfFileObj = open(filename,'rb')
#The pdfReader variable is a readable object that will be parsed.
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#Discerning the number of pages will allow us to parse through all the pages.
num_pages = pdfReader.numPages
print(num_pages)
count = 0
text = ""
#The while loop will read each page.
while count < num_pages:
    print(count)
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
    print(text)
#This if statement exists to check if the above library returned words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text.
else:
   text = textract.process(filename, method='tesseract', language='eng')
#Now we have a text variable that contains all the text derived from our PDF file. Type print(text) to see what it contains. It likely contains a lot of spaces, possibly junk such as '\n,' etc.
#Now, we will clean our text variable and return it as a list of keywords.
print(text)

