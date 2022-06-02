ss=input()
alpha=0
digit=0
special=0
for s in ss:
    if(s>='a' and s<='z' ) or(s>='A' and s<='Z'):
        alpha+=1
    elif(s>='0' and s<='9'):
        digit+=1
    elif((s>=chr(32) and s<=chr(47) )or (s>=chr(58) and s<=chr(64)) or (s>=chr(91) and s<=chr(96)) or(s>=chr(123) and s<=chr(126))):
        special+=1
print(alpha)
print(digit)
print(special)