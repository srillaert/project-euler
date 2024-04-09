import prime

def get_truncations(n):
	yield n
	d = 10
	while d <= n:
		yield n % d
		yield n // d
		d *= 10

def get_truncatable_primes():
	till = 1000000
	is_prime = prime.get_is_prime_array(till)
	for n in range(11, till, 2):
		if all(is_prime[m] for m in get_truncations(n)):
			yield n

if __name__ == "__main__":
	truncatable_primes = get_truncatable_primes()
	solution = sum(truncatable_primes)
	print(solution)
