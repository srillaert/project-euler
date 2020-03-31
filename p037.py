import prime

def get_truncations(n):
	yield n
	d = 10
	while d <= n:
		yield n % d
		yield n // d
		d *= 10

till = 1000000
is_prime = prime.get_is_prime_array(till)
result = sum(n for n in range(11, till, 2) if all(is_prime[m] for m in get_truncations(n)))
print(result)
