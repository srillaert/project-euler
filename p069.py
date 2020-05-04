from itertools import count
from prime import is_prime

product = 1
for i in count(1):
    if is_prime(i):
        if product * i > 10**6:
            print(product)
            break
        else:
            product *= i