import pandas as pd 
import numpy as np

df  = pd.read_csv("train.csv", encoding ="utf-8-sig")
df1 = pd.read_csv("folders.csv", encoding ="utf-8-sig")


print(df["intent"].value_counts())
print()
print(df1["Intent"].value_counts())

# print(len(df["File Name"].unique()))