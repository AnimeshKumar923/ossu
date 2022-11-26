count = 0
sum = 0
print('Before', count, sum)
for value in [2,34,5,67,0,83,4]:
    count=count+1
    sum=sum+value
    print(count, sum, value)
print('After', count, sum, sum/count)