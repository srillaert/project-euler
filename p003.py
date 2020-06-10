from math import ceil, sqrt

number =  600851475143 # 13195
till = ceil(sqrt(number))
n = 2
while n < till:
    while number % n == 0:
        number //= n
        till = ceil(sqrt(number))
    n += 1
print(number)
