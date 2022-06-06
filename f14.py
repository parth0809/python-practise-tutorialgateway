n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
mul=1
for x in lst:
    mul*=x
print(mul)