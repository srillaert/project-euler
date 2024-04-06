# Based on https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p035.py
from prime import get_is_prime_array

def is_circular_prime(is_prime, n):
	str_n = str(n)
	return all(is_prime[int(str_n[i:] + str_n[:i])] for i in range(len(str_n)))

def get_circular_prime_count(till):
	is_prime = get_is_prime_array(till)
	count = sum(1 for n in range(till) if is_circular_prime(is_prime, n))
	return count

if __name__ == "__main__":
	solution = get_circular_prime_count(10**6)
	print(solution)
