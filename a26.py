import math


print('a*x^2+b*x+c \n enter a,b,c')
a= int(input())
b= int(input())
c= int(input())
d=math.sqrt(b*b-4*a*c)
x1=(-b+d)/2
x2=(-b-d)/2
print (x1,'  ',x2)