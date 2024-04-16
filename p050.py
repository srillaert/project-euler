from itertools import takewhile
from prime import get_is_prime_array

def get_next_prime(n, is_prime_array):
	result = n + 1
	while not is_prime_array[result]:
		result += 1
	return result

def get_consecutive_primes(prime, is_prime_array):
	while True:
		yield prime
		prime = get_next_prime(prime, is_prime_array)

def aggregate_consecutive_primes(start_prime, is_prime_array, till_sum):
	sum = 0
	count = 0
	for prime in get_consecutive_primes(start_prime, is_prime_array):
		sum += prime
		count += 1
		if sum >= till_sum:
			break
		yield count, sum

# Find the biggest prime less than 1 million that is the sum of the most consecutive primes
def get_solution(till_sum):
	is_prime_array = get_is_prime_array(till_sum)
	# the prime 5 is the sum of the 2 consecutive primes 2 and 3
	max_count = 2
	prime_sum = 5
	for start_prime in takewhile(lambda p: p <= (till_sum // max_count), get_consecutive_primes(2, is_prime_array)):
		for count, sum in aggregate_consecutive_primes(start_prime, is_prime_array, till_sum):
			if count > max_count and is_prime_array[sum]:
				max_count = count
				prime_sum = sum			
	return prime_sum

if __name__ == "__main__":
	solution = get_solution(1000000)
	print(solution)
