def checkpalindrome(n):
    count=0
    temp=n
    while(temp!=0):
        count+=1
        temp=temp//10
    temp=n
    sum=0
    while(temp!=0):
        count-=1
        sum+=(temp%10)*10**(count)
        temp=temp//10
    return(sum==n)
for i in range(1,101):
    if(checkpalindrome(i)):
        print(i)