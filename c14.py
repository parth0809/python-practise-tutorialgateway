n= int(input())
def digitsquare(i):
    sum=0
    while(i>0):
        sum+=(i%10)**2
        i=int(i/10)
    return sum
temp=n
while(temp!=1 and temp!=4):
    temp=digitsquare(temp)
if(temp==1):
    print(f'{n} is happy number')
else:
    print(f'{n} is not a happy number')