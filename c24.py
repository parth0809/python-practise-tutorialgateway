def check_prime(n):
    nn=True
    for i in range(2,n):
        if(n%i==0):
            nn=False
    return(nn)#True for prime number
for i in range(1,101):
    if(check_prime(i)):
        print(i)