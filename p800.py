from prime_sieve import PrimeSieve
from math import log

def get_number_hybrid_integers(base, exponent):
	log_till = exponent * log(base)
	sieve_till = 16000000 # 800800 * log2(800800)
	sieve = PrimeSieve(sieve_till)
	primes = list(sieve.get_primes())
	count = 0
	for i in range(len(primes)):
		p = primes[i]
		if 2 * p * log(p) >= log_till:
			break
		# Use binary search to find the first prime q where p**q * q**p > base**exponent
		low, high = i + 1, len(primes)
		while low < high:
			mid = (low + high) // 2
			q = primes[mid]
			log_hybrid_integer = q * log(p) + p * log(q)
			if log_hybrid_integer > log_till + 1e-9:
				high = mid
			else:
				low = mid + 1
		count += low - (i + 1)
	return count

if __name__ == "__main__":
	solution = get_number_hybrid_integers(800800, 800800)
	print(solution)