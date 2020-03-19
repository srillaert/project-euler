from prime import is_prime

def number_quadratic_primes(a, b):
	n = 0
	while True:
		r = n*n + a*n + b
		if not is_prime(abs(r)):
			break
		n += 1
	return n

max_a = 0
max_b = 0
max_number_primes = 0
for b in range(-999, 1000):
	if is_prime(abs(b)):
		for a in range(-999, 1000):
			n = number_quadratic_primes(a, b)
			if n > max_number_primes:
				max_a = a
				max_b = b
				max_number_primes = n

result = max_a * max_b
print(result)
