constant=0
x=input()
vowels=0
for i in x:
    if(i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels+=1
    elif((i>='A' and i<='Z') or (i>='a'and i<='z')):
        constant+=1
print(vowels)
print(constant)