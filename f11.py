lst=[1,2,3,4,5,6,7,8,9,23,67,32,67,30]
greatest=0
smallest=100
for i in lst:
    if(greatest<i):
        greatest=i
    if(smallest>i):
        smallest=i
print(greatest,smallest)