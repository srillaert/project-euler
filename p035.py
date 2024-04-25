# Based on https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p035.py
from prime_sieve import PrimeSieve

def is_circular_prime(sieve, n):
	str_n = str(n)
	return all(sieve.is_prime(int(str_n[i:] + str_n[:i])) for i in range(len(str_n)))

def get_circular_prime_count(till):
	sieve = PrimeSieve(till)
	count = sum(1 for n in range(till) if is_circular_prime(sieve, n))
	return count

if __name__ == "__main__":
	solution = get_circular_prime_count(10**6)
	print(solution)
