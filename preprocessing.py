import os
import PyPDF2 as pdf
import pandas as pd


csv_data=[]
directory="/home/soumi/EY_GDS_Project/data_to_preprocess/"
for filename in os.listdir(directory):
    if filename.endswith(".pdf"): 
        file = open(os.path.join(directory, filename),'rb')
        read_pdf = pdf.PdfFileReader(file)
        number_of_pages = read_pdf.getNumPages()
        pdf_content=""
        for page_number in range(number_of_pages):   # use xrange in Py2
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
            pdf_content+=page_content
           
    csv_data.append({"PDF_Name":filename,'text':pdf_content,'intent':""})
        
df = pd.DataFrame(csv_data)
df.to_csv('text_intent.csv') 
