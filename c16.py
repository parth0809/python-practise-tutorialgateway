def sumofdigit(temp):
    sum=0
    while(temp!=0):
        sum+=temp%10
        temp=int(temp/10)
    return sum
n=int (input())
sum=sumofdigit(n)
temp=n%sum
print(temp==0)
