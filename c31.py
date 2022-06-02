def fact( n):
    ans=1
    if(n==0):
        return 1
    for i in range(1,n+1):
        ans*=i
    return ans
def check_strong(n):
    temp=n
    sum=0
    while(n!=0):
        sum+=fact(n%10)
        n=n//10
    return(temp==sum)
for i in range(1,100):
    if(check_strong(i)):
        print(i)