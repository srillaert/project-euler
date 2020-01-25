from math import *

number =  600851475143 # 13195
till = floor(sqrt(number))
n = 2
while n < till:
    while number % n == 0:
        number = int(number / n)
        till = floor(sqrt(number))
    n += 1
print(number)
