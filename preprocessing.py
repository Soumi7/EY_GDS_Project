import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import PyPDF2 as pdf

#extracting the blue color from the images using the max and min hsv values

csv_data=[]
directory="/home/soumi/dataset_intent"
for filename in os.listdir(directory):
    if filename.endswith(".jpg"): 
        file = open(os.path.join(directory, filename),'rb')
        pdf_reader = pdf.PdfFileReader(file)
        number_of_pages = read_pdf.getNumPages()
        pdf_content=""
        for page_number in range(number_of_pages):   # use xrange in Py2
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
            pdf_content+=page_content
           
        csv_data.append({"PDF_Name":filename,'text':pdf_content,'intent':""})
        
df = pd.DataFrame(csv_data, index=False)
df.to_csv('text_intent.csv') 
