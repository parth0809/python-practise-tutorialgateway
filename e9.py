count=0
x=input()
for i in x:
    if((i>='A' and i<='Z')or(i>='a'and i<='z')):
        print(i)
        count+=1
print(count)