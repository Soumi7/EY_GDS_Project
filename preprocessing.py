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
        for page_number in range(number_of_pages):   # use xrange in Py2
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
            text_file.write(page_content)
           
        csv_data.append({"IMG_NAME":filename,'area':area1,'count_of_cancerous_cells':counter1,'cancer_type':os.path.basename(os.path.normpath(directory))})
        

df = pd.DataFrame(csv_data, index=False)
df.to_csv('text_intent.csv') 
