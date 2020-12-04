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
import tensorflow as tf
from tensorflow import keras

import bert
from bert import BertModelLayer
from bert.loader import StockBertConfig, map_stock_config_to_params, load_stock_weights
from bert.tokenization.bert_tokenization import FullTokenizer

while True:
    n = input("Enter query")
    if n == "EXIT":
        print("Exiting")
        break
    sentence = [n]
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

    df = pd.read_csv("/content/test_data_from_crawler.csv", encoding = "utf-8-sig")
    for word in intents_we_came_across:
        for i in range(len(df['intent'])):
            if df['intent'][i]==word:
                print(df["File Name"][i])
                print(df["File Location"][i])
                print()
        