'''
Name: Anjan Rana Magar
Date: August 3rd, 2022
doc_to_txt.py :: python class to conver the .docx and .pdf file to .txt
                Advatages: easier to parse the document in .txt file than from other file format
'''

# Instruction:
# 1. you will need to install pypandoc and PyPDF2 for the project!
    # install PyPDF2: pip3 install PyPDF2
    # to install pypandoc (which converts the .docs to .txt: we use: pip install pypandoc

# 2. inorder to conver the file make sure your .docx and .pdf file are on same folder or directory.

import pypandoc
import PyPDF2

class Conversion_docx_To_txt:

    def __init__(self, docfile):
        self.docfile = docfile

    def docx_to_txtfile(self):
        '''return the .txt file by converting .docx file:
        convert_file: methods takes filename, 'type', and outputfile to write a file int txt format!'''

        output = pypandoc.convert_file(self.docfile , 'plain', outputfile= self.docfile[:-6]+".txt")
        return output

class Coversion_pdf_To_txt(Conversion_docx_To_txt):

    def __init__(self, docfile):
        super().__init__(docfile)

    def pdf_to_txtfile(self):

        '''convert the .pdf file and give .txt file'''

        #create file object variable
        # opening method will be rb (read bianry)
        # rb : Opens the file as read-only in binary format and starts reading from the beginning of the file.
        pdf_file_obj= open(self.docfile,'rb')

        #create reader variable that will read the pdffileobj
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        # print(pdf_reader)

        #This will store the number of pages of this pdf file
        x = pdf_reader.numPages

        #create a variable that will select the selected number of pages
        page_obj = pdf_reader.getPage(x-1)

        #(x+1) because python indentation starts with 0.
        #create text variable which will store all text datafrom pdf file
        text_file= page_obj.extractText()

        #save the extracted data from pdf to a txt file
        #we will use file handling here
        #dont forget to put r before you put the file path
        #go to the file location copy the path by right clicking on the file
        #click properties and copy the location path and paste it here.
        #put "\\your_txtfilename"

        file1= open(self.docfile[:-4]+"anj.txt","a")
        # file1.writelines(text_file)
        return file1.writelines(text_file)

