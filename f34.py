lst=[67,34,23,8,45,23,8]
lst.sort()
oddsum=0
evensum=0
for i in lst:
    if(i%2==0):
        evensum+=i
    else:
        oddsum+=i
print(evensum)
print(oddsum)