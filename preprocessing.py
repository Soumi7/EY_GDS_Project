import os
import cv2 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from skimage.morphology import convex_hull_image
from skimage import morphology

#defining the kernel size for morphological operations
kernel = np.array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=np.uint8)

#extracting the blue color from the images using the max and min hsv values
cell_hsvmax  = (140,255,255)
cell_hsvmin  = (100,100,80)  
csv_data=[]
directory="/home/lohith/Documents/CS-3rd Year -Projects/3rd_Year_project/Negative for Intraepithelial malignancy"
for filename in os.listdir(directory):
    if filename.endswith(".jpg"): 
        # print(os.path.join(directory, filename))
        image = cv2.imread(os.path.join(directory, filename))
        image_copy =  image.copy()
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV) 
        color_thresh = cv2.inRange(hsv, cell_hsvmin, cell_hsvmax)
        opening = cv2.morphologyEx(color_thresh, cv2.MORPH_OPEN, kernel, iterations =5)
        processed1 = morphology.remove_small_objects(opening.astype(bool), min_size=1500, connectivity=0.01).astype(int)
        u1 = processed1.astype(np.uint8)
        contours, hierarchy = cv2.findContours(u1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        area1 = 0
        counter1 = 0
        for i in range(len(contours)):
            area1 += cv2.contourArea(contours[i])
            if cv2.contourArea(contours[i]) > 1000:
                counter1 += 1
        csv_data.append({"IMG_NAME":filename,'area':area1,'count_of_cancerous_cells':counter1,'cancer_type':os.path.basename(os.path.normpath(directory))})
        if os.path.basename(os.path.normpath(directory))=="cancerous":
            k=1
        else:
            k=0
        csv_data.append({'area':area1,'count_of_cancerous_cells':counter1,'cancer_type':k})

df = pd.DataFrame(csv_data, index=False)
df.to_csv('non_cancerous.csv') 
