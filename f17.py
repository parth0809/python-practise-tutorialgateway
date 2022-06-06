lst=[23,45,89,0,56]
avg=sum(lst)/5
for i in range(len(lst)-1,-1,-1):
    if(lst[i]>avg):
        print(lst[i])