from math import factorial
sum_digits = sum(int(c) for c in str(factorial(100)))
print(sum_digits)
