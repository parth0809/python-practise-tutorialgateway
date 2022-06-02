n=int(input())
nn=True
for i in range(2,n):
    if(n%i==0):
        nn=False
print(nn)