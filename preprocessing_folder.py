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
import nltk
# nltk.download('punkt')

csv_data=[]
file_loc=[]
sentence =[]
label=[]
intent=[]
file_names=[]
file_name=[]
# directory="/home/lohith/Desktop/EY Hackathon/EY_GDS_Project/EY_DATA/"
dir="/home/lohith/Desktop/EY Hackathon/EY_GDS_Project/data_to_preprocess"
def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r
for i in list_files(dir):
    file_names.append(i)

# print(file_location)

for filename in file_names:
    # print(filename)
    if filename.endswith('.pdf'):
        output_string = StringIO()
        with open(filename, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams = LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
        # print(type(output_string.getvalue()))
        # print(type(output_string))
        text=output_string.getvalue()
        data = sent_tokenize(text)
        for line in data:
            res=re.sub('\s+',' ',line)
            line=str(res)
            file_loc.append(filename)
            sentence.append(line)
            label.append(0)
            intent.append(filename.split("/")[7])
            file_name.append(filename.split("/")[8])

    if filename.endswith(".pdf"):
        df = pd.DataFrame(list(zip(file_loc, file_name, sentence , label, intent)) , columns=["File Location", "File Name", "Sentence" , "Label", "Intent"])
        df.to_csv('folders.csv',encoding='utf-8-sig', index=False) 