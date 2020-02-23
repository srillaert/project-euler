import math

n = 0
divisors_count = 0
i = 1
while divisors_count <= 500:
    n += i
    i += 1
    divisors_count = 0
    sqrt_n = int(math.sqrt(n))
    for k in range(1, sqrt_n):
        if n%k == 0:
            divisors_count += 2
    if sqrt_n * sqrt_n == n:
        divisors_count += 1
print(n)
