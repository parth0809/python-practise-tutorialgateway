lst1=[1,2,3,4,5,6,7,8,9,10]
lst2=[2,4,6,8,10,12,14,16,18,20]
newlst=list(set(lst1)-set(lst2))+list(set(lst2)-set(lst1))
print(newlst)