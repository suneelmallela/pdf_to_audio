from tika import parser # pip install tika
from PyPDF2 import PdfFileWriter, PdfFileReader
from gtts import gTTS 
import os


def pdf_to_text(pdffile):
    raw = parser.from_file(pdffile)
    return raw['content']


def text_to_audio(text_file):
    audio_file = text_file.replace('text_pages', 'audio_files').replace('.txt', '.mp3')
    print(audio_file)
    f = open(text_file, "r")
    mytext = f.read()
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(audio_file)


def pdf_to_audio(folder, pdf_file):
    file_name = folder + pdf_file
    print(file_name)
    inputpdf = PdfFileReader(open(file_name, "rb"))
    for i in range(87, inputpdf.numPages):
        print(i)
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        
        output_pdf_file_name = folder + 'pdf_pages\\' + 'page_{}.pdf'.format(i+1)
        print(output_pdf_file_name)

        with open(output_pdf_file_name, "wb") as outputStream:
            output.write(outputStream)

        output_text_file_name = output_pdf_file_name.replace('pdf_pages', 'text_pages').replace('.pdf', '.txt')
        print(output_text_file_name)

        text = pdf_to_text(output_pdf_file_name)
        
        with open(output_text_file_name, "w") as text_file:
            text_file.write(text)

        text_to_audio(output_text_file_name)
        

folder = 'C:\\Users\\suneel\\Documents\\Python\\ThePDF\\'
pdf_file = 'ThePDF.pdf'
pdf_to_audio(folder,  pdf_file)
