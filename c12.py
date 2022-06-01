n= int(input())
temp=n
count=0
while(temp>0):
    count+=1
    temp=int(temp/10)
sum=0
temp=n
for i in range(count,0,-1):
    sum+=(n%10)**count
    count-=1
    n=int(n/10)
print(sum==temp)