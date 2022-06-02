s=input()
if(s>='a' and s<='z' ) or(s>='A' and s<='Z'):
    print('alphabet')
elif(s>='0' and s<='9'):
    print('Digit')
elif((s>=chr(32) and s<=chr(47) )or (s>=chr(58) and s<=chr(64)) or (s>=chr(91) and s<=chr(96)) or(s>=chr(123) and s<=chr(126))):
    print('specialsymbol')
else:
    print('others')