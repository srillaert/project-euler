from math import ceil, sqrt

def get_factors(n):
	till = ceil(sqrt(n))
	d = 2
	while d <= till:
		if n % d == 0:
			yield d
			while n % d == 0:
				n //= d
			till = ceil(sqrt(n))
		d += 1
	if n != 1:
		yield n

# Based on list_primality(n) of https://github.com/nayuki/Project-Euler-solutions/blob/master/python/eulerlib.py
def get_is_prime_array(till):
	# Sieve of Eratosthenes
	result = [True] * (till + 1)
	result[0] = result[1] = False
	for i in range(int(sqrt(till) + 1)):
		if result[i]:
			for j in range(i*i, till + 1, i):
				result[j] = False
	return result

def get_primes_from_is_prime_array(is_prime_array):
	yield 2
	for n in range(3, len(is_prime_array), 2):
		if is_prime_array[n]:
			yield n

def get_primes():
    yield 2
    yield 3
    n = 5
    while True:
        if is_prime(n):
            yield n
        if is_prime(n + 2):
            yield n + 2
        n += 6

def is_prime(n):
	if n == 2:
		return True
	if n%2 == 0:
		return False
	till = int(sqrt(n))
	for i in range(3, till+1, 2):
		if n%i == 0:
			return False
	return True
