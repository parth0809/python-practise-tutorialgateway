from asyncio.windows_events import NULL


lst=[23,45,'frsd',True,NULL]
for i in range(len(lst)-1,-1,-1):
    print(lst[i])