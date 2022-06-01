a1=0
a2=1
sum=0
n= int(input())
if(n==1):
    sum=a1
elif(n==2):
    sum=a1+a2
else:
    sum=a1+a2
    for i in range(3,n+1):
        sum1=a1+a2
        a1=a2
        a2=sum1
        sum+=sum1
print(sum)