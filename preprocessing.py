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
        text = data_func.convert_pdf_to_string(file1)
        text = text.replace('.','')
        text = text.replace('\x0c','')
        table_of_contents_raw = text.split('\n')
        for item in table_of_contents_raw:
            title, pagenum = \
                data_func.split_to_title_and_pagenum(item)
        print(table_of_contents_raw)
        print(text)
        sentences_list=text.split('.')
        s=0
        for sentence in sentences_list:
            csv_data.append({"PDF_Name":filename,'sentence_num': s,'text':sentence,'intent':filename[::-1]})
            s+=1
        '''
        for page_number in range(number_of_pages):   # use xrange in Py2
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
            doc = nlp(page_content)
            doc = doc.replace('.','')
            doc = doc.replace('\x0c','')
            tokens = [token.text for token in doc]
            sentence_tokens = [sent for sent in doc.sents]
            #pdf_content+="".join(tokens)
            page_content+="".join(tokens)
           
            csv_data.append({"PDF_Name":filename,'page_text': page_content,'intent':""})
        '''
        
df = pd.DataFrame(csv_data)
df.to_csv('text_intent.csv') 
