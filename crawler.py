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

################################################################################
#                            Utility functions                                 #
################################################################################

def create_model(max_seq_len, bert_ckpt_file):

  with tf.io.gfile.GFile(bert_config_file, "r") as reader:
      bc = StockBertConfig.from_json_string(reader.read())
      bert_params = map_stock_config_to_params(bc)
      bert_params.adapter_size = None
      bert = BertModelLayer.from_params(bert_params, name="bert")
        
  input_ids = keras.layers.Input(shape=(max_seq_len, ), dtype='int32', name="input_ids")
  bert_output = bert(input_ids)

  print("bert shape", bert_output.shape)

  cls_out = keras.layers.Lambda(lambda seq: seq[:, 0, :])(bert_output)
  cls_out = keras.layers.Dropout(0.5)(cls_out)
  logits = keras.layers.Dense(units=768, activation="tanh")(cls_out)
  logits = keras.layers.Dropout(0.5)(logits)
  logits = keras.layers.Dense(units=len(classes), activation="softmax")(logits)

  model = keras.Model(inputs=input_ids, outputs=logits)
  model.build(input_shape=(None, max_seq_len))

  load_stock_weights(bert, bert_ckpt_file)
        
  return model

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
max_seq_len=128

model = create_model(max_seq_len, bert_ckpt_file)

csv_data=[]
file_loc=[]
intent=[]

label=[]
file_names=[]
file_name=[]

final_output_csv_ey=[]

for filename in list_files(dir):
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
        # print(type(output_string.getvalue()))
        # print(type(output_string))
        text=output_string.getvalue()
        data = sent_tokenize(text)
        for line in data:
            res=re.sub('\s+',' ',line)
            line=str(res)
            sentence.append(line)            
    
        #here we load trained model and get predictions on each sentence in test_data_from_crawler_pdf
        #y_pred = model.predict(data.test_x).argmax(axis=-1)

    #sentences = ["we are studying for exam"]
    
    pred_tokens = map(tokenizer.tokenize, sentence)
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

    for count in range(len(intents_we_came_across)):
        file_loc.append(filename)
        file_name.append(filename.split("/")[-1])
        intent.append(intents_we_came_across[count])
    

df = pd.DataFrame(list(zip(file_loc, file_name, intents_we_came_across)) , columns=["File Location", "File Name", "Intent"])
df.to_csv('test_data_from_crawler.csv',encoding='utf-8-sig', index=False)
    
