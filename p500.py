from functools import reduce
from prime_sieve import PrimeSieve

def get_factors(primes_till, exponent_of_2):
	sieve = PrimeSieve(primes_till)
	primes = list(sieve.get_primes())
	indexes = [0]
	for _ in range(exponent_of_2):
		min_index = min(range(len(indexes)), key=lambda i: primes[indexes[i]])
		yield primes[indexes[min_index]]
		primes[indexes[min_index]] = primes[indexes[min_index]] * primes[indexes[min_index]]
		if indexes[min_index] == 0:
			indexes.append(0)
		indexes[min_index] = indexes[min_index] + 1

def get_smallest_number_with_power_of_2_divisors(primes_till, exponent_of_2):
	result = reduce(lambda acc, num: (acc * num) % 500_500_507, get_factors(primes_till, exponent_of_2), 1)
	return result

if __name__ == "__main__":
	solution = get_smallest_number_with_power_of_2_divisors(8_000_000, 500_500)
	print(solution)