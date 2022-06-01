def sumofdigit(temp):
    sum=0
    while(temp!=0):
        sum+=temp%10
        temp=int(temp/10)
    return sum
def checkno(n):
    sum=sumofdigit(n)
    temp=n%sum
    return(temp==0)

for i in range(1,101):
    if(checkno(i)==True):
        print(i)