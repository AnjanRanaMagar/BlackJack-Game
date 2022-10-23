
'''
Copied from https://towardsdatascience.com/merge-pdf-files-using-python-faaeafe4926c

One way of merging many PDF files would be to add the file names of every PDF files to a list manually and then perform
the same operation as in the previous section. But what if we have 100 PDF files in the folder? Using the os library we
can access all of the file names in a given directory as a list and iterate over it:
'''

from PyPDF2 import PdfFileMerger
import os

#Create an instance of PdfFileMerger() class
merger = PdfFileMerger()

#Define the path to the folder with the PDF files
path_to_files = r'Soka_Health_Clearance/'

#Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_files):
    #Iterate over the list of the file names
    for file_name in sorted(file_names):
        # sorting the file will make merge the list go as you like,
        # print(file_name)
        #Append PDF files
        merger.append(path_to_files + file_name)
#Write out the merged PDF file
merger.write("Soka_Health_Clearance.pdf")

merger.close()
