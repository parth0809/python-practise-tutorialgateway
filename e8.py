x=input()
dict={}
for nums in x:
    keys=dict.keys()
    if(nums in keys):
        dict[nums]+=1
    else:
        dict[nums]=1
print(dict)