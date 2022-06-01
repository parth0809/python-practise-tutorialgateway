def digitsquare(i):
        sum=0
        while(i>0):
            sum+=(i%10)**2
            i=int(i/10)
        return sum
def happyno(n):
    temp=n
    while(temp!=1 and temp!=4):
        temp=digitsquare(temp)
    if(temp==1):
        print(f'{n} is happy number')
for i in range(1,101):
    happyno(i)