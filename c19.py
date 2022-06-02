n=int(input())
squ=n**2
sum=0
while(squ>0):
    sum+=squ%10
    squ=int(squ/10)
print(sum==n)