x=input()
cnt=0
for i in x:
    if(i==' '):
        cnt+=1
if(x!=''):
    print(cnt+1)
else:
    print(0)