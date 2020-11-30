import os
import PyPDF2
import data_func
import csv
import pandas as pd
from io import StringIO
import re
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from nltk.tokenize import sent_tokenize
import pandas as pd
import csv

csv_data=[]
file_names=[]
sentence =[]
label=[]
directory="/home/soumi/EY_GDS_Project/EY_DATA/"

for filename in os.listdir(directory):
    output_string = StringIO()
    with open(os.path.join(directory, filename), 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams = LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    print(type(output_string.getvalue()))
    print(type(output_string))
    text=output_string.getvalue()
    data = sent_tokenize(text)
    for line in data:
        res=re.sub('\s+',' ',line)
        line=str(res)
        file_names.append(filename)
        sentence.append(line)
        label.append(0)
        
#df = pd.DataFrame(csv_data)
df = pd.DataFrame(list(zip(file_names, sentence , label)) , columns=["Filename", "Sentence" , "Label"])
df.to_csv('text_intent.csv',encoding='utf-8-sig') 