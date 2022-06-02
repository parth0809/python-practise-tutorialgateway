def check_pronic(n):
    flag=False
    for i in range(1,n+1):
        if(i*(i+1)==n):
            flag=True
            break
    return(flag)
for i in range(1,101):
    if(check_pronic(i)):
        print(i)