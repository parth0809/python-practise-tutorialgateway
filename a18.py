a= int(input('c p'))
b= int(input('sp'))
if(b>a):
    print(f'profit with {b-a}')
elif(b<a):
    print(f'loss with {a-b}')
else:
    print('sp = cp')