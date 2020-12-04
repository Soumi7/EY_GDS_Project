import pandas as pd 
import numpy as np

df  = pd.read_csv("folders.csv", encoding ="utf-8-sig")

print(df["Intent"].value_counts())

print(len(df["File Name"].unique()))