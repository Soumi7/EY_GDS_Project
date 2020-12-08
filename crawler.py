import os
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
import csv
import nltk
nltk.download('punkt')
import sklearn
import numpy as np
from sklearn.utils import shuffle

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            os.path.join(root, name)
            r.append(os.path.join(root, name))
            

    return r

dir="/content/drive/MyDrive/EY_DATA/data_to_preprocess/Company Details"

csv_data=[]
file_loc=[]
intent=[]

label=[]
file_names=[]
file_name=[]

for filename in list_files(dir):
    #printing file names
    print(filename)
    sentence =[]
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
        text=output_string.getvalue()
        data = sent_tokenize(text)
        for line in data:
            res=re.sub('\s+',' ',line)


            line=str(res)
            line = re.sub(r'[^\w\s]', '', line)
            line = re.sub(r'\b(?!(\D\S*|[12][0-9]{3})\b)\S+\b', '', line)
            line = line.strip()
            file_loc.append(filename)

            try:
                type(int(line)) != int
 
            except ValueError:
                if len(line) > 10:
                    line = line[:100]
                    sentence.append(line) 


    if filename.endswith('.pptx') :
        output_string = StringIO()
        with open(filename, 'rb') as in_file:
            prs = Presentation(in_file)
            content = ""
            slideCount = 0
            fullText = []
            for slide in prs.slides:
                slideCount += 1
                for shape in slide.shapes:
                    if (shape.has_text_frame):
                        for paragraph in shape.text_frame.paragraphs:
                            for run in paragraph.runs:
                                fullText.append(run.text)
            fullText='\n'.join(fullText)

        text=str(fullText)
        data = sent_tokenize(text)
        for line in data:
            res=re.sub('\s+',' ',line)
            line=str(res)

            line = re.sub(r'[^\w\s]', '', line)
            line = re.sub(r"\d+", "", line)
            # print(line)
            if len(line) != 0:
                file_loc.append(filename)
                try:
                    type(int(line)) != int

                except ValueError:
                    if len(line) > 10:
                        line = line[:100]
                        sentence.append(line)

            

    if filename.endswith('.docx'):
            output_string = StringIO()
            with open(filename, 'rb') as in_file:
                doc = docx.Document(in_file)
                fullText = []
                for para in doc.paragraphs:
                    fullText.append(para.text)
                fullText='\n'.join(fullText)

            text=str(fullText)
            data = sent_tokenize(text)
            for line in data:
                res=re.sub('\s+',' ',line)
                line=str(res)

                line = re.sub(r'[^\w\s]', '', line)
                line = re.sub(r"\d+", "", line)
                # print(line)
                if len(line) != 0:
                    file_loc.append(filename)
                    try:
                        type(int(line)) != int
    
                    except ValueError:
                        if len(line) > 10:
                            line = line[:100]
                            sentence.append(line)


        tokenizer = FullTokenizer(vocab_file= "vocab.txt")

        pred_tokens = map(tokenizer.tokenize, sentence)
        pred_tokens = map(lambda tok: ["[CLS]"] + tok + ["[SEP]"], pred_tokens)
        pred_token_ids = list(map(tokenizer.convert_tokens_to_ids, pred_tokens))

        max_seq_len=128

        pred_token_ids = map(lambda tids: tids +[0]*(max_seq_len-len(tids)),pred_token_ids)
        pred_token_ids = np.array(list(pred_token_ids))

         #################################################################
        #                 Taking predictions from model                 #
        #################################################################

        predictions = new_model.predict(pred_token_ids).argmax(axis=-1)

        intents_we_came_across = []

        for text, label in zip(sentence, predictions):
            if classes[label] not in intents_we_came_across:
                intents_we_came_across.append(classes[label])


        df_intents =  pd.DataFrame(intents_we_came_across)
        
        file_loc.append(filename)
        file_name.append(filename.split("/")[-1])
        intent = (df_intents[0].value_counts().keys().tolist())[0]
            

        df = pd.DataFrame(list(zip(file_loc, file_name, intent)) , columns=["File Location", "File Name", "Intent"])
        df.to_csv('test_data_from_crawler.csv',encoding='utf-8-sig', index=False)
