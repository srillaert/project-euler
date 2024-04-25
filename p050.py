from itertools import takewhile
from prime_sieve import PrimeSieve

def aggregate_consecutive_primes(primes, i):
	sum = 0
	count = 0
	for j in range(i, len(primes)):
		sum += primes[j]
		count += 1
		yield count, sum

# Find the biggest prime less than till_sum that is the sum of the most consecutive primes
def get_solution(till_sum):
	sieve = PrimeSieve(till_sum)
	primes = list(sieve.get_primes())
	# the prime 5 is the sum of the 2 consecutive primes 2 and 3
	max_count = 2
	prime_sum = 5
	for i in takewhile(lambda i: primes[i] < till_sum // max_count, range(len(primes))):
		for count, sum in takewhile(lambda t: t[1] < till_sum, aggregate_consecutive_primes(primes, i)):
			if count > max_count and sieve.is_prime(sum):
				max_count = count
				prime_sum = sum
	return prime_sum

if __name__ == "__main__":
	solution = get_solution(1000000)
	print(solution)
