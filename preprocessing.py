import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import PyPDF2 as pdf

#extracting the blue color from the images using the max and min hsv values

csv_data=[]
directory="/home/soumi/dataset_intent"
for filename in os.listdir(directory):
    if filename.endswith(".jpg"): 
        file = open(os.path.join(directory, filename),'rb')
        
        csv_data.append({"IMG_NAME":filename,'area':area1,'count_of_cancerous_cells':counter1,'cancer_type':os.path.basename(os.path.normpath(directory))})
        if os.path.basename(os.path.normpath(directory))=="cancerous":
            k=1
        else:
            k=0
        csv_data.append({'area':area1,'count_of_cancerous_cells':counter1,'cancer_type':k})

df = pd.DataFrame(csv_data, index=False)
df.to_csv('non_cancerous.csv') 
