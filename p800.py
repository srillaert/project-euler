from prime_sieve import PrimeSieve
from math import log10

def get_number_hybrid_integers(base, exponent):
	log_till = exponent * log10(base)
	sieve_till = 16000000 # 800800 * log2(800800)
	sieve = PrimeSieve(sieve_till)
	primes = list(sieve.get_primes())
	count = 0;
	for i in range(len(primes)):
		p = primes[i]
		if 2 * p * log10(p) >= log_till:
			break
		for j in range(i+1, len(primes)):
			q = primes[j]
			log_hybrid_integer = q * log10(p) + p * log10(q)
			if log_hybrid_integer - log_till > 1e-9:
				count = count + j - i - 1
				break
	return count

if __name__ == "__main__":
	solution = get_number_hybrid_integers(800800, 800800)
	print(solution)