import os
import PyPDF2
#import pdfminer
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
#dir="/home/lohith/Desktop/EY Hackathon/EY_GDS_Project/data_to_preprocess"
dir="/home/soumi/Downloads/EYintentRepository"
def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))

    return r
###########################################################
#                        Loading Model                    #
###########################################################

bert_model_name="uncased_L-12_H-768_A-12"

bert_ckpt_dir = os.path.join("model/", bert_model_name)
bert_ckpt_file = os.path.join(bert_ckpt_dir, "bert_model.ckpt")
bert_config_file = os.path.join(bert_ckpt_dir, "bert_config.json")

model = create_model(data.max_seq_len, bert_ckpt_file)

csv_data=[]
file_loc=[]
intent=[]
sentence =[]
label=[]
file_names=[]
file_name=[]

final_output_csv_ey=[]

for filename in list_files(dir):
    print(filename)
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
            #intent.append(filename.split("/")[7])
            file_name.append(filename.split("/")[-1])

    if filename.endswith(".pdf"):
        
        #here we load trained model and get predictions on each sentence in test_data_from_crawler_pdf
        y_pred = model.predict(data.test_x).argmax(axis=-1)

    #sentences = ["we are studying for exam"]
    sentences= df["text"]
    pred_tokens = map(tokenizer.tokenize, sentences)
    pred_tokens = map(lambda tok: ["[CLS]"] + tok + ["[SEP]"], pred_tokens)
    pred_token_ids = list(map(tokenizer.convert_tokens_to_ids, pred_tokens))

    pred_token_ids = map(lambda tids: tids +[0]*(data.max_seq_len-len(tids)),pred_token_ids)
    pred_token_ids = np.array(list(pred_token_ids))

    predictions = model.predict(pred_token_ids).argmax(axis=-1)

    intents_we_came_across = set()
    for text, label in zip(sentences, predictions):
        print("text:", text, "\nintent:", classes[label])
        intents_we_came_across.append(classes[label])
        print()

df = pd.DataFrame(list(zip(file_loc, file_name, sentence , label)) , columns=["File Location", "File Name", "Sentence" , "Label"])
df.to_csv('test_data_from_crawler.csv',encoding='utf-8-sig', index=False)
    
