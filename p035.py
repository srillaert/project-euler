# Based on https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p035.py
from prime import get_is_prime_array

till = 10**6
is_prime = get_is_prime_array(till)

def is_circular_prime(n):
	str_n = str(n)
	return all(is_prime[int(str_n[i:] + str_n[:i])] for i in range(len(str_n)))

result = sum(1 for n in range(till) if is_circular_prime(n))
print(result)
