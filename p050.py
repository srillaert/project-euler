from itertools import takewhile
from prime import get_is_prime_array, get_primes_from_is_prime_array

def aggregate_consecutive_primes(primes, i):
	sum = 0
	count = 0
	for j in range(i, len(primes)):
		sum += primes[j]
		count += 1
		yield count, sum

# Find the biggest prime less than till_sum that is the sum of the most consecutive primes
def get_solution(till_sum):
	is_prime_array = get_is_prime_array(till_sum)
	primes = list(get_primes_from_is_prime_array(is_prime_array))
	# the prime 5 is the sum of the 2 consecutive primes 2 and 3
	max_count = 2
	prime_sum = 5
	for i in takewhile(lambda i: primes[i] <= till_sum // max_count, range(len(primes))):
		for count, sum in takewhile(lambda t: t[1] <= till_sum, aggregate_consecutive_primes(primes, i)):
			if count > max_count and is_prime_array[sum]:
				max_count = count
				prime_sum = sum
	return prime_sum

if __name__ == "__main__":
	solution = get_solution(1000000)
	print(solution)
