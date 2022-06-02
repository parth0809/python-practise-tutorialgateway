sum=0
n= int(input())
while(n!=0):
    sum+=n%10
    n=n//10
print(sum)