import PyPDF2
import os

pdffile=["onePDF.pdf","TwoPDF.pdf","SamplePDF.pdf"]  # Name of all the PDF files that have to merge 
merger=PyPDF2.PdfMerger()   # Pdfmerger is a object class of a PyPDF2 library

for filename in pdffile:
                        pf=open(filename,'rb')
                        preader=PyPDF2.PdfReader(pf)
                        merger.append(preader)

pf.close()
merger.write("allMerged.pdf")  # Finally it will generate a merged PDF of all the PDF used 

#Requirement of this Merging PDF is needed in many project like some client want Merged PDF of two files. at that time it is necessary to give them 
#meged PDF of two PDF content.