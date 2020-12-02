import os
dir="/home/lohith/Desktop/EY Hackathon/EY_GDS_Project/data_to_preprocess"
def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r
for i in list_files(dir):
    print(i)