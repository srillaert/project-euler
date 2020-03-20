from prime import is_prime
import itertools

def number_quadratic_primes(a, b):
	for n in itertools.count():
		r = n*n + a*n + b
		if not is_prime(abs(r)):
			return n

till = 1000
max_a = 0
max_b = 0
max_number_primes = 0
for b in range(-till+1, till):
	if is_prime(abs(b)):
		for a in range(-till+1, till):
			n = number_quadratic_primes(a, b)
			if n > max_number_primes:
				max_a = a
				max_b = b
				max_number_primes = n

result = max_a * max_b
print(result)
