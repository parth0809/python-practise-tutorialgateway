def fact( n):
    ans=1
    if(n==0):
        return 1
    for i in range(1,n+1):
        ans*=i
    return ans
n=int(input())
temp=n
sum=0
while(n!=0):
    sum+=fact(n%10)
    n=n//10
print(temp==sum)