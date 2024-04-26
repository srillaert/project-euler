# 'Simple' solution because based on the assumption that the terms have to increase by exact 3330, see also the discussion on https://web.archive.org/web/20171231183448/http://www.mathblog.dk/project-euler-49-arithmetic-sequences-primes-permutations/
# From 'jepler' on https://projecteuler.net/thread=49#1672 :  '3330 has the property of leaving the low digit unchanged, and in a sense "rotating" the remaining digits.  Each of those other digits will increase by 3, except one which increases by 4 because of a carry operation.'
from prime_sieve import PrimeSieve

common_difference = 3330
till = 10000
sieve = PrimeSieve(till)

for i in range(1001, till - 2 * common_difference, 2):
	if sieve.is_prime(i) and sieve.is_prime(i+common_difference) and sieve.is_prime(i+2*common_difference):
		if sorted(str(i)) == sorted(str(i+common_difference)) == sorted(str(i+2*common_difference)):
			if i != 1487:
				print(str(i) + str(i+common_difference) + str(i+2*common_difference))
