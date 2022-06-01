n= int (input())
sum=0
temp=n
while(n>0):
    sum+=(n%10)**3
    n=n/10
    n=int(n)
print(temp==sum)