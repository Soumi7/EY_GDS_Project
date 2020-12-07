# dict1 = {}
from collections import defaultdict
list1 = ["lohith", "soumi", "lohith","swapnil","soumi"]

dict1 =  defaultdict(int) 
for names in list1:
    dict1[names] += 1

total_intents = sum(dict1.values()) 

final_list_of_intents = []


for intents in list(dict1.keys()):
    if (dict1[intents] / total_intents) >=  0.3:
        final_list_of_intents.append(intents)
    
# print(dict1["lohith"]/5)

print(final_list_of_intents)

# print( sum(dict1.values()))
# print(values)