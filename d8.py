s=input()
if((s=='a')or(s=='e')or(s=='i')or(s=='o')or(s=='u')or(s=='A')or(s=='E')or(s=='I')or(s=='O')or(s=='U')) :
        print('vowels')
elif((s>='a' and s<='z')or (s>='A' and s <='Z')):
    print('consonent')
else:
    print('others')
