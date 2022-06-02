def fact(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
    return ans
sum=0
n=int(input())
temp=n
while(temp>0):
    sum+=fact(temp%10)
    temp=int(temp/10)
print(sum==n)