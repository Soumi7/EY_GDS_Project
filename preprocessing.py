import os
import PyPDF2
import data_func
import csv
import pandas as pd

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
punctuation = punctuation + "\n"
stopwords = list(STOP_WORDS)
nlp = spacy.load("en_core_web_sm")


csv_data=[]
directory="/home/soumi/EY_GDS_Project/data_to_preprocess/"
for filename in os.listdir(directory):
    if filename.endswith(".pdf"): 
        file1 = open(os.path.join(directory, filename),'rb')
        print(file1)
        reader = PyPDF2.PdfFileReader(file1)
        print(reader.documentInfo)
        num_of_pages = reader.numPages
        writer = PyPDF2.PdfFileWriter()
        for page in range(0,num_of_pages):
            writer.addPage(reader.getPage(page))
        output_filename = 'data_to_preprocess/table_of_contents.pdf'
        with open(output_filename, 'wb') as output:
            writer.write(output)
        text = data_func.convert_pdf_to_string('./data_to_preprocess/table_of_contents.pdf')
        #text = data_func.convert_pdf_to_string(file1)
        text = text.replace('.','')
        text = text.replace('\x0c','')
        table_of_contents_raw = text.split('\n')
        print(table_of_contents_raw)
        print(text)
        sentences_list=text.split('.')
        s=0
        for sentence in sentences_list:
            csv_data.append({"PDF_Name":filename,'sentence_num': s,'text':sentence,'intent':filename[::-1]})
            s+=1
        
        
df = pd.DataFrame(csv_data)
df.to_csv('text_intent.csv') 

#ref : https://towardsdatascience.com/pdf-text-extraction-in-python-5b6ab9e92dd