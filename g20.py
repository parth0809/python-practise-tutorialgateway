

tup=(0,1,2,3,4,5,6,7,8,9,10)
lst=list(tup)
lst.sort()
oddsum=0
evensum=0
for i in lst:
    if(i%2==1):
        print(i)