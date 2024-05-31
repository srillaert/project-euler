import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] # all the primes below 51

def get_prime_factors(n):
	factors = [0] * len(primes)
	for i in range(len(primes)):
		while (n % primes[i] == 0):
			factors[i] += 1
			n /= primes[i]
		if n == 1:
			break
	return factors

def get_factorial_factors(till_n):
	factorial_factors = [[]]
	for n in range(1, till_n):
		factorial_factors.append(get_prime_factors(n))
	
	for n in range(2, till_n):
		for i in range(len(primes)):
			factorial_factors[n][i] = factorial_factors[n][i] + factorial_factors[n-1][i]

	return factorial_factors

def is_square_free(factorial_factors, n, p):	
	factors = [a - b for a, b in zip(factorial_factors[n], factorial_factors[p])]
	factors = [a - b for a, b in zip(factors, factorial_factors[n-p])]
	return all(x < 2 for x in factors)

def get_solution(till_n):
	factorial_factors = get_factorial_factors(till_n)
	distinct_square_free = set()
	for n in range(2, till_n):
		for k in range(1, n):
			if is_square_free(factorial_factors, n, k):
				distinct_square_free.add(math.comb(n, k))
	return 1 + sum(distinct_square_free)

if __name__ == "__main__":
	solution = get_solution(51)
	print(solution)