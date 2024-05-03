from itertools import count, groupby
from functools import reduce
from operator import mul

def trial_divisors():
	yield 2
	yield 3
	n = 5
	while True: # Odd numbers not divisible by 3
		yield n
		yield n + 2
		n += 6

def prime_factors(n):
	for d in trial_divisors():
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