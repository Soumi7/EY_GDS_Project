import sklearn
import pandas as pd

df = pd.read_csv("folders.csv")

train_df = df[:819]
test_df= df[819:1092]
valid_df = df[1092:]

train_df.to_csv('train.csv',encoding='utf-8-sig', index=False) 
test_df.to_csv('test.csv',encoding='utf-8-sig', index=False) 
valid_df.to_csv('valid.csv',encoding='utf-8-sig', index=False) 