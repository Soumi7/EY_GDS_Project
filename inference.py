import tensorflow as tf
import bert
from bert.tokenization.bert_tokenization import FullTokenizer
import numpy as np


new_model = tf.keras.models.load_model('/home/lohith/Desktop/EY Hackathon/EY_GDS_Project/saved_model/ey_model')

classes = ['Financial Reports', 'Case Study', 'Coding Guidelines']

while True:
    n = input("Enter query")
    if n == "EXIT":
        print("Exiting")
        break
    sentence = [n]

    tokenizer = FullTokenizer(vocab_file="vocab.txt")

    pred_tokens = map(tokenizer.tokenize, sentence)
    pred_tokens = map(lambda tok: ["[CLS]"] + tok + ["[SEP]"], pred_tokens)
    pred_token_ids = list(map(tokenizer.convert_tokens_to_ids, pred_tokens))
    
    max_seq_len=128

    pred_token_ids = map(lambda tids: tids +[0]*(max_seq_len-len(tids)),pred_token_ids)
    pred_token_ids = np.array(list(pred_token_ids))

    predictions = new_model.predict(pred_token_ids).argmax(axis=-1)

    intents_we_came_across = []
    for text, label in zip(sentence, predictions):
        print("text:", text, "\nintent:", classes[label])
        intents_we_came_across.append(classes[label])
        print()

    # for count in range(len(intents_we_came_across)):
    #     file_loc.append(filename)
    #     file_name.append(filename.split("/")[-1])
    #     intent.append(intents_we_came_across[count])
    
    # print(intent)