# First download the PyPDF2 library and import it
import PyPDF2
import sys
import os

# Create a PdfFileMerger object
merger = PyPDF2.PdfWriter()

# And make a loop to append all the pdf files in the CURRENT DIRECTORY. You must put the pdfs you want to merge in the same directory as the script
for pdf in os.listdir(os.curdir):
    if pdf.endswith(".pdf"):
        merger.append(pdf)

# Finally, write the merged pdf to a file. The file will be created in the current directory with the name "Combined_PDF.pdf"
merger.write("Combined_PDF.pdf") # You may change the name, but keep the ".pdf" extension
merger.close()