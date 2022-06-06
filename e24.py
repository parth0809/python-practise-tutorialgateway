n= input()
z= input('char ')
str=''
for i in range(len(n)-1,-1,-1):
    if(n[i] ==z):
        str=n[0:i]+n[i+1:len(n)]
        break
print(str)