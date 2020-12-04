import sklearn
import pandas as pd
import numpy as np
from sklearn.utils import shuffle

df = pd.read_csv("folders.csv", encoding="utf-8-sig")

df =  df[["Sentence","Intent"]]

df = shuffle(df)

size =  len(df)

train_df = df[:int(np.round(size*.6, 0))]
test_df = df[int(np.round(size*.6, 0)) : int(np.round(size*.6, 0))+int(np.round(size*.2, 0))]
valid_df = df[int(np.round(size*.6, 0))+int(np.round(size*.2, 0)):]


train_df.to_csv('train.csv',encoding='utf-8-sig', index=False) 
test_df.to_csv('test.csv',encoding='utf-8-sig', index=False) 
valid_df.to_csv('valid.csv',encoding='utf-8-sig', index=False) 

# import re

# s = "2 3 4 5 lohith 34"

# s = re.sub(r"\d+\W+|\b\d+\b|\W+\d+", "", s)
# print(s)