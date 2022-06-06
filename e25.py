punc='!@#$%^&*()_-+={}[]:;"<.>?/'
newstr=""
n=input()
for i in n:
    if(i not in punc):
        newstr+=i
print(newstr)