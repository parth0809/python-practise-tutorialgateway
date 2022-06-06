tup=(0,1,2,3,4,5,6,7,8,9,10)
lst=list(tup)
lst.sort()
sum=0
for i in lst:
    sum+=i
print(sum)