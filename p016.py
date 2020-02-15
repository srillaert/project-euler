number = 2
for i in range(1,1000):
    number *= 2
sum = 0
while(number > 0):
    sum += (number % 10)
    number //= 10
print(sum)
