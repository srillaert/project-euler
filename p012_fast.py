from cached_trial_division import CachedTrialDivision
from functools import reduce
from itertools import count, groupby
from math import floor, sqrt
from operator import mul

cache = CachedTrialDivision()

def prime_factors(n):
	square_root = floor(sqrt(n))
	for d in cache.get_primes(square_root):
		if d*d > n:
			break
		while n%d == 0:
			yield d
			n //= d
	if n != 1:
		yield n

def prime_factor_exponents(n):
	return (sum(1 for _ in group) for _, group in groupby(prime_factors(n)))

def number_of_divisors(n):
    return reduce(mul, (e + 1 for e in prime_factor_exponents(n)), 1)

def get_triangle_numbers():
    tn = 1
    for step in count(2):
          yield tn
          tn += step

def get_solution(minimum_number_of_divisors):
    return next(tn for tn in get_triangle_numbers() if number_of_divisors(tn) >= minimum_number_of_divisors)

if __name__ == "__main__":
    solution = get_solution(500)
    print(solution)