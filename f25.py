lst=[23,45,-4,89,0,56]
lst1=[]
lst2=[]
for i in lst:
    if(i<0):
        lst1.append(i)
    else:
        lst2.append(i)
print(lst1)
print(lst2)