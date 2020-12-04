import os

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            print(os.path.join(root, name))
            r.append(os.path.join(root, name))
            

    return r

print(list_files("/home/soumi/EY_GDS_Project"))