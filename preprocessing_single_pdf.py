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
nltk.download('punkt')
output_string = StringIO()
with open('/home/lohith/Desktop/EY Hackathon/EY_GDS_Project/data_to_preprocess/CaseStudy_SDC.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

# print(type(output_string.getvalue()))
# print(type(output_string))
text=output_string.getvalue()
data = sent_tokenize(text)


sentence =[]
label=[]
for line in data:
	res=re.sub('\s+',' ',line)
	line=str(res)
#	line = line.encode()
	sentence.append(line)
	label.append(0)

df = pd.DataFrame(list(zip(sentence , label)) , columns=["Sentence" , "Label"])

df.to_csv("file.csv",encoding='utf-8-sig', index=False)