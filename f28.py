lst1=[]
lst2=[34,12,34,2,65,34]
for i in range(len(lst2)-1,-1,-1):
    lst1.append(lst2[i])
print(lst1)