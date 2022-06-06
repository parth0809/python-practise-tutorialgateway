lst=[1,2,3,4,5,6,7,-8,9,23,67,32,-670,-30]
cnteven=0
cntodd=0
for i in lst:
    if(i<0):
        cntodd+=1
    else:
        cnteven+=1
print(cnteven, cntodd)