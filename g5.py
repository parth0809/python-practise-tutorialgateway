tup=(2,3,4,5,6,7,8,9,10,1,5)
item=int(input())
lst=list(tup)
lst.remove(item)
tup=tuple(lst)
print(tup)