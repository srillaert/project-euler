# 'Simple' solution because based on the assumption that the terms have to increase by exact 3330, see also the discussion on https://www.mathblog.dk/project-euler-49-arithmetic-sequences-primes-permutations/
from prime_sieve import PrimeSieve

step = 3330
till = 10000
sieve = PrimeSieve(till)

for i in range(1001, till - 2 * step, 2):
	if sieve.is_prime(i) and sieve.is_prime(i+step) and sieve.is_prime(i+2*step):
		if sorted(str(i)) == sorted(str(i+step)) == sorted(str(i+2*step)):
			if i != 1487:
				print(str(i) + str(i+step) + str(i+2*step))
