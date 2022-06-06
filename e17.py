n=(input('string : '))
z=input('char: ')
for i in range(len(n)-1,0,-1):
    if(z == n[i]):
        print(i+1)
        break