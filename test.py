import pandas as pd 
import numpy as np

df  = pd.read_csv("test.csv", encoding ="utf-8-sig")

print(df["intent"].value_counts())

# print(len(df["File Name"].unique()))