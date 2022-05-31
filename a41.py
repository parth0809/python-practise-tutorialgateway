a= int (input('units : '))
if(a<=100):
    sur=20
    bill=a*2.90
elif(a<=200):
    sur=30
    bill=a*4.20
elif(a<=400):
    sur=40
    bill=a*5.80
else:
    sur=50
    bill=a*6.55
print(f'bill={sur+bill}')