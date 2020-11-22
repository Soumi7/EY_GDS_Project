import os
import PyPDF2 as pdf
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
        file = open(os.path.join(directory, filename),'rb')
        print(file)
        read_pdf = pdf.PdfFileReader(file)
        number_of_pages = read_pdf.getNumPages()
        pdf_content=""
        for page_number in range(number_of_pages):   # use xrange in Py2
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
            doc = nlp(page_content)
            tokens = [token.text for token in doc]
            #sentence_tokens = [sent for sent in doc.sents]
            pdf_content+="".join(tokens)
           
    csv_data.append({"PDF_Name":filename,'text':pdf_content,'intent':""})
        
df = pd.DataFrame(csv_data)
df.to_csv('text_intent.csv') 
