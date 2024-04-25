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
