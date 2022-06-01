a=int(input())
even_sum=0
odd_sum=0
for i in range(1,a+1):
    if(i%2==1):
        odd_sum+=i
    else:
        even_sum+=i
print(even_sum)
print(odd_sum)