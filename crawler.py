import os
dir="/home/soumi/Downloads/EYintentRepository"
def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r
for i in list_files(dir):
    print(i)