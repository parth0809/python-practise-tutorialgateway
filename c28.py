def check_prime(n):
    flag=True
    for i in range(2,n):
        if(n%i==0):
            flag=False
            break
    return flag
n=int(input())
for i in range(1,n+1):
    if(n%i==0):
        if(check_prime(i)):
            print(i)