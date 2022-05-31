a= int(input())
if(a%4==0):
    if(a%100==0):
        if(a%400==0):
            print('leap year')
        else :
            print('not a leap year')
    else:
        print('Leap Year')
else:
    print('Not a Leap Year')