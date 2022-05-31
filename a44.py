import datetime
t=datetime.datetime.now()
print('current date and time = ',t)
d=t.strftime('%B %D %Y %H :%M: %S')
print(d)