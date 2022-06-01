n=int(input())
b=int(input())
if(b>n):
    temp=b
    b=n
    n=temp
for i in range(n+1,1,-1):
    if(n%i==0 and b%i==0):
        print(i)
        break