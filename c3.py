a1=0
a2=1
n= int(input())
if(n==1):
    print(a1)
elif(n==2):
    print(a1)
    print(a2)
else:
    print(a1)
    print(a2)
    for i in range(3,n+1):
        sum=a1+a2
        a1=a2
        a2=sum
        print(sum)